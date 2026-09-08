#!/usr/bin/env python3
"""Concept-consolidation stage: turn single-source concept shards into synthesis.

Runs after enrich on every pipeline invocation. Enrichment creates concepts one
document at a time and hardcodes a one-element `sources` list; compile only
merges a document into pages when THAT document changes. So a concept created
from document #60 is never revisited against documents #1-59, and 136 of 153
concepts cite exactly one project. This stage closes that loop in two phases,
replacing wiki_check's name-token duplicate heuristic for candidate generation:

  1. merge  — candidates come from three generators, most precise first: pages
              restating the same FIGURES, pages built from the same EVIDENCE
              BASE, and finally embedding rank as a recall net. Each pair gets
              one LLM merge/keep judgement; a merge is one merge-rewrite of the
              survivor through compile.generate_page, the loser deleted and its
              inbound wikilinks rewritten in code.
  2. back-merge — thin concepts (fewer than --min-sources cited projects) are
              offered their top-k most similar summaries through compile's
              existing CONCEPT_UPDATE_USER merge-rewrite.

Every rewrite is gated on losing nothing: no [src:] id and no figure present in
an input may be missing from the output.

The success metric is distinct [src:] ids in the page BODY, never the length of
the `sources` frontmatter list. The previous-generation corpus looked
multi-source but padded frontmatter with bare "See also" links on 60 of 81
pages; back-merge therefore has an explicit "return UNCHANGED" path and a
deterministic gate that discards any rewrite which does not add a real citation.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python pipeline/consolidate_concepts.py [--dry-run] [--root DIR]

--dry-run costs $0 and writes nothing: it ranks and prints both candidate lists
using only free embedding models, and makes no LLM calls.
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
import okf
from wiki_check import NUMBER, cited_ids, norm_num, paragraphs, source_ids, prose_only

# nomic is LBL-hosted and free; cohere is added for the merge phase only, as a
# second opinion on candidates (~$0.04 a pass). Embeddings are never cached:
# re-embedding is cheap and state/ stays free of multi-megabyte vector blobs.
EMBED_MODEL = os.environ.get("EMBED_MODEL", "openai/lbl/nomic-embed-text")
MERGE_MODELS = os.environ.get("MERGE_EMBED_MODELS",
                              "openai/lbl/nomic-embed-text,openai/cohere-embed-v4").split(",")
# the gateway corrupts big batches for every model, so keep them all small
MODEL_BATCH = {"openai/cohere-embed-v4": 32, "openai/gemini-embedding-001": 16}
# 8, not 100: the gateway duplicates nomic rows at a stride of 16, intermittently,
# so anything above 16 can come back corrupted. See embed().
FREE_MODELS = {"openai/lbl/nomic-embed-text"}   # LBL-hosted, $0/token
EMBED_BATCH = 8
EMBED_CHARS = 6000
UNCHANGED = "UNCHANGED"
# Bump when a prompt below changes, so cached negative verdicts are re-asked
# instead of silently outliving the prompt that produced them.
PROMPT_V = "v3-retain-figures"
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
- Weave rather than concatenate: aim for at most ~25% longer than the LONGER of
  the two inputs. This is a length GUIDANCE, not a licence to drop evidence — if
  keeping every measurement needs more room, take the room. Compress by merging
  duplicated sentences and shared framing, never by deleting a figure or a claim.

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


def embed(texts: list[str], model: str = EMBED_MODEL) -> list[list[float]]:
    """Embed and L2-normalise, so cosine is a plain dot product.

    Verifies that distinct inputs produced distinct vectors. The CBORG
    nomic endpoint intermittently returns DUPLICATED rows at a stride of 16:
    two unrelated concepts come back with byte-identical vectors (cos=1.000000).
    Nothing errors and the vectors look plausible; the only symptoms are
    impossible cosine=1.000 pairs and silently lost recall. Colliding rows are
    re-embedded singly, and we give up loudly rather than rank on bad vectors."""
    batch = MODEL_BATCH.get(model, EMBED_BATCH)
    raw: list[list[float]] = []
    for i in range(0, len(texts), batch):
        resp = litellm.embedding(
            model=model,
            input=[t[:EMBED_CHARS] for t in texts[i:i + batch]],
            api_key=os.environ["OPENAI_API_KEY"],
            api_base=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
        )
        raw += [d["embedding"] for d in resp.data]
    if len(raw) != len(texts):
        raise SystemExit(f"[ERROR] {model} returned {len(raw)} vectors for {len(texts)} inputs")
    for attempt in range(3):
        bad = _collisions(texts, raw)
        if not bad:
            return [unit(v) for v in raw]
        print(f"    {model}: {len(bad)} corrupted vector(s), re-embedding individually")
        for i in bad:
            resp = litellm.embedding(
                model=model, input=[texts[i][:EMBED_CHARS]],
                api_key=os.environ["OPENAI_API_KEY"],
                api_base=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"))
            raw[i] = resp.data[0]["embedding"]
    # A few residual collisions are tolerable: they add a spurious cosine=1.0
    # pair, and the LLM judge rejects it. Lost recall is the real harm, and the
    # repair passes above remove nearly all of it. Widespread corruption is not
    # tolerable — it would silently degrade the whole ranking.
    left = _collisions(texts, raw)
    if len(left) > max(4, len(texts) // 20):
        raise SystemExit(f"[ERROR] {model} returned {len(left)} duplicate vectors for distinct "
                         f"inputs after 3 repair passes — refusing to rank on corrupt embeddings")
    print(f"    [WARN] {model}: {len(left)} vector(s) still duplicated "
          f"({', '.join(str(i) for i in left[:6])}) — proceeding; the judge gates any false pair")
    return [unit(v) for v in raw]


def _collisions(texts: list[str], raw: list[list[float]]) -> list[int]:
    """Indices whose vector is shared with a DIFFERENT input's vector."""
    groups: dict[tuple, list[int]] = {}
    for i, v in enumerate(raw):
        groups.setdefault(tuple(v), []).append(i)
    return [i for g in groups.values() if len(g) > 1
            and len({texts[k][:EMBED_CHARS] for k in g}) > 1 for i in g]


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
        # Whole page, NOT just the lead. Measured against 8 duplicate pairs with
        # near-identical numbers: lead-only ranked them at median 2214 of 7381
        # (recall@45 = 0/8) because a lead paragraph carries topic vocabulary and
        # none of the evidence; the whole page ranks them at median 189.
        out.append({
            "stem": p.stem, "path": p, "fm": fm, "body": body, "digest": digest(text),
            "cited": body_src_ids(text), "nums": page_numbers(text),
            "etext": f"{p.stem.replace('-', ' ')}. {desc}\n{body}",
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


def both_mature(ca: set[str], cb: set[str], mature: int) -> bool:
    """Two concepts that each already cite `mature` projects are never merged
    into each other. Checked at candidate generation AND again against the
    live pages in phase_merge: a pair can become mature-mature mid-run, either
    because an earlier merge redirected one side onto a hub or because an
    earlier merge grew it. Checking only at generation merged a 28-project and
    a 32-project concept."""
    return len(ca) >= mature and len(cb) >= mature


def page_numbers(text: str) -> set[str]:
    return {norm_num(x) for par in paragraphs(text) for x in NUMBER.findall(prose_only(par))}


def evidence_candidates(concepts: list[dict], min_shared: int, min_jaccard: float) -> list[tuple]:
    """Pairs that restate the same measurements — deterministic, free, exact.

    The shard defect IS "two pages restating one study's numbers under different
    titles", so numeric overlap measures it directly instead of proxying it
    through semantic similarity. Embeddings rank these badly: a pair citing
    IDENTICAL number sets sat at rank 3016 of 7381 by cosine, because a whole-page
    vector encodes topic register far more strongly than which figures appear.
    Both sides must also cite a project in common, so coincidental number reuse
    across unrelated studies does not qualify."""
    out = []
    for i in range(len(concepts)):
        for j in range(i + 1, len(concepts)):
            a, b = concepts[i], concepts[j]
            if not (a["cited"] & b["cited"]):
                continue
            shared = a["nums"] & b["nums"]
            if len(shared) < min_shared:
                continue
            jac = len(shared) / max(1, len(a["nums"] | b["nums"]))
            if jac >= min_jaccard:
                out.append((jac, len(shared), i, j))
    return sorted(out, reverse=True)


def same_source_candidates(concepts: list[dict], mature: int) -> list[tuple]:
    """Thin pages built from the SAME evidence base — the structural signature of
    the defect, and a bounded set.

    `enrich_concepts.py` audits one summary at a time and may create several
    concepts from it, so its shards are pages resting on an IDENTICAL set of
    cited projects. That grouping is exact, free, and owes nothing to similarity:
    at the pre-consolidation revision it was 159 pairs out of 11,628, and judging
    it directly beats relying on a global embedding top-N whose measured recall
    on known duplicates was 29%.

    Equality, not containment: a shard whose source is merely a subset of a hub's
    is the absorb-into-hub case, which the figure and embedding generators
    already cover, and containment fires on almost every shard/hub pair once the
    corpus is mostly multi-source (128 candidates versus 8 on this corpus).

    It also catches what the numeric generator structurally cannot: qualitative
    shards that share a source but fewer than `--min-shared-numbers` figures."""
    out = []
    for i in range(len(concepts)):
        for j in range(i + 1, len(concepts)):
            a, b = concepts[i]["cited"], concepts[j]["cited"]
            if not a or not b or both_mature(a, b, mature):
                continue
            if a == b:                    # the SAME evidence base, not merely overlapping
                out.append((len(a), i, j))
    return sorted(out, reverse=True)


def merge_candidates(concepts: list[dict], vecs_by_model: dict[str, list],
                     topn: int, mature: int) -> list[tuple]:
    """Union of each model's top-`topn` pairs, skipping pairs where BOTH sides
    are already mature. Absorbing a shard into a hub is in scope; collapsing two
    mature hubs into one is a destructive rewrite this stage should not make.

    Selection is by RANK per model, not by a shared cosine cutoff: cosine ranges
    are not comparable across embedding models (cohere's medians sit ~0.2 below
    nomic's on identical text), so one threshold cannot serve both.

    Two models are used because one alone has recall holes. Measured on this
    corpus against 12 judge-confirmed duplicate pairs, nomic ranked 11 in its
    top-30 but buried `homology-search-negative-evidence` /
    `orthogonal-validation-of-gene-absence` at rank 518 of 11,628 — a genuine
    duplicate (same single source, same numbers restated) that cohere and gemini
    both put in their top-30. The union costs only extra judge calls, and the
    judge is what actually decides, so recall is the thing worth buying here.

    Returns (best_rank, sim, i, j), sorted best-rank first; `sim` is the score
    from whichever model ranked the pair highest, shown for eyeballing only."""
    best: dict[tuple[int, int], tuple[int, float]] = {}
    for vecs in vecs_by_model.values():
        pairs = sorted(
            ((cosine(vecs[i], vecs[j]), i, j)
             for i in range(len(concepts)) for j in range(i + 1, len(concepts))),
            reverse=True)[:topn]
        for rank, (sim, i, j) in enumerate(pairs, 1):
            if (rank, sim) < best.get((i, j), (10**9, 0.0)):
                best[(i, j)] = (rank, sim)
    return sorted((rank, sim, i, j) for (i, j), (rank, sim) in best.items()
                  if not both_mature(concepts[i]["cited"], concepts[j]["cited"], mature))


def backmerge_candidates(concepts: list[dict], cvecs: list[list[float]],
                         summaries: list[dict], svecs: list[list[float]],
                         threshold: float, topk: int, mature: int) -> list[tuple]:
    """Ranked (sim, concept_idx, summary_idx) for thin concepts only."""
    out = []
    for i, c in enumerate(concepts):
        if len(c["cited"]) >= mature:
            continue
        scored = sorted(
            ((cosine(cvecs[i], svecs[j]), j) for j, s in enumerate(summaries)
             if s["sid"] not in c["cited"]),
            reverse=True)
        out += [(sim, i, j) for sim, j in scored[:topk] if sim >= threshold]
    return sorted(out, reverse=True)


def rewrite_concept_links(text: str, loser: str, survivor: str, page: pathlib.Path | None = None) -> str:
    """Repoint [[concepts/loser]] and [[concepts/loser|alias]] at the survivor,
    then drop lines the rewrite made exact duplicates of an earlier line.

    Only exact duplicate link lines collapse; distinct rationales survive.
    """
    out = okf.map_prose(text, lambda chunk: re.sub(
        r"\[\[concepts/" + re.escape(loser) + r"((?:\|[^\]]*)?)\]\]",
        lambda m: f"[[concepts/{survivor}{m.group(1)}]]", chunk))
    def redirect(url):
        target = url.split("#", 1)[0]
        is_concept = "/concepts/" in "/" + target
        if page is not None:
            is_concept = (page.parent / target).resolve().parent.name == "concepts"
        return re.sub(r"(^|/)" + re.escape(loser) + r"(?=\.md(?:#|$))", lambda m: m[1] + survivor, url) if is_concept else url
    out = okf.map_links(out, redirect)
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
            new = rewrite_concept_links(text, loser, survivor, f)
            if new != text:
                f.write_text(new, encoding="utf-8")
                changed += 1
    return changed


# ---------------------------------------------------------------------------
# Generation with a citation-retention guard
# ---------------------------------------------------------------------------


def generate_retaining(messages: list[dict], step: str, sources: dict[str, str],
                       targets: set[str], required: set[str], required_nums: set[str],
                       unchanged_ok: bool = False) -> dict:
    """compile.generate_page plus a merge-specific guard: neither a [src:] id nor
    a FIGURE present in an input may be dropped.

    Checking ids alone is far too weak. A rewrite can delete any number of
    measurements and still keep one [src:] tag per source, and
    CONCEPT_MERGE_USER's "at most ~25% longer than the longer input" actively
    pressures it to do exactly that. Before numbers were checked here, merging
    `essentiality-prediction-task-definition` into `gene-essentiality` silently
    dropped 16 of its 97 figures — the condition-specific FBA correlations, the
    aromatic-degradation enrichments (OR 9.70, q 0.012) and a p = 0.80 null —
    and every gate in the pipeline passed, because wiki_check validates the
    numbers that remain, never the ones a rewrite deleted.

    generate_page takes no custom validator, so this is a post-check with its
    own single retry, phrased through the same RETRY_USER prompt."""
    def losses(obj: dict) -> tuple[list[str], list[str]]:
        content = (obj.get("content") or "").strip()
        if unchanged_ok and content == UNCHANGED:
            return [], []
        return (sorted(required - body_src_ids(content)),
                sorted(required_nums - page_numbers(content)))

    def violations(ids: list[str], nums: list[str]) -> str:
        v = [f"- you dropped citation [src: {s}]; every claim citing {s} must survive" for s in ids]
        if nums:
            v.append(f"- you deleted {len(nums)} figure(s) that appear in the page(s) above: "
                     f"{', '.join(nums[:25])}. Every measurement in the inputs must appear in "
                     f"your page, copied exactly. Restore the claims carrying them; if that makes "
                     f"the page longer than the length guidance, the length guidance yields.")
        return "\n".join(v)

    obj = C.generate_page(messages, step, sources, targets)
    lost_ids, lost_nums = losses(obj)
    if not lost_ids and not lost_nums:
        return obj
    print(f"    {step}: dropped {len(lost_ids)} citation(s), {len(lost_nums)} figure(s) — retrying")
    obj = C.generate_page(
        messages
        + [{"role": "assistant", "content": json.dumps(obj)},
           {"role": "user", "content": C.RETRY_USER.format(violations=violations(lost_ids, lost_nums))}],
        f"{step}/retention", sources, targets)
    lost_ids, lost_nums = losses(obj)
    if lost_ids or lost_nums:
        raise C.PageError(f"{step}: still dropping citations {lost_ids} / figures {lost_nums[:8]} "
                          f"after retry")
    return obj


# ---------------------------------------------------------------------------
# Phases
# ---------------------------------------------------------------------------


def replay_pending(root: pathlib.Path, state: dict, state_path: pathlib.Path) -> None:
    """Finish link repair a previous run was interrupted mid-way through."""
    for loser, survivor in list(state.get("pending", {}).items()):
        n = repoint_links(root, loser, survivor)
        print(f"  resuming interrupted merge {loser} -> {survivor}: {n} page(s) repointed")
        state["pending"].pop(loser, None)
    if state.get("pending") == {}:
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))


