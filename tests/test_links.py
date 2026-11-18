"""The links stage: code finds candidates, a model sorts them, answers cache per candidate."""

import json
import re

import pytest

from beril_wiki.agentic import curator
from beril_wiki.agentic.runtime import CandidateError, JobFailed, WorkflowError
from beril_wiki.stages import cards, links
from card_fakes import FakeAgent, install

A, B, C = "alpha--1a2b3c4d", "beta--5e6f7a8b", "gamma--9c0d1e2f"


def finding(root, fid, title, claim, quote="Essential genes were 82% core."):
    cards.write_page(
        root / "wiki/findings" / f"{fid}.md",
        {"type": "Finding", "description": claim, "result": "observation"}
        | {"source": fid.split("--")[0]},
        f"# {title}\n\n{claim} [src: x]\n\n## Evidence\n\n> {quote} [src: x]\n",
    )


def corpus(root):
    finding(root, A, "Essential genes are mostly core", "Essential genes are mostly core genes.")
    finding(root, B, "Essential genes are often core", "Essential genes are often core genes.")
    finding(root, C, "Iron reduction in clay", "Iron reduction markers differ in clay.")
    (root / "wiki/concepts").mkdir(parents=True)
    (root / "wiki/concepts/essential.md").write_text("# E\n\nCore. [src: alpha, beta]\n")
    (root / "wiki/conflicts").mkdir(parents=True)
    sources = root / "wiki/sources"
    sources.mkdir(parents=True)
    (sources / "alpha__REPORT.md").write_text(
        "# Report: Alpha conservation\n\nWe reuse the fitness table from `beta`.\n"
    )
    (sources / "beta__REPORT.md").write_text("# Report: Beta essential genes study\n\nText.\n")
    (sources / "gamma__REPORT.md").write_text("# Report: Gamma clay\n\nNothing.\n")


class Scripted(FakeAgent):
    """Answers every batch from a function of its step and prompt."""

    def __init__(self, store, answer, **kw):
        super().__init__(store, {}, **kw)
        self.answer = answer

    def ask(self, messages, step, *, model=None):
        self.asked.append(step)
        self.jobs.append(step)
        return self.answer(step, messages[0]["content"])


def default_answer(step, content):
    ids = sorted(set(re.findall(r'"([PR]\d+)"', content)))
    if "/pairs" in step or "pairs-" in step:
        items = [
            {
                "id": i,
                "relation": "same result",
                "label": "Both report how often essential genes are core",
            }
            for i in ids
        ]
    else:
        items = [
            {
                "id": i,
                "relation": "uses its data or methods",
                "label": "Reuses the gene fitness measurements the beta project made",
            }
            for i in ids
        ]
    return json.dumps({"items": items})


def run(tmp_path, monkeypatch, answer=default_answer, **kw):
    agent = Scripted(tmp_path / "store", answer, **kw)
    install(monkeypatch, agent)
    assert links.main(tmp_path) == 0
    return json.loads((tmp_path / "state/links.json").read_text()), agent


def test_candidates_are_sorted_into_typed_links(tmp_path, monkeypatch):
    corpus(tmp_path)
    state, agent = run(tmp_path, monkeypatch)
    kinds = {(x["a"], x["b"], x["level"], x["type"]) for x in state["links"]}
    assert kinds == {
        (A, B, "finding", "same result"),
        ("alpha", "beta", "project", "uses its data or methods"),
    }
    # Gamma shares no concept page with the others, so no pair is asked about.
    assert not any(C in cid for cid in state["candidates"])
    assert all(step.startswith("links/") for step in agent.asked)


