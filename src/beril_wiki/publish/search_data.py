#!/usr/bin/env python3
"""Keep the section vectors on the `search-data` branch, out of main's history.

The vectors (about 8 MB) are rebuilt whenever page text changes, so committing
them to main would add megabytes to its history on every compile. They live on
an orphan branch that always holds one commit with one file,
`section-vectors.jsonl`; each push replaces that commit.

    uv run python -m beril_wiki.publish.search_data pull
    uv run python -m beril_wiki.publish.search_data push [--prune]

`pull` merges the branch's vectors into the local store, `search/section-vectors.jsonl`.
scripts/build_quartz.sh runs it before indexing, in CI and locally, so a build
only embeds sections that have no vector anywhere. `push` merges the local
store into the branch, pushes it, and dispatches the Pages workflow on main so
the site picks the vectors up; a push to a branch with no workflow of its own
triggers nothing by itself. Both merge rather than replace, so a push
from a feature branch never drops vectors the live site still uses. `--prune`
drops vectors no section of the current build uses; run it from an up-to-date
main.
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

BRANCH = "search-data"
FILE = "section-vectors.jsonl"
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


def remote_head(root: pathlib.Path, remote: str) -> str | None:
    """The branch's commit on the remote, fetched; None when the branch does not exist yet."""
    out = git(root, "ls-remote", "--heads", remote, BRANCH).split()
    if not out:
        return None
    git(
        root,
        "fetch",
        "--quiet",
        "--no-tags",
        remote,
        f"+refs/heads/{BRANCH}:refs/remotes/{remote}/{BRANCH}",
    )
    return out[0]


def remote_rows(root: pathlib.Path, sha: str | None) -> dict[str, dict]:
    return parse(git(root, "show", f"{sha}:{FILE}"), f"{BRANCH}:{FILE}") if sha else {}


def pull(root: pathlib.Path, store: pathlib.Path, remote: str = "origin") -> tuple[int, int]:
    """Merge the branch's vectors into the local store. Returns (added, total)."""
    local = parse(store.read_text(), str(store)) if store.exists() else {}
    theirs = remote_rows(root, remote_head(root, remote))
    merged = theirs | local
    if merged != local:
        store.parent.mkdir(parents=True, exist_ok=True)
        tmp = store.with_suffix(".tmp")
        tmp.write_text(render(merged))
        tmp.replace(store)
    return len(merged) - len(local), len(merged)


def push(
    root: pathlib.Path,
    store: pathlib.Path,
    remote: str = "origin",
    prune_to: set[str] | None = None,
) -> str:
    """Merge the local store into the branch and push it as the branch's only commit."""
    if not store.exists():
        raise SearchDataError(
            f"{store} not found: run scripts/build_quartz.sh with CBORG_API_KEY set"
        )
    local = parse(store.read_text(), str(store))
    head = remote_head(root, remote)
    merged = remote_rows(root, head) | local
    if prune_to is not None:
        missing = prune_to - merged.keys()
        if missing:
            raise SearchDataError(
                f"refusing to prune: {len(missing)} current section(s) have no vector yet"
            )
        merged = {h: r for h, r in merged.items() if h in prune_to}
    if head and merged == remote_rows(root, head):
        return f"{BRANCH} is up to date ({len(merged)} vectors)"
    blob = git(root, "hash-object", "-w", "--stdin", input=render(merged).encode()).strip()
    tree = git(root, "mktree", input=f"100644 blob {blob}\t{FILE}\n".encode()).strip()
    commit = git(
        root, "commit-tree", tree, "-m", f"Section vectors: {len(merged)} sections"
    ).strip()
    # One commit with no parent, so the branch never accumulates old stores. The lease
    # refuses the push if someone else pushed in the meantime; pull and push again.
    lease = f"--force-with-lease=refs/heads/{BRANCH}:{head or ''}"
    git(root, "push", "--quiet", lease, remote, f"{commit}:refs/heads/{BRANCH}")
    return f"pushed {len(merged)} vectors to {BRANCH} ({commit[:8]})"


def redeploy(root: pathlib.Path) -> str:
    """Rebuild the live site from main with the new vectors."""
    cmd = ["gh", "workflow", "run", "pages.yml", "--ref", "main"]
    try:
        r = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    except FileNotFoundError:
        r = None
    if r is None or r.returncode:
        why = "gh is not installed" if r is None else r.stderr.strip()
        return f"[WARN] could not redeploy ({why}); run `{' '.join(cmd)}`"
    return "redeploying the site from main"


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("action", choices=["pull", "push"])
    ap.add_argument("--prune", action="store_true", help="push only vectors the current build uses")
    ap.add_argument("--remote", default="origin")
    ap.add_argument("--no-deploy", action="store_true", help="push without redeploying the site")
    args = ap.parse_args()
    from beril_wiki.stages.search_vectors import INPUT, STORE

    try:
        if args.action == "pull":
            added, total = pull(ROOT, STORE, args.remote)
            print(
                f"search_data: pulled {added} vector(s) from {BRANCH}; {total} in the local store"
            )
            return 0
        prune_to = None
        if args.prune:
            if not INPUT.exists():
                raise SearchDataError(f"{INPUT} not found: run scripts/build_quartz.sh first")
            prune_to = {r["h"] for r in json.loads(INPUT.read_text())}
        result = push(ROOT, STORE, args.remote, prune_to)
        print(f"search_data: {result}")
        if result.startswith("pushed") and not args.no_deploy:
            print(f"search_data: {redeploy(ROOT)}")
        return 0
    except SearchDataError as exc:
        # In CI a build without the vectors would publish meaning search half-broken, so fail it.
        print(
            f"[{'ERROR' if os.environ.get('CI') else 'WARN'}] search_data: {exc}", file=sys.stderr
        )
        return 1 if (args.action == "push" or os.environ.get("CI")) else 0


if __name__ == "__main__":
    raise SystemExit(main())
