#!/usr/bin/env python3
"""Literature labels: where each headline finding sits against PubMed.

Per finding in wiki/findings: GPT proposes claim-specific PubMed queries; NCBI
eutils retrieves their abstracts plus the papers the report itself cites; Claude
assigns one label and states the difference from the closest papers; code checks
every PMID against the retrieved set. "Candidate novel" and "In tension" stand only
when a model of the other vendor assigns the same label; otherwise the finding
takes the weaker label. contract/novelty-decisions.yaml pins or withdraws labels.

An empty search never earns "Candidate novel": it is "Insufficient literature
evidence" without a model call. A label is re-judged when its finding changes, and
on any run more than REFRESH_DAYS after retrieval, because unchanged corpus text
does not mean unchanged literature. When retrieval fails the previous label and
date stay, and a finding never labelled shows "Not assessed".

Output: state/novelty.json, joined into finding pages at publish.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import urllib.parse
from collections.abc import Callable
from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from beril_wiki.agentic.prose import (
    PageFailure,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import (
    CandidateError,
    Runtime,
    WorkflowError,
    atomic_json,
    backend_for,
    digest,
    model_for,
    prompt,
)
from beril_wiki.check import pmids_in
from beril_wiki.paths import ROOT
from beril_wiki.stages import cards
from beril_wiki.stages import literature as L

STATE = Path("state/novelty.json")
FINDINGS = Path("wiki/findings")
ESTABLISHED = "Established in retrieved literature"
EXTENDS = "Extends retrieved work"
TENSION = "In tension with retrieved work"
NOVEL = "Candidate novel"
INSUFFICIENT = "Insufficient literature evidence"
NOT_ASSESSED = "Not assessed"
LABELS = (ESTABLISHED, EXTENDS, TENSION, NOVEL, INSUFFICIENT, NOT_ASSESSED)
# Shown only with the agreement of a model from the other vendor.
GUARDED = (NOVEL, TENSION)
REFRESH_DAYS = 90
# Bump to re-judge every label after a change to how labels are judged.
JUDGE_REVISION = "novelty@2"
MAX_QUERIES = 3
PER_QUERY = 10
MAX_CITED = 10
MAX_PAPERS = 30
FETCH_BATCH = 10
FETCH_CAP = 2_000_000
ABSTRACT_CHARS = 2500

Judged = Literal[
    "Established in retrieved literature",
    "Extends retrieved work",
    "In tension with retrieved work",
    "Candidate novel",
    "Insufficient literature evidence",
]
Relation = Literal["same result", "same relationship elsewhere", "opposite or null", "related"]
# The relation a closest paper must have for each label to hold.
NEEDS = {
    ESTABLISHED: "same result",
    EXTENDS: "same relationship elsewhere",
    TENSION: "opposite or null",
}


class Queries(BaseModel):
    model_config = ConfigDict(extra="forbid")
    queries: list[str] = Field(min_length=1, max_length=MAX_QUERIES)


class Closest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pmid: str
    relation: Relation


class Judgment(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: Judged
    difference: str = Field(max_length=700)
    closest: list[Closest] = Field(max_length=4)


class Agreement(BaseModel):
    model_config = ConfigDict(extra="forbid")
    label: Judged
    reason: str = Field(max_length=700)


class Decision(BaseModel):
    model_config = ConfigDict(extra="forbid")
    finding: str
    label: str | None = None
    withdraw: bool = False
    reason: str = Field(min_length=1)


class Decisions(BaseModel):
    model_config = ConfigDict(extra="forbid")
    decisions: list[Decision] = []


LABEL_RULES = (
    "Labels, each exclusive of the others. 'Established in retrieved literature': a "
    "retrieved paper reports the same result in a comparable setting. 'Extends retrieved "
    "work': a retrieved paper reports the same relationship or effect in some setting, and "
    "this finding carries it to a new organism, scale, condition or method. 'In tension with "
    "retrieved work': a retrieved paper reports the opposite direction, or a null, for the "
    "same relationship. 'Candidate novel': no retrieved paper reports this relationship or "
    "effect in any setting, yet papers on the same genes, organisms or methods were "
    "retrieved, so the search was on target. 'Insufficient literature evidence': nothing "
    "relevant was retrieved, or the abstracts do not settle the comparison. Relations of a "
    "closest paper: 'same result', 'same relationship elsewhere', 'opposite or null', "
    "'related' (same genes, organisms or methods, not the relationship). "
    "A count, share or inventory of the report's own data (how many genes fall in each "
    "class, how records are spread across organisms, how much of a dataset an analysis "
    "covered) is not a relationship or effect: no paper could report those exact numbers, "
    "so it is never 'Candidate novel'. Label it 'Insufficient literature evidence' unless a "
    "retrieved paper reports the same pattern, and say in the difference that it is a "
    "description of this corpus's data. "
)
QUERY_PROMPT = prompt(
    "novelty-queries@1",
    "Propose PubMed searches that would find published work reporting the same result as "
    "this FINDING from a microbial-biology research report, or the same relationship in "
    "another organism or setting. Give up to 3 plain keyword queries without field tags: "
    "one naming the organisms, genes or datasets with common synonyms and identifiers, one "
    "naming the relationship or effect in general terms, and one naming the method. "
    'Return only JSON {"queries": ["..."]}.\n',
)
JUDGE_PROMPT = prompt(
    "novelty-judge@2",
    "Compare the FINDING from a research report with the CANDIDATE PAPERS retrieved from "
    "PubMed (abstracts only, not full text) and assign one label. "
    + LABEL_RULES
    + "Name up to 4 closest papers by PMID, from the candidates only, each with its relation. "
    "State the difference in one or two sentences: what this finding adds to or contradicts "
    "in the closest paper, naming it by PMID; leave it empty only for 'Insufficient "
    "literature evidence'. Judge only from the abstracts given, never from memory of other "
    "papers, and add no confidence label. "
    f"Return only JSON matching {json.dumps(Judgment.model_json_schema())}.\n",
)
AGREE_PROMPT = prompt(
    "novelty-agree@2",
    "A first reviewer compared the FINDING with the CANDIDATE PAPERS and proposed the label "
    "in PROPOSED. Assign your own label independently from the same abstracts. "
    + LABEL_RULES
    + 'Return only JSON {"label": "<one label>", "reason": "<one sentence>"}.\n',
)


def today() -> datetime.date:
    return datetime.date.today()


def age(entry: dict) -> int:
    stamp = entry.get("retrieved_on")
    if not stamp:
        return REFRESH_DAYS + 1
    return (today() - datetime.date.fromisoformat(stamp)).days


def cited_pmids(report_text: str) -> list[str]:
    """PMIDs the report itself cites, in order: its own references are on target."""
    found = re.findall(r"PMID:?\s*(\d{5,9})|pubmed\.ncbi\.nlm\.nih\.gov/(\d{5,9})", report_text)
    out: list[str] = []
    for a, b in found:
        if (pid := a or b) not in out:
            out.append(pid)
    return out[:MAX_CITED]


def search_ids(query: str) -> list[str]:
    found = L.eutils("esearch", term=query, retmax=PER_QUERY, sort="relevance")
    result = found.get("esearchresult", {})
    # NCBI reports a failed search in the body of a successful response.
    if error := found.get("error") or result.get("ERROR"):
        raise WorkflowError(f"PubMed search failed: {error}")
    return list(result.get("idlist", []))


def fetch_abstracts(ids: list[str]) -> dict[str, str]:
    papers: dict[str, str] = {}
    # 30 full records with MeSH and references can pass the 2 MB cap in one response.
    batches = [ids[start : start + FETCH_BATCH] for start in range(0, len(ids), FETCH_BATCH)]
    while batches:
        batch = batches.pop(0)
        url = f"{L.EUTILS}/efetch.fcgi?" + urllib.parse.urlencode(
            {"db": "pubmed", "id": ",".join(batch), "retmode": "xml", "tool": "beril-wiki"}
        )
        raw = L.paced_get(url, FETCH_CAP + 1)
        if len(raw) > FETCH_CAP:
            # One record with thousands of authors or references can pass the cap alone.
            if len(batch) > 1:
                batches[:0] = [[i] for i in batch]
            else:
                print(f"    [WARN] PubMed record PMID {batch[0]} exceeds 2MB; left out")
            continue
        # An error document parses as zero articles; it must not read as an empty search.
        error = re.search(rb"<ERROR>(.*?)</ERROR>", raw, re.S)
        if error:
            raise WorkflowError(f"PubMed fetch failed: {error.group(1).decode(errors='replace')}")
        papers |= L.abstracts_from_xml(raw, set(batch))
    return papers


def retrieve(store: Path, queries: list[str], cited: list[str]) -> tuple[dict[str, str], str]:
    """Abstracts for the queries and the report's citations, with the date retrieved.

    Cached under the runtime store with that date and reused for REFRESH_DAYS."""
    cache = store / "papers" / f"novelty-{digest([queries, cited])[:32]}.json"
    if cache.exists():
        saved = json.loads(cache.read_text(encoding="utf-8"))
        if age(saved) <= REFRESH_DAYS:
            return saved["papers"], saved["retrieved_on"]
    # The report's own citations go first: searches fill only the room they leave.
    ids: list[str] = list(dict.fromkeys(cited[:MAX_CITED]))
    for query in queries[:MAX_QUERIES]:
        ids += [i for i in search_ids(query) if i not in ids]
    ids = ids[:MAX_PAPERS]
    if any(not re.fullmatch(r"\d+", i) for i in ids):
        raise WorkflowError("PubMed returned an invalid identifier")
    papers = fetch_abstracts(ids) if ids else {}
    stamp = today().isoformat()
    cache.parent.mkdir(parents=True, exist_ok=True)
    cache.write_text(json.dumps({"retrieved_on": stamp, "papers": papers}, indent=1))
    return papers, stamp


class RetrievalError(Exception):
    """PubMed could not supply this finding's papers; its previous label stays."""


