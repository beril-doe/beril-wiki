"""Offline checks for the page agent's host state and hooks (no model calls)."""

import asyncio
import dataclasses
import json
from typing import Any

import pytest

from beril_wiki.agentic import page_agent as PA
from beril_wiki.agentic.runtime import CandidateError

REAL_RUN = PA.run  # the autouse fixture in conftest replaces it with a recorded session


def _page(tmp_path, check=None, review=None):
    return PA.Page(
        step="write/concepts/a.md",
        messages=[{"role": "user", "content": "task"}],
        text="Old body.",
        meta={"description": "A.", "accounted_evidence": {}},
        meta_help="",
        check=check or (lambda text, meta: [] if "[src:" in text else ["needs a citation"]),
        review=review or (lambda text, meta: [] if "good" in text else ["claim unsupported"]),
        reads=[tmp_path / "staging"],
    )


def _session(tmp_path, **kw):
    work = tmp_path / "work"
    work.mkdir(parents=True)
    session = PA.Session(_page(tmp_path, **kw), work, max_reviews=3)
    PA._restore(session)
    return session


def test_submit_takes_only_the_text_both_approved(tmp_path):
    s = _session(tmp_path)
    page = s.workdir / "page.md"
    assert s.do_review()["issues"] == ["call check first: this text has not passed"]
    assert s.do_check() == {"passed": False, "issues": ["needs a citation"]}
    page.write_text("A claim. [src: x]")
    assert s.do_check()["passed"]
    assert s.do_review() == {"accepted": False, "issues": ["claim unsupported"]}
    page.write_text("A good claim. [src: x]")
    assert s.do_check()["passed"] and s.do_review()["accepted"]
    # An edit after both approvals voids them: submit refuses the changed text.
    page.write_text("A good claim, edited. [src: x]")
    assert s.do_submit()["missing"] == ["check", "review"]
    page.write_text("A good claim. [src: x]")
    assert s.do_submit()["accepted"] and s.submitted == ("A good claim. [src: x]", s.page.meta)


def test_review_limit_and_stage_stop_end_the_session(tmp_path):
    s = _session(tmp_path)
    (s.workdir / "page.md").write_text("Still unsupported. [src: x]")
    s.do_check()
    for _ in range(3):
        assert s.do_review()["accepted"] is False
    assert "review limit" in s.do_review()["stop"] and s.fatal

    def stop(text, meta):
        raise CandidateError("no progress", ["open objection"])

    t = _session(tmp_path / "b", review=stop)
    (t.workdir / "page.md").write_text("Text. [src: x]")
    t.do_check()
    assert t.do_review()["stop"] and t.open == ["open objection"] and t.fatal


def test_hooks_fence_writes_and_deny_only_repeats_of_unchanged_content(tmp_path):
    (tmp_path / "staging").mkdir()
    source = tmp_path / "staging/r.md"
    source.write_text("report")
    s = _session(tmp_path)
    hooks = PA.hooks_for(s)
    pre = hooks["PreToolUse"][0].hooks[0]
    post = hooks["PostToolUse"][0].hooks[0]
    compact = hooks["PreCompact"][0].hooks[0]
    stop = hooks["Stop"][0].hooks[0]

    def call(fn, data):
        return asyncio.run(fn(data, None, None))

    denied = lambda out: out.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"  # noqa: E731
    assert denied(call(pre, {"tool_name": "Edit", "tool_input": {"file_path": str(source)}}))
    assert not denied(
        call(pre, {"tool_name": "Edit", "tool_input": {"file_path": str(s.workdir / "page.md")}})
    )
    assert denied(call(pre, {"tool_name": "Read", "tool_input": {"file_path": "/etc/hosts"}}))
    read = {"tool_name": "Read", "tool_input": {"file_path": str(source)}}
    assert not denied(call(pre, read))
    assert denied(call(pre, read))  # the same content is already in context
    source.write_text("report, revised")
    assert not denied(call(pre, read))  # changed content may be read again
    page = {"tool_name": "Read", "tool_input": {"file_path": str(s.workdir / "page.md")}}
    assert not denied(call(pre, page)) and denied(call(pre, page))
    call(post, {"tool_name": "Edit", "tool_input": {"file_path": str(s.workdir / "page.md")}})
    assert not denied(call(pre, page))  # an edit clears the entry
    assert denied(call(pre, page))
    call(compact, {})
    assert not denied(call(pre, page))  # a compaction clears everything
    # One premature stop is blocked; a second, or a stop after submit, is not.
    assert call(stop, {})["decision"] == "block"
    assert call(stop, {}) == {}


