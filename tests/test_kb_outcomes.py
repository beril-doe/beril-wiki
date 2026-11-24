"""Verify which labels the stateful pipeline owes and what the publisher receives."""

from pathlib import Path

import pytest

from beril_wiki.kb.jobs import Scope, write_state
from beril_wiki.kb.jobs import followups as followup_jobs
from beril_wiki.kb.jobs import outcomes as outcome_jobs
from beril_wiki.kb.tools import Rejected
from beril_wiki.publish.cards.corpus import accepted
from beril_wiki.stages import cards, classify, followups, outcomes
from card_fakes import lakehouse

TABLE = "kescience.fitnessbrowser.experiment"
MODEL = "claude-labels"


def finding(root: Path, fid: str, result: str = "null result") -> None:
    """Write a finding in the curator's page format."""
    cards.write_page(
        root / outcomes.FINDINGS / f"{fid}.md",
        {"description": "Growth was similar.", "result": result, "source": fid.rpartition("--")[0]},
        "# Similar growth\n\n## Evidence\n\n> Growth was similar in both cultures.\n\n"
        "## Caveat\n\n> Both cultures used the same strain.\n",
    )


def direction(root: Path, did: str, topic: str) -> None:
    """Write a direction whose slug is independent of its topic."""
    cards.write_page(
        root / followups.DIRECTIONS / f"{did}.md",
        {"topics": [topic], "hypothesis": "Temperature changes growth.", "tables": [TABLE]},
        "# Does temperature change growth?\n\n## How to test it\n\n"
        "Grow strains at two temperatures.",
    )


def test_outcomes_owe_only_listed_findings_of_the_run_source(tmp_path: Path) -> None:
    """Reject re-labeling an accepted finding, an unlisted one, or another report's."""
    gists = {"gist": "Growth was similar in both cultures.", "case": "measured absence"}
    write_state(
        tmp_path / outcomes.GISTS,
        {
            "alpha--new": gists | {"title": "Growth stays similar"},
            "alpha--saved": gists,
            "alpha--retry": gists,
            "alpha--repeat": gists | {"repeats": "alpha--saved"},
            "alpha--unmeasured": gists | {"case": "missing data"},
            "alpha--other--new": gists,
        },
    )
    for fid in classify.load(tmp_path / outcomes.GISTS):
        finding(tmp_path, fid)
    state_path = tmp_path / outcomes.STATE
    saved = {
        "input": "old-policy-hash",
        "type": "negative",
        "reason": "The two cultures grew similarly.",
    }
    write_state(state_path, {"alpha--saved": saved, "alpha--retry": saved | {"failed": True}})
    scope = Scope(tmp_path, "alpha", "ingest")

    new, retry = outcome_jobs.jobs(scope)
    assert [new.key, retry.key] == ["outcomes/alpha--new", "outcomes/alpha--retry"]
    assert new.pack["FINDING"]["title"] == "Growth stays similar"
    assert new.pack["FINDING"]["caveat_quote"] == "Both cultures used the same strain."
    write_state(state_path, {f"alpha--{name}": saved for name in ("new", "saved", "retry")})
    assert outcome_jobs.jobs(scope) == []


def test_outcome_job_rejects_bad_reason_and_publishes_the_label(tmp_path: Path) -> None:
    """Catch a bypassed outcome checker or a state update that drops another label."""
    fid = "alpha--new"
    finding(tmp_path, fid)
    write_state(
        tmp_path / outcomes.GISTS,
        {fid: {"gist": "Growth was similar.", "case": "measured absence"}},
    )
    state_path = tmp_path / outcomes.STATE
    prior = {"input": "old", "type": "positive", "reason": "The groups grew at different rates."}
    write_state(state_path, {"beta--saved": prior})
    (job,) = outcome_jobs.jobs(Scope(tmp_path, "alpha", "ingest", "run", models={"labels": MODEL}))

    assert (job.writer, job.reviewer) == ("labels", "card_review")
    with pytest.raises(Rejected) as refused:
        job.check({"type": "negative", "reason": "Too short."})
    assert "reason has 2 words" in refused.value.objections
    reason = "The two cultures grew similarly."
    job.publish(job.check({"type": "negative", "reason": f" {reason} "}))
    assert accepted(state_path) == {
        "beta--saved": prior,
        fid: {"input": "kb:run", "type": "negative", "reason": reason, "model": MODEL},
    }


def test_followups_owe_only_new_or_failed_labels_for_accepted_topics(tmp_path: Path) -> None:
    """Catch reading directions from another topic, an unaccepted job, or no run at all."""
    lakehouse(tmp_path)
    for did, topic in (
        ("new", "growth"),
        ("retry", "growth"),
        ("saved", "growth"),
        ("untouched", "yield"),
        ("rejected", "stress"),
    ):
        direction(tmp_path, did, topic)
    state_path = tmp_path / followups.STATE
    saved = {
        "input": "old-policy-hash",
        "need": "experiment",
        "first_step_existing": False,
        "data_unclear": False,
        "reason": "Growth measurements decide the question.",
        "tables": [],
    }
    write_state(state_path, {"saved": saved, "retry": saved | {"failed": True}})
    scope = Scope(tmp_path, "alpha", "ingest")
    assert followup_jobs.jobs(scope) == []

    scope.notes["directions"] = {
        "directions/growth": {"status": "accepted"},
        "directions/stress": {"status": "rejected"},
    }
    new, retry = followup_jobs.jobs(scope)
    assert [new.key, retry.key] == ["followups/new", "followups/retry"]
    assert new.pack["QUESTION"]["how_to_test_it"] == "Grow strains at two temperatures."
    assert new.pack["DIRECTION_TABLES"] == [TABLE]
    write_state(state_path, dict.fromkeys(("new", "saved", "retry"), saved))
    assert followup_jobs.jobs(scope) == []


def test_followup_job_checks_catalog_and_publishes_canonical_tables(tmp_path: Path) -> None:
    """Catch accepting an unknown table or saving a label without the publisher's table field."""
    lakehouse(tmp_path)
    direction(tmp_path, "new", "growth")
    state_path = tmp_path / followups.STATE
    reason = "Growth measurements decide the question."
    record = {
        "need": "experiment",
        "first_step_existing": True,
        "data_unclear": False,
        "reason": reason,
        "tables": [TABLE],
    }
    prior = {"input": "old", "model": "old-model", **record}
    write_state(state_path, {"other": prior, "new": prior | {"failed": True}})
    scope = Scope(
        tmp_path,
        "alpha",
        "ingest",
        "run",
        models={"labels": MODEL},
        notes={"directions": {"directions/growth": {"status": "accepted"}}},
    )
    (job,) = followup_jobs.jobs(scope)

    assert (job.writer, job.reviewer) == ("labels", "card_review")
    with pytest.raises(Rejected) as refused:
        job.check(record | {"tables": ["unknown.table"]})
    assert "not in the lakehouse catalog" in refused.value.objections[0]
    job.publish(job.check(record | {"tables": [TABLE.upper()]}))
    assert accepted(state_path) == {
        "other": prior,
        "new": {"input": "kb:run", "model": MODEL, **record},
    }
