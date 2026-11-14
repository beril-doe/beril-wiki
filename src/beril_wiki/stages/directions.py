#!/usr/bin/env python3
"""Research directions: the biological questions a topic's findings open.

For every topic in contract/cards.yaml, the model reads the topic's headline
findings with their literature labels and closest papers, the topic's conflicts,
and the proposals its pages already make, then proposes a handful of research
directions: a question, a falsifiable hypothesis, why it matters, the decisive
test and what would support or refute it. A direction that would repeat, correct
or tidy an existing analysis is rejected in code; those proposals are listed for
the reports' maintainers at publish instead (publish/cards/). The model also reads
a directory of the lakehouse catalog (state/lakehouse/) and the tables code matched
to the topic, and names the databases and tables each test reads. Code checks that
every direction rests on a finding or conflict of the topic, names only papers the
novelty stage retrieved and databases and tables the catalog holds, claims no data
is absent from the lakehouse, and states no result figure the evidence lacks. Each
direction becomes wiki/directions/<slug>.md. `--status` compares the saved replies
with today's packs and calls no model.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from beril_wiki import lakehouse, records
from beril_wiki.agentic.prose import PLATFORM, prune_failures, record_failure
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, file_hash, prompt
from beril_wiki.check import numbers_in, pmids_in, prose_only
from beril_wiki.lakehouse import Catalog, absence_claims
from beril_wiki.paths import ROOT
from beril_wiki.records import FINDINGS, slugify, title_of
from beril_wiki.stages import cards
from beril_wiki.wording import (
    IDENTIFIER,
    REPORT_TALK,
    asks_to_redo,
    is_reanalysis,
    statistical,
)

OUT = Path("wiki/directions")
STATE = Path("state/directions.json")
LABELS = Path("state/novelty.json")
MIN_DIRECTIONS, MAX_DIRECTIONS = 3, 8
TITLE_WORDS = 14
# The check allows a few words past the prompt's limit: a question needs more words
# than a label, and a draft one word over cost a full rewrite.
TITLE_CHECK_WORDS = 18
# Bump when render() changes: pages re-render from the saved reply at no cost.
RENDER = "direction-page@2"
Approach = Literal["lakehouse analysis", "experiment", "analysis then experiment"]
Readiness = Literal["data in the lakehouse", "needs compute", "needs new measurements", "unknown"]
# A direction with one of these readiness or approach values must name the tables it reads.
NEEDS_TABLES_READINESS = ("data in the lakehouse", "needs compute")
NEEDS_TABLES_APPROACH = ("lakehouse analysis", "analysis then experiment")
MATCHED_TABLES = 40


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
    databases: list[str] = Field(default_factory=list, max_length=8)
    tables: list[str] = Field(default_factory=list, max_length=12)
    readiness: Readiness
    readiness_basis: str = Field(min_length=5, max_length=400)
    findings: list[str] = Field(default_factory=list)
    conflicts: list[str] = Field(default_factory=list)
    papers: list[str] = Field(default_factory=list, max_length=6)
    prior_work: str = Field(default="", max_length=600)


class Reply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    directions: list[Direction]


PROMPT_TAG = "directions@4"
_LEGACY_PROMPT_TAG = "directions@4"
PROMPT = prompt(
    PROMPT_TAG,
    "Propose research directions for scientists choosing their next project in one topic of "
    "a microbial-biology research wiki built from AI-run analyses over the KBase Data "
    "Lakehouse. You get the topic's FINDINGS (headline results, each with a literature label "
    "from a PubMed comparison and its closest papers), its CONFLICTS (places where projects "
    "disagree), PROPOSALS the wiki's pages already make (raw ideas, many of them routine), "
    "PAPERS (the retrieved papers you may cite), DATABASES (a directory of the lakehouse "
    "catalog: each database it covers with its first table names) and TABLES (catalog "
    "tables matched to this topic, with their columns and sample values).\n"
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
    "analysis on lakehouse data, or the experiment, or both, naming the organisms, "
    "genes, conditions or datasets the findings name); outcomes (what result would support "
    "it and what would refute it); approach (lakehouse analysis, experiment, or analysis "
    "then experiment); databases (names from DATABASES the test reads, only those); tables "
    "(the tables the test reads, each written <database>.<table>, only those); readiness "
    "(data in the lakehouse, needs compute, needs new measurements, or unknown) and "
    "readiness_basis (one sentence on what it rests on). tables must name at least one "
    "table when readiness is data in the lakehouse or needs compute, or when approach is "
    "lakehouse analysis or analysis then experiment. A value or column missing from "
    "DATABASES or TABLES is unknown, not absent; a table marked columns_truncated, complete "
    "false or basis sample holds more than is shown. The catalog covers only some of the "
    "lakehouse: never claim the lakehouse lacks data; say the catalog did not show it. "
    "findings (ids from FINDINGS it "
    "builds on) and conflicts (slugs from CONFLICTS), at least one of the two; papers (up "
    "to 6 PMIDs from PAPERS that are its closest published work) and prior_work (one "
    "sentence on how it goes beyond them, naming them by PMID; empty if none apply). "
    "Use only result figures stated in FINDINGS or CONFLICTS, keep each finding's "
    "qualifications, and add no confidence label, ranking or claim about a person.\n"
    "A scientist outside the subfield reads every field. Write them in plain words: no "
    "test statistics (p-values, correlation coefficients, FDR or q-values, AUC, odds "
    "ratios, accuracy scores) and no statistical words such as 'significant' or 'nominal'; "
    "say what was seen in words. In prose name a dataset in plain words, never by a "
    "database or table name, and use no notebook, node or sample identifiers. Say what was "
    "found, not what 'the report' or 'the evidence' says. The title is a question ending in '?' "
    "and does not state the hypothesis as a fact.\n"
    "The decisive test must be able to fail in an informative way, and outcomes say what "
    "result would refute the hypothesis. A direction whose main step checks whether an "
    "existing result holds after a control, a correction or a replication is a "
    "re-analysis, not a new project. OTHER_TOPICS lists the directions other topics "
    "already propose: do not propose the same project again, and leave a project that "
    "builds on the same evidence to the topic that has it. "
    + PLATFORM
    + f"\nReturn only JSON matching {json.dumps(Reply.model_json_schema())}.\n",
)

# Exact rendered prompt for raw-key migration; shared wording and schemas may change.
_LEGACY_PROMPT = (
    "Propose research directions for scientists choosing their next project in one topic "
    "of a microbial-biology research wiki built from AI-run analyses over the KBase Data "
    "Lakehouse. You get the topic's FINDINGS (headline results, each with a literature "
    "label from a PubMed comparison and its closest papers), its CONFLICTS (places where "
    "projects disagree), PROPOSALS the wiki's pages already make (raw ideas, many of them "
    "routine), PAPERS (the retrieved papers you may cite), DATABASES (a directory of the "
    "lakehouse catalog: each database it covers with its first table names) and TABLES "
    "(catalog tables matched to this topic, with their columns and sample values).\n"
    "Propose 3 to 8 directions. A research direction is a biological question a scientist "
    "in this field would choose to spend months on because the answer would change what "
    "is believed: a mechanism, an ecological or evolutionary explanation, a prediction "
    "that could fail. It is never a repeat, correction, reconciliation, recount, audit or "
    "re-analysis of existing work, nor data plumbing (joining tables, standardizing "
    "names, documenting pipelines); those go to the reports' maintainers and are excluded "
    "here. Prefer directions that start from 'Candidate novel' or 'In tension' findings, "
    "from null results that rule out one explanation and leave another open, and from "
    "conflicts read as competing biological hypotheses rather than as numerical "
    "discrepancies. Do not restate a proposal unless you turn it into a question with a "
    "hypothesis. Directions may join findings from different reports.\n"
    "For each direction give: id (D1, D2, ... in order; when you revise, a direction "
    "keeps its id even if rewritten, a new direction takes the next unused id and a "
    "dropped id is never reused, so reviewers can name directions by id); title (at most "
    "14 words, no figures, phrased as the idea, not as a task); question; hypothesis "
    "(falsifiable, one or two sentences); why_it_matters (what would change in "
    "understanding or practice if it holds); test (the decisive analysis on lakehouse "
    "data, or the experiment, or both, naming the organisms, genes, conditions or "
    "datasets the findings name); outcomes (what result would support it and what would "
    "refute it); approach (lakehouse analysis, experiment, or analysis then experiment); "
    "databases (names from DATABASES the test reads, only those); tables (the tables the "
    "test reads, each written <database>.<table>, only those); readiness (data in the "
    "lakehouse, needs compute, needs new measurements, or unknown) and readiness_basis "
    "(one sentence on what it rests on). tables must name at least one table when "
    "readiness is data in the lakehouse or needs compute, or when approach is lakehouse "
    "analysis or analysis then experiment. A value or column missing from DATABASES or "
    "TABLES is unknown, not absent; a table marked columns_truncated, complete false or "
    "basis sample holds more than is shown. The catalog covers only some of the "
    "lakehouse: never claim the lakehouse lacks data; say the catalog did not show it. "
    "findings (ids from FINDINGS it builds on) and conflicts (slugs from CONFLICTS), at "
    "least one of the two; papers (up to 6 PMIDs from PAPERS that are its closest "
    "published work) and prior_work (one sentence on how it goes beyond them, naming them "
    "by PMID; empty if none apply). Use only result figures stated in FINDINGS or "
    "CONFLICTS, keep each finding's qualifications, and add no confidence label, ranking "
    "or claim about a person.\n"
    "A scientist outside the subfield reads every field. Write them in plain words: no "
    "test statistics (p-values, correlation coefficients, FDR or q-values, AUC, odds "
    "ratios, accuracy scores) and no statistical words such as 'significant' or "
    "'nominal'; say what was seen in words. In prose name a dataset in plain words, never "
    "by a database or table name, and use no notebook, node or sample identifiers. Say "
    "what was found, not what 'the report' or 'the evidence' says. The title is a "
    "question ending in '?' and does not state the hypothesis as a fact.\n"
    "The decisive test must be able to fail in an informative way, and outcomes say what "
    "result would refute the hypothesis. A direction whose main step checks whether an "
    "existing result holds after a control, a correction or a replication is a "
    "re-analysis, not a new project. OTHER_TOPICS lists the directions other topics "
    "already propose: do not propose the same project again, and leave a project that "
    "builds on the same evidence to the topic that has it. The data platform is the KBase "
    "Data Lakehouse; never write BERDL or BER Data Lakehouse (the project id "
    'berdl_data_atlas and its title "BERDL Data Atlas" are a project\'s names and stay).\n'
    'Return only JSON matching {"$defs": {"Direction": {"additionalProperties": false, '
    '"properties": {"id": {"pattern": "^D[1-9][0-9]?$", "title": "Id", "type": '
    '"string"}, "title": {"maxLength": 140, "minLength": 5, "title": "Title", '
    '"type": "string"}, "question": {"maxLength": 400, "minLength": 15, "title": '
    '"Question", "type": "string"}, "hypothesis": {"maxLength": 600, "minLength": '
    '15, "title": "Hypothesis", "type": "string"}, "why_it_matters": {"maxLength": '
    '600, "minLength": 15, "title": "Why It Matters", "type": "string"}, "test": '
    '{"maxLength": 1000, "minLength": 20, "title": "Test", "type": "string"}, '
    '"outcomes": {"maxLength": 600, "minLength": 15, "title": "Outcomes", "type": '
    '"string"}, "approach": {"enum": ["lakehouse analysis", "experiment", "analysis '
    'then experiment"], "title": "Approach", "type": "string"}, "databases": '
    '{"items": {"type": "string"}, "maxItems": 8, "title": "Databases", "type": '
    '"array"}, "tables": {"items": {"type": "string"}, "maxItems": 12, "title": '
    '"Tables", "type": "array"}, "readiness": {"enum": ["data in the lakehouse", '
    '"needs compute", "needs new measurements", "unknown"], "title": "Readiness", '
    '"type": "string"}, "readiness_basis": {"maxLength": 400, "minLength": 5, '
    '"title": "Readiness Basis", "type": "string"}, "findings": {"items": '
    '{"type": "string"}, "title": "Findings", "type": "array"}, "conflicts": '
    '{"items": {"type": "string"}, "title": "Conflicts", "type": "array"}, '
    '"papers": {"items": {"type": "string"}, "maxItems": 6, "title": "Papers", '
    '"type": "array"}, "prior_work": {"default": "", "maxLength": 600, "title": '
    '"Prior Work", "type": "string"}}, "required": ["id", "title", "question", '
    '"hypothesis", "why_it_matters", "test", "outcomes", "approach", "readiness", '
    '"readiness_basis"], "title": "Direction", "type": "object"}}, '
    '"additionalProperties": false, "properties": {"directions": {"items": {"$ref": '
    '"#/$defs/Direction"}, "title": "Directions", "type": "array"}}, "required": '
    '["directions"], "title": "Reply", "type": "object"}.\n'
)


def first_paragraph(text: str) -> str:
    body = re.sub(r"^<!--.*?-->\n?", "", text)
    body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
    parts = [p.strip() for p in body.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    return parts[0] if parts else ""


def section(text: str, name: str, limit: int = 1800) -> str:
    m = re.search(rf"^## {name}\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
    return m.group(1).strip()[:limit] if m else ""


def topic_pack(root: Path, topic: str, reports: list[str], cat: Catalog) -> dict:
    """Build what the model reads for one topic, and what the checks hold its reply to.

    Parameters
    ----------
    root : Path
        The checkout.
    topic : str
        The topic slug.
    reports : list[str]
        The reports in scope, whose forward-looking bullets become PROPOSALS.
    cat : Catalog
        The lakehouse catalog. DATABASES is its directory; TABLES is its tables matched
        to the findings' and conflicts' text and their projects.

    Returns
    -------
    dict
        The sections the prompt carries, plus ``_findings`` and ``_conflicts`` for the
        checks.
    """
    groups = records.topic_groups(root)
    cites = records.concept_citations(root)
    labels_path = root / LABELS
    labels = cards.load_state(labels_path)
    findings, papers = {}, {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        if topic not in records.main_topics(fields.get("source", ""), groups, cites):
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
                "projects": records.projects_in(text),
            }
    topic_reports = [sid for sid in reports if topic in records.main_topics(sid, groups, cites)]
    proposals = [
        b["text"]
        for b in records.forward_bullets(root, topic, topic_reports)
        if not is_reanalysis(b["text"])
    ]
    text = " ".join(
        [f"{f['title']} {f['claim']}" for f in findings.values()]
        + [f"{c['title']} {c['lead']}" for c in conflicts.values()]
    )
    projects = sorted(
        {f["report"] for f in findings.values()}
        | {p for c in conflicts.values() for p in c["projects"]}
    )
    return {
        "FINDINGS": list(findings.values()),
        "CONFLICTS": [
            {k: c[k] for k in ("slug", "title", "lead", "sides")} for c in conflicts.values()
        ],
        "PROPOSALS": proposals,
        "PAPERS": [{"pmid": k, "title": v} for k, v in sorted(papers.items())],
        "DATABASES": cat.directory(),
        "TABLES": cat.matched(text, projects, MATCHED_TABLES),
        "_findings": findings,
        "_conflicts": conflicts,
    }


def is_database(cat: Catalog, name: str) -> bool:
    """Whether ``name`` is a database of the catalog (a table name is not)."""
    row = cat.exists(name)
    return row is not None and "table" not in row


def is_table(cat: Catalog, name: str) -> bool:
    """Whether ``name`` is a table of the catalog (a database name is not)."""
    row = cat.exists(name)
    return row is not None and "table" in row


def text_of(d: Direction) -> str:
    return " ".join(
        (d.title, d.question, d.hypothesis, d.why_it_matters, d.test, d.outcomes, d.readiness_basis)
    )


# Shared share of cited findings and conflicts at which two directions are one project.
SAME_EVIDENCE, SAME_EVIDENCE_MIN = 0.6, 3


def builds_on(d: Direction | dict) -> set[str]:
    get = d.get if isinstance(d, dict) else lambda k, _=None: getattr(d, k)
    return set(get("findings", []) or []) | set(get("conflicts", []) or [])


def same_project(a: set[str], b: set[str]) -> bool:
    shared = len(a & b)
    return shared >= SAME_EVIDENCE_MIN and shared / len(a | b) >= SAME_EVIDENCE


def new_result_figures(text: str, pool: str) -> list[str]:
    """Result-like figures (decimals, percentages, large counts) the evidence never states.
    A plan's small counts ("the top 20 candidates") are proposals, not results."""
    have = numbers_in(prose_only(pool))
    return sorted(n for n in numbers_in(prose_only(text)) if n not in have)