def test_restore_continues_only_from_matching_scratch(tmp_path):
    s = _session(tmp_path)
    (s.workdir / "page.md").write_text("Checked. [src: x]")
    s.do_check()
    s.deps["staging/r.md"] = "hash"  # finding B2: a resumed session keeps what it read
    s.save()
    again = PA.Session(s.page, s.workdir, max_reviews=3)
    assert PA._restore(again) and again.checked == s.checked
    assert again.deps == {"staging/r.md": "hash"}
    (s.workdir / "page.md").write_text("Changed after the check.")
    third = PA.Session(s.page, s.workdir, max_reviews=3)
    assert not PA._restore(third)
    assert (s.workdir / "page.md").read_text() == "Old body."
    assert json.loads((s.workdir / "meta.json").read_text())["description"] == "A."


def test_a_page_with_too_many_earlier_sessions_fails_the_page_not_the_run(tmp_path, monkeypatch):
    from types import SimpleNamespace

    class Rows:
        def execute(self, sql, args):
            return SimpleNamespace(fetchone=lambda: ("failed", ""))

    agent: Any = SimpleNamespace(
        config={"model": "m"},
        root=tmp_path,
        ledger=SimpleNamespace(db=Rows()),
        jobs=[],
        effort=lambda step: None,
    )
    monkeypatch.setattr(PA, "MAX_SESSIONS", 3)
    with pytest.raises(PA.Exhausted, match="3 earlier sessions"):
        REAL_RUN(agent, _page(tmp_path), tmp_path / "work")


def test_the_reviewer_model_and_effort_key_the_session(tmp_path, monkeypatch):
    from types import SimpleNamespace

    keys = []

    class Rows:
        def execute(self, sql, args):
            keys.append(args[0])
            return SimpleNamespace(fetchone=lambda: ("failed", ""))

    monkeypatch.setattr(PA, "MAX_SESSIONS", 1)
    efforts = {}
    for review, level in (("gpt-a", None), ("gpt-b", None), ("gpt-b", "low")):
        efforts["review"] = level
        agent: Any = SimpleNamespace(
            config={"model": "m", "step_models": {"review": review}},
            root=tmp_path,
            ledger=SimpleNamespace(db=Rows()),
            jobs=[],
            effort=lambda step: efforts["review"] if step.endswith("/review") else None,
        )
        with pytest.raises(PA.Exhausted):
            REAL_RUN(agent, _page(tmp_path), tmp_path / "work")
    assert len(set(keys)) == 3


def test_scratch_approvals_belong_to_one_task_and_only_a_crash_resumes(tmp_path):
    work = tmp_path / "w"
    work.mkdir()
    first = PA.Session(_page(tmp_path), work, max_reviews=3, task="task-1")
    PA._restore(first)
    (work / "page.md").write_text("A good claim. [src: x]")
    assert first.do_check()["passed"] and first.do_review()["accepted"]
    # A crash before the session ended: the same task resumes with its approvals.
    crashed = PA.Session(_page(tmp_path), work, max_reviews=3, task="task-1")
    assert PA._restore(crashed) and crashed.reviewed == first.reviewed
    # New evidence is a new task: nothing carries over, the page starts from its text.
    other = PA.Session(_page(tmp_path), work, max_reviews=3, task="task-2")
    assert not PA._restore(other) and other.reviewed == "" and other.reviews == 0
    assert (work / "page.md").read_text() == "Old body."
    # A session that ended (here: spent its reviews) is never resumed, so a retry gets
    # its reviews back instead of inheriting the exhausted count.
    (work / "page.md").write_text("Still unsupported. [src: x]")
    other.do_check()
    for _ in range(4):
        other.do_review()
    assert other.fatal
    other.ended = True
    other.save()
    retry = PA.Session(_page(tmp_path), work, max_reviews=3, task="task-2")
    assert not PA._restore(retry) and retry.reviews == 0


