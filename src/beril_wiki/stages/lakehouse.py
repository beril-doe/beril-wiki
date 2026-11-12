#!/usr/bin/env python3
"""Lakehouse catalog: the tables, columns and values the question stages may cite.

Merges three local snapshots into ``state/lakehouse/``, with no model and no
network:

- the hub catalog packet of 2026-11-11 (``--packet``, a folder with its ``.zip``
  beside it): schema, row counts and value profiles for the 11 tenants the
  exporting account can read;
- a pinned semcat snapshot (``--semcat``, commit e3a8b81, harvested 2026-11-04):
  production tables, columns, types, row counts and producer-written
  descriptions for 12 more tenants, never values;
- the May 2026 BERDL Data Atlas table map (``--atlas``): the tables of 8 of those
  tenants that semcat lacks, schema only and marked "May 2026, not re-checked".

``--tenants`` optionally adds a hub tenant listing, so the coverage note can name
the tenants the catalog does not cover. ``usage.json`` records which databases
and tables each observatory project (``BERIL_CHECKOUT``) names.

Outputs: ``catalog.jsonl``, ``values.jsonl.gz``, ``databases.jsonl``,
``usage.json``, ``coverage.json`` and ``manifest.json``. Values are kept only
for the shared tenants in ``VALUE_TENANTS``; personal namespaces, people fields
and email-, ORCID- or URL-shaped values never reach an output, and ``--check``
re-proves that on the committed files.

Refresh cost: the build itself is free, but a changed ``catalog.jsonl`` reruns
directions for every topic (about USD 22 to 38) and then followups.

    uv run python -m beril_wiki.stages.lakehouse --packet DIR --semcat DIR --atlas CSV
        [--tenants JSONL]
    uv run python -m beril_wiki.stages.lakehouse --check [--semcat DIR]
"""

from __future__ import annotations

import argparse
import csv
import gzip
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict
from collections.abc import Iterable, Iterator
from pathlib import Path

from pydantic import BaseModel, ConfigDict

from beril_wiki.paths import ROOT
from beril_wiki.stages.fetch import CHECKOUT

OUT = Path("state/lakehouse")
SOURCES = ("packet-2026-11-11", "semcat-2026-11-04", "atlas-2026-05")
SOURCE_DATES = dict(zip(SOURCES, ("2026-11-11", "2026-11-04", "2026-05"), strict=True))
VALUE_TENANTS = ("globalusers", "kbase", "kescience", "nmdc", "planetmicrobe", "refdata")
ATLAS_TENANTS = (
    "arkinlab",
    "ese",
    "evaluation",
    "lambda",
    "netl",
    "phagefoundry",
    "protect",
    "usgs",
)
SEMCAT_TENANTS = (*ATLAS_TENANTS, "aiale", "aimbiocm", "conwaylab", "enigmay12")
LEGACY_EXCEPTIONS = {"kbase.nmdc_arkin": "nmdc_arkin"}
REDACT_TOKENS: frozenset[str] = frozenset(
    """url urls uri uris purl purls orcid orcids email emails password passwd token tokens
    secret secrets apikey api_key phone phones user users username usernames author authors
    coauthors person persons investigator investigators contributor contributors creator
    creators submitter submitters contact contacts agent agents expert experts people curator
    curators maintainer maintainers owner owners""".split()
)
PERSON_COLUMNS: frozenset[str] = frozenset(
    # full_name stays off: taxon and gene tables use it; a people table's copy goes anyway.
    """first_name last_name given_name family_name middle_name surname firstname
    lastname""".split()
)
# A table named for people holds their names in columns no token marks (first_name, expert).
PERSON_TABLES: frozenset[str] = frozenset(
    """user users person persons people author authors contact contacts expert experts
    contributor contributors creator creators submitter submitters investigator investigators
    agent agents""".split()
)
DATABASE_NAME = re.compile(r"[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*")
TABLE_NAME = re.compile(r"[A-Za-z0-9_]+")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
ORCID = re.compile(r"(?<![0-9])[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9Xx](?![0-9A-Za-z])")
URL = re.compile(r"(?i)\b(?:https?|s?ftp)://\S|\bwww\.[A-Za-z0-9-]+\.")
PERSONAL_TEXT = re.compile(r"(?<![\w.])u_[a-z0-9_]+\.[a-z0-9_]")

