"""Site artifacts: immutable versions in a store, a movable pointer, verified unpacking."""

from __future__ import annotations

import io
import json
import tarfile
from pathlib import Path

import pytest

from beril_wiki.publish import artifact as A


def make_repo(tmp_path: Path) -> tuple[Path, Path]:
    root = tmp_path / "repo"
    site = root / "quartz/public"
    for rel, body in {
        "index.html": "home",
        "a.html": "page a",
        "concepts/x.html": "x",
        "static/search/pages.json": json.dumps({"build": "b1", "pages": []}),
    }.items():
        (site / rel).parent.mkdir(parents=True, exist_ok=True)
        (site / rel).write_text(body)
    (root / "wiki/sources").mkdir(parents=True)
    (root / "wiki/sources/demo__REPORT.md").write_text("# demo\n\nExact text.\n")
    (root / "wiki/findings").mkdir()
    (root / "wiki/findings/demo--1.md").write_text("# F1\n")
    (root / "state").mkdir()
    (root / "state/agentic.json").write_text(
        json.dumps({"fingerprint": "abcdef0123", "revision": "r"})
    )
    return root, site


@pytest.fixture
def store(tmp_path) -> A.DirStore:
    return A.DirStore(tmp_path / "bucket")


def gate(site: Path) -> dict:
    """A gate record showing all three checks passed on exactly this site."""
    return {
        "ran_at": "2026-11-13T00:00:00+00:00",
        "site_digest": A.site_digest(site),
        "results": {name: {"passed": True, "output": ""} for name in A.GATES},
    }


def push(store, keys, root, site, artifact_id, **kw):
    return A.push(store, keys, root, site, artifact_id, gate=gate(site), history=False, **kw)


def test_push_packs_site_and_corpus_and_points_current(tmp_path, store, monkeypatch):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", lambda r: _plain_corpus(r))
    keys = A.Keys("wiki")
    pointer = push(store, keys, root, site, "v1", base_url="localhost:8080/wiki")
    assert pointer["id"] == "v1" and pointer["previous"] is None
    assert store.exists("wiki/site-v1.tar.gz") and store.exists("wiki/site-v1.manifest.json")
    manifest = json.loads(store.get("wiki/site-v1.manifest.json"))
    assert manifest["page_count"] == 3
    assert manifest["agentic"]["fingerprint"] == "abcdef0123"
    assert set(manifest["sources"]) == {"demo__REPORT.md"}
    assert manifest["tarball_sha256"] == A.sha256(store.get("wiki/site-v1.tar.gz"))
    with tarfile.open(fileobj=io.BytesIO(store.get("wiki/site-v1.tar.gz"))) as tar:
        names = set(tar.getnames())
    assert {"manifest.json", "site/index.html", "site/concepts/x.html"} <= names
    assert "corpus/sources/demo__REPORT.md" in names
    assert json.loads(store.get("wiki/current.json")) == pointer


def _plain_corpus(root: Path) -> dict[str, bytes]:
    # Without a full corpus the cards export cannot run; keep the Markdown only.
    return {
        f"corpus/{folder}/{p.name}": p.read_bytes()
        for folder in A.CORPUS_DIRS
        for p in sorted((root / "wiki" / folder).glob("*.md"))
    }


def test_artifacts_are_immutable_and_ids_are_checked(tmp_path, store, monkeypatch):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    keys = A.Keys("wiki")
    push(store, keys, root, site, "v1")
    with pytest.raises(A.ArtifactError, match="immutable"):
        push(store, keys, root, site, "v1")
    with pytest.raises(A.ArtifactError, match="bad artifact id"):
        push(store, keys, root, site, "../v2")
    with pytest.raises(A.ArtifactError, match="no built site"):
        A.push(
            store,
            keys,
            root,
            tmp_path / "empty",
            "v3",
            gate=gate(tmp_path / "empty"),
            history=False,
        )


def test_rollback_moves_the_pointer_only_to_an_existing_artifact(tmp_path, store, monkeypatch):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    keys = A.Keys("wiki")
    push(store, keys, root, site, "v1")
    push(store, keys, root, site, "v2")
    assert A.current(store, keys)["id"] == "v2"
    pointer = A.point(store, keys, "v1")
    assert pointer["id"] == "v1" and pointer["previous"] == "v2"
    assert A.current(store, keys)["id"] == "v1"
    with pytest.raises(A.ArtifactError, match="no artifact v9"):
        A.point(store, keys, "v9")


