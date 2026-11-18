"""The vendored corpus: the committed copy verifies, and fetch mirrors it exactly."""

import subprocess
from pathlib import Path

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


@pytest.mark.parametrize("failure", ["missing", "copy", "promote"])
def test_failed_import_preserves_existing_corpus(tmp_path, monkeypatch, failure):
    src = checkout(tmp_path, ["a", "b"])
    out = tmp_path / "corpus"
    corpus.import_v1(src, out)
    before = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
    (src / "projects/a/REPORT.md").write_text("# Replacement\n")
    if failure == "missing":
        (src / corpus.SHARED[0]).unlink()
        error, message = SystemExit, "checkout lacks"
    elif failure == "copy":
        copy = corpus.shutil.copy2

        def fail_copy(source, destination):
            if Path(source).name == "REPORT.md":
                raise OSError("copy failed")
            return copy(source, destination)

        monkeypatch.setattr(corpus.shutil, "copy2", fail_copy)
        error, message = OSError, "copy failed"
    else:
        replace = Path.replace
        failed = False

        def fail_promotion(path, target):
            nonlocal failed
            if Path(target) == out and not failed:
                failed = True
                raise OSError("promotion failed")
            return replace(path, target)

        monkeypatch.setattr(Path, "replace", fail_promotion)
        error, message = OSError, "promotion failed"
    with pytest.raises(error, match=message):
        corpus.import_v1(src, out)
    assert {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()} == before
    assert corpus.verify(out) == []
    assert list(tmp_path.glob(".corpus-import-*")) == []


def test_import_replaces_the_complete_corpus(tmp_path):
    src = checkout(tmp_path, ["a", "b"])
    out = tmp_path / "corpus"
    corpus.import_v1(src, out)
    corpus.shutil.rmtree(src / "projects/b")
    (src / "projects/a/REPORT.md").write_text("# Replacement\n")
    manifest = corpus.import_v1(src, out)
    assert set(manifest["projects"]) == {"a"}
    assert not (out / "projects/b").exists()
    assert (out / "projects/a/REPORT.md").read_text() == "# Replacement\n"
    assert corpus.verify(out) == []


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


@pytest.mark.parametrize(
    "paths",
    [
        ("runs/r1/out/figures/b.png", "runs/r2/out/figures/b.png"),
        ("figures/a/plot.png", "figures/b/plot.png"),
    ],
)
def test_run_output_figures_reach_placement_with_their_paths(tmp_path, monkeypatch, paths):
    """Raw reports and placements preserve figure paths with shared basenames."""
    import hashlib

    from beril_wiki.publish import ingest
    from beril_wiki.stages import figures

    root = tmp_path / "wiki-root"
    (root / "wiki/sources").mkdir(parents=True)
    report = (
        f"Growth rose.\n\n![First]({paths[0]})\n\n![Second]({paths[1]})\n\n![Old](figures/f.png)\n"
    )
    (root / "wiki/sources/p__REPORT.md").write_text(report)
    for rel, data in zip(paths, (b"first", b"second"), strict=True):
        figure = root / "wiki/figures" / corpus.figure_destination("p", rel)
        figure.parent.mkdir(parents=True, exist_ok=True)
        figure.write_bytes(data)
    (root / "wiki/figures/p/f.png").write_bytes(b"f")
    monkeypatch.setattr(figures, "ROOT", root)
    monkeypatch.setattr(figures, "STATE", root / "state")
    files = [(f["file"], f["caption"]) for f in figures.build_manifest()["p"]]
    assert files == [(paths[0], "First"), (paths[1], "Second"), ("figures/f.png", "Old")]
    page = "First.\n\nSecond.\n"
    placed = [
        {
            "project": "p",
            "file": rel,
            "caption": str(i),
            "after_paragraph": i,
        }
        for i, rel in enumerate(paths)
    ]
    entry = {"page_hash": hashlib.sha256(page.encode()).hexdigest()[:16], "placements": placed}
    site = tmp_path / "site"
    spliced = ingest.splice_figures(page, entry, root, site)
    raw_site = tmp_path / "raw-site"
    rewritten = ingest.rewrite_source_figures(report, "p", root, raw_site)
    assert "](../figures/p/f.png)" in rewritten
    assert (raw_site / "figures/p/f.png").read_bytes() == b"f"
    for rel, data in zip(paths, (b"first", b"second"), strict=True):
        destination = corpus.figure_destination("p", rel)
        for text, output in ((spliced, site), (rewritten, raw_site)):
            assert f"](../figures/{destination})" in text
            assert (output / "figures" / destination).read_bytes() == data