def test_a_state_file_cut_short_by_a_crash_starts_fresh(tmp_path):
    work = tmp_path / "w"
    work.mkdir()
    (work / "page.md").write_text("Text.")
    (work / "state.json").write_text('{"checked": "ab')
    session = PA.Session(_page(tmp_path), work, max_reviews=3)
    assert not PA._restore(session)
    assert (work / "page.md").read_text() == "Old body."


def test_a_later_objection_voids_an_earlier_approval(tmp_path):
    verdicts = iter([[], ["now unsupported"]])
    s = _session(tmp_path, review=lambda text, meta: next(verdicts))
    (s.workdir / "page.md").write_text("A claim. [src: x]")
    s.do_check()
    assert s.do_review()["accepted"]
    assert s.do_review()["accepted"] is False
    assert s.do_submit()["missing"] == ["review"]


def test_hooks_resolve_relative_edits_and_fence_patterns_and_record_reads(tmp_path):
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/r.md").write_text("report")
    work = tmp_path / "w"
    work.mkdir()
    s = PA.Session(_page(tmp_path), work, max_reviews=3, root=tmp_path)
    PA._restore(s)
    pre = PA.hooks_for(s)["PreToolUse"][0].hooks[0]

    def denied(data):
        out = asyncio.run(pre(data, None, None))
        return out.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"

    assert not denied({"tool_name": "Edit", "tool_input": {"file_path": "page.md"}})
    assert denied({"tool_name": "Edit", "tool_input": {"file_path": "../page.md"}})
    for pattern in ("../*.sqlite", "/etc/*", "~/*"):
        assert denied({"tool_name": "Glob", "tool_input": {"pattern": pattern}})
    assert denied({"tool_name": "Grep", "tool_input": {"pattern": "x", "glob": "../**"}})
    assert not denied({"tool_name": "Grep", "tool_input": {"pattern": "../x", "path": str(work)}})
    assert not denied(
        {"tool_name": "Read", "tool_input": {"file_path": str(tmp_path / "staging/r.md")}}
    )
    assert not denied(
        {"tool_name": "Glob", "tool_input": {"pattern": "*.md", "path": str(tmp_path / "staging")}}
    )
    assert set(s.deps) == {"staging/r.md", "inventory:staging"}


def test_a_session_that_hits_its_turn_limit_ends_without_raising(tmp_path, monkeypatch):
    from types import SimpleNamespace

    from claude_agent_sdk import ResultMessage

    async def query(prompt, options):
        yield ResultMessage(
            subtype="error_max_turns",
            duration_ms=1,
            duration_api_ms=1,
            is_error=True,
            num_turns=24,
            session_id="s",
            usage={"input_tokens": 1, "output_tokens": 1},
            total_cost_usd=0.5,
        )
        raise Exception("Claude Code returned an error result: Reached maximum number of turns")

    monkeypatch.setattr(PA, "query", query)
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("rules")
    agent: Any = SimpleNamespace(
        config={"cli": "claude"}, store=tmp_path, root=tmp_path, effort=lambda step: None
    )
    session = _session(tmp_path)
    _, usage, cost, error, refused = asyncio.run(PA._drive(agent, session, "k", "m", False))
    assert (cost, error, refused) == (0.5, "SDK ended: error_max_turns", "")


