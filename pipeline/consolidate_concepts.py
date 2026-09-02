#!/usr/bin/env python3
"""Concept-consolidation stage: turn single-source concept shards into synthesis.

Runs after enrich on every pipeline invocation. Enrichment creates concepts one
document at a time and hardcodes a one-element `sources` list; compile only
merges a document into pages when THAT document changes. So a concept created
from document #60 is never revisited against documents #1-59, and 136 of 153
concepts cite exactly one project. This stage closes that loop in two phases,
both driven by embeddings from CBORG's LBL-hosted nomic-embed-text (free), which
replaces wiki_check's name-token duplicate heuristic for candidate generation:

  1. merge  — near-duplicate concept pages (cosine >= --merge-threshold) get one
              LLM merge/keep judgement; a merge is one merge-rewrite of the
              survivor through compile.generate_page, the loser deleted and its
              inbound wikilinks rewritten in code.
  2. back-merge — thin concepts (fewer than --min-sources cited projects) are
              offered their top-k most similar summaries through compile's
              existing CONCEPT_UPDATE_USER merge-rewrite.

The success metric is distinct [src:] ids in the page BODY, never the length of
the `sources` frontmatter list. The previous-generation corpus looked
multi-source but padded frontmatter with bare "See also" links on 60 of 81
pages; back-merge therefore has an explicit "return UNCHANGED" path and a
deterministic gate that discards any rewrite which does not add a real citation.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python pipeline/consolidate_concepts.py [--dry-run] [--root DIR]

--dry-run costs $0: it embeds, ranks and prints both candidate lists, and makes
no LLM calls and no writes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import pathlib
import re
import sys

import litellm

import compile as C
from wiki_check import cited_ids, paragraphs, source_ids

# LBL-hosted and free on the CBORG gateway ("Nomic Embed Text (Free)", 8192-token
# context), so embeddings are never cached: 228 pages re-embed in ~5s for $0 and
# state/ does not gain a multi-megabyte vector blob.
EMBED_MODEL = os.environ.get("EMBED_MODEL", "openai/lbl/nomic-embed-text")
EMBED_BATCH = 100
EMBED_CHARS = 6000
UNCHANGED = "UNCHANGED"
# Bump when a prompt below changes, so cached negative verdicts are re-asked
# instead of silently outliving the prompt that produced them.
PROMPT_V = "v2-evidence-overlap"
REPORT_THRESHOLDS = (0.75, 0.78, 0.80, 0.82, 0.85, 0.87, 0.90)


MERGE_JUDGE_USER = """\
Two concept pages from the wiki may be near-duplicates of the same phenomenon.

Page A — concepts/{a}, cites project(s): {ids_a}
{body_a}

Page B — concepts/{b}, cites project(s): {ids_b}
{body_b}

Projects cited by BOTH pages: {shared}

Decide whether these are the SAME phenomenon written up twice, or two genuinely
distinct concepts that happen to share vocabulary.

The decisive question is what EVIDENCE each page rests on, not how each page is
framed:
- If both pages draw on the SAME project(s) and restate the same measurements,
  they are one concept that the enrichment stage split in two — MERGE them, even
  when their framings differ. A phenomenon and its proposed explanation, a
  result and its caveat, or a finding and the mechanism hypothesised for it are
  ONE page with sections, not two concept pages. This is the specific defect
  this stage exists to repair, and it is the common case here.
- If the two pages rest on DIFFERENT evidence and each would still stand with
  the other deleted, they are distinct concepts — do NOT merge. A shared subject
  area, shared vocabulary, or shared method is not a duplicate.

If they should merge, name the survivor: prefer the page whose title states the
more general phenomenon, and prefer the page citing more projects when the two
titles are equally general.

Return ONLY valid JSON, no fences:
{{"merge": true, "survivor": "concept-slug", "justification": "one sentence"}}
"""

CONCEPT_MERGE_USER = """\
Merge concept page concepts/{loser} INTO concepts/{survivor} (title: {title}).

Current content of concepts/{survivor}:
{survivor_body}

