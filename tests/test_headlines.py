"""The headlines stage: capped, figure-checked finding records per report."""

import json

import pytest

from beril_wiki.stages import cards, headlines
from card_fakes import FakeAgent, evidence, install, report, scope

TEXT = (
    "# Dark genes\n\nDark genes were depleted under stress (odds ratio 0.53; 28.7% vs 43.2%).\n"
    "No effect of copper was detected (p = 0.41).\nOnly 3,200 genes were tested.\n"
)
RECORDS = [
    {
        "id": "a:0:0",
        "kind": "finding",
        "claim": "Depleted",
        "quote": "Dark genes were depleted under stress (odds ratio 0.53; 28.7% vs 43.2%).",
    },
    {
        "id": "a:0:1",
        "kind": "null",
        "claim": "No copper effect",
        "quote": "No effect of copper was detected (p = 0.41).",
    },
    {
        "id": "a:0:2",
        "kind": "caveat",
        "claim": "Only 3,200 genes tested",
        "quote": "Only 3,200 genes were tested.",
    },
]


def headline(evidence_id="a:0:0", result="observation", claim=None, value="0.53"):
    return {
        "evidence": evidence_id,
        "result": result,
        "title": "Dark genes are depleted under stress",
        "claim": claim or "Dark genes were depleted under stress (odds ratio 0.53).",
        "quantities": [
            {"value": value, "what": "odds ratio", "unit": "", "denominator": "", "scope": ""}
        ],
        "caveat_evidence": "a:0:2",
        "caveat": "Only 3,200 genes were tested.",
    }


def setup(tmp_path, monkeypatch, replies, objections=None):
    report(tmp_path, "a", TEXT)
    evidence(tmp_path / "store", tmp_path, "a", RECORDS)
    scope(tmp_path, reports=["a"])
    agent = FakeAgent(tmp_path / "store", replies, objections)
    install(monkeypatch, agent)
    return agent


def test_headlines_writes_capped_records(tmp_path, monkeypatch):
    five = {"headlines": [headline() for _ in range(5)]}
    good = {
        "headlines": [
            headline(),
            headline(
                "a:0:1", "null result", "No effect of copper was detected (p = 0.41).", "0.41"
            ),
        ]
    }
    agent = setup(
        tmp_path,
        monkeypatch,
        {"headlines/a": [json.dumps(five)], "headlines/a/repair": [json.dumps(good)]},
    )
    assert headlines.main(tmp_path) == 0
    pages = sorted((tmp_path / "wiki/findings").glob("*.md"))
    assert len(pages) == 2
    fields, body = cards.read_page(pages[0] if "0.53" in pages[0].read_text() else pages[1])
    assert fields["type"] == "Finding" and fields["source"] == "a"
    assert fields["finding_id"] == cards.finding_id("a", RECORDS[0]["quote"])
    assert "[src: a]" in body and "## Caveat" in body and "> Dark genes were depleted" in body
    assert "headlines/a/science-review" in agent.asked


def test_headlines_rejects_figure_absent_from_quote(tmp_path, monkeypatch):
    bad = {
        "headlines": [headline(claim="Dark genes were depleted under stress (odds ratio 0.61).")]
    }
    setup(
        tmp_path,
        monkeypatch,
        {"headlines/a": [json.dumps(bad)], "headlines/a/repair": [json.dumps(bad)] * 3},
    )
    assert headlines.main(tmp_path) == 0  # a failure is recorded, the stage continues
    assert not list((tmp_path / "wiki/findings").glob("*.md"))


def test_headlines_null_must_come_from_null_record(tmp_path, monkeypatch):
    parse = headlines.checker(RECORDS)
    wrong = {"headlines": [headline(result="null result")]}
    try:
        parse(json.dumps(wrong))
    except Exception as exc:  # noqa: BLE001
        assert "kind null" in str(exc)
    else:
        raise AssertionError("a null result from a finding record was accepted")


def test_headlines_skips_source_without_matching_evidence(tmp_path, monkeypatch):
    agent = setup(tmp_path, monkeypatch, {})
    report(tmp_path, "a", TEXT + "\nRevised.\n")
    assert headlines.main(tmp_path) == 0
    assert agent.asked == []


def test_headlines_unchanged_input_makes_no_calls(tmp_path, monkeypatch):
    good = {"headlines": [headline()]}
    agent = setup(tmp_path, monkeypatch, {"headlines/a": [json.dumps(good)]})
    assert headlines.main(tmp_path) == 0
    calls = len(agent.asked)
    assert headlines.main(tmp_path) == 0
    assert len(agent.asked) == calls


def test_headlines_retires_pages_of_out_of_scope_reports(tmp_path, monkeypatch):
    good = {"headlines": [headline()]}
    setup(tmp_path, monkeypatch, {"headlines/a": [json.dumps(good)]})
    assert headlines.main(tmp_path) == 0
    assert list((tmp_path / "wiki/findings").glob("a--*.md"))
    scope(tmp_path, reports=[])
    assert headlines.main(tmp_path) == 0
    assert not list((tmp_path / "wiki/findings").glob("*.md"))