def _result(cost=0.5):
    from claude_agent_sdk import ResultMessage

    return ResultMessage(
        subtype="success",
        duration_ms=1,
        duration_api_ms=1,
        is_error=False,
        num_turns=1,
        session_id="s",
        usage={"input_tokens": 1, "output_tokens": 1},
        total_cost_usd=cost,
    )


def test_a_failed_re_review_voids_the_earlier_approval(tmp_path):
    """Review finding E: submit takes nothing after a review that stopped the session."""
    verdicts = [[], CandidateError("reviewer returned no usable verdict twice")]

    def review(text, meta):
        verdict = verdicts.pop(0)
        if isinstance(verdict, Exception):
            raise verdict
        return verdict

    s = _session(tmp_path, review=review)
    (s.workdir / "page.md").write_text("A good claim. [src: x]")
    assert s.do_check()["passed"] and s.do_review()["accepted"]
    assert s.do_review()["stop"]
    assert s.do_submit()["missing"] == ["review"]


def test_the_review_tool_runs_a_claude_reviewer_inside_the_session_loop(tmp_path, monkeypatch):
    """Review finding G: the review tool's handler runs on the session's event loop, so a
    Claude reviewer's query cannot use asyncio.run there."""
    from beril_wiki.agentic import runtime as R

    async def fake_query(self, payload, key, model):
        return json.dumps({"accepted": True, "issues": []})

    monkeypatch.setattr(R.Runtime, "_query", fake_query)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("rules")
    agent = R.Runtime(
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "store"),
            run="t",
            model="claude-opus-5-5",
            cli="claude",
            max_tokens=10**7,
            max_jobs=50,
            reserve_tokens=10,
            step_models={"review": "claude-sonnet-5-5"},
        )
    )
    messages = [{"role": "user", "content": "write page"}]

    def review(text, meta):
        agent.review(messages, text, "write/concepts/a.md")
        return []

    captured = {}
    real_server = PA.create_sdk_mcp_server

    def server(name, tools):
        captured.update({t.name: t for t in tools})
        return real_server(name, tools=tools)

    monkeypatch.setattr(PA, "create_sdk_mcp_server", server)
    replies = []

    async def query(prompt, options):
        (session.workdir / "page.md").write_text("A good claim. [src: x]")
        replies.append(await captured["check"].handler({}))
        replies.append(await captured["review"].handler({}))
        yield _result()

    monkeypatch.setattr(PA, "query", query)
    session = _session(tmp_path, review=review)
    asyncio.run(PA._drive(agent, session, "k", "claude-haiku-5-5", False))
    verdict = json.loads(replies[1]["content"][0]["text"])
    assert verdict == {"accepted": True, "next": "call submit"}


def test_an_edit_clears_searches_and_reads_of_the_page_in_any_path_form(tmp_path):
    """Review finding N: a search of the working directory, or a read of page.md under
    another path form, may run again after an edit; a search elsewhere stays denied."""
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/r.md").write_text("report claim")
    s = _session(tmp_path)
    hooks = PA.hooks_for(s)
    pre, post = hooks["PreToolUse"][0].hooks[0], hooks["PostToolUse"][0].hooks[0]

    def denied(data):
        out = asyncio.run(pre(data, None, None))
        return out.get("hookSpecificOutput", {}).get("permissionDecision") == "deny"

    page = s.workdir / "page.md"
    calls = [
        {"tool_name": "Grep", "tool_input": {"pattern": "claim"}},
        {"tool_name": "Glob", "tool_input": {"pattern": "*.json", "path": "."}},
        {"tool_name": "Read", "tool_input": {"file_path": "page.md"}},
    ]
    staging = str(tmp_path / "staging")
    elsewhere = {"tool_name": "Grep", "tool_input": {"pattern": "claim", "path": staging}}
    for data in [*calls, elsewhere]:
        assert not denied(data) and denied(data)
    before = page.read_text()
    page.write_text("A new claim.")
    edit = {"tool_name": "Edit", "tool_input": {"file_path": str(page)}}
    asyncio.run(post(edit, None, None))
    page.write_text(before)  # the read's content hash alone would still deny it
    asyncio.run(post(edit, None, None))
    assert not any(denied(data) for data in calls)
    assert denied(elsewhere)


