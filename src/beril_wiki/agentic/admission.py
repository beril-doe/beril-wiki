"""Admit a run that adds or updates one project and owes no other work.

Two passes, each over a scratch copy of the live trees. The base pass fetches the
corpus committed at HEAD and refuses when `main` already owes editorial stages,
label refreshes, failed card entries of the project or a ledger reconciliation, since
a researcher's run would pay for them. Other projects' failed card entries do not
refuse: a run for one project leaves them as saved. The import pass fetches the given
checkout and refuses when anything but the expected project would change, or when the
run would re-integrate every source.
Nothing is written to the live trees or the job ledger.
"""

from __future__ import annotations

import contextlib
import io
import json
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

from beril_wiki import corpus
from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.runner import (
    adopts,
    checkout_inputs,
    due_editorial,
    invalidation,
    load_accepted,
    snapshot_trees,
)
from beril_wiki.agentic.runtime import WorkflowError, contract_manifest, digest
from beril_wiki.stages.cards import owners
from beril_wiki.stages.fetch import fetch_local
from beril_wiki.stages.novelty import labels_due
from beril_wiki.stages.shared import group_members

PROJECT_ID = r"[A-Za-z0-9][A-Za-z0-9_-]*"
# Card stages re-ask an entry saved as failed; a run for one project only its own.
CARD_STATE = (
    "gists",
    "links",
    "shared",
    "headlines",
    "novelty",
    "outcomes",
    "followups",
    "directions",
)


def head_corpus(root: Path, dest: Path) -> Path:
    """`corpus/` as committed at the root's HEAD."""
    archive = subprocess.run(
        ["git", "-C", str(root), "archive", "--format=tar", "HEAD", "corpus"],
        capture_output=True,
        check=False,
    )
    if archive.returncode:
        detail = archive.stderr.decode(errors="replace").strip()
        raise WorkflowError(f"cannot read corpus/ at HEAD: {detail}")
    with tarfile.open(fileobj=io.BytesIO(archive.stdout)) as tar:
        tar.extractall(dest, filter="data")
    if not (dest / "corpus" / corpus.MANIFEST).is_file():
        raise WorkflowError(f"corpus/{corpus.MANIFEST} is not committed at HEAD")
    return dest / "corpus"


def prepare(root: Path, work: Path, checkout: Path) -> dict[str, str]:
    """Copy the live trees into `work` and fetch `checkout` into cleared staging, as
    `run` prepares its own snapshot. Returns the checkout's inputs."""
    external = checkout_inputs(checkout)
    work.mkdir()
    snapshot_trees(root, work, checkout, external)
    shutil.rmtree(work / "staging")
    (work / "staging").mkdir()
    # fetch reports synced figures on stdout, which carries the plan's JSON.
    with contextlib.redirect_stdout(sys.stderr):
        fetch_local(work / "staging", work / "reference")
    return external


