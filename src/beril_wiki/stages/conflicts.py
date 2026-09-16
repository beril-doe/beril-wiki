#!/usr/bin/env python3
"""Promote cross-project tensions to dedicated conflict pages, one per disagreement.

Every paragraph of a concept page's `## Tensions` section that cites two or
more projects is one disagreement and becomes one conflict page under
wiki/conflicts/ (Evidence Sides + Resolving Work). Paragraphs restating the
same figures are folded onto one page. A page is written from a packed
evidence prompt, gated, reviewed and patched by agentic.prose; one that does
not converge keeps its previous version and is recorded as a failure while
the stage continues. Idempotent: an unchanged paragraph (content hash in a
leading comment) is skipped.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.conflicts
"""

from __future__ import annotations

import hashlib
import re
import sys

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import (
    NO_PREAMBLE,
    PLATFORM,
    Contract,
    PageFailure,
    derived_page,
    limit,
    parallel,
    prune_failures,
    record_failure,
    source_excerpts,
    strict_pages,
    workers,
)
from beril_wiki.check import SRC_TAG, numbers_in, source_ids
from beril_wiki.paths import ROOT

OUT = ROOT / "wiki" / "conflicts"
FORCE = "--force" in sys.argv

CONTRACT = Contract(
    rules=(
        "Write 300-600 words in total (the code gate allows 10% either way).",
        "Sections in this order: an H1 title phrasing the disagreement as a tension without "
        "taking a side; one lead paragraph saying what the disagreement is and why it matters; "
        "## Evidence Sides with one bolded subsection per side; ## Possible Reconciliations, "
        "each labelled as a hypothesis; ## Resolving Work with 3-5 bullets of data + method + "
        "question.",
        "Use only figures (numbers, percentages, counts, statistics) that appear in the TENSION "
        "text; never import a figure from the source excerpts, never compute or round one.",
        "Keep every [src: ...] tag exactly as the TENSION text gives it, beside the claim it "
        "supports; never re-tag a claim to another project and never invent a citation.",
        "State each side's direction, denominator and threshold exactly as the TENSION text "
        "does: a null result stays null, a threshold stays a threshold, a hypothesis stays a "
        "hypothesis; never resolve the tension by averaging or preferring one side.",
        "Any figure in the lead must also appear, cited, in Evidence Sides.",
        "Define jargon (abbreviations, method names, statistics) at first use.",
        "Link the concept page(s) the tension comes from as [[concepts/<stem>]]; link no other "
        "page.",
        NO_PREAMBLE.format(first="the H1"),
        PLATFORM,
    ),
    words=(300, 600),
    headings=("## Evidence Sides", "## Possible Reconciliations", "## Resolving Work"),
)
TASK = (
    "Write the CONFLICT page for the disagreement in the TENSION text: a first-class record "
    "of a real disagreement between projects in the corpus."
)


def tension_blocks() -> list[dict]:
    """One block per Tensions paragraph that cites two or more projects."""
    blocks = []
    for page in sorted((ROOT / "wiki/concepts").glob("*.md")):
        text = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^## Tensions?\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
        if not m:
            continue
        for index, par in enumerate(
            p.strip() for p in re.split(r"\n\s*\n", m.group(1)) if p.strip()
        ):
            projects = {
                re.sub(r"__REPORT$", "", p.strip())
                for tag in SRC_TAG.finditer(par)
                for p in re.split(r"[,;]", tag.group(1))
            }
            if len(projects) >= 2:
                blocks.append(
                    {"concept": page.stem, "index": index, "text": par, "projects": projects}
                )
    return blocks


def merge_similar_groups(blocks: list[dict]) -> list[list[dict]]:
    """Fold paragraphs that restate ONE disagreement onto one page.

    A merge needs a shared project and the same evidence: at least three shared
    figures making up at least half of their union. Text similarity is not
    used, since these paragraphs share a template and the old embedding path
    merged pages that were alike in shape rather than in claim."""
    figures = [numbers_in(b["text"]) for b in blocks]
    parent = list(range(len(blocks)))

    def find(i: int) -> int:
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    for i in range(len(blocks)):
        for j in range(i + 1, len(blocks)):
            if not (blocks[i]["projects"] & blocks[j]["projects"]):
                continue
            shared = figures[i] & figures[j]
            if len(shared) >= 3 and len(shared) / max(1, len(figures[i] | figures[j])) >= 0.5:
                parent[find(j)] = find(i)
    groups: dict[int, list[dict]] = {}
    for i, block in enumerate(blocks):
        groups.setdefault(find(i), []).append(block)
    return [sorted(g, key=lambda b: (b["concept"], b["index"])) for g in groups.values()]


