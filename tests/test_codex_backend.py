"""The Codex app-server backend: same tools, ledger and budgets as the Claude branch."""

import asyncio
import json
import threading
from pathlib import Path
from types import SimpleNamespace

import pytest

from beril_wiki.agentic import codex as C
from beril_wiki.agentic import runtime as R


def usage(input=100, cached=20, output=40, reasoning=30, write=0):
    total = SimpleNamespace(
        input_tokens=input,
        cached_input_tokens=cached,
        output_tokens=output,
        reasoning_output_tokens=reasoning,
        cache_write_input_tokens=write,
        total_tokens=input + output,
    )
    return SimpleNamespace(total=total, last=total)


def test_usage_counts_reasoning_once_and_splits_cached_input():
    assert C.map_usage(usage()) == {
        "input_tokens": 80,
        "output_tokens": 40,
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 20,
    }
    assert C.map_usage(None) is None


def test_final_response_prefers_the_final_answer_phase():
    items = [
        SimpleNamespace(root=SimpleNamespace(type="agentMessage", phase=None, text="draft")),
        SimpleNamespace(root=SimpleNamespace(type="mcpToolCall", tool="read_evidence")),
        SimpleNamespace(root=SimpleNamespace(type="agentMessage", phase="final_answer", text="{}")),
    ]
    assert C.final_response(items) == "{}"
    assert C.final_response(items[:2]) == "draft"
    assert C.final_response([]) == ""


@pytest.fixture
def host():
    server = C.EvidenceHost()
    yield server
    server.close()


def call(url, name, args):
    from mcp import ClientSession
    from mcp.client.streamable_http import streamablehttp_client

    async def go():
        async with streamablehttp_client(url) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                return await session.call_tool(name, args)

    return asyncio.run(go())


def test_host_serves_bound_reader_and_refuses_tools_outside_the_profile(tmp_path, host):
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/a__REPORT.md").write_text("The Q10 value was 2.3 (n=12).")
    reader = R.ReadTools(tmp_path)
    host.binding = C.Binding(reader, ["read_evidence"], None, turns=2)
    args = {"path": "staging/a__REPORT.md", "start": 0, "end": 7}
    result = call(host.url, "read_evidence", args)
    assert not result.isError
    assert json.loads(result.content[0].text)["text"] == "The Q10"
    assert "staging/a__REPORT.md" in reader.dependencies
    denied = call(host.url, "search_evidence", {"query": "Q10", "scope": "staging", "offset": 0})
    assert denied.isError and "not available" in denied.content[0].text
    call(host.url, "read_evidence", args)  # turns are charged per batch by consume()
    host.binding.turns = 0
    over = call(host.url, "read_evidence", args)
    assert over.isError and "turn budget" in over.content[0].text
    assert "return the final answer now" in over.content[0].text
    assert host.binding.refused == 1
    host.binding = None
    unbound = call(host.url, "read_evidence", args)
    assert unbound.isError and "no job" in unbound.content[0].text


def test_validate_candidate_reports_validator_issues(tmp_path, host):
    def validator(candidate):
        raise R.WorkflowError("missing evidence id e1")

    host.binding = C.Binding(R.EvidenceTools(tmp_path), ["validate_candidate"], validator, 3)
    result = call(host.url, "validate_candidate", {"candidate": "{}"})
    assert json.loads(result.content[0].text) == {
        "valid": False,
        "issues": ["missing evidence id e1"],
    }


def agent_for(tmp_path, **extra):
    (tmp_path / "contract").mkdir(exist_ok=True)
    (tmp_path / "contract/AGENTS.md").write_text("Preserve source evidence.")
    config = (
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "jobs"),
            run="test",
            model="gpt-6-astra",
            cli="claude",
            max_tokens=100000,
            max_jobs=20,
            reserve_tokens=10,
            max_turns=4,
            timeout=5,
        )
        | extra
    )
    agent = R.Runtime(config)
    agent._step = "curator/topics"
    return agent