def checker(pack: dict, cat: Catalog, counted: bool = True) -> Callable[[str], Reply]:
    """Code checks on a reply. `counted=False` skips the 3-to-8 count, for a saved reply a
    salvage left shorter. Names are checked against the whole catalog, not TABLES: a table
    the match left out is still a real table."""
    findings, conflicts = pack["_findings"], pack["_conflicts"]
    papers = {p["pmid"] for p in pack["PAPERS"]}
    others = pack.get("OTHER_TOPICS", [])

    def parse(raw: str) -> Reply:
        reply = cards.parse_reply(raw, Reply)
        problems: list[str] = []
        if counted and not MIN_DIRECTIONS <= len(reply.directions) <= MAX_DIRECTIONS:
            problems.append(f"give {MIN_DIRECTIONS} to {MAX_DIRECTIONS} directions")
        ids = [d.id for d in reply.directions]
        if dup := sorted({i for i in ids if ids.count(i) > 1}):
            problems.append(f"direction ids {dup} are repeated")
        for i, d in enumerate(reply.directions):
            where = f"{d.id} ({d.title[:50]})"
            if asks_to_redo(d.title) or asks_to_redo(d.question):
                problems.append(f"{where}: repeats or corrects existing work; propose a question")
            if len(d.title.split()) > TITLE_CHECK_WORDS or numbers_in(d.title):
                problems.append(f"{where}: title over {TITLE_CHECK_WORDS} words or carries figures")
            if not d.title.rstrip().endswith("?"):
                problems.append(f"{where}: the title must be a question ending in '?'")
            prose = text_of(d)
            if statistical(prose):
                problems.append(
                    f"{where}: carries a test statistic or statistical wording; say it in words"
                )
            if found := sorted(set(IDENTIFIER.findall(prose))):
                problems.append(
                    f"{where}: names identifiers {found[:4]}; use the dataset's title "
                    "or plain words"
                )
            if REPORT_TALK.search(prose):
                problems.append(
                    f"{where}: says what 'the report' or 'the evidence' says; say what was found"
                )
            for other in others:
                if same_project(builds_on(d), builds_on(other)):
                    problems.append(
                        f"{where}: builds on the same evidence as '{other['title']}' in "
                        f"{other['topic']}; drop it or build on different findings"
                    )
            for e in reply.directions[:i]:
                if same_project(builds_on(d), builds_on(e)):
                    problems.append(
                        f"{where}: builds on the same evidence as {e.id}; merge them into one"
                    )
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
            if bad := [n for n in d.databases if not is_database(cat, n)]:
                problems.append(f"{where}: databases {bad} are not in the lakehouse catalog")
            if bad := [n for n in d.tables if not is_table(cat, n)]:
                problems.append(f"{where}: tables {bad} are not in the lakehouse catalog")
            if not d.tables and (
                d.readiness in NEEDS_TABLES_READINESS or d.approach in NEEDS_TABLES_APPROACH
            ):
                problems.append(
                    f"{where}: names no table; readiness '{d.readiness}' or approach "
                    f"'{d.approach}' needs the tables its test reads"
                )
            if hits := absence_claims(d.readiness_basis):
                problems.append(
                    f"{where}: readiness_basis says the lakehouse lacks data ({hits}); "
                    "say the catalog did not show it"
                )
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


