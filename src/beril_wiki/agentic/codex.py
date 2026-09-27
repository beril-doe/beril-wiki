"""Codex app-server backend: GPT models through the same tools, ledger and budgets.

The Claude branch lives in Runtime._query and must not change (its source is part
of the planning cache key), so everything Codex-specific lives here and Runtime.ask
dispatches on the model name."""

from __future__ import annotations

import ast
import atexit
import json
import os
import threading
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any

from beril_wiki.agentic.runtime import (
    SYSTEM,
    EvidenceTools,
    ReadTools,
    Runtime,
    WorkflowError,
    digest,
    tool_profile,
)

EFFORT = "high"
REVISION = digest([ast.dump(ast.parse(Path(__file__).read_text())), EFFORT])
ENV_PREFIXES = ("OPENAI_", "ANTHROPIC_", "CLAUDE_")
# Verified accepted by `codex exec --strict-config` on CLI 0.157.1.
OVERRIDES = (
    'forced_login_method="chatgpt"',
    'model_provider="openai"',
    "features.shell_tool=false",
    "features.memories=false",
    'web_search="disabled"',
    'approval_policy="never"',
    "notify=[]",
    # Under a never-ask policy an MCP call is denied unless its tool is pre-approved.
    'mcp_servers.evidence.tools.read_evidence.approval_mode="approve"',
    'mcp_servers.evidence.tools.search_evidence.approval_mode="approve"',
    'mcp_servers.evidence.tools.validate_candidate.approval_mode="approve"',
)
PROFILE_SENTENCE = {
    "none": "All evidence is supplied in the prompt; there are no tools.",
    "read": "Use only the supplied evidence read tool.",
    "extended": "Use only the supplied read-only evidence, search and candidate-check tools.",
}
TRANSCRIPT_LIMIT = 4_000_000


def map_usage(usage: Any) -> dict | None:
    """One fresh thread per job, so the thread total is the job's usage; reasoning
    tokens are already inside output_tokens."""
    if usage is None:
        return None
    t = usage.total
    return {
        "input_tokens": max(0, t.input_tokens - t.cached_input_tokens),
        "output_tokens": t.output_tokens,
        "cache_creation_input_tokens": t.cache_write_input_tokens or 0,
        "cache_read_input_tokens": t.cached_input_tokens,
    }


def final_response(items: list) -> str:
    """The final-answer agent message, else the last unphased one, else empty."""
    fallback = ""
    for item in reversed(items):
        root = getattr(item, "root", item)
        if getattr(root, "type", None) != "agentMessage":
            continue
        phase = getattr(root, "phase", None)
        phase = getattr(phase, "value", phase)
        if phase == "final_answer":
            return root.text or ""
        if phase is None and not fallback:
            fallback = root.text or ""
    return fallback


class Binding:
    """What the host serves for the job in flight: reader, allowed tools, validator,
    remaining tool turns."""

    def __init__(
        self,
        reader: ReadTools,
        tools: list[str],
        validator: Callable[[str], Any] | None,
        turns: int,
    ) -> None:
        self.reader, self.tools, self.validator, self.turns = reader, tools, validator, turns
        self.overrun = False