def phase_merge(root: pathlib.Path, concepts: list[dict], pairs: list[tuple],
                sources: dict[str, str], system: str, state: dict, mature: int,
                state_path: pathlib.Path, refused: list[str]) -> int:
    wiki = root / "wiki"
    targets = C.wikilink_targets(root)
    redirect: dict[str, str] = {}
    merged = 0
    for rank, sim, i, j in pairs:
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
        # Re-check against the LIVE pages, not the candidate-time snapshot: a
        # redirect or an earlier merge can have made both sides mature since.
        if both_mature(ca, cb, mature):
            print(f"    skipping {a}+{b}: both mature ({len(ca)}, {len(cb)} projects)")
            continue

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
        print(f"  merging concepts/{loser} -> concepts/{survivor} (rank {rank}, sim {sim:.3f}): "
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
                f"merge/{survivor}", sources, targets, required=ca | cb,
                required_nums=page_numbers(ta) | page_numbers(tb))
        except C.PageError as e:
            # NOT a failure: the retention gate refusing a lossy rewrite is the
            # gate doing its job, and both pages are left intact. Counting it in
            # C._failures would exit 1, and run_pipeline.sh runs under
            # `set -euo pipefail`, so one safely-declined merge would abort the
            # whole pipeline before conflicts, hubs and figures ever run.
            print(f"    [WARN] declined merge — {e}; keeping both pages")
            refused.append(f"merge:{survivor}+{loser}")
            continue

        # Union then canonicalise: a union alone carries both pages' padding forward.
        srcs = C.canonical_sources(obj["content"],
                                   list({okf.source_id(s): s for s in (sfm.get("sources") or [])
                                                      + (lfm.get("sources") or [])}.values()))
        okf.write(wiki / "concepts" / f"{survivor}.md",
            C.fm_block({**lfm, **sfm, "type": "Concept", "description": obj.get("description", ""), "sources": srcs})
            + obj["content"].strip() + "\n", encoding="utf-8")
        # Persist the redirect BEFORE deleting, so an interrupt between the
        # unlink and the link rewrite is recoverable: the next run finds the
        # loser gone, has no candidate to re-derive it from, and would otherwise
        # leave every inbound [[concepts/<loser>]] dangling forever.
        state.setdefault("pending", {})[loser] = survivor
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        (wiki / "concepts" / f"{loser}.md").unlink()
        targets.discard(f"concepts/{loser}")
        n = repoint_links(root, loser, survivor)
        state["pending"].pop(loser, None)
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        redirect[loser] = survivor
        for k, v in list(redirect.items()):
            if v == loser:
                redirect[k] = survivor
        print(f"    merged; {n} page(s) repointed")
        merged += 1
    return merged


