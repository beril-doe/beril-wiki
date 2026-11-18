"""The collection index pages and the JSON export for agents."""

from __future__ import annotations

import json
import pathlib

from beril_wiki.publish.cards.corpus import ISSUES, Corpus, eligible, join, result_type
from beril_wiki.publish.cards.data import cited, data_page
from beril_wiki.publish.cards.links import links_index, shared_index
from beril_wiki.publish.cards.pages import follow_fields, issues_page
from beril_wiki.publish.cards.picks import home_picks, pick_lists
from beril_wiki.publish.cards.text import (
    CHIP,
    COMPARE_NOTES,
    COMPARE_ORDER,
    FOLLOW_ORDER,
    FOLLOW_TEXT,
    NOT_ASSESSED,
    SOMETHING_NEW,
    follow_notes,
)
from beril_wiki.records import title_of

INDEXES = {
    "findings": (
        "Results",
        "Results from the project reports, by topic and by how new each one is.",
    ),
    "directions": (
        "Open questions",
        "Questions the project results leave open, by topic and by what following them up needs.",
    ),
}


def export(c: Corpus) -> dict:
    """The same records as JSON, for agents."""
    findings = []
    for fid, (fields, body) in c.findings.items():
        entry = c.labels.get(fid, {})
        findings.append(
            {
                "id": fid,
                "url": f"findings/{fid}",
                "title": title_of(body, fid),
                "claim": fields.get("description"),
                "result": fields.get("result"),
                "source": fields.get("source"),
                "quantities": fields.get("quantities", []),
                "caveat": fields.get("caveat"),
                "topics": c.topics_of(fields.get("source", "")),
                "label": entry.get("label", NOT_ASSESSED),
                "label_date": entry.get("retrieved_on"),
                # An unconfirmed judgment's papers argued for the label that was rejected.
                "closest": entry.get("closest", []) if entry.get("agreed") is not False else [],
                "gist": c.gists.get(fid, {}).get("gist", ""),
                "type": result_type(c, fid),
                "listed": eligible(c, fid),
            }
        )
    directions = [
        {"id": d, "url": f"directions/{d}", "title": title_of(body, d)}
        | {
            k: fields.get(k)
            for k in ("description", "hypothesis", "approach", "readiness", "readiness_basis")
        }
        | {
            k: fields.get(k, [])
            for k in (
                "findings",
                "conflicts",
                "papers",
                "projects",
                "topics",
            )
        }
        # The checked databases and tables come from here, not the direction's frontmatter.
        | follow_fields(fields | {"_id": d}, c)
        for d, (fields, body) in c.directions.items()
    ]
    for entry in directions:
        # Not checked yet makes no data claim, so the readiness note stays out.
        if entry["follow"] == "unchecked":
            entry["readiness_basis"] = None
    issues = {sid: [b["text"] for b in items] for sid, items in c.issues.items()}
    return {
        "findings": findings,
        "research_directions": directions,
        "data_issues": issues,
        "home": home_picks(c),
        "topic_picks": pick_lists(c)[1],
        "links": links_index(c),
        "shared": shared_index(c),
    }


def picture_data(c: Corpus) -> dict:
    """What the Results picture and the home cards read from the results index page."""
    links = links_index(c)
    named = {x[k] for x in links for k in ("pa", "pb")}
    return {
        "compare_order": COMPARE_ORDER,
        # The first two columns are the two kinds of new; the map heads them as a group.
        "something_new": [SOMETHING_NEW, CHIP["Candidate novel"], CHIP["Extends retrieved work"]],
        "compare_notes": {text: COMPARE_NOTES[text] for text in COMPARE_ORDER},
        "links": links,
        "shared": shared_index(c),
        "project_titles": {sid: c.report_title(sid) for sid in sorted(named)},
        "empty_topics": sorted(
            set(c.topic_titles)
            - {
                c.display_topic(c.findings[fid][0].get("source", ""))
                for fid in c.findings
                if eligible(c, fid)
            }
        ),
    }


def write_extras(dst: pathlib.Path, c: Corpus, provenance: str) -> int:
    """Collection landing pages, generated data pages and the JSON export; returns the
    pages written."""
    n = 0
    for folder, pages in (("findings", c.findings), ("directions", c.directions)):
        if pages:
            title, blurb = INDEXES[folder]
            fields: dict = {"title": title}
            if folder == "findings":
                fields |= picture_data(c)
            else:
                fields |= {
                    "follow_order": FOLLOW_ORDER,
                    "follow_text": FOLLOW_TEXT,
                    "follow_notes": follow_notes(c.catalog.tenants_covered(), c.catalog.snapshot()),
                }
            (dst / folder / "index.md").write_text(
                join(fields, f"{provenance}\n\n{blurb}\n"), encoding="utf-8"
            )
            n += 1
    if c.issues:
        (dst / ISSUES).mkdir(exist_ok=True)
        titles = {f"conflicts/{k}": title_of(v, k) for k, v in c.conflicts.items()}
        titles |= c.concept_titles
        for sid, items in c.issues.items():
            (dst / ISSUES / f"{sid}.md").write_text(
                issues_page(sid, items, provenance, titles), encoding="utf-8"
            )
        rows = "\n".join(
            f"- [[{ISSUES}/{sid}|{sid}]]: {len(items)} item(s)" for sid, items in c.issues.items()
        )
        (dst / ISSUES / "index.md").write_text(
            f'---\ntitle: "Data issues"\n---\n{provenance}\n\nProposals that would repeat, '
            "correct or reconcile existing analyses, grouped by the report they concern. They "
            f"are for the reports' maintainers, not research directions.\n\n{rows}\n",
            encoding="utf-8",
        )
        n += len(c.issues) + 1
    for database in cited(c):
        if c.catalog.curated(database):
            continue
        tables = [r for r in c.catalog.tables if r["database"] == database]
        page = dst / f"{c.catalog.route(database)}.md"
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(data_page(database, tables, c, provenance), encoding="utf-8")
        n += 1
    (dst / "cards.json").write_text(json.dumps(export(c), indent=1), encoding="utf-8")
    return n