def render(topic: str, d: Direction, pack: dict, cat: Catalog) -> tuple[str, dict, str]:
    """Return a direction's page name, frontmatter and body.

    Frontmatter carries the canonical dotted ``tables`` in reply order and ``databases``,
    the sorted union of the named databases and the tables' databases. The body names no
    table: publish writes the table list.
    """
    findings, conflicts = pack["_findings"], pack["_conflicts"]
    titles = {p["pmid"]: p["title"] for p in pack["PAPERS"]}
    name = f"{slugify(d.title)[:60].strip('-')}--{digest([d.question, d.hypothesis])[:6]}"
    tables = list(dict.fromkeys(n for t in d.tables if (n := cat.canonical(t))))
    databases = sorted(
        {n for b in d.databases if (n := cat.canonical(b))} | {t.rpartition(".")[0] for t in tables}
    )
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
        "databases": databases,
        "tables": tables,
        "findings": d.findings,
        "conflicts": d.conflicts,
        "papers": d.papers,
        "builds_on": [f"findings/{f}" for f in d.findings]
        + [f"conflicts/{c}" for c in d.conflicts],
        "projects": [p for p in projects if p not in records.DIGESTS],
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
        "",
        "## Builds on",
        "",
    ]
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


def accepted(reply: dict, pack: dict, cat: Catalog) -> bool:
    try:
        checker(pack, cat, counted=False)(json.dumps(reply))
    except CandidateError:
        return False
    return True


