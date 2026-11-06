"""Offline checks for the pilot's outcome and judgement bookkeeping (no model calls)."""

import json

import pytest

from beril_wiki.agentic import pilot as P
from beril_wiki.agentic import runtime as R


def _tree(root, pages):
    for page, text in pages.items():
        path = root / "wiki" / page
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)


def test_outcomes_follow_what_the_host_did(tmp_path):
    tree, cell = tmp_path / "tree", tmp_path / "cell"
    pages = {"concepts/a.md": "old a", "concepts/b.md": "old b", "concepts/c.md": "old c"}
    _tree(tree, pages)
    _tree(cell / "root", pages | {"concepts/a.md": "new a", "concepts/b.md": "new b"})
    (cell / "salvaged.json").write_text(
        json.dumps({"write/concepts/b.md/pass/1": {"removed": ["s:0:1", "s:0:2"]}})
    )
    (cell / "failures.json").write_text(json.dumps({"concepts/c.md": {"step": "write"}}))
    got = P.outcomes(tree, cell, list(pages) + ["concepts/d.md"])
    assert got["concepts/a.md"] == {"status": "written", "dropped": [], "written": True}
    # Accepted review verdicts on an earlier pass do not make a salvaged page accepted.
    assert got["concepts/b.md"]["status"] == "salvaged"
    assert got["concepts/b.md"]["dropped"] == ["s:0:1", "s:0:2"]
    assert got["concepts/c.md"]["status"] == "failed"
    assert got["concepts/d.md"]["status"] == "not run"  # no writer was given it


def test_judge_scores_both_orders_and_records_refusals_as_unjudged(tmp_path, monkeypatch):
    scratch = tmp_path
    cell = scratch / "cells/x"
    _tree(scratch / "derived", {"concepts/a.md": "baseline a", "concepts/r.md": "baseline r"})
    _tree(cell / "root", {"concepts/a.md": "candidate a", "concepts/r.md": "candidate r"})
    (cell / "packs").mkdir(parents=True)
    for page in ("a", "r"):
        (cell / "packs" / f"write__concepts__{page}.md.json").write_text(
            json.dumps({"messages": [{"role": "system", "content": f"evidence for {page}"}]})
        )
    outcome = {"status": "written", "dropped": [], "written": True}
    (cell / "manifest.json").write_text(
        json.dumps(
            {
                "kind": "integrated",
                "outcomes": {"concepts/a.md": outcome, "concepts/r.md": outcome},
            }
        )
    )

    def ask(self, messages, step, *, model=None):
        task = json.loads(messages[0]["content"].split("\n", 1)[1])
        assert task["writer_input"]
        if "concepts/r.md" in step:
            raise R.JobFailed("content flagged for possible biological risk")
        candidate = "A" if task["candidate_A"].startswith("candidate") else "B"
        other = "B" if candidate == "A" else "A"
        return json.dumps(
            {
                "better": candidate,
                "fidelity": {candidate: 8, other: 7},
                "coverage": {candidate: 6, other: 6},
                "clarity": {candidate: 5, other: 7},
            }
        )

    monkeypatch.setattr(R.Runtime, "ask", ask)
    config = {"model": "m", "step_models": {"review": "gpt-x"}, "run": "pilot", "reserve_tokens": 1}
    verdicts = P.judge(scratch, "x", config | {"max_tokens": 10, "max_jobs": 10})
    assert verdicts["concepts/a.md"]["status"] == "judged"
    assert verdicts["concepts/a.md"]["fidelity_delta"] == 1
    assert verdicts["concepts/a.md"]["clarity_delta"] == -2
    assert all(o["winner"] == "candidate" for o in verdicts["concepts/a.md"]["orders"])
    assert verdicts["concepts/r.md"]["status"] == "unjudged"
    assert "fidelity_delta" not in verdicts["concepts/r.md"]


def test_a_page_without_kept_writer_input_is_unjudged_not_scored(tmp_path):
    cell = tmp_path / "cells/x"
    _tree(tmp_path / "derived", {"concepts/a.md": "baseline"})
    _tree(cell / "root", {"concepts/a.md": "candidate"})
    (cell / "manifest.json").write_text(
        json.dumps(
            {
                "kind": "integrated",
                "outcomes": {
                    "concepts/a.md": {"status": "written", "dropped": [], "written": True}
                },
            }
        )
    )
    config = {"model": "m", "step_models": {"review": "gpt-x"}, "run": "p", "reserve_tokens": 1}
    verdicts = P.judge(tmp_path, "x", config | {"max_tokens": 10, "max_jobs": 10})
    assert verdicts["concepts/a.md"] == {"status": "unjudged", "reason": "no writer input kept"}


def _pack(cell, step, evidence_id):
    (cell / "packs").mkdir(parents=True, exist_ok=True)
    content = P.PACKED + json.dumps({"existing": "", "evidence": [{"id": evidence_id}]})
    (cell / "packs" / f"{step.replace('/', '__')}.json").write_text(
        json.dumps({"messages": [{"role": "system", "content": content}]})
    )


