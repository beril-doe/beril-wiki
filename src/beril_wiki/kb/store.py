"""The canonical records under ``knowledge/``: plain text that Git merges and diffs.

    knowledge/sources.jsonl          one row per report: the content hash last ingested
    knowledge/claims/<source>.jsonl  one claim per line, each anchored to a verbatim quote
    knowledge/pages/<kind>/<slug>.json
                                     which claims each section of a page rests on
    knowledge/backlog/<source>.jsonl findings queued because a cap was reached
    knowledge/log/<run>.jsonl        one line per accepted change: who wrote and reviewed it

Files are split by report, page or run so that two machines ingesting different reports
touch different files and Git merges them without conflict.

Nothing here is a cache. A row changes only when a report is ingested or revised or a
section is edited, never because code, prompts or configuration changed.
"""

from __future__ import annotations

import fcntl
import hashlib
import json
import os
import re
import tempfile
from collections.abc import Iterable, Iterator
from contextlib import contextmanager
from pathlib import Path

# Collection pages built from the observatory's docs, not project reports.
DIGESTS = ("discoveries", "pitfalls")
CLAIM_KINDS = ("finding", "caveat", "figure", "entity", "null")
HEADING = re.compile(r"^(#{1,6}) +(.+?)\s*$", re.M)


class Busy(Exception):
    """Another run holds the checkout."""


@contextmanager
def checkout_lock(root: Path) -> Iterator[None]:
    """One writer per checkout. The file is the curator's own lock
    (``agentic.runner.locked``), so a curator run and this pipeline exclude each other."""
    folder = Path(root) / ".agentic"
    folder.mkdir(exist_ok=True)
    with (folder / "lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Busy("another pipeline run owns this checkout") from None
        yield


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_text(path: Path, text: str) -> None:
    """Replace a file in one step, so a crash leaves the old or the new content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            out.write(text)
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    write_text(path, "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def block_of(text: str, start: int) -> tuple[str, str]:
    """The report heading a character offset falls under, and a hash of that block.

    A quote can survive a revision that changes the table or the denominator beside it.
    The block hash lets ``revise`` tell a claim whose surroundings changed from one that
    only moved.
    """
    begin, heading = 0, ""
    end = len(text)
    for m in HEADING.finditer(text):
        if m.start() <= start:
            begin, heading = m.start(), m.group(2)
        else:
            end = m.start()
            break
    return heading, sha256(text[begin:end].strip())[:12]


def blocks(text: str) -> list[tuple[int, int, str]]:
    """A report cut at its headings: (start, end, hash) per block, as ``block_of`` hashes."""
    cuts = [0, *[m.start() for m in HEADING.finditer(text) if m.start() > 0], len(text)]
    return [
        (a, b, sha256(text[a:b].strip())[:12])
        for a, b in zip(cuts, cuts[1:], strict=False)
        if b > a
    ]


class Store:
    def __init__(self, root: Path) -> None:
        self.root = Path(root)
        self.dir = self.root / "knowledge"

    # Reports

    def source_path(self, source: str) -> Path:
        """Where the vendored corpus keeps a report or a digest."""
        if source in DIGESTS:
            return self.root / "corpus" / "docs" / f"{source}.md"
        return self.root / "corpus" / "projects" / source / "REPORT.md"

    def source_text(self, source: str) -> str:
        return self.source_path(source).read_text(encoding="utf-8")

    def corpus_sources(self) -> list[str]:
        """Every report id the corpus holds, digests included."""
        projects = self.root / "corpus" / "projects"
        found = [p.parent.name for p in projects.glob("*/REPORT.md")] if projects.is_dir() else []
        found += [d for d in DIGESTS if self.source_path(d).exists()]
        return sorted(found)

    def sources(self) -> dict[str, dict]:
        return {r["id"]: r for r in read_jsonl(self.dir / "sources.jsonl")}

    def write_sources(self, rows: dict[str, dict]) -> None:
        write_jsonl(self.dir / "sources.jsonl", (rows[k] for k in sorted(rows)))

    # Claims

    def claims_path(self, source: str) -> Path:
        return self.dir / "claims" / f"{source}.jsonl"

    def claims(self, source: str) -> list[dict]:
        return read_jsonl(self.claims_path(source))

    def write_claims(self, source: str, claims: list[dict]) -> None:
        write_jsonl(self.claims_path(source), claims)

    def claim_sources(self) -> list[str]:
        folder = self.dir / "claims"
        return sorted(p.stem for p in folder.glob("*.jsonl")) if folder.is_dir() else []

    # Page sidecars

    def sidecar_path(self, page: str) -> Path:
        return self.dir / "pages" / f"{page}.json"

    def sidecar(self, page: str) -> dict:
        path = self.sidecar_path(page)
        if not path.exists():
            return {"sections": {}}
        return json.loads(path.read_text(encoding="utf-8"))

    def write_sidecar(self, page: str, data: dict) -> None:
        data = {**data, "sections": {k: v for k, v in data.get("sections", {}).items() if v}}
        path = self.sidecar_path(page)
        if not data["sections"] and not data.get("claims"):
            path.unlink(missing_ok=True)
            return
        write_text(path, json.dumps(data, ensure_ascii=False, indent=1, sort_keys=True) + "\n")

    def sidecars(self) -> dict[str, dict]:
        folder = self.dir / "pages"
        if not folder.is_dir():
            return {}
        return {
            str(p.relative_to(folder).with_suffix("")): json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(folder.rglob("*.json"))
        }

    # Backlog and lineage

    def backlog(self, source: str | None = None) -> list[dict]:
        folder = self.dir / "backlog"
        if source is not None:
            return read_jsonl(folder / f"{source}.jsonl")
        if not folder.is_dir():
            return []
        return [row for path in sorted(folder.glob("*.jsonl")) for row in read_jsonl(path)]

    def queue(self, source: str, rows: list[dict]) -> None:
        """Add queued findings for one report, replacing rows with the same id."""
        path = self.dir / "backlog" / f"{source}.jsonl"
        kept = {r["id"]: r for r in read_jsonl(path)} | {r["id"]: r for r in rows}
        if kept:
            write_jsonl(path, (kept[k] for k in sorted(kept)))

    def unqueue(self, source: str, ids: set[str]) -> None:
        path = self.dir / "backlog" / f"{source}.jsonl"
        kept = [r for r in read_jsonl(path) if r["id"] not in ids]
        if kept:
            write_jsonl(path, kept)
        else:
            path.unlink(missing_ok=True)

    def log(self, run: str, **entry: object) -> None:
        path = self.dir / "log" / f"{run}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as out:
            out.write(json.dumps(entry, ensure_ascii=False) + "\n")

    # Wiki pages

    def page_path(self, page: str) -> Path:
        return self.root / "wiki" / f"{page}.md"

    def page_ids(self) -> list[str]:
        wiki = self.root / "wiki"
        return sorted(str(p.relative_to(wiki).with_suffix("")) for p in wiki.rglob("*.md"))
