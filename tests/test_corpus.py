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
    assert corpus.verify(out) == ["manifest.json: missing; run import-v1"]
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


def test_run_output_figures_reach_placement_with_their_paths(tmp_path, monkeypatch):
    """Placement saw only `figures/` embeds, and splicing flattened a placed figure to
    its basename, where two runs' figures/b.png would collide."""
    import hashlib

    from beril_wiki.publish import ingest
    from beril_wiki.stages import figures

    root = tmp_path / "wiki-root"
    (root / "wiki/sources").mkdir(parents=True)
    (root / "wiki/sources/p__REPORT.md").write_text(
        "Growth rose.\n\n![Growth](runs/r1/out/figures/b.png)\n\n![Old](figures/f.png)\n"
    )
    for rel, data in (("runs/r1/out/figures/b.png", b"r1"), ("runs/r2/out/figures/b.png", b"r2")):
        (root / "wiki/figures/p" / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / "wiki/figures/p" / rel).write_bytes(data)
    (root / "wiki/figures/p/f.png").write_bytes(b"f")
    monkeypatch.setattr(figures, "ROOT", root)
    monkeypatch.setattr(figures, "STATE", root / "state")
    files = [(f["file"], f["caption"]) for f in figures.build_manifest()["p"]]
    assert files == [("runs/r1/out/figures/b.png", "Growth"), ("figures/f.png", "Old")]
    page = "First.\n\nSecond.\n"
    placed = [
        {
            "project": "p",
            "file": f"runs/{run}/out/figures/b.png",
            "caption": run,
            "after_paragraph": i,
        }
        for i, run in enumerate(("r1", "r2"))
    ]
    entry = {"page_hash": hashlib.sha256(page.encode()).hexdigest()[:16], "placements": placed}
    site = tmp_path / "site"
    spliced = ingest.splice_figures(page, entry, root, site)
    for run in ("r1", "r2"):
        assert f"](../figures/p/runs/{run}/out/figures/b.png)" in spliced
        assert (site / f"figures/p/runs/{run}/out/figures/b.png").read_bytes() == run.encode()
