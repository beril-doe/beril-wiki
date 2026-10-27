"""The directions stage: research questions grounded in findings, never reanalysis."""

import json

import pytest

from beril_wiki.agentic.runtime import JobFailed, Refused
from beril_wiki.stages import cards, directions
from card_fakes import FakeAgent, install, report, scope

TOPIC = "dark-matter"
FID = "a--1a2b3c4d"
CONFLICT = "conflict--gap--1234abcd"


def corpus(root):
    (root / "state").mkdir(parents=True, exist_ok=True)
    (root / "state/curator-topics.json").write_text(
        json.dumps({"groups": [{"title": "Dark Matter", "concepts": ["gap"]}]})
    )
    (root / "wiki/concepts").mkdir(parents=True)
    (root / "wiki/concepts/gap.md").write_text(
        "# Gap\n\nDark genes. [src: a]\n\n## Open Directions\n\n"
        "- Recompute the stress rates per experiment. [src: a]\n"
        "- Test whether dark genes encode transporters. [src: a]\n"
    )
    (root / "wiki/conflicts").mkdir(parents=True)
    (root / "wiki/conflicts" / f"{CONFLICT}.md").write_text(
        "<!-- tension-hash: 1 -->\n# Stress dominance versus depletion\n\n"
        "Two projects disagree about stress (28.7% vs 43.2%). [src: a, b]\n\n"
        "## Evidence Sides\n\nSide A says stress dominates. [src: b]\n"
    )
    (root / "wiki/data").mkdir(parents=True)
    (root / "wiki/data/kbase-ke-pangenome.md").write_text("# KBase pangenome\n")
    cards.write_page(
        root / "wiki/findings" / f"{FID}.md",
        {
            "description": "Truly dark genes are depleted in stress (28.7% vs 43.2%).",
            "source": "a",
            "result": "null result",
            "caveat": "Only 48 organisms.",
        },
        "# Dark genes avoid stress\n\nClaim. [src: a]\n",
    )
    (root / "state/novelty.json").write_text(
        json.dumps(
            {
                FID: {
                    "label": "Candidate novel",
                    "retrieved_on": "2026-10-23",
                    "difference": "No paper compares conditions.",
                    "closest": [
                        {"pmid": "29769716", "title": "Mutant phenotypes", "relation": "related"}
                    ],
                    "candidates": ["29769716"],
                }
            }
        )
    )
    report(root, "a", "# A\n")
    report(root, "b", "# B\n")
    scope(root, reports=["a"], topics=[TOPIC])


def direction(**kw):
    return {
        "id": "D1",
        "title": "Dark genes as nutrient and community-interaction genes",
        "question": "Do dark genes with strong phenotypes act in nutrient uptake?",
        "hypothesis": "Their fitness profiles co-vary with known transporter genes.",
        "why_it_matters": "It would move annotation screens toward nutrient conditions.",
        "test": "Cofitness of dark genes with transporter genes across Fitness Browser organisms.",
        "outcomes": "Higher cofitness with transporters supports it; none refutes it.",
        "approach": "lakehouse analysis",
        "collections": ["kbase_ke_pangenome"],
        "readiness": "data in the lakehouse",
        "readiness_basis": "Fitness data are in the lakehouse.",
        "findings": [FID],
        "conflicts": [CONFLICT],
        "papers": ["29769716"],
        "prior_work": "PMID 29769716 maps phenotypes but not condition classes.",
    } | kw


def reply(*items):
    return json.dumps({"directions": list(items)})


THREE = reply(
    direction(),
    direction(
        id="D2",
        title="Iron limitation as the niche of truly dark genes",
        question="Is iron the niche?",
    ),
    direction(
        id="D3",
        title="Community interaction genes hidden among hypotheticals",
        question="Do they mediate interactions?",
    ),
)


def run(tmp_path, monkeypatch, replies, **kw):
    corpus(tmp_path)
    agent = FakeAgent(tmp_path / "store", replies, **kw)
    install(monkeypatch, agent)
    assert directions.main(tmp_path) == 0
    return agent


def test_directions_writes_grounded_pages(tmp_path, monkeypatch):
    agent = run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    pages = sorted((tmp_path / "wiki/directions").glob("*.md"))
    assert len(pages) == 3
    fields, body = cards.read_page(pages[0])
    assert fields["type"] == "Research direction" and fields["topics"] == [TOPIC]
    assert (
        f"findings/{FID}" in fields["builds_on"] and f"conflicts/{CONFLICT}" in fields["builds_on"]
    )
    assert "## Hypothesis" in body and "## Closest published work" in body
    assert "[[data/kbase-ke-pangenome|KBase pangenome]]" in body
    assert f"directions/{TOPIC}/science-review" in agent.asked


def test_pack_leaves_reanalysis_proposals_out(tmp_path):
    corpus(tmp_path)
    pack = directions.topic_pack(tmp_path, TOPIC, ["a"])
    assert pack["PROPOSALS"] == ["Test whether dark genes encode transporters. [src: a]"]
    assert [f["id"] for f in pack["FINDINGS"]] == [FID]
    assert pack["PAPERS"] == [{"pmid": "29769716", "title": "Mutant phenotypes"}]


@pytest.mark.parametrize(
    ("change", "message"),
    [
        ({"title": "Recompute stress rates per experiment"}, "repeats or corrects"),
        (
            {"question": "Should we re-run the comparison with one threshold?"},
            "repeats or corrects",
        ),
        ({"findings": [], "conflicts": []}, "builds on no finding"),
        ({"findings": ["a--deadbeef"]}, "unknown finding ids"),
        ({"papers": ["11111111"]}, "not in PAPERS"),
        ({"prior_work": "PMID 22222222 already did this."}, "not in PAPERS"),
        ({"collections": ["kbase_made_up"]}, "not in COLLECTIONS"),
        ({"hypothesis": "Depletion reaches 61.5% in iron."}, "61.5"),
    ],
)
def test_checker_rejects(tmp_path, change, message):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    bad = reply(direction(**change), *json.loads(THREE)["directions"][1:])
    with pytest.raises(cards.CandidateError, match=message):
        parse(bad)
    assert parse(THREE).directions


