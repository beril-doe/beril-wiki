"""The server's store routes carry artifacts from a curator that shares no bucket or
volume with it; artifact.HttpStore is the client side."""

from __future__ import annotations

import socket
import threading
import time

import pytest
import uvicorn
from starlette.testclient import TestClient

from beril_wiki.publish import artifact as A
from beril_wiki.serve import create_app
from test_serve import published, reloading_app

AUTH = {"Authorization": "Bearer secret"}


@pytest.fixture
def site(tmp_path):
    root = tmp_path / "public"
    root.mkdir()
    (root / "index.html").write_text("baked")
    return root


@pytest.fixture
def store(tmp_path):
    return A.DirStore(tmp_path / "bucket")


@pytest.fixture
def client(site, tmp_path, store):
    with TestClient(reloading_app(site, tmp_path, store, sync_on_start=False)) as c:
        yield c


def test_put_get_head_and_list_round_trip(client, store):
    r = client.put("/wiki/_admin/store/wiki/a/b.txt", content=b"hello", headers=AUTH)
    assert r.status_code == 200
    assert r.json() == {"key": "wiki/a/b.txt", "bytes": 5, "sha256": A.sha256(b"hello")}
    assert (store.root / "wiki/a/b.txt").read_bytes() == b"hello"
    assert client.get("/wiki/_admin/store/wiki/a/b.txt", headers=AUTH).content == b"hello"
    assert client.head("/wiki/_admin/store/wiki/a/b.txt", headers=AUTH).status_code == 200
    assert client.head("/wiki/_admin/store/wiki/nope", headers=AUTH).status_code == 404
    assert client.get("/wiki/_admin/store/wiki/nope", headers=AUTH).status_code == 404
    client.put("/wiki/_admin/store/other/c", content=b"x", headers=AUTH)
    listed = client.get("/wiki/_admin/store?prefix=wiki/", headers=AUTH).json()
    assert listed == {"keys": ["wiki/a/b.txt"]}


def test_store_routes_require_the_bearer_token(client):
    assert client.put("/wiki/_admin/store/wiki/k", content=b"x").status_code == 401
    assert client.get("/wiki/_admin/store/wiki/k").status_code == 401
    assert client.get("/wiki/_admin/store").status_code == 401
    wrong = {"Authorization": "Bearer wrong"}
    assert client.put("/wiki/_admin/store/wiki/k", content=b"x", headers=wrong).status_code == 401


def test_oversized_bodies_are_refused_and_leave_nothing(site, tmp_path, store):
    small = create_app(
        site,
        "/wiki",
        site_root=tmp_path / "artifacts",
        store=store,
        keys=A.Keys("wiki"),
        reload_token="secret",
        sync_on_start=False,
        store_max_bytes=100,
    )
    with TestClient(small) as c:
        r = c.put("/wiki/_admin/store/wiki/big", content=b"x" * 101, headers=AUTH)
        assert r.status_code == 413
        # A chunked body with no declared length is caught while streaming.
        chunked = {**AUTH, "Transfer-Encoding": "chunked"}
        r = c.put("/wiki/_admin/store/wiki/big", content=iter([b"y" * 60] * 2), headers=chunked)
        assert r.status_code == 413
        assert not (store.root / "wiki/big").exists()
        assert not list(store.root.rglob(".*"))  # no temporary file left behind
        ok = c.put("/wiki/_admin/store/wiki/ok", content=b"z" * 100, headers=AUTH)
        assert ok.status_code == 200


@pytest.mark.parametrize("key", ["wiki/..%2Fescape", "..%2Fescape", ".hidden", "wiki/.tmp", "a//b"])
def test_traversal_and_hidden_keys_are_refused(client, store, key):
    r = client.put(f"/wiki/_admin/store/{key}", content=b"x", headers=AUTH)
    assert r.status_code == 400, r.text
    assert client.get(f"/wiki/_admin/store/{key}", headers=AUTH).status_code == 400
    assert not list(store.root.parent.rglob("escape"))


def test_without_a_directory_store_the_routes_answer_503(site, tmp_path):
    class Remote:
        def get(self, key):
            raise A.ArtifactError("x")

        def put(self, key, data, content_type):
            pass

        def exists(self, key):
            return False

    with TestClient(reloading_app(site, tmp_path, Remote(), sync_on_start=False)) as c:
        assert c.put("/wiki/_admin/store/wiki/k", content=b"x", headers=AUTH).status_code == 503


# ------------------------------------------------- end to end over a real socket


@pytest.fixture
def live(site, tmp_path, store):
    """The wiki server on a loopback port, as the curator job reaches it."""
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    app = reloading_app(site, tmp_path, store, sync_on_start=False)
    server = uvicorn.Server(uvicorn.Config(app, host="127.0.0.1", port=port, log_level="error"))
    thread = threading.Thread(target=server.run, daemon=True)
    thread.start()
    for _ in range(100):
        if server.started:
            break
        time.sleep(0.05)
    else:
        raise RuntimeError("server did not start")
    yield f"http://127.0.0.1:{port}"
    server.should_exit = True
    thread.join(timeout=5)


