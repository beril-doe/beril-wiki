"""The site server resolves URLs the way GitHub Pages does, and only inside the site."""

from __future__ import annotations

import json

import pytest
from starlette.testclient import TestClient

from beril_wiki.serve import create_app


@pytest.fixture
def site(tmp_path):
    root = tmp_path / "public"
    for rel, body in {
        "index.html": "home",
        "a.html": "page a",
        "d/index.html": "folder d",
        "404.html": "custom 404",
        "static/x.js": "js",
    }.items():
        (root / rel).parent.mkdir(parents=True, exist_ok=True)
        (root / rel).write_text(body)
    (tmp_path / "secret.txt").write_text("outside the site")
    return root


@pytest.fixture
def client(site):
    return TestClient(create_app(site, "/wiki"), follow_redirects=False)


def test_prefix_and_root_redirect_to_the_index(client):
    for url in ("/wiki", "/"):
        r = client.get(url)
        assert r.status_code == 308 and r.headers["location"] == "/wiki/"
    r = client.get("/wiki/")
    assert r.status_code == 200 and r.text == "home"


def test_extensionless_page_and_folder_index(client):
    assert client.get("/wiki/a").text == "page a"
    assert client.get("/wiki/a.html").text == "page a"
    assert client.get("/wiki/d/").text == "folder d"


# Page links are relative, so each page works at one form of its URL only: a
# folder index (which links ../index.css) at d/, a page without the slash.
@pytest.mark.parametrize(
    "url, location",
    [
        ("/wiki/d", "/wiki/d/"),
        ("/wiki/a/", "/wiki/a"),
        ("/wiki/a.html/", "/wiki/a.html"),
        ("/wiki/d?q=x y", "/wiki/d/?q=x%20y"),
    ],
)
def test_the_wrong_trailing_slash_redirects(client, url, location):
    r = client.get(url)
    assert r.status_code == 308 and r.headers["location"] == location


def test_assets_are_served_with_a_short_cache(client):
    r = client.get("/wiki/static/x.js")
    assert r.status_code == 200 and r.text == "js"
    assert r.headers["cache-control"] == "public, max-age=300"
    assert client.get("/wiki/a").headers["cache-control"] == "no-cache"


def test_head_has_no_body(client):
    r = client.head("/wiki/a")
    assert r.status_code == 200 and r.content == b""


@pytest.mark.parametrize("url", ["/wiki/nope", "/wiki/static/", "/elsewhere", "/wiki-old/a"])
def test_unknown_paths_get_the_site_404(client, url):
    r = client.get(url)
    assert r.status_code == 404 and r.text == "custom 404"


@pytest.mark.parametrize(
    "url", ["/wiki/../secret.txt", "/wiki/%2e%2e/secret.txt", "/wiki/..%2fsecret.txt"]
)
def test_nothing_outside_the_site_is_served(client, url):
    r = client.get(url)
    assert r.status_code == 404 and "outside" not in r.text


def test_plain_404_without_a_site_404_page(site):
    (site / "404.html").unlink()
    r = TestClient(create_app(site)).get("/wiki/nope")
    assert r.status_code == 404 and r.text == "Not Found"


def test_healthz(client):
    r = client.get("/healthz")
    assert r.status_code == 200 and r.text == "ok"


# ---------------------------------------------------------------- artifact reload

AUTH = {"Authorization": "Bearer secret"}


def published(tmp_path, store, artifact_id: str, body: str):
    """Push a tiny site named `artifact_id` whose index reads `body`."""
    from beril_wiki.publish import artifact as A

    root = tmp_path / f"repo-{artifact_id}"
    site = root / "quartz/public"
    (site / "static/search").mkdir(parents=True)
    (site / "index.html").write_text(body)
    (site / "404.html").write_text(f"404 of {artifact_id}")
    (site / "static/search/pages.json").write_text('{"build": "b", "pages": []}')
    (site / "static/search/sections.json").write_text('{"build": "b", "sections": []}')
    (root / "wiki/sources").mkdir(parents=True)
    (root / "wiki/sources/demo__REPORT.md").write_text(f"report of {artifact_id}")
    gate = {
        "ran_at": "now",
        "site_digest": A.site_digest(site),
        "corpus_digest": A.corpus_digest(root),
        "results": {n: {"passed": True, "output": ""} for n in A.GATES},
    }
    return A.push(store, A.Keys("wiki"), root, site, artifact_id, gate=gate, history=False)


@pytest.fixture
def store(tmp_path):
    from beril_wiki.publish import artifact as A

    return A.DirStore(tmp_path / "bucket")


def reloading_app(site, tmp_path, store, token="secret", sync_on_start=True):
    from beril_wiki.publish import artifact as A

    return create_app(
        site,
        "/wiki",
        site_root=tmp_path / "artifacts",
        store=store,
        keys=A.Keys("wiki"),
        reload_token=token,
        sync_on_start=sync_on_start,
    )


