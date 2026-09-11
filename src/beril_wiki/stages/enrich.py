#!/usr/bin/env python3
"""Concept-enrichment stage: grow the synthesis layer the compiler under-built.

Runs after compile on every pipeline invocation. Per summary page
(hash-cached in state/enrich.json, so unchanged summaries are no-ops), one
plan call asks which synthesis concepts are MISSING for this doc's findings —
with a deliberately pro-creation prompt, the inverse bias of compile's plan
step, because the Luna bootstrap produced 19 concepts where the reference
corpus has 81. Each justified create goes through compiler.py's normal
generate-page machinery, so write-time validation, retry, frontmatter, and
index maintenance are identical to compile-time creates. Idempotent: existing
concepts are never touched here (compile owns merges), so re-running is safe.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python src/beril_wiki/stages/enrich.py [--root DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys

from beril_wiki import compiler as C
from beril_wiki.check import duplicate_concepts
from beril_wiki.paths import ROOT

ENRICH_PLAN_USER = """\
The summary above is already integrated into the wiki. Your job is DIFFERENT
from normal compilation: audit the CONCEPT layer for what is MISSING.

Existing concept pages:
{concept_briefs}

Duplicate-concept audit (do not add overlaps of these):
{dup_report}

A reader-facing synthesis wiki needs a concept page for each abstract,
RECURRING idea/pattern/mechanism this document's findings speak to. A concept
earns a page only when it would plausibly draw evidence from at least two
OTHER projects in a corpus about microbial genomics, fitness, ecology, and
annotation — name one such likely project or theme in the justification. Most
documents warrant 0-2 new concepts; a document whose findings all have
conceptual homes warrants 0. Good concepts argue across projects (e.g.
"phylogenetic-confounding", "cultivation-bias", "gene-essentiality") — never
document topics, single findings, organisms, or datasets (those are
entities), and never a finer-grained restatement of an existing page.

Return ONLY valid JSON:
{{"create": [{{"name": "concept-slug", "title": "Title",
  "justification": "why no existing page covers this phenomenon; name the closest existing
                    page and why it is not the same thing"}}]}}

Rules: only concepts genuinely evidenced by this summary; 0 is acceptable for
a document whose findings are all well covered; do not propose a slug that
already exists in the list above.
"""


def main(root: pathlib.Path) -> int:
    wiki = root / "wiki"
    sources = C.load_sources(root)
    system = C.SYSTEM.format(contract=(ROOT / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = root / "state" / "enrich.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    created = skipped = 0
    for spage in sorted((wiki / "summaries").glob("*.md")):
        text = spage.read_text(encoding="utf-8", errors="replace")
        digest = hashlib.sha256(text.encode()).hexdigest()[:16]
        if state.get(spage.name) == digest:
            skipped += 1
            continue
        stem = spage.stem
        sid = re.sub(r"__REPORT$", "", stem)
        _, summary_md = C.parse_fm(text)
        print(f"  enriching from {spage.name}")

        plan_raw = C.llm(
            [
                {"role": "system", "content": system},
                {"role": "user", "content": f"Summary of document {sid}:\n\n{summary_md}"},
                {
                    "role": "user",
                    "content": ENRICH_PLAN_USER.format(
                        concept_briefs=C.page_briefs(wiki / "concepts"),
                        dup_report="\n".join(duplicate_concepts(root)) or "(no duplicates flagged)",
                    ),
                },
            ],
            f"{sid}/enrich-plan",
        )
        try:
            plan = C.parse_json_reply(plan_raw)
        except (json.JSONDecodeError, ValueError) as e:
            print(f"    [ERROR] {sid}: unparseable enrich plan ({e}) — doc left dirty")
            C._failures.append(f"enrich:{sid}")
            continue

        targets = C.wikilink_targets(root)
        ok = True
        for it in plan.get("create") or []:
            if not isinstance(it, dict) or not str(it.get("name") or "").strip():
                continue
            name = re.sub(r"[^\w.-]+", "-", it["name"].strip()).strip("-")
            path = wiki / "concepts" / f"{name}.md"
            if path.exists():
                continue
            if not str(it.get("justification") or "").strip():
                print(f"    [WARN] rejecting unjustified concept {name!r}")
                continue
            targets.add(f"concepts/{name}")
            task = C.CONCEPT_CREATE_USER.format(
                title=it.get("title") or name, name=name, sid=sid, summary_stem=stem
            )
            try:
                obj = C.generate_page(
                    [
                        {"role": "system", "content": system},
                        {
                            "role": "user",
                            "content": C.KNOWN_TARGETS_USER.format(
                                targets="\n".join(f"- {t}" for t in sorted(targets))
                            ),
                        },
                        {"role": "user", "content": f"Summary of document {sid}:\n\n{summary_md}"},
                        {"role": "user", "content": task},
                    ],
                    f"{sid}/enrich/{name}",
                    sources,
                    targets,
                )
            except C.PageError as e:
                print(f"    [ERROR] {e} — concept not created")
                C._failures.append(f"enrich:{sid}:{name}")
                targets.discard(f"concepts/{name}")
                ok = False
                continue
            path.write_text(
                C.fm_block(
                    {
                        "type": "Concept",
                        "description": obj.get("description", ""),
                        "sources": C.canonical_sources(obj["content"], [f"summaries/{stem}.md"]),
                    }
                )
                + obj["content"].strip()
                + "\n",
                encoding="utf-8",
            )
            created += 1
        if ok:
            state[spage.name] = digest
            state_path.write_text(json.dumps(state, indent=1, sort_keys=True))

    C.rebuild_index(root)
    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(
        f"enrich: {created} concept(s) created, {skipped} summaries unchanged, "
        f"{len(C._failures)} failure(s); tokens in={C._usage['in']} out={C._usage['out']} "
        f"(~${est:.2f} est)"
    )
    return 1 if C._failures else 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=ROOT)
    sys.exit(main(ap.parse_args().root))