Content of concepts/{loser}, which is absorbed into the survivor and then
deleted:
{loser_body}

Write the merged page. Rules:
- Preserve ALL claims, numbers and citations from BOTH pages; never delete,
  weaken, round or reconcile evidence. Every [src: ...] id appearing in either
  page above must still appear in your page.
- Weave the two into ONE argument; do not concatenate them. Where both pages
  state the same claim, state it once carrying both citations.
- Where absorbed evidence sits next to an existing claim, state the relation in
  prose: "this **supports** ...", "this **contradicts** ...", or "this
  **refines** ..." — never just append a parallel fact.
- Genuine disagreements go under a ## Tensions section citing each side; never
  resolve by averaging or by silently preferring one side.
- Follow the wikilink whitelist rules above. Do not link [[concepts/{loser}]];
  that page is being deleted.
- Keep the ## Open Directions ending, merging both pages' entries.
- Keep it TIGHT: at most ~25% longer than the LONGER of the two inputs. This is
  a merge, not a concatenation.

Return ONLY valid JSON, no fences:
{{"description": "one line, at most 110 characters", "content": "# Title\\n\\n..."}}
"""

# Appended to compile.CONCEPT_UPDATE_USER. Back-merge candidates are matched by
# similarity, not by the plan step, so most of them genuinely have nothing to
# add — without this path the model invents a contribution to justify the call.
BACKMERGE_TAIL = """
IMPORTANT — this document was NOT previously part of this page. It was matched
by embedding similarity, so it may have nothing to contribute. If it contains no
evidence that genuinely supports, contradicts or refines a claim on this page,
return exactly:

{"description": "<this page's current description, unchanged>", "content": "UNCHANGED"}

