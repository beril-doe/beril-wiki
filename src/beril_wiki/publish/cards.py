"""Publish-time joins for finding and research-direction records (preview builds only).

The curator stages write each record alone; this step places them. It adds the
literature label from state/novelty.json, the topics a finding belongs to, the
conflicts and research directions related to it, and two texts a reader copies from
each direction: a prompt for BERIL and a handoff brief. It also writes a JSON export
for agents. Everything here is a deterministic join over pages the pipeline wrote,
so placement never costs a model call and never edits pages under wiki/.

Reanalysis proposals, which repeat or correct existing work, are listed per report
under data-issues/ for the reports' maintainers rather than as research.

The public build leaves the records out until the full-corpus run is approved:
set WIKI_PREVIEW=1 to publish them. ingest.py calls record() on each record page
before its generic transforms (title, [src:] links, dead-link repair) run.
"""

from __future__ import annotations

import json
import os
import pathlib
import re

import yaml

PREVIEW_ENV = "WIKI_PREVIEW"
DIRS = ("findings", "directions")
ISSUES = "data-issues"
FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
NOT_ASSESSED = "Not assessed"
PUBMED = "https://pubmed.ncbi.nlm.nih.gov/{}/"
# The guarded labels name the agreement that let them stand.
GUARDED = ("Candidate novel", "In tension with retrieved work")


def preview() -> bool:
    return os.environ.get(PREVIEW_ENV) == "1"


def split(text: str) -> tuple[dict, str]:
    m = FM.match(text)
    return ((yaml.safe_load(m.group(1)) or {}), text[m.end() :]) if m else ({}, text)


def join(fields: dict, body: str) -> str:
    return "---\n" + "".join(f"{k}: {json.dumps(v)}\n" for k, v in fields.items()) + "---\n" + body


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def cited(text: str) -> set[str]:
    return {
        re.sub(r"__REPORT$", "", part.strip())
        for tag in SRC_TAG.finditer(text)
        for part in re.split(r"[,;]", tag.group(1))
        if part.strip()
    }


class Corpus:
    """What the joins read: topic membership, citations, labels and the records."""

    def __init__(self, kb: pathlib.Path):
        wiki = kb / "wiki"
        groups_path = kb / "state" / "curator-topics.json"
        groups = json.loads(groups_path.read_text())["groups"] if groups_path.exists() else []
        self.topic_concepts = {slugify(g["title"]): set(g["concepts"]) for g in groups}
        self.topic_titles = {slugify(g["title"]): g["title"] for g in groups}
        self.concept_titles = {
            f"concepts/{p.stem}": title_of(p.read_text(encoding="utf-8", errors="replace"), p.stem)
            for p in (wiki / "concepts").glob("*.md")
        }
        self.concept_cites = {
            p.stem: cited(p.read_text(encoding="utf-8", errors="replace"))
            for p in (wiki / "concepts").glob("*.md")
        }
        self.conflicts = {
            p.stem: (p.read_text(encoding="utf-8", errors="replace"))
            for p in sorted((wiki / "conflicts").glob("*.md"))
        }
        labels_path = kb / "state" / "novelty.json"
        self.labels = json.loads(labels_path.read_text()) if labels_path.exists() else {}
        self.findings = {
            p.stem: split(p.read_text(encoding="utf-8"))
            for p in sorted((wiki / "findings").glob("*.md"))
        }
        self.directions = {
            p.stem: split(p.read_text(encoding="utf-8"))
            for p in sorted((wiki / "directions").glob("*.md"))
        }
        self.issues = data_issues(kb)

    def topics_of(self, sid: str) -> list[str]:
        from beril_wiki.stages.cards import main_topics

        return main_topics(sid, self.topic_concepts, self.concept_cites)

    def related_conflicts(self, sid: str, topics: list[str]) -> list[str]:
        concepts = (
            set().union(*(self.topic_concepts.get(t, set()) for t in topics)) if topics else set()
        )
        return [
            stem
            for stem, text in self.conflicts.items()
            if stem.split("--")[1] in concepts and sid in cited(text)
        ]

    def directions_on(self, fid: str) -> list[str]:
        return [
            d
            for d, (f, _) in self.directions.items()
            if f"findings/{fid}" in (f.get("builds_on") or [])
        ]


def data_issues(kb: pathlib.Path) -> dict[str, list[dict]]:
    """Report id -> the in-scope proposals that would redo or correct its work."""
    # Imported here: stages.topics imports this module through publish.ingest.
    from beril_wiki.stages import cards

    scope = cards.load_scope(kb)
    if scope is None:
        return {}
    out: dict[str, list[dict]] = {}
    seen: set[tuple[str, str]] = set()
    for topic in scope.topics:
        for b in cards.forward_bullets(kb, topic, scope.reports):
            if not cards.is_reanalysis(b["text"]):
                continue
            for sid in b["projects"]:
                if sid in cards.DIGESTS or (sid, b["text"]) in seen:
                    continue
                seen.add((sid, b["text"]))
                out.setdefault(sid, []).append(b)
    return dict(sorted(out.items()))


