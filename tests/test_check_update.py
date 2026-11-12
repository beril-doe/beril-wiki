"""Scope check for publisher branches, run on throwaway git repos."""

import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

spec = importlib.util.spec_from_file_location(
    "check_update", Path(__file__).parent.parent / "scripts" / "check_update.py"
)
assert spec and spec.loader
check_update = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check_update)


def sh(repo, *args):
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True)


def write(repo, rel, text):
    path = repo / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text if isinstance(text, str) else json.dumps(text))


@pytest.fixture
def repo(tmp_path, monkeypatch):
    sh(tmp_path, "init", "-q", "-b", "main")
    sh(tmp_path, "config", "user.email", "t@example.com")
    sh(tmp_path, "config", "user.name", "t")
    write(
        tmp_path,
        "corpus/manifest.json",
        {"version": 1, "shared": {}, "projects": {"old": {"digest": "1"}}},
    )
    write(tmp_path, "corpus/projects/old/REPORT.md", "old")
    write(tmp_path, "wiki/summaries/old__REPORT.md", "old")
    write(tmp_path, "state/novelty.json", {"old--aaaa1111": {"label": "x"}})
    write(tmp_path, "state/links.json", {"candidates": {}, "links": []})
    sh(tmp_path, "add", "-A")
    sh(tmp_path, "commit", "-qm", "base")
    sh(tmp_path, "switch", "-qc", "wiki/new")
    monkeypatch.chdir(tmp_path)
    return tmp_path


def commit(repo):
    sh(repo, "add", "-A")
    sh(repo, "commit", "-qm", "work")


def add_new_project(repo):
    write(
        repo,
        "corpus/manifest.json",
        {"version": 1, "shared": {}, "projects": {"old": {"digest": "1"}, "new": {"digest": "2"}}},
    )
    write(repo, "corpus/projects/new/REPORT.md", "new")
    write(repo, "wiki/summaries/new__REPORT.md", "new")
    write(repo, "wiki/figures/new/a.png", "png")
    write(
        repo,
        "state/novelty.json",
        {"old--aaaa1111": {"label": "x"}, "new--bbbb2222": {"label": "y"}},
    )
    write(
        repo,
        "state/links.json",
        {
            "candidates": {"pair:new--bbbb2222|old--aaaa1111": {}},
            "links": [{"a": "new--bbbb2222", "b": "old--aaaa1111"}],
        },
    )


def run(capsys, branch="wiki/new"):
    code = check_update.main(["--base", "main", "--head", "HEAD", "--branch", branch])
    return code, capsys.readouterr().out


def test_one_project_branch_passes(repo, capsys):
    add_new_project(repo)
    commit(repo)
    assert run(capsys)[0] == 0


def test_other_projects_summary_edit_fails_naming_it(repo, capsys):
    add_new_project(repo)
    write(repo, "wiki/summaries/old__REPORT.md", "rewritten")
    commit(repo)
    code, out = run(capsys)
    assert code == 1 and "wiki/summaries/old__REPORT.md" in out


def test_other_projects_card_state_and_manifest_entry_fail(repo, capsys):
    add_new_project(repo)
    write(repo, "state/novelty.json", {"old--aaaa1111": {"label": "changed"}, "new--bbbb2222": {}})
    write(
        repo,
        "corpus/manifest.json",
        {"version": 1, "shared": {}, "projects": {"old": {"digest": "9"}, "new": {}}},
    )
    commit(repo)
    code, out = run(capsys)
    assert code == 1 and "novelty.json: entry old--aaaa1111" in out and "projects.old" in out


def test_cross_project_links_and_shared_groups_may_change(repo, capsys):
    # links.py keys reference candidates `ref:<sid>><target>`, which a pair-only parser
    # read as no project; a new finding also moves unrelated pairs and regroups topics.
    add_new_project(repo)
    write(
        repo,
        "state/links.json",
        {
            "candidates": {
                "ref:new__REPORT.md>old": {"relation": "uses its data"},
                "ref:old__REPORT.md>other": {"relation": "extends"},
                "pair:old--aaaa1111|other--cccc3333": {},
            },
            "links": [{"a": "old--aaaa1111", "b": "other--cccc3333", "level": "finding"}],
        },
    )
    write(repo, "state/shared.json", {"g-1": {"projects": ["old", "other"], "input": "k"}})
    commit(repo)
    assert run(capsys) == (0, "")


def test_branch_behind_base_fails(repo, capsys):
    add_new_project(repo)
    commit(repo)
    sh(repo, "switch", "-q", "main")
    write(repo, "README.md", "later")
    commit(repo)
    sh(repo, "switch", "-q", "wiki/new")
    code, out = run(capsys)
    assert code == 1 and "not an ancestor" in out


def test_non_publisher_branch_passes(repo, capsys):
    write(repo, "wiki/summaries/old__REPORT.md", "maintainer edit")
    commit(repo)
    assert run(capsys, branch="fix/typo")[0] == 0
