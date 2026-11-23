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
    assert "hub" not in manifest  # the cursor is state, not corpus
    assert corpus.load_cursor(out.parent / "state") == {
        "url": "https://beril.test",
        "next_after": 1,
    }
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


def test_a_listed_figure_the_hub_does_not_serve_stops_the_pull(out, beril, client, capsys):
    # A 502 on a feed-listed figure is not a skip: skipping would install the project
    # without it, advance the cursor and never ask for the figure again.
    beril.broken.add("figures/plot.png")
    with pytest.raises(hub.HubError, match="figures/plot.png: HTTP 502"):
        corpus.pull_hub(out, client)
    assert not out.exists()
    beril.broken.clear()
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert (out / "projects/demo/figures/plot.png").read_bytes() == PLOT
    # A figure the report embeds but the submission does not carry is all a pull
    # can skip; it is not in the feed, so there is nothing to ask for later.
    beril.project(
        "nofig", {"REPORT.md": b"# n\n\n![x](figures/gone.png)\n"}, "2026-11-02T00:00:00Z"
    )
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert "figures/gone.png: skipped" in capsys.readouterr().err
    assert corpus.verify(out) == []


def test_a_project_held_without_a_declared_figure_is_pulled_again(out, beril, client):
    corpus.pull_hub(out, client)
    manifest = corpus.load(out)
    entry = manifest["projects"]["demo"]
    # As a corpus written before listed figures were required may hold it.
    del entry["files"]["figures/plot.png"]
    entry["digest"] = corpus.digest(entry["files"])
    (out / "projects/demo/figures/plot.png").unlink()
    corpus.save(manifest, out)
    assert corpus.verify(out) == []
    row = hub.latest(beril.rows)[(ORCID, "demo")]
    assert not corpus.unchanged(entry, row, out / "projects/demo")
    beril.project("demo", dict(beril.files[f"{ORCID}/demo"]), "2026-11-02T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert (out / "projects/demo/figures/plot.png").read_bytes() == PLOT
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


def test_a_feed_page_without_a_cursor_is_refused_and_next_since_is_followed(beril):
    beril.project("p1", {"REPORT.md": b"# 1\n"}, "2026-11-11T00:00:00Z")
    pages: list[str] = []

    def paging(request: httpx.Request) -> httpx.Response:
        if request.url.path != "/api/context/submissions":
            return beril.handle(request)
        pages.append(request.url.query.decode())
        since = request.url.params.get("since")
        if since is None:
            return httpx.Response(200, json={"submissions": beril.rows[:1], "next_since": "t1"})
        if since == "t1":
            return httpx.Response(200, json={"submissions": beril.rows[1:], "next_since": "t2"})
        return httpx.Response(200, json={"submissions": [], "next_since": since})

    client = hub.Hub("https://beril.test", "pat-1", transport=httpx.MockTransport(paging))
    rows, following = client.submissions(None, limit=1)
    assert [r["project"] for r in rows] == ["demo", "p1"] and following == "t2"
    assert pages == [
        "kind=approved%2Cseeded%2Cdocs&limit=1",
        "kind=approved%2Cseeded%2Cdocs&limit=1&since=t1",
        "kind=approved%2Cseeded%2Cdocs&limit=1&since=t2",
    ]

    def no_cursor(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"submissions": beril.rows[:1]})

    client = hub.Hub("https://beril.test", "pat-1", transport=httpx.MockTransport(no_cursor))
    with pytest.raises(hub.HubError, match="neither next_after nor next_since"):
        client.submissions(None, limit=1)


def test_a_pull_over_next_since_keeps_no_resumable_cursor(out, beril, monkeypatch):
    def paging(request: httpx.Request) -> httpx.Response:
        if request.url.path != "/api/context/submissions":
            return beril.handle(request)
        if request.url.params.get("since") is None:
            return httpx.Response(200, json={"submissions": beril.rows, "next_since": "t1"})
        return httpx.Response(200, json={"submissions": [], "next_since": "t1"})

    client = hub.Hub("https://beril.test", "pat-1", transport=httpx.MockTransport(paging))
    assert corpus.pull_hub(out, client) == {"projects": 1, "docs": 0, "next_after": None}
    assert corpus.load_cursor(out.parent / "state")["next_after"] is None
    assert corpus.pull_hub(out, client)["projects"] == 0  # re-listed, nothing re-downloaded


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


