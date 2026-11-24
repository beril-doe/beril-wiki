"""A SQLite view of the wiki, rebuilt from Git text in about a second.

The database is gitignored and disposable: delete it, or pull on another machine, and
the next command rebuilds it. It exists so an agent can ask "which sections discuss
this", "what does this section rest on" and "what links here" without reading pages.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import threading
import uuid
from pathlib import Path

import yaml

from beril_wiki.kb import pages
from beril_wiki.kb.store import DIGESTS, Store, sha256

SCHEMA = """
CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT);
CREATE TABLE sources (
    id TEXT PRIMARY KEY, title TEXT, path TEXT, sha256 TEXT, ingested TEXT, status TEXT);
CREATE TABLE claims (
    id TEXT PRIMARY KEY, source TEXT, kind TEXT, text TEXT, quote TEXT,
    start INTEGER, "end" INTEGER, heading TEXT, block TEXT, status TEXT, added TEXT);
CREATE INDEX claims_source ON claims (source);
CREATE TABLE pages (
    id TEXT PRIMARY KEY, kind TEXT, slug TEXT, title TEXT, type TEXT, description TEXT,
    words INTEGER);
CREATE TABLE sections (
    id TEXT PRIMARY KEY, page TEXT, anchor TEXT, ord INTEGER, heading TEXT, body TEXT,
    sha TEXT, words INTEGER);
CREATE INDEX sections_page ON sections (page);
CREATE TABLE section_sources (section TEXT, source TEXT, PRIMARY KEY (section, source));
CREATE INDEX section_sources_source ON section_sources (source);
CREATE TABLE section_claims (
    page TEXT, anchor TEXT, claim TEXT, how TEXT, PRIMARY KEY (page, anchor, claim));
CREATE INDEX section_claims_claim ON section_claims (claim);
CREATE TABLE links (src TEXT, anchor TEXT, dst TEXT, kind TEXT, label TEXT);
CREATE INDEX links_src ON links (src);
CREATE INDEX links_dst ON links (dst);
CREATE TABLE aliases (alias TEXT, page TEXT, PRIMARY KEY (alias, page));
CREATE TABLE backlog (
    id TEXT PRIMARY KEY, claim TEXT, source TEXT, target TEXT, reason TEXT, added TEXT);
CREATE VIRTUAL TABLE sections_fts USING fts5 (
    id UNINDEXED, kind UNINDEXED, title, heading, body, tokenize = 'porter unicode61');
CREATE VIRTUAL TABLE claims_fts USING fts5 (
    id UNINDEXED, source UNINDEXED, text, quote, tokenize = 'porter unicode61');
