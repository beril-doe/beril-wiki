"""The curator chooses actions; the host enforces completion and replay bounds."""

import json
from typing import cast

import pytest

from beril_wiki.agentic.runtime import Runtime, WorkflowError


@pytest.mark.parametrize(
    "order",
    [
        ["authors", "conflicts", "topics", "literature", "finish"],
        ["conflicts", "topics", "literature", "authors", "finish"],
    ],
)
def test_curator_accepts_independent_action_orders(tmp_path, monkeypatch, order):
    from beril_wiki.agentic import curator as C

    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    (tmp_path / "jobs").mkdir()
    actions = iter(order)
    calls = []

    class Agent:
        root = tmp_path
        store = tmp_path / "jobs"
        config = {"max_actions": 8, "model": "fixture"}

        def ask(self, task, step):
            assert len(json.dumps(task)) < 10000
            return json.dumps({"action": next(actions), "reason": "Maintain changed knowledge"})

    monkeypatch.setattr(C, "propose_topics", lambda root, agent: None)
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
    assert [x for x in calls if x in C.EDITORIAL] == order[:-1]
    assert set(state) == set(C.EDITORIAL)
    # Literature owns its section; its insertion must not dirty topic synthesis.
    assert C.pending_actions(tmp_path, state, Agent.config, integrated=True) == []


def test_curator_premature_finish_exhausts_without_promotion(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "jobs").mkdir()
    prompts = []

    class Agent:
        root = tmp_path
        store = tmp_path / "jobs"
        config = {"max_actions": 2, "model": "fixture"}

        def ask(self, task, step):
            prompts.append(task)
            return '{"action": "finish", "reason": "Attempt early completion"}'

    monkeypatch.setattr(C, "load_groups", lambda root: [])
    with pytest.raises(WorkflowError, match="action limit"):
        C.curate(tmp_path, cast(Runtime, Agent()), ["a__REPORT.md"], lambda *args: None, {})
    assert len(prompts) == 2
    assert "integrate" in json.dumps(prompts[-1])
    receipts = json.loads((tmp_path / "jobs/curator-receipts.json").read_text())
    assert len(receipts) == 2 and receipts[-1]["result"] == "rejected"


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


def test_curator_blocks_dependencies_and_reuses_current_action(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "jobs").mkdir()
    actions = iter(
        ["topics", "conflicts", "conflicts", "topics", "literature", "authors", "finish"]
    )
    calls = []

    class Agent:
        store = tmp_path / "jobs"
        config = {"max_actions": 8, "model": "fixture"}

        def ask(self, task, step):
            return json.dumps({"action": next(actions), "reason": "Maintain wiki"})

    monkeypatch.setattr(C, "load_groups", lambda root: [])
    monkeypatch.setattr(C, "propose_topics", lambda root, agent: None)
    C.curate(tmp_path, cast(Runtime, Agent()), [], lambda name, args: calls.append(name), {})
    assert calls.count("conflicts") == 1 and calls.count("topics") == 1
    receipts = json.loads((tmp_path / "jobs/curator-receipts.json").read_text())
    assert receipts[0]["result"] == "rejected"
    assert receipts[2]["result"] == "unchanged"


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


def test_action_limit_resume_reuses_paid_decisions(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C
    from beril_wiki.agentic import runtime as R

    config = dict(
        root=str(tmp_path),
        store=str(tmp_path / "jobs"),
        run="same-update",
        model="fixture",
        cli="unused",
        max_actions=2,
        max_tokens=1000,
        max_jobs=20,
        reserve_tokens=10,
    )
    agent = R.Runtime(config)
    calls = []
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    monkeypatch.setattr(C, "load_groups", lambda root: [])
    monkeypatch.setattr(C, "propose_topics", lambda root, agent: None)

    async def answer(payload, key):
        data = json.loads(json.loads(payload)[0]["content"].split("\n")[-1])
        action = next((a for a in data["available"] if a in data["pending"]), "finish")
        result = json.dumps({"action": action, "reason": "Refresh required work"})
        agent.ledger.finish(key, result, {"input_tokens": 2, "output_tokens": 3})
        calls.append(key)
        return result

    monkeypatch.setattr(agent, "_query", answer)
    with pytest.raises(WorkflowError, match="action limit"):
        C.curate(tmp_path, agent, [], lambda *args: None, {})
    assert len(calls) == 2
    config["max_actions"] = 8
    state = C.curate(tmp_path, agent, [], lambda *args: None, {})
    assert set(state) == set(C.EDITORIAL)
    assert len(calls) == 5 and agent.ledger.totals()["tokens"] == 25


def test_failed_editorial_action_keeps_receipt(tmp_path, monkeypatch):
    from beril_wiki.agentic import curator as C

    (tmp_path / "jobs").mkdir()

    class Agent:
        store = tmp_path / "jobs"
        config = {"max_actions": 8, "model": "fixture"}

        def ask(self, task, step):
            return '{"action": "conflicts", "reason": "Refresh tensions"}'

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
        return (
            '{"queries": ["yield"]}'
            if step.endswith("queries")
            else "## Literature Context\n\nExternal context. [PMID 1](https://pubmed.ncbi.nlm.nih.gov/1/)"
        )

    monkeypatch.setattr(L.C, "llm", reply)
    assert L.main(tmp_path) == 0
    assert "Literature Context" in page.read_text()
    assert L.main(tmp_path) == 0
    assert calls == ["lit/a/queries", "lit/a/review"]
