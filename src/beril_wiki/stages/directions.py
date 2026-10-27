#!/usr/bin/env python3
"""Research directions: the biological questions a topic's findings open.

For every topic in contract/cards.yaml, the model reads the topic's headline
findings with their literature labels and closest papers, the topic's conflicts,
and the proposals its pages already make, then proposes a handful of research
directions: a question, a falsifiable hypothesis, why it matters, the decisive
test and what would support or refute it. A direction that would repeat, correct
or tidy an existing analysis is rejected in code; those proposals are listed for
the reports' maintainers at publish instead (publish/cards.py). Code also checks
that every direction rests on a finding or conflict of the topic, names only
papers the novelty stage retrieved and collections under wiki/data/, and states
no result figure the evidence lacks. Each direction becomes wiki/directions/<slug>.md.
"""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from beril_wiki.agentic.prose import (
    PLATFORM,
    prune_failures,
    record_failure,
    strict_pages,
)
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, file_hash, prompt
from beril_wiki.check import numbers_in, pmids_in, prose_only
from beril_wiki.paths import ROOT
from beril_wiki.stages import cards
from beril_wiki.stages.topics import slugify

OUT = Path("wiki/directions")
STATE = Path("state/directions.json")
FINDINGS = Path("wiki/findings")
LABELS = Path("state/novelty.json")
MIN_DIRECTIONS, MAX_DIRECTIONS = 3, 8
TITLE_WORDS = 14
# Bump when render() changes: pages re-render from the saved reply at no cost.
RENDER = "direction-page@1"
READINESS = ("data in the lakehouse", "needs compute", "needs new measurements", "unknown")
Approach = Literal["lakehouse analysis", "experiment", "analysis then experiment"]
Readiness = Literal["data in the lakehouse", "needs compute", "needs new measurements", "unknown"]


class Direction(BaseModel):
    model_config = ConfigDict(extra="forbid")
    id: str = Field(pattern=r"^D[1-9][0-9]?$")
    title: str = Field(min_length=5, max_length=140)
    question: str = Field(min_length=15, max_length=400)
    hypothesis: str = Field(min_length=15, max_length=600)
    why_it_matters: str = Field(min_length=15, max_length=600)
    test: str = Field(min_length=20, max_length=1000)
    outcomes: str = Field(min_length=15, max_length=600)
    approach: Approach
    collections: list[str] = Field(default_factory=list, max_length=8)
    readiness: Readiness
    readiness_basis: str = Field(min_length=5, max_length=400)
    findings: list[str] = Field(default_factory=list)
    conflicts: list[str] = Field(default_factory=list)
    papers: list[str] = Field(default_factory=list, max_length=6)
    prior_work: str = Field(default="", max_length=600)


class Reply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    directions: list[Direction]


PROMPT = prompt(
    "directions@2",
    "Propose research directions for scientists choosing their next project in one topic of "
    "a microbial-biology research wiki built from AI-run analyses over the KBase Data "
    "Lakehouse. You get the topic's FINDINGS (headline results, each with a literature label "
    "from a PubMed comparison and its closest papers), its CONFLICTS (places where projects "
    "disagree), PROPOSALS the wiki's pages already make (raw ideas, many of them routine), "
    "PAPERS (the retrieved papers you may cite) and COLLECTIONS.\n"
    f"Propose {MIN_DIRECTIONS} to {MAX_DIRECTIONS} directions. A research direction is a "
    "biological question a scientist in this field would choose to spend months on because "
    "the answer would change what is believed: a mechanism, an ecological or evolutionary "
    "explanation, a prediction that could fail. It is never a repeat, correction, "
    "reconciliation, recount, audit or re-analysis of existing work, nor data plumbing "
    "(joining tables, standardizing names, documenting pipelines); those go to the reports' "
    "maintainers and are excluded here. Prefer directions that start from 'Candidate novel' "
    "or 'In tension' findings, from null results that rule out one explanation and leave "
    "another open, and from conflicts read as competing biological hypotheses rather than as "
    "numerical discrepancies. Do not restate a proposal unless you turn it into a question "
    "with a hypothesis. Directions may join findings from different reports.\n"
    "For each direction give: id (D1, D2, ... in order; when you revise, a direction keeps "
    "its id even if rewritten, a new direction takes the next unused id and a dropped id is "
    "never reused, so reviewers can name directions by id); title (at most 14 words, no "
    "figures, phrased as the idea, not as a task); question; hypothesis (falsifiable, one "
    "or two sentences); why_it_matters "
    "(what would change in understanding or practice if it holds); test (the decisive "
    "analysis on lakehouse collections, or the experiment, or both, naming the organisms, "
    "genes, conditions or datasets the findings name); outcomes (what result would support "
    "it and what would refute it); approach (lakehouse analysis, experiment, or analysis "
    "then experiment); collections (ids from COLLECTIONS the test reads, only those); "
    "readiness (data in the lakehouse, needs compute, needs new measurements, or unknown) "
    "and readiness_basis (one sentence on what it rests on); findings (ids from FINDINGS it "
    "builds on) and conflicts (slugs from CONFLICTS), at least one of the two; papers (up "
    "to 6 PMIDs from PAPERS that are its closest published work) and prior_work (one "
    "sentence on how it goes beyond them, naming them by PMID; empty if none apply). "
    "Use only result figures stated in FINDINGS or CONFLICTS, keep each finding's "
    "qualifications, and add no confidence label, ranking or claim about a person. "
    + PLATFORM
    + f"\nReturn only JSON matching {json.dumps(Reply.model_json_schema())}.\n",
)


