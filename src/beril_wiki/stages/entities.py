#!/usr/bin/env python3
"""Entity deduplication by identity resolution, not similarity.

The concept detectors must NOT be reused here, and this is the reason: over
entity pages, embeddings rank `aciad2176` and `aciad3137` — two different genes
— at 0.971, and numeric overlap scores `cyanobacteriia` against `photosystem-ii`
at 1.00. Similarity measures subject matter, and every gene in one organism
shares subject matter. Two entity pages are the same entity only when something
*identifies* them as the same thing.

Three identity signals, all deterministic and free:

  1. name        the titles normalise to the same string (`egg-nog`/`eggnog`,
                 singular/plural, hyphen and space variants)
  2. alias       one page's canonical name appears in the other's alias list.
                 contract/AGENTS.md already requires pages to list aliases;
                 this reads what the compiler was told to write.
  3. identifier  both pages record the same external id (NCBI taxid, CHEBI,
                 KEGG, UniProt, Pfam, assembly accession)

A differing `type:` is disqualifying: a Compound and an Organism sharing a name
are two things, not one. Only 26 of 336 pages record an external id and 173 say
outright that none was reported, so signal 3 is a bonus rather than the basis —
which is why an id-extraction pass was never the prerequisite it looked like.

Merging goes through consolidate_concepts.apply_merge, so an entity merge gets
the same retention gate as a concept one: no [src:] id and no figure present in
either input may be missing from the merged page, or the merge is refused and
both pages are kept.

    uv run python -m beril_wiki.stages.entities              # report, change nothing
    uv run python -m beril_wiki.stages.entities --apply      # merge the pairs found
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys

from beril_wiki import compiler as C
from beril_wiki.paths import ROOT
from beril_wiki.stages.consolidate import apply_merge

ALIAS_SENTENCE = re.compile(
    r"(?:known\s+)?alias(?:es)?\s+(?:include|are|is|:)\s*(.+?)(?:\.(?:\s|$))", re.I | re.S
)
EXTERNAL_ID = re.compile(
    r"\bCHEBI:\s*(?P<chebi>\d+)"
    r"|\bPF(?P<pfam>\d{5})\b"
    r"|\b(?:NCBI\s+)?tax(?:on|onomy)?\s*id\s*[:=]?\s*(?P<taxid>\d{3,})"
    r"|\bGC[AF]_(?P<assembly>\d{6,})"
    r"|\bUniProt(?:KB)?[:\s]+(?P<uniprot>[A-NR-Z][0-9][A-Z0-9]{3}[0-9])",
    re.I,
)
# Words that carry no identity: two pages differing only by one of these are
# still two pages until a human says otherwise.
NOISE = re.compile(r"\b(?:the|a|an|of|in|and|for|to)\b")


def normalise(name: str) -> str:
    """Fold a display name to an identity key.

    Case, punctuation, spacing and a trailing plural are spelling, not identity:
    `egg-nog`, `EggNOG` and `eggnogs` are one thing. Everything else is left
    alone — this must not fold two genuinely different names together."""
    s = name.lower().strip()
    s = NOISE.sub(" ", s)
    s = re.sub(r"[^a-z0-9]+", "", s)
    return re.sub(r"s$", "", s) if len(s) > 4 else s


def page_title(text: str) -> str:
    m = re.search(r"^#\s+(.+?)\s*$", text, re.M)
    return m.group(1).strip() if m else ""


def aliases(text: str) -> set[str]:
    """Alias names the page declares, as identity keys."""
    out: set[str] = set()
    for m in ALIAS_SENTENCE.finditer(text):
        for part in re.split(r",| and | or |/|;", m.group(1)):
            part = re.sub(r"\[src:[^\]]*\]|\(.*?\)", " ", part).strip(" .*_`")
            # An alias sentence can run into prose; keep short noun-phrase-like
            # fragments only, or "E. coli and is also used in the Keio
            # collection" contributes a sentence as an alias.
            if part and len(part) <= 40 and len(part.split()) <= 5:
                key = normalise(part)
                if len(key) >= 3:
                    out.add(key)
    return out


IDENTITY_SECTION = re.compile(r"^##\s+Identity\s*\n(.*?)(?=\n##\s|\Z)", re.S | re.M)


def identifiers(text: str) -> set[str]:
    """External ids the page claims for ITSELF.

    Only the ## Identity section counts, which is where contract/AGENTS.md says
    a page records its own identifier. Reading the whole page instead matched
    every Pfam accession a page merely discusses, and proposed merging
    `klebsiella` with `methanococcus-maripaludis` because both mention PF13455,
    and `independent-component-analysis` with `tnseq` over PF00356. A mentioned
    accession is subject matter, not identity — the same confusion that makes
    embeddings useless here."""
    section = IDENTITY_SECTION.search(text)
    if not section:
        return set()
    out = set()
    for m in EXTERNAL_ID.finditer(section.group(1)):
        for kind, val in m.groupdict().items():
            if val:
                out.add(f"{kind}:{val.lower()}")
    return out


def load(kb: pathlib.Path) -> list[dict]:
    pages = []
    for f in sorted((kb / "wiki" / "entities").glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        fm, body = C.parse_fm(text)
        title = page_title(body) or f.stem
        pages.append(
            {
                "stem": f.stem,
                "title": title,
                "type": (fm.get("type") or "").lower(),
                "key": normalise(title),
                "slug_key": normalise(f.stem),
                "aliases": aliases(body),
                "ids": identifiers(body),
                "sources": len(C.canonical_sources(body)),
            }
        )
    return pages


def duplicate_pairs(pages: list[dict]) -> list[tuple[str, dict, dict]]:
    """Pairs identified as the same entity, with the signal that identified them."""
    out = []
    for i, a in enumerate(pages):
        for b in pages[i + 1 :]:
            # A Compound and an Organism sharing a name are two things.
            if a["type"] and b["type"] and a["type"] != b["type"]:
                continue
            shared_id = a["ids"] & b["ids"]
            if shared_id:
                out.append((f"identifier {sorted(shared_id)[0]}", a, b))
            elif (
                a["key"]
                and a["key"] in (b["key"], b["slug_key"])
                or (b["key"] and b["key"] == a["slug_key"])
            ):
                out.append(("name", a, b))
            elif a["key"] in b["aliases"] or b["key"] in a["aliases"]:
                out.append(("alias", a, b))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=pathlib.Path, default=ROOT)
    ap.add_argument(
        "--apply",
        action="store_true",
        help="merge each identified pair through the shared retention gate",
    )
    args = ap.parse_args()

    pages = load(args.root)
    pairs = duplicate_pairs(pages)
    print(f"stages.entities: {len(pages)} entity pages, {len(pairs)} identified duplicate pair(s)")
    for signal, a, b in pairs:
        # The page citing more projects survives; a tie keeps the shorter name.
        keep, drop = (
            (a, b) if (a["sources"], -len(a["stem"])) >= (b["sources"], -len(b["stem"])) else (b, a)
        )
        print(
            f"  [{signal}] {drop['stem']} -> {keep['stem']} "
            f"({drop['sources']} vs {keep['sources']} sources)"
        )

    if not args.apply or not pairs:
        return 0

    # Idempotent: once merged the loser is gone, so the next run finds nothing
    # and makes no model call. This is why the stage can sit in run_pipeline.sh.
    sources = C.load_sources(args.root)
    if not sources:
        print(f"stages.entities: no staged docs under {args.root}/staging", file=sys.stderr)
        return 1
    system = C.SYSTEM.format(contract=(ROOT / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    targets = C.wikilink_targets(args.root)
    state_path = args.root / "state" / "consolidate.json"
    state = json.loads(state_path.read_text()) if state_path.exists() else {}
    state.setdefault("pending", {})

    failed = []
    for signal, a, b in pairs:
        keep, drop = (
            (a, b) if (a["sources"], -len(a["stem"])) >= (b["sources"], -len(b["stem"])) else (b, a)
        )
        print(f"  merging entities/{drop['stem']} -> entities/{keep['stem']} ({signal})")
        if not apply_merge(
            args.root,
            drop["stem"],
            keep["stem"],
            targets,
            sources,
            system,
            state,
            state_path,
            [],
            collection="entities",
            page_type=drop["type"].title() or "Other",
        ):
            failed.append(f"{drop['stem']}->{keep['stem']}")
    C.rebuild_index(args.root)
    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(
        f"stages.entities: {len(pairs) - len(failed)} merged, {len(failed)} refused "
        f"(~${est:.2f} est)"
    )
    for f in failed:
        print(f"  [ERROR] merge refused by the retention gate: {f}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
