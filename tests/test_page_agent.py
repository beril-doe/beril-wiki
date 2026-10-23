"""Offline checks for the page agent's host state and hooks (no model calls)."""

import asyncio
import json

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
    again = PA.Session(s.page, s.workdir, max_reviews=3)
    assert PA._restore(again) and again.checked == s.checked
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

    agent = SimpleNamespace(
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
        agent = SimpleNamespace(
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
    agent = SimpleNamespace(
        config={"cli": "claude"}, store=tmp_path, root=tmp_path, effort=lambda step: None
    )
    session = _session(tmp_path)
    _, usage, cost, error, refused = asyncio.run(PA._drive(agent, session, "k", "m", False))
    assert (cost, error, refused) == (0.5, "SDK ended: error_max_turns", "")
