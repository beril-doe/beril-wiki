"""Model-free scope check for a publisher branch (`wiki/<id>`).

    uv run python scripts/check_update.py --base origin/main --head HEAD [--branch wiki/ID]

The branch comes from `--branch` or `GITHUB_HEAD_REF`. A branch that does not start with
`wiki/` passes, so maintainer and code PRs keep today's behaviour. On a publisher branch
the project id is the rest of the name, and the check fails when:

- `--base` is not an ancestor of `--head`;
- `corpus/` changes outside `corpus/projects/ID/` and the `ID` entry of `manifest.json`;
- `wiki/sources`, `wiki/summaries` or `wiki/figures` change outside `ID`;
- `state/{headlines,novelty,gists,outcomes}.json` change an entry that belongs to no
  project of the branch.

`links.json` and `shared.json` relate findings across projects, as concept pages do, so a
new project may change any of their entries. `followups.json` and `directions.json` key
their entries by question or topic slug, which names no project. None of the four is checked.

Exit 0 when the branch is in scope, 1 with one line per violation otherwise.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Callable

PREFIX = "wiki/"
ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")
FINDING = re.compile(r"^(.+)--[0-9a-f]+$")


def git(*args: str) -> str:
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def show(ref: str, path: str) -> object:
    """Parsed JSON of `path` at `ref`; an absent file reads as empty."""
    try:
        text = git("show", f"{ref}:{path}")
    except subprocess.CalledProcessError:
        return {}
    return json.loads(text)


def project_of(finding: str) -> str:
    m = FINDING.match(finding)
    return m.group(1) if m else finding


def changed_keys(base: dict, head: dict) -> set[str]:
    return {k for k in base.keys() | head.keys() if base.get(k) != head.get(k)}


def by_key(ids: set[str]) -> Callable[[dict, dict], list[str]]:
    """Entries keyed by project id (headlines) or by `<project>--<hash>` (finding records)."""

    def check(base: dict, head: dict) -> list[str]:
        return [k for k in sorted(changed_keys(base, head)) if project_of(k) not in ids]

    return check


def corpus_path(path: str, ids: set[str]) -> bool:
    parts = path.split("/")
    return len(parts) > 2 and parts[1] == "projects" and parts[2] in ids and len(parts) > 3


def wiki_path(path: str, ids: set[str]) -> bool:
    parts = path.split("/")
    if len(parts) < 3:
        return False
    if parts[1] == "figures":
        return len(parts) > 3 and parts[2] in ids
    return len(parts) == 3 and re.sub(r"(__REPORT)?\.md$", "", parts[2]) in ids


def manifest_stale(base: object, head: object, ids: set[str]) -> list[str]:
    if not isinstance(base, dict) or not isinstance(head, dict):
        return ["corpus/manifest.json is not a JSON object"]
    bad = [
        k
        for k in sorted(base.keys() | head.keys())
        if k != "projects" and base.get(k) != head.get(k)
    ]
    bp, hp = base.get("projects", {}), head.get("projects", {})
    bad += [f"projects.{k}" for k in sorted(changed_keys(bp, hp)) if k not in ids]
    return bad


def violations(base: str, head: str, ids: set[str]) -> list[str]:
    out: list[str] = []
    if subprocess.run(["git", "merge-base", "--is-ancestor", base, head]).returncode != 0:
        out.append(f"{base} is not an ancestor of {head}; rebase the branch onto it")
    changed = git("diff", "--name-only", "--no-renames", "-z", base, head).split("\0")
    for path in sorted(p for p in changed if p):
        if path == "corpus/manifest.json":
            out += [
                f"corpus/manifest.json: {k} is outside {sorted(ids)}"
                for k in manifest_stale(show(base, path), show(head, path), ids)
            ]
        elif path.startswith("corpus/") and not corpus_path(path, ids):
            out.append(f"{path} is outside corpus/projects/{'|'.join(sorted(ids))}/")
        elif re.match(r"wiki/(sources|summaries|figures)/", path) and not wiki_path(path, ids):
            out.append(f"{path} belongs to a project outside {sorted(ids)}")
    checks = {
        "headlines": by_key(ids),
        "novelty": by_key(ids),
        "gists": by_key(ids),
        "outcomes": by_key(ids),
    }
    for name, check in checks.items():
        path = f"state/{name}.json"
        if path not in changed:
            continue
        b, h = show(base, path), show(head, path)
        if not isinstance(b, dict) or not isinstance(h, dict):
            out.append(f"{path} is not a JSON object")
            continue
        out += [
            f"{path}: entry {k} belongs to a project outside {sorted(ids)}" for k in check(b, h)
        ]
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument(
        "--base", required=True, help="ref the branch must descend from, e.g. origin/main"
    )
    ap.add_argument("--head", required=True, help="ref of the branch tip")
    ap.add_argument("--branch", help="branch name; default $GITHUB_HEAD_REF")
    args = ap.parse_args(argv)
    branch = args.branch or os.environ.get("GITHUB_HEAD_REF", "")
    if not branch.startswith(PREFIX):
        print(f"{branch or 'no branch'}: not a publisher branch, nothing to check")
        return 0
    project = branch.removeprefix(PREFIX)
    if not ID.match(project):
        print(f"{branch}: {project!r} is not a project id")
        return 1
    found = violations(args.base, args.head, {project})
    for line in found:
        print(line)
    return 1 if found else 0


if __name__ == "__main__":
    sys.exit(main())