def test_a_cursor_from_the_old_feed_relists_from_the_beginning(out, beril, client):
    corpus.pull_hub(out, client)
    state = out.parent / "state"
    corpus.save_cursor(state, {"url": "https://beril.test", "next_since": "2026-11-01T00:00:00Z"})
    beril.requests.clear()

    done = corpus.pull_hub(out, client)

    assert "after=" not in beril.requests[0]
    assert done == {"projects": 0, "docs": 0, "next_after": 1}  # demo unchanged: not re-downloaded
    assert corpus.load_cursor(state) == {"url": "https://beril.test", "next_after": 1}


def test_a_cursor_still_in_the_manifest_is_read_once_and_moved_out(out, beril, client):
    corpus.pull_hub(out, client)
    state = out.parent / "state"
    (state / corpus.CURSOR).unlink()
    manifest = corpus.load(out)
    manifest["hub"] = {"url": "https://beril.test", "next_after": 1, "docs": {"id": 9}}
    corpus.save(manifest, out)
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-02T00:00:00Z")
    beril.requests.clear()
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert beril.requests[0].endswith("after=1")  # resumed from the manifest's cursor
    assert "hub" not in corpus.load(out)
    assert corpus.load_cursor(state)["docs"] == {"id": 9}
    assert corpus.verify(out) == []


def test_a_moved_cursor_is_not_a_corpus_change_to_the_scope_checks(out, beril, client):
    import importlib.util

    from beril_wiki.agentic.admission import manifest_scope

    spec = importlib.util.spec_from_file_location(
        "check_update", Path(__file__).resolve().parents[1] / "scripts/check_update.py"
    )
    assert spec and spec.loader
    check_update = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(check_update)
    corpus.pull_hub(out, client)
    before = (out / corpus.MANIFEST).read_bytes()
    beril.project("other", {"REPORT.md": b"# other\n"}, "2026-11-02T00:00:00Z", owner=OTHER)
    corpus.pull_hub(out, client)
    beril.project("demo", {"REPORT.md": b"# stale\n"}, "2026-10-31T00:00:00Z")
    corpus.pull_hub(out, client)  # moves the cursor past an older completion
    assert corpus.load_cursor(out.parent / "state")["next_after"] == 3
    base, head = json.loads(before), corpus.load(out)
    assert manifest_scope(base, head, "other") == []
    assert check_update.manifest_stale(base, head, {"other"}) == []


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
    assert json.loads((out.parent / "state/hub.json").read_text())["next_after"] == 1
    assert corpus.main(["verify"]) == 0


def test_a_readme_or_figure_change_without_a_report_change_is_pulled(out, beril, client):
    corpus.pull_hub(out, client)
    # Same REPORT.md (same revision), new README: a run input the manifest fingerprints.
    beril.project(
        "demo",
        {"REPORT.md": REPORT, "figures/plot.png": PLOT, "README.md": README + b"edited\n"},
        "2026-11-02T00:00:00Z",
    )
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert (out / "projects/demo/README.md").read_bytes() == README + b"edited\n"
    # Same report and README, the embedded figure redrawn.
    beril.project(
        "demo",
        {"REPORT.md": REPORT, "figures/plot.png": PLOT + b"v2", "README.md": README + b"edited\n"},
        "2026-11-03T00:00:00Z",
    )
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert (out / "projects/demo/figures/plot.png").read_bytes() == PLOT + b"v2"
    # Nothing new: the row is skipped without a download.
    beril.requests.clear()
    assert corpus.pull_hub(out, client)["projects"] == 0
    assert all("/api/context/read" not in r for r in beril.requests)
    assert corpus.verify(out) == []


