"""Place new concepts in topic groups and write missing hubs during compile."""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki import compiler
from beril_wiki.agentic import prose
from beril_wiki.agentic.runtime import CandidateError, manifest
from beril_wiki.check import cited_ids, source_ids
from beril_wiki.kb import pages
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.store import DIGESTS, write_text
from beril_wiki.stages import topics
from beril_wiki.stages.cards import load_state
from beril_wiki.stages.gists import SENTENCE_END

STATE = "state/curator-topics.json"


class Membership(BaseModel):
    """The existing topic a concept belongs to, or an abstention."""

    model_config = ConfigDict(extra="forbid", strict=True)
    topic: str
    reason: str


class Hub(BaseModel):
    """Markdown for a topic hub with fixed membership."""

    model_config = ConfigDict(extra="forbid", strict=True)
    page: str


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


def _hub_jobs(root: Path, groups: list[dict]) -> list[Job]:
    missing = [
        (group, root / "wiki/topics" / f"{topics.slugify(group['title'])}.md") for group in groups
    ]
    missing = [(group, path) for group, path in missing if not path.exists()]
    if not missing:
        return []
    targets = compiler.wikilink_targets(root)
    sources = source_ids(root)
    definitions = root / "knowledge/topics.json"
    descriptions = (
        {
            topic["slug"]: topic["scope"]
            for topic in json.loads(definitions.read_text(encoding="utf-8"))
        }
        if definitions.is_file()
        else {}
    )
    return [
        _hub_job(
            root,
            group,
            path,
            group.get("description", descriptions.get(path.stem, "")),
            sources,
            targets | {f"topics/{path.stem}"},
        )
        for group, path in missing
    ]


def _hub_job(
    root: Path,
    group: dict,
    path: Path,
    description: str,
    sources: dict[str, str],
    targets: set[str],
) -> Job:
    title = group["title"]
    members = {
        stem: topics.parse_page(root / "wiki/concepts" / f"{stem}.md")
        for stem in sorted(group["concepts"])
    }
    bodies = {
        f"concepts/{stem}": compiler.parse_fm(concept["text"])[1]
        for stem, concept in members.items()
    }
    excerpts = prose.excerpts(bodies, topics.PACK_CHARS)
    projects = set(cited_ids("\n".join(bodies.values())))
    projects.update(sid for concept in members.values() for sid in concept["sources"])
    contract = topics.CONTRACT
    if not members:
        contract = replace(
            contract,
            words=None,
            rules=(
                "Write a brief hub with the exact title and required headings. Explain that "
                "the corpus has no member concepts for this topic yet. Add no claims, sources "
                "or suggested reading.",
                f"Use these headings in order: {', '.join(contract.headings)}.",
            ),
        )
    pack = {
        "TOPIC": {"title": title, "description": description},
        "MEMBER CONCEPT PAGES": excerpts,
        "PROJECTS IN SCOPE": sorted(projects),
        "RULES": contract.rules,
    }

    def parse(raw: str) -> Hub:
        try:
            record = Hub.model_validate_json(raw)
        except ValidationError as exc:
            raise CandidateError(f"invalid topic hub: {exc}") from exc
        text = prose.clean(record.page, targets)
        if text.split("\n", 1)[0] != f"# {title}":
            raise CandidateError(f"begin the topic hub with '# {title}'")
        headings = [f"## {s.heading}" for s in pages.parse(text).sections if s.heading]
        if tuple(headings) != contract.headings:
            raise CandidateError("write the three required sections in order")
        for stem, concept in members.items():
            text = _link_member(text, stem, concept)
        issues = prose.gate(text, contract, allowed=excerpts, sources=sources, valid_ids=projects)
        if issues:
            raise CandidateError(
                "topic hub failed its gates",
                [" ".join(filter(None, (issue.quote, issue.note))) for issue in issues],
            )
        return Hub(page=text)

    def publish(record: dict) -> None:
        if not path.exists():
            fields = {
                "type": "Topic",
                "description": description,
                "sources": [
                    f"summaries/{sid}{'__REPORT' if sid not in DIGESTS else ''}.md"
                    for sid in sorted(set(cited_ids(record["page"])))
                ],
            }
            write_text(path, compiler.fm_block(fields) + record["page"].rstrip() + "\n")

    def listing(refused: dict | None, objections: list[dict]) -> dict:
        """The hub as code can write it: the topic's scope and its concept pages."""
        lines = [f"# {title}", "", description.strip()]
        lines += ["", "No overview of this topic has passed review. Its concept pages follow."]
        lines += ["", contract.headings[0], ""]
        lines += [
            f"- [[concepts/{stem}|{concept['title']}]]: {concept['desc']}".rstrip(": ")
            for stem, concept in members.items()
        ] or ["The corpus has no concept page on this topic yet."]
        lines += ["", contract.headings[1], ""]
        lines += ["Each concept page above states the tensions and caveats of its own evidence."]
        lines += ["", contract.headings[2], ""]
        # Only pages on disk: a summary that was refused has none.
        names = [f"{sid}{'' if sid in DIGESTS else '__REPORT'}" for sid in sorted(projects)]
        lines += [
            f"- [[summaries/{name}]]"
            for name in names
            if (root / "wiki/summaries" / f"{name}.md").is_file()
        ] or ["No report summary is in scope yet."]
        return {"page": "\n".join(lines)}

    return Job(
        stage="topics",
        key=f"topics/{path.stem}",
        creates=f"topics/{path.stem}",
        pack=pack,
        check=legacy(parse),
        publish=publish,
        writer="write",
        reviewer="review",
        schema=Hub.model_json_schema(),
        fallback=listing,
    )