def write_extras(work: Path, checkout: Path) -> None:
    """Run the extras stage on `work` as a run's curator does first, so the author pages
    a README change rewrites make the authors stage due here too."""
    # extras reads ROOT and CHECKOUT at import, so it needs its own process.
    env = os.environ | {"BERIL_WIKI_ROOT": str(work), "BERIL_CHECKOUT": str(checkout)}
    done = subprocess.run(
        [sys.executable, "-m", "beril_wiki.stages.extras"],
        cwd=work,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if done.returncode:
        raise WorkflowError(f"extras failed in the admission scratch: {done.stderr[-1000:]}")


def unknown_usage(root: Path) -> list[str]:
    path = root / ".agentic/jobs.sqlite"
    if not path.exists():
        return []
    # Read-only: opening a Ledger would create its tables in the live store.
    try:
        db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        try:
            rows = db.execute("SELECT key FROM jobs WHERE status='unknown' ORDER BY rowid")
            return [key for (key,) in rows]
        finally:
            db.close()
    except sqlite3.Error as exc:
        raise WorkflowError(f"cannot read the job ledger {path}: {exc}") from exc


def failed_entries(root: Path, expect: str) -> tuple[list[str], list[str]]:
    """`<state>:<key>` for each card entry saved with `failed: true`: those of project
    `expect`, then the rest, which a topic-keyed store's entries always are."""
    own: list[str] = []
    others: list[str] = []
    members = group_members(root)
    for name in CARD_STATE:
        path = root / "state" / f"{name}.json"
        if not path.is_file():
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as exc:
            raise WorkflowError(f"cannot read {path}: {exc}") from exc
        if name == "links" and isinstance(data, dict):
            data = data.get("candidates", {})
        if not isinstance(data, dict):
            continue
        for key, entry in data.items():
            if isinstance(entry, dict) and entry.get("failed") is True:
                projects = owners(name, key, members.get(key, ()))
                mine = projects is not None and expect in projects
                (own if mine else others).append(f"{name}:{key}")
    return own, others


def outside(paths: set[str], expect: str) -> list[str]:
    return sorted(p for p in paths if not p.startswith(f"projects/{expect}/"))


def differing(before: dict, after: dict) -> set[str]:
    return {key for key in before.keys() | after.keys() if before.get(key) != after.get(key)}


def listed(items: list[str], limit: int = 10) -> str:
    more = f" and {len(items) - limit} more" if len(items) > limit else ""
    return ", ".join(items[:limit]) + more


def manifest_scope(base: dict, imported: dict, expect: str) -> list[str]:
    """Manifest entries other than `projects/<expect>` that differ between the two."""
    changed = sorted(differing(base, imported) - {"projects"})
    projects = differing(base.get("projects", {}), imported.get("projects", {})) - {expect}
    return changed + [f"projects/{pid}" for pid in sorted(projects)]


def admit(root: Path, checkout: Path, expect: str) -> dict:
    """Whether a run from `checkout` adds or updates project `expect` and nothing else.

    `pending_editorial` lists the stages the import makes due; `base_pending`,
    `labels_due` and `unknown_usage` describe what the base owes before it, and
    `maintenance_failed` the other projects' failed card entries, which do not refuse."""
    if not re.fullmatch(PROJECT_ID, expect):
        raise WorkflowError(f"--expect-source must match {PROJECT_ID}, got {expect!r}")
    if (root / ".agentic/promotion.json").exists():
        raise WorkflowError("promotion pending; run recover before inspection")
    if not (checkout / corpus.MANIFEST).is_file():
        raise WorkflowError(f"checkout {checkout} has no {corpus.MANIFEST}")
    reasons: list[str] = []
    accepted = load_accepted(root)
    with tempfile.TemporaryDirectory(prefix="beril-admit-") as tmp:
        # checkout_inputs refuses symlinked parents, and macOS links /var to /private/var.
        scratch = Path(tmp).resolve()
        head = head_corpus(root, scratch / "head")
        base = scratch / "base"
        base_inputs = prepare(root, base, head)
        base_pending = due_editorial(base)
        due = labels_due(base)
        unknown = unknown_usage(root)
        failed, maintenance = failed_entries(base, expect)
        if base_pending:
            reasons.append(f"main owes editorial stages: {', '.join(base_pending)}")
        if failed:
            reasons.append(f"main has failed card entries of {expect}: {listed(failed)}")
        if due:
            reasons.append("main owes a refresh of novelty labels past their age")
        if unknown:
            reasons.append(
                f"main has jobs with unknown usage; reconcile them with `agentic account`: "
                f"{listed(unknown)}"
            )
        work = scratch / "import"
        external = prepare(root, work, checkout)
        try:
            changed = changed_sources(work)
        except WorkflowError as exc:
            changed = []
            reasons.append(str(exc))
        if extra := [name for name in changed if name != f"{expect}__REPORT.md"]:
            reasons.append(
                f"sources other than {expect}__REPORT.md would integrate: {listed(extra)}"
            )
        reason = invalidation(work, accepted, adopts(accepted, digest(contract_manifest(work))))
        if reason:
            reasons.append(f"the accepted {reason} differs, so every source would re-integrate")
        if inputs := outside(differing(base_inputs, external), expect):
            reasons.append(
                f"checkout inputs outside projects/{expect}/ differ from HEAD: {listed(inputs)}"
            )
        if entries := manifest_scope(corpus.load(head), corpus.load(checkout), expect):
            reasons.append(
                f"{corpus.MANIFEST} differs from HEAD outside projects/{expect}: {listed(entries)}"
            )
        write_extras(work, work / "reference")
        pending = due_editorial(work)
    return {
        "admitted": not reasons,
        "reasons": reasons,
        "changed_sources": changed,
        "pending_editorial": pending,
        "base_pending": base_pending,
        "labels_due": due,
        "unknown_usage": unknown,
        "maintenance_failed": maintenance,
        "invalidation": reason,
    }
