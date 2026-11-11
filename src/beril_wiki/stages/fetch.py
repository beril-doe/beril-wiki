#!/usr/bin/env python3
"""Sync source docs into staging/ — the pipeline's single input gateway.

Two backends behind one function, selected by ``FETCH_BACKEND``:
  local  (default) copy REPORT.md per project + the discoveries/pitfalls
         digests from a checkout-shaped tree (``BERIL_CHECKOUT``, default
         the repository's own ``corpus/``; see ``beril_wiki.corpus``).
  hub    BERIL hub client — stub until projects/ moves there.

Other stages import ``CHECKOUT`` from here for figure/README/collections
paths, so the checkout location is configured in exactly one place.

    uv run python -m beril_wiki.stages.fetch [staging-dir]
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

from beril_wiki.corpus import FIG_EMBED, figure_destination
from beril_wiki.paths import ROOT

CHECKOUT = pathlib.Path(os.environ.get("BERIL_CHECKOUT", ROOT / "corpus"))
BACKEND = os.environ.get("FETCH_BACKEND", "local")


def fetch_local(staging: pathlib.Path) -> int:
    staging.mkdir(parents=True, exist_ok=True)
    # A report left from an earlier fetch would hide its deletion from changed_sources.
    for stale in staging.glob("*.md"):
        stale.unlink()
    figroot = staging.parent / "wiki" / "figures"
    n = nf = 0
    for report in sorted(CHECKOUT.glob("projects/*/REPORT.md")):
        text = report.read_text(encoding="utf-8", errors="replace")
        shutil.copy2(report, staging / f"{report.parent.name}__REPORT.md")
        n += 1
        # Figures referenced by the report travel with the wiki repo, so the
        # site is fully renderable from a clone; the checkout is fetch-only.
        for rel in set(FIG_EMBED.findall(text)):
            if ".." in pathlib.PurePosixPath(rel).parts:
                continue
            src = report.parent / rel
            if not src.exists():
                continue
            dst = figroot / figure_destination(report.parent.name, rel)
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                nf += 1
    for digest in ("discoveries.md", "pitfalls.md"):
        src = CHECKOUT / "docs" / digest
        if src.exists():
            shutil.copy2(src, staging / digest)
            n += 1
    if nf:
        print(f"synced {nf} figure(s) -> {figroot}")
    return n


def fetch_hub(staging: pathlib.Path) -> int:
    raise NotImplementedError(
        "hub backend: waiting on the BERIL hub client (projects/ is moving there)"
    )


def fetch(staging: pathlib.Path = ROOT / "staging") -> int:
    if BACKEND == "local":
        return fetch_local(staging)
    if BACKEND == "hub":
        return fetch_hub(staging)
    raise SystemExit(f"stages.fetch: unknown FETCH_BACKEND {BACKEND!r}")


if __name__ == "__main__":
    dest = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "staging"
    print(f"staged {fetch(dest)} docs -> {dest}")
