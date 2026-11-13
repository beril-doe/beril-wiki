"""The hub backend stages what the local one does, from BERIL's context API only."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx
import pytest

from beril_wiki.stages import fetch, hub

REPORT = b"# Report: demo\n\n![plot](figures/plot.png)\n\nText.\n"
PLOT = b"\x89PNG demo"
README = b"# demo\n\n## Authors\n\n- Ada Lovelace (0000-0001-2345-6789)\n"
YAML = b"status: approved\n"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


class FakeBeril:
    """The two routes, as the contract describes them, over an in-memory project set."""

    def __init__(self) -> None:
        self.files: dict[str, dict[str, bytes]] = {}
        self.rows: list[dict] = []
        self.requests: list[str] = []
        self.corrupt: set[str] = set()

    def project(
        self, name: str, files: dict[str, bytes], when: str, kind: str = "approved", **extra
    ) -> None:
        self.files[name] = files
        self.rows.append(
            {
                "project": name,
                "owner_orcid": "0000-0001-2345-6789",
                "address": f"0000-0001-2345-6789/{name}",
                "submitted_at": when,
                "kind": kind,
                "batch_id": f"b-{name}-{when}",
                "is_public": extra.get("is_public", True),
                # The feed lists what the context layer ingested: no figures.
                "files": [
                    {"path": p, "sha256": sha(b)}
                    for p, b in files.items()
                    if not p.startswith("figures/")
                ],
            }
        )

    def handle(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(f"{request.url.path}?{request.url.query.decode()}")
        if request.headers.get("authorization") != "Bearer pat-1":
            return httpx.Response(401, json={"detail": "unauthorized"})
        if request.url.path == "/api/context/submissions":
            since = request.url.params.get("since")
            limit = int(request.url.params.get("limit", "200"))
            rows = sorted(self.rows, key=lambda r: r["submitted_at"])
            rows = [r for r in rows if not since or r["submitted_at"] > since][:limit]
            nxt = rows[-1]["submitted_at"] if rows else since
            return httpx.Response(200, json={"submissions": rows, "next_since": nxt})
        if request.url.path == "/api/context/read":
            _owner, project, path = request.url.params["address"].split("/", 2)
            data = self.files.get(project, {}).get(path)
            if data is None:
                return httpx.Response(404, json={"detail": "not found"})
            if path in self.corrupt:
                data = data + b"tampered"
            digest = sha(self.files[project][path])
            if request.headers.get("accept") == "application/octet-stream":
                return httpx.Response(
                    200,
                    content=data,
                    headers={
                        "content-type": "application/octet-stream",
                        "X-Content-SHA256": digest,
                        "X-Content-Source": "archive" if path.startswith("figures/") else "context",
                    },
                )
            return httpx.Response(
                200,
                json={
                    "address": request.url.params["address"],
                    "content": data.decode(),
                    "encoding": "utf-8",
                    "sha256": digest,
                    "source": "context",
                },
            )
        return httpx.Response(404)


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


# Bound once: tests replace hub.Hub with a factory that calls this.
HUB = hub.Hub


def connect(beril: FakeBeril) -> hub.Hub:
    return HUB("https://beril.test", "pat-1", transport=httpx.MockTransport(beril.handle))


@pytest.fixture
def client(beril) -> hub.Hub:
    return connect(beril)


@pytest.fixture
def root(tmp_path, monkeypatch) -> Path:
    monkeypatch.setattr(fetch, "BACKEND", "hub")
    monkeypatch.setattr(fetch, "CHECKOUT", tmp_path / "no-checkout")
    (tmp_path / "state").mkdir()
    return tmp_path


def test_hub_stages_the_local_layout_and_records_the_feed(root, beril, client):
    n = fetch.fetch_hub(root / "staging", client)
    assert n == 1
    assert (root / "staging/demo__REPORT.md").read_bytes() == REPORT
    assert (root / "wiki/figures/demo/plot.png").read_bytes() == PLOT
    assert (root / "reference/projects/demo/README.md").read_bytes() == README
    assert (root / "reference/projects/demo/beril.yaml").read_bytes() == YAML
    state = json.loads((root / "state/hub.json").read_text())
    assert state["next_since"] == "2026-11-01T00:00:00Z"
    assert state["projects"]["demo"]["files"]["REPORT.md"] == sha(REPORT)
    assert state["projects"]["demo"]["kind"] == "seeded"
    # Every byte came through /api/context/*, as raw bytes; nothing touched /ov.
    assert all(r.startswith("/api/context/") for r in beril.requests)


def test_hub_refuses_a_download_whose_hash_differs(root, beril, client):
    beril.corrupt.add("REPORT.md")
    with pytest.raises(hub.HubError, match="does not match"):
        fetch.fetch_hub(root / "staging", client)
    assert not (root / "staging/demo__REPORT.md").exists()
    assert not (root / "state/hub.json").exists()  # a failed fetch records no progress


def test_figure_hash_comes_from_the_route_when_the_feed_omits_it(root, beril, client):
    beril.corrupt.add("figures/plot.png")
    with pytest.raises(hub.HubError, match="figures/plot.png.*does not match"):
        fetch.fetch_hub(root / "staging", client)


def test_hub_continues_from_next_since_and_restages_every_project(root, beril, client):
    fetch.fetch_hub(root / "staging", client)
    beril.requests.clear()
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    (root / "staging/demo__REPORT.md").unlink()  # the runner clears staging per run
    n = fetch.fetch_hub(root / "staging", client)
    assert n == 2
    assert beril.requests[0].endswith("since=2026-11-01T00%3A00%3A00Z")
    assert {p.name for p in (root / "staging").glob("*.md")} == {
        "demo__REPORT.md",
        "later__REPORT.md",
    }
    # The report, README and beril.yaml are fetched again (staging is rebuilt); the figure
    # is not listed by the feed, so it is fetched again too and compared by bytes.
    assert sum("demo%2FREPORT.md" in r for r in beril.requests) == 1
    state = json.loads((root / "state/hub.json").read_text())
    assert state["next_since"] == "2026-11-02T00:00:00Z"


def test_feed_pages_follow_next_since(beril, client):
    for i in range(5):
        beril.project(f"p{i}", {"REPORT.md": f"# {i}\n".encode()}, f"2026-11-1{i}T00:00:00Z")
    rows = client.submissions(None, limit=2)
    assert [r["project"] for r in rows] == ["demo", "p0", "p1", "p2", "p3", "p4"]


def test_private_projects_are_not_served_or_fingerprinted(root, beril, client):
    beril.project("hidden", {"REPORT.md": b"# h\n"}, "2026-11-03T00:00:00Z", is_public=False)
    fetch.fetch_hub(root / "staging", client)
    assert not (root / "staging/hidden__REPORT.md").exists()
    state = hub.load_state(root)
    assert set(hub.fingerprint(state)) == {
        "projects/demo/REPORT.md",
        "projects/demo/README.md",
        "projects/demo/beril.yaml",
    }


def test_central_digests_fall_back_to_the_accepted_sources(root, beril, client):
    (root / "wiki/sources").mkdir(parents=True)
    (root / "wiki/sources/discoveries.md").write_text("archive\n")
    assert fetch.fetch_hub(root / "staging", client) == 2
    assert (root / "staging/discoveries.md").read_text() == "archive\n"


def test_unsafe_paths_from_the_feed_are_refused():
    with pytest.raises(hub.HubError, match="unsafe"):
        hub.merge(
            {"projects": {}},
            [{"project": "x", "address": "o/x", "files": [{"path": "../../etc", "sha256": ""}]}],
        )
    with pytest.raises(hub.HubError, match="unsafe project"):
        hub.merge({"projects": {}}, [{"project": "../x", "address": "o/x", "files": []}])
    with pytest.raises(SystemExit, match="unsafe figure"):
        fetch.figure_rel("figures/../../x.png")


def test_settings_are_required(monkeypatch):
    monkeypatch.delenv("BERIL_URL", raising=False)
    monkeypatch.delenv("BERIL_TOKEN", raising=False)
    with pytest.raises(hub.HubError, match="BERIL_URL and BERIL_TOKEN"):
        hub.Hub()


def test_json_read_is_decoded_per_its_encoding():
    def handle(request: httpx.Request) -> httpx.Response:
        return httpx.Response(
            200,
            json={"content": "aGVsbG8=", "encoding": "base64", "sha256": sha(b"hello")},
        )

    client = hub.Hub("https://b", "t", transport=httpx.MockTransport(handle))
    assert client.read("o/p/REPORT.md") == (b"hello", sha(b"hello"), None)


def test_extras_read_hub_readmes_and_the_committed_collections(root, beril, client, monkeypatch):
    from beril_wiki.stages import extras

    monkeypatch.setattr(extras, "ROOT", root)
    monkeypatch.setattr(fetch, "ROOT", root)
    monkeypatch.setattr(extras, "OUT", root / "wiki")
    fetch.fetch_hub(root / "staging", client)
    assert fetch.project_readmes(root) == {"demo": README.decode()}
    # Without the kept copy the README is read from the hub itself.
    (root / "reference/projects/demo/README.md").unlink()
    monkeypatch.setattr(hub, "Hub", lambda: connect(beril))
    assert fetch.project_readmes(root) == {"demo": README.decode()}
    (root / "contract").mkdir()
    (root / "contract/collections.yaml").write_text(
        "collections:\n  - id: demo_coll\n    name: Demo\n    provider: KBase\n"
    )
    assert fetch.collections_config() == root / "contract/collections.yaml"
    assert extras.write_collections() == 1
    assert (root / "wiki/data/demo-coll.md").exists()
    assert extras.write_authors() >= 1
    assert (root / "wiki/authors/ada-lovelace.md").exists()


def test_local_backend_is_unchanged(tmp_path, monkeypatch):
    checkout = tmp_path / "checkout"
    (checkout / "projects/demo/figures").mkdir(parents=True)
    (checkout / "projects/demo/REPORT.md").write_bytes(REPORT)
    (checkout / "projects/demo/figures/plot.png").write_bytes(PLOT)
    (checkout / "projects/demo/README.md").write_bytes(README)
    (checkout / "docs").mkdir()
    (checkout / "docs/pitfalls.md").write_text("p")
    monkeypatch.setattr(fetch, "BACKEND", "local")
    monkeypatch.setattr(fetch, "CHECKOUT", checkout)
    root = tmp_path / "root"
    assert fetch.fetch_local(root / "staging") == 2
    assert (root / "wiki/figures/demo/plot.png").read_bytes() == PLOT
    assert fetch.project_readmes(root) == {"demo": README.decode()}
    assert fetch.collections_config().name == "collections.yaml"


def test_runner_fingerprints_the_feed_in_hub_mode(tmp_path, monkeypatch, beril):
    from beril_wiki.agentic import runner

    root = tmp_path / "repo"
    (root / "state").mkdir(parents=True)
    monkeypatch.setenv("FETCH_BACKEND", "hub")
    monkeypatch.setattr(runner.H, "Hub", lambda: connect(beril))
    external, feed = runner.external_inputs(root, tmp_path / "unused-checkout")
    assert feed is not None and feed["next_since"] == "2026-11-01T00:00:00Z"
    assert external == {
        "projects/demo/REPORT.md": sha(REPORT),
        "projects/demo/README.md": sha(README),
        "projects/demo/beril.yaml": sha(YAML),
    }
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    assert runner.external_inputs(root, tmp_path / "unused-checkout")[0] != external
    monkeypatch.setenv("FETCH_BACKEND", "nope")
    with pytest.raises(runner.WorkflowError, match="unknown FETCH_BACKEND"):
        runner.fetch_backend()
