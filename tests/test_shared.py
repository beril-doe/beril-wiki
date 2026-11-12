"""The shared stage: statements for results several projects reached."""

import json

import pytest

from beril_wiki.agentic import curator
from beril_wiki.agentic.runtime import CONTENT_FLAG, CandidateError, JobFailed, WorkflowError
from beril_wiki.stages import cards, shared
from card_fakes import install
from test_links import A, B, C, Scripted, finding

GOOD = {
    "title": "Essential genes are usually shared by all strains",
    "sentence": "Two projects found that genes a cell cannot lose are usually in the core "
    "genome shared by every strain of a species.",
    "question": "Are the genes a cell cannot lose shared by every strain?",
    "lanes": {A: "Essential genes across all fitness classes", B: "Essential versus neutral genes"},
    "how": "Both report the same 82% figure, so they share one analysis of the same data.",
}


def corpus(root, link_type="same result"):
    finding(root, A, "Essential genes are mostly core", "Essential genes are mostly core genes.")
    finding(root, B, "Essential genes are often core", "Essential genes are often core genes.")
    finding(root, C, "Iron reduction in clay", "Iron reduction markers differ in clay.")
    (root / "wiki/concepts").mkdir(parents=True, exist_ok=True)
    (root / "wiki/concepts/core.md").write_text("# Core\n\nCore. [src: alpha, beta]\n")
    (root / "wiki/concepts/fit.md").write_text("# Fit\n\nFitness. [src: alpha, beta]\n")
    (root / "state").mkdir(exist_ok=True)
    (root / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Pangenome", "concepts": ["core"]},
                    {"title": "Fitness", "concepts": ["fit"]},
                ]
            }
        )
    )
    links = [
        {"a": A, "b": B, "level": "finding", "type": link_type, "label": "Both report core genes"},
        {"a": "alpha", "b": "beta", "level": "project", "type": "uses its data or methods"}
        | {"label": "Reuses the table"},
    ]
    (root / "state/links.json").write_text(json.dumps({"links": links}))


def run(tmp_path, monkeypatch, reply=GOOD, **kw):
    agent = Scripted(tmp_path / "store", lambda step, content: json.dumps(reply), **kw)
    install(monkeypatch, agent)
    assert shared.main(tmp_path) == 0
    return json.loads((tmp_path / "state/shared.json").read_text()), agent


def test_a_linked_pair_across_topics_gets_one_statement(tmp_path, monkeypatch):
    corpus(tmp_path)
    state, agent = run(tmp_path, monkeypatch)
    (group,) = state.values()
    assert group["members"] == [A, B] and group["projects"] == ["alpha", "beta"]
    assert group["topics"] == ["fitness", "pangenome"]
    assert group["relation"] == "same result" and group["title"] == GOOD["title"]
    assert [s for s in agent.asked if not s.endswith("science-review")] == [
        f"shared/{next(iter(state))}"
    ]
    # Unchanged inputs ask nothing.
    _, again = run(tmp_path, monkeypatch)
    assert again.asked == []


def test_a_group_in_one_topic_is_not_highlighted(tmp_path, monkeypatch):
    corpus(tmp_path)
    (tmp_path / "wiki/concepts/fit.md").write_text("# Fit\n\nNo citation.\n")
    state, agent = run(tmp_path, monkeypatch)
    assert state == {} and agent.asked == []


