"""Follow-up needs for research directions written by this run."""

from __future__ import annotations

from beril_wiki import lakehouse
from beril_wiki.agentic.runtime import WorkflowError
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.stages import classify, directions, followups


def jobs(scope: Scope) -> list[Job]:
    """Owe directions of this run's accepted topics without an accepted follow-up label."""
    topics = {
        key.removeprefix("directions/")
        for key, outcome in scope.notes.get("directions", {}).items()
        if key.startswith("directions/") and outcome["status"] == "accepted"
    }
    if not topics:
        return []

    root = scope.root
    state_path = root / followups.STATE
    state = classify.load(state_path)
    owed_ids = {
        page.stem
        for topic in topics
        for page in directions.pages_for(root / followups.DIRECTIONS, topic)
        if not (saved := state.get(page.stem)) or saved.get("failed")
    }
    if not owed_ids:
        return []

    cat = lakehouse.load(root)
    if cat.empty:
        raise WorkflowError("followups: no lakehouse catalog; run stages.lakehouse first")
    owed = []
    for did, pack in followups.packs(root, cat).items():
        if did not in owed_ids:
            continue

        def publish(record: dict, did: str = did) -> None:
            current = classify.load(state_path)
            current[did] = {
                "input": f"kb:{scope.run}",
                **record,
                "model": scope.models.get("labels", ""),
            }
            write_state(state_path, current)

        owed.append(
            Job(
                stage="followups",
                key=f"followups/{did}",
                pack=pack,
                check=legacy(followups.checker(pack, cat)),
                publish=publish,
                writer="labels",
                reviewer="card_review",
                schema=followups.Followup.model_json_schema(),
            )
        )
    return owed
