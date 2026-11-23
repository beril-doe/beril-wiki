"""The wiki as an internal, token-guarded HTTP API, for the BERIL webapp's WikiManager.

Mounted by beril_wiki.serve under ``/wiki/_api/`` and meant for in-cluster use
only (``http://wiki:8080``); the ingress must not expose ``/wiki/_api`` or
``/wiki/_admin``. Every request carries ``Authorization: Bearer
$WIKI_INTERNAL_TOKEN``; without the variable the routes answer 503.

Addresses are ``wiki/<collection>/<slug>[#section]`` over concepts, topics,
conflicts, entities, summaries, sources, findings, directions and data; the
authors collection is excluded server-side. Every answer names the artifact it
was served from, so an agent's citations match what a reader sees.

  GET _api/search?q=&scope=&k=   {artifact, results: [{address, title, heading, text, score}]}
  GET _api/read?address=          {artifact, address, title, content, sources}
  GET _api/ls?path=               {artifact, path, entries: [{address, title}]}
  GET _api/source?project=&offset=&length=   exact characters of the source report
                                  (code-point offsets into the UTF-8 decoded file)

The tools read only what the artifact carries: the search index the site ships
(``static/search/pages.json`` and ``sections.json``) and, when the artifact or
the image carries a ``corpus/`` tree, the finding and direction records and the
exact source reports. Search is keyword only for now, a small BM25 over
sections.json with the same tokenisation as theme/src/search/config.ts.
TODO(vector search): fuse with the int8 nomic vectors once the server holds an
embedding key.

This module ships in the server image with serve.py and imports nothing else
from the package.
"""

from __future__ import annotations

import json
import math
import pathlib
import re
import secrets
import threading
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Any

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

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
        """The file's bytes decoded as UTF-8 (undecodable bytes replaced), with its line
        endings as stored: offsets the API reports count code points of this text, so
        a CRLF report keeps its CRs rather than being read through newline translation."""
        if not self.corpus or not ID_RE.fullmatch(name):
            return None
        path = self.corpus / folder / f"{name}.md"
        if path.is_file() and path.resolve().is_relative_to(self.corpus.resolve()):
            return path.read_bytes().decode("utf-8", errors="replace")
        return None

    def report(self, project: str) -> str | None:
        """A project's source report: the staging copy ``<id>__REPORT.md``, else a
        copy stored under the published name ``<id>.md``."""
        text = self.markdown("sources", f"{project}__REPORT")
        return text if text is not None else self.markdown("sources", project)

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


COLLECTIONS = (
    "concepts",
    "topics",
    "conflicts",
    "entities",
    "summaries",
    "sources",
    "findings",
    "directions",
    "data",
)
EXCLUDED = ("authors",)
ADDRESS_PREFIX = "wiki/"


def allowed_slug(slug: str) -> bool:
    """A page the API may name: in one of the served collections, never authors/."""
    collection, _, rest = slug.partition("/")
    return collection in COLLECTIONS and bool(rest)


def address_of(slug: str, anchor: str = "") -> str:
    return f"{ADDRESS_PREFIX}{slug}" + (f"#{anchor}" if anchor else "")


def parse_address(address: str) -> tuple[str, str]:
    """(slug, section anchor) from wiki/<collection>/<slug>[#section]."""
    value = address.strip()
    if not value.startswith(ADDRESS_PREFIX):
        raise ValueError(f"address must start with {ADDRESS_PREFIX!r}: {address!r}")
    body, _, section = value[len(ADDRESS_PREFIX) :].partition("#")
    slug = page_path(body)
    if not allowed_slug(slug):
        raise ValueError(f"not a served collection: {address!r}")
    return slug, section.strip()


def sources_of(c: Corpus, slug: str, page: dict) -> list[str]:
    """The project ids a page cites: its links to summaries and source copies, or, for
    a source itself, its own id."""
    if slug.startswith("sources/"):
        return [slug.split("/", 1)[1].removesuffix("__REPORT")]
    out = set()
    for target in page.get("out", []) or []:
        collection, _, rest = target.partition("/")
        if collection in ("summaries", "sources") and rest:
            out.add(rest.removesuffix("__REPORT"))
    return sorted(out)


def search(c: Corpus, query: str, scope: str | None, k: int) -> dict[str, Any]:
    k = max(1, min(int(k), 50))
    scope = (scope or "").strip().strip("/")

    def allowed(i: int) -> bool:
        s = c.sections[i]
        if not allowed_slug(s["s"]):
            return False
        if not scope:
            return True
        page = c.by_slug.get(s["s"], {})
        if scope in GROUPS:
            return page.get("group") == scope
        return s["s"].startswith(scope + "/") or s["s"] == scope

    results = []
    for i, score in c.index.search(query, k, allowed):
        s = c.sections[i]
        page = c.by_slug.get(s["s"], {})
        results.append(
            {
                "address": address_of(s["s"], s.get("a", "")),
                "title": page.get("title", s["s"]),
                "group": page.get("group", ""),
                "heading": s.get("p", ""),
                "text": s["t"],
                "snippet": snippet(s["t"], query),
                "score": round(score, 3),
            }
        )
    return {
        "artifact": c.artifact,
        "build": c.build,
        "query": query,
        "scope": scope or None,
        "results": results,
    }