class EvidenceHost:
    """The pipeline's evidence tools served over local streamable HTTP for Codex.

    Tool names, argument shapes and reply text match the Claude branch so prompts
    and validators are shared. The host holds no reader itself: run_job binds one
    per job and clears it afterwards."""

    def __init__(self) -> None:
        import uvicorn
        from mcp.server.fastmcp import FastMCP
        from mcp.types import ToolAnnotations

        self.binding: Binding | None = None
        mcp = FastMCP("evidence", stateless_http=True)
        read_only = ToolAnnotations(readOnlyHint=True)
        mcp.tool(
            name="read_evidence",
            annotations=read_only,
            description="Read an exact character range from a snapshot file. Paths are "
            "relative to the snapshot root: staging/<project>__REPORT.md or "
            "staging/discoveries.md for source reports; wiki/<collection>/<page>.md for "
            "pages, such as wiki/concepts/<stem>.md or wiki/summaries/<project>__REPORT.md. "
            "Ranges past the end are clamped; the reply reports the length.",
        )(self._read)
        mcp.tool(
            name="search_evidence",
            annotations=read_only,
            description="Search literal text in wiki or staging; paginate with next_offset.",
        )(self._search)
        mcp.tool(
            name="validate_candidate",
            annotations=read_only,
            description="Check a candidate JSON string against the bound page task; no writes.",
        )(self._validate)
        config = uvicorn.Config(
            mcp.streamable_http_app(), host="127.0.0.1", port=0, log_level="warning"
        )
        self.server = uvicorn.Server(config)
        threading.Thread(target=self.server.run, daemon=True, name="evidence-host").start()
        deadline = time.monotonic() + 15
        while not self.server.started:
            if time.monotonic() > deadline:
                raise WorkflowError("evidence host did not start")
            time.sleep(0.05)
        self.port = self.server.servers[0].sockets[0].getsockname()[1]

    @property
    def url(self) -> str:
        return f"http://127.0.0.1:{self.port}/mcp"

    def close(self) -> None:
        self.server.should_exit = True

    def _bound(self, name: str) -> Binding:
        bound = self.binding
        if bound is None:
            raise WorkflowError("no job is bound to the evidence host")
        if name not in bound.tools:
            raise WorkflowError(f"{name} is not available for this job")
        if bound.turns <= 0:
            bound.overrun = True
            raise WorkflowError("tool turn budget exhausted")
        bound.turns -= 1
        return bound

    def _read(self, path: str, start: int, end: int) -> str:
        bound = self._bound("read_evidence")
        return json.dumps(bound.reader.read(path, start, end))

    def _search(self, query: str, scope: str, offset: int) -> str:
        bound = self._bound("search_evidence")
        assert isinstance(bound.reader, EvidenceTools)
        return json.dumps(bound.reader.search(query, scope, offset))

    def _validate(self, candidate: str) -> str:
        bound = self._bound("validate_candidate")
        try:
            if bound.validator is None:
                raise WorkflowError("no writer validation context")
            bound.validator(candidate)
            value: dict = {"valid": True}
        except (WorkflowError, OSError, ValueError, TypeError, KeyError) as exc:
            value = {"valid": False, "issues": [str(exc)[:4000]]}
        text = json.dumps(value)
        if len(text.encode()) > bound.reader.remaining:
            raise WorkflowError("tool output budget exhausted")
        bound.reader.remaining -= len(text.encode())
        return text


def prepare_home(store: Path) -> Path:
    """An isolated CODEX_HOME so the user's MCP servers, plugins and skills stay out of
    pipeline threads; auth.json is a symlink so the ChatGPT login stays shared."""
    home = store / "codex-home"
    home.mkdir(parents=True, exist_ok=True)
    source = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser() / "auth.json"
    link = home / "auth.json"
    if not link.is_symlink():
        if link.exists():
            link.unlink()
        link.symlink_to(source)
    return home


def check_auth(client: Any) -> None:
    account = client.account().account
    kind = getattr(getattr(account, "root", account), "type", None)
    kind = getattr(kind, "value", kind)
    if kind != "chatgpt":
        raise WorkflowError("a ChatGPT subscription login is required for Codex; no API key")


class CodexSession:
    """One app server and one evidence host per worker thread."""

    def __init__(self, store: Path) -> None:
        from openai_codex import Codex, CodexConfig

        self.store = store
        self.host = EvidenceHost()
        env = {k: v for k, v in os.environ.items() if not k.startswith(ENV_PREFIXES)}
        env["CODEX_HOME"] = str(prepare_home(store))
        self.client = Codex(
            CodexConfig(
                env=env,
                config_overrides=(*OVERRIDES, f'mcp_servers.evidence.url="{self.host.url}"'),
            )
        )
        try:
            check_auth(self.client)
        except BaseException:
            self.close()
            raise

    def close(self) -> None:
        try:
            self.client.close()
        finally:
            self.host.close()


_local = threading.local()
_sessions: list[CodexSession] = []
_lock = threading.Lock()


def session(store: Path) -> CodexSession:
    current = getattr(_local, "session", None)
    if current is None or current.store != store:
        current = _local.session = CodexSession(store)
        with _lock:
            _sessions.append(current)
    return current


@atexit.register
def _close_sessions() -> None:
    for current in _sessions:
        try:
            current.close()
        except Exception:
            pass


