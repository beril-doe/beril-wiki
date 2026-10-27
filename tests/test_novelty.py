"""The novelty stage: literature labels with verified PMIDs and a cross-vendor guard."""

import datetime
import json
from urllib.parse import parse_qs, urlsplit

import pytest

from beril_wiki.stages import cards, novelty
from card_fakes import FakeAgent, install, report

FID = "a--1a2b3c4d"
PAPERS = {
    "111": "Depletion in E. coli\nABSTRACT (not full text):\nx",
    "222": "Unrelated\nABSTRACT:\ny",
}
CROSS: dict = {
    "model": "claude-sonnet-5-5",
    "step_models": {"review": "gpt-6.1-sol", "queries": "gpt-6.1-sol"},
}


def page(root):
    cards.write_page(
        root / "wiki/findings" / f"{FID}.md",
        {
            "type": "Finding",
            "description": "Dark genes were depleted.",
            "result": "observation",
            "source": "a",
        },
        "# Depleted\n\nDark genes were depleted. [src: a]\n\n"
        "## Evidence\n\n> Dark genes were depleted. [src: a]\n",
    )
    report(root, "a", "# A\n\nRefs: PMID: 333\n")


def judgment(
    label, closest=(("111", "related"),), difference="Adds archaea; PMID 111 studied E. coli."
):
    return json.dumps(
        {
            "label": label,
            "difference": difference,
            "closest": [{"pmid": p, "relation": r} for p, r in closest],
        }
    )


def run(
    tmp_path, monkeypatch, replies, papers=PAPERS, config=CROSS, day=datetime.date(2026, 10, 23)
):
    page(tmp_path)
    agent = FakeAgent(
        tmp_path / "store",
        {f"novelty/{FID}/queries": ['{"queries": ["dark genes stress"]}']} | replies,
    )
    agent.config = config
    install(monkeypatch, agent)
    monkeypatch.setattr(novelty, "today", lambda: day)
    monkeypatch.setattr(novelty, "search_ids", lambda q: list(papers))
    monkeypatch.setattr(
        novelty, "fetch_abstracts", lambda ids: {i: papers[i] for i in ids if i in papers}
    )
    assert novelty.main(tmp_path) == 0
    return json.loads((tmp_path / "state/novelty.json").read_text())[FID], agent


def test_novelty_empty_retrieval_is_insufficient(tmp_path, monkeypatch):
    entry, agent = run(tmp_path, monkeypatch, {}, papers={})
    assert entry["label"] == novelty.INSUFFICIENT
    assert f"novelty/{FID}/judge" not in agent.asked


def test_novelty_closest_pmids_must_be_retrieved(tmp_path, monkeypatch):
    bad = judgment(novelty.EXTENDS, closest=(("999", "same relationship elsewhere"),))
    good = judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
    entry, agent = run(
        tmp_path,
        monkeypatch,
        {f"novelty/{FID}/judge": [bad], f"novelty/{FID}/judge/repair": [good]},
    )
    assert entry["label"] == novelty.EXTENDS
    assert entry["closest"][0]["title"] == "Depletion in E. coli"
    assert entry["retrieved_on"] == "2026-10-23" and entry["abstracts_only"] is True
    assert entry["candidates"] == ["111", "222"]


def test_novelty_disagreement_takes_weaker_label(tmp_path, monkeypatch):
    replies = {
        f"novelty/{FID}/judge": [judgment(novelty.NOVEL)],
        f"novelty/{FID}/agree": [
            '{"label": "Extends retrieved work", "reason": "PMID 111 reports it."}'
        ],
    }
    entry, _ = run(tmp_path, monkeypatch, replies)
    assert entry["label"] == novelty.EXTENDS and entry["agreed"] is False
    assert entry["judged_label"] == novelty.NOVEL


def test_novelty_agreement_keeps_candidate_novel(tmp_path, monkeypatch):
    replies = {
        f"novelty/{FID}/judge": [judgment(novelty.NOVEL)],
        f"novelty/{FID}/agree": ['{"label": "Candidate novel", "reason": "None report it."}'],
    }
    entry, _ = run(tmp_path, monkeypatch, replies)
    assert entry["label"] == novelty.NOVEL and entry["agreed"] is True
    assert entry["agree_model"] == "gpt-6.1-sol"


def test_novelty_novel_cannot_cite_a_paper_reporting_the_relationship(tmp_path, monkeypatch):
    with pytest.raises(cards.CandidateError):
        novelty.judgment_checker(PAPERS)(judgment(novelty.NOVEL, closest=(("111", "same result"),)))


def test_novelty_same_vendor_cannot_award_novel(tmp_path, monkeypatch):
    same = {"model": "claude-sonnet-5-5", "step_models": {"review": "claude-opus-5-5"}}
    entry, agent = run(
        tmp_path, monkeypatch, {f"novelty/{FID}/judge": [judgment(novelty.NOVEL)]}, config=same
    )
    assert entry["label"] == novelty.INSUFFICIENT
    assert f"novelty/{FID}/agree" not in agent.asked