def test_each_session_message_reaches_the_transcript_before_the_next(tmp_path, monkeypatch):
    """Review finding O: a killed worker is charged from its transcript, so a turn that
    arrived must be on disk, not in a write buffer."""
    from types import SimpleNamespace

    from claude_agent_sdk import AssistantMessage

    seen = []

    async def query(prompt, options):
        yield AssistantMessage(content=[], model="m", usage={"input_tokens": 7})
        seen.append((tmp_path / "transcripts/k.jsonl").read_text())
        yield _result()

    monkeypatch.setattr(PA, "query", query)
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("rules")
    agent: Any = SimpleNamespace(
        config={"cli": "claude"}, store=tmp_path, root=tmp_path, effort=lambda step: None
    )
    asyncio.run(PA._drive(agent, _session(tmp_path), "k", "m", False))
    assert '"input_tokens": 7' in seen[0]


def test_a_wiki_search_does_not_make_the_session_rest_on_the_output_tree(tmp_path):
    """Review finding D: a page written after a writer searched wiki/ must not make that
    writer's finished session stale, or every replay buys it again."""
    from beril_wiki.agentic.runtime import current_dependencies

    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "wiki/concepts/b.md").write_text("A sibling page.")
    page = _page(tmp_path)
    s = PA.Session(
        dataclasses.replace(page, reads=[tmp_path / "wiki"]),
        tmp_path / "work",
        max_reviews=3,
        root=tmp_path,
    )
    (tmp_path / "work").mkdir()
    pre = PA.hooks_for(s)["PreToolUse"][0].hooks[0]
    search = {"pattern": "sibling", "path": str(tmp_path / "wiki")}
    asyncio.run(pre({"tool_name": "Grep", "tool_input": search}, None, None))
    (tmp_path / "wiki/concepts/a.md").write_text("The page this session wrote.")
    assert current_dependencies(tmp_path, s.deps) == s.deps


def _ledger_agent(tmp_path, monkeypatch, model="m"):
    """A real ledger and PA.run; the SDK session is the caller's fake _drive."""
    from types import SimpleNamespace

    from beril_wiki.agentic.runtime import Ledger

    monkeypatch.setattr(PA, "check_auth", lambda cli: None)
    monkeypatch.setattr(PA, "run", REAL_RUN)  # run() retries a refusal through itself
    (tmp_path / "contract").mkdir(exist_ok=True)
    (tmp_path / "contract/AGENTS.md").write_text("rules")
    (tmp_path / "staging").mkdir(exist_ok=True)
    ledger = Ledger(tmp_path / "jobs.sqlite", "run", 10**9, 99, 1)
    agent: Any = SimpleNamespace(
        config={"model": model, "cli": "claude"},
        root=tmp_path,
        store=tmp_path,
        ledger=ledger,
        jobs=[],
        effort=lambda step: None,
    )
    return agent


USAGE = {"input_tokens": 1, "output_tokens": 1}


def test_a_cached_page_is_rewritten_when_a_source_its_reviewer_read_changes(tmp_path, monkeypatch):
    """Review finding B: the reviewer's reads key the cached page as the writer's do."""
    from beril_wiki.agentic.runtime import file_hash

    agent = _ledger_agent(tmp_path, monkeypatch)
    source = tmp_path / "staging/r.md"
    source.write_text("value=1")

    def review(text, meta):
        job = f"review-{len(agent.jobs)}"
        agent.jobs.append(job)
        agent.ledger.reserve(job, "write/concepts/a.md/science-review", "gpt-6-luna")
        agent.ledger.finish(job, "{}", USAGE, "", {"staging/r.md": file_hash(source)})
        return []

    drives = []

    async def drive(agent_, session, key, model, resumed):
        assert not resumed and (session.workdir / "page.md").read_text() == "Old body."
        drives.append(key)
        (session.workdir / "page.md").write_text("Claims value=1. [src: x]")
        assert session.do_check()["passed"] and session.do_review()["accepted"]
        assert session.do_submit()["accepted"]
        return "done", USAGE, 0.0, "", ""

    monkeypatch.setattr(PA, "_drive", drive)
    page = _page(tmp_path, review=review)
    REAL_RUN(agent, page, tmp_path / "work")
    REAL_RUN(agent, page, tmp_path / "work")
    assert len(drives) == 1  # unchanged sources: the cached page
    source.write_text("value=2")
    REAL_RUN(agent, page, tmp_path / "work")
    assert len(drives) == 2


