#!/usr/bin/env python3
"""Promote cross-project tensions to dedicated conflict pages (v1's best idea).

Scans every concept page's `## Tensions` section, groups tensions that span
multiple projects, and writes one conflict page each to wiki-extra/conflicts/
with the v1 structure: Evidence Sides + Resolving Work. Idempotent: a tension
whose (sorted project set) was already promoted is skipped unless the source
tension text changed (content hash in frontmatter).

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        .venv/bin/python conflicts_build.py
"""

from __future__ import annotations

import hashlib
import os
import pathlib
import re
import sys

from litellm import completion

import compile as C
from consolidate_concepts import cosine, embed
from topics_build import bad_src_ids, strip_bad_src
from wiki_check import numbers_in, source_ids

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
OUT = ROOT / "wiki-extra" / "conflicts"
# Above the 99th percentile of pair similarity (0.900) on this corpus: conflict
# pages share a template, so the median pair is already 0.79.
CONFLICT_SIM = float(os.environ.get("CONFLICT_SIM", "0.93"))
FORCE = "--force" in sys.argv
MODEL = os.environ.get("WIKI_MODEL", "openai/gpt-5.6-luna")

PROMPT = """You are writing a CONFLICT page for a research wiki: a first-class record of a
real disagreement between projects in the corpus. Input: the tension text as written on
one or more concept pages, with its [src: project] citations.

Write markdown with exactly these sections:
# <Short conflict title — the disagreement, phrased as a tension>
(one-paragraph lead: what the disagreement is and why it matters)
## Evidence Sides
(one bolded subsection per side; each side's claim with its exact numbers and
 [src: project] tags copied from the input — never invent numbers or citations)
## Possible Reconciliations
(hypotheses that could make both sides right — measurement differences, scope
 differences, definitional differences — clearly labeled as hypotheses)
## Resolving Work
(3-5 bullets: the specific analyses or data that would settle it — data + method + question)

Rules: copy numbers exactly; a claim you cannot attribute must not be written; 300-600 words.
Link the source concept pages with [[concepts/<stem>]] wikilinks where given.
NAMING: the data platform is the KBase Data Lakehouse. Reports call it
BERDL or the BER Data Lakehouse; those are earlier names for the same
system and must not appear in a page you write. The project id
`berdl_data_atlas` and that project's title "BERDL Data Atlas" are names
of a project, not of the platform, and stay as they are.
"""


def tension_blocks() -> list[dict]:
    blocks = []
    for page in sorted((ROOT / "wiki/concepts").glob("*.md")):
        text = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^## Tensions?\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
        if not m:
            continue
        body = m.group(1).strip()
        projects = set()
        for t in re.finditer(r"\[src:\s*([^\]]+)\]", body):
            for p in re.split(r"[,;]", t.group(1)):
                projects.add(re.sub(r"__REPORT$", "", p.strip()))
        if len(projects) >= 2:
            blocks.append({"concept": page.stem, "text": body, "projects": projects})
    return blocks


def merge_similar_groups(groups: dict[tuple, list[dict]], threshold: float) -> dict[tuple, list[dict]]:
    """Fold together tension groups that describe ONE disagreement.

    Groups are keyed by their exact project set, so the same argument reaching a
    different set of projects becomes a second page. Two pages on this corpus
    said the same thing that way: "Species-Scale Null Versus Positive
    Metal-Conservation Associations" and "Species-Scale Nulls Versus Broad
    Environmental and Fitness Signals", cosine 0.954.

    A merge needs BOTH a shared project and near-identical text. Similarity
    alone is unsafe here: conflict pages share a rigid template, so the corpus
    median pair already sits at 0.79 and the 99th percentile at 0.90 — the
    default cutoff is deliberately above that, and over-merging would put two
    genuinely different disagreements on one page. Evidence overlap (the same
    figures restated) merges regardless of similarity, matching the concept
    stage's more precise detector."""
    keys = sorted(groups)
    if len(keys) < 2:
        return groups
    texts = ["\n".join(b["text"] for b in groups[k]) for k in keys]
    vecs = embed(texts)
    figs = [numbers_in(t) for t in texts]
    parent = {k: k for k in keys}

    def find(k):
        while parent[k] != k:
            parent[k] = parent[parent[k]]
            k = parent[k]
        return k

    for i, a in enumerate(keys):
        for j in range(i + 1, len(keys)):
            b = keys[j]
            if not (set(a) & set(b)):
                continue
            shared = figs[i] & figs[j]
            same_evidence = len(shared) >= 3 and len(shared) / max(1, len(figs[i] | figs[j])) >= 0.5
            if same_evidence or cosine(vecs[i], vecs[j]) >= threshold:
                ra, rb = find(a), find(b)
                if ra != rb:
                    parent[rb] = ra
                    print(f"  merging tension groups {sorted(set(b))[:3]} into {sorted(set(a))[:3]}"
                          f" ({'shared figures' if same_evidence else f'cosine {cosine(vecs[i], vecs[j]):.3f}'})")

    merged: dict[tuple, list[dict]] = {}
    for k in keys:
        merged.setdefault(find(k), []).extend(groups[k])
    # the surviving key must cover every project the folded groups carried
    out = {}
    for root, blocks in merged.items():
        out[tuple(sorted({p for b in blocks for p in b["projects"]}))] = blocks
    return out


