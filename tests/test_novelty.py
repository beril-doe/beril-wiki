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
    # F4: the first judge's relations argued for the unconfirmed label, so none remain.
    assert entry["difference"] == "" and entry["closest"] == []


def test_decision_applies_before_the_first_durable_save(tmp_path, monkeypatch):
    """F3: a run stopped right after a label is saved still shows the person's decision."""
    decisions = tmp_path / "contract/novelty-decisions.yaml"
    decisions.parent.mkdir(parents=True, exist_ok=True)
    decisions.write_text(
        f"decisions:\n  - finding: {FID}\n    withdraw: true\n    reason: checked by hand\n"
    )
    saved: list[dict] = []
    real = novelty.atomic_json

    def first_save_then_stop(path, data):
        saved.append(json.loads(json.dumps(data)))
        real(path, data)
        raise novelty.WorkflowError("budget admission refused")

    monkeypatch.setattr(novelty, "atomic_json", first_save_then_stop)
    good = judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
    with pytest.raises(novelty.WorkflowError):
        run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [good]})
    on_disk = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert saved[0][FID]["label"] == novelty.NOT_ASSESSED
    assert on_disk["label"] == novelty.NOT_ASSESSED and on_disk["override"] == "checked by hand"


def test_decision_reaches_a_cached_label_before_any_job(tmp_path, monkeypatch):
    """A withdrawal for an already-labelled finding is saved even if the run stops at once."""
    good = judgment(novelty.EXTENDS, closest=(("111", "same relationship elsewhere"),))
    first, _ = run(tmp_path, monkeypatch, {f"novelty/{FID}/judge": [good]})
    assert first["label"] == novelty.EXTENDS
    decisions = tmp_path / "contract/novelty-decisions.yaml"
    decisions.parent.mkdir(parents=True, exist_ok=True)
    decisions.write_text(
        f"decisions:\n  - finding: {FID}\n    withdraw: true\n    reason: checked by hand\n"
    )
    # A second finding needs a label, and the run stops before any job finishes.
    other = tmp_path / "wiki/findings/b--9f8e7d6c.md"
    other.write_bytes((tmp_path / "wiki/findings" / f"{FID}.md").read_bytes())

    def stop(*_a, **_k):
        raise novelty.WorkflowError("budget admission refused")

    monkeypatch.setattr(cards, "parallel", stop)
    with pytest.raises(novelty.WorkflowError):
        novelty.main(tmp_path)
    on_disk = json.loads((tmp_path / "state/novelty.json").read_text())[FID]
    assert on_disk["label"] == novelty.NOT_ASSESSED and on_disk["override"] == "checked by hand"
    assert on_disk["pipeline_label"] == novelty.EXTENDS


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


@pytest.mark.parametrize("remove", [False, True])
def test_changed_cited_pmids_rejudge_only_the_affected_report(tmp_path, monkeypatch, remove):
    page(tmp_path)
    source = report(tmp_path, "a", "# A\n\nPMID: 12345\n")
    if remove:
        source.write_text(source.read_text() + "PMID: 67890\n")
    other = "b--9f8e7d6c"
    fields, body = cards.read_page(tmp_path / "wiki/findings" / f"{FID}.md")
    cards.write_page(
        tmp_path / "wiki/findings" / f"{other}.md",
        fields | {"source": "b"},
        body.replace("[src: a]", "[src: b]"),
    )
    report(tmp_path, "b", "# B\n\nPMID: 98765\n")
    agent = FakeAgent(tmp_path / "store", {})
    install(monkeypatch, agent)
    monkeypatch.setattr(novelty, "today", lambda: datetime.date(2026, 10, 23))
    judged = []

    def judge(fid, finding, cited, agent):
        judged.append((fid, cited))
        return {"label": novelty.INSUFFICIENT, "retrieved_on": "2026-10-23", "closest": []}

    monkeypatch.setattr(novelty, "judge", judge)
    assert novelty.main(tmp_path) == 0
    saved = json.loads((tmp_path / novelty.STATE).read_text())
    judged.clear()
    raw = b"# A\n\n35\xb0C\nPMID: 12345\n" + (b"" if remove else b"PMID: 67890\n")
    source.write_bytes(raw)
    assert novelty.main(tmp_path) == 0
    expected = ["12345"] if remove else ["12345", "67890"]
    assert judged == [(FID, expected)]
    updated = json.loads((tmp_path / novelty.STATE).read_text())
    assert updated[other] == saved[other]
    assert updated[FID]["input"] == saved[FID]["input"]
    assert updated[FID]["cited_pmids"] == expected
    judged.clear()
    assert novelty.main(tmp_path) == 0
    assert judged == [] and agent.asked == []
    assert source.read_bytes() == raw


def test_legacy_labels_backfill_citations_without_rejudging_or_changing_input(
    tmp_path, monkeypatch
):
    first, agent = run(tmp_path, monkeypatch, {}, papers={})
    path = tmp_path / novelty.STATE
    legacy = {key: value for key, value in first.items() if key != "cited_pmids"}
    path.write_text(json.dumps({FID: legacy}))
    source = report(tmp_path, "a", "# A\n\nPMID: 12345\n")
    raw = source.read_bytes() + b"\n35\xb0C\n"
    source.write_bytes(raw)
    asked = list(agent.asked)

    def no_judgment(*_args):
        raise AssertionError("a legacy label must not buy a new judgment")

    monkeypatch.setattr(novelty, "judge", no_judgment)
    assert novelty.main(tmp_path) == 0
    assert json.loads(path.read_text())[FID] == legacy | {"cited_pmids": ["12345"]}
    assert agent.asked == asked
    assert source.read_bytes() == raw


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