@pytest.mark.parametrize("reader", ["writer", "reviewer"])
@pytest.mark.parametrize("stop", ["crash", "reviewer_stop"])
def test_a_crashed_session_cannot_restore_approvals_after_its_source_changes(
    tmp_path, monkeypatch, reader, stop
):
    from beril_wiki.agentic.runtime import WorkflowError, file_hash

    agent = _ledger_agent(tmp_path, monkeypatch)
    source = tmp_path / "staging/r.md"
    source.write_text("value=1")
    reviewed = []

    def review(text, meta):
        reviewed.append(source.read_text())
        if reader == "reviewer":
            key = f"review-{len(agent.jobs)}"
            agent.jobs.append(key)
            agent.ledger.reserve(key, "write/concepts/a.md/science-review", "gpt-6-luna")
            agent.ledger.finish(key, "{}", USAGE, "", {"staging/r.md": file_hash(source)})
        if stop == "reviewer_stop" and len(reviewed) == 1:
            raise WorkflowError("reviewer transport failed")
        return []

    resumed = []

    async def drive(agent_, session, key, model, continuing):
        resumed.append(continuing)
        if len(resumed) == 1:
            (session.workdir / "page.md").write_text("A good claim: value=1. [src: x]")
            if reader == "writer":
                session.deps["staging/r.md"] = file_hash(source)
            assert session.do_check()["passed"]
            try:
                assert session.do_review()["accepted"]
            except WorkflowError:
                return "writer exited", USAGE, 0.01, "", ""
            raise RuntimeError("crashed before submit")
        # A changed source requires both host gates before the resumed job can submit.
        assert (session.workdir / "page.md").read_text() == "Old body."
        assert session.do_submit()["missing"] == ["check", "review"]
        assert not session.full_review and session.reviews == 0
        (session.workdir / "page.md").write_text("A good claim: value=2. [src: x]")
        session.deps["staging/r.md"] = file_hash(source)
        assert session.do_check()["passed"] and session.do_review()["accepted"]
        assert session.do_submit()["accepted"]
        return "done", USAGE, 0.01, "", ""

    monkeypatch.setattr(PA, "_drive", drive)
    page = _page(tmp_path, review=review)
    error = RuntimeError if stop == "crash" else WorkflowError
    message = "crashed before submit" if stop == "crash" else "reviewer transport failed"
    with pytest.raises(error, match=message):
        REAL_RUN(agent, page, tmp_path / "work")
    agent.ledger.reconcile_stale(tmp_path / "transcripts")
    source.write_text("value=2")
    text, _ = REAL_RUN(agent, page, tmp_path / "work")
    assert text == "A good claim: value=2. [src: x]"
    assert resumed == [False, False] and reviewed == ["value=1", "value=2"]