def test_a_group_whose_link_is_gone_is_pruned(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    (tmp_path / "state/links.json").write_text(json.dumps({"links": []}))
    state, _ = run(tmp_path, monkeypatch)
    assert state == {}


@pytest.mark.parametrize(
    "field, value, problem",
    [
        ("how", "Both projects confirmed the same pattern in essential genes.", "confirmed"),
        ("sentence", "Essential genes were 99% core in two projects of bacteria.", "figures"),
        ("question", "Are essential genes core in bacteria", "end with"),
        ("lanes", {A: "Essential genes"}, "lanes must name"),
        ("title", "Essential genes core at p = 0.01 in both projects", "statistic"),
    ],
)
def test_checks_send_problems_back_to_the_writer(field, value, problem):
    members = {
        A: {"claim": "Essential genes are mostly core.", "quote": "82% core.", "quantities": []},
        B: {"claim": "Essential genes are often core.", "quote": "", "quantities": []},
    }
    with pytest.raises(CandidateError, match=problem):
        shared.checker(members)(json.dumps(GOOD | {field: value}))


def test_the_group_relation_is_the_weakest_of_its_links(tmp_path, monkeypatch):
    corpus(tmp_path, link_type="similar comparison, different scope")
    state, _ = run(tmp_path, monkeypatch)
    assert next(iter(state.values()))["relation"] == "similar comparison, different scope"


def test_shared_runs_after_links_in_the_schedule():
    order = list(curator.EDITORIAL)
    assert order.index("shared") > order.index("links")
    assert curator.EDITORIAL["shared"][2] == ("links",)
    assert "shared" in curator.CARD_STAGES


def test_status_runs_nothing(tmp_path, capsys):
    assert shared.main(tmp_path, ["--status"]) == 0
    assert "shared: 0 accepted" in capsys.readouterr().out


def test_no_finished_links_checkpoint_changes_nothing(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    before = (tmp_path / "state/shared.json").read_text()
    (tmp_path / "state/links.json").write_text(json.dumps({"candidates": {}}))
    agent = Scripted(tmp_path / "store", lambda step, content: json.dumps(GOOD))
    install(monkeypatch, agent)
    assert shared.main(tmp_path) == 0
    assert (tmp_path / "state/shared.json").read_text() == before and agent.asked == []


def test_changed_groups_lose_their_text_before_any_job_runs(tmp_path, monkeypatch):
    """A stop mid-run must not leave text written for older inputs publishable."""
    corpus(tmp_path)
    state, _ = run(tmp_path, monkeypatch)
    finding(
        tmp_path,
        A,
        "Essential genes are mostly core",
        "Essential genes are mostly core genes.",
        quote="Essential genes were 86% core.",
    )

    def stop(step, content):
        raise WorkflowError("USD cap admission refused: shared")

    install(monkeypatch, Scripted(tmp_path / "store", stop))
    with pytest.raises(WorkflowError):
        shared.main(tmp_path)
    saved = json.loads((tmp_path / "state/shared.json").read_text())
    assert all(g.get("failed") and "title" not in g for g in saved.values())


def test_publisher_ranks_relations_in_the_stage_order():
    """publish.cards.links.relation_of ranks by RELATION_TEXT; it must match the stage's ranking."""
    from beril_wiki.publish.cards.text import RELATION_TEXT

    assert tuple(RELATION_TEXT) == shared.RELATIONS


def test_prompt_keeps_disagreeing_results_apart():
    """Content review, Nov 2026: a group of results that disagreed read as one result."""
    assert shared.PROMPT_TAG == "shared@2"
    assert "never present them as one result" in shared.PROMPT


@pytest.mark.parametrize(("expect", "asked"), [("gamma", False), ("alpha", True), (None, True)])
def test_a_run_for_one_project_leaves_another_projects_failed_group(
    tmp_path, monkeypatch, expect, asked
):
    """A run for gamma must not re-ask the failed alpha and beta group or change its
    record, even under --strict-pages; a run for alpha and a maintainer run re-ask it."""
    corpus(tmp_path)

    def refuse(step, content):
        raise JobFailed(f"Codex turn failed: {CONTENT_FLAG}")

    install(monkeypatch, Scripted(tmp_path / "store", refuse))
    assert shared.main(tmp_path) == 0
    before = (tmp_path / "state/shared.json").read_text()
    assert all(g["failed"] for g in json.loads(before).values())
    agent = Scripted(tmp_path / "store", lambda step, content: json.dumps(GOOD))
    if expect:
        agent.config["expect_source"] = expect
    install(monkeypatch, agent)
    monkeypatch.setattr(cards, "strict_pages", lambda: True)
    assert shared.main(tmp_path) == 0
    after = (tmp_path / "state/shared.json").read_text()
    if asked:
        assert agent.asked and next(iter(json.loads(after).values()))["title"] == GOOD["title"]
    else:
        assert agent.asked == [] and after == before
