"""Reading the corpus pages and card records that the card stages and publish share.

Which reports and topics the card stages cover, which topics a report feeds, the
projects a page cites, the forward-looking bullets a topic's pages carry, and the
fields of a stored finding page. Nothing here calls a model or writes a file, and
nothing imports a stage or the publish step, so both can import it. A change here
reschedules every card stage (curator.stage_revision hashes this file).
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki.agentic.runtime import WorkflowError

SCOPE = "contract/cards.yaml"
FINDINGS = Path("wiki/findings")
# Collection pages built from the observatory's docs, not project reports.
DIGESTS = ("discoveries", "pitfalls")
# A null result a home or topic card may show: only the ones that measured something.
SHOWN_CASES = ("measured absence", "inconclusive test")
SRC = re.compile(r"\[src:\s*([^\]]+)\]")
H1 = re.compile(r"^# +(.+)$", re.M)
ITEM = re.compile(r"^(?:[-*]|\d+[.)])\s+(.*)$")
FORWARD = re.compile(r"^(Open Directions|Resolving Work)$")
REPORT_FORWARD = re.compile(r"Future Directions|Experimental Recommendations|Next Steps", re.I)


class Scope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    topics: list[str] | Literal["all"] = []
    reports: list[str] | Literal["all"] = []


class Resolved(BaseModel):
    topics: list[str]
    reports: list[str]


def slugify(text: str) -> str:
    """A topic or page slug; the same rule as stages.topics.slugify, which names hubs."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def title_of(text: str, fallback: str) -> str:
    """A page's first H1, else the fallback."""
    m = H1.search(text)
    return m.group(1).strip() if m else fallback


def source_path(root: Path, sid: str) -> Path:
    return root / "wiki" / "sources" / f"{sid}__REPORT.md"


def source_title(root: Path, sid: str) -> str:
    """The H1 of the report itself, under wiki/sources, else the report id."""
    return title_of(source_path(root, sid).read_text(encoding="utf-8", errors="replace"), sid)


def summary_title(root: Path, sid: str) -> str:
    """The H1 of the report's summary page, else the report id."""
    for name in (f"{sid}__REPORT.md", f"{sid}.md"):
        path = root / "wiki" / "summaries" / name
        if path.exists():
            return title_of(path.read_text(encoding="utf-8", errors="replace"), sid)
    return sid


def load_scope(root: Path) -> Resolved | None:
    """The topics and reports in scope, or None when the file is absent.

    "all" means every report under wiki/sources and every topic in the curator's
    topic decision, read at each run so new reports join without an edit.
    """
    path = root / SCOPE
    if not path.exists():
        return None
    try:
        scope = Scope.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    except (ValidationError, yaml.YAMLError) as exc:
        raise WorkflowError(f"invalid {SCOPE}: {exc}") from exc
    reports = scope.reports
    if reports == "all":
        reports = sorted(
            p.name.removesuffix("__REPORT.md") for p in (root / "wiki/sources").glob("*__REPORT.md")
        )
    topics = sorted(topic_groups(root)) if scope.topics == "all" else scope.topics
    return Resolved(topics=topics, reports=reports)


def projects_in(text: str) -> list[str]:
    """The report ids a page's [src: ...] tags cite, in first-cited order."""
    out: list[str] = []
    for tag in SRC.finditer(text):
        for part in re.split(r"[,;]", tag.group(1)):
            sid = re.sub(r"__REPORT$", "", part.strip())
            if sid and sid not in out:
                out.append(sid)
    return out


def curator_groups(root: Path) -> list[dict]:
    """The curator's topic decision: each group's title and concept stems."""
    path = root / "state" / "curator-topics.json"
    return json.loads(path.read_text(encoding="utf-8")).get("groups", []) if path.exists() else []


def topic_groups(root: Path) -> dict[str, set[str]]:
    """Topic slug -> the concept stems its hub gathers."""
    return {slugify(g["title"]): set(g["concepts"]) for g in curator_groups(root)}


def topic_concepts(root: Path, slug: str) -> list[str]:
    """The concept stems a topic hub gathers, from the curator's topic decision."""
    groups = curator_groups(root)
    return next((sorted(g["concepts"]) for g in groups if slugify(g["title"]) == slug), [])


def concept_citations(root: Path) -> dict[str, set[str]]:
    """Concept stem -> the reports the concept page cites."""
    return {
        p.stem: set(projects_in(p.read_text(encoding="utf-8", errors="replace")))
        for p in (root / "wiki/concepts").glob("*.md")
    }


