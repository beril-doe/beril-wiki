"""One-time import of the legacy evidence store into ``knowledge/``, with no model call.

The old runtime kept extracted findings in a gitignored ``.agentic/evidence/*.json`` and
its last plan's finding-to-concept routing in ``.agentic/last-plan.json``. This writes
them as Git text: one claims file per report, the hash each report had when it was
read, and a sidecar per page linking sections to the claims they rest on.

Section links are inferred here by rule and labelled with the rule that found them, so a
later reader can tell an inferred link from one an editor made:

    number   the paragraph cites the claim's report and repeats its figures
    overlap  the paragraph cites the claim's report and shares most of its words
    plan     the old plan routed the claim to this page; no paragraph matched
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

from beril_wiki.check import NUMBER, norm_num, paragraphs
from beril_wiki.kb import pages
from beril_wiki.kb.store import Store, block_of, blocks, checkout_lock, sha256

LINKED_KINDS = ("concepts", "entities", "conflicts", "summaries", "topics")
WORDS = re.compile(r"[a-z][a-z0-9-]{3,}")
STOP = frozenset(
    "that this with from were have been which their these those than into also only more most "
    "such each other between across within without report reports reported project analysis "
    "data results result using used based shows show found".split()
)
# Measured on the 126 concept pages against the old plan's own routing: sharing half
# the words linked 25,473 claim-page pairs of which 27% were routed there; these
# thresholds link 10,642 at 53%. Links stay advisory either way (see ``how``).
OVERLAP = 0.7
MIN_TERMS = 5
FIGURE_OVERLAP = 0.3
# One section per page: a figure repeated down a long page says little about where
# the claim is discussed.
PER_PAGE = 1


def figures(text: str) -> set[str]:
    return {norm_num(t) for t in NUMBER.findall(text)}


def words(text: str) -> set[str]:
    return set(WORDS.findall(text.lower())) - STOP


def pick_evidence(legacy: Path) -> tuple[dict, dict]:
    """The evidence file the last plan was made from, and that plan's routing."""
    plan_path = legacy / "last-plan.json"
    routing: dict[str, dict] = {}
    if plan_path.exists():
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        routing = {row["evidence"]: row for row in plan.get("coverage", [])}
    best, best_score = None, -1
    for path in sorted((legacy / "evidence").glob("*.json"), key=lambda p: p.stat().st_mtime):
        data = json.loads(path.read_text(encoding="utf-8"))
        ids = {f["id"] for f in data["findings"]}
        score = len(ids & set(routing)) if routing else len(ids)
        # Ties go to the newer file, which sorts later.
        if score >= best_score:
            best, best_score = data, score
    if best is None:
        raise SystemExit(f"no evidence files under {legacy / 'evidence'}")
    return best, routing


def import_claims(store: Store, evidence: dict) -> dict[str, list[dict]]:
    """Write claims and the source registry; return the claims by report."""
    by_source: dict[str, list[dict]] = defaultdict(list)
    for finding in evidence["findings"]:
        by_source[finding["source"]].append(finding)
    seen = {
        row["source"].removesuffix(".md").removesuffix("__REPORT"): row["sha256"]
        for row in evidence.get("coverage", [])
    }
    sources = store.sources()
    out: dict[str, list[dict]] = {}
    for source, findings in sorted(by_source.items()):
        text = store.source_text(source)
        claims = []
        for f in sorted(findings, key=lambda f: (f["start"], f["id"])):
            located = text[f["start"] : f["end"]] == f["quote"]
            heading, block = block_of(text, f["start"]) if located else ("", "")
            claims.append(
                {
                    "id": f["id"],
                    "kind": f["kind"],
                    "text": f["claim"],
                    "quote": f["quote"],
                    "start": f["start"],
                    "end": f["end"],
                    "heading": heading,
                    "block": block,
                    # A quote the current report no longer holds was read from an older
                    # revision; revise decides what becomes of it.
                    "status": "active" if located else "recheck",
                    "added": "import",
                }
            )
        store.write_claims(source, claims)
        out[source] = claims
        read = seen.get(source) or sha256(text)
        row = {"id": source, "sha256": read, "claims": len(claims), "ingested": "import"}
        # The block hashes are the baseline revise compares against, so they are only
        # recorded when the report on disk is the one the evidence was read from.
        if read == sha256(text):
            row["blocks"] = [h for _, _, h in blocks(text)]
        sources[source] = row
    store.write_sources(sources)
    return out


