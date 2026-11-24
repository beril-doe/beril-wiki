"""Corpus scheduling and idempotent publication for record stages."""

import json
from dataclasses import replace
from pathlib import Path

import pytest

from beril_wiki.kb.jobs import (
    Scope,
    authors,
    conflicts,
    directions,
    figures,
    followups,
    literature,
    topics,
    write_state,
)
from beril_wiki.kb.jobs import links as links_jobs
from beril_wiki.kb.jobs import shared as shared_jobs
from beril_wiki.kb.tools import Rejected
from beril_wiki.stages import cards, links, shared
from card_fakes import lakehouse
from test_kb import root as root
from test_kb_conflicts import PAGE as CONFLICT_PAGE
from test_kb_conflicts import scope as conflict_scope
from test_kb_directions import OTHER_FINDING, direction_root, proposal
from test_kb_figures import EMBED, PAGE, SUMMARY, TOPIC, put
from test_kb_links import PAIR_LABEL, A, B, C, D
from test_kb_links import scope as link_scope
from test_kb_outcomes import TABLE, direction
from test_kb_topics import QUERIES, SECTION

__all__ = ["conflict_scope", "direction_root", "link_scope"]


def corpus(root: Path, *sources: str) -> Scope:
    """Compile scope has no triggering report or run-local scheduling hints."""
    return Scope(root, "", "compile", sources=list(sources), run="compile-1")


def test_topics_write_only_missing_hubs_from_fixed_membership(root: Path) -> None:
    groups = [
        {"title": "Growth Research", "concepts": ["growth-yield"]},
        {"title": "Already Written", "concepts": []},
    ]
    write_state(root / topics.STATE, {"groups": groups})
    put(
        root,
        "knowledge/topics.json",
        json.dumps(
            [{"slug": "growth-research", "title": "Growth Research", "scope": "Culture growth."}]
        ),
    )
    put(root, "wiki/topics/already-written.md", "# Already Written\n")
    scope = corpus(root, "alpha", "beta")

    (job,) = topics.jobs(scope)
    assert job.key == job.creates == "topics/growth-research"
    assert job.tools == "record"
    assert job.pack["TOPIC"] == {"title": "Growth Research", "description": "Culture growth."}
    assert "concepts/growth-yield" in job.pack["MEMBER CONCEPT PAGES"]
    with pytest.raises(Rejected):
        job.check({"page": "# Renamed\n\nA new topic."})

    clause = "These studies compare the growth of cells in cultures using different substrates. "
    body = (
        "# Growth Research\n\nStudies of how cultures grow.\n\n"
        "## What the Corpus Shows\n\n"
        + clause
        * 70
        + "\n\n## Tensions and Caveats\n\nCompare the conditions before interpreting the results."
        "\n\n## Where to Go Deeper\n\nStart with the concept page."
    )
    job.publish(job.check({"page": body}))
    hub = root / "wiki/topics/growth-research.md"
    assert "[[concepts/growth-yield]]" in hub.read_text(encoding="utf-8")
    assert cards.read_page(hub)[0]["description"] == "Culture growth."
    assert cards.load_state(root / topics.STATE) == {"groups": groups}
    assert topics.jobs(scope) == []


def test_conflicts_owe_tensions_outside_the_run_edits(conflict_scope: Scope) -> None:
    scope = corpus(conflict_scope.root, "alpha", "beta")
    (job,) = conflicts.jobs(scope)
    assert job.key.startswith("conflicts/conflict--growth-yield--")
    assert "Yield was 0.42 g/g" in job.pack["SOURCE EXCERPTS (verification only)"]
    job.publish(job.check({"page": CONFLICT_PAGE}))
    assert (scope.root / "wiki" / f"{job.creates}.md").is_file()
    assert conflicts.jobs(scope) == []


