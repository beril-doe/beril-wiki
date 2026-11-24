"""Author contributions grounded in the summaries of that author's projects."""

from __future__ import annotations

import re
from collections.abc import Callable
from pathlib import Path

from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki import compiler as C
from beril_wiki.agentic import prose
from beril_wiki.agentic.runtime import CandidateError
from beril_wiki.check import cited_ids, source_ids
from beril_wiki.kb import pages
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.store import write_text
from beril_wiki.stages import authors, cards


class Contribution(BaseModel):
    """One Markdown section ready to splice into an author page."""

    model_config = ConfigDict(extra="forbid")
    section: str


def _checker(
    name: str, summaries: dict[str, str], sources: dict[str, str], targets: set[str]
) -> Callable[[str], Contribution]:
    allowed = "\n".join(summaries.values())
    valid_ids = set(summaries)

    def parse(reply: str) -> Contribution:
        try:
            record = Contribution.model_validate_json(reply)
        except ValidationError as exc:
            raise CandidateError("submit one string field named section") from exc
        heading, _, body = prose.clean(record.section, targets).partition("\n")
        if heading.rstrip() != authors.HEADING or re.search(
            r"^ {0,3}#{1,2}(?:[ \t]|$)", body, re.M
        ):
            raise CandidateError(f"submit one section beginning with {authors.HEADING!r}")
        parts = [authors.HEADING, *prose.blocks(body)]
        section = "\n\n".join(parts)
        issues = prose.gate(
            section, authors.CONTRACT, allowed=allowed, sources=sources, valid_ids=valid_ids
        )
        objections = [
            f"{issue.note} ({issue.quote})" if issue.quote else issue.note for issue in issues
        ]
        objections.extend(
            f"characterises the person; state what the project did or found: {hit[:300]}"
            for part in parts
            for hit in authors.subjective_hits(part, name)
        )
        if objections:
            raise CandidateError("author contributions failed the prose checks", objections)
        return Contribution(section=section)

    return parse


def jobs(scope: Scope) -> list[Job]:
    """Return owed Contributions jobs for the authors of the selected reports."""
    corpus = scope.reason == "compile" and not scope.source
    reports = set(scope.sources) if corpus else {scope.source} - {""}
    if not reports:
        return []
    wiki = scope.root / "wiki"
    state_path = scope.root / "state" / "authors.json"
    state = cards.load_state(state_path)
    stamp = f"kb:{scope.run}"
    is_new = scope.reason == "ingest" and scope.source not in scope.store.sources()
    owed = []
    inputs: tuple[dict[str, str], set[str]] | None = None
    for page in sorted((wiki / "authors").glob("*.md")):
        if page.stem == "index":
            continue
        stub = pages.parse(page.read_text(encoding="utf-8", errors="replace"))
        projects = next(
            (s for s in stub.sections if re.fullmatch(r"Projects(?: \(\d+\))?", s.heading)), None
        )
        if not projects:
            continue
        ids = set(authors.author_projects(projects.body))
        ids.update(re.findall(r"^- ([\w.-]+)$", projects.body, re.M))
        previous = stub.section("contributions") or stub.section("profile")
        # A revision that takes a person off the report leaves their page crediting
        # them with its results until the section is written again without it.
        removed = (
            scope.source not in ids
            and scope.reason == "revise"
            and bool(previous and scope.source in cited_ids(previous.body))
        )
        if not ids & reports and not removed:
            continue
        saved = state.get(page.name)
        if corpus and previous and previous.body:
            continue
        if previous and previous.body and saved and not removed:
            if scope.run and saved == stamp:
                continue
            covered = scope.source in cited_ids(previous.body)
            revised = scope.reason == "revise" and scope.withdrawn and covered
            if not revised and not (is_new and not covered):
                continue

        summaries = {}
        for pid in sorted(ids):
            path = wiki / "summaries" / f"{pid}__REPORT.md"
            if path.is_file():
                summaries[pid] = C.parse_fm(path.read_text(encoding="utf-8", errors="replace"))[1]
        if not summaries or (not reports.intersection(summaries) and not removed):
            continue
        if inputs is None:
            inputs = source_ids(scope.root), C.wikilink_targets(scope.root)

        def publish(record: dict, page: Path = page) -> None:
            stub_text = page.read_text(encoding="utf-8", errors="replace")
            body = re.sub(
                r"^## (?:Profile|Contributions)\s*\n.*?(?=\n## |\Z)",
                "",
                stub_text,
                flags=re.M | re.S,
            )
            at = body.find("## Projects")
            at = at if at >= 0 else len(body)
            current = cards.load_state(state_path)
            write_text(page, f"{body[:at].rstrip()}\n\n{record['section']}\n\n{body[at:]}")
            current[page.name] = stamp
            write_state(state_path, current)

        name = stub.title or page.stem
        owed.append(
            Job(
                stage="authors",
                key=f"authors/{page.stem}",
                pack={
                    "AUTHOR": name,
                    "SUMMARIES": prose.excerpts(
                        {f"summaries/{pid}__REPORT": text for pid, text in summaries.items()},
                        100_000,
                    ),
                },
                check=legacy(_checker(name, summaries, *inputs)),
                publish=publish,
                writer="write",
                reviewer="review",
                schema=Contribution.model_json_schema(),
            )
        )
    return owed
