"""What the lakehouse catalog adds at publish: question table lists, data pages, coverage.

A question page lists the catalog tables its direction and its followup name, each
checked against the committed catalog, with the catalog date, a hedge and a link to
the About page's coverage section. Each cited database without a curated page under
wiki/data/ gets a generated page. The About page's markers take the coverage numbers.
Every claim here is positive: a table the catalog does not show may still exist.
"""

from __future__ import annotations

import json
import re

from beril_wiki.lakehouse import Catalog
from beril_wiki.publish.cards.corpus import Corpus

SCHEMA_ONLY = {
    "atlas-2026-05": " · schema only, May 2026",
    "semcat-2026-11-04": " · schema only, semcat 2026-11-04",
}
COVERAGE_SOURCE = {
    "packet-2026-11-11": "hub catalog export",
    "semcat-2026-11-04": "semcat snapshot",
    "atlas-2026-05": "BERDL Data Atlas",
}
PAGE_COLUMNS = 30
MARKERS = ("<!-- lakehouse-coverage -->", "<!-- lakehouse-tenants -->", "<!-- lakehouse-date -->")
_SPECIAL = re.compile(r"([\\`*_\[\]<>|#])")


def md_text(s: str) -> str:
    """Return catalog free text that Markdown and HTML render as the same characters.

    Parameters
    ----------
    s : str
        A description, display name or other text the catalog holds.

    Returns
    -------
    str
        ``s`` on one line, with a backslash before each backslash, backtick, ``*``,
        ``_``, ``[``, ``]``, ``<``, ``>``, ``|`` and ``#``.
    """
    # A newline could start a list item or heading inside the page.
    return _SPECIAL.sub(r"\\\1", " ".join(str(s).split()))


def code(s: str) -> str:
    """Return ``s`` as an inline code span that a backtick inside it cannot close."""
    run = max((len(m) for m in re.findall(r"`+", s)), default=0)
    fence = "`" * (run + 1)
    pad = " " if run else ""
    return f"{fence}{pad}{s}{pad}{fence}"


def row_count(row: dict) -> str:
    """Return a table's row count in reader words."""
    n = row.get("rows")
    return f"{n:,} rows" if isinstance(n, int) else "row count unknown"


def question_tables(fields: dict, entry: dict | None, cat: Catalog) -> list[dict]:
    """Return the catalog rows a question names: its direction's tables, then its followup's.

    Parameters
    ----------
    fields : dict
        The direction page's frontmatter.
    entry : dict or None
        The question's accepted followup entry.
    cat : Catalog
        The committed lakehouse catalog.

    Returns
    -------
    list[dict]
        Catalog table rows, each passing ``exists()`` as a table, without repeats.
    """
    out: dict[tuple[str, str], dict] = {}
    for name in [*(fields.get("tables") or []), *((entry or {}).get("tables") or [])]:
        row = cat.exists(str(name))
        if row is not None and "table" in row:
            out.setdefault((row["database"], row["table"]), row)
    return list(out.values())


def coverage_line(cat: Catalog) -> str:
    """Return the line that links a question page to the About page's coverage section."""
    return (
        f"The catalog covers {cat.tenants_covered()} tenants, and a table missing from it may "
        "still be in the lakehouse: [[about#lakehouse-coverage|what the catalog covers]]."
    )


def data_lines(rows: list[dict], cat: Catalog) -> list[str]:
    """Return a question page's table list, its hedge and the coverage link.

    Parameters
    ----------
    rows : list[dict]
        Catalog rows from ``question_tables``.
    cat : Catalog
        The committed lakehouse catalog.

    Returns
    -------
    list[str]
        One line per table, the hedge when any table is listed, then the coverage line.
    """
    lines = [
        f"- [[{cat.route(r['database'])}|{cat.title(r['database'])}]] · {code(r['table'])} · "
        f"{row_count(r)}{SCHEMA_ONLY.get(r.get('source', ''), '')}"
        for r in rows
    ]
    if lines:
        lines += [
            "",
            f"An AI model matched this question to these tables in the lakehouse catalog of "
            f"{cat.snapshot()}. No one has run the analysis.",
        ]
    return [*lines, "", coverage_line(cat)] if lines else [coverage_line(cat)]


def cited(c: Corpus) -> dict[str, list[dict]]:
    """Return each database a question's prompt and ``cards.json`` name, with the rows its
    page lists from it (none for a database named without a table)."""
    from beril_wiki.publish.cards.pages import follow_fields  # pages imports this module

    out: dict[str, dict[str, dict]] = {}
    for did, (fields, _) in c.directions.items():
        follow = follow_fields(fields | {"_id": did}, c)
        for database in follow["databases"]:
            out.setdefault(database, {})
        for name in follow["tables"]:
            row = c.catalog.exists(name)
            if row is not None and "table" in row:
                out.setdefault(row["database"], {}).setdefault(row["table"], row)
    return {db: [tables[t] for t in sorted(tables)] for db, tables in sorted(out.items())}