def title_of(body: str, fallback: str) -> str:
    m = re.search(r"^# +(.+)$", body, re.M)
    return m.group(1).strip() if m else fallback


def literature_section(entry: dict | None) -> str:
    """The label with how it was reached: queries, papers, closest, difference."""
    if not entry or entry.get("label", NOT_ASSESSED) == NOT_ASSESSED:
        why = (entry or {}).get("override")
        return "## Literature check\n\n**Not assessed.** " + (
            f"A person withdrew the pipeline's label: {why}"
            if why
            else "The literature check has not run on this finding."
        )
    if not entry.get("retrieved_on"):
        # A label a person pinned on a finding the pipeline never reached.
        return (
            f"## Literature check\n\n**{entry['label']}.** A person set this label: "
            f"{entry.get('override', '')} The pipeline has not retrieved literature for this "
            "finding."
        )
    lines = [
        "## Literature check",
        "",
        f"**{entry['label']}.** A pipeline judgment against literature retrieved from PubMed on "
        f"{entry['retrieved_on']}, read from abstracts only. No person reviewed it.",
    ]
    if entry.get("difference"):
        lines += ["", entry["difference"]]
    lines += [""]
    queries = "; ".join(f"“{q}”" for q in entry.get("queries", []))
    lines.append(
        f"- Searched: {queries}, plus the papers the report cites; "
        f"{entry.get('retrieved', 0)} papers with abstracts were compared."
    )
    for paper in entry.get("closest", []):
        lines.append(
            f"- Closest: [PMID {paper['pmid']}]({PUBMED.format(paper['pmid'])}) "
            f"{paper.get('title', '')} ({paper['relation']})"
        )
    if entry["label"] in GUARDED and entry.get("agreed"):
        lines.append(f"- Confirmed independently by {entry.get('agree_model')}.")
    if entry.get("agreed") is False:
        lines.append(
            f"- {entry.get('judge_model')} proposed “{entry.get('judged_label')}”, which "
            f"{entry.get('agree_model')} did not confirm, so the weaker label shows."
        )
    if entry.get("override"):
        lines.append(f"- A person set this label: {entry['override']}")
    return "\n".join(lines)


def finding_page(fid: str, c: Corpus) -> str:
    fields, body = c.findings[fid]
    entry = c.labels.get(fid)
    sid = fields.get("source", "")
    topics = c.topics_of(sid)
    fields = fields | {
        "label": (entry or {}).get("label", NOT_ASSESSED),
        "label_date": (entry or {}).get("retrieved_on", ""),
        "topics": topics,
    }
    # The literature check sits under the claim, before the figures that support it.
    head, sep, rest = body.partition("\n## ")
    parts = [head.rstrip(), "", literature_section(entry)]
    if sep:
        parts += ["", "## " + rest.rstrip()]
    conflicts = c.related_conflicts(sid, topics)
    if conflicts:
        parts += ["", "## Related conflicts", ""]
        parts += [f"- [[conflicts/{s}|{title_of(c.conflicts[s], s)}]]" for s in conflicts]
    directions = c.directions_on(fid)
    if directions:
        parts += ["", "## Research directions that build on this", ""]
        parts += [f"- [[directions/{d}|{title_of(c.directions[d][1], d)}]]" for d in directions]
    return join(fields, "\n".join(parts) + "\n")


def sections(body: str) -> dict[str, str]:
    return {
        k.strip(): v.strip()
        for k, v in re.findall(r"^## (.+?)\n+(.*?)(?=\n## |\Z)", body, re.M | re.S)
    }


