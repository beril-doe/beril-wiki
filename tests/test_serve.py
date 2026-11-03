"""The site server resolves URLs the way GitHub Pages does, and only inside the site."""

from __future__ import annotations

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
