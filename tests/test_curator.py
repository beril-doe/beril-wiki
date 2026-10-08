"""The schedule runs stale stages in dependency order; the host enforces completion."""

import json
from typing import cast

import pytest

from beril_wiki.agentic.runtime import Runtime, WorkflowError


def test_schedule_runs_stale_stages_in_table_order(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    (tmp_path / "jobs").mkdir()
    calls = []

    class Agent:
        root = tmp_path
        store = tmp_path / "jobs"
        config = {"model": "fixture"}

        def ask(self, task, step):
            raise AssertionError("the schedule makes no decision calls")

    monkeypatch.setattr(C, "propose_topics", lambda root, agent: calls.append("propose"))
    monkeypatch.setattr(C, "load_groups", lambda root: [])

    def refresh(name, args):
        calls.append(name)
        if name == "topics":
            (tmp_path / "wiki/topics").mkdir(exist_ok=True)
            (tmp_path / "wiki/topics/a.md").write_text("# A\n\nSupported knowledge.\n")
        if name == "literature":
            path = tmp_path / "wiki/topics/a.md"
            path.write_text(path.read_text() + "\n## Literature Context\n\nPaper evidence.\n")

    state = C.curate(tmp_path, cast(Runtime, Agent()), [], refresh, {})
    assert calls == [
        "extras",
        "names-core",
        "conflicts",
        "propose",
        "topics",
        "literature",
        "authors",
    ]
    assert set(state) == set(C.EDITORIAL)
    # Literature owns its section; its insertion must not dirty topic synthesis.
    assert C.pending_actions(tmp_path, state, Agent.config, integrated=True) == []
    receipts = json.loads((tmp_path / "jobs/curator-receipts.json").read_text())
    assert [r["action"] for r in receipts] == ["conflicts", "topics", "literature", "authors"]
    assert all(r["result"] == "completed" for r in receipts)
    calls.clear()
    # Only stale stages and their dependents run again.
    (tmp_path / "wiki/concepts/new.md").write_text("# New\n")
    C.curate(tmp_path, cast(Runtime, Agent()), [], refresh, state)
    assert calls == [
        "extras",
        "names-core",
        "conflicts",
        "propose",
        "topics",
        "literature",
        "authors",
    ]


def test_schedule_integrates_changed_sources_first(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "jobs").mkdir()
    calls = []

    class Agent:
        root = tmp_path
        store = tmp_path / "jobs"
        config = {"model": "fixture"}

    monkeypatch.setattr(C, "load_groups", lambda root: [])
    monkeypatch.setattr(C, "propose_topics", lambda root, agent: None)
    monkeypatch.setattr(
        C, "compile_batch", lambda root, agent, names: calls.append(("integrate", names))
    )
    C.curate(tmp_path, cast(Runtime, Agent()), ["a__REPORT.md"], lambda n, a: calls.append(n), {})
    assert calls[:6] == [
        "extras",
        "names-core",
        ("integrate", ["a__REPORT.md"]),
        "entities",
        "names-core",
        "extras",
    ]
    assert calls[6:] == ["conflicts", "topics", "literature", "authors"]


def test_stage_made_stale_by_integration_still_runs(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "wiki/summaries").mkdir(parents=True)
    (tmp_path / "wiki/concepts").mkdir()
    (tmp_path / "jobs").mkdir()
    (tmp_path / "wiki/summaries/a__REPORT.md").write_text("old summary")
    calls = []

    class Agent:
        root = tmp_path
        store = tmp_path / "jobs"
        config = {"model": "fixture"}

    monkeypatch.setattr(C, "load_groups", lambda root: [])
    monkeypatch.setattr(C, "propose_topics", lambda root, agent: None)
    prior = {name: C.stage_snapshot(tmp_path, name, Agent.config) for name in C.EDITORIAL}
    assert C.pending_actions(tmp_path, prior, Agent.config, integrated=True) == []

    def integrate(root, agent, names):
        (tmp_path / "wiki/summaries/a__REPORT.md").write_text("revised summary")

    monkeypatch.setattr(C, "compile_batch", integrate)
    state = C.curate(
        tmp_path, cast(Runtime, Agent()), ["a__REPORT.md"], lambda n, a: calls.append(n), prior
    )
    assert "authors" in calls and "conflicts" not in calls
    assert C.pending_actions(tmp_path, state, Agent.config, integrated=True) == []


def test_literature_changes_only_its_owned_fingerprint(tmp_path):
    from beril_wiki.agentic import curator as C

    folder = tmp_path / "wiki/topics"
    folder.mkdir(parents=True)
    path = folder / "a.md"
    path.write_text("# A\n\nLead.\n\n## Findings\n\nEvidence.\n")
    before = {n: C.stage_snapshot(tmp_path, n, {"model": "fixture"}) for n in C.EDITORIAL}
    path.write_text(
        "# A\n\nLead.\n\n## Literature Context\n\nA paper.\n\n## Findings\n\nEvidence.\n"
    )
    after = {n: C.stage_snapshot(tmp_path, n, {"model": "fixture"}) for n in C.EDITORIAL}
    assert before["topics"] == after["topics"]
    assert before["literature"] != after["literature"]


def test_dirty_output_invalidates_only_its_page_cache(tmp_path):
    from beril_wiki.agentic.curator import invalidate_outputs

    (tmp_path / "state").mkdir()
    path = tmp_path / "state/topics-state.json"
    path.write_text(json.dumps({"a": "a-hash", "b": "b-hash", "__names__": {}}))
    before = {
        "semantic": "v1",
        "outputs": {"wiki/topics/a.md": "a", "wiki/topics/b.md": "b", "wiki/index.md": "old"},
    }
    after = {
        "semantic": "v1",
        "outputs": {"wiki/topics/a.md": "changed", "wiki/topics/b.md": "b", "wiki/index.md": "new"},
    }
    assert invalidate_outputs(tmp_path, "topics", before, after) == ["--refresh-home"]
    assert json.loads(path.read_text()) == {"b": "b-hash", "__names__": {}}
    invalidate_outputs(tmp_path, "topics", before, after | {"semantic": "v2"})
    assert json.loads(path.read_text()) == {"__names__": {}}


def test_search_cli_reads_accepted_wiki_and_refuses_pending_promotion(
    tmp_path, monkeypatch, capsys
):
    import sys

    from beril_wiki.agentic.__main__ import main

    path = tmp_path / "wiki/concepts/a.md"
    path.parent.mkdir(parents=True)
    path.write_text("# Yield\n\nYield was 42%. [src: report-a]\n")
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "search", "yield"])
    assert main() == 0
    result = json.loads(capsys.readouterr().out)
    assert result["matches"][0]["path"] == "wiki/concepts/a.md"
    assert result["matches"][0]["sources"] == ["report-a"]
    assert result["exhausted"] is True
    (tmp_path / ".agentic/promotion.json").write_text("{}")
    assert main() == 1
    assert "promotion pending" in capsys.readouterr().out


