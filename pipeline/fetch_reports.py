#!/usr/bin/env python3
"""Sync source docs into staging/ — the pipeline's single input gateway.

Two backends behind one function, selected by ``FETCH_BACKEND``:
  local  (default) copy REPORT.md per project + the discoveries/pitfalls
         digests from a BERIL observatory checkout (``BERIL_CHECKOUT``).
  hub    BERIL hub client — stub until projects/ moves there.

Other stages import ``CHECKOUT`` from here for figure/README/collections
paths, so the checkout location is configured in exactly one place.

    uv run python pipeline/fetch_reports.py [staging-dir]
"""

from __future__ import annotations

import os
import pathlib
import shutil
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
CHECKOUT = pathlib.Path(
    os.environ.get("BERIL_CHECKOUT", "/Volumes/WorkSSD/Work/BERIL/BERIL-research-observatory")
)
BACKEND = os.environ.get("FETCH_BACKEND", "local")


def fetch_local(staging: pathlib.Path) -> int:
    staging.mkdir(parents=True, exist_ok=True)
    n = 0
    for report in sorted(CHECKOUT.glob("projects/*/REPORT.md")):
        shutil.copy2(report, staging / f"{report.parent.name}__REPORT.md")
        n += 1
    for digest in ("discoveries.md", "pitfalls.md"):
        src = CHECKOUT / "docs" / digest
        if src.exists():
            shutil.copy2(src, staging / digest)
            n += 1
    return n


def fetch_hub(staging: pathlib.Path) -> int:
    raise NotImplementedError("hub backend: waiting on the BERIL hub client (projects/ is moving there)")


def fetch(staging: pathlib.Path = ROOT / "staging") -> int:
    if BACKEND == "local":
        return fetch_local(staging)
    if BACKEND == "hub":
        return fetch_hub(staging)
    raise SystemExit(f"fetch_reports: unknown FETCH_BACKEND {BACKEND!r}")


if __name__ == "__main__":
    dest = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "staging"
    print(f"staged {fetch(dest)} docs -> {dest}")