def test_salvage_drops_only_named_directions(tmp_path, monkeypatch):
    objection = ["Direction 2 overstates the iron enrichment"]
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": objection},
        still_open={f"directions/{TOPIC}": objection},
    )
    titles = [
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    ]
    # "Direction 2" is index 1 counted from 1 and index 2 from 0: both are dropped.
    assert titles == ["# Dark genes as nutrient and community-interaction genes"]


def test_unchanged_input_makes_no_calls_and_rerenders_from_reply(tmp_path, monkeypatch):
    agent = run(tmp_path, monkeypatch, {f"directions/{TOPIC}": [THREE]})
    calls = len(agent.asked)
    page = next((tmp_path / "wiki/directions").glob("*.md"))
    page.write_text("edited")
    assert directions.main(tmp_path) == 0
    assert len(agent.asked) == calls
    assert "## Hypothesis" in page.read_text()


def test_is_reanalysis_reads_the_opening_clause():
    assert cards.is_reanalysis("Using the metadata, recompute rates per experiment.")
    assert cards.is_reanalysis("Reconcile the two counts.")
    assert not cards.is_reanalysis(
        "Test whether dark genes encode transporters across 48 organisms."
    )


@pytest.mark.parametrize(
    "error",
    [
        JobFailed("Codex turn failed: This content was flagged for possible biological risk."),
        Refused("refused on claude-opus-5", "claude-opus-5"),
    ],
)
def test_content_refusal_fails_only_its_topic(tmp_path, monkeypatch, capsys, error):
    agent = run(
        tmp_path,
        monkeypatch,
        {f"directions/{TOPIC}": [THREE]},
        review_error={f"directions/{TOPIC}": error},
    )
    assert f"directions/{TOPIC}/science-review" in agent.asked
    assert not list((tmp_path / "wiki/directions").glob("*.md"))
    assert f"[FAILED] directions/{TOPIC}" in capsys.readouterr().out


def test_other_job_failures_still_stop_the_stage(tmp_path, monkeypatch):
    with pytest.raises(JobFailed, match="transport"):
        run(
            tmp_path,
            monkeypatch,
            {f"directions/{TOPIC}": [THREE]},
            review_error={f"directions/{TOPIC}": JobFailed("Codex transport failed: reset")},
        )


def renamed(n, title):
    items = json.loads(THREE)["directions"]
    items[n] = items[n] | {"title": title, "question": "A rewritten question about it?"}
    return reply(*items)


def test_salvage_follows_a_rewritten_direction_by_id(tmp_path, monkeypatch):
    objection = ["D2 overstates the iron enrichment"]
    rewritten = renamed(1, "Iron scarcity selects for truly dark genes")
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [rewritten] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": objection},
        still_open={f"directions/{TOPIC}": objection},
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert titles == [
        "# Community interaction genes hidden among hypotheticals",
        "# Dark genes as nutrient and community-interaction genes",
    ]


def test_salvage_reads_a_restated_issue_through_its_original(tmp_path, monkeypatch):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D3 has no decisive test"]},
        still_open={f"directions/{TOPIC}": ["Issue 0 remains: the test is still not decisive"]},
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert "# Community interaction genes hidden among hypotheticals" not in titles
    assert len(titles) == 2


def test_checker_rejects_repeated_ids(tmp_path):
    corpus(tmp_path)
    parse = directions.checker(directions.topic_pack(tmp_path, TOPIC, ["a"]))
    items = json.loads(THREE)["directions"]
    with pytest.raises(cards.CandidateError, match="repeated"):
        parse(reply(items[0], items[1] | {"id": "D1"}, items[2]))


def test_a_refused_verification_fails_the_topic_without_salvage(tmp_path, monkeypatch, capsys):
    refusal = JobFailed("Codex turn failed: flagged for possible biological risk")
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        review_error={},
        verify_error={f"directions/{TOPIC}": refusal},
    )
    out = capsys.readouterr().out
    assert "[SALVAGED]" not in out and f"[FAILED] directions/{TOPIC}" in out
    assert not list((tmp_path / "wiki/directions").glob("*.md"))


def test_a_new_objection_that_mentions_an_old_issue_names_its_own_item(tmp_path, monkeypatch):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        still_open={
            f"directions/{TOPIC}": ["D3 adds an unsupported mechanism while fixing issue 0"]
        },
    )
    titles = sorted(
        cards.read_page(p)[1].splitlines()[0] for p in (tmp_path / "wiki/directions").glob("*.md")
    )
    assert titles == [
        "# Dark genes as nutrient and community-interaction genes",
        "# Iron limitation as the niche of truly dark genes",
    ]


def test_an_unresolvable_restatement_fails_the_topic(tmp_path, monkeypatch, capsys):
    replies = {f"directions/{TOPIC}": [THREE], f"directions/{TOPIC}/repair": [THREE] * 3}
    run(
        tmp_path,
        monkeypatch,
        replies,
        objections={f"directions/{TOPIC}": ["D2 overstates the iron enrichment"]},
        still_open={f"directions/{TOPIC}": ["Issue 7 remains: the test is not decisive"]},
    )
    assert f"[FAILED] directions/{TOPIC}" in capsys.readouterr().out