def jobs(scope: Scope) -> list[Job]:
    """Write missing compile hubs or place newly created concepts."""
    root = scope.root
    groups = load_state(root / STATE).get("groups", [])
    if scope.reason == "compile" and not scope.source:
        return _hub_jobs(root, groups)
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
            lead = prose.blocks(pages.parse(page["text"]).sections[0].body)
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


def home(scope: Scope) -> list[Job]:
    """The landing page, owed once in a compile when every hub it lists is written."""
    root = scope.root
    path = root / "wiki/index.md"
    if scope.reason != "compile" or scope.source or path.exists():
        return []
    hubs = []
    for group in load_state(root / STATE).get("groups", []):
        slug = topics.slugify(group["title"])
        hub = root / "wiki/topics" / f"{slug}.md"
        if not hub.is_file():
            # A hub still owed: the home page waits, or it would list part of the wiki
            # and never be asked for again.
            return []
        lead = pages.parse(hub.read_text(encoding="utf-8")).sections[0].body
        first = (prose.blocks(lead) or [""])[0][:400]
        hubs.append(
            f"- [[topics/{slug}|{group['title']}]] ({len(group['concepts'])} concepts): {first}"
        )
    if not hubs:
        return []
    contract = topics.HOME
    stats = topics.corpus_stats(root)
    listing = "\n".join(hubs)
    allowed = (
        f"TOPIC HUBS (title, slug, lead, concept count):\n{listing}\n\nCORPUS COUNTS:\n{stats}"
    )
    targets = compiler.wikilink_targets(root) | {"about", "catalog", "authors/index", "data/index"}

    def parse(raw: str) -> Hub:
        try:
            record = Hub.model_validate_json(raw)
        except ValidationError as exc:
            raise CandidateError(f"invalid home page: {exc}") from exc
        text = prose.clean(record.page, targets)
        if text.split("\n", 1)[0] != contract.first:
            raise CandidateError(f"begin the page with '{contract.first}'")
        headings = [f"## {s.heading}" for s in pages.parse(text).sections if s.heading]
        if tuple(headings) != contract.headings:
            raise CandidateError(f"use these sections in order: {', '.join(contract.headings)}")
        issues = prose.gate(text, contract, allowed=allowed, sources={}, valid_ids=set())
        if issues:
            raise CandidateError(
                "the home page failed its gates",
                [" ".join(filter(None, (issue.quote, issue.note))) for issue in issues],
            )
        return Hub(page=text)

    def publish(record: dict) -> None:
        write_text(path, record["page"].rstrip() + "\n")
        # The model was given the counts, but it must not own them.
        topics.refresh_corpus_line(path, topics.corpus_stats(root))
        topics.refresh_acknowledgement(path)

    def plain(refused: dict | None, objections: list[dict]) -> dict:
        """The home page as code can write it: what the wiki is and its topics."""
        return {
            "page": "\n".join(
                [
                    contract.first,
                    "",
                    "The BERIL Research Observatory is a body of AI-conducted microbial-biology "
                    "research over the KBase Data Lakehouse. Each project wrote up its results "
                    "as a report, and this wiki compiles those reports into linked pages.",
                    "",
                    "Start from the topics below. Each topic gathers concept pages that argue "
                    "across projects. Entity pages describe the organisms, genes, methods and "
                    "datasets that recur, and summary pages cover one project each.",
                    "",
                    contract.headings[0],
                    "",
                    listing,
                    "",
                    contract.headings[1],
                    "",
                    stats,
                    "",
                    contract.headings[2],
                    "",
                    *(
                        f"- [[{target}|{words}]]"
                        for target, words in (
                            ("catalog", "Full page catalog"),
                            ("summaries/discoveries", "Discoveries digest"),
                            ("summaries/pitfalls", "Pitfalls digest"),
                            ("authors/index", "Authors"),
                            ("data/index", "Data collections"),
                        )
                        # Only pages on disk: a compile of some reports has no digests.
                        if (root / "wiki" / f"{target}.md").is_file()
                    ),
                ]
            )
        }

    return [
        Job(
            stage="topics",
            key="topics/home",
            pack={"HOME": allowed, "RULES": contract.rules},
            check=legacy(parse),
            publish=publish,
            writer="write",
            reviewer="review",
            schema=Hub.model_json_schema(),
            fallback=plain,
        )
    ]


# The home page reads the hubs, so it is asked for after them.
PHASES = (jobs, home)


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Refresh the home count even when no new concept needed placement."""
    topics.refresh_corpus_line(scope.root / "wiki/index.md", topics.corpus_stats(scope.root))