MAX_COLUMNS = 200
MAX_VALUE = 60
MAX_DESCRIPTION = 400
CAPS = {"catalog.jsonl": 3_000_000, "values.jsonl.gz": 4_000_000}
FILES = (
    "catalog.jsonl",
    "values.jsonl.gz",
    "databases.jsonl",
    "usage.json",
    "coverage.json",
    "manifest.json",
)
COST_NOTE = (
    "a changed catalog reruns directions for every topic (about USD 22 to 38) and then followups"
)


class Inputs(BaseModel):
    """Paths of one build's inputs.

    Attributes
    ----------
    packet : Path
        The hub catalog packet folder; ``<packet>.zip`` must sit beside it.
    semcat : Path
        The pinned semcat snapshot folder, with ``COMMIT`` and ``SHA256SUMS``.
    atlas : Path
        The May 2026 atlas ``table_topic_map.csv``.
    tenants : Path or None
        An optional hub tenant listing (JSON lines).
    checkout : Path
        The observatory checkout whose ``projects/`` the usage scan reads.
    """

    packet: Path
    semcat: Path
    atlas: Path
    tenants: Path | None
    checkout: Path


class _Row(BaseModel):
    # Unlisted fields (owner, bounds, people, L4 text) are never read into a model.
    model_config = ConfigDict(extra="ignore")


class PacketColumn(_Row):
    name: str
    type: str | None = None


class PacketTable(_Row):
    database: str
    table: str
    comment: str | None = None
    row_count: int | None = None
    columns: list[PacketColumn] = []


class PacketTenant(_Row):
    name: str
    display_name: str | None = None
    description: str | None = None


class ProfileValue(_Row):
    value: str | int | float | bool | None = None
    count: int | float | None = None


class Profile(_Row):
    database: str
    table: str
    column: str
    basis: str
    distinct_estimate: int | float | None = None
    values: list[ProfileValue] | None = None
    top_values: list[ProfileValue] | None = None


class SemcatTable(_Row):
    tenant: str
    database: str
    table: str
    row_count: int | None = None
    n_columns: int | None = None
    description: str | None = None
    description_source: str | None = None
    provenance_class: str | None = None


class SemcatColumn(_Row):
    tenant: str
    database: str
    table: str
    column: str
    type: str | None = None


class AtlasRow(_Row):
    tenant: str
    agency: str = ""
    program: str = ""
    database: str
    table: str
    n_columns: int = 0
    column_names: str = ""
    has_more_columns: bool = False


class ListedTenant(_Row):
    name: str
    display_name: str | None = None
    organization: str | None = None
    website: str | None = None


def personal(name: str | None) -> bool:
    """Whether a tenant or database name is a personal namespace (``u`` or ``u_*``)."""
    return bool(name) and (name == "u" or name.startswith("u_") or name.split(".")[0] == "u")


def legacy_name(database: str) -> str:
    """The underscore name a dotted database was queried by before tenants."""
    return LEGACY_EXCEPTIONS.get(database, database.replace(".", "_", 1))


def redacted_column(column: str) -> bool:
    """Whether a column's name marks its values as personal or secret."""
    if column.lower() in PERSON_COLUMNS:
        return True
    parts = [p for p in re.split(r"[^a-z0-9]+", column.lower()) if p]
    pairs = {f"{a}_{b}" for a, b in zip(parts, parts[1:], strict=False)}
    return bool((set(parts) | pairs) & REDACT_TOKENS)


def redacted_table(table: str) -> bool:
    """Whether a table's name marks every column's values as personal."""
    return bool(set(table.lower().split("_")) & PERSON_TABLES)


def shaped(text: str, *, url: bool = True) -> bool:
    """Whether text holds an email-, ORCID- or (optionally) URL-shaped string."""
    return bool(EMAIL.search(text) or ORCID.search(text) or (url and URL.search(text)))


def known(text: str | None) -> str | None:
    """Stripped text, or None when it is empty or a placeholder such as "Unknown"."""
    text = (text or "").strip()
    return text if text and text.lower() != "unknown" else None


def clean_description(text: str | None) -> str | None:
    """A description cut to 400 characters, or None when unknown or holding an email or ORCID."""
    text = known(text)
    if text is None or shaped(text, url=False):
        return None
    return text[:MAX_DESCRIPTION]