def test_http_store_pushes_and_the_server_reloads_from_it(live, tmp_path, store):
    http = A.HttpStore(f"{live}/wiki/_admin/store", "secret")
    assert not http.exists("wiki/current.json")
    pointer = published(tmp_path, http, "v1", "site v1")
    assert pointer["id"] == "v1"
    # The bytes landed in the server's own directory store, where reload reads them.
    assert store.exists("wiki/site-v1.tar.gz") and store.exists("wiki/current.json")
    assert http.get("wiki/current.json") == store.get("wiki/current.json")
    assert http.list_keys("wiki/") == [
        "wiki/current.json",
        "wiki/site-v1.manifest.json",
        "wiki/site-v1.tar.gz",
    ]
    with pytest.raises(A.ArtifactError, match="missing object"):
        http.get("wiki/absent")
    import urllib.request

    req = urllib.request.Request(
        f"{live}/wiki/_admin/reload", method="POST", headers={"Authorization": "Bearer secret"}
    )
    with urllib.request.urlopen(req, timeout=10) as r:
        assert r.status == 200
    with urllib.request.urlopen(f"{live}/wiki/", timeout=10) as r:
        assert r.read() == b"site v1"
    with urllib.request.urlopen(f"{live}/wiki/_admin/status", timeout=10) as r:
        assert b'"artifact":"v1"' in r.read().replace(b" ", b"")
    with pytest.raises(A.ArtifactError, match="HTTP 401"):
        A.HttpStore(f"{live}/wiki/_admin/store", "wrong").put("wiki/x", b"x", "text/plain")
    with pytest.raises(A.ArtifactError, match="needs WIKI_RELOAD_TOKEN"):
        A.store_from_env({"WIKI_ARTIFACT_ENDPOINT": f"{live}/wiki/_admin/store"})
    env = {"WIKI_ARTIFACT_ENDPOINT": f"{live}/wiki/_admin/store/", "WIKI_RELOAD_TOKEN": "t"}
    assert isinstance(A.store_from_env(env), A.HttpStore)


# ------------------------------------------- HttpStore's error mapping, no server


def mock_store(handler):
    """An HttpStore over a scripted transport; `handler` takes the request and returns
    a response or raises the transport error to simulate."""
    import httpx

    return A.HttpStore("http://wiki:8080/wiki/_admin/store", "t", 5, httpx.MockTransport(handler))


def answer(status, body=b"", json=None):
    import httpx

    if json is not None:
        return lambda req: httpx.Response(status, json=json)
    return lambda req: httpx.Response(status, content=body)


def test_http_store_reports_a_404_on_put_as_a_missing_route_not_different_bytes():
    with pytest.raises(A.ArtifactError, match=r"store PUT wiki/x: HTTP 404 not found$"):
        mock_store(answer(404, b"not found")).put("wiki/x", b"x", "text/plain")


def test_http_store_reports_a_2xx_without_the_sha_echo_and_a_wrong_echo():
    with pytest.raises(A.ArtifactError, match="HTTP 200 with no sha256 echo"):
        mock_store(answer(200, b"<html>")).put("wiki/x", b"x", "text/plain")
    with pytest.raises(A.ArtifactError, match="stored different bytes"):
        mock_store(answer(200, json={"sha256": "0" * 64})).put("wiki/x", b"x", "text/plain")
    mock_store(answer(200, json={"sha256": A.sha256(b"x")})).put("wiki/x", b"x", "text/plain")


def test_http_store_listing_errors_carry_the_status_not_a_decode_error():
    with pytest.raises(A.ArtifactError, match=r"store GET: HTTP 404"):
        mock_store(answer(404)).list_keys("wiki/")
    with pytest.raises(A.ArtifactError, match="HTTP 200 with no key list"):
        mock_store(answer(200, b"<html>")).list_keys("wiki/")
    assert mock_store(answer(200, json={"keys": ["wiki/a"]})).list_keys("wiki/") == ["wiki/a"]


def test_http_store_exists_is_false_only_on_404():
    assert mock_store(answer(200)).exists("wiki/x") is True
    assert mock_store(answer(404)).exists("wiki/x") is False
    for status in (401, 500, 503):
        with pytest.raises(A.ArtifactError, match=f"store HEAD wiki/x: HTTP {status}"):
            mock_store(answer(status)).exists("wiki/x")
    with pytest.raises(A.ArtifactError, match="missing object wiki/x"):
        mock_store(answer(404)).get("wiki/x")
    with pytest.raises(A.ArtifactError, match="store GET wiki/x: HTTP 503"):
        mock_store(answer(503)).get("wiki/x")


@pytest.mark.parametrize(
    ("error", "expected"),
    [
        ("ReadTimeout", r"store GET wiki/x: no answer within 5s from http://wiki:8080"),
        ("ConnectError", r"store GET wiki/x: ConnectError: .*\(http://wiki:8080"),
        ("RemoteProtocolError", r"store GET wiki/x: RemoteProtocolError: disconnected"),
    ],
)
def test_http_store_transport_failures_become_artifact_errors(error, expected):
    import httpx

    def failing(req):
        raise getattr(httpx, error)("disconnected", request=req)

    with pytest.raises(A.ArtifactError, match=expected):
        mock_store(failing).get("wiki/x")