def notification(method, **payload):
    return SimpleNamespace(method=method, payload=SimpleNamespace(**payload))


class FakeTurn:
    def __init__(self, events, block=None):
        self.id, self.thread_id = "t1", "th1"
        self.events, self.block, self.interrupted = events, block, False

    def stream(self):
        yield from self.events
        if self.block is not None:
            self.block.wait()

    def interrupt(self):
        self.interrupted = True
        if self.block is not None:
            self.block.set()


class FakeClient:
    def __init__(self, turn):
        self.turn, self.starts, self.turns = turn, [], []

    def thread_start(self, **kw):
        self.starts.append(kw)
        client = self

        class Thread:
            def turn(self, text, **kw):
                client.turns.append((text, kw))
                return client.turn

        return Thread()

    def close(self):
        pass


def fake_session(monkeypatch, turn):
    client = FakeClient(turn)
    fake = SimpleNamespace(client=client, host=SimpleNamespace(binding=None, url="http://h"))
    monkeypatch.setattr(C, "session", lambda store: fake)
    return fake


def completed(text, status="completed", error=None):
    message = SimpleNamespace(type="agentMessage", phase="final_answer", text=text)
    return [
        notification("item/agentMessage/delta", turn_id="t1", delta="DELTA-TEXT"),
        notification("thread/tokenUsage/updated", turn_id="t1", token_usage=usage()),
        notification("item/completed", turn_id="t1", item=SimpleNamespace(root=message)),
        notification("turn/completed", turn=SimpleNamespace(id="t1", status=status, error=error)),
    ]


def test_run_job_records_usage_transcript_and_clears_binding(tmp_path, monkeypatch):
    agent = agent_for(tmp_path)
    fake = fake_session(monkeypatch, FakeTurn(completed('{"ok": true}')))
    agent.ledger.reserve("k1", agent._step, "gpt-6-astra")
    payload = json.dumps(
        [{"role": "system", "content": "PACKED"}, {"role": "user", "content": "write"}]
    )
    assert C.run_job(agent, payload, "k1", "gpt-6-astra") == '{"ok": true}'
    start = fake.client.starts[0]
    assert start["model"] == "gpt-6-astra" and start["ephemeral"] is True
    assert "Preserve source evidence." in start["base_instructions"]
    assert start["base_instructions"].endswith("PACKED")
    assert "candidate-check tools" in start["base_instructions"]
    text, options = fake.client.turns[0]
    assert json.loads(getattr(text, "text", text)) == [{"role": "user", "content": "write"}]
    assert getattr(options["effort"], "value", options["effort"]) == "high"
    assert fake.host.binding is None
    row = agent.ledger.db.execute("SELECT status,tokens,cost FROM jobs WHERE key='k1'").fetchone()
    assert row == ("done", 140, None)
    path = Path(agent.store) / "transcripts/k1.jsonl"
    assert R.transcript_usage(path) == (C.map_usage(usage()), None)
    transcript = path.read_text()
    assert "DELTA-TEXT" not in transcript and '"method": "item/completed"' in transcript


def test_failed_turn_keeps_usage_and_fails_the_job(tmp_path, monkeypatch):
    agent = agent_for(tmp_path)
    failed = completed("", status="failed", error=SimpleNamespace(message="boom"))
    fake_session(monkeypatch, FakeTurn(failed))
    agent.ledger.reserve("k2", agent._step, "gpt-6-astra")
    with pytest.raises(R.WorkflowError, match="boom"):
        C.run_job(agent, json.dumps([{"role": "user", "content": "x"}]), "k2", "gpt-6-astra")
    row = agent.ledger.db.execute("SELECT status,tokens,error FROM jobs WHERE key='k2'").fetchone()
    assert row[0] == "failed" and row[1] == 140 and "boom" in row[2]


