#!/usr/bin/env python3
"""Show a source's own error beside every figure it reaches.

A report's arithmetic slip passes every gate: the compiler copies its figures
faithfully and the checker only asks whether a figure appears in the source
it cites. The reports themselves are archived unedited, so the correction has
to live beside the claim on the compiled page. contract/errata.yaml records
each error as a person judged it; this stage appends the erratum under every
paragraph that cites the source and states all of the listed figures, on every
compile, idempotently. It runs after stages.names and before stages.figures so
placements are computed on the page the reader sees. A note may only use
figures its source states, so the callout passes the same checks as the claim
above it; the correction is given in the report's numbers or in words.

    uv run python -m beril_wiki.stages.errata [root]
"""

from __future__ import annotations

import pathlib
import re
import sys

import yaml

from beril_wiki.check import (
    NUMBER,
    cited_ids,
    derivable_numbers,
    norm_num,
    numbers_in,
    source_ids,
    unsupported_numbers,
)
from beril_wiki.paths import ROOT
from beril_wiki.stages.names import TARGETS, placement_key, restamp

ERRATA = pathlib.Path("contract") / "errata.yaml"
MARK = "> **Erratum.**"
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def load(root: pathlib.Path) -> list[dict]:
    """The errata, validated; a bad entry stops the stage rather than matching nothing."""
    path = root / ERRATA
    if not path.is_file():
        return []
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        raise ValueError(f"{ERRATA}: expected a list of entries")
    for n, entry in enumerate(data):
        if not isinstance(entry, dict) or set(entry) != {"source", "contains", "note"}:
            raise ValueError(f"{ERRATA} entry {n}: needs exactly source, contains, note")
        if not (root / "wiki" / "summaries" / f"{entry['source']}__REPORT.md").is_file():
            raise ValueError(f"{ERRATA} entry {n}: unknown source {entry['source']!r}")
        if not entry["contains"] or not all(isinstance(t, str) and t for t in entry["contains"]):
            raise ValueError(f"{ERRATA} entry {n}: contains must list non-empty strings")
        if not isinstance(entry["note"], str) or not entry["note"].strip():
            raise ValueError(f"{ERRATA} entry {n}: note must be non-empty text")
    # The callout is cited to the source it corrects and checked like any other
    # paragraph, so a note may only state figures that source itself contains.
    sources = source_ids(root)
    for n, entry in enumerate(data):
        text = callout(entry)
        ids = cited_ids(text)
        loose = [t for t in unsupported_numbers(text, ids, sources)]
        loose = [t for t in loose if t not in derivable_numbers(text, ids, sources)]
        if loose:
            raise ValueError(
                f"{ERRATA} entry {n}: note states {loose} which {entry['source']} does not; "
                "give the correction in the report's own figures or in words"
            )
    return data


def matches(par: str, entry: dict, page_source: str | None) -> bool:
    """The paragraph cites the source and states every listed token."""
    if page_source != entry["source"] and entry["source"] not in cited_ids(par):
        return False
    figures = numbers_in(par)
    for token in entry["contains"]:
        if NUMBER.fullmatch(token):
            if norm_num(token) not in figures:
                return False
        elif token not in par:
            return False
    return True


def callout(entry: dict) -> str:
    return f"{MARK} {' '.join(entry['note'].split())} [src: {entry['source']}]"


def apply(text: str, entries: list[dict], page_source: str | None) -> str:
    """The page with an erratum under each matching paragraph, or the text unchanged."""
    head = FRONTMATTER.match(text)
    prefix = head.group(0) if head else ""
    body = text[len(prefix) :]
    blocks = re.split(r"\n\s*\n", body)
    kept = [b for b in blocks if not b.lstrip().startswith(MARK)]
    out: list[str] = []
    hit = len(kept) != len(blocks)
    for block in kept:
        out.append(block)
        if block.lstrip().startswith("#"):
            continue
        for entry in entries:
            if matches(block, entry, page_source):
                out.append(callout(entry))
                hit = True
    if not hit:
        return text
    tail = "\n" if body.endswith("\n") else ""
    return prefix + "\n\n".join(b.strip("\n") for b in out) + tail


def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    entries = load(root)
    touched = added = 0
    rewritten: dict[str, str] = {}
    for sub, glob in TARGETS:
        for path in sorted((root / sub).glob(glob)):
            if not path.is_file():
                continue
            page_source = path.stem.removesuffix("__REPORT") if sub == "wiki/summaries" else None
            text = path.read_text(encoding="utf-8")
            new = apply(text, entries, page_source)
            if new != text:
                path.write_text(new, encoding="utf-8")
                touched += 1
                rewritten[placement_key(root, path)] = new
            added += new.count(MARK)
    stamped = restamp(root, rewritten)
    print(
        f"stages.errata: {len(entries)} erratum(s) placed {added} time(s); "
        f"{touched} file(s) rewritten, {stamped} figure placement(s) re-stamped"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