def sha256(path: Path) -> str:
    """The SHA-256 hex digest of a file."""
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _lines(path: Path) -> Iterator[dict]:
    opener = gzip.open if path.suffix == ".gz" else open
    with opener(path, "rt", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def _text(path: Path) -> str:
    data = path.read_bytes()
    return (gzip.decompress(data) if path.suffix == ".gz" else data).decode("utf-8")


def _jsonl(rows: Iterable[dict]) -> bytes:
    return "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows).encode("utf-8")


def _json(data: object) -> bytes:
    return (json.dumps(data, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def _gzip(data: bytes) -> bytes:
    buf = io.BytesIO()
    # The default header embeds a timestamp and the file name, so the bytes would change per run.
    with gzip.GzipFile(filename="", fileobj=buf, mode="wb", mtime=0) as f:
        f.write(data)
    return buf.getvalue()


def catalog_row(
    database: str,
    table: str,
    rows: int | None,
    column_count: int,
    columns: list[list[str]],
    truncated: bool,
    source: str,
    description: str | None,
) -> dict:
    """One ``catalog.jsonl`` row, in the fixed key order."""
    return {
        "database": database,
        "legacy": legacy_name(database),
        "tenant": database.split(".")[0],
        "table": table,
        "rows": rows,
        "column_count": column_count,
        "columns": columns[:MAX_COLUMNS],
        "columns_truncated": truncated or len(columns) > MAX_COLUMNS,
        "source": source,
        "description": description,
    }


def read_packet(packet: Path) -> tuple[list[dict], dict[str, PacketTenant], list[dict]]:
    """Catalog rows, tenants and values lines from the hub packet.

    Parameters
    ----------
    packet : Path
        The packet folder.

    Returns
    -------
    tuple
        Catalog rows, tenants by name, and values lines for ``VALUE_TENANTS`` only.
    """
    rows = []
    for raw in _lines(packet / "tables.jsonl"):
        t = PacketTable.model_validate(raw)
        if personal(t.database):
            continue
        columns = [[c.name, c.type or ""] for c in t.columns]
        rows.append(
            catalog_row(
                t.database,
                t.table,
                t.row_count,
                len(columns),
                columns,
                False,
                SOURCES[0],
                clean_description(t.comment),
            )
        )
    tenants = {}
    for raw in _lines(packet / "tenants.jsonl"):
        tenant = PacketTenant.model_validate(raw)
        if not personal(tenant.name):
            tenants[tenant.name] = tenant
    keys = {(r["database"], r["table"]) for r in rows}
    values = []
    for raw in _lines(packet / "profiles.jsonl"):
        if raw.get("database", "").split(".")[0] not in VALUE_TENANTS:
            continue
        p = Profile.model_validate(raw)
        if (
            (p.database, p.table) not in keys
            or redacted_column(p.column)
            or redacted_table(p.table)
        ):
            continue
        line = values_line(p)
        if line is not None:
            values.append(line)
    return rows, tenants, values


def values_line(p: Profile) -> dict | None:
    """One ``values.jsonl.gz`` line from a profile, or None when no value survives."""
    complete = p.values is not None
    listed = p.values if p.values is not None else p.top_values or []
    listed = sorted(listed, key=lambda v: -(v.count or 0))
    kept: list[str] = []
    for item in listed:
        if item.value is None:
            continue
        value = item.value if isinstance(item.value, str) else json.dumps(item.value)
        if shaped(value):
            complete = False
            continue
        if len(value) > MAX_VALUE:
            # A cut value no longer lists the column's real values exhaustively.
            complete = False
        cut = value[:MAX_VALUE]
        if cut not in kept:
            kept.append(cut)
    if not kept:
        return None
    return {
        "database": p.database,
        "table": p.table,
        "column": p.column,
        "basis": p.basis,
        "complete": complete,
        "distinct": None if p.distinct_estimate is None else int(p.distinct_estimate),
        "values": kept,
    }


def verify_semcat(semcat: Path, names: Iterable[str]) -> dict[str, str]:
    """SHA-256 of each semcat file read, after checking it against ``SHA256SUMS``.

    Raises
    ------
    ValueError
        When a file is missing from ``SHA256SUMS`` or its digest differs.
    """
    listed = {}
    for line in (semcat / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        if line.strip():
            digest, name = line.split(maxsplit=1)
            listed[name.strip().lstrip("*")] = digest
    out = {}
    for name in names:
        actual = sha256(semcat / name)
        if listed.get(name) != actual:
            raise ValueError(f"semcat {name}: SHA-256 does not match SHA256SUMS")
        out[name] = actual
    return out


def read_semcat(semcat: Path) -> tuple[list[dict], set[tuple[str, str]]]:
    """Production catalog rows for ``SEMCAT_TENANTS``, and every listed (database, table).

    The second set holds tables at any ``provenance_class``, so the atlas never adds back
    a table semcat marks duplicate, staging, test or backup.
    """
    tables: list[SemcatTable] = []
    listed = set()
    for raw in _lines(semcat / "tables.jsonl"):
        t = SemcatTable.model_validate(raw)
        if t.tenant not in SEMCAT_TENANTS or personal(t.database):
            continue
        listed.add((f"{t.tenant}.{t.database}", t.table))
        if t.provenance_class == "production":
            tables.append(t)
    wanted = {(t.tenant, t.database, t.table) for t in tables}
    columns: dict[tuple[str, str, str], list[list[str]]] = defaultdict(list)
    for raw in _lines(semcat / "columns.jsonl.gz"):
        key = (raw.get("tenant"), raw.get("database"), raw.get("table"))
        if key in wanted:
            c = SemcatColumn.model_validate(raw)
            columns[(c.tenant, c.database, c.table)].append([c.column, c.type or ""])
    rows = []
    for t in tables:
        cols = columns.get((t.tenant, t.database, t.table), [])
        count = t.n_columns if t.n_columns is not None else len(cols)
        description = t.description if t.description_source == "producer" else None
        rows.append(
            catalog_row(
                f"{t.tenant}.{t.database}",
                t.table,
                t.row_count,
                count,
                cols,
                count > min(len(cols), MAX_COLUMNS),
                SOURCES[1],
                clean_description(description),
            )
        )
    return rows, listed


def read_atlas(atlas: Path) -> list[AtlasRow]:
    """Every non-personal row of the atlas table map."""
    with atlas.open(encoding="utf-8", newline="") as f:
        rows = [AtlasRow.model_validate(r) for r in csv.DictReader(f)]
    return [r for r in rows if not (personal(r.tenant) or personal(r.database))]


def atlas_rows(atlas: list[AtlasRow], semcat_listed: set[tuple[str, str]]) -> list[dict]:
    """Catalog rows for the atlas tables of ``ATLAS_TENANTS`` that semcat lacks."""
    rows = []
    for r in atlas:
        if r.tenant not in ATLAS_TENANTS:
            continue
        database = f"{r.tenant}.{r.database[len(r.tenant) + 1 :]}"
        if (database, r.table) in semcat_listed:
            continue
        names = [n for n in r.column_names.split("|") if n]
        rows.append(
            catalog_row(
                database,
                r.table,
                None,
                r.n_columns,
                [[n, ""] for n in names],
                r.has_more_columns,
                SOURCES[2],
                None,
            )
        )
    return rows


def first_source(sources: Iterable[str]) -> str:
    """The first of ``SOURCES`` among the given labels."""
    present = set(sources)
    return next(s for s in SOURCES if s in present)


def database_rows(catalog: list[dict], names: dict[str, tuple[str, str | None]]) -> list[dict]:
    """One ``databases.jsonl`` row per database that has a table in the catalog."""
    by_db: dict[str, list[dict]] = defaultdict(list)
    for r in catalog:
        by_db[r["database"]].append(r)
    out = []
    for database in sorted(by_db):
        tables = by_db[database]
        tenant = tables[0]["tenant"]
        counts = [t["rows"] for t in tables]
        name, description = names.get(tenant, (tenant, None))
        out.append(
            {
                "database": database,
                "legacy": legacy_name(database),
                "tenant": tenant,
                "tenant_name": name,
                "tenant_description": description,
                "tables": len(tables),
                "rows": None if any(c is None for c in counts) else sum(counts),
                "source": first_source(t["source"] for t in tables),
            }
        )
    return out


def tenant_names(
    packet_tenants: dict[str, PacketTenant], atlas: list[AtlasRow]
) -> dict[str, tuple[str, str | None]]:
    """Display name and description of every tenant the catalog may hold."""
    names: dict[str, tuple[str, str | None]] = {
        t.name: (known(t.display_name) or t.name, clean_description(t.description))
        for t in packet_tenants.values()
    }
    programs = sorted(
        {
            (r.tenant, known(r.program), known(r.agency))
            for r in atlas
            if r.tenant in SEMCAT_TENANTS
        },
        key=lambda p: (p[0], p[1] or "", p[2] or ""),
    )
    for tenant, program, agency in programs:
        if tenant not in names and program:
            described = f"{program} ({agency})" if agency else None
            names[tenant] = (program, clean_description(described))
    for tenant in SEMCAT_TENANTS:
        names.setdefault(tenant, (tenant, None))
    return names


def coverage(
    databases: list[dict], names: dict[str, tuple[str, str | None]], listing: Path | None
) -> dict:
    """The covered tenants, the listed tenants the catalog lacks, and the listing date."""
    sources: dict[str, list[str]] = defaultdict(list)
    for d in databases:
        sources[d["tenant"]].append(d["source"])
    covered = []
    for tenant in sorted(sources):
        source = first_source(sources[tenant])
        covered.append(
            {
                "name": tenant,
                "display_name": names.get(tenant, (tenant, None))[0],
                "source": source,
                "date": SOURCE_DATES[source],
            }
        )
    if listing is None:
        return {"covered": covered, "uncovered": [], "listing_date": None, "listing": "none"}
    manifest = listing.parent / "tenants_all.manifest.json"
    meta = json.loads(manifest.read_text(encoding="utf-8"))
    stamp = meta.get("snapshot_utc") if isinstance(meta, dict) else None
    if not (isinstance(stamp, str) and re.match(r"\d{4}-\d{2}-\d{2}", stamp)):
        raise ValueError(f"{manifest}: snapshot_utc is missing or does not start with a date")
    listed: dict[str, ListedTenant] = {}
    for raw in _lines(listing):
        t = ListedTenant.model_validate(raw)
        if not (personal(t.name) or t.name in sources):
            listed.setdefault(t.name, t)
    uncovered = [
        {
            "name": t.name,
            "display_name": known(t.display_name) or t.name,
            "organization": known(t.organization),
        }
        for _, t in sorted(listed.items())
    ]
    return {
        "covered": covered,
        "uncovered": uncovered,
        "listing_date": stamp[:10],
        "listing": "hub",
    }


def project_texts(project: Path) -> Iterator[tuple[Path, str]]:
    """REPORT.md, code files and notebook cell sources (never outputs) of one project."""
    report = project / "REPORT.md"
    if report.is_file():
        yield report, report.read_text(encoding="utf-8", errors="replace")
    for path in sorted(project.rglob("*")):
        if ".ipynb_checkpoints" in path.parts or not path.is_file():
            continue
        if path.suffix in (".py", ".sql"):
            yield path, path.read_text(encoding="utf-8", errors="replace")
        elif path.suffix == ".ipynb":
            try:
                notebook = json.loads(path.read_text(encoding="utf-8", errors="replace"))
            except json.JSONDecodeError:
                print(f"usage: skipped unreadable notebook {path}")
                continue
            cells = notebook.get("cells", []) if isinstance(notebook, dict) else []
            parts = []
            for cell in cells:
                source = cell.get("source", "") if isinstance(cell, dict) else ""
                parts.append("".join(source) if isinstance(source, list) else str(source))
            yield path, "\n".join(parts)


def usage(checkout: Path, catalog: list[dict]) -> dict[str, dict[str, list[str]]]:
    """Project id to the databases and tables its report and code name.

    A table counts only as ``<dotted>.<table>`` or ``<legacy>.<table>``; a bare table
    name never counts.
    """
    names: dict[str, str] = {}
    tables: dict[str, set[str]] = defaultdict(set)
    for r in catalog:
        names[r["database"]] = names[r["legacy"]] = r["database"]
        tables[r["database"]].add(r["table"])
    if not names:
        return {}
    alternation = "|".join(re.escape(n) for n in sorted(names, key=lambda n: (-len(n), n)))
    pattern = re.compile(rf"(?<![\w.])({alternation})(?!\w)(?:\.(\w+))?")
    out = {}
    for project in sorted(p for p in (checkout / "projects").glob("*") if p.is_dir()):
        dbs, tabs = set(), set()
        for _, text in project_texts(project):
            for m in pattern.finditer(text):
                database = names[m.group(1)]
                dbs.add(database)
                if m.group(2) in tables[database]:
                    tabs.add(f"{database}.{m.group(2)}")
        if dbs:
            out[project.name] = {"databases": sorted(dbs), "tables": sorted(tabs)}
    return out


def observatory_commit(checkout: Path) -> str | None:
    """The checkout's HEAD commit, or None when it is not a Git checkout."""
    try:
        done = subprocess.run(
            ["git", "-C", str(checkout), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=False,
        )
    except OSError:
        return None
    commit = done.stdout.strip()
    return commit if done.returncode == 0 and commit else None


def build(inputs: Inputs, root: Path) -> list[str]:
    """Build all six files, check them, and replace ``root / OUT`` only when they pass.

    Parameters
    ----------
    inputs : Inputs
        The snapshots and the observatory checkout to read.
    root : Path
        The repository root to write into.

    Returns
    -------
    list of str
        The check's messages on the new files; empty when they pass. When any is
        returned, the previous ``root / OUT`` is left as it was.

    Raises
    ------
    FileNotFoundError
        When the packet zip or an input file is missing.
    ValueError
        When a semcat file does not match ``SHA256SUMS``.
    """
    zip_path = inputs.packet.with_name(inputs.packet.name + ".zip")
    if not zip_path.is_file():
        raise FileNotFoundError(f"packet zip not found: {zip_path}")
    semcat_files = verify_semcat(inputs.semcat, ("tables.jsonl", "columns.jsonl.gz"))
    packet_rows, packet_tenants, values = read_packet(inputs.packet)
    semcat_rows, semcat_listed = read_semcat(inputs.semcat)
    atlas = read_atlas(inputs.atlas)
    merged: dict[tuple[str, str], dict] = {}
    for r in [*packet_rows, *semcat_rows, *atlas_rows(atlas, semcat_listed)]:
        merged.setdefault((r["database"], r["table"]), r)
    catalog = [merged[k] for k in sorted(merged)]
    values.sort(key=lambda v: (v["database"], v["table"], v["column"]))
    names = tenant_names(packet_tenants, atlas)
    databases = database_rows(catalog, names)
    cover = coverage(databases, names, inputs.tenants)
    used = usage(inputs.checkout, catalog)
    per_source = Counter(r["source"] for r in catalog)
    packet_meta = json.loads((inputs.packet / "manifest.json").read_text(encoding="utf-8"))
    manifest = {
        "snapshot_utc": packet_meta.get("snapshot_utc"),
        "packet_zip_sha256": sha256(zip_path),
        "semcat_commit": (inputs.semcat / "COMMIT").read_text(encoding="utf-8").strip(),
        "semcat_files": semcat_files,
        "atlas_sha256": sha256(inputs.atlas),
        "tenants_sha256": sha256(inputs.tenants) if inputs.tenants else None,
        "observatory_commit": observatory_commit(inputs.checkout),
        "counts": {
            "tables": len(catalog),
            "tables_by_source": {s: per_source.get(s, 0) for s in SOURCES},
            "databases": len(databases),
            "tenants_covered": len(cover["covered"]),
            "tenants_uncovered": len(cover["uncovered"]),
            "value_columns": len(values),
            "projects_with_usage": len(used),
        },
        "value_tenants": list(VALUE_TENANTS),
        "legacy_exceptions": LEGACY_EXCEPTIONS,
        "redaction": {
            "tokens": sorted(REDACT_TOKENS),
            "person_columns": sorted(PERSON_COLUMNS),
            "person_tables": sorted(PERSON_TABLES),
            "value_patterns": {"email": EMAIL.pattern, "orcid": ORCID.pattern, "url": URL.pattern},
        },
    }
    out = root / OUT
    catalog_bytes = _jsonl(catalog)
    old = out / "catalog.jsonl"
    changed = not old.is_file() or old.read_bytes() != catalog_bytes
    payloads = {
        "catalog.jsonl": catalog_bytes,
        "values.jsonl.gz": _gzip(_jsonl(values)),
        "databases.jsonl": _jsonl(databases),
        "usage.json": _json(used),
        "coverage.json": _json(cover),
        "manifest.json": _json(manifest),
    }
    messages = replace_checked(root, payloads, inputs.semcat)
    print("tables per source: " + ", ".join(f"{s} {per_source.get(s, 0)}" for s in SOURCES))
    print(f"covered tenants: {len(cover['covered'])}")
    atlas_dbs = {r.database for r in atlas}
    packet_dbs = {r["database"] for r in packet_rows}
    missing = sorted(d for d in packet_dbs if d.replace(".", "_", 1) not in atlas_dbs)
    print(f"packet databases whose naive legacy name is absent from the atlas ({len(missing)}):")
    for database in missing:
        print(f"  {database}")
    if messages:
        print(f"lakehouse: check failed, {OUT} left as it was")
    elif changed:
        print(COST_NOTE)
    return messages


def replace_checked(root: Path, payloads: dict[str, bytes], semcat: Path | None) -> list[str]:
    """Write ``payloads`` beside ``root / OUT``, check them, and swap them in only if they pass.

    Parameters
    ----------
    root : Path
        The repository root.
    payloads : dict of str to bytes
        The six output files by name.
    semcat : Path or None
        The semcat snapshot for the owner scan, as ``check`` takes it.

    Returns
    -------
    list of str
        The check's messages; when any is returned, ``root / OUT`` is unchanged.
    """
    out = root / OUT
    out.parent.mkdir(parents=True, exist_ok=True)
    staged = Path(tempfile.mkdtemp(prefix=f".{out.name}-new-", dir=out.parent))
    staged.chmod(0o755)  # mkdtemp makes it 0700, and the folder keeps that mode once swapped in
    retired = out.parent / f".{out.name}-old"
    try:
        for name, data in payloads.items():
            (staged / name).write_bytes(data)
        messages = check(root, semcat, folder=staged)
        if messages:
            return messages
        shutil.rmtree(retired, ignore_errors=True)
        if out.exists():
            out.rename(retired)
        try:
            staged.rename(out)
        except OSError:
            if retired.exists() and not out.exists():
                retired.rename(out)
            raise
        shutil.rmtree(retired, ignore_errors=True)
        return []
    finally:
        shutil.rmtree(staged, ignore_errors=True)


def _owner_pattern(semcat: Path) -> re.Pattern[str] | None:
    # owner is read only here, held in memory, and never written or printed.
    owners = set()
    for raw in _lines(semcat / "tables.jsonl"):
        owner = raw.get("owner")
        if isinstance(owner, str) and owner.strip():
            owners.add(owner.strip())
    if not owners:
        return None
    alternation = "|".join(re.escape(o) for o in sorted(owners, key=lambda o: (-len(o), o)))
    return re.compile(rf"(?<![A-Za-z0-9])(?:{alternation})(?![A-Za-z0-9])")


def check(root: Path, semcat: Path | None = None, folder: Path | None = None) -> list[str]:
    """Check the catalog files under ``root / OUT``, or under ``folder`` when given.

    Parameters
    ----------
    root : Path
        The repository root.
    semcat : Path, optional
        The semcat snapshot whose ``owner`` values must appear in no output. Without it,
        ``docs/drafts/semcat-<commit[:7]>/`` is used when present.
    folder : Path, optional
        A folder of the six files to check in place of ``root / OUT``.

    Returns
    -------
    list of str
        One message per failure; empty when every rule holds.
    """
    out = folder if folder is not None else root / OUT
    missing = [name for name in FILES if not (out / name).is_file()]
    if missing:
        return [f"{OUT / name}: missing" for name in missing]
    messages = []
    for name, cap in CAPS.items():
        size = (out / name).stat().st_size
        if size > cap:
            messages.append(f"{name}: {size} bytes exceeds the {cap}-byte cap")
    catalog = list(_lines(out / "catalog.jsonl"))
    keys = [(r["database"], r["table"]) for r in catalog]
    if keys != sorted(keys):
        messages.append("catalog.jsonl: not sorted by (database, table)")
    for key, n in Counter(keys).items():
        if n > 1:
            messages.append(f"catalog.jsonl: {key[0]}.{key[1]} appears {n} times")
    databases = list(_lines(out / "databases.jsonl"))
    # Names reach page links and titles unescaped, so they must stay plain identifiers.
    named_dbs = [("catalog.jsonl", d) for d, _ in keys] + [
        ("databases.jsonl", d["database"]) for d in databases
    ]
    for name, database in sorted(set(named_dbs)):
        if not DATABASE_NAME.fullmatch(database):
            messages.append(f"{name}: database name {database!r} is not a plain identifier")
    for database, table in keys:
        if not TABLE_NAME.fullmatch(table):
            messages.append(f"catalog.jsonl: {database} table {table!r} is not a plain identifier")
    known = set(keys)
    values = list(_lines(out / "values.jsonl.gz"))
    for v in values:
        where = f"{v['database']}.{v['table']}.{v['column']}"
        if v["database"].split(".")[0] not in VALUE_TENANTS:
            messages.append(f"values.jsonl.gz: {where} is outside the value allowlist")
        if (v["database"], v["table"]) not in known:
            messages.append(f"values.jsonl.gz: {where} is not in the catalog")
        if redacted_column(v["column"]):
            messages.append(f"values.jsonl.gz: {where} has a redacted column name")
        if redacted_table(v["table"]):
            messages.append(f"values.jsonl.gz: {where} is in a table whose name marks people")
        for value in v["values"]:
            for label, pattern in (("an email", EMAIL), ("an ORCID", ORCID), ("a URL", URL)):
                if pattern.search(str(value)):
                    messages.append(f"values.jsonl.gz: {where} keeps a value shaped like {label}")
    cover = json.loads((out / "coverage.json").read_text(encoding="utf-8"))
    used = json.loads((out / "usage.json").read_text(encoding="utf-8"))
    named = [
        *(("catalog.jsonl", r[k]) for r in catalog for k in ("database", "legacy", "tenant")),
        *(("values.jsonl.gz", v["database"]) for v in values),
        *(("databases.jsonl", d[k]) for d in databases for k in ("database", "legacy", "tenant")),
        *(("coverage.json", c["name"]) for part in ("covered", "uncovered") for c in cover[part]),
        *(("usage.json", n) for u in used.values() for n in u["databases"]),
    ]
    for name, value in sorted(set(named)):
        if personal(value):
            messages.append(f"{name}: personal namespace {value}")
    texts = {name: _text(out / name) for name in FILES}
    for name, text in texts.items():
        if PERSONAL_TEXT.search(text):
            messages.append(f"{name}: holds text shaped like a personal namespace")
    both = {c["name"] for c in cover["covered"]} & {u["name"] for u in cover["uncovered"]}
    for tenant in sorted(both):
        messages.append(f"coverage.json: {tenant} is in both covered and uncovered")
    described = [
        *((f"{r['database']}.{r['table']}", r["description"]) for r in catalog),
        *((d["database"], d["tenant_description"]) for d in databases),
    ]
    for where, text in described:
        if text and shaped(text, url=False):
            messages.append(f"{where}: description holds an email- or ORCID-shaped string")
    if semcat is None:
        manifest = json.loads(texts["manifest.json"])
        commit = str(manifest.get("semcat_commit") or "")
        local = root / "docs/drafts" / f"semcat-{commit[:7]}"
        semcat = local if commit and local.is_dir() else None
    if semcat is None or not (semcat / "tables.jsonl").is_file():
        print("semcat owner scan skipped: snapshot not present")
    else:
        pattern = _owner_pattern(semcat)
        for name, text in texts.items():
            if pattern and pattern.search(text):
                messages.append(f"{name}: holds a semcat owner value")
    return messages


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    """Build the catalog from the given snapshots, or ``--check`` the committed one."""
    parser = argparse.ArgumentParser(
        prog="python -m beril_wiki.stages.lakehouse",
        description="Build or check state/lakehouse/ from local lakehouse snapshots.",
    )
    parser.add_argument("--packet", type=Path, help="hub catalog packet folder")
    parser.add_argument("--semcat", type=Path, help="pinned semcat snapshot folder")
    parser.add_argument("--atlas", type=Path, help="May 2026 atlas table_topic_map.csv")
    parser.add_argument("--tenants", type=Path, help="optional hub tenant listing (JSON lines)")
    parser.add_argument("--check", action="store_true", help="check the committed catalog")
    args = parser.parse_args(argv)
    if args.check:
        if args.packet or args.atlas or args.tenants:
            parser.error("--check takes only --semcat")
        messages = check(root, args.semcat)
    else:
        if not (args.packet and args.semcat and args.atlas):
            parser.error("a build needs --packet, --semcat and --atlas (or use --check)")
        inputs = Inputs(
            packet=args.packet,
            semcat=args.semcat,
            atlas=args.atlas,
            tenants=args.tenants,
            checkout=CHECKOUT,
        )
        try:
            messages = build(inputs, root)
        except (OSError, ValueError) as exc:
            print(f"lakehouse: {exc}", file=sys.stderr)
            return 2
    for message in messages:
        print(message)
    if not messages:
        print("lakehouse catalog: check passed")
    return 1 if messages else 0


if __name__ == "__main__":
    sys.exit(main())
