#!/usr/bin/env python3
"""Computed evidence labels for synthesis pages.

How much of the corpus stands behind a page, derived from the corpus alone:
how many distinct source projects the page cites, whether the corpus records
a conflict over those same sources, and whether the page carries a literature
context section. That last term states PRESENCE, not review: it is a heading
test, and nothing here re-verifies the PMIDs that stages/literature.py checked when
the section was written.

This is deliberately NOT the v1 atlas's `confidence:` field, and that field is
the reason. All 141 atlas pages carry `generated_by: Codex GPT-5` and
`status: draft`, none names a reviewer, and `last_reviewed:` clusters on five
dates matching generation batches. So `confidence: medium` there was a model
rating its own output, and `last_reviewed:` is a generation timestamp under a
name that asserts human review. A field is not evidence of the thing it is
named after.

Everything here is countable instead, and the label never claims anyone read
the page — the site-wide banner says the opposite, once, on every page.

Applies to synthesis pages (concepts, entities, topic hubs, conflicts), where
"how much backs this" is a real question. Summaries and raw reports are 1:1
with a single project by construction, so a label there would say nothing.

    uv run python src/beril_wiki/evidence.py          # print the label for every page
"""

from __future__ import annotations

import pathlib
import re
import sys

from beril_wiki.paths import ROOT

SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
LABELLED = ("concepts", "entities", "topics", "conflicts")
LIT_HEADING = re.compile(r"^##\s+Literature Context\s*$", re.M)


def page_sources(text: str) -> set[str]:
    """Distinct project ids cited in a page body."""
    out: set[str] = set()
    for m in SRC_TAG.finditer(text):
        for part in re.split(r"[,;]", m.group(1)):
            pid = re.sub(r"__REPORT$", "", part.strip())
            if pid:
                out.add(pid)
    return out


def conflict_sources(kb: pathlib.Path) -> list[set[str]]:
    """Project sets the corpus records a disagreement over.

    Read from each conflict page's own [src:] citations, NOT its filename.
    stages.conflicts.conflict_slug names a page after its first three projects
    and appends a digest beyond that, so 33 of 41 filenames cannot express the
    full set: a page overlapping only the omitted projects silently missed its
    "conflict on record" flag. The body cites every project in the group, so it
    is the authoritative set, and reading it also removes the filename-parsing
    special cases entirely."""
    out = []
    for f in sorted((kb / "wiki" / "conflicts").glob("conflict--*.md")):
        srcs = page_sources(f.read_text(encoding="utf-8", errors="replace"))
        if len(srcs) > 1:  # a one-project set can never meet the two-source test
            out.append(srcs)
    return out


def label(text: str, collection: str, conflicts: list[set[str]]) -> str | None:
    """Interpunct-joined evidence terms for a page, or None if it earns none.

    Returns the terms alone; the caller decides how to present them (publish
    renders them as the title of a callout under the page's H1)."""
    if collection not in LABELLED:
        return None
    srcs = page_sources(text)
    if not srcs:
        return None
    n = len(srcs)
    tier = "single-source" if n == 1 else "corroborated" if n < 4 else "well corroborated"
    bits = [f"{n} source project{'s' if n != 1 else ''}", tier]
    # A conflict page is itself the record of the disagreement; saying it has
    # one on record is circular.
    if collection != "conflicts" and any(len(srcs & c) >= 2 for c in conflicts):
        bits.append("conflict on record")
    if LIT_HEADING.search(text):
        bits.append("literature context")
    return " · ".join(bits)


def main() -> int:
    kb = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ROOT)
    conflicts = conflict_sources(kb)
    counts: dict[str, int] = {}
    for f in sorted((kb / "wiki").rglob("*.md")):
        line = label(f.read_text(encoding="utf-8", errors="replace"), f.parent.name, conflicts)
        if line:
            tier = line.split("·")[1].strip()
            counts[tier] = counts.get(tier, 0) + 1
            print(f"{f.relative_to(kb)}: {line}")
    print(
        f"\n{sum(counts.values())} labelled; "
        + ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
