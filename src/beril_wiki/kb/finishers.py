"""Run the curator's deterministic postprocessing on a stateful checkout."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

from beril_wiki.agentic.runtime import WorkflowError, manifest


def finish(root: Path) -> dict[str, bool]:
    """Run extras, titles, names and errata, reporting changed file content per stage."""
    root = root.resolve()
    checkout = root / "reference"
    if not checkout.is_dir():
        checkout = root / "corpus"
    inherited = ("PATH", "PYTHONPATH", "PYTHONDONTWRITEBYTECODE", "SYSTEMROOT")
    env = {key: os.environ[key] for key in inherited if key in os.environ}
    env.update(
        BERIL_WIKI_ROOT=str(root),
        BERIL_CHECKOUT=str(checkout),
        FETCH_BACKEND="local",
        LITELLM_LOCAL_MODEL_COST_MAP="True",
    )
    changed = {}
    before = manifest(root, ("wiki", "state"))
    for stage in ("extras", "titles", "names", "errata"):
        args = [] if stage == "extras" else [str(root)]
        result = subprocess.run(
            [sys.executable, "-m", f"beril_wiki.stages.{stage}", *args],
            cwd=root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            encoding="utf-8",
            errors="replace",
            timeout=14_400,
        )
        if result.returncode or "[ERROR]" in result.stdout:
            tail = "\n".join(result.stdout.splitlines()[-12:])[-2500:]
            raise WorkflowError(f"stage {stage} failed (exit {result.returncode})\n{tail}")
        after = manifest(root, ("wiki", "state"))
        changed[stage] = before != after
        before = after
    return changed