def pages_for(out: Path, topic: str) -> list[Path]:
    return [p for p in sorted(out.glob("*.md")) if topic in cards.read_page(p)[0].get("topics", [])]


def retire_broken(root: Path, out: Path, topic: str) -> None:
    """Delete a kept page that builds on a finding or conflict now gone, which the strict
    check would reject for the whole run."""
    for page in pages_for(out, topic):
        refs = cards.read_page(page)[0].get("builds_on", [])
        if any(not (root / "wiki" / f"{ref}.md").exists() for ref in refs):
            page.unlink()
            print(f"  directions/{topic}: retired {page.name}; it builds on removed work")


def topic_key(public: dict, policy: str) -> str:
    """Return a topic's cache key: its public pack, semantic prompt tag and model policy.

    Other topics' directions steer the draft but stay out of the key: in it, each topic's
    rewrite would make every other topic stale, and the topics would keep rewriting one
    another.
    """
    return digest([public, PROMPT_TAG, policy])


def matches_topic_input(
    root: Path, topic: str, reports: list[str], public: dict, policy: str, saved_input: str | None
) -> bool:
    """Match today's key or a raw legacy key under its original tag and current inputs."""
    if saved_input == topic_key(public, policy):
        return True
    if not saved_input or PROMPT_TAG != _LEGACY_PROMPT_TAG:
        return False
    legacy = public | {
        "PROPOSALS": [
            bullet["text"]
            for bullet in records.forward_bullets(root, topic, reports)
            if not is_reanalysis(bullet["text"])
        ]
    }
    return any(
        saved_input
        == digest([[{"role": "user", "content": _LEGACY_PROMPT + json.dumps(pack)}], policy])
        for pack in (public, legacy)
    )


