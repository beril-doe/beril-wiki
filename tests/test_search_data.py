"""The search-data branch: vectors travel through an orphan branch, merged, never lost."""

from __future__ import annotations

import base64
import json
import subprocess

import pytest

from beril_wiki.publish import search_data as sd


def row(h: str, fill: int = 1) -> str:
    return json.dumps({"h": h, "v": base64.b64encode(bytes([fill]) * sd.DIM).decode(), "s": 0.01})


def run(*args: str, cwd) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


@pytest.fixture
def repos(tmp_path):
    """A bare remote and two clones of it, as two maintainers' checkouts."""
    remote = tmp_path / "remote.git"
    run("git", "init", "--quiet", "--bare", str(remote), cwd=tmp_path)
    clones = []
    for name in ("a", "b"):
        c = tmp_path / name
        run("git", "init", "--quiet", str(c), cwd=tmp_path)
        run("git", "remote", "add", "origin", str(remote), cwd=c)
        for k, v in (("user.name", "t"), ("user.email", "t@example.org")):
            run("git", "config", k, v, cwd=c)
        clones.append(c)
    return remote, clones


def branch_rows(remote) -> dict:
    return sd.parse(run("git", "show", f"{sd.BRANCH}:{sd.FILE}", cwd=remote), "test")


def test_push_creates_a_one_commit_orphan_branch(repos):
    remote, (a, _) = repos
    store = a / "search/section-vectors.jsonl"
    store.parent.mkdir()
    store.write_text(row("h1") + "\n")
    assert "pushed 1 vectors" in sd.push(a, store)
    assert set(branch_rows(remote)) == {"h1"}
    store.write_text(row("h1") + "\n" + row("h2") + "\n")
    sd.push(a, store)
    # Each push replaces the branch's only commit, so old stores never pile up.
    assert run("git", "rev-list", "--count", sd.BRANCH, cwd=remote).strip() == "1"
    assert set(branch_rows(remote)) == {"h1", "h2"}
    assert "up to date" in sd.push(a, store)


def test_pull_and_push_merge_instead_of_replacing(repos):
    remote, (a, b) = repos
    sa, sb = a / "store.jsonl", b / "store.jsonl"
    sa.write_text(row("h1") + "\n")
    sd.push(a, sa)
    # The second maintainer pulls h1, embeds h2 locally, and pushes: both survive.
    assert sd.pull(b, sb) == (1, 1)
    sb.write_text(sb.read_text() + row("h2") + "\n")
    sd.push(b, sb)
    # The first maintainer, who never saw h2, pushes h3: h2 is merged, not dropped.
    sa.write_text(row("h1") + "\n" + row("h3") + "\n")
    sd.push(a, sa)
    assert set(branch_rows(remote)) == {"h1", "h2", "h3"}


def test_prune_keeps_only_current_sections_and_refuses_gaps(repos):
    remote, (a, _) = repos
    store = a / "store.jsonl"
    store.write_text(row("h1") + "\n" + row("old") + "\n")
    sd.push(a, store)
    with pytest.raises(sd.SearchDataError, match="no vector yet"):
        sd.push(a, store, prune_to={"h1", "h9"})
    sd.push(a, store, prune_to={"h1"})
    assert set(branch_rows(remote)) == {"h1"}


def test_a_malformed_store_is_refused(repos):
    _, (a, _) = repos
    store = a / "store.jsonl"
    store.write_text(json.dumps({"h": "h1", "v": "AAAA", "s": 0.1}) + "\n")
    with pytest.raises(sd.SearchDataError, match="768-dimension"):
        sd.push(a, store)


def test_pull_without_the_branch_keeps_the_local_store(repos):
    _, (a, _) = repos
    store = a / "store.jsonl"
    store.write_text(row("h1") + "\n")
    assert sd.pull(a, store) == (0, 1)
    assert set(sd.parse(store.read_text(), "t")) == {"h1"}