def test_startup_serves_the_current_artifact_and_reload_swaps(site, tmp_path, store):
    published(tmp_path, store, "v1", "site v1")
    with TestClient(reloading_app(site, tmp_path, store)) as c:
        assert c.get("/wiki/").text == "site v1"
        status = c.get("/wiki/_admin/status", headers=AUTH).json()
        assert status["artifact"] == "v1" and status["page_count"] == 2 and status["corpus"]
        published(tmp_path, store, "v2", "site v2")
        assert c.get("/wiki/").text == "site v1"  # nothing changes until asked
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert r.status_code == 200
        assert r.json() == {"artifact": "v2", "previous": "v1", "page_count": 2, "changed": True}
        assert c.get("/wiki/").text == "site v2"
        assert c.get("/wiki/nope").text == "404 of v2"
        # Rollback is the pointer moving back, then the same reload.
        from beril_wiki.publish import artifact as A

        A.point(store, A.Keys("wiki"), "v1")
        c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert c.get("/wiki/").text == "site v1"
        link = tmp_path / "artifacts/current"
        assert link.is_symlink() and link.resolve().name == "site-v1"


def test_reload_requires_the_bearer_token(site, tmp_path, store):
    published(tmp_path, store, "v1", "site v1")
    with TestClient(reloading_app(site, tmp_path, store)) as c:
        assert c.post("/wiki/_admin/reload").status_code == 401
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer wrong"})
        assert r.status_code == 401
        assert c.get("/wiki/_admin/reload").status_code == 404  # a GET is a page lookup
    with TestClient(reloading_app(site, tmp_path, store, token=None)) as c:
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert r.status_code == 503


def test_without_a_store_the_baked_site_is_served(site):
    with TestClient(create_app(site, "/wiki", reload_token="secret")) as c:
        assert c.get("/wiki/").text == "home"
        status = c.get("/wiki/_admin/status", headers=AUTH).json()
        assert status["artifact"] == "baked" and status["store"] is False
        assert c.post("/wiki/_admin/reload", headers=AUTH).status_code == 503


def test_status_answers_only_to_the_reload_token(site):
    # The documented ingress forwards every /wiki path: artifact metadata stays in-cluster.
    with TestClient(create_app(site, "/wiki", reload_token="secret")) as c:
        assert c.get("/wiki/_admin/status").status_code == 401
        r = c.get("/wiki/_admin/status", headers={"Authorization": "Bearer wrong"})
        assert r.status_code == 401
        assert c.get("/wiki/_admin/status", headers=AUTH).status_code == 200
    with TestClient(create_app(site, "/wiki")) as c:
        assert c.get("/wiki/_admin/status", headers=AUTH).status_code == 503


def test_unreachable_store_falls_back_to_the_last_unpacked_then_baked(site, tmp_path, store):
    from beril_wiki.publish import artifact as A

    published(tmp_path, store, "v1", "site v1")
    with TestClient(reloading_app(site, tmp_path, store)) as c:
        assert c.get("/wiki/").text == "site v1"

    class Down:
        def get(self, key):
            raise A.ArtifactError("store down")

        def put(self, *a):
            raise A.ArtifactError("store down")

        def exists(self, key):
            return False

    # The previous run left site-v1 behind the `current` symlink: served again.
    with TestClient(reloading_app(site, tmp_path, Down())) as c:
        assert c.get("/wiki/").text == "site v1"
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert r.status_code == 502 and r.json()["artifact"] == "v1"
    # A fresh container with nothing unpacked serves the image's own tree.
    with TestClient(reloading_app(site, tmp_path / "fresh", Down())) as c:
        assert c.get("/wiki/").text == "home"
        assert c.get("/wiki/_admin/status", headers=AUTH).json()["artifact"] == "baked"


def test_a_bad_artifact_does_not_replace_the_served_one(site, tmp_path, store):
    published(tmp_path, store, "v1", "site v1")
    with TestClient(reloading_app(site, tmp_path, store)) as c:
        assert c.get("/wiki/").text == "site v1"
        published(tmp_path, store, "v2", "site v2")
        store.put("wiki/site-v2.tar.gz", b"not a tarball", "application/gzip")
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert r.status_code == 502
        assert c.get("/wiki/").text == "site v1"
        assert c.get("/wiki/_admin/status", headers=AUTH).json()["artifact"] == "v1"


def test_a_manifest_without_gate_results_is_refused(site, tmp_path, store):
    from beril_wiki.publish import artifact as A

    published(tmp_path, store, "v1", "site v1")
    manifest = json.loads(store.get("wiki/site-v1.manifest.json"))
    del manifest["gates"]
    # Re-pack v1's tarball with the gate-less manifest and point current at it.
    import io
    import tarfile

    old = store.get("wiki/site-v1.tar.gz")
    buf = io.BytesIO()
    with (
        tarfile.open(fileobj=io.BytesIO(old)) as src,
        tarfile.open(fileobj=buf, mode="w:gz") as dst,
    ):
        for member in src.getmembers():
            handle = src.extractfile(member) if member.isfile() else None
            data = handle.read() if handle else b""
            if member.name == "manifest.json":
                data = json.dumps(manifest).encode()
                member.size = len(data)
            dst.addfile(member, io.BytesIO(data))
    store.put("wiki/site-v1.tar.gz", buf.getvalue(), "application/gzip")
    pointer = json.loads(store.get("wiki/current.json"))
    pointer["sha256"] = A.sha256(buf.getvalue())
    store.put("wiki/current.json", json.dumps(pointer).encode(), "application/json")
    with TestClient(reloading_app(site, tmp_path, store)) as c:
        assert c.get("/wiki/").text == "home"  # refused on start: the baked site
        r = c.post("/wiki/_admin/reload", headers={"Authorization": "Bearer secret"})
        assert r.status_code == 502 and "gates" in r.json()["error"]
