"""Result types for listed findings of the run's report."""

from __future__ import annotations

from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.stages import classify, outcomes


def jobs(scope: Scope) -> list[Job]:
    """Owe each listed finding of this report without an accepted result type."""
    state_path = scope.root / outcomes.STATE
    state = classify.load(state_path)
    owed = []
    for fid, pack in outcomes.packs(scope.root).items():
        if fid.rpartition("--")[0] != scope.source:
            continue
        saved = state.get(fid)
        if saved and not saved.get("failed"):
            continue

        def publish(record: dict, fid: str = fid) -> None:
            current = classify.load(state_path)
            current[fid] = {
                "input": f"kb:{scope.run}",
                **record,
                "model": scope.models.get("labels", ""),
            }
            write_state(state_path, current)

        owed.append(
            Job(
                stage="outcomes",
                key=f"outcomes/{fid}",
                pack=pack,
                check=legacy(outcomes.checker(pack)),
                publish=publish,
                writer="labels",
                reviewer="card_review",
                schema=outcomes.Outcome.model_json_schema(),
            )
        )
    return owed
