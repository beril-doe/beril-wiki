"""Read-only view of the lakehouse catalog that the directions and followups stages share.

``state/lakehouse/`` is built by ``beril_wiki.stages.lakehouse``. This module only
reads it, imports nothing outside the standard library, and is hashed into the
stage cache keys, so every output must be identical across processes (no set or
hash-seed order may reach the text).
"""

from __future__ import annotations

import gzip
import json
import math
import re
from collections.abc import Iterable, Sequence
from pathlib import Path

CATALOG_DIR = Path("state/lakehouse")
FILES = (
    "catalog.jsonl",
    "values.jsonl.gz",
    "databases.jsonl",
    "usage.json",
    "coverage.json",
    "manifest.json",
)

ROUTES: dict[str, str] = {
    "kbase.uniref50": "data/kbase-uniref",
    "kbase.uniref90": "data/kbase-uniref",
    "kbase.uniref100": "data/kbase-uniref",
    "kbase.nmdc_arkin": "data/nmdc-arkin",
    "protect.genomedepot": "data/protect-genomedepot",
}
TENANT_ROUTES: dict[str, str] = {
    "phagefoundry": "data/phagefoundry",
    "planetmicrobe": "data/planetmicrobe",
}

ABSENCE: tuple[re.Pattern[str], ...] = tuple(
    re.compile(p, re.IGNORECASE)
    for p in (
        r"\bnot (?:held |stored |available |present )?in the (?:kbase )?(?:data )?lakehouse\b",
        r"\blakehouse (?:lacks|is missing)\b",
        r"\blakehouse does(?: not|n't) (?:hold|have|contain|include)\b",
        r"\bno (?:kbase )?(?:data )?lakehouse data\b",
        r"\bthe lakehouse (?:holds|has|contains) no\b",
        r"\babsent from the (?:kbase )?(?:data )?lakehouse\b",
    )
)

MAX_COLUMNS = 60
MAX_TABLE_NAMES = 40
MAX_NAME_CHARS = 240  # keeps the directory under about 10K tokens as the catalog grows
MAX_VALUES = 20
TOP_VALUES = 5
STOPWORDS = frozenset(
    "and the for with from that this are was were what which how why does not can has have "
    "its into than then them they their there these those about between across using used "
    "use any all but also may might more most other such only over under per via our out "
    "who whom whose when where while will would should could been being both each few some".split()
)
MONTHS = (
    "January February March April May June July August September October November December"
).split()
_WORD = re.compile(r"[a-z0-9]{3,}")
_QUOTES = " \t\r\n`'\""


def absence_claims(text: str) -> list[str]:
    """Return the phrases in ``text`` that claim data is absent from the lakehouse.

    Parameters
    ----------
    text : str
        Prose to scan.

    Returns
    -------
    list[str]
        The matched phrases in the order they appear.
    """
    found = [(m.start(), m.group(0)) for pattern in ABSENCE for m in pattern.finditer(text)]
    return [phrase for _, phrase in sorted(found)]


def slug(database: str) -> str:
    """Return the page slug of a database name."""
    return re.sub(r"[^a-z0-9]+", "-", database.lower()).strip("-")


def words(text: str) -> frozenset[str]:
    """Return the lowercase alphanumeric words of 3 or more characters, minus stopwords."""
    return frozenset(w for w in _WORD.findall(text.lower()) if w not in STOPWORDS)


def clean(name: str) -> str:
    """Strip whitespace, quotes, backticks and a trailing period, then lowercase."""
    prev = None
    while prev != name:
        prev = name
        name = name.strip(_QUOTES).rstrip(".")
    return name.lower()


def _read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