def phase_backmerge(root: pathlib.Path, concepts: list[dict], summaries: list[dict],
                    cands: list[tuple], sources: dict[str, str], system: str,
                    state: dict, refused: list[str]) -> tuple[int, int]:
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
        # Body citations, not frontmatter: a `sources` entry the prose never
        # cites is padding, and treating it as "already integrated" would let
        # that padding permanently block the back-merge that would fix it.
        if s["sid"] in body_src_ids(text):
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
                required=body_src_ids(text), required_nums=page_numbers(text),
                unchanged_ok=True)
        except C.PageError as e:
            print(f"    [WARN] declined back-merge — {e}; keeping old version")
            refused.append(f"backmerge:{c['stem']}+{s['sid']}")
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
        okf.write(path,
            C.fm_block({"type": "Concept", "description": obj.get("description", ""),
                        "sources": C.canonical_sources(content, C.merge_sources(fm, s["rel"]))})
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
    print(f"concept-concept cosine ({EMBED_MODEL}) at thresholds:")
    for t in REPORT_THRESHOLDS:
        print(f"    >= {t:.2f}: {sum(1 for s in allpairs if s >= t):5d}")
    print(f"\n{len(pairs)} MERGE CANDIDATES "
          f"(evidence-overlap, then same-source, then embedding top-{args.merge_topn} per model; "
          f"pairs with both sides >= {args.min_sources} cited projects skipped):")
    for rank, sim, i, j in pairs:
        print(f"    #{rank:<3d} {sim:.3f}  {concepts[i]['stem']} ({len(concepts[i]['cited'])})"
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
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    state.setdefault("rejected", {})
    state.setdefault("no_evidence", {})
    state.setdefault("pending", {})

    concepts, summaries = load_concepts(wiki), load_summaries(wiki)
    models = [m.strip() for m in args.merge_models.split(",") if m.strip()]
    # --dry-run is advertised as $0, so it may only use free models. cohere is
    # ~$0.04 a pass; running it here would quietly bill an inspection command.
    if args.dry_run:
        models = [m for m in models if m in FREE_MODELS] or [EMBED_MODEL]
    if EMBED_MODEL not in models:            # back-merge always ranks with EMBED_MODEL
        models.append(EMBED_MODEL)
    print(f"consolidate: embedding {len(concepts)} concepts + {len(summaries)} summaries "
          f"({', '.join(models)})")
    cvecs_by = {m: embed([c["etext"] for c in concepts], m) for m in models}
    cvecs, svecs = cvecs_by[EMBED_MODEL], embed([s["etext"] for s in summaries])
    # Three generators, most-precise first. Both deterministic ones are free and
    # exact; embeddings are the recall net behind them for cross-source paraphrase.
    ev = [(0, j, i, k) for j, _, i, k in
          evidence_candidates(concepts, args.min_shared_numbers, args.evidence_jaccard)
          if not both_mature(concepts[i]["cited"], concepts[k]["cited"], args.min_sources)]
    seen = {(i, j) for _, _, i, j in ev}
    ss = [(1, float(n), i, j) for n, i, j in same_source_candidates(concepts, args.min_sources)
          if (i, j) not in seen]
    seen |= {(i, j) for _, _, i, j in ss}
    emb = [p for p in merge_candidates(concepts, cvecs_by, args.merge_topn, args.min_sources)
           if (p[2], p[3]) not in seen]
    pairs = ev + ss + emb
    print(f"  merge candidates: {len(ev)} evidence-overlap + {len(ss)} same-source + "
          f"{len(emb)} embedding = {len(pairs)}")
    cands = backmerge_candidates(concepts, cvecs, summaries, svecs,
                                 args.backmerge_threshold, args.topk, args.min_sources)

    if args.dry_run:
        report(concepts, summaries, cvecs, pairs, cands, args)
        return 0

    state_path.parent.mkdir(exist_ok=True)   # first write of the run happens here
    replay_pending(root, state, state_path)
    refused: list[str] = []
    merged = phase_merge(root, concepts, pairs, sources, system, state, args.min_sources,
                         state_path, refused)
    state_path.write_text(json.dumps(state, indent=1, sort_keys=True))

    if merged:   # survivors changed and losers are gone — re-embed before phase 2
        concepts = load_concepts(wiki)
        cvecs = embed([c["etext"] for c in concepts])
    cands = backmerge_candidates(concepts, cvecs, summaries, svecs,
                                 args.backmerge_threshold, args.topk, args.min_sources)
    added, skipped = phase_backmerge(root, concepts, summaries, cands, sources, system, state, refused)
    state_path.write_text(json.dumps(state, indent=1, sort_keys=True))

    C.rebuild_index(root)
    final = load_concepts(wiki)
    single = sum(1 for c in final if len(c["cited"]) < 2)
    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(f"consolidate: {merged} merge(s), {added} back-merge(s), {skipped} no-evidence, "
          f"{len(refused)} declined to avoid evidence loss, "
          f"{len(final)} concepts ({single} still citing one project), "
          f"{len(C._failures)} failure(s); tokens in={C._usage['in']} out={C._usage['out']} "
          f"(~${est:.2f} est)")
    if refused:
        print(f"  declined: {', '.join(refused)}")
    return 1 if C._failures else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=C.REPO)
    ap.add_argument("--dry-run", action="store_true", help="rank and print candidates; no LLM calls, $0")
    ap.add_argument("--min-shared-numbers", type=int, default=3,
                    help="evidence-overlap generator: shared exact figures required")
    ap.add_argument("--evidence-jaccard", type=float, default=0.5,
                    help="evidence-overlap generator: numeric-set Jaccard floor")
    ap.add_argument("--merge-topn", type=int, default=45,
                    help="pairs taken from EACH embedding model's ranking; the union is judged")
    ap.add_argument("--merge-models", default=",".join(MERGE_MODELS),
                    help="comma-separated embedding models for merge candidate generation")
    # 0.78 chosen from the dry-run sweep: it reaches 68 of 139 thin concepts,
    # where 0.82 reaches 39 and 0.75 only adds weak candidates that no-op.
    ap.add_argument("--backmerge-threshold", type=float, default=0.78)
    ap.add_argument("--topk", type=int, default=2, help="summaries offered per thin concept")
    ap.add_argument("--min-sources", type=int, default=4,
                    help="a concept citing fewer projects than this is thin; two concepts "
                         "that are both at or above it are never merged with each other")
    a = ap.parse_args()
    sys.exit(main(a.root, a))
