"""Add literature context to an edited hub that has no such section yet."""

from __future__ import annotations

import re
import urllib.parse
from collections.abc import Callable, Iterator
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from beril_wiki.agentic import prose
from beril_wiki.agentic.runtime import CandidateError
from beril_wiki.kb import pages
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.stages import literature
from beril_wiki.stages.cards import load_state

STATE = "state/litcontext.json"
NO_PAPERS = {"status": "no-relevant-papers"}


class LiteratureUnavailable(Exception):
    """PubMed could not complete the requested search."""


def fetch_candidates(queries: list[str]) -> dict[str, str]:
    """PMID -> title and abstract for the papers two searches return.

    The curator's function of this name returns bare citations unless its own runtime
    is configured, which it never is here; a section that sets findings against the
    literature needs what the papers say.
    """
    ids: list[str] = []
    failure = None
    for query in queries[:2]:
        try:
            found = literature.eutils(
                "esearch", term=query, retmax=literature.MAX_PAPERS // 2, sort="relevance"
            )
        except Exception as exc:  # a PubMed fault skips the query, not the run
            print(f"    literature: search failed for {query!r}: {exc}")
            failure = exc
            continue
        ids += [i for i in found["esearchresult"].get("idlist", []) if i not in ids]
    ids = [i for i in ids if i.isdigit()][: literature.MAX_PAPERS]
    if not ids:
        if failure:
            raise LiteratureUnavailable(
                "a search failed before finding any candidates"
            ) from failure
        return {}
    params = {"db": "pubmed", "id": ",".join(ids), "retmode": "xml", "tool": "beril-wiki"}
    try:
        raw = literature.paced_get(
            f"{literature.EUTILS}/efetch.fcgi?{urllib.parse.urlencode(params)}", 2_000_001
        )
    except Exception as exc:
        raise LiteratureUnavailable(f"abstracts could not be fetched: {exc}") from exc
    if len(raw) > 2_000_000:
        raise LiteratureUnavailable("the abstracts exceeded the retrieval limit")
    return literature.abstracts_from_xml(raw, set(ids))


class Queries(BaseModel):
    """A broad and a narrow PubMed keyword query."""

    model_config = ConfigDict(extra="forbid", strict=True, str_strip_whitespace=True)
    queries: list[str] = Field(min_length=2, max_length=2)


class Section(BaseModel):
    """A literature section or the curator's no-relevant-papers sentinel."""

    model_config = ConfigDict(extra="forbid", strict=True)
    section: str


def _hubs(scope: Scope) -> Iterator[tuple[Path, str]]:
    wiki = scope.root / "wiki"
    candidates = set()
    for section_id in scope.edited:
        page_id, _, section = section_id.partition("#")
        kind, _, slug = page_id.partition("/")
        if section and kind == "topics" and slug and slug != "index" and "/" not in slug:
            candidates.add(wiki / "topics" / f"{slug}.md")
    corpus = scope.reason == "compile" and not scope.source
    if corpus:
        candidates.update(
            page
            for kind in ("concepts", "topics")
            for page in (wiki / kind).glob("*.md")
            if page.stem != "index"
        )
    state = load_state(scope.root / STATE) if corpus else {}
    for page in sorted(candidates):
        if state.get(_state_key(page)) == NO_PAPERS:
            continue
        if page.is_file():
            text = page.read_text(encoding="utf-8", errors="replace")
            if not any(s.heading == "Literature Context" for s in pages.parse(text).sections):
                yield page, text


def _state_key(page: Path) -> str:
    return page.name if page.parent.name == "topics" else f"{page.parent.name}/{page.name}"


def _job_input(scope: Scope, page: Path) -> Path:
    return (
        scope.root
        / ".agentic/runs"
        / scope.run
        / "literature"
        / (_state_key(page).removesuffix(".md") + ".json")
    )


def _parse_queries(raw: str) -> Queries:
    try:
        record = Queries.model_validate_json(raw)
    except ValidationError as exc:
        raise CandidateError(f"invalid PubMed queries: {exc}") from exc
    if any(not query or re.search(r"\[[^\]]+\]", query) for query in record.queries):
        raise CandidateError("write two nonempty keyword queries without PubMed field tags")
    return record


