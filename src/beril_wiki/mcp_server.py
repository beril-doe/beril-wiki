"""The wiki as a read-only MCP tool server, mounted by beril_wiki.serve at /wiki/mcp.

Stateless streamable HTTP. Every tool answers from the artifact the server is
serving at that moment and names it (``artifact``), so an agent's citations are
consistent with what a reader sees. The tools read only what the artifact
carries: the search index the site ships (``static/search/pages.json`` and
``sections.json``, the same sections the browser search ranks) and, when the
artifact or the image carries a ``corpus/`` tree, the finding and direction
records (``cards.json``, their Markdown) and the exact source reports.

Search is keyword only for now, a small BM25 over sections.json with the same
tokenisation as theme/src/search/config.ts.
TODO(vector search): fuse with the int8 nomic vectors in ``vectors.i8`` once the
server holds an embedding key; the browser does this today with the reader's key.

This module ships in the server image with serve.py and imports nothing else
from the package.
"""

from __future__ import annotations

import json
import math
import pathlib
import re
import threading
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

STOP = frozenset(
    """a an and are as at be been but by can could did do does for from had has have how in into
    is it its of on or that the their there these they this those to was were what when where
    which while who why with would about across between than then not no so such via per may
    might also more most other""".split()
)
SPLIT = re.compile(r"""[\s,;:!?()\[\]{}"“”'’/]+""")
TRIM = re.compile(r"^[^\w]+|[^\w]+$", re.UNICODE)
GROUPS = (
    "topic",
    "concept",
    "conflict",
    "finding",
    "direction",
    "entity",
    "report",
    "source",
    "other",
)
MAX_READ = 24_000
FINDING_FIELDS = ("id", "title", "claim", "result", "source", "topics", "label", "type")
PAGE_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_./-]*$")
ID_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9_.-]*$")


def tokenize(text: str) -> list[str]:
    out: list[str] = []
    for raw in SPLIT.split(text):
        if not raw:
            continue
        parts = [raw]
        if re.search(r"[-_.]", raw):
            parts += [p for p in re.split(r"[-_.]+", raw) if p]
        for part in parts:
            w = TRIM.sub("", part.lower())
            if len(w) >= 2 and w not in STOP:
                out.append(w)
    return out


class BM25:
    """An inverted index over short documents; k1=1.2, b=0.75."""

    def __init__(self, docs: list[list[str]], k1: float = 1.2, b: float = 0.75) -> None:
        self.k1, self.b = k1, b
        self.n = len(docs)
        self.lengths = [len(d) for d in docs]
        self.avg = (sum(self.lengths) / self.n) if self.n else 1.0
        self.postings: dict[str, list[tuple[int, int]]] = {}
        for i, doc in enumerate(docs):
            for term, tf in Counter(doc).items():
                self.postings.setdefault(term, []).append((i, tf))

    def search(self, query: str, k: int, allowed: Callable[[int], bool]) -> list[tuple[int, float]]:
        scores: dict[int, float] = {}
        for term in set(tokenize(query)):
            posting = self.postings.get(term)
            if not posting:
                continue
            idf = math.log(1 + (self.n - len(posting) + 0.5) / (len(posting) + 0.5))
            for i, tf in posting:
                norm = self.k1 * (1 - self.b + self.b * self.lengths[i] / self.avg)
                scores[i] = scores.get(i, 0.0) + idf * tf * (self.k1 + 1) / (tf + norm)
        ranked = sorted(scores.items(), key=lambda x: (-x[1], x[0]))
        return [(i, s) for i, s in ranked if allowed(i)][:k]