def test_sync_unpacks_verifies_and_reuses(tmp_path, store, monkeypatch):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    keys = A.Keys("wiki")
    push(store, keys, root, site, "v1")
    site_root = tmp_path / "artifacts"
    artifact_id, where, manifest = A.sync(store, keys, site_root)
    assert artifact_id == "v1" and where == site_root / "site-v1"
    assert (where / "site/index.html").read_text() == "home"
    assert (where / "corpus/sources/demo__REPORT.md").exists()
    assert manifest["page_count"] == 3
    # A second sync finds the unpacked copy whole and downloads nothing.
    calls = []
    original = store.get

    def counting(key):
        calls.append(key)
        return original(key)

    monkeypatch.setattr(store, "get", counting)
    A.sync(store, keys, site_root)
    assert calls == ["wiki/current.json"]
    # A damaged copy is unpacked again.
    (where / "site/a.html").unlink()
    A.sync(store, keys, site_root)
    assert (where / "site/a.html").exists()


def test_sync_refuses_a_tampered_tarball_or_manifest(tmp_path, store, monkeypatch):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    keys = A.Keys("wiki")
    push(store, keys, root, site, "v1")
    good = store.get("wiki/site-v1.tar.gz")
    store.put("wiki/site-v1.tar.gz", good + b"x", "application/gzip")
    with pytest.raises(A.ArtifactError, match="sha256 does not match"):
        A.sync(store, keys, tmp_path / "artifacts")
    assert not (tmp_path / "artifacts/site-v1").exists()
    # A manifest whose id or page count disagrees with the tree is refused too.
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        for name, body in {
            "manifest.json": json.dumps({"id": "v1", "page_count": 7}).encode(),
            "site/index.html": b"home",
        }.items():
            info = tarfile.TarInfo(name)
            info.size = len(body)
            tar.addfile(info, io.BytesIO(body))
    with pytest.raises(A.ArtifactError, match="manifest says 7 pages"):
        A.unpack(buf.getvalue(), tmp_path / "artifacts/site-v1", "v1", None)
    with pytest.raises(A.ArtifactError, match="manifest id"):
        A.unpack(buf.getvalue(), tmp_path / "artifacts/site-v2", "v2", None)


def test_unpack_refuses_members_that_escape(tmp_path):
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        body = b"evil"
        info = tarfile.TarInfo("../outside.txt")
        info.size = len(body)
        tar.addfile(info, io.BytesIO(body))
    with pytest.raises((A.ArtifactError, tarfile.TarError)):
        A.unpack(buf.getvalue(), tmp_path / "artifacts/site-v1", "v1", None)
    assert not (tmp_path / "outside.txt").exists()


def test_store_from_env(tmp_path):
    env = {"WIKI_ARTIFACT_ENDPOINT": f"file://{tmp_path}/bucket", "WIKI_ARTIFACT_PREFIX": "/p/"}
    assert isinstance(A.store_from_env(env), A.DirStore)
    assert A.prefix_from_env(env) == "p"
    assert A.Keys("p").tarball("v1") == "p/site-v1.tar.gz"
    assert A.Keys("").current == "current.json"
    with pytest.raises(A.ArtifactError, match="WIKI_ARTIFACT_BUCKET"):
        A.store_from_env({"WIKI_ARTIFACT_ENDPOINT": "http://minio:9000"})
    assert not A.configured({})


def test_cli_push_and_current(tmp_path, monkeypatch, capsys):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    monkeypatch.setenv("WIKI_ARTIFACT_ENDPOINT", f"file://{tmp_path}/bucket")
    monkeypatch.setenv("WIKI_ARTIFACT_PREFIX", "wiki")
    assert A.main(["push", "--root", str(root), "--id", "v1", "--no-history"]) == 1  # no gates
    (root / "quartz/gate-results.json").write_text(json.dumps(gate(site)))
    assert A.main(["push", "--root", str(root), "--id", "v1", "--no-history"]) == 0
    assert A.main(["current"]) == 0
    assert '"id": "v1"' in capsys.readouterr().out
    assert A.main(["rollback", "--to", "v9"]) == 1
    assert "no history tag for v9" in capsys.readouterr().err


def test_corpus_tree_is_written_for_the_image(tmp_path, monkeypatch, capsys):
    root, _ = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    assert A.main(["corpus", str(tmp_path / "corpus"), "--root", str(root)]) == 0
    assert (tmp_path / "corpus/sources/demo__REPORT.md").exists()
    assert (tmp_path / "corpus/findings/demo--1.md").exists()


def test_footer_link_is_root_relative():
    from beril_wiki.publish.quartz_config import site_path

    assert site_path("beril.kbase.us/wiki") == "/wiki"
    assert site_path("beril-doe.org/beril-wiki/") == "/beril-wiki"
    assert site_path("localhost:8080") == ""
