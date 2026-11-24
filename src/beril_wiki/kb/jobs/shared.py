"""Shared statements for unanswered result groups that include the run's report."""

from __future__ import annotations

from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.records import summary_title
from beril_wiki.stages import cards, links, shared


def _job(scope: Scope, gid: str, members: dict[str, dict], metadata: dict, pack: dict) -> Job:
    path = scope.root / shared.STATE

    def publish(record: dict) -> None:
        state = cards.load_state(path)
        state[gid] = metadata | {"input": f"kb:{scope.run}"} | record
        write_state(path, state)

    return Job(
        stage="shared",
        key=f"shared/{gid}",
        pack=pack,
        check=legacy(shared.checker(members)),
        publish=publish,
        schema=shared.Group.model_json_schema(),
    )


def jobs(scope: Scope) -> list[Job]:
    """Find eligible groups with a member from this report and no accepted statement."""
    root = scope.root
    groups = shared.group_members(root)
    if not groups:
        return []
    state = cards.load_state(root / shared.STATE)
    findings = links.read_findings(root)
    linked = shared.related(cards.load_state(root / shared.LINKS)["links"], findings)
    owed = []
    for gid, members in groups.items():
        projects = sorted({findings[fid]["report"] for fid in members})
        if scope.source not in projects or len(members) > shared.MAX_MEMBERS or len(projects) < 2:
            continue
        saved = state.get(gid, {})
        if saved.get("title") and not saved.get("failed"):
            continue
        topics = shared.group_topics(root, projects)
        if len(topics) < 2:
            continue
        inner = [link for link in linked if link["a"] in members and link["b"] in members]
        relation = max((link["type"] for link in inner), key=shared.RELATIONS.index)
        texts = {
            fid: {k: findings[fid][k] for k in ("title", "claim", "quote", "quantities")}
            | {"project": summary_title(root, findings[fid]["report"])}
            for fid in members
        }
        metadata = {
            "members": members,
            "projects": projects,
            "topics": topics,
            "relation": relation,
        }
        pack = {"RESULTS": texts, "RELATION": relation, "LINKS": [link["label"] for link in inner]}
        owed.append(_job(scope, gid, {fid: findings[fid] for fid in members}, metadata, pack))
    return owed