def test_timeout_interrupts_the_turn_and_charges_what_arrived(tmp_path, monkeypatch):
    agent = agent_for(tmp_path, timeout=0.2)
    turn = FakeTurn(completed("late")[1:2], block=threading.Event())
    fake_session(monkeypatch, turn)
    agent.ledger.reserve("k3", agent._step, "gpt-6-astra")
    with pytest.raises(R.WorkflowError, match="timed out"):
        C.run_job(agent, json.dumps([{"role": "user", "content": "x"}]), "k3", "gpt-6-astra")
    assert turn.interrupted
    row = agent.ledger.db.execute("SELECT status,tokens FROM jobs WHERE key='k3'").fetchone()
    assert row == ("failed", 140)


def tool_batch(count):
    """One model turn issuing `count` parallel tool calls, then their completions."""
    call_item = SimpleNamespace(root=SimpleNamespace(type="mcpToolCall", tool="read_evidence"))
    started = [notification("item/started", turn_id="t1", item=call_item) for _ in range(count)]
    done = [notification("item/completed", turn_id="t1", item=call_item) for _ in range(count)]
    thinking = SimpleNamespace(root=SimpleNamespace(type="reasoning"))
    return [*started, *done, notification("item/started", turn_id="t1", item=thinking)]


class SpyHost:
    url = "http://h"

    def __init__(self):
        self._binding, self.seen = None, None

    @property
    def binding(self):
        return self._binding

    @binding.setter
    def binding(self, value):
        if value is not None:
            self.seen = value
        self._binding = value


def test_parallel_tool_calls_spend_one_turn_per_batch_and_a_loop_is_interrupted(
    tmp_path, monkeypatch
):
    agent = agent_for(tmp_path)  # max_turns 4 -> budget 3
    events = tool_batch(5) + tool_batch(3) + tool_batch(1) + completed("answer")
    fake = fake_session(monkeypatch, FakeTurn(events))
    fake.host = SpyHost()
    agent.ledger.reserve("k4", agent._step, "gpt-6-astra")
    payload = json.dumps([{"role": "user", "content": "x"}])
    assert C.run_job(agent, payload, "k4", "gpt-6-astra") == "answer"
    assert fake.host.seen.batches == 3 and fake.host.seen.turns == 0

    # Seven tool-calling turns against a budget of three: interrupted, charged, failed.
    turn = FakeTurn([e for _ in range(7) for e in tool_batch(2)] + completed("late"))
    fake = fake_session(monkeypatch, turn)
    fake.host = SpyHost()
    agent.ledger.reserve("k5", agent._step, "gpt-6-astra")
    with pytest.raises(R.WorkflowError, match="overrun"):
        C.run_job(agent, payload, "k5", "gpt-6-astra")
    assert turn.interrupted
    row = agent.ledger.db.execute("SELECT status,tokens FROM jobs WHERE key='k5'").fetchone()
    assert row == ("failed", 140)


def test_one_session_per_thread(tmp_path, monkeypatch):
    built = []

    class FakeSession:
        def __init__(self, store):
            built.append(store)
            self.store = store

    monkeypatch.setattr(C, "CodexSession", FakeSession)
    monkeypatch.setattr(C, "_local", threading.local())
    for _ in range(3):
        assert C.session(tmp_path) is C.session(tmp_path)
    assert built == [tmp_path]


def test_each_session_gets_its_own_home_with_the_shared_login(tmp_path, monkeypatch):
    monkeypatch.setenv("CODEX_HOME", str(tmp_path / "user"))
    (tmp_path / "user").mkdir()
    (tmp_path / "user/auth.json").write_text("{}")
    first, second = C.prepare_home(tmp_path / "store", "a"), C.prepare_home(tmp_path / "store", "b")
    assert first != second and first.is_dir() and second.is_dir()
    assert (first / "auth.json").resolve() == (tmp_path / "user/auth.json").resolve()
    assert C.prepare_home(tmp_path / "store", "a") == first


