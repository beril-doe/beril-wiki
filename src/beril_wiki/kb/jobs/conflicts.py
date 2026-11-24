"""Conflict pages owed by newly accepted edits to concept Tensions sections."""

from __future__ import annotations

import re
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki.agentic import prose
from beril_wiki.agentic.runtime import CandidateError
from beril_wiki.check import cited_ids, source_ids
from beril_wiki.compiler import WIKILINK, wikilink_targets
from beril_wiki.kb.jobs import Job, Scope, legacy
from beril_wiki.kb.store import sha256, write_text
from beril_wiki.stages import conflicts

TENSIONS = re.compile(r"^## Tensions?\s*\n(.*?)(?=\n## |\Z)", re.M | re.S)


class Conflict(BaseModel):
    """One conflict page, in Markdown."""

    model_config = ConfigDict(extra="forbid")
    page: str


def _tension_blocks(concept: str, text: str) -> list[dict]:
    section = TENSIONS.search(text)
    if section is None:
        return []
    return [
        {"concept": concept, "index": index, "text": paragraph, "projects": projects}
        for index, paragraph in enumerate(prose.blocks(section[1]))
        if len(projects := set(cited_ids(paragraph))) >= 2
    ]


def _checker(
    allowed: str, projects: set[str], sources: dict[str, str], targets: set[str]
) -> Callable[[str], Conflict]:
    valid_ids = projects & sources.keys()

    def check(raw: str) -> Conflict:
        try:
            record = Conflict.model_validate_json(raw)
        except ValidationError as exc:
            raise CandidateError(str(exc)) from exc
        parts = prose.blocks(prose.clean(record.page, None))
        page = "\n\n".join(parts)
        issues = prose.gate(
            page, conflicts.CONTRACT, allowed=allowed, sources=sources, valid_ids=valid_ids
        ) + conflicts.empty_sides(parts)
        objections = [" ".join(filter(None, (issue.quote, issue.note))) for issue in issues]
        for link in WIKILINK.finditer(page):
            target = link[1].strip().lstrip("/")
            if target not in targets:
                objections.append(f"wikilink {link[0]} targets a page that does not exist")
        if objections:
            raise CandidateError("conflict page failed its gates", objections)
        return Conflict(page=page)

    return check


def _job(
    path: Path,
    group: list[dict],
    concepts: dict[str, str],
    sources: dict[str, str],
    targets: set[str],
) -> Job:
    allowed = "\n".join(block["text"] for block in group)
    digest = sha256(allowed)[:16]
    projects: set[str] = set().union(*(block["projects"] for block in group))
    tension = "\n\n".join(
        f"[from wiki/concepts/{block['concept']}.md, Tensions paragraph {block['index']}]\n"
        f"{block['text']}"
        for block in group
    )
    leads = "\n\n".join(
        f"[concepts/{stem}]\n{conflicts.concept_lead(concepts[stem])}"
        for stem in sorted({block["concept"] for block in group})
    )

    def publish(record: dict) -> None:
        if not path.exists():
            write_text(path, f"<!-- tension-hash: {digest} -->\n{record['page']}\n")

    return Job(
        stage="conflicts",
        key=f"conflicts/{path.stem}",
        creates=f"conflicts/{path.stem}",
        pack={
            "TENSION": tension,
            "CONCEPT CONTEXT (framing only)": leads,
            "SOURCE EXCERPTS (verification only)": prose.source_excerpts(
                tension, projects, sources
            ),
            "RULES": conflicts.CONTRACT.rules,
        },
        check=legacy(_checker(allowed, projects, sources, targets)),
        publish=publish,
        writer="write",
        reviewer="review",
        schema=Conflict.model_json_schema(),
    )


def _edited(scope: Scope) -> set[str]:
    return {
        section.removesuffix("#tensions").removeprefix("concepts/")
        for section in scope.edited
        if section.startswith("concepts/") and section.endswith("#tensions")
    }


def tension_groups(root: Path) -> tuple[list[list[dict]], dict[str, str]]:
    """Every disagreement the concept pages state, grouped as the curator groups them.

    All concepts are read, not only the edited ones: two concepts that state one
    disagreement share a page, and its name depends on the whole group.
    """
    concepts: dict[str, str] = {}
    blocks: list[dict] = []
    for path in sorted((root / "wiki/concepts").glob("*.md")):
        text = path.read_text(encoding="utf-8", errors="replace")
        concepts[path.stem] = text
        blocks.extend(_tension_blocks(path.stem, text))
    return conflicts.merge_similar_groups(blocks), concepts


def jobs(scope: Scope) -> list[Job]:
    """Schedule missing conflict pages from edited concepts or the whole corpus."""
    edited = _edited(scope)
    corpus = scope.reason == "compile" and not scope.source
    if not (corpus or edited):
        return []
    groups, concepts = tension_groups(scope.root)
    out = scope.root / "wiki/conflicts"
    missing = []
    for group in groups:
        path = out / f"{conflicts.conflict_slug(group)}.md"
        if not path.exists() and (corpus or edited & {block["concept"] for block in group}):
            missing.append((path, group))
    if not missing:
        return []
    sources = source_ids(scope.root)
    targets = wikilink_targets(scope.root)
    return [_job(path, group, concepts, sources, targets) for path, group in missing]


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """Retire the pages of disagreements an edited concept no longer states.

    A page is named after its paragraph's text, so an edited paragraph gets a new page
    and leaves the old one behind. As in the curator, nothing is retired in a run where
    a replacement was not accepted: the old page is then the only one there is.
    """
    edited = _edited(scope)
    if not edited or any(o["status"] != "accepted" for o in outcomes.values()):
        return
    groups, _ = tension_groups(scope.root)
    live = {conflicts.conflict_slug(group) for group in groups}
    for page in sorted((scope.root / "wiki/conflicts").glob("conflict--*.md")):
        concept = page.stem.removeprefix("conflict--").rpartition("--")[0]
        if concept in edited and page.stem not in live:
            page.unlink()
