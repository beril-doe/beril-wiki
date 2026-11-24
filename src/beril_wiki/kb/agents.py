"""Start a vendor harness on one task: instructions, a prompt and the wiki tools.

Two adapters with one contract. A model named ``gpt-*`` runs on the Codex app server
(``openai-codex``); ``claude-*`` runs on the Claude Agent SDK. Each gets the skill text
as its instructions, the session's MCP URL as its only tool source, and no shell, file
or web access. Everything editorial lives in the skill and the tools; an adapter only
knows how to log in, start a turn, stop it at a deadline and report usage.

Both use a subscription login by default. ``BERIL_WIKI_AUTH=api`` keeps the
``ANTHROPIC_*`` and ``OPENAI_*`` variables so each harness bills its API key instead.
"""

from __future__ import annotations

import asyncio
import dataclasses
import json
import os
import threading
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

CLAUDE_AUTH_ENV = (
    "ANTHROPIC_API_KEY",
    "ANTHROPIC_AUTH_TOKEN",
    "ANTHROPIC_BASE_URL",
    "CLAUDE_CODE_USE_BEDROCK",
    "CLAUDE_CODE_USE_VERTEX",
    "CLAUDE_CODE_USE_FOUNDRY",
    "CLAUDE_CODE_OAUTH_TOKEN",
)
CODEX_ENV_PREFIXES = ("OPENAI_", "ANTHROPIC_", "CLAUDE_")
TRANSCRIPT_LIMIT = 4_000_000


@dataclass
class Agent:
    model: str
    effort: str = "medium"

    @property
    def provider(self) -> str:
        return "codex" if self.model.startswith("gpt-") else "claude"

    @classmethod
    def parse(cls, spec: str) -> Agent:
        """``model`` or ``model@effort``, such as ``gpt-6.1-sol@high``."""
        model, _, effort = spec.partition("@")
        return cls(model.strip(), effort.strip() or "medium")

    def __str__(self) -> str:
        return f"{self.model}@{self.effort}"


@dataclass
class Run:
    agent: str
    ok: bool = False
    error: str = ""
    text: str = ""
    seconds: float = 0.0
    turns: int = 0
    input_tokens: int = 0  # not served from cache
    cached_tokens: int = 0
    cache_write_tokens: int = 0
    output_tokens: int = 0
    cost_usd: float | None = None  # what the harness reported; None on a subscription

    @property
    def tokens(self) -> int:
        return self.input_tokens + self.cached_tokens + self.cache_write_tokens + self.output_tokens


def api_auth() -> bool:
    return os.environ.get("BERIL_WIKI_AUTH", "subscription") == "api"


def run(
    agent: Agent,
    instructions: str,
    prompt: str,
    mcp_url: str,
    tools: tuple[str, ...],
    workdir: Path,
    *,
    transcript: Path | None = None,
    timeout: float = 900.0,
    max_turns: int = 40,
    native: Path | None = None,
    max_usd: float | None = None,
) -> Run:
    """Run one agent to completion. Never raises for a model or transport failure:
    the returned ``Run`` says what happened, and the staged session says what it did.

    ``native`` gives the harness its own read-only file tools in that folder. Pipeline
    runs leave it unset; it exists to measure what the wiki tools save.
    """
    workdir.mkdir(parents=True, exist_ok=True)
    began = time.monotonic()
    out = transcript.open("w", encoding="utf-8") if transcript else None
    try:
        if agent.provider == "codex":
            result = _codex(
                agent,
                instructions,
                prompt,
                mcp_url,
                tools,
                workdir,
                out,
                timeout,
                native,
                max_turns,
            )
        else:
            result = asyncio.run(
                _claude(
                    agent,
                    instructions,
                    prompt,
                    mcp_url,
                    tools,
                    workdir,
                    out,
                    timeout,
                    max_turns,
                    native,
                    max_usd,
                )
            )
    except Exception as exc:  # reported, not raised: the caller decides what a failure costs
        result = Run(str(agent), error=f"{type(exc).__name__}: {exc}"[:500])
    finally:
        if out:
            out.close()
    result.seconds = round(time.monotonic() - began, 1)
    return result


def _record(out: Any, record: dict) -> None:
    if out is not None and out.tell() < TRANSCRIPT_LIMIT:
        out.write(json.dumps(record, default=str) + "\n")
        out.flush()


# Codex app server