def test_a_later_pass_goes_straight_to_the_model_that_answered_a_refusal(tmp_path, monkeypatch):
    """Review finding P: a writer that refused one pass of a page is not asked again for
    the next pass, as Runtime.ask already rules for other jobs."""
    agent = _ledger_agent(tmp_path, monkeypatch, model="claude-haiku-5-5")
    models = []

    async def drive(agent_, session, key, model, resumed):
        models.append(model)
        assert not resumed and (session.workdir / "page.md").read_text() == "Old body."
        (session.workdir / "page.md").write_text("A good claim. [src: x]")
        assert session.do_check()["passed"] and session.do_review()["accepted"]
        if model == "claude-haiku-5-5":
            return "I can't help with that.", USAGE, 0.01, "", "claude-sonnet-5-5"
        assert session.do_submit()["accepted"]
        return "done", USAGE, 0.0, "", ""

    monkeypatch.setattr(PA, "_drive", drive)
    for n in (0, 1):
        page = dataclasses.replace(_page(tmp_path), step=f"write/concepts/a.md/pass/{n}")
        REAL_RUN(agent, page, tmp_path / f"work{n}")
    assert models == ["claude-haiku-5-5", "claude-sonnet-5-5", "claude-sonnet-5-5"]


def test_a_re_review_that_crashes_cannot_restore_the_voided_approval(tmp_path):
    """PR #21 review: the approval a re-review voids is voided on disk before the
    reviewer runs, so an operational error mid-review leaves nothing to resume."""
    from beril_wiki.agentic.runtime import WorkflowError

    verdicts: list = [[], WorkflowError("Codex transport failed")]

    def review(text, meta):
        verdict = verdicts.pop(0)
        if isinstance(verdict, Exception):
            raise verdict
        return verdict

    s = _session(tmp_path, review=review)
    (s.workdir / "page.md").write_text("A good claim. [src: x]")
    assert s.do_check()["passed"] and s.do_review()["accepted"]
    with pytest.raises(WorkflowError):
        s.do_review()
    resumed = PA.Session(s.page, s.workdir, max_reviews=3)
    assert PA._restore(resumed)
    assert resumed.do_submit()["missing"] == ["review"]
    assert resumed.reviews == 2  # the failed review still counts against the limit


@pytest.mark.parametrize("ending", ["review_limit", "stage_stop", "writer_stop"])
def test_a_decided_or_exhausted_session_starts_fresh_on_retry(tmp_path, monkeypatch, ending):
    from beril_wiki.agentic.runtime import WorkflowError

    agent = _ledger_agent(tmp_path, monkeypatch)
    attempts = []

    def review(text, meta):
        if len(attempts) == 1:
            if ending == "review_limit":
                raise WorkflowError("reviewer transport failed on last allowance")
            if ending == "stage_stop":
                raise CandidateError("no scientific progress", ["unsupported claim"])
        return []

    async def drive(agent_, session, key, model, resumed):
        attempts.append(resumed)
        assert not resumed and (session.workdir / "page.md").read_text() == "Old body."
        assert session.reviews == 0 and session.do_submit()["missing"] == ["check", "review"]
        (session.workdir / "page.md").write_text("A good claim. [src: x]")
        assert session.do_check()["passed"]
        try:
            verdict = session.do_review()
        except WorkflowError:
            return "writer exited", USAGE, 0.01, "", ""
        if len(attempts) > 1:
            assert verdict["accepted"] and session.do_submit()["accepted"]
        return "done", USAGE, 0.01, "", ""

    monkeypatch.setattr(PA, "_drive", drive)
    page = _page(tmp_path, review=review)
    error = WorkflowError if ending == "review_limit" else PA.Exhausted
    with pytest.raises(error):
        REAL_RUN(agent, page, tmp_path / "work", max_reviews=1)
    assert json.loads((tmp_path / "work/state.json").read_text())["ended"]
    assert REAL_RUN(agent, page, tmp_path / "work", max_reviews=1)[0] == "A good claim. [src: x]"
    assert attempts == [False, False]