def consume(turn: Any, out: Any, timeout: float) -> dict:
    """Drain a turn's notifications on a worker thread; interrupt at the deadline.

    Usage is kept from the last token-usage notification whatever happens next, so a
    failed or interrupted turn is still charged."""
    state: dict = {"items": [], "usage": None, "turn": None, "error": None, "timed_out": False}

    def pump() -> None:
        try:
            for event in turn.stream():
                payload = event.payload
                # Streamed deltas repeat the text a token at a time; the completed
                # items carry it once, so only those and the turn events are kept.
                if not event.method.endswith(("/delta", "Delta")):
                    dump = getattr(payload, "model_dump", None)
                    body = dump(mode="json") if dump else str(payload)
                    record = {"method": event.method, "payload": body}
                    out.write(json.dumps(record, default=str) + "\n")
                    out.flush()
                    if out.tell() > TRANSCRIPT_LIMIT:
                        raise WorkflowError("transcript output limit reached")
                if event.method == "item/completed" and payload.turn_id == turn.id:
                    state["items"].append(payload.item)
                elif event.method == "thread/tokenUsage/updated" and payload.turn_id == turn.id:
                    state["usage"] = payload.token_usage
                elif event.method == "turn/completed" and payload.turn.id == turn.id:
                    state["turn"] = payload.turn
                    return
        except BaseException as exc:  # recorded, then reported by the caller
            state["error"] = exc

    worker = threading.Thread(target=pump, daemon=True, name="codex-turn")
    worker.start()
    worker.join(timeout)
    if worker.is_alive():
        state["timed_out"] = True
        try:
            turn.interrupt()
        except Exception:
            pass
        worker.join(30)
    return state


def run_job(agent: Runtime, payload: str, key: str, model: str) -> str:
    """One reserved ledger job on Codex, mirroring Runtime._query's contract."""
    from openai_codex import ApprovalMode, Sandbox, TextInput
    from openai_codex.types import ReasoningEffort

    profile = tool_profile(agent._step)
    reader = EvidenceTools(agent.root) if profile == "extended" else ReadTools(agent.root)
    tools = [] if profile == "none" else ["read_evidence"]
    if profile == "extended":
        tools.append("search_evidence")
        if agent._validator is not None:
            tools.append("validate_candidate")
    messages = json.loads(payload)
    system_parts = [m["content"] for m in messages if m.get("role") == "system"]
    user_payload = json.dumps(
        [m for m in messages if m.get("role") != "system"], ensure_ascii=False
    )
    contract = (agent.root / "contract/AGENTS.md").read_text()
    system = SYSTEM.replace("Use only the supplied evidence read tool.", PROFILE_SENTENCE[profile])
    instructions = "\n\n".join([system + contract, *system_parts])
    turns = 1 if profile == "none" else int(agent.config.get("max_turns", 6))
    current = session(agent.store)
    binding = Binding(reader, tools, agent._validator, max(0, turns - 1))
    current.host.binding = binding
    scratch = agent.store / "codex-scratch"
    scratch.mkdir(parents=True, exist_ok=True)
    transcript = agent.store / "transcripts" / f"{key}.jsonl"
    transcript.parent.mkdir(parents=True, exist_ok=True)
    timeout = float(agent.config.get("timeout", 600))
    try:
        with transcript.open("w", encoding="utf-8") as out:
            thread = current.client.thread_start(
                model=model,
                sandbox=Sandbox.read_only,
                approval_mode=ApprovalMode.deny_all,
                cwd=str(scratch),
                ephemeral=True,
                base_instructions=instructions,
            )
            turn = thread.turn(TextInput(user_payload), model=model, effort=ReasoningEffort(EFFORT))
            state = consume(turn, out, timeout)
            usage = map_usage(state["usage"])
            if usage is not None:
                line = {"model": model, "usage": usage, "total_cost_usd": None}
                out.write(json.dumps(line) + "\n")
    finally:
        current.host.binding = None
    output = final_response(state["items"])
    finished = state["turn"]
    status = getattr(finished, "status", None)
    status = getattr(status, "value", status)
    commands = sum(
        1
        for i in state["items"]
        if getattr(getattr(i, "root", i), "type", None) == "commandExecution"
    )
    if commands:
        print(f"agentic: {agent._step} ran {commands} shell command(s) on Codex", flush=True)
    if state["timed_out"]:
        error = f"timed out after {timeout:g}s; the turn was interrupted"
    elif state["error"] is not None:
        error = f"Codex transport failed: {state['error']}"[:500]
    elif finished is None:
        error = "Codex turn ended without a completion event"
    elif status != "completed":
        detail = getattr(getattr(finished, "error", None), "message", "") or ""
        error = f"Codex turn {status}: {detail}"[:500]
    elif binding.overrun:
        error = "tool turn budget exhausted; the job kept calling tools past its budget"
    elif not output.strip():
        error = "empty Codex output"
    else:
        error = ""
    agent.ledger.finish(key, output, usage, error, reader.dependencies, cost=None)
    if error:
        raise WorkflowError(error)
    return output.strip()
