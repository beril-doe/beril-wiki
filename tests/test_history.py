"""The history branch records every push; rollback moves the pointer and restores."""

from __future__ import annotations

import fcntl
import json
import pathlib
import subprocess
from pathlib import Path

import pytest

from beril_wiki.publish import artifact as A
from beril_wiki.publish import history as H


def run(*args: str, cwd) -> str:
    return subprocess.run(args, cwd=cwd, check=True, capture_output=True, text=True).stdout


def checkout(tmp_path: Path) -> Path:
    """A working checkout on `main` with a committed wiki, as the curator host has."""
    repo = tmp_path / "repo"
    repo.mkdir()
    run("git", "init", "--quiet", "-b", "main", str(repo), cwd=tmp_path)
    for k, v in (("user.name", "t"), ("user.email", "t@example.org")):
        run("git", "config", k, v, cwd=repo)
    (repo / ".gitignore").write_text("/search/\n/staging/\n/.agentic/\n")
    for rel, body in {
        "wiki/sources/demo__REPORT.md": "# demo v1\n",
        "wiki/concepts/x.md": "# x v1\n",
        "state/agentic.json": json.dumps({"fingerprint": "f1"}),
        "corpus/manifest.json": json.dumps({"hub": {"next_since": "t1"}, "projects": {}}),
        "corpus/projects/demo/REPORT.md": "# demo v1\n",
        "search/section-vectors.jsonl": "",
    }.items():
        (repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (repo / rel).write_text(body)
    run("git", "add", ".", cwd=repo)
    run("git", "commit", "--quiet", "-m", "main", cwd=repo)
    return repo


def site_for(repo: Path, body: str) -> Path:
    site = repo / "quartz/public"
    site.mkdir(parents=True, exist_ok=True)
    (site / "index.html").write_text(body)
    return site


def gate(site: Path) -> dict:
    return {
        "ran_at": "2026-11-13T00:00:00+00:00",
        "site_digest": A.site_digest(site),
        "corpus_digest": A.corpus_digest(site.parents[1]),
        "results": {name: {"passed": True, "output": ""} for name in A.GATES},
    }


def test_record_commits_the_trees_without_touching_main(tmp_path):
    repo = checkout(tmp_path)
    head = run("git", "rev-parse", "HEAD", cwd=repo).strip()
    (repo / "wiki/concepts/x.md").write_text("# x v2 (uncommitted on main)\n")
    (repo / "search/section-vectors.jsonl").write_text('{"h": "x"}\n')
    commit = H.record(repo, "v2")
    assert run("git", "rev-parse", "HEAD", cwd=repo).strip() == head  # main untouched
    assert run("git", "rev-parse", "artifact/v2", cwd=repo).strip() == commit
    assert run("git", "rev-parse", H.BRANCH, cwd=repo).strip() == commit
    tracked = run("git", "ls-tree", "-r", "--name-only", commit, cwd=repo).split()
    assert set(tracked) == {
        "wiki/sources/demo__REPORT.md",
        "wiki/concepts/x.md",
        "state/agentic.json",
        "corpus/manifest.json",
        "corpus/projects/demo/REPORT.md",
        "search/section-vectors.jsonl",
    }
    assert (
        run("git", "show", f"{commit}:wiki/concepts/x.md", cwd=repo)
        == "# x v2 (uncommitted on main)\n"
    )
    # main's index still shows the file as modified, not staged.
    assert "M wiki/concepts/x.md" in run("git", "status", "--porcelain", cwd=repo)
    # The next record chains onto the branch; the same id cannot be recorded twice.
    second = H.record(repo, "v3")
    assert run("git", "rev-parse", f"{second}^", cwd=repo).strip() == commit
    with pytest.raises(H.HistoryError, match="already exists"):
        H.record(repo, "v3")


def test_a_fresh_clone_chains_its_record_onto_the_remote_history(tmp_path):
    repo = checkout(tmp_path)
    remote = tmp_path / "remote.git"
    # -b main: with git's default init branch unset (CI), a bare repo's HEAD names
    # master, and a clone of it checks nothing out, so wiki/ would not exist.
    run("git", "init", "--quiet", "--bare", "-b", "main", str(remote), cwd=tmp_path)
    run("git", "remote", "add", "origin", str(remote), cwd=repo)
    first = H.record(repo, "A")
    run("git", "push", "--quiet", "origin", "main", H.BRANCH, cwd=repo)
    clone = tmp_path / "clone"
    run("git", "clone", "--quiet", str(remote), str(clone), cwd=tmp_path)
    for k, v in (("user.name", "t"), ("user.email", "t@example.org")):
        run("git", "config", k, v, cwd=clone)
    assert H.ref(clone, f"refs/heads/{H.BRANCH}") is None  # only origin/history
    (clone / "wiki/concepts/x.md").write_text("# x v2\n")
    second = H.record(clone, "B")
    assert run("git", "rev-parse", f"{second}^", cwd=clone).strip() == first
    run("git", "push", "--quiet", "origin", H.BRANCH, cwd=clone)  # a fast-forward
    assert run("git", "rev-parse", H.BRANCH, cwd=repo).strip() == first
    run("git", "fetch", "--quiet", "origin", cwd=repo)
    assert run("git", "rev-parse", f"origin/{H.BRANCH}", cwd=repo).strip() == second


def test_push_records_history_and_rollback_restores_the_checkout(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    store, keys = A.DirStore(tmp_path / "bucket"), A.Keys("wiki")
    site = site_for(repo, "A")
    first = A.push(store, keys, repo, site, "A", gate=gate(site))
    assert first["history_commit"] == run("git", "rev-parse", "artifact/A", cwd=repo).strip()
    # A later promotion changes every tree, then is published as B.
    (repo / "wiki/sources/demo__REPORT.md").write_text("# demo v2\n")
    (repo / "wiki/concepts/y.md").write_text("# y\n")
    (repo / "state/agentic.json").write_text(json.dumps({"fingerprint": "f2"}))
    (repo / "corpus/manifest.json").write_text(json.dumps({"hub": {"next_since": "t2"}}))
    (repo / "corpus/projects/demo/REPORT.md").write_text("# demo v2\n")
    (repo / "corpus/projects/later/REPORT.md").parent.mkdir()
    (repo / "corpus/projects/later/REPORT.md").write_text("# later\n")
    (repo / "search/section-vectors.jsonl").write_text('{"h": "b"}\n')
    site_for(repo, "B")
    A.push(store, keys, repo, site, "B", gate=gate(site))
    assert A.current(store, keys)["id"] == "B"

    result = A.rollback(store, keys, repo, "A")
    assert A.current(store, keys)["id"] == "A" and result["previous"] == "B"
    assert result["restored_commit"] == first["history_commit"]
    assert (repo / "wiki/sources/demo__REPORT.md").read_text() == "# demo v1\n"
    assert not (repo / "wiki/concepts/y.md").exists()
    assert json.loads((repo / "state/agentic.json").read_text()) == {"fingerprint": "f1"}
    assert json.loads((repo / "corpus/manifest.json").read_text())["hub"] == {"next_since": "t1"}
    assert (repo / "corpus/projects/demo/REPORT.md").read_text() == "# demo v1\n"
    assert not (repo / "corpus/projects/later").exists()
    assert (repo / "search/section-vectors.jsonl").read_text() == ""
    # The site build and main's HEAD are not what rollback restores.
    assert (site / "index.html").read_text() == "B"
    assert run("git", "rev-parse", "--abbrev-ref", "HEAD", cwd=repo).strip() == "main"


def test_a_failed_restore_puts_the_checkout_back_and_leaves_current_alone(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    store, keys = A.DirStore(tmp_path / "bucket"), A.Keys("wiki")
    site = site_for(repo, "A")
    A.push(store, keys, repo, site, "A", gate=gate(site))
    (repo / "wiki/concepts/x.md").write_text("# x v2\n")
    (repo / "corpus/projects/demo/REPORT.md").write_text("# demo v2\n")
    (repo / "state/agentic.json").write_text(json.dumps({"fingerprint": "f2"}))
    site_for(repo, "B")
    A.push(store, keys, repo, site, "B", gate=gate(site))
    live = {p.relative_to(repo): p.read_text() for p in repo.rglob("*.md")}
    rename = H.os.rename
    failures = ["disk full"]

    def failing(src, dst):
        # Placing corpus/ fails once: wiki/ and state/ are already swapped by then.
        if pathlib.Path(dst) == repo / "corpus" and failures:
            raise OSError(failures.pop())
        rename(src, dst)

    monkeypatch.setattr(H.os, "rename", failing)
    with pytest.raises(A.ArtifactError, match="put back: disk full"):
        A.rollback(store, keys, repo, "A")
    assert {p.relative_to(repo): p.read_text() for p in repo.rglob("*.md")} == live
    assert json.loads((repo / "state/agentic.json").read_text()) == {"fingerprint": "f2"}
    assert A.current(store, keys)["id"] == "B"
    assert list(repo.glob(".restore.*")) == []
    monkeypatch.setattr(H.os, "rename", rename)
    assert A.rollback(store, keys, repo, "A")["id"] == "A"
    assert (repo / "wiki/concepts/x.md").read_text() == "# x v1\n"


def test_rollback_refuses_without_a_tag_or_while_a_run_holds_the_lock(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    store, keys = A.DirStore(tmp_path / "bucket"), A.Keys("wiki")
    site = site_for(repo, "A")
    A.push(store, keys, repo, site, "A", gate=gate(site), history=False)
    with pytest.raises(A.ArtifactError, match="no history tag"):
        A.rollback(store, keys, repo, "A")
    assert A.current(store, keys)["id"] == "A"  # the pointer did not move either
    H.record(repo, "A")
    (repo / ".agentic").mkdir()
    with (repo / ".agentic/lock").open("a") as held:
        fcntl.flock(held, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with pytest.raises(A.ArtifactError, match="holds .agentic/lock"):
            A.rollback(store, keys, repo, "A")
    assert A.rollback(store, keys, repo, "A")["id"] == "A"


def test_push_refuses_without_passing_gates_on_this_site(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    store, keys = A.DirStore(tmp_path / "bucket"), A.Keys("wiki")
    site = site_for(repo, "A")
    with pytest.raises(A.ArtifactError, match="no gate results"):
        A.push(store, keys, repo, site, "A", gate=None)
    failed = gate(site)
    failed["results"]["check_site"]["passed"] = False
    with pytest.raises(A.ArtifactError, match="gate\\(s\\) failed: check_site"):
        A.push(store, keys, repo, site, "A", gate=failed)
    stale = gate(site)
    (site / "index.html").write_text("edited after the gates ran")
    with pytest.raises(A.ArtifactError, match="different build"):
        A.push(store, keys, repo, site, "A", gate=stale)
    # The record is bound to the packed sources too: a manual push of a stale build
    # must not serve site A with sources B.
    moved_on = gate(site)
    monkeypatch.setattr(A, "corpus_files", lambda r: {"corpus/sources/demo__REPORT.md": b"B"})
    with pytest.raises(A.ArtifactError, match="different sources"):
        A.push(store, keys, repo, site, "A", gate=moved_on)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    assert not store.exists(keys.current)  # current never moved
    ok = A.push(store, keys, repo, site, "A", gate=gate(site), history=False)
    manifest = json.loads(store.get(keys.manifest(ok["id"])))
    assert all(manifest["gates"][name] is True for name in A.GATES)
    assert manifest["gates"]["site_digest"] == A.site_digest(site)


def test_a_promotion_history_cannot_record_is_not_made_live(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: {})
    store, keys = A.DirStore(tmp_path / "bucket"), A.Keys("wiki")
    site = site_for(repo, "A")
    A.push(store, keys, repo, site, "A", gate=gate(site))
    site_for(repo, "B")
    H.record(repo, "B")  # the tag exists already: record() will refuse
    with pytest.raises(A.ArtifactError, match="history not recorded.*tag artifact/B"):
        A.push(store, keys, repo, site, "B", gate=gate(site))
    assert A.current(store, keys)["id"] == "A"
    assert store.exists(keys.tarball("B"))  # uploaded, immutable, never current


def test_run_gates_records_each_command(tmp_path, monkeypatch):
    site = tmp_path / "site"
    site.mkdir()
    (site / "index.html").write_text("x")
    monkeypatch.setattr(
        A,
        "gate_commands",
        lambda root, site: {
            "check_strict": ["true"],
            "theme_typecheck": ["false"],
            "check_site": ["sh", "-c", "echo fine"],
        },
    )
    result = A.run_gates(tmp_path, site)
    assert result["results"]["check_strict"]["passed"] is True
    assert result["results"]["theme_typecheck"]["passed"] is False
    assert result["results"]["check_site"] == {"passed": True, "output": "fine"}
    assert A.gates_passed(result) == ["theme_typecheck"]
    assert result["site_digest"] == A.site_digest(site)
    assert result["corpus_digest"] == A.corpus_digest(tmp_path)


def test_restore_holds_the_curator_lock_for_its_whole_duration(tmp_path, monkeypatch):
    repo = checkout(tmp_path)
    H.record(repo, "A")
    seen: list[bool] = []
    original = H._restore

    def observing(root, commit, tag):
        seen.append(H.locked_by_a_run(root))  # True only while restore holds the flock
        return original(root, commit, tag)

    monkeypatch.setattr(H, "_restore", observing)
    H.restore(repo, "A")
    assert seen == [True]
    assert not H.locked_by_a_run(repo)  # released afterwards
    with H.held_lock(repo):
        with pytest.raises(H.HistoryError, match="holds .agentic/lock"):
            H.restore(repo, "A")