@pytest.mark.parametrize(
    "ending", ["success", "refused", "empty", "transport", "partial_transport", "unknown_usage"]
)
def test_review_admission_failure_survives_the_writer_exit(tmp_path, monkeypatch, ending):
    from claude_agent_sdk import AssistantMessage, SystemMessage
    from mcp.types import CallToolRequest, CallToolRequestParams

    from beril_wiki.agentic.runtime import WorkflowError

    agent = _ledger_agent(tmp_path, monkeypatch, model="claude-haiku-5-5")
    agent.ledger.caps = {"max_usd": 100}
    reason = "budget admission refused: jobs=56, effective=5090060, inflight=1"
    failure = WorkflowError(reason)
    reviews = []

    def review(text, meta):
        reviews.append(text)
        raise failure

    configured = {}
    real_server = PA.create_sdk_mcp_server

    def server(name, tools):
        mcp = real_server(name, tools=tools)
        configured["handler"] = mcp["instance"].request_handlers[CallToolRequest]
        return mcp

    monkeypatch.setattr(PA, "create_sdk_mcp_server", server)
    replies = []

    async def query(prompt, options):
        (tmp_path / "work/page.md").write_text("A good claim. [src: x]")
        for name in ("check", "review", "review"):
            reply = await configured["handler"](
                CallToolRequest(
                    method="tools/call", params=CallToolRequestParams(name=name, arguments={})
                )
            )
            replies.append(reply.root)
        if ending == "partial_transport":
            yield AssistantMessage(
                content=[], model="m", usage={"input_tokens": 7, "output_tokens": 3}
            )
        if ending in ("transport", "partial_transport"):
            raise RuntimeError("writer transport failed after the reviewer stopped")
        if ending == "empty":
            return
        if ending == "refused":
            yield SystemMessage(
                subtype="model_refusal_fallback", data={"fallback_model": "claude-sonnet-5-5"}
            )
        result = _result(cost=0.01)
        yield dataclasses.replace(result, usage=None) if ending == "unknown_usage" else result

    monkeypatch.setattr(PA, "query", query)
    with pytest.raises(WorkflowError, match=reason) as caught:
        REAL_RUN(agent, _page(tmp_path, review=review), tmp_path / "work")
    assert caught.value is failure
    assert not isinstance(caught.value, CandidateError)
    assert len(reviews) == 1  # MCP caught both errors, but the reviewer ran only once
    assert [reply.isError for reply in replies] == [False, True, True]
    status = "unknown" if ending in ("empty", "transport", "unknown_usage") else "failed"
    tokens = None if status == "unknown" else 10 if ending == "partial_transport" else 2
    cost = (
        PA.budget_for(_page(tmp_path).messages)[1]
        if ending in ("empty", "transport", "partial_transport")
        else 0.01
    )
    assert agent.ledger.db.execute("SELECT status,error,tokens,cost FROM jobs").fetchall() == [
        (status, reason, tokens, cost)
    ]
    saved = json.loads((tmp_path / "work/state.json").read_text())
    assert saved["checked"] and not saved["reviewed"] and not saved["ended"]
    draft = "A good claim. [src: x]"

    def retry_review(text, meta):
        reviews.append(text)
        return []

    async def retry_drive(agent_, session, key, model, resumed):
        assert resumed and (session.workdir / "page.md").read_text() == draft
        assert session.reviews == 1 and session.do_submit()["missing"] == ["review"]
        assert session.do_review()["accepted"] and session.do_submit()["accepted"]
        return "done", USAGE, 0.02, "", ""

    monkeypatch.setattr(PA, "_drive", retry_drive)
    page = _page(tmp_path, review=retry_review)
    if status == "unknown":
        with pytest.raises(WorkflowError, match="unknown usage"):
            REAL_RUN(agent, page, tmp_path / "work")
        assert (tmp_path / "work/page.md").read_text() == draft
        assert agent.ledger.db.execute("SELECT count(*) FROM jobs").fetchone() == (1,)
        agent.ledger.account(agent.jobs[0], 5)
    assert REAL_RUN(agent, page, tmp_path / "work")[0] == draft
    assert reviews == [draft, draft]
    assert agent.ledger.db.execute("SELECT cost FROM jobs ORDER BY rowid").fetchall() == [
        (cost,),
        (0.02,),
    ]
    assert json.loads((tmp_path / "work/state.json").read_text())["ended"]