def match(claim: dict, paragraph_figures: set[str], paragraph_words: set[str]) -> str:
    """How a paragraph that cites the claim's report supports it, or ''."""
    own = figures(claim["text"])
    terms = words(claim["text"])
    share = len(terms & paragraph_words) / len(terms) if terms else 0.0
    if own and own <= paragraph_figures and share >= FIGURE_OVERLAP:
        return "number"
    if len(terms) >= MIN_TERMS and share >= OVERLAP:
        return "overlap"
    return ""


def link_page(text: str, candidates: dict[str, list[dict]]) -> dict[str, dict[str, str]]:
    """Anchor -> {claim id: rule} for one page, given candidate claims by report."""
    scored: dict[str, list[tuple[float, str, str]]] = defaultdict(list)
    for section in pages.parse(text).sections:
        for par in paragraphs(section.body) if section.body else []:
            cited = [s for s in pages.sources_in(par) if s in candidates]
            if not cited:
                continue
            par_figures, par_words = figures(par), words(par)
            for source in cited:
                for claim in candidates[source]:
                    how = match(claim, par_figures, par_words)
                    if not how:
                        continue
                    terms = words(claim["text"])
                    share = len(terms & par_words) / len(terms) if terms else 0.0
                    scored[claim["id"]].append(
                        (share + (1.0 if how == "number" else 0.0), section.anchor, how)
                    )
    links: dict[str, dict[str, str]] = defaultdict(dict)
    for claim_id, hits in scored.items():
        kept: list[str] = []
        for _, anchor, how in sorted(hits, reverse=True):
            if anchor not in kept:
                kept.append(anchor)
                links[anchor][claim_id] = how
            if len(kept) == PER_PAGE:
                break
    return links


def import_links(store: Store, claims: dict[str, list[dict]], routing: dict[str, dict]) -> dict:
    """Write a sidecar for every synthesis page; return counts by rule."""
    routed: dict[str, list[dict]] = defaultdict(list)
    by_id = {c["id"]: (source, c) for source, rows in claims.items() for c in rows}
    for claim_id, row in routing.items():
        if claim_id not in by_id:
            continue
        for path in row.get("concepts", []):
            routed[path.removesuffix(".md")].append(by_id[claim_id][1])
        if row.get("summary_only"):
            source = by_id[claim_id][0]
            for name in (f"summaries/{source}__REPORT", f"summaries/{source}"):
                if store.page_path(name).exists():
                    routed[name].append(by_id[claim_id][1])
    counts = {"number": 0, "overlap": 0, "plan": 0, "pages": 0}
    for page_id in store.page_ids():
        kind = page_id.split("/")[0]
        if kind not in LINKED_KINDS:
            continue
        text = store.page_path(page_id).read_text(encoding="utf-8", errors="replace")
        plan_claims = routed.get(page_id, [])
        if kind == "concepts" and plan_claims:
            # The plan already says which claims a concept page carries; matching
            # every claim of every cited report would only add weaker guesses.
            candidates: dict[str, list[dict]] = defaultdict(list)
            for claim in plan_claims:
                candidates[by_id[claim["id"]][0]].append(claim)
        else:
            candidates = {s: claims[s] for s in pages.sources_in(text) if s in claims}
        links = link_page(text, candidates)
        anchored = {claim_id for section in links.values() for claim_id in section}
        loose = {c["id"]: "plan" for c in plan_claims if c["id"] not in anchored}
        sidecar = {"sections": {a: {"claims": dict(sorted(c.items()))} for a, c in links.items()}}
        if loose:
            sidecar["claims"] = dict(sorted(loose.items()))
        store.write_sidecar(page_id, sidecar)
        counts["pages"] += bool(links or loose)
        counts["plan"] += len(loose)
        for section in links.values():
            for how in section.values():
                counts[how] += 1
    return counts


def run(root: Path, legacy: Path) -> dict:
    with checkout_lock(root):
        return _run(root, legacy)


def _run(root: Path, legacy: Path) -> dict:
    store = Store(root)
    if (store.dir / "sources.jsonl").exists():
        raise SystemExit(
            "knowledge/ already holds records; importing again would replace claims, links "
            "and review stamps accepted since. Remove knowledge/ first if that is intended."
        )
    evidence, routing = pick_evidence(legacy)
    claims = import_claims(store, evidence)
    counts = import_links(store, claims, routing)
    total = sum(len(rows) for rows in claims.values())
    return {"sources": len(claims), "claims": total, "links": counts}