def test_links_batch_unanswered_pairs_and_references_from_all_reports(link_scope: Scope) -> None:
    scope = corpus(link_scope.root, "alpha", "beta", "gamma", "delta")
    saved = {"relation": "same result", "label": PAIR_LABEL}
    path = scope.root / links.STATE
    write_state(path, {"candidates": {f"pair:{A}|{B}": saved}})
    pair, *refs = links_jobs.jobs(scope)
    assert {
        item["report"] for comparison in pair.pack["PAIRS"].values() for item in comparison.values()
    } == {"gamma", "delta"}
    assert {job.pack["REPORT"] for job in refs} == {"Alpha study", "Beta study", "Gamma study"}
    pair.publish(
        pair.check({"items": [{"id": "P1", "relation": "same result", "label": PAIR_LABEL}]})
    )
    for job in refs:
        job.publish(
            job.check(
                {
                    "items": [
                        {"id": ref_id, "relation": "not a reference", "label": ""}
                        for ref_id in job.pack["NAMED"]
                    ]
                }
            )
        )
    assert len(cards.load_state(path)["candidates"]) == 5
    assert links_jobs.jobs(scope) == []


def test_shared_stores_unanswered_groups_from_all_reports(link_scope: Scope) -> None:
    scope = corpus(link_scope.root, "alpha", "beta", "gamma", "delta")
    write_state(
        scope.root / links.STATE,
        {
            "links": [
                {"a": a, "b": b, "level": "finding", "type": "same result", "label": PAIR_LABEL}
                for a, b in ((A, B), (D, C))
            ]
        },
    )
    owed = shared_jobs.jobs(scope)
    assert {job.key for job in owed} == {
        f"shared/{shared.group_id([A, B])}",
        f"shared/{shared.group_id([D, C])}",
    }
    for job in owed:
        record = {
            "title": "Essential genes across genomes",
            "sentence": "The projects share an analysis of how often essential genes are core.",
            "question": "How often are essential genes core?",
            "lanes": {fid: "Essential genes" for fid in job.pack["RESULTS"]},
            "how": "Both reports draw on the same analysis of shared data.",
        }
        job.publish(job.check(record))
    assert shared_jobs.jobs(scope) == []


def test_directions_owe_each_topic_with_findings_and_keep_accepted_empty_replies(
    direction_root: Path,
) -> None:
    scope = corpus(direction_root, "alpha", "beta")
    state = direction_root / topics.STATE
    groups = cards.load_state(state)["groups"] + [{"title": "Empty", "concepts": []}]
    write_state(state, {"groups": groups})
    alpha, zeta = directions.jobs(scope)
    assert (alpha.key, zeta.key) == ("directions/alpha", "directions/zeta")
    assert alpha.pack["MAX_NEW"] == 5
    assert all(len(json.dumps(job.pack, ensure_ascii=False)) <= 120_000 for job in (alpha, zeta))
    with pytest.raises(Rejected, match="at most 5"):
        alpha.check({"directions": [proposal(n, finding=OTHER_FINDING) for n in range(1, 7)]})
    alpha.publish(alpha.check({"directions": [proposal(1, finding=OTHER_FINDING)]}))
    zeta.publish(zeta.check({"directions": []}))

    assert list((direction_root / "wiki/directions").glob("*.md"))
    assert directions.jobs(replace(scope, run="compile-2")) == []


def test_followups_find_unlabelled_directions_without_an_accepted_topic_event(
    tmp_path: Path,
) -> None:
    lakehouse(tmp_path)
    direction(tmp_path, "growth", "growth")
    direction(tmp_path, "yield", "yield")
    scope = corpus(tmp_path, "alpha", "beta")
    owed = followups.jobs(scope)
    assert [job.key for job in owed] == ["followups/growth", "followups/yield"]
    for job in owed:
        assert job.pack["DIRECTION_TABLES"] == [TABLE]
        assert len(json.dumps(job.pack, ensure_ascii=False)) < 40_000
        job.publish(
            job.check(
                {
                    "need": "experiment",
                    "first_step_existing": False,
                    "data_unclear": False,
                    "reason": "Growth measurements decide the question.",
                    "tables": [],
                }
            )
        )
    assert followups.jobs(scope) == []


