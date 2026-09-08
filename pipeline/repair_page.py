#!/usr/bin/env python3
"""Targeted page repair: fix a generated page that fails write-time validation.

Compile's resume-skip is per *document*, not per page, so a page that
mis-attributes one number stays broken as long as it legitimately cites that
document elsewhere — the document is integrated, so nothing re-runs. That is
how `entities/mycobacterium-tuberculosis.md` kept crediting a 91% accessory-AMR
fraction to `metabolic_capability_dependency`, which never reports it, while
wiki_check warned about it on every run. wiki/ is generated, so the fix cannot
be a hand edit.

This stage closes that hole: it re-runs the affected page alone against its own
cited sources, quoting the exact violations, through the same generate_page
write-time validation and retry the compiler uses. Idempotent by construction —
a page that already validates is a no-op, so it costs $0 in the steady state.

    uv run python pipeline/repair_page.py                 # every failing page
    uv run python pipeline/repair_page.py wiki/entities/foo.md
    uv run python pipeline/repair_page.py --dry-run       # report, change nothing
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import compile as C

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


def page_violations(path: pathlib.Path, sources: dict[str, str],
                    targets: set[str]) -> tuple[dict, str, list[str]]:
    fm, body = C.parse_fm(path.read_text(encoding="utf-8", errors="replace"))
    return fm, body, C.validate_page(body, sources, targets)


def repair(path: pathlib.Path, sources: dict[str, str], targets: set[str],
           system: str, dry_run: bool) -> bool:
    """True if the page was repaired (or would be, under --dry-run)."""
    fm, body, violations = page_violations(path, sources, targets)
    if not violations:
        return False
    rel = path.relative_to(C.REPO)
    print(f"  {rel}: {len(violations)} violation(s)")
    for v in violations[:6]:
        print(f"      - {v}")
    if dry_run:
        return True

    # Only the sources this page cites — a repair must not pull in new evidence.
    cited = {s for par in C.paragraphs(body) for s in C.cited_ids(par)}
    ctx = "\n\n---\n\n".join(
        f"[source: {sid}]\n{sources[sid]}" for sid in sorted(cited) if sid in sources
    )
    try:
        obj = C.generate_page(
            [{"role": "system", "content": system},
             {"role": "user", "content": f"SOURCE DOCUMENTS THIS PAGE CITES:\n\n{ctx}"},
             {"role": "user", "content": REPAIR_USER.format(
                 violations="\n".join(f"- {v}" for v in violations), body=body)}],
            f"repair/{rel.stem}", sources, targets)
    except C.PageError as e:
        print(f"      [ERROR] {e} — page left unchanged")
        return False

    new_body = (obj.get("content") or "").strip()
    if not new_body:
        print("      [ERROR] empty repair — page left unchanged")
        return False
    # Hubs and conflict pages carry no frontmatter; only wiki/ pages have a
    # `sources` list to keep in step with the body's citations.
    if fm:
        fm["sources"] = C.canonical_sources(new_body, fm.get("sources"))
    path.write_text((C.fm_block(fm) if fm else "") + new_body + "\n", encoding="utf-8")
    print("      repaired")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("pages", nargs="*", type=pathlib.Path,
                    help="pages to repair (default: every failing wiki/ page)")
    ap.add_argument("--dry-run", action="store_true", help="report violations, change nothing")
    args = ap.parse_args()

    sources = C.load_sources(C.REPO)
    if not sources:
        print(f"repair_page: no staged docs under {C.REPO}/staging — "
              "run fetch_reports first (needs BERIL_CHECKOUT)", file=sys.stderr)
        return 1
    system = C.SYSTEM.format(contract=(C.REPO / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    targets = C.wikilink_targets(C.REPO)

    # Paths may be given relative to the repo root or the shell's cwd.
    pages = [p if p.is_absolute() else (C.REPO / p).resolve() for p in args.pages] or sorted(
        p for d in ("concepts", "entities") for p in (C.REPO / "wiki" / d).glob("*.md")
    )
    print(f"repair_page: checking {len(pages)} page(s)")
    repaired = sum(repair(p, sources, targets, system, args.dry_run) for p in pages)

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    verb = "would repair" if args.dry_run else "repaired"
    print(f"repair_page: {verb} {repaired} page(s); "
          f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