def test_an_unrelated_new_result_reasks_nothing(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    finding(tmp_path, "delta--3a4b5c6d", "Phage defence islands", "Defence islands move often.")
    _, agent = run(tmp_path, monkeypatch)
    assert agent.asked == []


def test_a_failed_batch_leaves_no_current_answer(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    finding(
        tmp_path,
        A,
        "Essential genes are mostly core",
        "Essential genes are mostly core genes.",
        quote="Essential genes were 86% core.",
    )

    def refuse(step, content):
        if "pairs-" in step:
            raise JobFailed("Codex turn failed: flagged for possible biological risk.")
        return default_answer(step, content)

    state, _ = run(tmp_path, monkeypatch, answer=refuse)
    assert not any(x["level"] == "finding" for x in state["links"])
    assert state["candidates"][f"pair:{A}|{B}"]["failed"] is True


def test_links_to_removed_results_are_pruned(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    (tmp_path / "wiki/findings" / f"{B}.md").unlink()
    state, _ = run(tmp_path, monkeypatch)
    assert f"pair:{A}|{B}" not in state["candidates"]
    assert all(x["level"] == "project" for x in state["links"])


@pytest.mark.parametrize(
    "label, problem",
    [
        ("Both projects confirmed that essential genes are core", "confirmed"),
        ("The two analyses agree on how essential genes are core", "agree"),
        ("Essential genes core at p = 0.01 in both projects", "statistic"),
        ("Essential genes were 99% core in both of the projects", "figures"),
        ("Uses the gene_to_cluster mapping from the other project", "gene_to_cluster"),
        ("Builds on the other project's link table for essential genes", "'table'"),
        ("Uses its essential gene counts for the core comparison", "whose data"),
    ],
)
def test_labels_that_claim_confirmation_or_add_figures_go_back(label, problem):
    parse = links.checker(["P1"], ("same result", "not the same question"), {"P1": "82% core"})
    with pytest.raises(CandidateError, match=problem):
        parse(json.dumps({"items": [{"id": "P1", "relation": "same result", "label": label}]}))
    ok = parse(
        json.dumps({"items": [{"id": "P1", "relation": "not the same question", "label": ""}]})
    )
    assert ok.items[0].relation == "not the same question"


def test_links_is_scheduled_after_headlines_as_a_card_stage():
    order = list(curator.EDITORIAL)
    assert order.index("links") > order.index("headlines")
    assert curator.EDITORIAL["links"][1] == ("state/links.json",)
    assert "links" in curator.CARD_STAGES
    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic.runtime import role_for

    assert "links" in cli.CARD_STAGES
    assert role_for("links/pairs-abc") == "cards"
    assert role_for("links/pairs-abc/science-review") == "card_review"


def test_a_stopped_run_keeps_the_links_still_current(tmp_path, monkeypatch):
    """A budget stop after one batch must not leave readers with no links."""
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    finding(
        tmp_path,
        A,
        "Essential genes are mostly core",
        "Essential genes are mostly core genes.",
        quote="Essential genes were 86% core.",
    )

    def stop_on_pairs(step, content):
        if "pairs-" in step:
            raise WorkflowError("USD cap admission refused: links")
        return default_answer(step, content)

    agent = Scripted(tmp_path / "store", stop_on_pairs)
    install(monkeypatch, agent)
    with pytest.raises(WorkflowError):
        links.main(tmp_path)
    saved = json.loads((tmp_path / "state/links.json").read_text())
    # The project link is still current; the changed pair has no current answer.
    assert [(x["a"], x["level"]) for x in saved["links"]] == [("alpha", "project")]


def test_labels_with_significance_wording_are_asked_again(tmp_path, monkeypatch):
    corpus(tmp_path)

    def wording(step, content):
        reply = json.loads(default_answer(step, content))
        if "pairs-" in step and not step.endswith("/repair"):
            reply["items"][0]["label"] = "Both report a non-significant core gene difference"
        return json.dumps(reply)

    state, agent = run(tmp_path, monkeypatch, answer=wording)
    assert any(s.endswith("/repair") for s in agent.asked)
    assert all("significant" not in x["label"] for x in state["links"])


def test_only_labels_todays_rules_reject_are_asked_again(tmp_path, monkeypatch):
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    path = tmp_path / "state/links.json"
    state = json.loads(path.read_text())
    ref = next(k for k, v in state["candidates"].items() if k.startswith("ref:"))
    state["candidates"][ref]["label"] = "Takes its fitness table as input data"
    path.write_text(json.dumps(state))
    _, agent = run(tmp_path, monkeypatch)
    assert agent.asked and all(step.startswith("links/refs-") for step in agent.asked)


def test_a_label_naming_the_other_project_may_say_its_later():
    """Rerun, Nov 2026: a later 'its' failed labels that already said whose data."""
    for label in (
        "Builds on the other project's conservation test, extending its core enrichment.",
        "Compares its osmotic-stress gene overlap with the other project's overlap.",
    ):
        assert links.label_problem(label) == ""
    assert links.label_problem("Uses its essential gene counts for the comparison")


@pytest.mark.parametrize(("expect", "asked"), [("gamma", False), ("alpha", True), (None, True)])
def test_a_run_for_one_project_leaves_another_projects_failed_link(
    tmp_path, monkeypatch, expect, asked
):
    """A run for gamma must not re-ask the failed alpha|beta pair or change its record,
    even under --strict-pages; a run for alpha and a maintainer run re-ask it."""
    corpus(tmp_path)
    run(tmp_path, monkeypatch)
    finding(
        tmp_path,
        A,
        "Essential genes are mostly core",
        "Essential genes are mostly core genes.",
        quote="Essential genes were 86% core.",
    )

    def refuse(step, content):
        if "pairs-" in step:
            raise JobFailed("Codex turn failed: flagged for possible biological risk.")
        return default_answer(step, content)

    state, _ = run(tmp_path, monkeypatch, answer=refuse)
    assert state["candidates"][f"pair:{A}|{B}"]["failed"] is True
    before = (tmp_path / "state/links.json").read_text()
    agent = Scripted(tmp_path / "store", default_answer)
    if expect:
        agent.config["expect_source"] = expect
    install(monkeypatch, agent)
    monkeypatch.setattr(cards, "strict_pages", lambda: True)
    assert links.main(tmp_path) == 0
    after = (tmp_path / "state/links.json").read_text()
    if asked:
        assert any("pairs-" in step for step in agent.asked)
        assert json.loads(after)["candidates"][f"pair:{A}|{B}"]["relation"] == "same result"
    else:
        assert agent.asked == [] and after == before