def labels_due(root: Path) -> bool:
    """Whether a shown label is older than REFRESH_DAYS. The scheduler reads this,
    because no input file changes when literature only ages."""
    path = root / STATE
    if not path.exists():
        return False
    state = json.loads(path.read_text(encoding="utf-8"))
    # A failed refresh keeps its old date, so it stays due and is tried again.
    return any(e.get("retrieved_on") and age(e) > REFRESH_DAYS for e in state.values())


def weaker(agree_label: str | None) -> str:
    """The label a guarded judgment falls back to when it is not confirmed."""
    return EXTENDS if agree_label in (ESTABLISHED, EXTENDS) else INSUFFICIENT


def finding_text(fields: dict, body: str) -> dict:
    quote = re.search(r"^## Evidence\s*\n+> (.+?)(?: \[src: [^\]]+\])?$", body, re.M)
    return {
        "claim": fields.get("description", ""),
        "result": fields.get("result", ""),
        "quantities": fields.get("quantities", []),
        "caveat": fields.get("caveat", ""),
        "quote": quote.group(1) if quote else "",
        "report": fields.get("source", ""),
    }


def judgment_checker(papers: dict[str, str]) -> Callable[[str], Judgment]:
    def parse(raw: str) -> Judgment:
        judged = cards.parse_reply(raw, Judgment)
        assert isinstance(judged, Judgment)
        named = [c.pmid for c in judged.closest] + sorted(pmids_in(judged.difference))
        problems = [f"PMID {pmid} is not a candidate" for pmid in named if pmid not in papers]
        relations = {c.relation for c in judged.closest}
        if judged.label in NEEDS and NEEDS[judged.label] not in relations:
            problems.append(
                f"'{judged.label}' needs a closest paper with relation '{NEEDS[judged.label]}'"
            )
        if judged.label == NOVEL:
            if not judged.closest:
                problems.append("'Candidate novel' needs the on-target papers as closest")
            if relations & {"same result", "same relationship elsewhere"}:
                problems.append(
                    "'Candidate novel' contradicts a closest paper reporting the relationship"
                )
        if judged.label != INSUFFICIENT and not judged.difference.strip():
            problems.append("state the difference from the closest paper")
        if problems:
            raise CandidateError("; ".join(problems))
        return judged

    return parse