def conflict_slug(projects: tuple[str, ...]) -> str:
    """Filename for a tension group, unique to its COMPLETE project set.

    The slug used to be the first three ids only, so two groups sharing those
    three overwrote one file — three such collisions existed on this corpus, and
    because `existing` is read once, the collided file flipped between the two
    groups on every otherwise-unchanged run. Groups of three or fewer keep the
    readable name; longer ones carry a short digest of the full set so identity
    is exact without unbounded filenames."""
    head = "conflict--" + "--".join(projects[:3])
    if len(projects) <= 3:
        return head
    tail = hashlib.sha256("|".join(projects).encode()).hexdigest()[:8]
    return f"{head}--{tail}"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    src_texts = source_ids(ROOT)
    targets = C.wikilink_targets(ROOT)
    existing = {}
    if FORCE:
        print("  --force: ignoring cached tension hashes")
    for f in ([] if FORCE else OUT.glob("*.md")):
        m = re.search(r"^<!-- tension-hash: (\w+) -->", f.read_text(encoding="utf-8"), re.M)
        if m:
            existing[f.stem] = m.group(1)

    # Group tensions that share their project set (same disagreement seen from
    # multiple concept pages).
    groups: dict[tuple, list[dict]] = {}
    for b in tension_blocks():
        groups.setdefault(tuple(sorted(b["projects"])), []).append(b)
    groups = merge_similar_groups(groups, CONFLICT_SIM)

    written = skipped = 0
    live: set[str] = set()
    for projects, blocks in sorted(groups.items()):
        slug = conflict_slug(projects)
        live.add(slug)
        digest = hashlib.sha256("\n".join(b["text"] for b in blocks).encode()).hexdigest()[:16]
        if existing.get(slug) == digest:
            skipped += 1
            continue
        payload = "\n\n---\n\n".join(
            f"[from concept page: concepts/{b['concept']}]\n{b['text']}" for b in blocks
        )
        resp = completion(
            model=MODEL,
            api_key=os.environ["OPENAI_API_KEY"],
            base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
            messages=[{"role": "system", "content": PROMPT},
                      {"role": "user", "content": payload}],
            temperature=0.3, timeout=600,
        ).choices[0].message.content.strip()
        # Concept names must never end up inside [src:]; topics_build has always
        # stripped them, conflicts_build never did, and wiki_check could not see
        # it because it did not scan this directory.
        bad = bad_src_ids(resp, set(src_texts))
        if bad:
            print(f"  ! conflicts/{slug}: invalid [src:] ids {bad[:4]} — stripping")
            resp = strip_bad_src(resp, set(src_texts))
        nv = C.prose_violations(resp, src_texts)
        if nv:
            print(f"  ! conflicts/{slug}: {len(nv)} unsupported figure(s) — retrying")
            resp = completion(
                model=MODEL, api_key=os.environ["OPENAI_API_KEY"],
                base_url=os.environ.get("OPENAI_BASE_URL", "https://api.cborg.lbl.gov"),
                messages=[{"role": "system", "content": PROMPT},
                          {"role": "user", "content": payload},
                          {"role": "assistant", "content": resp},
                          {"role": "user", "content":
                           "Figures in your page appear in none of the sources cited beside them:\n"
                           + "\n".join(f"- {x}" for x in nv[:12])
                           + "\nRewrite the full page. Copy every number exactly from a source cited "
                             "in the same paragraph, or drop the claim."}],
                temperature=0.3, timeout=600,
            ).choices[0].message.content.strip()
        resp = C.downgrade_dead_links(resp, targets)
        (OUT / f"{slug}.md").write_text(f"<!-- tension-hash: {digest} -->\n{resp}\n", encoding="utf-8")
        written += 1
        print(f"  wrote conflicts/{slug}.md ({len(blocks)} tension block(s), {len(projects)} projects)")
    # Retire conflict pages whose tension group no longer exists. topics_build
    # has always reaped its stale hubs; this stage never did, so every concept
    # merge stranded a page. Only reap after a clean pass, so an interrupted run
    # cannot delete pages it simply did not get to.
    reaped = 0
    if written or skipped:
        for stale in sorted(OUT.glob("*.md")):
            if stale.stem not in live:
                stale.unlink()
                reaped += 1
                print(f"  removed stale conflicts/{stale.stem}.md")
    print(f"conflicts: {written} written, {skipped} unchanged, {reaped} retired, {len(live)} live")


if __name__ == "__main__":
    main()