def read(c: Corpus, address: str) -> dict[str, Any] | None:
    """A page (or one section of it) as the site shows it; a source address returns the
    exact Markdown of the report. None when the page does not exist."""
    slug, section = parse_address(address)
    page = c.by_slug.get(slug)
    if slug.startswith("sources/"):
        # publish.ingest.published() drops the `__REPORT` staging suffix from the
        # page name; the corpus keeps it, so look the report up under both.
        text = c.report(slug.split("/", 1)[1])
        if text is None and page is None:
            return None
        content = text if text is not None else "\n\n".join(s["t"] for s in c.page_sections(slug))
        return {
            "artifact": c.artifact,
            "address": address_of(slug),
            "title": (page or {}).get("title", slug),
            "content": content,
            "sources": sources_of(c, slug, page or {}),
            "exact": text is not None,
        }
    if page is None:
        return None
    sections = c.page_sections(slug)
    if section:
        want = section.lower()
        sections = [
            s for s in sections if s.get("a", "").lower() == want or want in s.get("p", "").lower()
        ]
    parts = []
    for s in sections:
        heading = s.get("p", "")
        parts.append((f"## {heading}\n\n" if heading else "") + s["t"])
    return {
        "artifact": c.artifact,
        "address": address_of(slug, section),
        "title": page.get("title", slug),
        "group": page.get("group", ""),
        "description": page.get("desc", ""),
        "topics": page.get("topicSlugs", []),
        "content": "\n\n".join(parts),
        "sections": [{"heading": s.get("p", ""), "anchor": s.get("a", "")} for s in sections],
        "sources": sources_of(c, slug, page),
    }


def ls(c: Corpus, path: str) -> dict[str, Any]:
    """The collections, or the pages of one collection."""
    value = path.strip().strip("/").removeprefix(ADDRESS_PREFIX.rstrip("/")).strip("/")
    if not value:
        entries = [{"address": f"{ADDRESS_PREFIX}{name}", "title": name} for name in COLLECTIONS]
        return {"artifact": c.artifact, "path": ADDRESS_PREFIX, "entries": entries}
    if value not in COLLECTIONS:
        raise ValueError(f"not a served collection: {path!r}")
    entries = [
        {"address": address_of(p["slug"]), "title": p.get("title", p["slug"])}
        for p in c.pages
        if p["slug"].startswith(value + "/") and allowed_slug(p["slug"])
    ]
    return {"artifact": c.artifact, "path": f"{ADDRESS_PREFIX}{value}", "entries": entries}


def source(c: Corpus, project: str, offset: int, length: int) -> dict[str, Any]:
    """A slice of a project's source report by character offset, for exact quotes.
    Offsets, ``end`` and ``total`` count code points of the UTF-8 decoded file (see
    Corpus.markdown), the same text ``read`` returns whole."""
    if not ID_RE.fullmatch(project):
        raise ValueError("bad project id")
    text = c.report(project)
    if text is None:
        return {"artifact": c.artifact, "project": project, "error": "source not available"}
    offset = max(0, int(offset))
    length = max(1, min(int(length), MAX_READ))
    if offset >= len(text):
        return {"artifact": c.artifact, "project": project, "error": f"offset beyond {len(text)}"}
    piece = text[offset : offset + length]
    return {
        "artifact": c.artifact,
        "project": project,
        "offset": offset,
        "end": offset + len(piece),
        "total": len(text),
        "text": piece,
    }


def create_router(current: Callable[[], Corpus], token: str | None, prefix: str = "/wiki"):
    """The FastAPI router for /wiki/_api, guarded by the internal token."""
    router = APIRouter(prefix=prefix + "/_api")

    def refused(request: Request) -> JSONResponse | None:
        if not token:
            return JSONResponse({"error": "internal API is not configured"}, status_code=503)
        scheme, _, given = request.headers.get("authorization", "").partition(" ")
        if scheme.lower() != "bearer" or not secrets.compare_digest(given, token):
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        return None

    @router.get("/search")
    async def api_search(request: Request, q: str = "", scope: str | None = None, k: int = 8):
        if r := refused(request):
            return r
        c = current()
        if not q.strip():
            return JSONResponse({"artifact": c.artifact, "error": "q is required"}, status_code=400)
        return search(c, q, scope, k)

    @router.get("/read")
    async def api_read(request: Request, address: str):
        if r := refused(request):
            return r
        c = current()
        try:
            result = read(c, address)
        except ValueError as exc:
            return JSONResponse({"artifact": c.artifact, "error": str(exc)}, status_code=400)
        if result is None:
            return JSONResponse(
                {"artifact": c.artifact, "address": address, "error": "no such page"},
                status_code=404,
            )
        return result

    @router.get("/ls")
    async def api_ls(request: Request, path: str = ""):
        if r := refused(request):
            return r
        c = current()
        try:
            return ls(c, path)
        except ValueError as exc:
            return JSONResponse({"artifact": c.artifact, "error": str(exc)}, status_code=400)

    @router.get("/source")
    async def api_source(request: Request, project: str, offset: int = 0, length: int = 4000):
        if r := refused(request):
            return r
        c = current()
        try:
            result = source(c, project, offset, length)
        except ValueError as exc:
            return JSONResponse({"artifact": c.artifact, "error": str(exc)}, status_code=400)
        if "error" in result:
            return JSONResponse(result, status_code=404)
        return result

    return router