def other_topics(state: dict, topic: str, topics: list[str]) -> list[dict]:
    """The directions the other topics in scope saved, which a topic must not repeat."""
    return [
        {"topic": t, "title": d["title"]}
        | {"findings": d.get("findings", []), "conflicts": d.get("conflicts", [])}
        for t, saved_other in sorted(state.items())
        if t != topic and t in topics
        for d in (saved_other.get("reply") or {}).get("directions", [])
    ]


def status(root: Path = ROOT) -> int:
    """Print how many topics' saved directions today's run would keep; call no model.

    A topic is skipped when it has no findings and no conflicts, failed when
    ``.agentic/failures.json`` lists it or its saved state is marked failed, current
    when its saved key matches today's inputs or their legacy proposal pack and today's
    checks accept its saved reply, and stale otherwise.

    Parameters
    ----------
    root : Path
        The checkout.

    Returns
    -------
    int
        1 when any topic is stale or failed, else 0.
    """
    from beril_wiki.stages import classify

    cat = lakehouse.load(root)
    scope = records.load_scope(root)
    topics, reports = (scope.topics, scope.reports) if scope else ([], [])
    state = cards.load_state(root / STATE)
    failures = cards.load_state(root / ".agentic/failures.json")
    policy = cards.policy(classify.status_config(root), ("cards", "card_review"))
    current = stale = failed = skipped = 0
    for topic in topics:
        pack = topic_pack(root, topic, reports, cat)
        public = {k: v for k, v in pack.items() if not k.startswith("_")}
        pack["OTHER_TOPICS"] = other_topics(state, topic, topics)
        saved = state.get(topic, {})
        if not pack["FINDINGS"] and not pack["CONFLICTS"]:
            skipped += 1
        elif f"directions/{topic}" in failures or saved.get("failed"):
            failed += 1
        elif (
            matches_topic_input(root, topic, reports, public, policy, saved.get("input"))
            and saved.get("reply")
            and accepted(saved["reply"], pack, cat)
        ):
            current += 1
        else:
            stale += 1
    print(
        f"directions: {current} current, {stale} stale, {failed} failed, {skipped} skipped, "
        f"{len(topics)} total"
    )
    return 1 if stale or failed else 0


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--status", action="store_true", help="count current topics; run nothing")
    args = parser.parse_args(argv or [])
    cat = lakehouse.load(root)
    if cat.empty:
        print(
            "stages.directions: no lakehouse catalog; run stages.lakehouse first", file=sys.stderr
        )
        return 1
    if args.status:
        return status(root)
    if not cards.require_runtime("directions"):
        return 0
    agent = cards.runtime()
    scope = records.load_scope(root)
    topics, reports = (scope.topics, scope.reports) if scope else ([], [])
    out = root / OUT
    out.mkdir(parents=True, exist_ok=True)
    state_path = root / STATE
    state = cards.load_state(state_path)
    policy = cards.policy(agent.config, ("cards", "card_review"))
    written = failed = 0
    for topic in topics:
        # A topic's failure lists only its own jobs: a retry of it rejects every job
        # listed, and must not re-buy the reviewed jobs of the topics before it.
        agent.jobs.clear()
        pack = topic_pack(root, topic, reports, cat)
        public = {k: v for k, v in pack.items() if not k.startswith("_")}
        key = topic_key(public, policy)
        pack["OTHER_TOPICS"] = other_topics(state, topic, topics)
        draft = PROMPT + json.dumps(public | {"OTHER_TOPICS": pack["OTHER_TOPICS"]})
        saved = state.get(topic, {})
        on_disk = {p.name: file_hash(p) for p in pages_for(out, topic)}
        # A saved reply stays while its input is unchanged and today's checks accept it,
        # so a code change re-asks only the topics whose replies its rules now reject.
        if (
            matches_topic_input(root, topic, reports, public, policy, saved.get("input"))
            and saved.get("reply")
            and not saved.get("failed")
            and accepted(saved["reply"], pack, cat)
        ):
            if saved.get("input") != key:
                saved = saved | {"input": key}
                state[topic] = saved
                atomic_json(state_path, state)
            if saved.get("render") == RENDER and saved.get("pages") == on_disk:
                continue
            reply = Reply.model_validate(saved["reply"])
        else:
            if not pack["FINDINGS"] and not pack["CONFLICTS"]:
                # Earlier directions would cite findings or conflicts that are gone.
                for page in pages_for(out, topic):
                    page.unlink()
                state.pop(topic, None)
                atomic_json(state_path, state)
                record_failure(f"directions/{topic}", None)
                print(f"  directions/{topic}: no findings or conflicts; no directions")
                continue
            if cards.leaves_failed(agent.config, saved.get("failed") is True, None):
                retire_broken(root, out, topic)
                continue
            parse = checker(pack, cat)
            try:
                reply = cards.reviewed(
                    [{"role": "user", "content": draft}],
                    f"directions/{topic}",
                    parse,
                    agent=agent,
                    salvage=salvager(parse),
                )
            except CandidateError as exc:
                failed += 1
                result = cards.failure(f"directions/{topic}", exc, agent)
                record_failure(f"directions/{topic}", result)
                print(f"  [FAILED] directions/{topic}: {result}")
                # Committed, unlike failures.json, so a run from a fresh job store sees it;
                # the last reply stays to steer other topics' drafts.
                state[topic] = saved | {"failed": True}
                atomic_json(state_path, state)
                # The last accepted pages stay, except one that builds on removed work.
                retire_broken(root, out, topic)
                continue
        names = set()
        for d in reply.directions:
            name, fields, body = render(topic, d, pack, cat)
            # Two topics can accept the same direction; each keeps its own page.
            if (taken := out / f"{name}.md").exists():
                owners = set(cards.read_page(taken)[0].get("topics", []))
                if topic not in owners and owners & set(topics):
                    name = f"{name}-{slugify(topic)[:24].strip('-')}"
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
    return cards.exit_code(failed)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