def generated_routes(c: Corpus) -> set[str]:
    """Return the ``route()`` of each cited database that has no curated page."""
    return {c.catalog.route(db) for db in cited(c) if not c.catalog.curated(db)}


def data_page(database: str, rows: list[dict], c: Corpus, provenance: str) -> str:
    """Return a generated data page for one database.

    Parameters
    ----------
    database : str
        The dotted database name.
    rows : list[dict]
        The database's catalog table rows to list.
    c : Corpus
        The publish corpus, whose catalog supplies the tenant and date.
    provenance : str
        The provenance callout every published page carries.

    Returns
    -------
    str
        The page's Markdown with frontmatter.
    """
    cat = c.catalog
    meta = cat.exists(database) or {}
    tenant = md_text(meta.get("tenant_name") or meta.get("tenant") or database.split(".")[0])
    about = meta.get("tenant_description")
    source = meta.get("source") or (rows[0].get("source", "") if rows else "")
    source = COVERAGE_SOURCE.get(source, source)
    lines = [
        f'---\ntitle: {json.dumps(database)}\ntype: "Data collection"\n---',
        provenance,
        "",
        f"Tenant: {tenant}." + (f" {md_text(about)}" if about else ""),
        "",
        f"Listed in the lakehouse catalog of {cat.snapshot()} ({source}). A table missing "
        "from the catalog may still be in the lakehouse: "
        "[[about#lakehouse-coverage|what the catalog covers]].",
        "",
        "## Tables",
    ]
    for r in rows:
        # Upstream column names hold spaces and punctuation, so they render as escaped text.
        columns = [md_text(str(col[0])) for col in r.get("columns", [])[:PAGE_COLUMNS]]
        more = max(int(r.get("column_count") or 0), len(r.get("columns", []))) - len(columns)
        if more > 0 or (r.get("columns_truncated") and columns):
            columns.append(f"+{more} more" if more > 0 else "and more")
        lines += ["", f"### {code(r['table'])}", ""]
        lines.append(row_count(r).capitalize() + SCHEMA_ONLY.get(r.get("source", ""), "") + ".")
        if r.get("description"):
            lines += ["", md_text(r["description"])]
        if columns:
            lines += ["", "Columns: " + ", ".join(columns)]
    counts = [r.get("rows") for r in rows]
    total = (
        f"{sum(n for n in counts if isinstance(n, int)):,}"
        if counts and all(isinstance(n, int) for n in counts)
        else "unknown"
    )
    lines += ["", f"Total rows: {total}."]
    return "\n".join(lines) + "\n"


def coverage_section(cat: Catalog) -> str:
    """Return the About page's section on which tenants the catalog covers.

    Parameters
    ----------
    cat : Catalog
        The committed lakehouse catalog.

    Returns
    -------
    str
        A ``## Lakehouse coverage`` section: the covered tenants with source and date,
        then the uncovered tenants or a sentence saying others exist.
    """
    cov = cat.coverage()
    covered = cov.get("covered") or []
    uncovered = cov.get("uncovered") or []
    lines = [
        "## Lakehouse coverage",
        "",
        f"The lakehouse catalog of {cat.snapshot()} covers {len(covered)} tenants of the "
        "KBase Data Lakehouse:",
        "",
    ]
    for t in covered:
        source = COVERAGE_SOURCE.get(t.get("source", ""), t.get("source", ""))
        name = md_text(t.get("display_name") or t["name"])
        lines.append(f"- {name}: {source}, {t.get('date', '')}")
    lines.append("")
    if uncovered:
        lines += ["The lakehouse also holds these tenants, which the catalog does not cover:", ""]
        for t in uncovered:
            name = md_text(t.get("display_name") or t["name"])
            org = t.get("organization")
            lines.append(f"- {name} ({md_text(org)})" if org else f"- {name}")
        lines.append("")
    else:
        lines += ["The lakehouse holds other tenants this catalog does not cover.", ""]
    lines.append("A table missing from the catalog may still be in the lakehouse.")
    return "\n".join(lines)


def about_text(text: str, cat: Catalog) -> str:
    """Return the About page with its lakehouse markers filled.

    Parameters
    ----------
    text : str
        The About page's source.
    cat : Catalog
        The committed lakehouse catalog.

    Returns
    -------
    str
        The page with the coverage section, the covered-tenant count and the catalog date.

    Raises
    ------
    ValueError
        When a marker is missing, so a reworded page cannot drop the coverage note.
    """
    missing = [m for m in MARKERS if m not in text]
    if missing:
        raise ValueError(f"about.md lacks the marker(s) {', '.join(missing)}")
    coverage, tenants, date = MARKERS
    return (
        text.replace(coverage, coverage_section(cat))
        .replace(tenants, str(cat.tenants_covered()))
        .replace(date, cat.snapshot())
    )