"""
VERSION = "1"
ALIASES = re.compile(r"\*\*Known aliases:\*\*\s*(.+)")
TITLE = re.compile(r"^# +(.+?)\s*$", re.M)
# Edit sessions run in parallel threads and each tool call may find the index stale.
_BUILD = threading.Lock()
WATCHED = ("wiki", "knowledge", "corpus/projects", "corpus/docs")
STATE_FILES = ("curator-topics.json", "links.json")


def db_path(root: Path) -> Path:
    return Path(os.environ.get("BERIL_WIKI_INDEX", root / ".agentic" / "index.db"))


def fingerprint(root: Path) -> str:
    """Changes whenever a file the index reads is added, removed or rewritten."""
    count, newest, size = 0, 0, 0
    files = [root / "state" / name for name in STATE_FILES]
    for top in WATCHED:
        base = root / top
        if base.is_dir():
            files.extend(p for p in base.rglob("*") if p.suffix in (".md", ".json", ".jsonl"))
    for path in files:
        try:
            stat = path.stat()
        except OSError:
            continue
        count += 1
        size += stat.st_size
        newest = max(newest, stat.st_mtime_ns)
    return f"{VERSION}:{count}:{size}:{newest}"


def front_fields(front: str) -> dict:
    if not front:
        return {}
    try:
        fields = yaml.safe_load(front.strip().strip("-"))
    except yaml.YAMLError:
        return {}
    return fields if isinstance(fields, dict) else {}


def normalize(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def build(root: Path, path: Path | None = None) -> Path:
    """Write a fresh index beside the old one, then swap it in."""
    store = Store(root)
    path = path or db_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = fingerprint(root)
    tmp = path.with_name(f"{path.name}.{uuid.uuid4().hex}.tmp")
    db = sqlite3.connect(tmp)
    try:
        db.executescript(SCHEMA)
        _sources(db, store)
        _claims(db, store)
        known = _pages(db, store)
        _sidecars(db, store, known)
        _state_links(db, root, known)
        db.executemany(
            "INSERT OR REPLACE INTO backlog VALUES (?, ?, ?, ?, ?, ?)",
            [
                (
                    b["id"],
                    b.get("claim"),
                    b.get("source"),
                    b.get("target"),
                    b.get("reason"),
                    b.get("added"),
                )
                for b in store.backlog()
            ],
        )
        db.execute("INSERT INTO meta VALUES ('fingerprint', ?)", (stamp,))
        db.commit()
    except BaseException:
        db.close()
        tmp.unlink(missing_ok=True)
        raise
    db.close()
    os.replace(tmp, path)
    return path


def _sources(db: sqlite3.Connection, store: Store) -> None:
    ingested = store.sources()
    for sid in sorted(set(store.corpus_sources()) | set(ingested)):
        file = store.source_path(sid)
        text = file.read_text(encoding="utf-8") if file.exists() else None
        current = sha256(text) if text is not None else None
        seen = ingested.get(sid, {}).get("sha256")
        if text is None:
            status = "missing"
        elif seen is None:
            status = "new"
        else:
            status = "current" if seen == current else "changed"
        title = TITLE.search(text) if text else None
        db.execute(
            "INSERT INTO sources VALUES (?, ?, ?, ?, ?, ?)",
            (
                sid,
                re.sub(r"^Report:\s*", "", title.group(1)) if title else sid,
                str(file.relative_to(store.root)),
                current,
                seen,
                status,
            ),
        )


def _claims(db: sqlite3.Connection, store: Store) -> None:
    for source in store.claim_sources():
        rows = store.claims(source)
        db.executemany(
            "INSERT INTO claims VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [
                (
                    c["id"],
                    source,
                    c["kind"],
                    c["text"],
                    c["quote"],
                    c["start"],
                    c["end"],
                    c.get("heading", ""),
                    c.get("block", ""),
                    c.get("status", "active"),
                    c.get("added", ""),
                )
                for c in rows
            ],
        )
        db.executemany(
            "INSERT INTO claims_fts VALUES (?, ?, ?, ?)",
            [
                (c["id"], source, c["text"], c["quote"])
                for c in rows
                if c.get("status", "active") != "retracted"
            ],
        )


def _pages(db: sqlite3.Connection, store: Store) -> set[str]:
    known = set(store.page_ids())
    for page_id in sorted(known):
        text = store.page_path(page_id).read_text(encoding="utf-8", errors="replace")
        page = pages.parse(text)
        kind, _, slug = page_id.rpartition("/")
        fields = front_fields(page.front)
        title = page.title or slug
        db.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                page_id,
                kind,
                slug,
                title,
                str(fields.get("type", "")),
                str(fields.get("description", "")),
                sum(s.words for s in page.sections),
            ),
        )
        names = {normalize(title), normalize(slug)}
        for ord_, section in enumerate(page.sections):
            sid = f"{page_id}#{section.anchor}"
            db.execute(
                "INSERT INTO sections VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    sid,
                    page_id,
                    section.anchor,
                    ord_,
                    section.heading,
                    section.body,
                    section.sha,
                    section.words,
                ),
            )
            # Raw reports are evidence, read by span; searching them would return the
            # source in place of what the wiki says about it.
            if kind != "sources":
                db.execute(
                    "INSERT INTO sections_fts VALUES (?, ?, ?, ?, ?)",
                    (sid, kind, title, section.heading, section.body),
                )
            db.executemany(
                "INSERT OR IGNORE INTO section_sources VALUES (?, ?)",
                [(sid, s) for s in pages.sources_in(section.body)],
            )
            db.executemany(
                "INSERT INTO links VALUES (?, ?, ?, 'wikilink', '')",
                [(page_id, section.anchor, dst) for dst in pages.links_in(section.body)],
            )
            if kind == "entities":
                for found in ALIASES.finditer(section.body):
                    listed = pages.SRC_TAG.sub("", found.group(1)).strip().rstrip(".")
                    if not listed.lower().startswith("no "):
                        names.update(normalize(a) for a in re.split(r"[;,]", listed))
        db.executemany(
            "INSERT OR IGNORE INTO aliases VALUES (?, ?)", [(n, page_id) for n in names if n]
        )
    return known


def _sidecars(db: sqlite3.Connection, store: Store, known: set[str]) -> None:
    for page_id, data in store.sidecars().items():
        if page_id not in known:
            continue
        rows = [(page_id, "", claim, how) for claim, how in data.get("claims", {}).items()]
        for anchor, section in data.get("sections", {}).items():
            rows += [(page_id, anchor, c, how) for c, how in section.get("claims", {}).items()]
        db.executemany("INSERT OR IGNORE INTO section_claims VALUES (?, ?, ?, ?)", rows)


def _state_links(db: sqlite3.Connection, root: Path, known: set[str]) -> None:
    """Relations the card stages already keep: topic membership, linked findings,
    and the concept each conflict page belongs to."""
    topics = root / "state" / "curator-topics.json"
    if topics.exists():
        for group in json.loads(topics.read_text(encoding="utf-8")).get("groups", []):
            hub = f"topics/{pages.slug(group['title'])}"
            db.executemany(
                "INSERT INTO links VALUES (?, '', ?, 'topic', ?)",
                [(hub, f"concepts/{stem}", group["title"]) for stem in group["concepts"]],
            )
    linked = root / "state" / "links.json"
    if linked.exists():
        rows = json.loads(linked.read_text(encoding="utf-8")).get("links", [])
        db.executemany(
            "INSERT INTO links VALUES (?, '', ?, 'finding-link', ?)",
            [
                (f"findings/{r['a']}", f"findings/{r['b']}", f"{r.get('type', '')}: {r['label']}")
                for r in rows
            ],
        )
    for page_id in known:
        if page_id.startswith("conflicts/conflict--"):
            concept = f"concepts/{page_id.split('--')[1]}"
            if concept in known:
                db.execute(
                    "INSERT INTO links VALUES (?, '', ?, 'conflict', '')", (page_id, concept)
                )


def _stale(root: Path, path: Path) -> bool:
    if not path.exists():
        return True
    db = sqlite3.connect(path)
    try:
        row = db.execute("SELECT value FROM meta WHERE key = 'fingerprint'").fetchone()
        return row is None or row[0] != fingerprint(root)
    except sqlite3.DatabaseError:
        return True
    finally:
        db.close()


def connect(root: Path) -> sqlite3.Connection:
    """A read connection to a current index, rebuilding it first when files changed."""
    path = db_path(root)
    if _stale(root, path):
        with _BUILD:
            # Another thread may have rebuilt it while this one waited.
            if _stale(root, path):
                build(root, path)
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    return db


def is_digest(source: str) -> bool:
    return source in DIGESTS