def conflict_slug(group: list[dict]) -> str:
    """conflict--<concept>--<digest>: identity follows the paragraph, not the project set.

    Naming by project set let two disagreements on one concept overwrite each
    other; a short digest of the tension text keeps every disagreement distinct
    and retires the page when its paragraph changes."""
    tail = hashlib.sha256("\n".join(b["text"] for b in group).encode()).hexdigest()[:8]
    return f"conflict--{group[0]['concept']}--{tail}"


def concept_lead(text: str) -> str:
    body = C.parse_fm(text)[1]
    m = re.search(r"^(# .+?)\n+(.+?)(?:\n\n|\n#|\Z)", body, re.S)
    return f"{m.group(1)}\n{m.group(2).strip()}" if m else body[:600]


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    src_texts = source_ids(ROOT)
    targets = C.wikilink_targets(ROOT)
    concepts = {
        p.stem: p.read_text(encoding="utf-8", errors="replace")
        for p in (ROOT / "wiki/concepts").glob("*.md")
    }
    existing = {}
    if FORCE:
        print("  --force: ignoring cached tension hashes")
    for f in [] if FORCE else OUT.glob("*.md"):
        m = re.search(r"^<!-- tension-hash: (\w+) -->", f.read_text(encoding="utf-8"), re.M)
        if m:
            existing[f.stem] = m.group(1)

    todo, live, skipped = [], set(), 0
    for group in merge_similar_groups(tension_blocks()):
        slug = conflict_slug(group)
        live.add(slug)
        digest = hashlib.sha256("\n".join(b["text"] for b in group).encode()).hexdigest()[:16]
        if existing.get(slug) == digest:
            skipped += 1
            continue
        todo.append((slug, group, digest))

    def write(item: tuple) -> str:
        slug, group, _ = item
        projects = set().union(*(b["projects"] for b in group))
        tension = "\n\n".join(
            f"[from wiki/concepts/{b['concept']}.md, Tensions paragraph {b['index']}]\n{b['text']}"
            for b in group
        )
        leads = "\n\n".join(
            f"[concepts/{stem}]\n{concept_lead(concepts[stem])}"
            for stem in sorted({b["concept"] for b in group})
        )
        pack = (
            f"TENSION:\n{tension}\n\nCONCEPT CONTEXT (framing only):\n{leads}\n\n"
            "SOURCE EXCERPTS (verification only; a figure here that is absent from the "
            f"TENSION text must not be used):\n{source_excerpts(tension, projects, src_texts)}"
        )
        return derived_page(
            f"conflicts/{slug}",
            CONTRACT,
            TASK,
            pack,
            allowed="\n".join(b["text"] for b in group),
            sources=src_texts,
            valid_ids=projects,
            targets=targets,
        )

    cap = limit(sys.argv)
    if cap is not None:
        print(f"  --limit {cap}: writing at most {cap} page(s), retiring none")
        todo = todo[:cap]
    written = failed = 0
    for (slug, group, digest), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"conflicts/{slug}", result)
            print(f"  [FAILED] conflicts/{slug}: {result}")
            continue
        (OUT / f"{slug}.md").write_text(
            f"<!-- tension-hash: {digest} -->\n{result}\n", encoding="utf-8"
        )
        record_failure(f"conflicts/{slug}", None)
        written += 1
        print(f"  wrote conflicts/{slug}.md ({len(group)} paragraph(s))")
    # Retire pages whose disagreement no longer exists. Slugs follow the paragraph text,
    # so a failed replacement's predecessor lives under another slug: retire nothing in a
    # pass with failures, or the "keep the previous version" promise is empty.
    reaped = 0
    if failed:
        print(f"  {failed} page(s) failed: retiring nothing this pass")
    for stale in [] if cap is not None or failed else sorted(OUT.glob("*.md")):
        if stale.stem not in live:
            stale.unlink()
            reaped += 1
            print(f"  removed stale conflicts/{stale.stem}.md")
    prune_failures("conflicts/", {f"conflicts/{slug}" for slug in live})
    print(
        f"conflicts: {written} written, {skipped} unchanged, {failed} failed, "
        f"{reaped} retired, {len(live)} live"
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