def codex_home(workdir: Path) -> Path:
    """An isolated CODEX_HOME, so the user's own MCP servers, plugins and skills stay out
    of a pipeline thread. The login is shared through a symlink."""
    home = workdir / "codex-home" / f"{os.getpid()}-{threading.get_ident()}"
    home.mkdir(parents=True, exist_ok=True)
    source = Path(os.environ.get("CODEX_HOME", "~/.codex")).expanduser() / "auth.json"
    link = home / "auth.json"
    if not link.is_symlink():
        link.unlink(missing_ok=True)
        link.symlink_to(source)
    return home


def codex_overrides(mcp_url: str, tools: tuple[str, ...], shell: bool) -> tuple[str, ...]:
    overrides = [
        'model_provider="openai"',
        f"features.shell_tool={'true' if shell else 'false'}",
        "features.memories=false",
        # The login's ChatGPT apps and plugins bring their own tools into every thread;
        # a model asked to "search" once called the GitHub connector in place of the wiki.
        "features.apps=false",
        "features.plugins=false",
        "features.multi_agent=false",
        "features.image_generation=false",
        'web_search="disabled"',
        'approval_policy="never"',
        "notify=[]",
        f'mcp_servers.wiki.url="{mcp_url}"',
    ]
    if not api_auth():
        overrides.append('forced_login_method="chatgpt"')
    # Under a never-ask policy an MCP call is denied unless its tool is pre-approved.
    overrides += [f'mcp_servers.wiki.tools.{t}.approval_mode="approve"' for t in tools]
    return tuple(overrides)


def _codex(
    agent: Agent,
    instructions: str,
    prompt: str,
    mcp_url: str,
    tools: tuple[str, ...],
    workdir: Path,
    out: Any,
    timeout: float,
    native: Path | None,
    max_turns: int,
) -> Run:
    from openai_codex import ApprovalMode, Codex, CodexConfig, Sandbox, TextInput
    from openai_codex.types import ReasoningEffort

    result = Run(str(agent))
    # The SDK starts the app server with os.environ overlaid by this mapping, so a
    # credential is kept out of the child only by overriding it, not by leaving it out.
    env = {"CODEX_HOME": str(codex_home(workdir))}
    if not api_auth():
        env |= {k: "" for k in os.environ if k.startswith(CODEX_ENV_PREFIXES)}
    scratch = workdir / "codex-scratch"
    scratch.mkdir(exist_ok=True)
    overrides = codex_overrides(mcp_url, tools, shell=native is not None)
    # BERIL_WIKI_CODEX_BIN runs a Codex binary other than the one the SDK bundles,
    # for a model the bundled release does not list yet.
    binary = os.environ.get("BERIL_WIKI_CODEX_BIN") or None
    client = Codex(CodexConfig(codex_bin=binary, env=env, config_overrides=overrides))
    state: dict[str, Any] = {"items": [], "usage": None, "turn": None, "error": None, "calls": 0}
    try:
        thread = client.thread_start(
            model=agent.model,
            sandbox=Sandbox.read_only,
            approval_mode=ApprovalMode.deny_all,
            cwd=str(native or scratch),
            ephemeral=True,
            base_instructions=instructions,
        )
        turn = thread.turn(
            TextInput(prompt), model=agent.model, effort=ReasoningEffort(agent.effort)
        )

        def pump() -> None:
            try:
                for event in turn.stream():
                    payload: Any = event.payload
                    if not event.method.endswith(("/delta", "Delta")):
                        dump = getattr(payload, "model_dump", None)
                        body = dump(mode="json") if dump else str(payload)
                        _record(out, {"method": event.method, "payload": body})
                    if event.method == "item/started":
                        started = getattr(payload.item, "root", payload.item)
                        if getattr(started, "type", None) == "mcpToolCall":
                            state["calls"] += 1
                            # The server refuses calls past the session budget, but a
                            # model that keeps asking still burns tokens; stop it.
                            if state["calls"] == max_turns + 1:
                                turn.interrupt()
                    if event.method == "item/completed" and payload.turn_id == turn.id:
                        state["items"].append(payload.item)
                    elif event.method == "thread/tokenUsage/updated":
                        state["usage"] = payload.token_usage
                    elif event.method == "turn/completed" and payload.turn.id == turn.id:
                        state["turn"] = payload.turn
                        return
            except BaseException as exc:  # reported below
                state["error"] = exc

        worker = threading.Thread(target=pump, daemon=True, name="codex-turn")
        worker.start()
        worker.join(timeout)
        timed_out = worker.is_alive()
        if timed_out:
            try:
                turn.interrupt()
            except Exception:
                pass
            worker.join(30)
    finally:
        client.close()
    usage = getattr(state["usage"], "total", None)
    if usage is not None:
        result.cached_tokens = usage.cached_input_tokens
        result.input_tokens = max(0, usage.input_tokens - usage.cached_input_tokens)
        result.cache_write_tokens = getattr(usage, "cache_write_input_tokens", 0) or 0
        result.output_tokens = usage.output_tokens
    roots = [getattr(i, "root", i) for i in state["items"]]
    result.turns = sum(1 for r in roots if getattr(r, "type", None) == "mcpToolCall")
    messages = [r for r in roots if getattr(r, "type", None) == "agentMessage"]
    result.text = (messages[-1].text or "") if messages else ""
    finished = state["turn"]
    status = getattr(getattr(finished, "status", None), "value", getattr(finished, "status", None))
    if timed_out:
        result.error = f"timed out after {timeout:g}s; the turn was interrupted"
    elif state["calls"] > max_turns:
        result.error = f"interrupted after {state['calls']} tool calls; the limit is {max_turns}"
    elif state["error"] is not None:
        result.error = f"Codex transport failed: {state['error']}"[:500]
    elif finished is None:
        result.error = "Codex turn ended without a completion event"
    elif status != "completed":
        detail = getattr(getattr(finished, "error", None), "message", "") or ""
        result.error = f"Codex turn {status}: {detail}"[:500]
    result.ok = not result.error
    return result