def test_literature_publishes_concepts_and_topics_with_the_same_slug(
    root: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    concept = root / "wiki/concepts/growth-yield.md"
    topic = put(root, "wiki/topics/growth-yield.md", "# Growth yield\n\nStudy of culture growth.\n")
    put(root, "wiki/concepts/index.md", "# Concepts index\n")
    scope = corpus(root, "alpha", "beta")
    monkeypatch.setattr(
        literature,
        "fetch_candidates",
        lambda _: {"12345": "Growth varies with culture conditions."},
    )
    queries = literature.query_jobs(scope)
    assert [job.key for job in queries] == [
        "literature/concepts/growth-yield/queries",
        "literature/growth-yield/queries",
    ]
    for job in queries:
        job.publish(job.check({"queries": QUERIES}))
    assert literature.query_jobs(scope) == []

    concept_job, topic_job = literature.section_jobs(scope)
    concept_job.publish(concept_job.check({"section": "NONE"}))
    topic_job.publish(topic_job.check({"section": SECTION}))
    assert "## Literature Context" not in concept.read_text(encoding="utf-8")
    assert "## Literature Context" in topic.read_text(encoding="utf-8")
    later = replace(scope, run="compile-2")
    assert literature.query_jobs(later) == literature.section_jobs(later) == []


def test_authors_owe_one_contribution_for_each_corpus_author(root: Path) -> None:
    put(root, "wiki/summaries/alpha__REPORT.md", "# Alpha\n\nGrowth changed.\n")
    put(root, "wiki/sources/alpha__REPORT.md", "# Alpha\n\nGrowth changed.\n")
    for name, sources in (("alex", ("alpha", "beta")), ("blair", ("beta",)), ("casey", ("other",))):
        projects = "\n".join(f"- [[summaries/{source}__REPORT]]" for source in sources)
        put(root, f"wiki/authors/{name}.md", f"# {name.title()}\n\n## Projects\n\n{projects}\n")
    scope = corpus(root, "alpha", "beta")

    alex, blair = authors.jobs(scope)
    assert (alex.key, blair.key) == ("authors/alex", "authors/blair")
    assert "summaries/alpha__REPORT" in alex.pack["SUMMARIES"]
    assert "summaries/alpha__REPORT" not in blair.pack["SUMMARIES"]
    for job in (alex, blair):
        job.publish(job.check({"section": "## Contributions\n\nBeta studied growth [src: beta]."}))
    assert authors.jobs(replace(scope, run="compile-2")) == []


def test_figures_copy_all_report_assets_and_schedule_untouched_pages(tmp_path: Path) -> None:
    for source in ("alpha", "beta"):
        put(tmp_path, f"corpus/projects/{source}/REPORT.md", f"# Report\n\n![caption]({EMBED})\n")
        put(tmp_path, f"corpus/projects/{source}/{EMBED}", source)
    put(tmp_path, f"wiki/{SUMMARY}.md", PAGE)
    put(tmp_path, f"wiki/{TOPIC}.md", PAGE.replace("alpha", "beta"))
    put(tmp_path, "wiki/concepts/unplaced.md", PAGE)
    scope = corpus(tmp_path, "alpha", "beta")

    summary, topic = figures.jobs(scope)
    assert (summary.key, topic.key) == (f"figures/{SUMMARY}", f"figures/{TOPIC}")
    assert [c["project"] for c in topic.pack["CANDIDATE_FIGURES"]] == ["beta"]
    for job in (summary, topic):
        job.publish(job.check({"placements": [{"figure": 0, "after_paragraph": 0}]}))
    assert set(cards.load_state(tmp_path / figures.MANIFEST)) == {"alpha", "beta"}
    assert figures.jobs(replace(scope, run="compile-2")) == []