def first_paragraph(text: str) -> str:
    body = re.sub(r"^<!--.*?-->\n?", "", text)
    body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    parts = [p.strip() for p in body.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    return parts[0] if parts else ""


def section(text: str, name: str, limit: int = 1800) -> str:
    m = re.search(rf"^## {name}\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
    return m.group(1).strip()[:limit] if m else ""


def title_of(text: str, fallback: str) -> str:
    m = re.search(r"^# +(.+)$", text, re.M)
    return m.group(1).strip() if m else fallback


def topic_pack(root: Path, topic: str, reports: list[str]) -> dict:
    """What the model reads for one topic, and what the checks hold its reply to."""
    groups = cards.topic_groups(root)
    cites = cards.concept_citations(root)
    labels_path = root / LABELS
    labels = json.loads(labels_path.read_text(encoding="utf-8")) if labels_path.exists() else {}
    findings, papers = {}, {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        if topic not in cards.main_topics(fields.get("source", ""), groups, cites):
            continue
        entry = labels.get(page.stem, {})
        findings[page.stem] = {
            "id": page.stem,
            "title": title_of(body, page.stem),
            "claim": fields.get("description", ""),
            "result": fields.get("result", ""),
            "report": fields.get("source", ""),
            "caveat": fields.get("caveat", ""),
            "label": entry.get("label", "Not assessed"),
            "difference": entry.get("difference", ""),
            "closest": [p["pmid"] for p in entry.get("closest", [])],
        }
        for p in entry.get("closest", []):
            papers[p["pmid"]] = p.get("title", "")
    concepts = groups.get(topic, set())
    conflicts = {}
    for page in sorted((root / "wiki/conflicts").glob("conflict--*.md")):
        if page.stem.split("--")[1] in concepts:
            text = page.read_text(encoding="utf-8")
            conflicts[page.stem] = {
                "slug": page.stem,
                "title": title_of(text, page.stem),
                "lead": first_paragraph(text),
                "sides": section(text, "Evidence Sides"),
                "projects": cards.projects_in(text),
            }
    proposals = [
        b["text"]
        for b in cards.forward_bullets(root, topic, reports)
        if not cards.is_reanalysis(b["text"])
    ]
    return {
        "FINDINGS": list(findings.values()),
        "CONFLICTS": [
            {k: c[k] for k in ("slug", "title", "lead", "sides")} for c in conflicts.values()
        ],
        "PROPOSALS": proposals,
        "PAPERS": [{"pmid": k, "title": v} for k, v in sorted(papers.items())],
        "COLLECTIONS": [{"id": k, "title": v} for k, v in cards.collections(root).items()],
        "_findings": findings,
        "_conflicts": conflicts,
    }


def text_of(d: Direction) -> str:
    return " ".join(
        (d.title, d.question, d.hypothesis, d.why_it_matters, d.test, d.outcomes, d.readiness_basis)
    )


def new_result_figures(text: str, pool: str) -> list[str]:
    """Result-like figures (decimals, percentages, large counts) the evidence never states.
    A plan's small counts ("the top 20 candidates") are proposals, not results."""
    have = numbers_in(prose_only(pool))
    return sorted(n for n in numbers_in(prose_only(text)) if n not in have)


def checker(pack: dict) -> Callable[[str], Reply]:
    findings, conflicts = pack["_findings"], pack["_conflicts"]
    papers = {p["pmid"] for p in pack["PAPERS"]}
    known = {c["id"] for c in pack["COLLECTIONS"]}

    def parse(raw: str) -> Reply:
        reply = cards.parse_reply(raw, Reply)
        problems: list[str] = []
        if not MIN_DIRECTIONS <= len(reply.directions) <= MAX_DIRECTIONS:
            problems.append(f"give {MIN_DIRECTIONS} to {MAX_DIRECTIONS} directions")
        ids = [d.id for d in reply.directions]
        if dup := sorted({i for i in ids if ids.count(i) > 1}):
            problems.append(f"direction ids {dup} are repeated")
        for d in reply.directions:
            where = f"{d.id} ({d.title[:50]})"
            if cards.is_reanalysis(d.title) or cards.is_reanalysis(d.question):
                problems.append(f"{where}: repeats or corrects existing work; propose a question")
            if len(d.title.split()) > TITLE_WORDS or numbers_in(d.title):
                problems.append(f"{where}: title over {TITLE_WORDS} words or carries figures")
            if not d.findings and not d.conflicts:
                problems.append(f"{where}: builds on no finding or conflict")
            if bad := sorted(set(d.findings) - findings.keys()):
                problems.append(f"{where}: unknown finding ids {bad}")
            if bad := sorted(set(d.conflicts) - conflicts.keys()):
                problems.append(f"{where}: unknown conflict slugs {bad}")
            if bad := sorted(
                (set(d.papers) | pmids_in(d.prior_work) | pmids_in(text_of(d))) - papers
            ):
                problems.append(f"{where}: PMIDs {bad} are not in PAPERS")
            if bad := [c for c in d.collections if cards.collection_id(c) not in known]:
                problems.append(f"{where}: collections {bad} are not in COLLECTIONS")
            pool = " ".join(
                [
                    findings[f]["claim"] + " " + findings[f]["caveat"]
                    for f in d.findings
                    if f in findings
                ]
                + [
                    conflicts[c]["lead"] + " " + conflicts[c]["sides"]
                    for c in d.conflicts
                    if c in conflicts
                ]
            )
            if bad := new_result_figures(text_of(d), pool):
                problems.append(
                    f"{where}: figures {bad} are not in the findings or conflicts it cites"
                )
        if problems:
            raise CandidateError("; ".join(problems))
        return reply

    return parse


def named_directions(reply: Reply, objection: str) -> set[str]:
    """Ids an objection names: an id, a title, or "direction N" counted from 0 or 1."""
    text = objection.lower()
    ids = {d.id for d in reply.directions}
    hits = {f"D{n}" for n in re.findall(r"\bd(\d+)\b", text)} & ids
    hits |= {d.id for d in reply.directions if d.title.lower() in text}
    for number in re.findall(r"\bdirection\s+(\d+)\b", text):
        k = int(number)
        hits |= {reply.directions[i].id for i in (k - 1, k) if 0 <= i < len(reply.directions)}
    return hits


def salvager(
    parse: Callable[[str], Reply],
) -> Callable[[Reply, list[tuple[str, Reply]]], tuple[Reply, list[str]] | None]:
    """Drop the directions an open objection names; fail if one names none.

    Each objection is read against the reply it was raised on. A direction keeps its id
    through repairs that rewrite it, so the named ids are dropped from the final reply;
    an id it no longer has was dropped by a repair already."""

    def rescue(reply: Reply, notes: list[tuple[str, Reply]]) -> tuple[Reply, list[str]] | None:
        named: set[str] = set()
        for objection, seen in notes:
            hits = named_directions(seen, objection)
            if not hits and cards.restates(objection):
                continue
            if not hits:
                return None
            named |= hits
        removed = [d.title for d in reply.directions if d.id in named]
        keep = [d for d in reply.directions if d.id not in named]
        if not keep:
            return None
        try:
            # The count bound is for drafts; a salvaged reply keeps what survived.
            kept = Reply(directions=keep)
            checked = parse(kept.model_dump_json()) if len(keep) >= MIN_DIRECTIONS else kept
        except CandidateError:
            return None
        return checked, sorted(removed)

    return rescue


def render(topic: str, d: Direction, pack: dict, known: dict[str, str]):
    findings, conflicts = pack["_findings"], pack["_conflicts"]
    titles = {p["pmid"]: p["title"] for p in pack["PAPERS"]}
    name = f"{slugify(d.title)[:60].strip('-')}--{digest([d.question, d.hypothesis])[:6]}"
    slugs = [cards.collection_id(c) for c in d.collections]
    projects = sorted(
        {findings[f]["report"] for f in d.findings if f in findings}
        | {p for c in d.conflicts if c in conflicts for p in conflicts[c]["projects"]}
    )
    fields = {
        "type": "Research direction",
        "description": d.question,
        "hypothesis": d.hypothesis,
        "approach": d.approach,
        "readiness": d.readiness,
        "readiness_basis": d.readiness_basis,
        "collections": slugs,
        "findings": d.findings,
        "conflicts": d.conflicts,
        "papers": d.papers,
        "builds_on": [f"findings/{f}" for f in d.findings]
        + [f"conflicts/{c}" for c in d.conflicts],
        "projects": [p for p in projects if p not in cards.DIGESTS],
        "topics": [topic],
    }
    lines = [
        f"# {d.title}",
        "",
        d.question,
        "",
        "## Hypothesis",
        "",
        d.hypothesis,
        "",
        "## Why it matters",
        "",
        d.why_it_matters,
        "",
        "## How to test it",
        "",
        d.test,
        "",
        "## What would support or refute it",
        "",
        d.outcomes,
        "",
        "## Data",
        "",
        f"Approach: {d.approach}. Readiness: {d.readiness}. {d.readiness_basis}",
    ]
    if slugs:
        lines += [""] + [f"- Collection: [[data/{s}|{known[s]}]]" for s in slugs]
    lines += ["", "## Builds on", ""]
    lines += [
        f"- Finding: [[findings/{f}|{findings[f]['title']}]] ({findings[f]['label']})"
        for f in d.findings
    ]
    lines += [f"- Conflict: [[conflicts/{c}|{conflicts[c]['title']}]]" for c in d.conflicts]
    if d.papers:
        lines += ["", "## Closest published work", ""]
        lines += [
            f"- [PMID {p}](https://pubmed.ncbi.nlm.nih.gov/{p}/) {titles.get(p, '')}"
            for p in d.papers
        ]
        if d.prior_work:
            lines += ["", d.prior_work]
    return name, fields, "\n".join(lines)


def pages_for(out: Path, topic: str) -> list[Path]:
    return [p for p in sorted(out.glob("*.md")) if topic in cards.read_page(p)[0].get("topics", [])]


def main(root: Path = ROOT) -> int:
    if not cards.require_runtime("directions"):
        return 0
    agent = cards.runtime()
    scope = cards.load_scope(root)
    topics, reports = (scope.topics, scope.reports) if scope else ([], [])
    out = root / OUT
    out.mkdir(parents=True, exist_ok=True)
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    known = cards.collections(root)
    written = failed = 0
    for topic in topics:
        pack = topic_pack(root, topic, reports)
        public = {k: v for k, v in pack.items() if not k.startswith("_")}
        messages = [{"role": "user", "content": PROMPT + json.dumps(public)}]
        key = digest([messages, cards.policy(agent.config, ("cards", "review"))])
        saved = state.get(topic, {})
        on_disk = {p.name: file_hash(p) for p in pages_for(out, topic)}
        if saved.get("input") == key and saved.get("reply"):
            if saved.get("render") == RENDER and saved.get("pages") == on_disk:
                continue
            reply = Reply.model_validate(saved["reply"])
        else:
            if not pack["FINDINGS"] and not pack["CONFLICTS"]:
                print(f"  directions/{topic}: no findings or conflicts yet; skipped")
                continue
            parse = checker(pack)
            try:
                reply = cards.reviewed(
                    messages, f"directions/{topic}", parse, agent=agent, salvage=salvager(parse)
                )
            except CandidateError as exc:
                failed += 1
                result = cards.failure(f"directions/{topic}", exc, agent)
                record_failure(f"directions/{topic}", result)
                print(f"  [FAILED] directions/{topic}: {result}")
                continue
        names = set()
        for d in reply.directions:
            name, fields, body = render(topic, d, pack, known)
            cards.write_page(out / f"{name}.md", fields, body)
            names.add(f"{name}.md")
        for stale in pages_for(out, topic):
            if stale.name not in names:
                stale.unlink()
        state[topic] = {
            "input": key,
            "render": RENDER,
            "reply": reply.model_dump(),
            "pages": {p.name: file_hash(p) for p in pages_for(out, topic)},
        }
        atomic_json(state_path, state)
        record_failure(f"directions/{topic}", None)
        written += 1
        print(f"  wrote {len(names)} direction(s) for {topic}")
    retired = 0
    for page in sorted(out.glob("*.md")):
        if not set(cards.read_page(page)[0].get("topics", [])) & set(topics):
            page.unlink()
            retired += 1
    for topic in [t for t in state if t not in topics]:
        state.pop(topic)
    atomic_json(state_path, state)
    prune_failures("directions/", {f"directions/{t}" for t in topics})
    print(f"directions: {written} topic(s) written, {failed} failed, {retired} page(s) retired")
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
