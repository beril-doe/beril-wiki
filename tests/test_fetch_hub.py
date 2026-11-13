"""The hub backend fills the committed corpus from BERIL's context API; staging is whole."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import httpx
import pytest

from beril_wiki.stages import corpus, fetch, hub

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
        self.rows: list[dict] = []
        self.requests: list[str] = []
        self.corrupt: set[str] = set()

    def project(
        self, name: str, files: dict[str, bytes], when: str, kind="approved", owner=ORCID
    ) -> None:
        self.files[f"{owner}/{name}"] = files
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
                "archive_path": f"s3a://cdm-lake/projects/{name}",
                "files": [{"path": p, "sha256": sha(b), "size": len(b)} for p, b in files.items()],
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
            owner, project, path = request.url.params["address"].split("/", 2)
            data = self.files.get(f"{owner}/{project}", {}).get(path)
            if data is None:
                return httpx.Response(404, json={"detail": "not found"})
            digest = sha(data)
            if path in self.corrupt:
                data = data + b"tampered"
            if request.headers.get("accept") == "application/octet-stream":
                return httpx.Response(
                    200,
                    content=data,
                    headers={
                        "content-type": "application/octet-stream",
                        "X-Content-SHA256": digest,
                        "X-Content-Source": "submission",
                    },
                )
            return httpx.Response(
                200, json={"content": data.decode(), "encoding": "utf-8", "sha256": digest}
            )
        return httpx.Response(404)


# Bound once: tests replace hub.Hub with a factory that calls this.
HUB = hub.Hub


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
def root(tmp_path, monkeypatch) -> Path:
    monkeypatch.setattr(fetch, "BACKEND", "hub")
    monkeypatch.setattr(fetch, "CHECKOUT", tmp_path / "no-checkout")
    (tmp_path / "state").mkdir()
    (tmp_path / "wiki/sources").mkdir(parents=True)
    return tmp_path


def test_hub_writes_the_corpus_and_stages_all_of_it(root, beril, client):
    assert fetch.fetch_hub(root / "staging", client) == 1
    where = root / "corpus" / ORCID / "demo"
    assert (where / "REPORT.md").read_bytes() == REPORT
    assert (where / "README.md").read_bytes() == README
    assert (where / "beril.yaml").read_bytes() == YAML
    assert (where / "figures/plot.png").read_bytes() == PLOT
    assert (root / "staging/demo__REPORT.md").read_bytes() == REPORT
    assert (root / "wiki/figures/demo/plot.png").read_bytes() == PLOT
    assert corpus.load_index(root)[f"{ORCID}/demo"] == {
        "sid": "demo",
        "revision": sha(REPORT),
        "submitted_at": "2026-11-01T00:00:00Z",
        "kind": "seeded",
    }
    state = json.loads((root / "state/hub.json").read_text())
    assert state["next_since"] == "2026-11-01T00:00:00Z"
    assert all(r.startswith("/api/context/") for r in beril.requests)


def test_hub_refuses_a_download_whose_hash_differs(root, beril, client):
    beril.corrupt.add("REPORT.md")
    with pytest.raises(hub.HubError, match="does not match"):
        fetch.fetch_hub(root / "staging", client)
    assert not (root / "corpus" / ORCID / "demo").exists()
    assert not (root / "state/hub.json").exists()  # a failed fetch records no progress
    assert not (root / "corpus/index.json").exists()


def test_only_changed_revisions_are_downloaded_and_staging_stays_whole(root, beril, client):
    fetch.fetch_hub(root / "staging", client)
    beril.requests.clear()
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    (root / "staging/demo__REPORT.md").unlink()  # the runner clears staging per run
    assert fetch.fetch_hub(root / "staging", client) == 2
    assert beril.requests[0].endswith("since=2026-11-01T00%3A00%3A00Z")
    assert not any("demo" in r for r in beril.requests[1:])  # unchanged: not fetched again
    assert {p.name for p in (root / "staging").glob("*.md")} == {
        "demo__REPORT.md",
        "later__REPORT.md",
    }
    # A new revision of demo is fetched and replaces the corpus copy.
    beril.project("demo", {"REPORT.md": REPORT + b"v2\n"}, "2026-11-03T00:00:00Z")
    assert fetch.import_hub(root, client) == 1
    assert (root / "corpus" / ORCID / "demo/REPORT.md").read_bytes() == REPORT + b"v2\n"
    assert not (root / "corpus" / ORCID / "demo/README.md").exists()


def test_sids_are_unique_per_owner_and_pinned(root, beril, client):
    (root / "wiki/sources/pinned__REPORT.md").write_bytes(b"# pinned\n")
    beril.project("demo", {"REPORT.md": b"# other demo\n"}, "2026-11-02T00:00:00Z", owner=OTHER)
    beril.project("pinned", {"REPORT.md": b"# pinned\n"}, "2026-11-03T00:00:00Z", owner=OTHER)
    fetch.fetch_hub(root / "staging", client)
    index = corpus.load_index(root)
    assert index[f"{ORCID}/demo"]["sid"] == "demo"
    assert index[f"{OTHER}/demo"]["sid"] == f"demo__{OTHER}"
    # The legacy source kept its slug and the entry moved to its real owner.
    assert index[f"{OTHER}/pinned"]["sid"] == "pinned" and "legacy/pinned" not in index
    assert {p.name for p in (root / "staging").glob("*.md")} == {
        "demo__REPORT.md",
        f"demo__{OTHER}__REPORT.md",
        "pinned__REPORT.md",
    }
    # Re-seeding or re-fetching never reassigns.
    assert corpus.assign_sid(index, OTHER, "demo") == f"demo__{OTHER}"
    assert corpus.assign_sid(index, ORCID, "demo") == "demo"


def test_legacy_sources_without_corpus_files_stage_the_accepted_copy(root, beril, client):
    (root / "wiki/sources/old__REPORT.md").write_bytes(b"# old\n")
    assert fetch.fetch_hub(root / "staging", client) == 2
    assert (root / "staging/old__REPORT.md").read_bytes() == b"# old\n"
    assert corpus.load_index(root)["legacy/old"]["kind"] == "legacy"


def test_docs_submissions_supply_the_digests(root, beril, client):
    (root / "wiki/sources/pitfalls.md").write_text("archive\n")
    beril.project(
        "docs", {"discoveries.md": b"# D\n"}, "2026-11-02T00:00:00Z", kind="docs", owner="beril"
    )
    assert fetch.fetch_hub(root / "staging", client) == 3
    assert (root / "corpus/beril/docs/discoveries.md").read_bytes() == b"# D\n"
    assert (root / "staging/discoveries.md").read_bytes() == b"# D\n"
    assert (root / "staging/pitfalls.md").read_text() == "archive\n"  # legacy fallback


def test_feed_pages_follow_next_since(beril, client):
    for i in range(5):
        beril.project(f"p{i}", {"REPORT.md": f"# {i}\n".encode()}, f"2026-11-1{i}T00:00:00Z")
    rows = client.submissions(None, limit=2)
    assert [r["project"] for r in rows] == ["demo", "p0", "p1", "p2", "p3", "p4"]


def test_unsafe_names_from_the_feed_are_refused():
    row = {"project": "x", "owner_orcid": "o", "address": "o/x"}
    with pytest.raises(hub.HubError, match="unsafe"):
        hub.merge({"projects": {}}, [row | {"files": [{"path": "../../etc", "sha256": ""}]}])
    with pytest.raises(hub.HubError, match="unsafe owner"):
        hub.merge({"projects": {}}, [row | {"project": "../x", "files": []}])
    with pytest.raises(corpus.CorpusError, match="unsafe figure"):
        corpus.figure_rel("figures/../../x.png")
    with pytest.raises(corpus.CorpusError, match="unsafe owner"):
        corpus.key_of("..", "x")


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
    assert client.read("o/p/REPORT.md") == (b"hello", sha(b"hello"), None)


def test_extras_read_corpus_readmes_and_the_committed_collections(root, beril, client, monkeypatch):
    from beril_wiki.stages import extras

    monkeypatch.setattr(extras, "ROOT", root)
    monkeypatch.setattr(fetch, "ROOT", root)
    monkeypatch.setattr(extras, "OUT", root / "wiki")
    fetch.fetch_hub(root / "staging", client)
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


def test_local_backend_fills_the_corpus_under_legacy(tmp_path, monkeypatch):
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
    (root / "wiki/sources").mkdir(parents=True)
    assert fetch.fetch_local(root / "staging") == 2
    assert (root / "corpus/legacy/demo/REPORT.md").read_bytes() == REPORT
    assert (root / "corpus/beril/docs/pitfalls.md").read_text() == "p"
    assert (root / "wiki/figures/demo/plot.png").read_bytes() == PLOT
    assert (root / "staging/pitfalls.md").exists()
    assert fetch.project_readmes(root) == {"demo": README.decode()}
    assert corpus.load_index(root)["legacy/demo"]["kind"] == "local"


def test_runner_fingerprints_the_feed_in_hub_mode(tmp_path, monkeypatch, beril):
    from beril_wiki.agentic import runner

    root = tmp_path / "repo"
    (root / "state").mkdir(parents=True)
    monkeypatch.setenv("FETCH_BACKEND", "hub")
    monkeypatch.setattr(runner.H, "Hub", lambda: connect(beril))
    external, feed = runner.external_inputs(root, tmp_path / "unused-checkout")
    assert feed is not None and feed["next_since"] == "2026-11-01T00:00:00Z"
    assert external == {
        f"corpus/{ORCID}/demo/REPORT.md": sha(REPORT),
        f"corpus/{ORCID}/demo/README.md": sha(README),
        f"corpus/{ORCID}/demo/beril.yaml": sha(YAML),
        f"corpus/{ORCID}/demo/figures/plot.png": sha(PLOT),
    }
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    assert runner.external_inputs(root, tmp_path / "unused-checkout")[0] != external
    monkeypatch.setenv("FETCH_BACKEND", "nope")
    with pytest.raises(runner.WorkflowError, match="unknown FETCH_BACKEND"):
        runner.fetch_backend()