def account_of(kind):
    account = None if kind is None else SimpleNamespace(root=SimpleNamespace(type=kind))
    return SimpleNamespace(account=lambda: SimpleNamespace(account=account))


def test_auth_requires_a_chatgpt_account():
    C.check_auth(account_of("chatgpt"))
    with pytest.raises(R.WorkflowError, match="ChatGPT"):
        C.check_auth(account_of("apiKey"))
    with pytest.raises(R.WorkflowError, match="ChatGPT"):
        C.check_auth(account_of(None))


def test_gpt_models_dispatch_to_codex_and_claude_keys_ignore_the_codex_revision(
    tmp_path, monkeypatch
):
    agent = agent_for(tmp_path, model="claude-opus-5-5")
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    seen = []

    async def fake_query(payload, key, model):
        seen.append(("claude", key, model))
        agent.ledger.finish(key, "claude answer", {"input_tokens": 1, "output_tokens": 1})
        return "claude answer"

    monkeypatch.setattr(agent, "_query", fake_query)
    messages = [{"role": "user", "content": "write"}]
    assert agent.ask(messages, "write/concepts/x.md") == "claude answer"
    key_before = seen[0][1]

    def fake_run(agent_, payload, key, model):
        seen.append(("codex", key, model))
        agent_.ledger.finish(key, "codex answer", {"input_tokens": 1, "output_tokens": 1})
        return "codex answer"

    monkeypatch.setattr(C, "run_job", fake_run)
    monkeypatch.setattr(C, "check_auth", lambda client: None)
    monkeypatch.setattr(C, "session", lambda store: SimpleNamespace(client=None))
    monkeypatch.setitem(agent.config, "model", "gpt-6-astra")
    assert agent.ask(messages, "write/concepts/x.md") == "codex answer"
    key_codex = seen[1][1]
    assert seen[1][0] == "codex" and seen[1][2] == "gpt-6-astra"

    # A new adapter revision re-keys Codex jobs only.
    monkeypatch.setattr(R, "CODEX_REVISION", "codex@changed")
    assert agent.ask(messages, "write/concepts/x.md") == "codex answer"
    assert seen[2][1] != key_codex
    monkeypatch.setitem(agent.config, "model", "claude-opus-5-5")
    assert agent.ask(messages, "write/concepts/x.md") == "claude answer"
    assert len(seen) == 3  # cached under the unchanged Claude key
    assert key_before == seen[0][1]


def test_codex_jobs_ignore_remembered_claude_refusals(tmp_path, monkeypatch):
    agent = agent_for(tmp_path, model="gpt-6-astra")
    step = "write/concepts/x.md"
    agent.ledger.reserve("old", step, "claude-opus-5-5")
    agent.ledger.finish(
        "old",
        json.dumps({"refused_to": "claude-opus-5"}),
        {"input_tokens": 1, "output_tokens": 1},
        "refused on claude-opus-5-5 [bio]",
        status="rejected",
    )
    assert agent.ledger.refused_model(R.refusal_scope(step)) == "claude-opus-5"
    models = []

    def fake_run(agent_, payload, key, model):
        models.append(model)
        agent_.ledger.finish(key, "answer", {"input_tokens": 1, "output_tokens": 1})
        return "answer"

    monkeypatch.setattr(C, "run_job", fake_run)
    monkeypatch.setattr(C, "session", lambda store: SimpleNamespace(client=None))
    monkeypatch.setattr(C, "check_auth", lambda client: None)
    assert agent.ask([{"role": "user", "content": "x"}], step) == "answer"
    assert models == ["gpt-6-astra"]


def test_backend_for_prefixes():
    assert R.backend_for("gpt-6-astra") == "codex"
    assert R.backend_for("claude-opus-5-5") == "claude"
    assert R.backend_for("test") == "claude"