def test_writer_input_takes_exactly_this_pages_packs(tmp_path):
    cell = tmp_path / "cell"
    _pack(cell, "write/entities/urea.md", "E-urea")
    _pack(cell, "write/entities/urea.md/pass/1", "E-urea-2")
    _pack(cell, "write/entities/urease-complex.md", "E-urease")
    got = P.writer_input(cell, "entities/urea.md")
    assert [e["id"] for e in got[0]["evidence"]] == ["E-urea", "E-urea-2"]


def test_a_verdict_without_its_scores_is_unjudged(tmp_path, monkeypatch):
    cell = tmp_path / "cells/x"
    _tree(tmp_path / "derived", {"concepts/a.md": "baseline"})
    _tree(cell / "root", {"concepts/a.md": "candidate"})
    _pack(cell, "write/concepts/a.md", "E1")
    written = {"status": "written", "dropped": [], "written": True}
    (cell / "manifest.json").write_text(
        json.dumps({"kind": "integrated", "outcomes": {"concepts/a.md": written}})
    )
    monkeypatch.setattr(R.Runtime, "ask", lambda self, messages, step, *, model=None: "{}")
    config = {"model": "m", "step_models": {"review": "gpt-x"}, "run": "p", "reserve_tokens": 1}
    verdicts = P.judge(tmp_path, "x", config | {"max_tokens": 10, "max_jobs": 10})
    assert verdicts["concepts/a.md"]["status"] == "unjudged"


def test_a_failing_cell_still_writes_its_manifest_and_cells_take_a_lock(tmp_path, monkeypatch):
    import fcntl

    scratch = tmp_path
    (scratch / ".agentic").mkdir()
    _tree(scratch / "derived", {"concepts/a.md": "baseline"})
    config = {"model": "m", "run": "p", "reserve_tokens": 1, "cli": "claude"}

    def crash(*args, **kwargs):
        raise RuntimeError("SDK process died")

    monkeypatch.setattr(P, "run_stage", crash)
    manifest = P.run_cell(scratch, "d", "derived", ["conflicts/c"], config)
    assert manifest["error"].startswith("RuntimeError: SDK process died")
    assert (scratch / "cells/d/manifest.json").exists()
    with (scratch / ".agentic/pilot.lock").open("w") as held:
        fcntl.flock(held, fcntl.LOCK_EX)
        with pytest.raises(R.WorkflowError, match="another pilot cell is running"):
            P.run_cell(scratch, "e", "derived", ["conflicts/c"], config)


def test_report_groups_split_cells_and_accepts_short_names(tmp_path):
    from beril_wiki.agentic.runtime import Ledger

    Ledger(tmp_path / ".agentic/jobs.sqlite", "p", 10, 10, 1)
    for name in ("x", "int-haiku", "int-haiku-b"):
        cell = tmp_path / "cells" / name
        cell.mkdir(parents=True)
        (cell / "manifest.json").write_text(
            json.dumps(
                {
                    "cell": name,
                    "kind": "integrated",
                    "models": {},
                    "seconds": 0,
                    "error": "",
                    "usage": {},
                    "detail": {},
                    "rows": [1, 0],
                    "outcomes": {},
                }
            )
        )
    assert set(P.report(tmp_path)["models"]) == {"x", "int-haiku"}


def test_cell_usage_leaves_out_a_judge_running_beside_it():
    import sqlite3
    from types import SimpleNamespace

    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE jobs (step, model, status, usage, cost, error, tokens)")
    db.executemany(
        "INSERT INTO jobs VALUES (?,?,?,?,?,?,?)",
        [
            ("write/a.md/review", "gpt-6-luna", "done", "{}", None, "", 100),
            ("pilot/judge/other/a.md/baseline-first", "gpt-6-sol", "done", "{}", None, "", 900),
            ("write/a.md", "claude-haiku-5-5", "done", "{}", 0.5, "", 10),
        ],
    )
    total = P.usage(SimpleNamespace(ledger=SimpleNamespace(db=db)), 1)
    assert (total["codex_tokens"], total["claude_usd"], total["jobs"]) == (100, 0.5, 2)


def _finding(eid, start, end, claim):
    return {
        "id": eid,
        "source": eid.split(":")[0],
        "start": start,
        "end": end,
        "claim": claim,
        "quote": "q",
        "kind": "finding",
    }


def test_extraction_overlap_counts_shared_quotes_and_numbers():
    accepted = [
        _finding("s:0:0", 0, 10, "1,200 genes, 45% core"),
        _finding("s:0:1", 20, 30, "p=0.14"),
    ]
    new = [_finding("s:0:0", 5, 15, "1200 genes and 45% core")]
    got = P.extraction_overlap(accepted, new)
    assert got == {
        "accepted": 2,
        "findings": 1,
        "quote_recall": 0.25,  # 5 of the 20 accepted characters
        "quote_precision": 0.5,
        "number_recall": 0.667,  # 1200 and 45% of 1200, 45% and 0.14
    }
    assert P.extraction_overlap([], new)["quote_recall"] is None


