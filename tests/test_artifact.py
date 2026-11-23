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
        "corpus_digest": A.corpus_digest(site.parents[1]),
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
            gate=gate(tmp_path / "empty") | {"corpus_digest": A.corpus_digest(root)},
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


class FakeS3:
    """Answers per key: bytes, or an exception to raise."""

    def __init__(self, answers: dict) -> None:
        self.answers = answers

    def _answer(self, key):
        answer = self.answers[key]
        if isinstance(answer, Exception):
            raise answer
        return answer

    def get_object(self, Bucket, Key):
        return {"Body": io.BytesIO(self._answer(Key))}

    def head_object(self, Bucket, Key):
        self._answer(Key)

    def put_object(self, Bucket, Key, Body, ContentType, **conditions):
        self.conditions = conditions
        self._answer(Key)

    def delete_object(self, Bucket, Key):
        self._answer(Key)


def s3_store(answers: dict) -> A.S3Store:
    store = A.S3Store.__new__(A.S3Store)
    store.bucket, store.client = "b", FakeS3(answers)
    return store


def test_s3_failures_are_artifact_errors_and_a_denied_head_is_not_missing():
    from botocore.exceptions import ClientError, EndpointConnectionError

    def client_error(code: str) -> ClientError:
        return ClientError({"Error": {"Code": code, "Message": code}}, "HeadObject")

    store = s3_store(
        {
            "ok": b"data",
            "gone": client_error("NoSuchKey"),
            "none": client_error("404"),
            "denied": client_error("403"),
            "down": EndpointConnectionError(endpoint_url="https://s3.test"),
        }
    )
    assert store.get("ok") == b"data" and store.exists("ok")
    with pytest.raises(A.ArtifactError, match="missing object gone"):
        store.get("gone")
    assert not store.exists("gone") and not store.exists("none")
    for key, why in (("denied", "403"), ("down", "s3.test")):
        with pytest.raises(A.ArtifactError, match=why):
            store.exists(key)
        with pytest.raises(A.ArtifactError, match=why):
            store.get(key)
        with pytest.raises(A.ArtifactError, match=why):
            store.put(key, b"x", "text/plain")
    with pytest.raises(A.ArtifactError, match="no current artifact"):
        A.current(s3_store({"wiki/current.json": client_error("NoSuchKey")}), A.Keys("wiki"))


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


def test_the_publish_lease_refuses_a_second_publisher_and_takes_over_a_stale_one(
    tmp_path, store, monkeypatch
):
    root, site = make_repo(tmp_path)
    monkeypatch.setattr(A, "corpus_files", _plain_corpus)
    keys = A.Keys("wiki")
    push(store, keys, root, site, "v1")
    assert not store.exists(keys.lease)  # released after a push
    with A.publish_lease(store, keys, "push", "v2", seconds=60) as held:
        assert json.loads(store.get(keys.lease)) == held
        assert held["operation"] == "push" and held["artifact_id"] == "v2"
        with pytest.raises(A.ArtifactError, match="another publisher holds wiki/publish.lease"):
            push(store, keys, root, site, "v2")
        assert A.current(store, keys)["id"] == "v1" and not store.exists(keys.tarball("v2"))
    assert not store.exists(keys.lease)
    # A failed push releases the lease too.
    with pytest.raises(A.ArtifactError, match="immutable"):
        push(store, keys, root, site, "v1")
    assert not store.exists(keys.lease)
    # A lease whose holder died is taken over once it has expired.
    stale = {"holder": "dead:1:x", "operation": "push", "expires_at": "2000-01-01T00:00:00+00:00"}
    store.put(keys.lease, json.dumps(stale).encode(), "application/json")
    assert push(store, keys, root, site, "v2")["id"] == "v2"
    assert not store.exists(keys.lease)
    # One without a readable expiry is never taken over on a guess.
    store.put(keys.lease, b"not json", "application/json")
    with pytest.raises(A.ArtifactError, match="until an unknown time"):
        push(store, keys, root, site, "v3")
    assert A.current(store, keys)["id"] == "v2"
    assert A.lease_seconds({}) == 3600 and A.lease_seconds({A.LEASE_SECONDS_ENV: "5"}) == 5


def test_dir_store_creates_a_lease_exclusively(tmp_path):
    store = A.DirStore(tmp_path / "bucket")
    assert store.put_new("wiki/publish.lease", b"a", "application/json")
    assert not store.put_new("wiki/publish.lease", b"b", "application/json")
    assert store.get("wiki/publish.lease") == b"a"
    store.delete("wiki/publish.lease")
    store.delete("wiki/publish.lease")  # already gone: not an error
    assert store.put_new("wiki/publish.lease", b"c", "application/json")


def test_s3_store_leases_with_if_none_match_and_reads_a_precondition_failure_as_held():
    from botocore.exceptions import ClientError

    def client_error(code: str) -> ClientError:
        return ClientError({"Error": {"Code": code, "Message": code}}, "PutObject")

    store = s3_store(
        {
            "free": b"",
            "held": client_error("PreconditionFailed"),
            "denied": client_error("403"),
            "gone": client_error("NoSuchKey"),
        }
    )
    assert store.put_new("free", b"x", "application/json")
    assert store.client.conditions == {"IfNoneMatch": "*"}
    assert not store.put_new("held", b"x", "application/json")
    with pytest.raises(A.ArtifactError, match="put-new denied"):
        store.put_new("denied", b"x", "application/json")
    store.delete("gone")  # missing is fine
    with pytest.raises(A.ArtifactError, match="delete denied"):
        store.delete("denied")
