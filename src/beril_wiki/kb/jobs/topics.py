"""Place newly created concepts in the wiki's existing topic groups."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki.agentic.prose import blocks
from beril_wiki.agentic.runtime import CandidateError, manifest
from beril_wiki.kb import pages
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.store import write_text
from beril_wiki.stages import topics
from beril_wiki.stages.cards import load_state
from beril_wiki.stages.gists import SENTENCE_END

STATE = "state/curator-topics.json"


class Membership(BaseModel):
    """The existing topic a concept belongs to, or an abstention."""

    model_config = ConfigDict(extra="forbid", strict=True)
    topic: str
    reason: str


def _link_member(text: str, stem: str, concept: dict) -> str:
    if f"concepts/{stem}" in pages.links_in(text):
        return text
    prefix = f"[[concepts/{stem}"
    # The curator's link helper treats longer stems with this prefix as the same link.
    masked = "\0" + prefix[1:]
    linked = topics.link_missing_members(text.replace(prefix, masked), [stem], {stem: concept})
    return linked.replace(masked, prefix)


def _publish(root: Path, concept: dict, record: dict) -> None:
    slug = record["topic"]
    if not slug:
        return
    state_path = root / STATE
    current = load_state(state_path)
    groups = current["groups"]
    stem = concept["stem"]
    if any(stem in group["concepts"] for group in groups):
        return
    group = next(group for group in groups if topics.slugify(group["title"]) == slug)
    hub = root / "wiki/topics" / f"{slug}.md"
    text = hub.read_text(encoding="utf-8")
    linked = _link_member(text, stem, concept)
    # If a run stops here, the missing membership keeps the link work retryable.
    if linked != text:
        write_text(hub, linked)
    group["concepts"] = sorted([*group["concepts"], stem])
    current["concepts"] = manifest(root, ("wiki/concepts",))
    write_state(state_path, current)


def jobs(scope: Scope) -> list[Job]:
    """Ask only about concept pages created in this run with no saved membership."""
    root = scope.root
    groups = load_state(root / STATE).get("groups", [])
    members = {stem for group in groups for stem in group["concepts"]}
    created = set()
    for page_id in scope.created:
        kind, _, stem = page_id.partition("/")
        if kind == "concepts" and stem and "/" not in stem and stem not in members:
            created.add(stem)
    if not created:
        return []

    catalog: dict[str, dict[str, str]] = {}
    for group in groups:
        slug = topics.slugify(group["title"])
        hub = root / "wiki/topics" / f"{slug}.md"
        if hub.is_file():
            page = topics.parse_page(hub)
            lead = blocks(pages.parse(page["text"]).sections[0].body)
            description = page["desc"] or (lead[0] if lead else "")
            catalog[slug] = {"title": group["title"], "description": description}

    if not catalog:
        return []

    def parse(raw: str) -> Membership:
        try:
            record = Membership.model_validate_json(raw)
        except ValidationError as exc:
            raise CandidateError(f"invalid topic membership: {exc}") from exc
        if record.topic and record.topic not in catalog:
            raise CandidateError("topic must be an existing topic slug or empty")
        reason = record.reason.strip()
        if not reason or SENTENCE_END.search(reason):
            raise CandidateError("reason must be one sentence")
        return record.model_copy(update={"reason": reason})

    owed = []
    for stem in sorted(created):
        path = root / "wiki/concepts" / f"{stem}.md"
        if not path.is_file():
            continue
        concept = topics.parse_page(path)

        def publish(record: dict, concept: dict = concept) -> None:
            _publish(root, concept, record)

        owed.append(
            Job(
                stage="topics",
                key=f"topics/{stem}",
                pack={
                    "CONCEPT": {
                        "title": concept["title"],
                        "description": concept["desc"],
                        "lead": pages.parse(concept["text"]).sections[0].body,
                    },
                    "TOPICS": catalog,
                },
                check=legacy(parse),
                publish=publish,
                writer="curate",
                reviewer="",
                schema=Membership.model_json_schema(),
            )
        )
    return owed


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Refresh the home count even when no new concept needed placement."""
    topics.refresh_corpus_line(scope.root / "wiki/index.md", topics.corpus_stats(scope.root))