class Catalog:
    """The catalog files of one checkout, read once and queried by name or by words."""

    def __init__(self, root: Path | None = None) -> None:
        self.root = root
        folder = (root / CATALOG_DIR) if root is not None else None
        self.tables: list[dict] = []
        self._databases: list[dict] = []
        self._usage: dict = {}
        self._coverage: dict = {}
        self._manifest: dict = {}
        self._values_path: Path | None = None
        if folder is not None and (folder / "catalog.jsonl").is_file():
            self.tables = self._jsonl(folder / "catalog.jsonl")
            self._databases = self._jsonl(folder / "databases.jsonl")
            self._usage = _read_json(folder / "usage.json")
            self._coverage = _read_json(folder / "coverage.json")
            self._manifest = _read_json(folder / "manifest.json")
            self._values_path = folder / "values.jsonl.gz"
        self.empty = not self.tables
        self.tables.sort(key=lambda r: (r["database"], r["table"]))
        self._by_table = {(r["database"], r["table"]): r for r in self.tables}
        # clean() lowercases a requested name, so lookups use the lowercased table name.
        self._by_lower: dict[tuple[str, str], dict] = {}
        for row in self.tables:
            self._by_lower.setdefault((row["database"], row["table"].lower()), row)
        self._by_database: dict[str, dict] = {}
        for row in self._databases:
            self._by_database[row["database"]] = row
        self._database_names: dict[str, str] = {}
        for dotted, row in sorted(self._by_database.items()):
            self._database_names[dotted] = dotted
            self._database_names.setdefault(str(row.get("legacy", "")).lower(), dotted)
        for row in self.tables:
            self._database_names.setdefault(row["database"], row["database"])
            self._database_names.setdefault(str(row.get("legacy", "")).lower(), row["database"])
        self._values: dict[tuple[str, str], list[dict]] | None = None
        self._index: dict[str, dict[str, set[int]]] | None = None
        self._tables_of: dict[str, list[str]] = {}
        for row in self.tables:
            self._tables_of.setdefault(row["database"], []).append(row["table"])

    @staticmethod
    def _jsonl(path: Path) -> list[dict]:
        try:
            with path.open(encoding="utf-8") as f:
                return [json.loads(line) for line in f if line.strip()]
        except OSError:
            return []

    def _database(self, name: str) -> str | None:
        return self._database_names.get(clean(name))

    def exists(self, name: str) -> dict | None:
        """Return the catalog row for a table or the databases row for a database.

        Accepts dotted or legacy names in any case, wrapped in quotes or backticks.
        A database is tried first, then a table split at the last ".".

        Parameters
        ----------
        name : str
            A table or database name as a model or reader wrote it.

        Returns
        -------
        dict or None
            A row with ``"table"`` for a table, one without for a database, else None.
        """
        cleaned = clean(name)
        dotted = self._database_names.get(cleaned)
        if dotted is not None:
            return self._by_database.get(dotted) or {"database": dotted}
        head, _, tail = cleaned.rpartition(".")
        dotted = self._database_names.get(head)
        if dotted is None or not tail:
            return None
        return self._by_lower.get((dotted, tail))

    def canonical(self, name: str) -> str | None:
        """Return ``"<db>.<table>"`` or ``"<db>"`` in dotted form with the stored spelling,
        or None when unknown."""
        row = self.exists(name)
        if row is None:
            return None
        return f"{row['database']}.{row['table']}" if "table" in row else row["database"]

    def directory(self) -> str:
        """List every covered database with its tenant, table count and first table names."""
        if self.empty:
            return ""
        names = ", ".join(str(t.get("display_name") or t["name"]) for t in self._covered())
        lines = [
            f"Covered tenants: {names}. Other tenants exist in the lakehouse and are not "
            "shown here, so a table missing from this list may still exist."
        ]
        for dotted in sorted(self._tables_of):
            tables = sorted(self._tables_of[dotted])
            row = self._by_database.get(dotted, {})
            tenant = row.get("tenant_name") or row.get("tenant") or dotted.split(".")[0]
            shown: list[str] = []
            size = 0
            for name in tables[:MAX_TABLE_NAMES]:
                if shown and size + len(name) > MAX_NAME_CHARS:
                    break
                shown.append(name)
                size += len(name) + 2
            more = len(tables) - len(shown)
            tail = f" +{more} more" if more > 0 else ""
            lines.append(f"{dotted} ({tenant}, {len(tables)} tables): {', '.join(shown)}{tail}")
        return "\n".join(lines)

    def _covered(self) -> list[dict]:
        covered = self._coverage.get("covered", [])
        return covered if isinstance(covered, list) else []

    def _value_rows(self) -> dict[tuple[str, str], list[dict]]:
        if self._values is None:
            by_table: dict[tuple[str, str], list[dict]] = {}
            if self._values_path is not None and self._values_path.is_file():
                with gzip.open(self._values_path, "rt", encoding="utf-8") as f:
                    for line in f:
                        if line.strip():
                            row = json.loads(line)
                            by_table.setdefault((row["database"], row["table"]), []).append(row)
            for rows in by_table.values():
                rows.sort(key=lambda r: r["column"])
            self._values = by_table
        return self._values

    def _word_index(self) -> dict[str, dict[str, set[int]]]:
        """Map each word to the tables that hold it as a table name, column name or value."""
        if self._index is None:
            index: dict[str, dict[str, set[int]]] = {"table": {}, "column": {}, "value": {}}
            position = {key: i for i, key in enumerate(self._by_table)}
            for (database, table), i in position.items():
                for w in words(table):
                    index["table"].setdefault(w, set()).add(i)
                for column in self._by_table[(database, table)]["columns"]:
                    for w in words(column[0]):
                        index["column"].setdefault(w, set()).add(i)
            for key, rows in self._value_rows().items():
                i = position.get(key)
                if i is None:
                    continue
                for row in rows:
                    for value in row["values"]:
                        for w in words(value):
                            index["value"].setdefault(w, set()).add(i)
            self._index = index
        return self._index

    def _scores(self, text: str) -> dict[int, float]:
        index = self._word_index()
        total = max(len(self.tables), 1)
        scores: dict[int, float] = {}
        for kind, weight in (("table", 3.0), ("column", 2.0), ("value", 1.0)):
            for w in sorted(words(text)):
                hits = index[kind].get(w, ())
                if not hits:
                    continue
                gain = weight * math.log(1 + total / len(hits))
                for i in hits:
                    scores[i] = round(scores.get(i, 0.0) + gain, 6)
        return scores

    def matched(
        self, text: str, projects: Sequence[str], limit: int, tables: Sequence[str] = ()
    ) -> list[dict]:
        """Return up to ``limit`` table views ranked for a question.

        Order: ``tables`` as given, then the tables that ``projects`` use in
        ``usage.json``, then the rest by word overlap with table names, column
        names and values. Ties break by (database, table).

        Parameters
        ----------
        text : str
            The topic or question the view serves.
        projects : Sequence[str]
            Project ids whose usage ranks tables first.
        limit : int
            The most tables to return.
        tables : Sequence[str]
            Tables to place first, in any accepted name form.

        Returns
        -------
        list[dict]
            One view per table: ``table``, ``rows``, ``column_count``, ``columns``,
            ``columns_truncated``, ``source`` and ``values`` (at most 20 values).
        """
        if self.empty or limit <= 0:
            return []
        keys = list(self._by_table)
        position = {key: i for i, key in enumerate(keys)}
        scores = self._scores(text)
        chosen: list[tuple[str, str]] = []
        seen: set[tuple[str, str]] = set()

        def take(candidates: Iterable[tuple[str, str]]) -> None:
            for key in candidates:
                if key in self._by_table and key not in seen:
                    seen.add(key)
                    chosen.append(key)

        for name in tables:
            row = self.exists(name)
            if row and "table" in row:
                take([(row["database"], row["table"])])
        used: set[tuple[str, str]] = set()
        for project in projects:
            for name in self._usage.get(project, {}).get("tables", []):
                head, _, tail = name.rpartition(".")
                used.add((head, tail))
        take(sorted(used, key=lambda k: (-scores.get(position.get(k, -1), 0.0), k)))
        rest = [k for k in keys if k not in seen and scores.get(position[k], 0.0) > 0]
        take(sorted(rest, key=lambda k: (-scores[position[k]], k)))
        wanted = words(text)
        return [self._view(key, wanted) for key in chosen[:limit]]

    def _view(self, key: tuple[str, str], wanted: frozenset[str]) -> dict:
        row = self._by_table[key]
        columns = [f"{n} {t}".strip() for n, t in row["columns"][:MAX_COLUMNS]]
        order = {n: i for i, (n, _) in enumerate(row["columns"])}
        profiled = sorted(
            self._value_rows().get(key, []),
            key=lambda r: (order.get(r["column"], len(order)), r["column"]),
        )
        picked: dict[str, list[str]] = {r["column"]: [] for r in profiled}
        budget = MAX_VALUES
        for r in profiled:
            for value in r["values"]:
                if budget and words(value) & wanted:
                    picked[r["column"]].append(value)
                    budget -= 1
        for r in profiled:
            for value in r["values"][:TOP_VALUES]:
                if budget and value not in picked[r["column"]]:
                    picked[r["column"]].append(value)
                    budget -= 1
        values = {}
        for r in profiled:
            if picked[r["column"]]:
                shown = [v for v in r["values"] if v in picked[r["column"]]]
                values[r["column"]] = {
                    "values": shown,
                    "complete": bool(r["complete"]) and len(shown) == len(r["values"]),
                    "basis": r["basis"],
                }
        return {
            "table": f"{key[0]}.{key[1]}",
            "rows": row["rows"],
            "column_count": row["column_count"],
            "columns": columns,
            "columns_truncated": bool(row["columns_truncated"])
            or len(columns) < row["column_count"],
            "source": row["source"],
            "values": values,
        }

    def route(self, database: str) -> str:
        """Return the site path (``data/<slug>``) of a database's page."""
        dotted = self._database(database) or clean(database)
        if dotted in ROUTES:
            return ROUTES[dotted]
        row = self._by_database.get(dotted, {})
        tenant = row.get("tenant") or dotted.split(".")[0].split("_")[0]
        if tenant in TENANT_ROUTES:
            return TENANT_ROUTES[tenant]
        return f"data/{slug(dotted)}"

    def _page(self, database: str) -> Path | None:
        if self.root is None:
            return None
        page = self.root / "wiki" / f"{self.route(database)}.md"
        return page if page.is_file() else None

    def curated(self, database: str) -> bool:
        """Return True when the database's route stem is a page under ``wiki/data/``."""
        return self._page(database) is not None

    def title(self, database: str) -> str:
        """Return the curated page's H1, else the dotted database name."""
        dotted = self._database(database) or clean(database)
        page = self._page(database)
        if page is not None:
            for line in page.read_text(encoding="utf-8").splitlines():
                if line.startswith("# "):
                    return line[2:].strip()
        return dotted

    def coverage(self) -> dict:
        """Return ``coverage.json``: the covered and uncovered tenants."""
        return self._coverage

    def tenants_covered(self) -> int:
        """Return how many tenants the catalog covers."""
        return len(self._covered())

    def snapshot(self) -> str:
        """Return the packet snapshot date as ``11 November 2026``, or "" when unknown."""
        stamp = str(self._manifest.get("snapshot_utc", ""))
        m = re.match(r"(\d{4})-(\d{2})-(\d{2})", stamp)
        if not m:
            return ""
        return f"{int(m[3])} {MONTHS[int(m[2]) - 1]} {m[1]}"


_CACHE: dict[tuple[Path, tuple[int | None, ...]], Catalog] = {}


def load(root: Path) -> Catalog:
    """Return the catalog under ``root``, cached until any of its six files changes.

    Parameters
    ----------
    root : Path
        The checkout holding ``state/lakehouse/``.

    Returns
    -------
    Catalog
        An empty catalog when ``catalog.jsonl`` is absent.
    """
    root = root.resolve()
    folder = root / CATALOG_DIR
    if not (folder / "catalog.jsonl").is_file():
        return Catalog(None)
    stamps = []
    for name in FILES:
        try:
            stamps.append((folder / name).stat().st_mtime_ns)
        except OSError:
            stamps.append(None)
    key = (root, tuple(stamps))
    if key not in _CACHE:
        _CACHE.clear()
        _CACHE[key] = Catalog(root)
    return _CACHE[key]
