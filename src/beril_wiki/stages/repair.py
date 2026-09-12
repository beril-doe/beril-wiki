#!/usr/bin/env python3
"""Targeted page repair: fix a generated page that fails write-time validation.

Compile's resume-skip is per *document*, not per page, so a page that
mis-attributes one number stays broken as long as it legitimately cites that
document elsewhere — the document is integrated, so nothing re-runs. That is
how `entities/mycobacterium-tuberculosis.md` kept crediting a 91% accessory-AMR
fraction to `metabolic_capability_dependency`, which never reports it, while
check warned about it on every run. wiki/ is generated, so the fix cannot
be a hand edit.

This stage closes that hole: it re-runs the affected page alone against its own
cited sources, quoting the exact violations, through the same generate_page
write-time validation and retry the compiler uses. Idempotent by construction —
a page that already validates is a no-op, so it costs $0 in the steady state.

    uv run python -m beril_wiki.stages.repair                 # every failing page
    uv run python -m beril_wiki.stages.repair wiki/entities/foo.md
    uv run python -m beril_wiki.stages.repair --dry-run       # report, change nothing
"""

from __future__ import annotations

import argparse
import pathlib
import sys

from beril_wiki import compiler as C
from beril_wiki.paths import ROOT

REPAIR_USER = """\
The page below is published in the wiki and fails write-time validation:

{violations}

Return the corrected page. Rules:
- Fix ONLY the violations. Every other sentence, number, heading, citation and
  wikilink must survive byte-for-byte — this is a repair, not a rewrite.
- A number credited to a source that does not report it is the most common
  case. Move the claim to the [src:] id that DOES report it (check the source
  texts above), or delete the claim if no cited source supports it. Never keep
  a number by guessing a citation for it.
- Do not add frontmatter; it is managed by code.

CURRENT PAGE (body only):

{body}

Return one JSON object: {{"content": "<the corrected page body as Markdown>"}}
Return ONLY valid JSON, no fences.
"""


def page_violations(
    path: pathlib.Path, sources: dict[str, str], targets: set[str]
) -> tuple[dict, str, list[str]]:
    fm, body = C.parse_fm(path.read_text(encoding="utf-8", errors="replace"))
    return fm, body, C.validate_page(body, sources, targets)


def canonicalise_sources(path: pathlib.Path, dry_run: bool) -> bool:
    """Drop `sources` entries the page body does not cite. True if it changed.

    Deterministic and free — no model call. docs/design.md's corpus contract says
    `sources` must never list a project the body does not cite, but nothing
    enforced it, so pages drifted: one entity listed 47 sources against 31 real
    citations. A padded list reads as synthesis without being it, and it drives
    compile's resume-skip, so a phantom entry tells the next run "already
    integrated" about a document that is not."""
    text = path.read_text(encoding="utf-8", errors="replace")
    fm, body = C.parse_fm(text)
    if not fm or "sources" not in fm:
        return False
    canonical = C.canonical_sources(body, fm.get("sources"))
    if canonical == fm["sources"]:
        return False
    dropped = len(fm["sources"]) - len(canonical)
    print(f"  {path.relative_to(ROOT)}: dropping {dropped} uncited source(s) from frontmatter")
    if not dry_run:
        fm["sources"] = canonical
        path.write_text(C.fm_block(fm) + body, encoding="utf-8")
    return True


def repair(
    path: pathlib.Path, sources: dict[str, str], targets: set[str], system: str, dry_run: bool
) -> str:
    """One of "clean", "repaired", "would-repair", or "failed".

    Failure and no-op must be distinguishable: main() exits nonzero on failure,
    and this stage runs before check under `set -euo pipefail`, so a
    repair that quietly gave up used to let an invalid page reach publish."""
    fm, body, violations = page_violations(path, sources, targets)
    if not violations:
        return "clean"
    rel = path.relative_to(ROOT)
    print(f"  {rel}: {len(violations)} violation(s)")
    for v in violations[:6]:
        print(f"      - {v}")
    if dry_run:
        return "would-repair"

    # Only the sources this page cites — a repair must not pull in new evidence.
    cited = {s for par in C.paragraphs(body) for s in C.cited_ids(par)}
    ctx = "\n\n---\n\n".join(
        f"[source: {sid}]\n{sources[sid]}" for sid in sorted(cited) if sid in sources
    )
    try:
        obj = C.generate_page(
            [
                {"role": "system", "content": system},
                {"role": "user", "content": f"SOURCE DOCUMENTS THIS PAGE CITES:\n\n{ctx}"},
                {
                    "role": "user",
                    "content": REPAIR_USER.format(
                        violations="\n".join(f"- {v}" for v in violations), body=body
                    ),
                },
            ],
            f"repair/{rel.stem}",
            sources,
            targets,
        )
    except C.PageError as e:
        print(f"      [ERROR] {e} — page left unchanged")
        return "failed"

    new_body = (obj.get("content") or "").strip()
    if not new_body:
        print("      [ERROR] empty repair — page left unchanged")
        return "failed"
    # Hubs and conflict pages carry no frontmatter; only wiki/ pages have a
    # `sources` list to keep in step with the body's citations.
    if fm:
        fm["sources"] = C.canonical_sources(new_body, fm.get("sources"))
    path.write_text((C.fm_block(fm) if fm else "") + new_body + "\n", encoding="utf-8")
    # Trust nothing: re-read from disk and confirm the written page validates.
    # generate_page validated the model's reply, not the file that reply became
    # once frontmatter was reattached.
    if page_violations(path, sources, targets)[2]:
        print("      [ERROR] page still invalid after repair")
        return "failed"
    print("      repaired")
    return "repaired"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "pages",
        nargs="*",
        type=pathlib.Path,
        help="pages to repair (default: every failing wiki/ page)",
    )
    ap.add_argument("--dry-run", action="store_true", help="report violations, change nothing")
    args = ap.parse_args()

    sources = C.load_sources(ROOT)
    if not sources:
        print(
            f"stages.repair: no staged docs under {ROOT}/staging — "
            "run stages.fetch first (needs BERIL_CHECKOUT)",
            file=sys.stderr,
        )
        return 1
    system = C.SYSTEM.format(contract=(ROOT / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    targets = C.wikilink_targets(ROOT)

    # Paths may be given relative to the repo root or the shell's cwd.
    pages = [p if p.is_absolute() else (ROOT / p).resolve() for p in args.pages] or sorted(
        p for d in ("concepts", "entities") for p in (ROOT / "wiki" / d).glob("*.md")
    )
    print(f"stages.repair: checking {len(pages)} page(s)")
    # Free deterministic pass first: a frontmatter fix needs no model, and
    # doing it before the LLM pass keeps the paid path to real prose defects.
    fm_fixed = sum(canonicalise_sources(p, args.dry_run) for p in pages)
    outcomes = [repair(p, sources, targets, system, args.dry_run) for p in pages]
    repaired = sum(o in ("repaired", "would-repair") for o in outcomes)
    failed = sum(o == "failed" for o in outcomes)

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    verb = "would repair" if args.dry_run else "repaired"
    print(
        f"stages.repair: {fm_fixed} frontmatter fix(es), {verb} {repaired} page(s), "
        f"{failed} still invalid; "
        f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)"
    )
    # Fail closed: an unrepaired violation must stop the pipeline here rather
    # than reach check as a non-blocking warning and then publish.
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
