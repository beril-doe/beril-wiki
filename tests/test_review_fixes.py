"""Regression tests for the findings of the Oct 2026 independent review of the card stages."""

import datetime
import json
import re
import xml.etree.ElementTree as ET

import pytest

from beril_wiki.agentic import curator as C
from beril_wiki.stages import cards, headlines, novelty
from card_fakes import FakeAgent, install
from test_headlines import RECORDS, headline
from test_headlines import setup as headline_setup
from test_novelty import CROSS, FID, PAPERS, judgment, page, run

GOOD = judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))


def test_expired_label_makes_novelty_pending(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [GOOD]})
    config = {"model": "m"}
    state = {name: C.stage_snapshot(tmp_path, name, config) for name in C.EDITORIAL}
    assert "novelty" not in C.pending_actions(tmp_path, state, config, integrated=True)
    monkeypatch.setattr(novelty, "today", lambda: datetime.date(2027, 3, 1))
    assert novelty.labels_due(tmp_path)
    assert "novelty" in C.pending_actions(tmp_path, state, config, integrated=True)


def test_invalidation_keeps_published_labels(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [GOOD]})
    before = (tmp_path / "state/novelty.json").read_text()
    now = C.stage_snapshot(tmp_path, "novelty", {"model": "m"})
    C.invalidate_outputs(tmp_path, "novelty", {}, now)
    assert (tmp_path / "state/novelty.json").read_text() == before


def test_new_figures_counts_small_integers_but_not_identifiers():
    assert cards.new_figures("Measured 999 genes", "Measured 42 genes") == ["999"]
    assert cards.new_figures("domain PF00034 in GCF_000005845", "") == []
    assert cards.new_figures("Of 121 strains", "Of 121 strains") == []


def test_quantity_value_must_match_a_whole_figure():
    quote = "Of 121 strains, 42 lost the operon (34.7%)."
    records = [
        {"id": "s:0:0", "kind": "finding", "claim": "x", "quote": quote},
        RECORDS[2],
    ]
    bad = headline("s:0:0", claim="Of 121 strains, 42 lost the operon.", value="21")
    with pytest.raises(cards.CandidateError, match="not in the quote"):
        headlines.checker(records)(json.dumps({"headlines": [bad]}))


def test_quantity_description_is_checked_against_the_quote():
    h = headline()
    h["quantities"][0]["what"] = "odds ratio across 3,200 genes"
    with pytest.raises(cards.CandidateError, match="3200"):
        headlines.checker(RECORDS)(json.dumps({"headlines": [h]}))


def test_retrieval_reserves_room_for_cited_papers(tmp_path, monkeypatch):
    seen = []
    monkeypatch.setattr(novelty, "search_ids", lambda q: [f"{q}{n}" for n in range(10)])
    monkeypatch.setattr(novelty, "fetch_abstracts", lambda ids: seen.extend(ids) or {})
    monkeypatch.setattr(novelty.re, "fullmatch", lambda *a: True)
    novelty.retrieve(tmp_path, ["1", "2", "3"], ["99999"])
    assert "99999" in seen and len(seen) <= novelty.MAX_PAPERS


def test_difference_may_name_only_retrieved_papers():
    parse = novelty.judgment_checker(PAPERS)
    bad = judgment(
        novelty.EXTENDS,
        closest=(("111", "same relationship elsewhere"),),
        difference="PMID 99999999 already reports this; PMID 111 does not.",
    )
    with pytest.raises(cards.CandidateError, match="99999999"):
        parse(bad)


def test_check_flags_unretrieved_pmid_in_difference(tmp_path):
    from beril_wiki.check import card_errors

    (tmp_path / "state").mkdir()
    (tmp_path / "wiki/findings").mkdir(parents=True)
    (tmp_path / "state/novelty.json").write_text(
        json.dumps(
            {
                "x": {
                    "label": novelty.EXTENDS,
                    "retrieved_on": "2026-10-23",
                    "candidates": ["111"],
                    "closest": [{"pmid": "111"}],
                    "difference": "See PMIDs 111 and 222.",
                }
            }
        )
    )
    assert any("PMID 222" in e for e in card_errors(tmp_path, {}))


def test_model_change_reruns_headlines(tmp_path, monkeypatch):
    reply = json.dumps({"headlines": [headline()]})
    agent = headline_setup(tmp_path, monkeypatch, {"headlines/a": [reply, reply]})
    agent.config = {"model": "claude-sonnet-5-5", "step_models": {}}
    assert headlines.main(tmp_path) == 0
    calls = len(agent.asked)
    agent.config = {"model": "claude-opus-5-5", "step_models": {}}
    assert headlines.main(tmp_path) == 0
    assert len(agent.asked) > calls


def test_model_change_rejudges_labels(tmp_path, monkeypatch):
    _, agent = run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [GOOD]})
    later = FakeAgent(
        tmp_path / "store",
        {f"novelty/{FID}/queries": ['{"queries": ["q2"]}'], f"novelty/{FID}/judge": [GOOD]},
    )
    later.config = CROSS | {"step_models": CROSS["step_models"] | {"cards": "claude-opus-5-5"}}
    install(monkeypatch, later)
    assert novelty.main(tmp_path) == 0
    assert f"novelty/{FID}/judge" in later.asked