@dataclass
class Corpus:
    """One artifact's searchable content, loaded once per artifact."""

    artifact: str
    site: pathlib.Path
    corpus: pathlib.Path | None
    build: str = ""
    pages: list[dict] = field(default_factory=list)
    sections: list[dict] = field(default_factory=list)
    by_slug: dict[str, dict] = field(default_factory=dict)
    _index: BM25 | None = None
    _cards: dict | None = None
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def __post_init__(self) -> None:
        search = self.site / "static/search"
        try:
            pages = json.loads((search / "pages.json").read_text(encoding="utf-8"))
            sections = json.loads((search / "sections.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            return
        self.build = pages.get("build", "")
        self.pages = pages.get("pages", [])
        self.sections = sections.get("sections", [])
        self.by_slug = {p["slug"]: p for p in self.pages}

    @property
    def index(self) -> BM25:
        with self._lock:
            if self._index is None:
                docs = []
                for s in self.sections:
                    page = self.by_slug.get(s["s"], {})
                    docs.append(
                        tokenize(page.get("title", "")) * 2
                        + tokenize(s.get("p", ""))
                        + tokenize(" ".join(page.get("aliases", [])))
                        + tokenize(s.get("t", ""))
                    )
                self._index = BM25(docs)
            return self._index

    @property
    def cards(self) -> dict[str, Any]:
        with self._lock:
            if self._cards is None:
                self._cards = {}
                if self.corpus and (self.corpus / "cards.json").is_file():
                    try:
                        self._cards = json.loads(
                            (self.corpus / "cards.json").read_text(encoding="utf-8")
                        )
                    except ValueError:
                        self._cards = {}
            return self._cards

    def markdown(self, folder: str, name: str) -> str | None:
        if not self.corpus or not ID_RE.fullmatch(name):
            return None
        path = self.corpus / folder / f"{name}.md"
        if path.is_file() and path.resolve().is_relative_to(self.corpus.resolve()):
            return path.read_text(encoding="utf-8", errors="replace")
        return None

    def page_sections(self, slug: str) -> list[dict]:
        return [s for s in self.sections if s["s"] == slug]


def snippet(text: str, query: str, width: int = 240) -> str:
    terms = set(tokenize(query))
    words = text.split()
    hit = next((i for i, w in enumerate(words) if tokenize(w) and set(tokenize(w)) & terms), 0)
    start = max(0, hit - 20)
    out = " ".join(words[start : start + 60])
    if len(out) > width:
        out = out[:width].rsplit(" ", 1)[0] + "…"
    return ("…" if start else "") + out


def page_path(value: str) -> str:
    slug = value.strip().strip("/").removesuffix(".md").removesuffix(".html")
    if not PAGE_RE.fullmatch(slug) or ".." in slug.split("/"):
        raise ValueError(f"not a page path: {value!r}")
    return slug


def create_mcp(current: Callable[[], Corpus]) -> FastMCP:
    """The tool server; ``current`` returns the corpus of the artifact being served."""
    mcp = FastMCP(
        "beril-wiki",
        instructions=(
            "Read-only tools over the BERIL Knowledge Wiki, an AI-generated synthesis of "
            "AI-conducted research reports. Cite the page or finding a tool returned, keep "
            "numbers verbatim, and verify quotes with get_source. Every answer names the "
            "artifact it came from."
        ),
        streamable_http_path="/",
        stateless_http=True,
        json_response=True,
        transport_security=TransportSecuritySettings(enable_dns_rebinding_protection=False),
    )

    def meta(c: Corpus) -> dict[str, Any]:
        return {"artifact": c.artifact, "build": c.build}

    @mcp.tool()
    def search(query: str, scope: str | None = None, k: int = 8) -> dict[str, Any]:
        """Keyword search over every section of the wiki. `scope` narrows to a page group
        (topic, concept, conflict, finding, direction, entity, report, source, other) or to
        a path prefix such as `concepts/`. Returns up to k sections with page, heading,
        anchor and a snippet."""
        c = current()
        k = max(1, min(int(k), 50))
        scope = (scope or "").strip().strip("/")

        def allowed(i: int) -> bool:
            if not scope:
                return True
            s = c.sections[i]
            page = c.by_slug.get(s["s"], {})
            if scope in GROUPS:
                return page.get("group") == scope
            return s["s"].startswith(scope + "/") or s["s"] == scope

        hits = []
        for i, score in c.index.search(query, k, allowed):
            s = c.sections[i]
            page = c.by_slug.get(s["s"], {})
            hits.append(
                {
                    "path": s["s"],
                    "title": page.get("title", s["s"]),
                    "group": page.get("group", ""),
                    "heading": s.get("p", ""),
                    "anchor": s.get("a", ""),
                    "snippet": snippet(s["t"], query),
                    "score": round(score, 3),
                }
            )
        return meta(c) | {"query": query, "scope": scope or None, "hits": hits}

    @mcp.tool()
    def read_page(path: str) -> dict[str, Any]:
        """A page's metadata and every section of its text, as the site shows it
        (citation markers removed). `path` is the page slug, e.g. concepts/gene-essentiality."""
        c = current()
        slug = page_path(path)
        page = c.by_slug.get(slug)
        if page is None:
            return meta(c) | {"path": slug, "error": "no such page"}
        return meta(c) | {
            "path": slug,
            "title": page.get("title"),
            "group": page.get("group"),
            "description": page.get("desc", ""),
            "topics": page.get("topicSlugs", []),
            "links_out": page.get("out", []),
            "sections": [
                {"heading": s.get("p", ""), "anchor": s.get("a", ""), "text": s["t"]}
                for s in c.page_sections(slug)
            ],
        }

    @mcp.tool()
    def read_section(path: str, heading: str) -> dict[str, Any]:
        """The sections of a page under one heading (case-insensitive match on the heading
        path, e.g. "Core evidence" or "Core evidence › Subsection")."""
        c = current()
        slug = page_path(path)
        if slug not in c.by_slug:
            return meta(c) | {"path": slug, "error": "no such page"}
        want = heading.strip().lower()
        found = [
            {"heading": s.get("p", ""), "anchor": s.get("a", ""), "text": s["t"]}
            for s in c.page_sections(slug)
            if want and want in s.get("p", "").lower()
        ]
        return meta(c) | {"path": slug, "heading": heading, "sections": found}

    def finding_rows(c: Corpus) -> list[dict]:
        return c.cards.get("findings", [])

    @mcp.tool()
    def list_findings(
        topic: str | None = None, project: str | None = None, k: int = 50
    ) -> dict[str, Any]:
        """Finding records, optionally for one topic (slug or title) or one project
        (report id). Returns id, title, claim, result type, source project and topics."""
        c = current()
        k = max(1, min(int(k), 500))
        rows = []
        want_topic = (topic or "").strip().lower()
        for f in finding_rows(c):
            if project and f.get("source") != project:
                continue
            if want_topic and not any(
                want_topic in str(t).lower() for t in f.get("topics", []) or []
            ):
                continue
            rows.append(
                {
                    k_: f.get(k_)
                    for k_ in (
                        "id",
                        "title",
                        "claim",
                        "result",
                        "source",
                        "topics",
                        "label",
                        "type",
                    )
                }
            )
            if len(rows) >= k:
                break
        return meta(c) | {
            "topic": topic,
            "project": project,
            "count": len(rows),
            "findings": rows,
            "available": bool(c.cards),
        }

    @mcp.tool()
    def get_finding(id: str) -> dict[str, Any]:
        """One finding record in full (claim, quantities, caveat, label, closest papers)
        plus its page's Markdown when the artifact carries it."""
        c = current()
        if not ID_RE.fullmatch(id):
            return meta(c) | {"id": id, "error": "bad id"}
        record = next((f for f in finding_rows(c) if f.get("id") == id), None)
        md = c.markdown("findings", id)
        if record is None and md is None:
            return meta(c) | {"id": id, "error": "no such finding"}
        return meta(c) | {"id": id, "record": record, "markdown": md}

    @mcp.tool()
    def get_direction(id: str) -> dict[str, Any]:
        """One research-direction record in full plus its page's Markdown when the artifact
        carries it."""
        c = current()
        if not ID_RE.fullmatch(id):
            return meta(c) | {"id": id, "error": "bad id"}
        record = next(
            (d for d in c.cards.get("research_directions", []) if d.get("id") == id), None
        )
        md = c.markdown("directions", id)
        if record is None and md is None:
            return meta(c) | {"id": id, "error": "no such direction"}
        return meta(c) | {"id": id, "record": record, "markdown": md}

    @mcp.tool()
    def get_source(project: str, offset: int = 0, length: int = 4000) -> dict[str, Any]:
        """A slice of a project's source report (REPORT.md) by character offset, for exact
        quote verification. Clamped to 24,000 characters; `total` is the report's length."""
        c = current()
        if not ID_RE.fullmatch(project):
            return meta(c) | {"project": project, "error": "bad project id"}
        text = c.markdown("sources", f"{project}__REPORT")
        if text is None:
            return meta(c) | {"project": project, "error": "source not available in this artifact"}
        offset = max(0, int(offset))
        length = max(1, min(int(length), MAX_READ))
        if offset >= len(text):
            return meta(c) | {"project": project, "error": f"offset beyond length {len(text)}"}
        piece = text[offset : offset + length]
        return meta(c) | {
            "project": project,
            "offset": offset,
            "end": offset + len(piece),
            "total": len(text),
            "text": piece,
        }

    return mcp
