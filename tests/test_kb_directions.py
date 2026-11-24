"""The stateful directions job selects, checks and publishes one topic."""

from pathlib import Path

import pytest

from beril_wiki.agentic.runtime import file_hash
from beril_wiki.kb.jobs import Scope, write_state
from beril_wiki.kb.jobs.directions import jobs
from beril_wiki.kb.tools import Rejected
from beril_wiki.stages import cards, directions

SOURCE_FINDING = "alpha--1a2b3c4d"
OTHER_FINDING = "beta--2a3b4c5d"
CONFLICT = "conflict--shared--1234abcd"


@pytest.fixture
def direction_root(tmp_path: Path) -> Path:
    """Build two overlapping topics with findings from two reports."""
    write_state(
        tmp_path / "state/curator-topics.json",
        {
            "groups": [
                {"title": "Alpha", "concepts": ["shared", "alpha-only"]},
                {"title": "Zeta", "concepts": ["shared", "zeta-only"]},
            ],
        },
    )
    concepts = tmp_path / "wiki/concepts"
    concepts.mkdir(parents=True)
    (concepts / "shared.md").write_text("# Shared\n\nGrowth varied. [src: alpha, beta]\n")
    (concepts / "zeta-only.md").write_text("# Acetate\n\nGrowth varied. [src: alpha]\n")
    for source, fid in (("alpha", SOURCE_FINDING), ("beta", OTHER_FINDING)):
        cards.write_page(
            tmp_path / "wiki/findings" / f"{fid}.md",
            {"source": source, "description": "Yeast grew on acetate."},
            "# Growth on acetate",
        )
    cards.write_page(
        tmp_path / "wiki/conflicts" / f"{CONFLICT}.md",
        {},
        "# Growth on acetate\n\nYeast growth varied. [src: alpha, beta]",
    )
    return tmp_path


def proposal(number: int, *, finding: str = SOURCE_FINDING, **changes: object) -> dict:
    return directions.Direction.model_validate(
        {
            "id": f"D{number}",
            "title": "Does stored carbon sustain growth?",
            "question": "Can yeast grow on acetate using stored carbon?",
            "hypothesis": "Yeast releases stored carbon to sustain growth on acetate.",
            "why_it_matters": "It would explain how yeast survives changes in food supply.",
            "test": "Measure growth on acetate in yeast with and without carbon stores.",
            "outcomes": "Slower growth without stores supports it. Equal growth refutes it.",
            "approach": "experiment",
            "readiness": "needs new measurements",
            "readiness_basis": "The test requires fresh growth measurements.",
            "findings": [finding],
        }
        | changes
    ).model_dump()


def test_only_top_topic_is_owed_and_a_tie_breaks_alphabetically(direction_root: Path) -> None:
    root = direction_root
    ingested = Scope(root, "alpha", "ingest", run="ingest-alpha")
    revised = Scope(root, "alpha", "revise", run="revise-alpha")
    (job,) = jobs(ingested)
    assert job.key == "directions/zeta"
    assert (job.writer, job.reviewer) == ("cards", "card_review")
    assert [job.key for job in jobs(revised)] == ["directions/zeta"]

    reply = {"directions": [proposal(n) for n in (1, 2, 3)]}
    write_state(root / directions.STATE, {"zeta": {"input": "old-policy", "reply": reply}})
    assert jobs(revised) == []
    assert [job.key for job in jobs(ingested)] == ["directions/zeta"]

    (root / "wiki/concepts/alpha-only.md").write_text("# Other\n\nGrowth varied. [src: alpha]\n")
    assert [job.key for job in jobs(ingested)] == ["directions/alpha"]


def test_first_reply_uses_curator_checker_without_source_restriction(direction_root: Path) -> None:
    (job,) = jobs(Scope(direction_root, "alpha", "ingest"))
    reply = {"directions": [proposal(n, finding=OTHER_FINDING) for n in (1, 2, 3)]}
    assert job.pack["ACCEPTED"] == []
    assert job.check(reply) == reply
    with pytest.raises(Rejected) as refused:
        job.check({"directions": reply["directions"][:2]})
    assert "give 3 to 8 directions" in refused.value.objections


def test_live_accepted_directions_cannot_be_dropped_or_edited(direction_root: Path) -> None:
    root = direction_root
    live = [proposal(1), proposal(2, conflicts=[CONFLICT]), proposal(3, finding=OTHER_FINDING)]
    saved = {"directions": [*live, proposal(4, conflicts=["conflict--shared--gone"])]}
    write_state(root / directions.STATE, {"zeta": {"reply": saved, "failed": True}})
    assert jobs(Scope(root, "alpha", "revise")) == []
    (job,) = jobs(Scope(root, "alpha", "ingest"))
    # D4 builds on a conflict page that is gone, so it is not offered as accepted.
    assert job.pack["ACCEPTED"] == live
    assert job.pack["SOURCE"] == "alpha"
    accepted = {"directions": [*live, proposal(5), proposal(6)]}
    assert job.check(accepted) == accepted

    for altered in (
        [*live[1:], proposal(5)],
        [proposal(1, title="Will yeast store carbon?"), *live[1:]],
    ):
        with pytest.raises(Rejected) as refused:
            job.check({"directions": altered})
        assert any(
            "D1: return the accepted direction unchanged" in s for s in refused.value.objections
        )

    with pytest.raises(Rejected) as refused:
        job.check(
            {"directions": [*live, proposal(4), proposal(5), proposal(6, finding=OTHER_FINDING)]}
        )
    assert "add at most two new directions" in refused.value.objections
    assert (
        "D6: a new direction must build on at least one finding of alpha"
        in refused.value.objections
    )


def test_publish_uses_curator_shape_and_preserves_other_topics(direction_root: Path) -> None:
    root = direction_root
    scope = Scope(root, "alpha", "ingest", run="directions-run")
    (job,) = jobs(scope)
    reply = job.check(
        {
            "directions": [
                proposal(1, conflicts=[CONFLICT]),
                proposal(2, title="Can yeast rely on stored carbon?"),
                proposal(3, title="Does acetate change carbon storage?"),
            ]
        }
    )
    out = root / directions.OUT
    job.publish(reply)
    collision = next(p for p in out.glob("does-stored-carbon*"))
    other = {"input": "curator", "pages": {collision.name: "saved"}}
    state = cards.load_state(root / directions.STATE) | {"alpha": other}
    write_state(root / directions.STATE, state)
    cards.write_page(collision, {"topics": ["alpha"]}, "# Another topic's page")
    other_bytes = collision.read_bytes()
    stale = out / "retired.md"
    cards.write_page(stale, {"topics": ["zeta"]}, "# A stale direction")

    (job,) = jobs(scope)
    job.publish(job.check(reply))
    current = cards.load_state(root / directions.STATE)
    pages = directions.pages_for(out, "zeta")
    assert len(pages) == 3 and not stale.exists()
    assert collision.read_bytes() == other_bytes
    assert current == {
        "alpha": other,
        "zeta": {
            "input": "kb:directions-run",
            "render": directions.RENDER,
            "reply": reply,
            "pages": {page.name: file_hash(page) for page in pages},
        },
    }
    fields, body = cards.read_page(out / f"{collision.stem}-zeta.md")
    assert fields["type"] == "Research direction"
    assert fields["topics"] == ["zeta"]
    assert fields["builds_on"] == [f"findings/{SOURCE_FINDING}", f"conflicts/{CONFLICT}"]
    assert fields["projects"] == ["alpha", "beta"]
    assert "## What would support or refute it" in body