# Claude Agent SDK


async def _claude(
    agent: Agent,
    instructions: str,
    prompt: str,
    mcp_url: str,
    tools: tuple[str, ...],
    workdir: Path,
    out: Any,
    timeout: float,
    max_turns: int,
    native: Path | None,
    max_usd: float | None,
) -> Run:
    from claude_agent_sdk import ClaudeAgentOptions, ResultMessage, query

    result = Run(str(agent))
    env = {"CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1"}
    if not api_auth():
        env |= dict.fromkeys(CLAUDE_AUTH_ENV, "")
    files = ("Read", "Grep", "Glob") if native else ()
    options = ClaudeAgentOptions(
        model=agent.model,
        system_prompt=instructions,
        tools=list(files),
        allowed_tools=[*files, *(f"mcp__wiki__{t}" for t in tools)],
        mcp_servers={"wiki": {"type": "http", "url": mcp_url}},
        strict_mcp_config=True,
        setting_sources=[],
        skills=[],
        plugins=[],
        cwd=native or workdir,
        env=env,
        permission_mode="dontAsk",
        max_turns=max_turns,
        max_budget_usd=max_usd,
        fallback_model=None,
        effort=cast(Any, agent.effort),
        extra_args={"no-session-persistence": None, "disable-slash-commands": None},
    )

    async def messages():
        yield {"type": "user", "message": {"role": "user", "content": prompt}}

    terminal = None
    try:
        async with asyncio.timeout(timeout):
            async for message in query(prompt=messages(), options=options):
                if dataclasses.is_dataclass(message):
                    _record(out, dataclasses.asdict(message))  # type: ignore[arg-type]
                if isinstance(message, ResultMessage):
                    terminal = message
    except TimeoutError:
        result.error = f"timed out after {timeout:g}s"
    except Exception as exc:
        # The CLI exits non-zero after an is_error result (max turns and the like);
        # that result already carried the usage, so keep it.
        if terminal is None:
            raise
        result.error = f"{type(exc).__name__}: {exc}"[:300]
    if terminal is not None:
        usage = terminal.usage or {}
        result.input_tokens = int(usage.get("input_tokens", 0) or 0)
        result.cached_tokens = int(usage.get("cache_read_input_tokens", 0) or 0)
        result.cache_write_tokens = int(usage.get("cache_creation_input_tokens", 0) or 0)
        result.output_tokens = int(usage.get("output_tokens", 0) or 0)
        result.cost_usd = terminal.total_cost_usd
        result.turns = int(getattr(terminal, "num_turns", 0) or 0)
        result.text = terminal.result or ""
        if terminal.is_error or terminal.subtype != "success":
            result.error = result.error or f"Claude run ended {terminal.subtype}"
    elif not result.error:
        result.error = "Claude run ended without a result"
    result.ok = not result.error
    return result