def test_failed_editorial_action_keeps_receipt(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "jobs").mkdir()

    class Agent:
        store = tmp_path / "jobs"
        config = {"model": "fixture"}

    monkeypatch.setattr(C, "load_groups", lambda root: [])

    def refresh(name, args):
        if name == "conflicts":
            raise WorkflowError("stage stopped")

    with pytest.raises(WorkflowError, match="stage stopped"):
        C.curate(tmp_path, cast(Runtime, Agent()), [], refresh, {})
    receipt = json.loads((tmp_path / "jobs/curator-receipts.json").read_text())[-1]
    assert receipt["result"] == "failed" and receipt["action"] == "conflicts"
    assert "conflicts" in receipt["pending"]


def test_literature_page_cache_converges_after_real_splice(tmp_path, monkeypatch):
    from beril_wiki.stages import literature as L

    (tmp_path / "wiki/topics").mkdir(parents=True)
    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Cite evidence.")
    page = tmp_path / "wiki/topics/a.md"
    page.write_text("# Yield\n\nLead.\n## Findings\n\nEvidence.")
    monkeypatch.setattr(L, "ROOT", tmp_path)
    monkeypatch.setattr(L, "configured", lambda: True)
    monkeypatch.setattr(L.sys, "argv", ["literature"])
    monkeypatch.setattr(L.C, "_failures", [])
    monkeypatch.setattr(L, "fetch_candidates", lambda queries: {"1": "Title. ABSTRACT: Evidence."})
    calls = []

    def reply(messages, step):
        calls.append(step)
        if step.endswith("queries"):
            return '{"queries": ["yield"]}'
        return "## Literature Context\n\nExternal context. " + (
            "[PMID 1](https://pubmed.ncbi.nlm.nih.gov/1/) " + "Evidence is cited. " * 100
        )

    monkeypatch.setattr(L.C, "llm", reply)
    monkeypatch.setattr("beril_wiki.agentic.prose.ask", reply)
    assert L.main(tmp_path) == 0
    assert "Literature Context" in page.read_text()
    assert L.main(tmp_path) == 0
    assert calls == ["lit/a/queries", "lit/a/section"]


def test_pubmed_pacing_spaces_starts_without_holding_the_lock(monkeypatch):
    import threading

    from beril_wiki.stages import literature as L

    clock = [100.0]
    monkeypatch.setattr(L.time, "monotonic", lambda: clock[0])
    slept = []
    monkeypatch.setattr(L.time, "sleep", lambda s: slept.append(round(s, 2)))
    L._next_request[0] = 0.0
    L.pace()
    L.pace()
    assert slept == [0.0, 0.4] and not L.NCBI.locked()
    held = threading.Event()
    with L.NCBI:
        held.set()
    assert held.is_set()
