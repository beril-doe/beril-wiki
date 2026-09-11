#!/usr/bin/env python3
"""Parity acceptance test for the first-party compiler (docs/design.md protocol).

Compiles the held-out projects INTO a copy of the reference corpus
(reference/wiki-v3) and compares the resulting merges against how the
reference handled the same projects:

  parity/ours  reference copy with the held-out summaries removed and
               state/hashes.json seeded so only the held-out docs compile
  parity/ref   pristine reference copy (the benchmark)

Then runs check.py on both and prints which pages our compiler
created/updated. Requires a populated staging/ (run stages/fetch.py first)
and OPENAI_API_KEY/OPENAI_BASE_URL for the compile step.

    uv run python src/beril_wiki/parity.py
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import shutil
import subprocess
import sys

from beril_wiki.paths import ROOT

REF = ROOT / "reference" / "wiki-v3"
PARITY = ROOT / "parity"

HELD_OUT = ["metal_specificity", "bacdive_phenotype_metal_tolerance", "prophage_amr_comobilization"]


def snapshot(root: pathlib.Path) -> dict[str, str]:
    return {
        str(f.relative_to(root)): hashlib.sha256(f.read_bytes()).hexdigest()
        for f in (root / "wiki").rglob("*.md")
    }


def setup() -> None:
    shutil.rmtree(PARITY, ignore_errors=True)
    for name in ("ours", "ref"):
        dest = PARITY / name
        shutil.copytree(REF / "wiki", dest / "wiki")
        os.symlink(ROOT / "staging", dest / "staging")

    ours = PARITY / "ours"
    hashes = {}
    for f in sorted((ROOT / "staging").glob("*.md")):
        sid = f.stem.removesuffix("__REPORT")
        if sid not in HELD_OUT:
            hashes[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()
    (ours / "state").mkdir()
    (ours / "state" / "hashes.json").write_text(json.dumps(hashes, indent=1, sort_keys=True))
    for sid in HELD_OUT:
        (ours / "wiki" / "summaries" / f"{sid}__REPORT.md").unlink()


def run_check(root: pathlib.Path, label: str) -> str:
    r = subprocess.run(
        [sys.executable, "-m", "beril_wiki.check", str(root)], capture_output=True, text=True
    )
    (PARITY / f"wiki_check.{label}.txt").write_text(r.stdout + r.stderr)
    tail = r.stdout.strip().splitlines()[-1] if r.stdout.strip() else "(no output)"
    print(f"  {label}: {tail} (exit {r.returncode})")
    return r.stdout


def main() -> int:
    if not (ROOT / "staging").is_dir() or not any((ROOT / "staging").glob("*.md")):
        raise SystemExit("parity: run stages/fetch.py first (staging/ is empty)")
    setup()
    before = snapshot(PARITY / "ours")

    docs = [f"{sid}__REPORT.md" for sid in HELD_OUT]
    print(f"== compiling {len(docs)} held-out doc(s) into parity/ours")
    r = subprocess.run(
        [sys.executable, "-m", "beril_wiki.compiler", "--root", str(PARITY / "ours"), *docs]
    )
    compile_rc = r.returncode

    after = snapshot(PARITY / "ours")
    created = sorted(p for p in after if p not in before)
    updated = sorted(
        p
        for p in after
        if p in before
        and after[p] != before[p]
        and not p.startswith("wiki/catalog")
        and not p.startswith("wiki/log")
    )
    print(f"\n== pages: {len(created)} created, {len(updated)} updated (catalog/log excluded)")
    for p in created:
        print(f"  created  {p}")
    for p in updated:
        print(f"  updated  {p}")

    print("\n== check")
    run_check(PARITY / "ours", "ours")
    run_check(PARITY / "ref", "ref")
    print(f"\nparity artifacts in {PARITY}/ ; compile exit {compile_rc}")
    return compile_rc


if __name__ == "__main__":
    sys.exit(main())