def plain(text: str) -> str:
    """Markdown link syntax as reading text, for text a reader pastes elsewhere."""
    text = re.sub(r"\[\[[^\]|]+\|([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).rsplit("/", 1)[-1], text)
    return re.sub(r"\[(PMID \d+)\]\([^)]+\)", r"\1", text)


def grounding(fields: dict, c: Corpus) -> list[str]:
    lines = []
    for f in fields.get("findings") or []:
        if f in c.findings:
            meta = c.findings[f][0]
            lines.append(f"- Finding ({meta.get('source', '')}): {meta.get('description', '')}")
    for k in fields.get("conflicts") or []:
        if k in c.conflicts:
            lines.append(f"- Conflict: {title_of(c.conflicts[k], k)}")
    return lines


def beril_prompt(fields: dict, body: str, c: Corpus) -> str:
    """What a reader pastes into BERIL to start the project."""
    sec = sections(body)
    data = ", ".join(fields.get("collections") or []) or "none named"
    lines = [
        "I want to pursue this research direction with BERIL on the KBase Data Lakehouse.",
        "",
        f"Question: {fields.get('description', '')}",
        f"Hypothesis: {fields.get('hypothesis', '')}",
        f"Proposed test: {sec.get('How to test it', '')}",
        f"What would support or refute it: {sec.get('What would support or refute it', '')}",
        f"Collections: {data} (readiness: {fields.get('readiness', 'unknown')}; "
        f"{fields.get('readiness_basis', '')})",
        "",
        "It builds on these results from the BERIL wiki:",
        *grounding(fields, c),
        "",
        "Before running anything, check that the data the test needs is in the lakehouse, "
        "then propose an analysis plan and its first query.",
    ]
    return plain("\n".join(lines))


def brief(fields: dict, body: str, c: Corpus) -> str:
    """The Markdown a reader copies to hand a direction to a collaborator or a lab."""
    sec = sections(body)
    lines = [
        f"# {title_of(body, 'Research direction')}",
        "",
        f"**Question.** {fields.get('description', '')}",
        "",
        f"**Hypothesis.** {fields.get('hypothesis', '')}",
        "",
        f"**Why it matters.** {sec.get('Why it matters', '')}",
        "",
        f"**How to test it.** {sec.get('How to test it', '')}",
        "",
        f"**What would support or refute it.** {sec.get('What would support or refute it', '')}",
        "",
        f"**Approach and data.** {fields.get('approach', '')}; readiness: "
        f"{fields.get('readiness', 'unknown')}. {fields.get('readiness_basis', '')}",
        "",
        "**Builds on**",
        *grounding(fields, c),
    ]
    if sec.get("Closest published work"):
        lines += ["", "**Closest published work**", sec["Closest published work"]]
    lines += [
        "",
        "Source: the BERIL wiki, an AI-generated wiki compiled from AI-conducted research "
        "reports. No person reviewed this direction.",
    ]
    return plain("\n".join(lines))


def direction_page(did: str, c: Corpus) -> str:
    fields, body = c.directions[did]
    extra = {"beril_prompt": beril_prompt(fields, body, c), "brief": brief(fields, body, c)}
    return join(fields | extra, body.rstrip() + "\n")


def issues_page(sid: str, items: list[dict], provenance: str, titles: dict[str, str]) -> str:
    """One report's maintainer list: proposals that would redo or correct its work."""
    lines = [
        f'---\ntitle: {json.dumps(f"Data issues: {sid}")}\ntype: "Data issues"\n---',
        provenance,
        "",
        f"Proposals in the wiki that would repeat, correct or reconcile work in "
        f"[[summaries/{sid}|{sid}]]. They are for the report's maintainers, not research "
        "directions. Each names the page that proposes it.",
        "",
    ]
    for b in items:
        page = b["page"]
        if page.startswith("sources/"):
            where = f"[[summaries/{sid}|the report]] ({b['section']})"
        else:
            where = f"[[{page}|{titles.get(page, page.rsplit('/', 1)[-1])}]] ({b['section']})"
        text = SRC_TAG.sub(
            lambda m: "(" + ", ".join(x.strip() for x in m.group(1).split(",")) + ")", b["text"]
        )
        lines.append(f"- {text} From {where}.")
    return "\n".join(lines) + "\n"


INDEXES = {
    "findings": (
        "Findings",
        "Headline results from each project report, with the caveat that travels with each "
        "one and a literature label: a pipeline judgment of where the result sits against "
        "PubMed abstracts. Null results and corrections are findings too.",
    ),
    "directions": (
        "Research directions",
        "Biological questions the findings and conflicts open, each with a hypothesis, the "
        "decisive test, the data it needs and its closest published work. Sorted by "
        "readiness, then by how many findings and conflicts each builds on. There is no "
        "score. Proposals that would repeat or correct existing work are listed per report "
        "for maintainers under Data issues.",
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
                "closest": entry.get("closest", []),
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
    return {"findings": findings, "research_directions": directions, "data_issues": issues}


def record(rel: pathlib.Path, c: Corpus) -> str:
    """A record page's source text with its joins, before ingest's generic transforms."""
    return finding_page(rel.stem, c) if rel.parts[0] == "findings" else direction_page(rel.stem, c)


def write_extras(dst: pathlib.Path, c: Corpus, provenance: str) -> int:
    """Collection landing pages and the JSON export; returns the pages written."""
    n = 0
    for folder, pages in (("findings", c.findings), ("directions", c.directions)):
        if pages:
            title, blurb = INDEXES[folder]
            (dst / folder / "index.md").write_text(
                f"---\ntitle: {json.dumps(title)}\n---\n{provenance}\n\n{blurb}\n",
                encoding="utf-8",
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