def test_an_identical_later_submission_keeps_its_date_so_an_older_one_is_rejected(
    out, beril, client
):
    corpus.pull_hub(out, client)
    files = dict(beril.files[f"{ORCID}/demo"])
    # C: identical bytes, dated Nov 3, completes first; B: different bytes, dated Nov 2,
    # completes after C. read now serves C's bytes, so B must be skipped, not fetched.
    beril.project("demo", files, "2026-11-03T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 0
    assert corpus.load(out)["projects"]["demo"]["submitted_at"] == "2026-11-03T00:00:00Z"
    beril.project("demo", files | {"README.md": b"# older edit\n"}, "2026-11-02T00:00:00Z")
    beril.requests.clear()
    assert corpus.pull_hub(out, client)["projects"] == 0
    assert all("/api/context/read" not in r for r in beril.requests)
    assert (out / "projects/demo/README.md").read_bytes() == README
    assert corpus.verify(out) == []


def test_an_older_docs_submission_completing_later_is_skipped(out, beril, client):
    newer = {"discoveries.md": b"# discoveries v2\n", "pitfalls.md": b"# pitfalls v2\n"}
    beril.project("docs", newer, "2026-11-05T00:00:00Z", kind="docs", owner="beril")
    assert corpus.pull_hub(out, client)["docs"] == 2
    assert (
        corpus.load_cursor(out.parent / "state")["docs"]["submitted_at"] == "2026-11-05T00:00:00Z"
    )
    older = {"discoveries.md": b"# discoveries v1\n"}
    beril.project("docs", older, "2026-11-04T00:00:00Z", kind="docs", owner="beril")
    result = corpus.pull_hub(out, client)
    assert result["docs"] == 0 and result["next_after"] == len(beril.rows)
    assert (out / "docs/discoveries.md").read_bytes() == newer["discoveries.md"]
    assert corpus.verify(out) == []


def test_a_removed_readme_or_figure_without_a_report_change_is_pulled(out, beril, client):
    corpus.pull_hub(out, client)
    assert (out / "projects/demo/README.md").exists()
    # Same report, README withdrawn from the submission: stale author metadata must go.
    beril.project("demo", {"REPORT.md": REPORT, "figures/plot.png": PLOT}, "2026-11-02T00:00:00Z")
    assert corpus.pull_hub(out, client)["projects"] == 1
    assert not (out / "projects/demo/README.md").exists()
    assert "README.md" not in corpus.load(out)["projects"]["demo"]["files"]
    assert corpus.verify(out) == []


def test_an_install_interrupted_between_swaps_is_undone_and_the_next_pull_retries(
    out, beril, client, monkeypatch, capsys
):
    """After every download verified, the trees are swapped in one by one. A failure
    between two swaps (here: placing the second project) must not leave the first
    project new while the manifest, cursor and second project are old."""
    corpus.pull_hub(out, client)
    before = {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()}
    cursor = (out.parent / "state/hub.json").read_bytes()
    beril.project("demo", {"REPORT.md": REPORT + b"v2\n"}, "2026-11-02T00:00:00Z")
    beril.project("later", {"REPORT.md": b"# later\n"}, "2026-11-03T00:00:00Z")
    rename = corpus.os.rename

    def failing(src, dst):
        if Path(dst) == out / "projects/later":  # demo is already swapped by now
            raise OSError("disk full")
        rename(src, dst)

    monkeypatch.setattr(corpus.os, "rename", failing)
    # First, the process dies with the journal in place: nothing undoes it inline.
    monkeypatch.setattr(corpus, "recover", lambda c=None: False)
    with pytest.raises(OSError, match="disk full"):
        corpus.pull_hub(out, client)
    assert (out / corpus.JOURNAL).is_file()
    assert (out / "projects/demo/REPORT.md").read_bytes() == REPORT + b"v2\n"  # split
    assert not (out / "projects/later").exists()
    monkeypatch.undo()
    monkeypatch.setattr(corpus.os, "rename", failing)
    # The next pull recovers before it reads the manifest, then fails the same way;
    # this time the inline recovery puts the corpus back.
    with pytest.raises(OSError, match="disk full"):
        corpus.pull_hub(out, client)
    assert not (out / corpus.JOURNAL).exists()
    assert {p.relative_to(out): p.read_bytes() for p in out.rglob("*") if p.is_file()} == before
    assert (out.parent / "state/hub.json").read_bytes() == cursor
    assert list(out.parent.glob(".corpus-pull-*")) == []
    assert corpus.verify(out) == []
    assert "interrupted pull-hub install was undone" in capsys.readouterr().err
    monkeypatch.undo()
    assert corpus.pull_hub(out, client)["projects"] == 2
    assert (out / "projects/later/REPORT.md").read_bytes() == b"# later\n"
    assert corpus.verify(out) == []


def test_verify_undoes_an_interrupted_install_first(out, beril, client, monkeypatch):
    corpus.pull_hub(out, client)
    beril.project("demo", {"REPORT.md": REPORT + b"v2\n"}, "2026-11-02T00:00:00Z")
    monkeypatch.setattr(corpus, "save", lambda m, c: (_ for _ in ()).throw(OSError("full")))
    monkeypatch.setattr(corpus, "recover", lambda c=None: False)
    with pytest.raises(OSError, match="full"):
        corpus.pull_hub(out, client)
    monkeypatch.undo()
    assert (out / corpus.JOURNAL).is_file()
    assert corpus.verify(out) == []
    assert (out / "projects/demo/REPORT.md").read_bytes() == REPORT
    assert corpus.load(out)["projects"]["demo"]["submitted_at"] == "2026-11-01T00:00:00Z"
    # A journal whose staging directory is gone cannot be undone silently.
    (out / corpus.JOURNAL).write_text(
        json.dumps({"staging": ".nowhere", "state": "state", "moves": []})
    )
    with pytest.raises(hub.HubError, match="staging directory .* is gone"):
        corpus.verify(out)