Returning UNCHANGED is the correct and expected answer for most documents. Do
NOT manufacture a contribution: do not add a "See also" link, a bare mention of
the project, a restatement of the summary, or a generic sentence about the
document's topic. Only real, citable evidence earns an edit to this page.
"""


# ---------------------------------------------------------------------------
# Embeddings + similarity (no numpy: 153x153 and 139x75 are trivial)
# ---------------------------------------------------------------------------


def embed(texts: list[str]) -> list[list[float]]:
    """Embed and L2-normalise, so cosine is a plain dot product."""
    raw: list[list[float]] = []
    for i in range(0, len(texts), EMBED_BATCH):
        resp = litellm.embedding(
            model=EMBED_MODEL,
            input=[t[:EMBED_CHARS] for t in texts[i:i + EMBED_BATCH]],
            api_key=os.environ["OPENAI_API_KEY"],
            api_base=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
        )
        raw += [d["embedding"] for d in resp.data]
    return [unit(v) for v in raw]


def unit(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# Page bookkeeping
# ---------------------------------------------------------------------------


def body_src_ids(text: str) -> set[str]:
    """Distinct project ids actually cited in prose — the metric that matters.

    Deliberately NOT len(frontmatter['sources']): the v3 corpus listed sources
    it never cited, which is padding dressed up as synthesis."""
    return {s for par in paragraphs(text) for s in cited_ids(par)}


def sid_of(summary_stem: str) -> str:
    return re.sub(r"__REPORT$", "", summary_stem)


def digest(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def load_concepts(wiki: pathlib.Path) -> list[dict]:
    out = []
    for p in sorted((wiki / "concepts").glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = C.parse_fm(text)
        desc = str(fm.get("description") or "")
        lead = body.split("\n## ")[0].strip()
        out.append({
            "stem": p.stem, "path": p, "fm": fm, "body": body, "digest": digest(text),
            "cited": body_src_ids(text),
            "etext": f"{p.stem.replace('-', ' ')}. {desc}\n{lead}",
        })
    return out


def load_summaries(wiki: pathlib.Path) -> list[dict]:
    out = []
    for p in sorted((wiki / "summaries").glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = C.parse_fm(text)
        out.append({
            "stem": p.stem, "sid": sid_of(p.stem), "rel": f"summaries/{p.stem}.md",
            "body": body, "digest": digest(text),
            "etext": f"{sid_of(p.stem).replace('_', ' ')}. {fm.get('description') or ''}\n{body}",
        })
    return out


def merge_candidates(concepts: list[dict], vecs: list[list[float]],
                     threshold: float, mature: int) -> list[tuple]:
    """Ranked (sim, i, j) pairs above threshold, skipping pairs where BOTH sides
    are already mature. Absorbing a shard into a hub is in scope; collapsing two
    mature hubs into one is a destructive rewrite this stage should not make."""
    out = []
    for i in range(len(concepts)):
        for j in range(i + 1, len(concepts)):
            sim = cosine(vecs[i], vecs[j])
            if sim < threshold:
                continue
            if len(concepts[i]["cited"]) >= mature and len(concepts[j]["cited"]) >= mature:
                continue
            out.append((sim, i, j))
    return sorted(out, reverse=True)


def backmerge_candidates(concepts: list[dict], cvecs: list[list[float]],
                         summaries: list[dict], svecs: list[list[float]],
                         threshold: float, topk: int, mature: int) -> list[tuple]:
    """Ranked (sim, concept_idx, summary_idx) for thin concepts only."""
    out = []
    for i, c in enumerate(concepts):
        if len(c["cited"]) >= mature:
            continue
        have = set(c["fm"].get("sources") or []) | {f"summaries/{s}__REPORT.md" for s in c["cited"]}
        scored = sorted(
            ((cosine(cvecs[i], svecs[j]), j) for j, s in enumerate(summaries)
             if s["rel"] not in have and s["sid"] not in c["cited"]),
            reverse=True)
        out += [(sim, i, j) for sim, j in scored[:topk] if sim >= threshold]
    return sorted(out, reverse=True)


def rewrite_concept_links(text: str, loser: str, survivor: str) -> str:
    """Repoint [[concepts/loser]] and [[concepts/loser|alias]] at the survivor,
    then drop lines the rewrite made exact duplicates of an earlier line.

    # ponytail: only EXACT duplicate lines collapse. Two Slots-Into bullets that
    # now link the survivor with different rationales both survive; that reads
    # slightly redundant but loses no claim. Dedupe semantically if it shows up.
    """
    out = re.sub(
        r"\[\[concepts/" + re.escape(loser) + r"((?:\|[^\]]*)?)\]\]",
        lambda m: f"[[concepts/{survivor}{m.group(1)}]]", text)
    if out == text:
        return text
    link = f"[[concepts/{survivor}"
    seen: set[str] = set()
    kept = []
    for line in out.split("\n"):
        if link in line and line.strip():
            if line in seen:
                continue
            seen.add(line)
        kept.append(line)
    return "\n".join(kept)


def repoint_links(root: pathlib.Path, loser: str, survivor: str) -> int:
    changed = 0
    for base in (root / "wiki", root / "wiki-extra"):
        for f in base.rglob("*.md") if base.is_dir() else []:
            text = f.read_text(encoding="utf-8", errors="replace")
            new = rewrite_concept_links(text, loser, survivor)
            if new != text:
                f.write_text(new, encoding="utf-8")
                changed += 1
    return changed


# ---------------------------------------------------------------------------
# Generation with a citation-retention guard
# ---------------------------------------------------------------------------


def generate_retaining(messages: list[dict], step: str, sources: dict[str, str],
                       targets: set[str], required: set[str],
                       unchanged_ok: bool = False) -> dict:
    """compile.generate_page plus a merge-specific guard: no [src:] id may be
    dropped. generate_page takes no custom validator, so this is a post-check
    with its own single retry, phrased through the same RETRY_USER prompt."""
    def lost_ids(obj: dict) -> list[str]:
        content = (obj.get("content") or "").strip()
        if unchanged_ok and content == UNCHANGED:
            return []
        return sorted(required - body_src_ids(content))

    obj = C.generate_page(messages, step, sources, targets)
    lost = lost_ids(obj)
    if not lost:
        return obj
    print(f"    {step}: dropped [src:] {lost} — retrying")
    obj = C.generate_page(
        messages
        + [{"role": "assistant", "content": json.dumps(obj)},
           {"role": "user", "content": C.RETRY_USER.format(violations="\n".join(
               f"- you dropped citation [src: {s}]; every claim citing {s} must survive" for s in lost))}],
        f"{step}/retention", sources, targets)
    lost = lost_ids(obj)
    if lost:
        raise C.PageError(f"{step}: still dropping [src:] {lost} after retry")
    return obj


# ---------------------------------------------------------------------------
# Phases
# ---------------------------------------------------------------------------


def phase_merge(root: pathlib.Path, concepts: list[dict], pairs: list[tuple],
                sources: dict[str, str], system: str, state: dict) -> int:
    wiki = root / "wiki"
    targets = C.wikilink_targets(root)
    redirect: dict[str, str] = {}
    merged = 0
    for sim, i, j in pairs:
        a, b = concepts[i]["stem"], concepts[j]["stem"]
        a, b = redirect.get(a, a), redirect.get(b, b)
        if a == b:
            continue
        pa, pb = wiki / "concepts" / f"{a}.md", wiki / "concepts" / f"{b}.md"
        if not pa.exists() or not pb.exists():
            continue
        ta, tb = pa.read_text(encoding="utf-8", errors="replace"), pb.read_text(encoding="utf-8", errors="replace")
        key = f"{PROMPT_V}|{min(a, b)}|{max(a, b)}|{digest(ta)}{digest(tb)}"
        if key in state["rejected"]:
            continue
        fa, ba = C.parse_fm(ta)
        fb, bb = C.parse_fm(tb)
        ca, cb = body_src_ids(ta), body_src_ids(tb)

        raw = C.llm([{"role": "system", "content": system},
                     {"role": "user", "content": MERGE_JUDGE_USER.format(
                         a=a, b=b, body_a=ba, body_b=bb,
                         ids_a=", ".join(sorted(ca)) or "(none)",
                         ids_b=", ".join(sorted(cb)) or "(none)",
                         shared=", ".join(sorted(ca & cb)) or "(none)")}],
                    f"merge-judge/{a}+{b}")
        try:
            verdict = C.parse_json_reply(raw)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"    [WARN] unparseable merge verdict for {a}+{b} ({e}) — keeping both")
            continue
        survivor = str(verdict.get("survivor") or "").strip()
        if not verdict.get("merge") or survivor not in (a, b):
            state["rejected"][key] = str(verdict.get("justification") or "")[:200]
            continue
        loser = b if survivor == a else a
        sfm, sbody = (fa, ba) if survivor == a else (fb, bb)
        lfm, lbody = (fb, bb) if survivor == a else (fa, ba)
        print(f"  merging concepts/{loser} -> concepts/{survivor} (sim {sim:.3f}): "
              f"{str(verdict.get('justification') or '')[:90]}")

        task = CONCEPT_MERGE_USER.format(
            loser=loser, survivor=survivor,
            title=(sbody.splitlines() or ["#"])[0].lstrip("# ").strip() or survivor,
            survivor_body=sbody, loser_body=lbody)
        try:
            obj = generate_retaining(
                [{"role": "system", "content": system},
                 {"role": "user", "content": C.KNOWN_TARGETS_USER.format(
                     targets="\n".join(f"- {t}" for t in sorted(targets - {f"concepts/{loser}"})))},
                 {"role": "user", "content": task}],
                f"merge/{survivor}", sources, targets, required=ca | cb)
        except C.PageError as e:
            print(f"    [ERROR] {e} — keeping both pages")
            C._failures.append(f"consolidate:merge:{survivor}+{loser}")
            continue

        srcs = list(dict.fromkeys((sfm.get("sources") or []) + (lfm.get("sources") or [])))
        (wiki / "concepts" / f"{survivor}.md").write_text(
            C.fm_block({"type": "Concept", "description": obj.get("description", ""), "sources": srcs})
            + obj["content"].strip() + "\n", encoding="utf-8")
        (wiki / "concepts" / f"{loser}.md").unlink()
        targets.discard(f"concepts/{loser}")
        n = repoint_links(root, loser, survivor)
        redirect[loser] = survivor
        for k, v in list(redirect.items()):
            if v == loser:
                redirect[k] = survivor
        print(f"    merged; {n} page(s) repointed")
        merged += 1
    return merged


def phase_backmerge(root: pathlib.Path, concepts: list[dict], summaries: list[dict],
                    cands: list[tuple], sources: dict[str, str], system: str,
                    state: dict) -> tuple[int, int]:
    wiki = root / "wiki"
    targets = C.wikilink_targets(root)
    added = skipped = 0
    for sim, i, j in cands:
        c, s = concepts[i], summaries[j]
        path = wiki / "concepts" / f"{c['stem']}.md"
        if not path.exists():          # merged away in phase 1
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = C.parse_fm(text)
        if s["rel"] in (fm.get("sources") or []):
            continue
        key = f"{PROMPT_V}|{c['stem']}|{s['stem']}|{digest(text)}{s['digest']}"
        if key in state["no_evidence"]:
            continue

        title = (body.splitlines() or ["#"])[0].lstrip("# ").strip() or c["stem"]
        task = C.CONCEPT_UPDATE_USER.format(
            title=title, name=c["stem"], existing=body, sid=s["sid"], summary_stem=s["stem"]
        ) + BACKMERGE_TAIL
        try:
            obj = generate_retaining(
                [{"role": "system", "content": system},
                 {"role": "user", "content": C.KNOWN_TARGETS_USER.format(
                     targets="\n".join(f"- {t}" for t in sorted(targets)))},
                 {"role": "user", "content": f"Summary of document {s['sid']}:\n\n{s['body']}"},
                 {"role": "user", "content": task}],
                f"backmerge/{c['stem']}+{s['sid']}", sources, targets,
                required=body_src_ids(text), unchanged_ok=True)
        except C.PageError as e:
            print(f"    [ERROR] {e} — keeping old version")
            C._failures.append(f"consolidate:backmerge:{c['stem']}+{s['sid']}")
            continue

        content = (obj.get("content") or "").strip()
        # The anti-padding gate: frontmatter may only grow alongside a real
        # citation in prose. A rewrite that merely name-drops the project (a
        # See-also link, a bare mention) is discarded whole.
        if content == UNCHANGED or s["sid"] not in body_src_ids(content):
            why = "no evidence" if content == UNCHANGED else "no [src:] added — discarded"
            print(f"    backmerge/{c['stem']}+{s['sid']} (sim {sim:.3f}): {why}")
            state["no_evidence"][key] = True
            skipped += 1
            continue
        path.write_text(
            C.fm_block({"type": "Concept", "description": obj.get("description", ""),
                        "sources": C.merge_sources(fm, s["rel"])})
            + content + "\n", encoding="utf-8")
        print(f"    backmerge/{c['stem']}+{s['sid']} (sim {sim:.3f}): evidence added")
        added += 1
    return added, skipped


# ---------------------------------------------------------------------------


def report(concepts: list[dict], summaries: list[dict], cvecs,
           pairs: list[tuple], cands: list[tuple], args) -> None:
    hist: dict[int, int] = {}
    for c in concepts:
        hist[len(c["cited"])] = hist.get(len(c["cited"]), 0) + 1
    thin = sum(n for k, n in hist.items() if k < args.min_sources)
    print(f"\n{len(concepts)} concepts, {len(summaries)} summaries")
    print(f"cited projects per concept (body [src:] ids): {dict(sorted(hist.items()))}")
    print(f"thin concepts (< {args.min_sources} cited projects): {thin}\n")

    allpairs = sorted((cosine(cvecs[i], cvecs[j]) for i in range(len(concepts))
                       for j in range(i + 1, len(concepts))), reverse=True)
    print("concept-concept pairs above threshold (before the mature-pair skip):")
    for t in REPORT_THRESHOLDS:
        print(f"    >= {t:.2f}: {sum(1 for s in allpairs if s >= t):5d}")
    print(f"\n{len(pairs)} MERGE CANDIDATES at >= {args.merge_threshold} "
          f"(both sides >= {args.min_sources} cited projects skipped):")
    for sim, i, j in pairs:
        print(f"    {sim:.3f}  {concepts[i]['stem']} ({len(concepts[i]['cited'])})"
              f"  ||  {concepts[j]['stem']} ({len(concepts[j]['cited'])})")

    print(f"\n{len(cands)} BACK-MERGE CANDIDATES at >= {args.backmerge_threshold}, "
          f"top-{args.topk} per thin concept:")
    by_concept: dict[str, list[str]] = {}
    for sim, i, j in cands:
        by_concept.setdefault(concepts[i]["stem"], []).append(f"{sim:.3f} {summaries[j]['sid']}")
    for stem in sorted(by_concept):
        print(f"    {stem:<54} {'  '.join(by_concept[stem])}")
    print("\ndry run: no LLM calls, no writes, $0.")


def main(root: pathlib.Path, args) -> int:
    wiki = root / "wiki"
    sources = source_ids(root)
    system = C.SYSTEM.format(contract=(C.REPO / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = root / "state" / "consolidate.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    state.setdefault("rejected", {})
    state.setdefault("no_evidence", {})

    concepts, summaries = load_concepts(wiki), load_summaries(wiki)
    print(f"consolidate: embedding {len(concepts)} concepts + {len(summaries)} summaries "
          f"({EMBED_MODEL}, free)")
    cvecs, svecs = embed([c["etext"] for c in concepts]), embed([s["etext"] for s in summaries])
    pairs = merge_candidates(concepts, cvecs, args.merge_threshold, args.min_sources)
    cands = backmerge_candidates(concepts, cvecs, summaries, svecs,
                                 args.backmerge_threshold, args.topk, args.min_sources)

    if args.dry_run:
        report(concepts, summaries, cvecs, pairs, cands, args)
        return 0

    merged = phase_merge(root, concepts, pairs, sources, system, state)
    state_path.write_text(json.dumps(state, indent=1, sort_keys=True))

    if merged:   # survivors changed and losers are gone — re-embed ($0) before phase 2
        concepts = load_concepts(wiki)
        cvecs = embed([c["etext"] for c in concepts])
    cands = backmerge_candidates(concepts, cvecs, summaries, svecs,
                                 args.backmerge_threshold, args.topk, args.min_sources)
    added, skipped = phase_backmerge(root, concepts, summaries, cands, sources, system, state)
    state_path.write_text(json.dumps(state, indent=1, sort_keys=True))

    C.rebuild_index(root)
    final = load_concepts(wiki)
    single = sum(1 for c in final if len(c["cited"]) < 2)
    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(f"consolidate: {merged} merge(s), {added} back-merge(s), {skipped} no-evidence, "
          f"{len(final)} concepts ({single} still citing one project), "
          f"{len(C._failures)} failure(s); tokens in={C._usage['in']} out={C._usage['out']} "
          f"(~${est:.2f} est)")
    return 1 if C._failures else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=C.REPO)
    ap.add_argument("--dry-run", action="store_true", help="rank and print candidates; no LLM calls, $0")
    ap.add_argument("--merge-threshold", type=float, default=0.85)
    # 0.78 chosen from the dry-run sweep: it reaches 68 of 139 thin concepts,
    # where 0.82 reaches 39 and 0.75 only adds weak candidates that no-op.
    ap.add_argument("--backmerge-threshold", type=float, default=0.78)
    ap.add_argument("--topk", type=int, default=2, help="summaries offered per thin concept")
    ap.add_argument("--min-sources", type=int, default=4,
                    help="a concept citing fewer projects than this is thin; two concepts "
                         "that are both at or above it are never merged with each other")
    a = ap.parse_args()
    sys.exit(main(a.root, a))
