"""`corpus pull-hub` fills corpus/ from BERIL's context API; fetch then stages it whole."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx
import pytest

from beril_wiki import corpus
from beril_wiki.stages import fetch, hub

REPORT = b"# Report: demo\n\n![plot](figures/plot.png)\n\nText.\n"
PLOT = b"\x89PNG demo"
README = b"# demo\n\n## Authors\n\n- Ada Lovelace (0000-0001-2345-6789)\n"
YAML = b"status: approved\n"
ORCID = "0000-0001-2345-6789"
OTHER = "0000-0002-9999-0000"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class FakeBeril:
    """The two routes, as the revision-2 contract describes them."""

    def __init__(self) -> None:
        self.files: dict[str, dict[str, bytes]] = {}
        self.when: dict[str, str] = {}
        self.rows: list[dict] = []
        self.requests: list[str] = []
        self.corrupt: set[str] = set()
        self.broken: set[str] = set()  # paths the read route answers 502 for

    def project(
        self, name: str, files: dict[str, bytes], when: str, kind="approved", owner=ORCID
    ) -> None:
        # Like BERIL's read with no revision: the newest submission's files.
        if when >= self.when.get(f"{owner}/{name}", ""):
            self.files[f"{owner}/{name}"] = files
            self.when[f"{owner}/{name}"] = when
        report = files.get("REPORT.md")
        self.rows.append(
            {
                "id": len(self.rows) + 1,
                "project": name,
                "owner_orcid": owner,
                "address": f"{owner}/{name}",
                "revision": sha(report if report is not None else b"".join(files.values())),
                "submitted_at": when,
                "kind": kind,
                "files": [{"path": p, "sha256": sha(b), "size": len(b)} for p, b in files.items()],
            }
        )

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(f"{request.url.path}?{request.url.query.decode()}")
        if request.headers.get("authorization") != "Bearer pat-1":
            return httpx.Response(401, json={"detail": "unauthorized"})
        if request.url.path == "/api/context/submissions":
            # Feed position = completion order = the order rows were added.
            after = int(request.url.params.get("after", "0"))
            limit = int(request.url.params.get("limit", "200"))
            rows = [r for r in self.rows if r["id"] > after][:limit]
            nxt = rows[-1]["id"] if rows else after
            return httpx.Response(200, json={"submissions": rows, "next_after": nxt})
        if request.url.path == "/api/context/read":
            owner, project, path = request.url.params["address"].split("/", 2)
            data = self.files.get(f"{owner}/{project}", {}).get(path)
            if data is None:
                return httpx.Response(404, json={"detail": "not found"})
            if path in self.broken:
                return httpx.Response(502, text="bad gateway")
            digest = sha(data)
            if path in self.corrupt:
                data = data + b"tampered"
            return httpx.Response(
                200,
                content=data,
                headers={"content-type": "application/octet-stream", "X-Content-SHA256": digest},
            )
        return httpx.Response(404)


HUB = hub.Hub  # bound once: a test may replace hub.Hub with a factory that calls this


def connect(beril: FakeBeril) -> hub.Hub:
    return HUB("https://beril.test", "pat-1", transport=httpx.MockTransport(beril.handle))


@pytest.fixture
def beril() -> FakeBeril:
    b = FakeBeril()
    b.project(
        "demo",
        {"REPORT.md": REPORT, "figures/plot.png": PLOT, "README.md": README, "beril.yaml": YAML},
        "2026-11-01T00:00:00Z",
        kind="seeded",
    )
    return b


@pytest.fixture
def client(beril) -> hub.Hub:
    return connect(beril)


@pytest.fixture
def out(tmp_path) -> Path:
    return tmp_path / "corpus"


def test_pull_writes_the_checkout_layout_and_the_manifest(out, beril, client):
    done = corpus.pull_hub(out, client)
    assert done == {"projects": 1, "docs": 0, "next_after": 1}
    where = out / "projects/demo"
    assert (where / "REPORT.md").read_bytes() == REPORT
    assert (where / "README.md").read_bytes() == README
    assert (where / "beril.yaml").read_bytes() == YAML
    assert (where / "figures/plot.png").read_bytes() == PLOT
    manifest = corpus.load(out)
    assert manifest["hub"] == {"url": "https://beril.test", "next_after": 1}
    entry = manifest["projects"]["demo"]
    assert entry["files"] == {
        "README.md": "sha256:" + sha(README),
        "REPORT.md": "sha256:" + sha(REPORT),
        "beril.yaml": "sha256:" + sha(YAML),
        "figures/plot.png": "sha256:" + sha(PLOT),
    }
    assert entry["digest"] == corpus.digest(entry["files"])
    assert {k: entry[k] for k in ("owner_orcid", "project", "revision", "kind", "address")} == {
        "owner_orcid": ORCID,
        "project": "demo",
        "revision": sha(REPORT),
        "kind": "seeded",
        "address": f"{ORCID}/demo",
    }
    assert entry["submitted_at"] == "2026-11-01T00:00:00Z" and entry["origin"] == "hub@1"
    assert corpus.verify(out) == []
    assert all(r.startswith("/api/context/") for r in beril.requests)


def test_pull_output_is_what_fetch_local_stages(out, beril, client, tmp_path, monkeypatch):
    beril.project(
        "docs", {"discoveries.md": b"# D\n"}, "2026-11-02T00:00:00Z", kind="docs", owner="beril"
    )
    assert corpus.pull_hub(out, client)["docs"] == 1
    assert corpus.load(out)["shared"] == {"docs/discoveries.md": "sha256:" + sha(b"# D\n")}
    assert corpus.verify(out) == []
    root = tmp_path / "root"
    monkeypatch.setattr(fetch, "CHECKOUT", out)
    assert fetch.fetch_local(root / "staging") == 2
    assert (root / "staging/demo__REPORT.md").read_bytes() == REPORT
    assert (root / "staging/discoveries.md").read_bytes() == b"# D\n"
    assert (root / "wiki/figures/demo/plot.png").read_bytes() == PLOT


def test_a_download_whose_hash_differs_installs_nothing(out, beril, client):
    beril.corrupt.add("REPORT.md")
    with pytest.raises(hub.HubError, match="does not match"):
        corpus.pull_hub(out, client)
    assert not out.exists()
    assert list(out.parent.glob(".corpus-pull-*")) == []
    beril.corrupt = {"figures/plot.png"}  # a listed figure must match too
    with pytest.raises(hub.HubError, match="does not match"):
        corpus.pull_hub(out, client)
    assert not out.exists()


def test_a_figure_the_hub_refuses_is_skipped_with_a_warning(out, beril, client, capsys):
    beril.broken.add("figures/plot.png")
    beril.project(
        "nofig", {"REPORT.md": b"# n\n\n![x](figures/gone.png)\n"}, "2026-11-02T00:00:00Z"
    )
    assert corpus.pull_hub(out, client)["projects"] == 2
    assert not (out / "projects/demo/figures").exists()
    assert "figures/plot.png: skipped" in capsys.readouterr().err
    assert "figures/plot.png" not in corpus.load(out)["projects"]["demo"]["files"]
    assert corpus.verify(out) == []


def test_only_changed_revisions_are_downloaded_and_a_new_revision_replaces(out, beril, client):
    corpus.pull_hub(out, client)
    beril.requests.clear()
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert beril.requests[0].endswith("after=1")
    assert not any("demo" in r for r in beril.requests[1:])
    assert corpus.pull_hub(out, client) == {"projects": 0, "docs": 0, "next_after": 2}
    beril.project("demo", {"REPORT.md": REPORT + b"v2\n"}, "2026-11-03T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert (out / "projects/demo/REPORT.md").read_bytes() == REPORT + b"v2\n"
    assert not (out / "projects/demo/README.md").exists()  # the old tree is replaced
    assert set(corpus.load(out)["projects"]) == {"demo", "later"}
    assert corpus.verify(out) == []


def test_sids_are_unique_per_owner_and_vendored_ids_are_pinned(out, beril, client):
    out.mkdir()
    corpus.save(
        {
            "version": 1,
            "shared": {},
            "projects": {"pinned": {"origin": "v1@abc", "files": {}, "digest": corpus.digest({})}},
        },
        out,
    )
    beril.project("demo", {"REPORT.md": b"# other demo\n"}, "2026-11-02T00:00:00Z", owner=OTHER)
    beril.project("pinned", {"REPORT.md": b"# pinned\n"}, "2026-11-03T00:00:00Z", owner=OTHER)
    beril.project("pinned", {"REPORT.md": b"# mine\n"}, "2026-11-04T00:00:00Z", owner=ORCID)
    corpus.pull_hub(out, client)
    projects = corpus.load(out)["projects"]
    assert projects["demo"]["owner_orcid"] == ORCID
    assert projects[f"demo__{OTHER}"]["owner_orcid"] == OTHER
    assert projects["pinned"]["owner_orcid"] == OTHER  # first submitter under the slug
    assert projects[f"pinned__{ORCID}"]["owner_orcid"] == ORCID
    assert (out / f"projects/pinned__{ORCID}/REPORT.md").read_bytes() == b"# mine\n"
    manifest = corpus.load(out)
    assert corpus.assign_sid(manifest, OTHER, "demo") == f"demo__{OTHER}"
    assert corpus.assign_sid(manifest, ORCID, "demo") == "demo"
    assert corpus.verify(out) == []


def test_feed_pages_follow_next_after(beril, client):
    for i in range(5):
        beril.project(f"p{i}", {"REPORT.md": f"# {i}\n".encode()}, f"2026-11-1{i}T00:00:00Z")
    rows, following = client.submissions(None, limit=2)
    assert [r["project"] for r in rows] == ["demo", "p0", "p1", "p2", "p3", "p4"]
    assert following == 6
    assert client.submissions(following) == ([], 6)


def test_the_newest_revision_wins_when_an_older_one_completes_later(out, beril, client):
    # v2 is fed first; v1 (submitted earlier) completes after it. Within one
    # pull and across pulls, the corpus keeps v2.
    beril.project("demo", {"REPORT.md": b"# v2\n"}, "2026-11-05T00:00:00Z")
    beril.project("demo", {"REPORT.md": b"# v1\n"}, "2026-11-04T00:00:00Z")
    corpus.pull_hub(out, client)
    assert (out / "projects/demo/REPORT.md").read_bytes() == b"# v2\n"

    beril.project("demo", {"REPORT.md": b"# v0\n"}, "2026-11-03T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 0
    assert (out / "projects/demo/REPORT.md").read_bytes() == b"# v2\n"
    assert corpus.load(out)["projects"]["demo"]["submitted_at"] == "2026-11-05T00:00:00Z"
    assert corpus.verify(out) == []


def test_a_manifest_with_the_old_cursor_relists_from_the_beginning(out, beril, client):
    corpus.pull_hub(out, client)
    manifest = corpus.load(out)
    manifest["hub"] = {"url": "https://beril.test", "next_since": "2026-11-01T00:00:00Z"}
    corpus.save(manifest, out)
    beril.requests.clear()

    done = corpus.pull_hub(out, client)

    assert "after=" not in beril.requests[0]
    assert done == {"projects": 0, "docs": 0, "next_after": 1}  # demo unchanged: not re-downloaded
    assert corpus.load(out)["hub"] == {"url": "https://beril.test", "next_after": 1}


def test_unsafe_names_from_the_feed_are_refused():
    row = {"project": "x", "owner_orcid": "o", "address": "o/x"}
    with pytest.raises(hub.HubError, match="unsafe"):
        hub.latest([row | {"files": [{"path": "../../etc", "sha256": ""}]}])
    with pytest.raises(hub.HubError, match="unsafe owner"):
        hub.latest([row | {"project": "../x", "files": []}])
    with pytest.raises(hub.HubError, match="address"):
        hub.latest([row | {"address": "o/y", "files": []}])


def test_settings_are_required(monkeypatch):
    monkeypatch.delenv("BERIL_URL", raising=False)
    monkeypatch.delenv("BERIL_TOKEN", raising=False)
    with pytest.raises(hub.HubError, match="BERIL_URL and BERIL_TOKEN"):
        hub.Hub()


def test_json_read_is_decoded_per_its_encoding():
    def handle(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200, json={"content": "aGVsbG8=", "encoding": "base64", "sha256": sha(b"hello")}
        )

    client = hub.Hub("https://b", "t", transport=httpx.MockTransport(handle))
    assert client.read("o/p/REPORT.md") == (b"hello", sha(b"hello"))


def test_cli_reports_the_pull(out, beril, monkeypatch, capsys):
    monkeypatch.setattr(corpus, "CORPUS", out)
    monkeypatch.setattr(hub, "Hub", lambda: connect(beril))
    assert corpus.main(["pull-hub"]) == 0
    assert "1 project(s) and 0 digest(s) updated" in capsys.readouterr().out
    assert json.loads((out / "manifest.json").read_text())["hub"]["next_after"] == 1
    assert corpus.main(["verify"]) == 0
