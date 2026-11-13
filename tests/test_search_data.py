"""Vectors are read from the history branch and merged into the local store, never lost."""

from __future__ import annotations

import base64
import json
import subprocess

import pytest

from beril_wiki.publish import history as H
from beril_wiki.publish import search_data as sd


def row(h: str, fill: int = 1) -> str:
    return json.dumps({"h": h, "v": base64.b64encode(bytes([fill]) * sd.DIM).decode(), "s": 0.01})


def run(*args: str, cwd) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repos(tmp_path):
    """A bare remote and two clones of it, as the curator host and a maintainer."""
    remote = tmp_path / "remote.git"
    run("git", "init", "--quiet", "--bare", str(remote), cwd=tmp_path)
    clones = []
    for name in ("a", "b"):
        c = tmp_path / name
        run("git", "init", "--quiet", str(c), cwd=tmp_path)
        run("git", "remote", "add", "origin", str(remote), cwd=c)
        for k, v in (("user.name", "t"), ("user.email", "t@example.org")):
            run("git", "config", k, v, cwd=c)
        (c / "wiki").mkdir()
        (c / "wiki/index.md").write_text("# w\n")
        clones.append(c)
    return remote, clones


def publish_vectors(repo, artifact_id: str, *hashes: str) -> None:
    """What `artifact push` does for the vectors: record them on history and push."""
    store = repo / sd.FILE
    store.parent.mkdir(exist_ok=True)
    store.write_text("".join(row(h) + "\n" for h in hashes))
    H.record(repo, artifact_id)
    run("git", "push", "--quiet", "origin", H.BRANCH, cwd=repo)


def test_pull_reads_the_history_branch_and_merges(repos):
    remote, (a, b) = repos
    publish_vectors(a, "v1", "h1")
    store = b / "store.jsonl"
    assert sd.pull(b, store) == (1, 1)
    # Local rows the branch lacks survive; branch rows are added.
    store.write_text(store.read_text() + row("h2") + "\n")
    publish_vectors(a, "v2", "h1", "h3")
    assert sd.pull(b, store) == (1, 3)
    assert set(sd.parse(store.read_text(), "t")) == {"h1", "h2", "h3"}
    assert run("git", "rev-list", "--count", H.BRANCH, cwd=remote).strip() == "2"


def test_pull_falls_back_to_the_local_history_branch(repos):
    _, (a, _) = repos
    store = a / sd.FILE
    store.parent.mkdir()
    store.write_text(row("h1") + "\n")
    H.record(a, "v1")  # recorded but never pushed
    store.unlink()
    assert sd.pull(a, store) == (1, 1)


def test_a_malformed_branch_store_is_refused(repos):
    _, (a, _) = repos
    store = a / sd.FILE
    store.parent.mkdir()
    store.write_text(json.dumps({"h": "h1", "v": "AAAA", "s": 0.1}) + "\n")
    H.record(a, "v1")
    with pytest.raises(sd.SearchDataError, match="768-dimension"):
        sd.pull(a, a / "fresh.jsonl")


def test_pull_without_the_branch_keeps_the_local_store(repos):
    _, (a, _) = repos
    store = a / "store.jsonl"
    store.write_text(row("h1") + "\n")
    assert sd.pull(a, store) == (0, 1)
    assert set(sd.parse(store.read_text(), "t")) == {"h1"}