def test_novelty_keeps_previous_label_on_retrieval_failure(tmp_path, monkeypatch):
    first, _ = run(
        tmp_path,
        monkeypatch,
        {
            f"novelty/{FID}/judge": [
                judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
            ]
        },
    )
    (tmp_path / "wiki/findings" / f"{FID}.md").write_text(
        (tmp_path / "wiki/findings" / f"{FID}.md")
        .read_text()
        .replace("depleted.", "depleted under stress.")
    )

    def down(query):
        raise OSError("NCBI unreachable")

    agent = FakeAgent(tmp_path / "store", {f"novelty/{FID}/queries": ['{"queries": ["other"]}']})
    agent.config = CROSS
    install(monkeypatch, agent)
    monkeypatch.setattr(novelty, "search_ids", down)
    assert novelty.main(tmp_path) == 0
    entry = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert entry["label"] == first["label"] and entry["retrieved_on"] == first["retrieved_on"]
    assert entry["failed"] is True


def test_novelty_first_failure_shows_not_assessed(tmp_path, monkeypatch):
    page(tmp_path)
    agent = FakeAgent(tmp_path / "store", {f"novelty/{FID}/queries": ['{"queries": ["q"]}']})
    agent.config = CROSS
    install(monkeypatch, agent)
    monkeypatch.setattr(novelty, "search_ids", lambda q: (_ for _ in ()).throw(OSError("down")))
    assert novelty.main(tmp_path) == 0
    assert (
        json.loads((tmp_path / "state/novelty.json").read_text())[FID]["label"]
        == novelty.NOT_ASSESSED
    )


def test_novelty_override_pins_and_withdraws(tmp_path, monkeypatch):
    run(
        tmp_path,
        monkeypatch,
        {
            f"novelty/{FID}/judge": [
                judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
            ]
        },
    )
    decisions = tmp_path / "contract/novelty-decisions.yaml"
    decisions.parent.mkdir(exist_ok=True)
    decisions.write_text(
        f"decisions:\n  - finding: {FID}\n    withdraw: true\n    reason: checked by hand\n"
    )
    assert novelty.main(tmp_path) == 0
    entry = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert entry["label"] == novelty.NOT_ASSESSED and entry["override"] == "checked by hand"
    decisions.write_text("decisions: []\n")
    assert novelty.main(tmp_path) == 0
    assert (
        json.loads((tmp_path / "state/novelty.json").read_text())[FID]["label"] == novelty.EXTENDS
    )


def test_novelty_refreshes_after_90_days(tmp_path, monkeypatch):
    good = judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
    _, agent = run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [good]})
    assert novelty.main(tmp_path) == 0  # fresh: no new calls
    assert agent.asked.count(f"novelty/{FID}/judge") == 1
    later = FakeAgent(
        tmp_path / "store",
        {
            f"novelty/{FID}/queries": ['{"queries": ["dark genes stress"]}'],
            f"novelty/{FID}/judge": [good],
        },
    )
    later.config = CROSS
    install(monkeypatch, later)
    monkeypatch.setattr(novelty, "today", lambda: datetime.date(2027, 2, 1))
    assert novelty.main(tmp_path) == 0
    entry = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert entry["retrieved_on"] == "2027-02-01"


def test_cited_pmids_reads_report_references():
    assert novelty.cited_pmids(
        "x PMID: 29769716 y https://pubmed.ncbi.nlm.nih.gov/30617347/ PMID 29769716"
    ) == [
        "29769716",
        "30617347",
    ]


def test_abstracts_are_fetched_in_batches_under_the_size_cap(monkeypatch):
    from beril_wiki.stages import literature as L

    asked: list[list[str]] = []

    def fake_get(url, cap=None):
        ids = parse_qs(urlsplit(url).query)["id"][0].split(",")
        asked.append(ids)
        return b"<PubmedArticleSet/>"

    monkeypatch.setattr(L, "paced_get", fake_get)
    monkeypatch.setattr(L, "abstracts_from_xml", lambda raw, ids: {i: "abstract" for i in ids})
    got = novelty.fetch_abstracts([str(n) for n in range(25)])
    assert [len(b) for b in asked] == [10, 10, 5]
    assert sorted(got, key=int) == [str(n) for n in range(25)]


def test_an_oversized_record_is_skipped_not_fatal(monkeypatch, capsys):
    from beril_wiki.stages import literature as L

    def fake_get(url, cap=None):
        ids = parse_qs(urlsplit(url).query)["id"][0].split(",")
        return b"x" * (cap or 0) if "2" in ids else ("|".join(ids)).encode()

    monkeypatch.setattr(L, "paced_get", fake_get)
    monkeypatch.setattr(
        L, "abstracts_from_xml", lambda raw, ids: {i: "a" for i in raw.decode().split("|")}
    )
    got = novelty.fetch_abstracts(["1", "2", "3"])
    assert sorted(got) == ["1", "3"]
    assert "PMID 2" in capsys.readouterr().out
