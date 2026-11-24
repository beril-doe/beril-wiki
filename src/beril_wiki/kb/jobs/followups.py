"""Follow-up needs for research directions without a saved classification."""

from __future__ import annotations

from beril_wiki import lakehouse, records
from beril_wiki.agentic.runtime import WorkflowError
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.jobs.directions import table_context
from beril_wiki.stages import cards, classify, directions, followups


def jobs(scope: Scope) -> list[Job]:
    """Owe unlabelled directions in the compile or this run's accepted topics."""
    topics = {
        key.removeprefix("directions/")
        for key, outcome in scope.notes.get("directions", {}).items()
        if key.startswith("directions/") and outcome["status"] == "accepted"
    }
    corpus = scope.reason == "compile" and not scope.source
    if not (corpus or topics):
        return []

    root = scope.root
    state_path = root / followups.STATE
    state = classify.load(state_path)
    folder = root / followups.DIRECTIONS
    candidates = (
        set(folder.glob("*.md"))
        if corpus
        else {page for topic in topics for page in directions.pages_for(folder, topic)}
    )
    missing = [
        page
        for page in sorted(candidates)
        if page.stem != "index" and (not (saved := state.get(page.stem)) or saved.get("failed"))
    ]
    if not missing:
        return []

    cat = lakehouse.load(root)
    if cat.empty:
        raise WorkflowError("followups: no lakehouse catalog; run stages.lakehouse first")
    owed = []
    for page in missing:
        did = page.stem
        fields, body = cards.read_page(page)
        question = {
            "title": records.title_of(body, did),
            "hypothesis": fields.get("hypothesis", ""),
            **{s.lower().replace(" ", "_"): followups.section(body, s) for s in followups.SECTIONS},
            "approach": fields.get("approach", ""),
            "data_note": fields.get("readiness_basis", ""),
        }
        named = fields.get("tables") or []
        search = " ".join(
            question[k]
            for k in ("title", "hypothesis", "how_to_test_it", "what_would_support_or_refute_it")
        )
        pack = {
            "QUESTION": question,
            "DIRECTION_TABLES": named,
            **table_context(
                cat.matched(search, (), followups.MATCHED_TABLES, tables=named), 12_000
            ),
        }

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
