"""The vendored corpus: the committed copy verifies, and fetch mirrors it exactly."""

import subprocess

import pytest

from beril_wiki import corpus
from beril_wiki.agentic import runner
from beril_wiki.agentic.batch import changed_sources
from beril_wiki.agentic.runtime import WorkflowError
from beril_wiki.stages import fetch


def checkout(tmp_path, projects):
    root = tmp_path / "checkout"
    for rel in corpus.SHARED:
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(f"{rel}\n")
    for pid in projects:
        (root / "projects" / pid / "figures").mkdir(parents=True)
        (root / "projects" / pid / "README.md").write_text(f"# {pid}\n\n## Authors\n- A\n")
        (root / "projects" / pid / "REPORT.md").write_text(f"# {pid}\n![f](figures/f.png)\n")
        (root / "projects" / pid / "figures/f.png").write_bytes(pid.encode())
    subprocess.run(["git", "init", "-q", str(root)], check=True)
    subprocess.run(["git", "-C", str(root), "add", "."], check=True)
    subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "c"],
        check=True,
    )
    return root


def test_committed_corpus_matches_its_manifest():
    assert corpus.verify() == []


def test_verify_names_an_edited_file(tmp_path):
    out = tmp_path / "corpus"
    corpus.import_v1(checkout(tmp_path, ["a", "b"]), out)
    assert corpus.verify(out) == []
    (out / "projects/a/README.md").write_text("edited\n")
    (out / "projects/b/figures/extra.png").write_bytes(b"x")
    assert corpus.verify(out) == [
        "projects/b/figures/extra.png: not in the manifest",
        "projects/a/README.md: hash differs from the manifest",
    ]


def test_fetch_drops_a_report_the_checkout_no_longer_has(tmp_path, monkeypatch):
    src = checkout(tmp_path, ["a", "b"])
    root = tmp_path / "wiki-root"
    (root / "wiki/sources").mkdir(parents=True)
    monkeypatch.setattr(fetch, "CHECKOUT", src)
    fetch.fetch_local(root / "staging")
    for name in ("a__REPORT.md", "b__REPORT.md"):
        (root / "wiki/sources" / name).write_bytes((root / "staging" / name).read_bytes())
    (src / "projects/b/REPORT.md").unlink()
    fetch.fetch_local(root / "staging")
    assert not (root / "staging/b__REPORT.md").exists()
    with pytest.raises(WorkflowError, match="source deletion requires explicit retraction"):
        changed_sources(root)


def test_run_output_figures_are_vendored_and_fetched(tmp_path, monkeypatch):
    src = checkout(tmp_path, ["p"])
    project = src / "projects/p"
    (project / "REPORT.md").write_text("![a](figures/f.png)\n![b](runs/r1/out/figures/b.png)\n")
    run_fig = project / "runs/r1/out/figures/b.png"
    run_fig.parent.mkdir(parents=True)
    run_fig.write_bytes(b"run")
    assert corpus.project_files(project) == [
        "README.md",
        "REPORT.md",
        "figures/f.png",
        "runs/r1/out/figures/b.png",
    ]
    root = tmp_path / "wiki-root"
    monkeypatch.setattr(fetch, "CHECKOUT", src)
    fetch.fetch_local(root / "staging")
    assert (root / "wiki/figures/p/f.png").read_bytes() == b"p"
    assert (root / "wiki/figures/p/runs/r1/out/figures/b.png").read_bytes() == b"run"
    assert "projects/p/runs/r1/out/figures/b.png" in runner.checkout_inputs(src)
