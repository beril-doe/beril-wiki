"""The collection index pages and the JSON export for agents."""

from __future__ import annotations

import json
import pathlib

from beril_wiki.publish.cards.corpus import ISSUES, Corpus, join
from beril_wiki.publish.cards.links import links_index, shared_index
from beril_wiki.publish.cards.pages import issues_page
from beril_wiki.publish.cards.picks import eligible, home_picks, pick_lists
from beril_wiki.publish.cards.text import COMPARE_ORDER, NOT_ASSESSED
from beril_wiki.records import title_of

INDEXES = {
    "findings": (
        "Results",
        "Results from the project reports, one per card.",
    ),
    "directions": (
        "Open questions",
        "Questions the project results leave open, by topic and by what answering them needs.",
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
            for k in ("collections", "findings", "conflicts", "papers", "projects", "topics")
        }
        for d, (fields, body) in c.directions.items()
    ]
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
    """Collection landing pages and the JSON export; returns the pages written."""
    n = 0
    for folder, pages in (("findings", c.findings), ("directions", c.directions)):
        if pages:
            title, blurb = INDEXES[folder]
            fields: dict = {"title": title}
            if folder == "findings":
                fields |= picture_data(c)
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
    (dst / "cards.json").write_text(json.dumps(export(c), indent=1), encoding="utf-8")
    return n