def test_headlines_cap_counts_distinct_findings():
    records = RECORDS + [
        {"id": f"a:1:{n}", "kind": "finding", "claim": "x", "quote": RECORDS[0]["quote"]}
        for n in range(4)
    ]
    five = {"headlines": [headline()] + [headline(f"a:1:{n}") for n in range(4)]}
    try:
        headlines.checker(records)(json.dumps(five))
    except Exception as exc:  # noqa: BLE001
        assert "at most 4" in str(exc) and "twice" not in str(exc)
    else:
        raise AssertionError("five observations were accepted")


TWO = {
    "headlines": [
        headline(),
        headline("a:0:1", "null result", "No effect of copper was detected (p = 0.41).", "0.41"),
    ]
}


def test_headlines_salvage_drops_only_named_headlines(tmp_path, monkeypatch):
    objection = ["Headline a:0:1 overstates the null"]
    replies = {"headlines/a": [json.dumps(TWO)], "headlines/a/repair": [json.dumps(TWO)] * 3}
    agent = setup(tmp_path, monkeypatch, replies)
    agent.objections = {"headlines/a": objection}
    agent.still_open = {"headlines/a": objection}
    assert headlines.main(tmp_path) == 0
    pages = list((tmp_path / "wiki/findings").glob("*.md"))
    assert [cards.read_page(p)[0]["result"] for p in pages] == ["observation"]


def test_headlines_unmatched_objection_fails_the_report(tmp_path, monkeypatch):
    objection = ["The caveats are too vague"]
    replies = {"headlines/a": [json.dumps(TWO)], "headlines/a/repair": [json.dumps(TWO)] * 3}
    agent = setup(tmp_path, monkeypatch, replies)
    agent.objections = {"headlines/a": objection}
    agent.still_open = {"headlines/a": objection}
    assert headlines.main(tmp_path) == 0
    assert not list((tmp_path / "wiki/findings").glob("*.md"))


def test_headlines_salvage_reads_headline_numbers_both_ways():
    rescue = headlines.salvager(RECORDS)
    reply = headlines.Reply.model_validate(TWO)
    kept = rescue(reply, [("Headline 2's caveat is wrong", reply)])
    # "headline 2" is index 1 counted from 1 and would be index 2 from 0: only index 1 exists.
    assert kept is not None and [h.evidence for h in kept[0].headlines] == ["a:0:0"]
    assert rescue(reply, [("headline 1 is fine but headline 0 is not", reply)]) is None


def test_headlines_long_title_is_a_code_error():
    title = "A title that runs on well past the twelve word limit set for cards"
    long = headline() | {"title": title}
    with pytest.raises(cards.CandidateError, match="more than 12 words"):
        headlines.checker(RECORDS)(json.dumps({"headlines": [long]}))


def test_render_does_not_repeat_a_unit_the_value_carries():
    h = headlines.Headline.model_validate(
        headline(value="28.7%") | {"quantities": [{"value": "28.7%", "what": "share", "unit": "%"}]}
    )
    _, _, body = headlines.render("a", h, RECORDS, "2026-10-23", "x")
    assert "**28.7%**" in body and "% %" not in body


def test_headlines_rerender_uses_the_saved_reply(tmp_path, monkeypatch):
    agent = setup(tmp_path, monkeypatch, {"headlines/a": [json.dumps({"headlines": [headline()]})]})
    assert headlines.main(tmp_path) == 0
    calls = len(agent.asked)
    page = next((tmp_path / "wiki/findings").glob("*.md"))
    page.write_text("edited by hand")
    monkeypatch.setattr(headlines, "RENDER", "finding-page@test")
    assert headlines.main(tmp_path) == 0
    assert len(agent.asked) == calls
    assert "## Evidence" in page.read_text()


def test_render_drops_a_percent_unit_the_value_shows():
    assert headlines.carries_unit("23.0%", "percent") and headlines.carries_unit("5", "")
    assert not headlines.carries_unit("13", "percentage points")


def test_headlines_salvage_reads_abbreviated_record_ids():
    rescue = headlines.salvager(RECORDS)
    reply = headlines.Reply.model_validate(TWO)
    kept = rescue(reply, [("The revised caveat for headline :0:1 misstates the null", reply)])
    assert kept is not None and [h.evidence for h in kept[0].headlines] == ["a:0:0"]
    assert rescue(reply, [("see :0:10 instead", reply)]) is None


def test_other_caveats_leave_out_figures_their_quote_lacks():
    derived = {
        "id": "a:0:3",
        "kind": "caveat",
        "claim": "51/8 is 6.375, so the 8x comparison is inconsistent",
        "quote": "The pathway needs 51 genes, over 8 times the core set.",
    }
    stated = {
        "id": "a:0:4",
        "kind": "caveat",
        "claim": "Only 12 conditions were assayed",
        "quote": "Only 12 conditions were assayed.",
    }
    h = headlines.Headline.model_validate(headline())
    _, _, body = headlines.render("a", h, [*RECORDS, derived, stated], "2026-10-23", "x")
    assert "Only 12 conditions were assayed" in body
    assert "6.375" not in body