def judge(fid: str, finding: dict, cited: list[str], agent: Runtime) -> dict:
    """One finding's label entry; raises CandidateError or a network error on failure."""
    ask = {"role": "user"}
    config, store = agent.config, agent.store
    queries = cards.asked(
        [ask | {"content": QUERY_PROMPT + json.dumps({"FINDING": finding})}],
        f"novelty/{fid}/queries",
        lambda raw: cards.parse_reply(raw, Queries),
        attempts=2,
        agent=agent,
    ).queries
    try:
        papers, stamp = retrieve(store, queries, cited)
    except Exception as exc:  # any PubMed fault belongs to this finding, not the stage
        raise RetrievalError(f"{type(exc).__name__}: {exc}") from exc
    judge_model = model_for(config, f"novelty/{fid}/judge")
    agree_model = model_for(config, f"novelty/{fid}/agree")
    entry = {
        "queries": queries,
        "retrieved": len(papers),
        "candidates": sorted(papers),
        "retrieved_on": stamp,
        "abstracts_only": True,
        "judge_model": judge_model,
        "agree_model": None,
        "agreed": None,
        "difference": "",
        "closest": [],
    }
    if not papers:
        return entry | {"label": INSUFFICIENT}
    candidates = "\n\n".join(f"PMID {pid}: {text[:ABSTRACT_CHARS]}" for pid, text in papers.items())
    pack = json.dumps({"FINDING": finding}) + "\n\nCANDIDATE PAPERS:\n" + candidates
    judged = cards.asked(
        [ask | {"content": JUDGE_PROMPT + pack}],
        f"novelty/{fid}/judge",
        judgment_checker(papers),
        agent=agent,
    )
    label = judged.label
    if label in GUARDED:
        if backend_for(judge_model) == backend_for(agree_model):
            print(f"  novelty/{fid}: no other-vendor model to confirm '{label}'")
            label = INSUFFICIENT
        else:
            proposed = json.dumps({"PROPOSED": judged.model_dump()})
            other = cards.asked(
                [ask | {"content": AGREE_PROMPT + pack + "\n\n" + proposed}],
                f"novelty/{fid}/agree",
                lambda raw: cards.parse_reply(raw, Agreement),
                attempts=2,
                agent=agent,
            )
            entry |= {"agree_model": agree_model, "agreed": other.label == label}
            if other.label != label:
                label = weaker(other.label)
    titles = {pid: text.split("\n", 1)[0] for pid, text in papers.items()}
    return entry | {
        "label": label,
        "judged_label": judged.label,
        "difference": judged.difference.strip(),
        "closest": [c.model_dump() | {"title": titles[c.pmid]} for c in judged.closest],
    }