def _extraction_scratch(tmp_path, monkeypatch, accepted, extracted, gap=False):
    scratch = tmp_path
    (scratch / ".agentic").mkdir()
    staging = scratch / "integrated/staging"
    staging.mkdir(parents=True)
    (staging / "s.md").write_text("passage text " * 10)
    monkeypatch.setattr(P, "saved_plan", lambda store: (accepted, None, None))

    def extract(root, agent, names):
        if gap:
            (agent.store / "extraction-gaps.json").write_text(json.dumps({"extract/s.md/0": []}))
        coverage = [
            {
                "source": "s.md",
                "start": 0,
                "end": 130,
                "context_end": 130,
                "evidence": [f["id"] for f in extracted],
            }
        ]
        return extracted, coverage

    monkeypatch.setattr(P, "extract_sources", extract)
    config = {"model": "m", "run": "p", "reserve_tokens": 1, "cli": "claude"}
    return P.run_cell(scratch, "x", "extraction", ["s.md"], config)


def test_an_extraction_cell_compares_with_the_accepted_records(tmp_path, monkeypatch):
    accepted = [_finding("s:0:0", 0, 10, "12 genes")]
    manifest = _extraction_scratch(
        tmp_path, monkeypatch, accepted, [_finding("s:0:0", 0, 10, "12 genes")], gap=True
    )
    assert manifest["error"] == ""
    assert manifest["detail"]["s.md"]["quote_recall"] == 1.0
    # Outcomes are per chunk, keyed by step, and a gap the reviewer left is recorded.
    assert manifest["outcomes"] == {
        "extract/s.md/0": {"status": "gap", "dropped": [], "written": True, "findings": 1}
    }
    assert (tmp_path / "cells/x/extraction-gaps.json").exists()
    assert not (tmp_path / ".agentic/extraction-gaps.json").exists()


def test_the_judge_compares_extracted_chunks_on_precision(tmp_path, monkeypatch):
    accepted = [_finding("s:0:0", 0, 10, "accepted claim")]
    _extraction_scratch(tmp_path, monkeypatch, accepted, [_finding("s:0:0", 0, 10, "new claim")])
    seen = []

    def ask(self, messages, step, *, model=None):
        rubric, raw = messages[0]["content"].split("\n", 1)
        task = json.loads(raw)
        seen.append((step, model))
        assert rubric == P.EXTRACTION_RUBRIC and task["passage"].startswith("passage text")
        new = "A" if task["candidate_A"][0]["claim"] == "new claim" else "B"
        old = "B" if new == "A" else "A"
        return json.dumps(
            {
                "better": old,
                "fidelity": {new: 7, old: 8},
                "coverage": {new: 6, old: 6},
                "precision": {new: 9, old: 6},
            }
        )

    monkeypatch.setattr(R.Runtime, "ask", ask)
    config = {"model": "m", "step_models": {"review": "claude-j"}, "run": "p", "reserve_tokens": 1}
    verdicts = P.judge(tmp_path, "x", config | {"max_tokens": 10, "max_jobs": 10})
    got = verdicts["extract/s.md/0"]
    assert got["status"] == "judged"
    assert (got["fidelity_delta"], got["precision_delta"]) == (-1, 3)
    assert "clarity_delta" not in got
    assert [s for s, _ in seen] == [
        "pilot/judge/x/extract/s.md/0/baseline-first",
        "pilot/judge/x/extract/s.md/0/candidate-first",
    ]


def test_an_extraction_cell_refuses_a_source_without_accepted_records(tmp_path, monkeypatch):
    accepted = [_finding("other:0:0", 0, 10, "12 genes")]
    manifest = _extraction_scratch(tmp_path, monkeypatch, accepted, [_finding("s:0:0", 0, 10, "x")])
    assert "no accepted extraction of s.md" in manifest["error"]
    assert manifest["outcomes"] == {}


def test_a_failing_source_keeps_the_sources_extracted_before_it(tmp_path, monkeypatch):
    accepted = [_finding("s:0:0", 0, 10, "12 genes"), _finding("t:0:0", 0, 10, "3 genes")]
    scratch = tmp_path
    (scratch / ".agentic").mkdir()
    (scratch / "integrated/staging").mkdir(parents=True)
    monkeypatch.setattr(P, "saved_plan", lambda store: (accepted, None, None))

    def extract(root, agent, names):
        if names == ["t.md"]:
            raise R.JobFailed("Codex token cap reached")
        coverage = [
            {"source": "s.md", "start": 0, "end": 10, "context_end": 10, "evidence": ["s:0:0"]}
        ]
        return [_finding("s:0:0", 0, 10, "12 genes")], coverage

    monkeypatch.setattr(P, "extract_sources", extract)
    config = {"model": "m", "run": "p", "reserve_tokens": 1, "cli": "claude"}
    manifest = P.run_cell(scratch, "x", "extraction", ["s.md", "t.md"], config)
    assert "Codex token cap reached" in manifest["error"]
    assert list(manifest["outcomes"]) == ["extract/s.md/0"]
