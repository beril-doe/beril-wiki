#!/usr/bin/env python3
"""Pull the section vectors from the `history` branch into the local store.

The vectors (about 8 MB) are rebuilt whenever page text changes. They travel
two ways, both written by `beril_wiki.publish.artifact push`: inside every site
artifact (``corpus/section-vectors.jsonl``) and on the ``history`` branch, which
records ``search/section-vectors.jsonl`` with ``wiki/``, ``state/`` and
``corpus/index.json`` for every published artifact. The single-commit
``search-data`` branch this module used to push to is retired.

    uv run python -m beril_wiki.publish.search_data pull

scripts/build_quartz.sh runs it before indexing, in CI and locally, so a build
only embeds sections that have no vector anywhere. `pull` merges the branch's
rows into ``search/section-vectors.jsonl`` and keeps local rows the branch lacks,
so a feature branch's build never drops vectors it embedded itself. With
``SEARCH_REQUIRE_VECTORS=1`` (pull-request builds) the index builder then fails
on any section without a vector, as before.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import pathlib
import subprocess
import sys

from beril_wiki.paths import ROOT
from beril_wiki.publish.history import BRANCH

FILE = "search/section-vectors.jsonl"
DIM = 768


class SearchDataError(RuntimeError):
    pass


def git(root: pathlib.Path, *args: str, input: bytes | None = None) -> str:
    r = subprocess.run(["git", "-C", str(root), *args], input=input, capture_output=True)
    if r.returncode:
        raise SearchDataError(f"git {' '.join(args)}: {r.stderr.decode().strip()}")
    return r.stdout.decode()


def parse(text: str, where: str) -> dict[str, dict]:
    """Rows by hash; a malformed row fails loudly rather than shipping a broken store."""
    rows: dict[str, dict] = {}
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            r = json.loads(line)
            if len(base64.b64decode(r["v"])) != DIM or not isinstance(r["s"], (int, float)):
                raise ValueError("bad vector")
        except (ValueError, KeyError, TypeError) as exc:
            raise SearchDataError(f"{where}:{n}: not a {DIM}-dimension vector row ({exc})") from exc
        rows[r["h"]] = {"v": r["v"], "s": r["s"]}
    return rows


def render(rows: dict[str, dict]) -> str:
    # Same format as stages.search_vectors.write_store: sorted, so a diff shows only changed rows.
    lines = [
        json.dumps({"h": h, "v": r["v"], "s": round(r["s"], 9)}) for h, r in sorted(rows.items())
    ]
    return "\n".join(lines) + ("\n" if lines else "")


def history_head(root: pathlib.Path, remote: str) -> str | None:
    """The history branch's commit: the remote's when it has one (fetched), else the
    local branch's; None when neither exists."""
    out = git(root, "ls-remote", "--heads", remote, BRANCH).split() if remote else []
    if out:
        git(
            root,
            "fetch",
            "--quiet",
            "--no-tags",
            remote,
            f"+refs/heads/{BRANCH}:refs/remotes/{remote}/{BRANCH}",
        )
        return out[0]
    r = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "--verify", "--quiet", f"refs/heads/{BRANCH}"],
        capture_output=True,
        text=True,
    )
    return r.stdout.strip() or None


def branch_rows(root: pathlib.Path, sha: str | None) -> dict[str, dict]:
    if not sha:
        return {}
    r = subprocess.run(
        ["git", "-C", str(root), "show", f"{sha}:{FILE}"], capture_output=True, text=True
    )
    if r.returncode:  # the branch exists but has no vectors yet
        return {}
    return parse(r.stdout, f"{BRANCH}:{FILE}")


def pull(root: pathlib.Path, store: pathlib.Path, remote: str = "origin") -> tuple[int, int]:
    """Merge the branch's vectors into the local store. Returns (added, total)."""
    local = parse(store.read_text(), str(store)) if store.exists() else {}
    theirs = branch_rows(root, history_head(root, remote))
    merged = theirs | local
    if merged != local:
        store.parent.mkdir(parents=True, exist_ok=True)
        tmp = store.with_suffix(".tmp")
        tmp.write_text(render(merged))
        tmp.replace(store)
    return len(merged) - len(local), len(merged)


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("action", choices=["pull", "push"])
    ap.add_argument("--remote", default="origin")
    args = ap.parse_args()
    from beril_wiki.stages.search_vectors import STORE

    if args.action == "push":
        print(
            "search_data: `push` is retired; vectors are committed to the history branch by "
            "`beril_wiki.publish.artifact push` (scripts/publish_artifact.sh)",
            file=sys.stderr,
        )
        return 1
    try:
        added, total = pull(ROOT, STORE, args.remote)
        print(f"search_data: pulled {added} vector(s) from {BRANCH}; {total} in the local store")
        return 0
    except SearchDataError as exc:
        # In CI a build without the vectors would publish meaning search half-broken, so fail it.
        print(
            f"[{'ERROR' if os.environ.get('CI') else 'WARN'}] search_data: {exc}", file=sys.stderr
        )
        return 1 if os.environ.get("CI") else 0


if __name__ == "__main__":
    raise SystemExit(main())