def load_decisions(root: Path) -> dict[str, Decision]:
    path = root / cards.DECISIONS
    if not path.exists():
        return {}
    try:
        parsed = Decisions.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    except (ValidationError, yaml.YAMLError) as exc:
        raise WorkflowError(f"invalid {cards.DECISIONS}: {exc}") from exc
    for d in parsed.decisions:
        if not d.withdraw and d.label not in LABELS:
            raise WorkflowError(f"{cards.DECISIONS}: unknown label {d.label!r} for {d.finding}")
    return {d.finding: d for d in parsed.decisions}


def apply_decision(entry: dict, decision: Decision | None) -> dict:
    """The shown label: a person's pin or withdrawal over the pipeline's judgment."""
    entry = {k: v for k, v in entry.items() if k != "override"}
    entry["label"] = entry.get("pipeline_label", entry.get("label", NOT_ASSESSED))
    if decision is not None:
        entry["override"] = decision.reason
        entry["label"] = NOT_ASSESSED if decision.withdraw else decision.label
    return entry


def main(root: Path = ROOT) -> int:
    if not cards.require_runtime("novelty"):
        return 0
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    decisions = load_decisions(root)
    findings = {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        findings[page.stem] = finding_text(fields, body)
    # A new judge, reviewer or query model re-judges every label; the old one stays
    # as the fallback if retrieval then fails.
    revision = digest([JUDGE_REVISION, cards.policy(cards.runtime().config)])
    for fid in decisions.keys() - findings.keys():
        print(f"  [WARN] {cards.DECISIONS}: no finding {fid}")
    reports: dict[str, list[str]] = {}

    todo = []
    for fid, finding in findings.items():
        key = digest([finding, revision])
        prev = state.get(fid, {})
        if prev.get("input") == key and not prev.get("failed") and age(prev) <= REFRESH_DAYS:
            continue
        sid = finding["report"]
        if sid not in reports:
            path = cards.source_path(root, sid)
            reports[sid] = cited_pmids(path.read_text(encoding="utf-8")) if path.exists() else []
        todo.append((fid, finding, key))

    def label(item: tuple) -> dict:
        fid, finding, _ = item
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        try:
            return cards.content_refusal_fails_item(
                f"novelty/{fid}", lambda: judge(fid, finding, reports[finding["report"]], mine)
            )
        except CandidateError as exc:
            raise cards.failure(f"novelty/{fid}", exc, mine) from exc
        except RetrievalError as exc:
            # PubMed or the network: keep what the finding showed before.
            note = WorkflowError(f"retrieval failed: {exc}")
            raise cards.failure(f"novelty/{fid}", note, mine) from exc

    done = failed = 0
    for (fid, _, key), result in parallel(todo, label, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"novelty/{fid}", result)
            print(f"  [FAILED] novelty/{fid}: {result}")
            kept = state.get(fid) or {"label": NOT_ASSESSED, "pipeline_label": NOT_ASSESSED}
            state[fid] = kept | {"failed": True}
            continue
        state[fid] = {**result, "pipeline_label": result["label"], "input": key}
        # Saved per label, so a run stopped by its budget keeps what it finished.
        atomic_json(state_path, dict(sorted(state.items())))
        record_failure(f"novelty/{fid}", None)
        done += 1
    for fid in list(state):
        if fid not in findings:
            state.pop(fid)
        else:
            state[fid] = apply_decision(state[fid], decisions.get(fid))
    atomic_json(state_path, dict(sorted(state.items())))
    prune_failures("novelty/", {f"novelty/{fid}" for fid in findings})
    counts: dict[str, int] = {}
    for entry in state.values():
        counts[entry["label"]] = counts.get(entry["label"], 0) + 1
    print(
        f"novelty: {done} labelled, {len(findings) - len(todo)} current, {failed} failed; {counts}"
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