def main_topics(
    sid: str, groups: dict[str, set[str]], concept_cites: dict[str, set[str]]
) -> list[str]:
    """The topics a report mainly feeds: those whose concepts cite it at least half
    as often as its most-citing topic does. Counting every topic with one citing
    concept put most reports in most topics, so topic filters selected nothing."""
    counts = {
        slug: sum(sid in concept_cites.get(c, set()) for c in concepts)
        for slug, concepts in groups.items()
    }
    top = max(counts.values(), default=0)
    return sorted(slug for slug, n in counts.items() if n and 2 * n >= top)


def bullets(text: str, heading: re.Pattern[str]) -> list[str]:
    """List items under every heading the pattern matches, continuation lines joined."""
    out: list[str] = []
    lines = text.splitlines()
    inside = False
    level = 0
    for line in lines:
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            if inside and len(h.group(1)) <= level:
                inside = False
            if not inside and heading.search(h.group(2)):
                inside, level = True, len(h.group(1))
            continue
        if not inside:
            continue
        m = ITEM.match(line.strip()) if line[:1] not in (" ", "\t") else None
        if m:
            out.append(m.group(1).strip())
        elif line.strip() and out and line[:1] in (" ", "\t"):
            out[-1] += " " + line.strip()
    return out


def forward_bullets(root: Path, topic: str, reports: list[str]) -> list[dict]:
    """Every forward-looking bullet the topic's pages and in-scope reports carry."""
    concepts = topic_concepts(root, topic)
    items: list[dict] = []

    def add(page: str, section: str, text: str, projects: list[str]) -> None:
        items.append(
            {"id": f"b{len(items)}", "page": page, "section": section, "text": text}
            | {"projects": projects or projects_in(text)}
        )

    for stem in concepts:
        path = root / "wiki/concepts" / f"{stem}.md"
        if path.exists():
            for text in bullets(path.read_text(encoding="utf-8"), FORWARD):
                add(f"concepts/{stem}", "Open Directions", text, [])
    for path in sorted((root / "wiki/conflicts").glob("conflict--*.md")):
        if path.stem.split("--")[1] in concepts:
            body = path.read_text(encoding="utf-8")
            sides = projects_in(body)
            for text in bullets(body, FORWARD):
                add(f"conflicts/{path.stem}", "Resolving Work", text, projects_in(text) or sides)
    for sid in reports:
        path = source_path(root, sid)
        if path.exists():
            for text in bullets(path.read_text(encoding="utf-8"), REPORT_FORWARD):
                add(f"sources/{sid}__REPORT", "Future Directions", text, [sid])
    return items


def finding_text(fields: dict, body: str) -> dict:
    """What a stored finding page says: its claim, result kind, key figures, caveat,
    the evidence quote and the report it came from."""
    quote = re.search(r"^## Evidence\s*\n+> (.+?)(?: \[src: [^\]]+\])?$", body, re.M)
    return {
        "claim": fields.get("description", ""),
        "result": fields.get("result", ""),
        "quantities": fields.get("quantities", []),
        "caveat": fields.get("caveat", ""),
        "quote": quote.group(1) if quote else "",
        "report": fields.get("source", ""),
    }


def caveat_quote(body: str) -> str:
    """The blockquote lines under `## Caveat`, source tags removed."""
    section = re.search(r"^## Caveat\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not section:
        return ""
    quoted = [
        re.sub(r"\s*\[src: [^\]]+\]", "", line[1:]).strip()
        for line in section.group(1).splitlines()
        if line.startswith(">")
    ]
    return " ".join(q for q in quoted if q)


def report_caveats(body: str) -> list[str]:
    """The bullets under `## Other caveats in this report`, source tags removed."""
    section = re.search(r"^## Other caveats in this report\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not section:
        return []
    return [
        re.sub(r"\s*\[src: [^\]]+\]", "", line[2:]).strip()
        for line in section.group(1).splitlines()
        if line.startswith("- ")
    ]


def components(edges: list[tuple[str, str]]) -> list[list[str]]:
    """The connected groups an edge list forms, each sorted, in sorted order."""
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        parent[find(a)] = find(b)
    groups: dict[str, list[str]] = {}
    for x in parent:
        groups.setdefault(find(x), []).append(x)
    return sorted(sorted(g) for g in groups.values())
