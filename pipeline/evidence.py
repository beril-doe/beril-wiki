#!/usr/bin/env python3
"""Computed evidence labels for synthesis pages.

How much of the corpus stands behind a page, derived from the corpus alone:
how many distinct source projects the page cites, whether the corpus records
a conflict over those same sources, and whether the page carries a
PMID-verified literature review.

This is deliberately NOT the v1 atlas's `confidence:` field. That field was a
human judgement carrying a `last_reviewed` date; this wiki has no reviewer and
no review ledger, so a generated `confidence: medium` would be an unbacked
assertion wearing metadata's clothes. Everything here is countable, and the
label never claims a human read the page — the site-wide banner says the
opposite, once, on every page.

Applies to synthesis pages (concepts, entities, topic hubs, conflicts), where
"how much backs this" is a real question. Summaries and raw reports are 1:1
with a single project by construction, so a label there would say nothing.

    uv run python pipeline/evidence.py          # print the label for every page
"""

from __future__ import annotations

import pathlib
import re
import sys

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

    Read from conflict page filenames (conflict--<proj>--<proj>...--<hash>.md),
    which conflicts_build owns and keeps in step with the page bodies."""
    out = []
    for f in (kb / "wiki-extra" / "conflicts").glob("conflict--*.md"):
        parts = f.stem.split("--")[1:]
        if len(parts) > 1:  # last part is the tension hash, not a project
            out.append(set(parts[:-1]))
    return out


def label(text: str, collection: str, conflicts: list[set[str]]) -> str | None:
    """The evidence line for a page, or None when it earns no label."""
    if collection not in LABELLED:
        return None
    srcs = page_sources(text)
    if not srcs:
        return None
    n = len(srcs)
    tier = ("single-source" if n == 1
            else "corroborated" if n < 4
            else "well corroborated")
    bits = [f"{n} source project{'s' if n != 1 else ''}", tier]
    # A conflict page is itself the record of the disagreement; saying it has
    # one on record is circular.
    if collection != "conflicts" and any(len(srcs & c) >= 2 for c in conflicts):
        bits.append("conflict on record")
    if LIT_HEADING.search(text):
        bits.append("literature-reviewed")
    return "> **Evidence** · " + " · ".join(bits)


def main() -> int:
    kb = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else pathlib.Path(__file__).parent.parent)
    conflicts = conflict_sources(kb)
    counts: dict[str, int] = {}
    for root in (kb / "wiki", kb / "wiki-extra"):
        for f in sorted(root.rglob("*.md")):
            line = label(f.read_text(encoding="utf-8", errors="replace"), f.parent.name, conflicts)
            if line:
                counts[line.split("·")[2].strip()] = counts.get(line.split("·")[2].strip(), 0) + 1
                print(f"{f.relative_to(kb)}: {line[2:]}")
    print(f"\n{sum(counts.values())} labelled; " + ", ".join(f"{v} {k}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