@pytest.mark.parametrize(
    "error",
    [ET.ParseError("bad xml"), novelty.WorkflowError("PubMed response exceeds 2MB")],
)
def test_any_retrieval_fault_is_a_per_finding_failure(tmp_path, monkeypatch, error):
    page(tmp_path)
    agent = FakeAgent(tmp_path / "store", {f"novelty/{FID}/queries": ['{"queries": ["q"]}']})
    agent.config = CROSS
    install(monkeypatch, agent)
    monkeypatch.setattr(novelty, "search_ids", lambda q: ["111"])

    def broken(ids):
        raise error

    monkeypatch.setattr(novelty, "fetch_abstracts", broken)
    assert novelty.main(tmp_path) == 0
    entry = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert entry["failed"] is True


def test_pin_without_retrieval_publishes_and_checks(tmp_path):
    from beril_wiki.check import card_errors
    from beril_wiki.publish.cards import literature_section

    decision = novelty.Decision(finding="x", label=novelty.EXTENDS, reason="checked by hand")
    entry = novelty.apply_decision({"label": novelty.NOT_ASSESSED, "failed": True}, decision)
    text = literature_section(entry)
    assert "checked by hand" in text and "Extends retrieved work" in text
    (tmp_path / "state").mkdir()
    (tmp_path / "wiki/findings").mkdir(parents=True)
    (tmp_path / "wiki/findings/x.md").write_text("---\nfinding_id: x\nsource: a\n---\n# X\n")
    (tmp_path / "state/novelty.json").write_text(json.dumps({"x": entry}))
    assert not [e for e in card_errors(tmp_path, {"a": "x"}) if "retrieval date" in e]


# Second review (Codex, Oct 2026)

from test_headlines import TWO  # noqa: E402


def test_salvage_follows_the_named_item_through_a_reorder(tmp_path, monkeypatch):
    swapped = {"headlines": list(reversed(TWO["headlines"]))}
    objection = ["Headline 2's caveat is wrong"]  # a:0:1, counted from 1 in the reviewed reply
    replies = {"headlines/a": [json.dumps(TWO)], "headlines/a/repair": [json.dumps(swapped)] * 3}
    agent = headline_setup(tmp_path, monkeypatch, replies)
    agent.objections = {"headlines/a": objection}
    agent.still_open = {"headlines/a": objection}
    assert headlines.main(tmp_path) == 0
    pages = list((tmp_path / "wiki/findings").glob("*.md"))
    assert [cards.read_page(p)[0]["result"] for p in pages] == ["observation"]


def test_failed_expired_label_stays_due(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [GOOD]})
    path = tmp_path / "state/novelty.json"
    state = json.loads(path.read_text())
    state[FID]["failed"] = True
    path.write_text(json.dumps(state))
    monkeypatch.setattr(novelty, "today", lambda: datetime.date(2027, 3, 1))
    assert novelty.labels_due(tmp_path)


def test_efetch_error_document_is_a_retrieval_failure(monkeypatch):
    from beril_wiki.stages import literature as L

    monkeypatch.setattr(
        L, "paced_get", lambda *a, **k: b"<eFetchResult><ERROR>busy</ERROR></eFetchResult>"
    )
    with pytest.raises(novelty.WorkflowError, match="busy"):
        novelty.fetch_abstracts(["12345"])


def test_esearch_error_is_a_retrieval_failure(monkeypatch):
    from beril_wiki.stages import literature as L

    monkeypatch.setattr(L, "eutils", lambda *a, **k: {"esearchresult": {"ERROR": "Invalid query"}})
    with pytest.raises(novelty.WorkflowError, match="Invalid query"):
        novelty.search_ids("x")


def test_card_figures_keep_the_percent_sign():
    assert cards.new_figures("42% of genes were essential", "42 genes were tested.") == ["42%"]
    assert not cards.in_quote("42%", "42 genes were tested.")
    assert cards.in_quote("28.7%", "stress (28.7% vs 43.2%)")


def test_cards_command_leaves_status_readable(tmp_path, monkeypatch):
    import sys

    from beril_wiki.agentic import __main__ as cli

    monkeypatch.setattr(cli, "run_stage", lambda *a: None)
    cli.run_cards(tmp_path, {"model": "m", "max_tokens": 10, "max_jobs": 1, "cli": "unused"})
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "status"])
    assert cli.main() == 0


def test_card_styles_leave_record_classes_alone():
    from pathlib import Path

    css = (Path(__file__).parents[1] / "theme/styles/_cards.scss").read_text()
    for name in ("kind", "chips", "chip", "more"):
        assert not re.search(rf"(^|[\s,]){re.escape('.' + name)}\b", css, re.M), name


# PR #13 review (Codex bot, Oct 2026)


def test_expired_label_stays_pending_after_its_snapshot_is_accepted(tmp_path, monkeypatch):
    run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [GOOD]})
    config = {"model": "m"}
    monkeypatch.setattr(novelty, "today", lambda: datetime.date(2027, 3, 1))
    # A failed refresh keeps the old date; the run then accepts a snapshot taken while due.
    state = {name: C.stage_snapshot(tmp_path, name, config) for name in C.EDITORIAL}
    assert "novelty" in C.pending_actions(tmp_path, state, config, integrated=True)