def query_jobs(scope: Scope) -> list[Job]:
    """Prepare the broad and narrow searches for each owed hub."""
    owed = []
    for page, text in _hubs(scope):
        path = _job_input(scope, page)
        if path.exists():
            continue

        def publish(record: dict, path: Path = path) -> None:
            # A resumed run may skip the completed query job before it writes the section.
            write_state(path, record)

        owed.append(
            Job(
                stage="literature",
                key=f"literature/{_state_key(page).removesuffix('.md')}/queries",
                pack={"HUB PAGE": text},
                check=legacy(_parse_queries),
                publish=publish,
                writer="queries",
                reviewer="",
                schema=Queries.model_json_schema(),
            )
        )
    return owed


def _papers(path: Path, page: Path, hub: str) -> dict[str, str] | None:
    saved = load_state(path)
    if "papers" in saved:
        return dict(saved["papers"])
    if not saved.get("queries"):
        return None
    try:
        papers = fetch_candidates(saved["queries"])
        if not papers:
            h1 = re.search(r"^# (.+)$", hub, re.M)
            title = re.sub(r"[^\w\s-]", " ", h1.group(1)) if h1 else page.stem.replace("-", " ")
            papers = fetch_candidates([f"{title} bacteria", title])
    except LiteratureUnavailable as exc:
        print(f"    literature/{_state_key(page)}: {exc}")
        raise
    write_state(path, saved | {"papers": list(papers.items())})
    return papers


def _checker(allowed: str, papers: dict[str, str]) -> Callable[[dict], dict]:
    def parse(raw: str) -> Section:
        try:
            record = Section.model_validate_json(raw)
        except ValidationError as exc:
            raise CandidateError(f"invalid literature section: {exc}") from exc
        text = prose.clean(record.section, None)
        if text == literature.CONTRACT.empty:
            return Section(section=text)
        parts = prose.blocks(text)
        text = "\n\n".join(parts)
        issues = prose.gate(text, literature.CONTRACT, allowed=allowed, sources={}, valid_ids=set())
        objections = [f"{issue.category}: {issue.quote} {issue.note}" for issue in issues]
        objections.extend(
            f"citation: PMID {pid} is not a candidate"
            for pid in dict.fromkeys(literature.PMID_LINK.findall(text))
            if pid not in papers
        )
        headings = [s.heading for s in pages.parse(text).sections if s.heading]
        if headings != ["Literature Context"]:
            objections.append("write a single section headed '## Literature Context'")
        if objections:
            raise CandidateError("invalid literature section", objections)
        return Section(section=text)

    return legacy(parse)


def section_jobs(scope: Scope) -> list[Job]:
    """Retrieve papers and ask for a section only when candidate evidence exists."""
    state_path = scope.root / STATE
    corpus = scope.reason == "compile" and not scope.source
    owed = []
    for page, text in _hubs(scope):
        try:
            papers = _papers(_job_input(scope, page), page, text)
        except LiteratureUnavailable as exc:
            # A search that failed is not an answer: the run that asked stays open and
            # asks again. Abstracts too large to fetch will be too large next time too.
            if "retrieval limit" not in str(exc):
                scope.notes.setdefault("literature_unavailable", []).append(_state_key(page))
            continue
        if papers is None:
            continue
        if not papers:
            if corpus:
                write_state(state_path, load_state(state_path) | {_state_key(page): NO_PAPERS})
            continue
        paper_block = "\n".join(f"- PMID {pid}: {cite}" for pid, cite in papers.items())
        allowed = (
            f"HUB PAGE:\n\n{text}\n\nCANDIDATE PAPERS (the only citable literature):\n{paper_block}"
        )

        def publish(record: dict, page: Path = page) -> None:
            current = load_state(state_path)
            if record["section"] == literature.CONTRACT.empty:
                current[_state_key(page)] = NO_PAPERS if corpus else f"kb:{scope.run}"
            else:
                literature.splice(page, record["section"])
                current[_state_key(page)] = f"kb:{scope.run}"
            write_state(state_path, current)

        owed.append(
            Job(
                stage="literature",
                key=f"literature/{_state_key(page).removesuffix('.md')}/section",
                pack={
                    "HUB PAGE": text,
                    "CANDIDATE PAPERS": papers,
                    "LITERATURE CONTRACT": literature.CONTRACT.rules,
                },
                check=_checker(allowed, papers),
                publish=publish,
                writer="write",
                reviewer="review",
                schema=Section.model_json_schema(),
            )
        )
    return owed


PHASES = (query_jobs, section_jobs)
