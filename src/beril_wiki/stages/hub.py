"""Read project files from BERIL's context API, never from OpenViking directly.

The wiki runs off-cluster and reaches the observatory's projects only through two
BERIL routes, with a BERIL personal access token (``BERIL_URL``, ``BERIL_TOKEN``):

  GET /api/context/submissions?since=<iso>&kind=approved,seeded&limit=<n>
      the "changed since" feed: one row per completed ingest batch, ascending,
      each naming the project's files and their sha256; ``next_since`` continues.
  GET /api/context/read?address=<owner>/<project>/<path>
      one allowlisted file (REPORT.md, README.md, beril.yaml, CORRECTIONS.md,
      REFUTATION_<n>.md, figures/**). Asked for as raw bytes so what the wiki
      hashes and quotes is byte-exact.

The feed is incremental, so ``state/hub.json`` keeps the merged view of every
project ever reported plus the ``next_since`` to continue from; a run stages all
of them, as the local backend stages every checkout report. Every download is
checked against the sha256 the feed declared for the path (or, for a file the
feed does not list, the one the route itself declares) and refused on mismatch.
"""

from __future__ import annotations

import base64
import hashlib
import json
import os
import pathlib
import re
from typing import Any

import httpx

FEED_PAGE = 200
STATE_FILE = "hub.json"
KINDS = "approved,seeded"
TEXT_FILES = ("REPORT.md", "beril.yaml", "README.md")
SAFE_PATH = re.compile(r"^(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+$")


class HubError(RuntimeError):
    """A hub read that must stop the stage: no token, a refused file, a bad hash."""


def settings() -> tuple[str, str]:
    url = os.environ.get("BERIL_URL", "").rstrip("/")
    token = os.environ.get("BERIL_TOKEN", "")
    if not url or not token:
        raise HubError("FETCH_BACKEND=hub needs BERIL_URL and BERIL_TOKEN")
    return url, token


def safe_path(path: str) -> str:
    if not SAFE_PATH.fullmatch(path) or ".." in path.split("/"):
        raise HubError(f"unsafe project path {path!r}")
    return path


class Hub:
    """One authenticated client. ``transport`` is for tests (httpx.MockTransport)."""

    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        transport: httpx.BaseTransport | None = None,
        timeout: float = 60.0,
    ) -> None:
        if url is None or token is None:
            url, token = settings()
        self.url = url.rstrip("/")
        self.client = httpx.Client(
            base_url=self.url,
            headers={"Authorization": f"Bearer {token}", "User-Agent": "beril-wiki/fetch"},
            timeout=timeout,
            transport=transport,
            follow_redirects=False,
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> Hub:
        return self

    def __exit__(self, *exc: object) -> None:
        self.close()

    def submissions(self, since: str | None, limit: int = FEED_PAGE) -> list[dict]:
        """Every feed row after ``since``, in order, following ``next_since``."""
        rows: list[dict] = []
        seen: set[str | None] = set()
        while True:
            params: dict[str, Any] = {"kind": KINDS, "limit": limit}
            if since:
                params["since"] = since
            r = self.client.get("/api/context/submissions", params=params)
            if r.status_code != 200:
                raise HubError(f"submissions feed: HTTP {r.status_code} {r.text[:200]}")
            body = r.json()
            page = body.get("submissions") or []
            rows.extend(page)
            following = body.get("next_since")
            if not page or not following or following == since or following in seen:
                break
            seen.add(since)
            since = following
        return rows

    def read(self, address: str) -> tuple[bytes, str | None, str | None]:
        """A file's exact bytes, the sha256 the route declares, and its source."""
        r = self.client.get(
            "/api/context/read",
            params={"address": address},
            headers={"Accept": "application/octet-stream"},
        )
        if r.status_code == 404:
            raise HubError(f"read {address}: not found")
        if r.status_code != 200:
            raise HubError(f"read {address}: HTTP {r.status_code} {r.text[:200]}")
        if r.headers.get("content-type", "").startswith("application/json"):
            # A server that answers JSON regardless: decode per its own encoding field.
            body = r.json()
            raw = body.get("content", "")
            data = (
                base64.b64decode(raw) if body.get("encoding") == "base64" else raw.encode("utf-8")
            )
            return data, body.get("sha256"), body.get("source")
        return r.content, r.headers.get("x-content-sha256"), r.headers.get("x-content-source")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_state(root: pathlib.Path) -> dict:
    path = root / "state" / STATE_FILE
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    return {"next_since": None, "projects": {}}


def save_state(root: pathlib.Path, state: dict) -> None:
    path = root / "state" / STATE_FILE
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def merge(state: dict, rows: list[dict]) -> dict:
    """The state after the feed rows: later rows for a project replace earlier ones."""
    projects = dict(state.get("projects", {}))
    latest = state.get("next_since")
    for row in rows:
        project = row["project"]
        if not re.fullmatch(r"[A-Za-z0-9_.-]+", project):
            raise HubError(f"feed names an unsafe project id {project!r}")
        files = {safe_path(f["path"]): f["sha256"] for f in row.get("files", [])}
        projects[project] = {
            "address": row["address"],
            "owner_orcid": row.get("owner_orcid"),
            "submitted_at": row.get("submitted_at"),
            "kind": row.get("kind"),
            "batch_id": row.get("batch_id"),
            "is_public": row.get("is_public", True),
            "files": files,
        }
        if row.get("submitted_at") and (latest is None or row["submitted_at"] > latest):
            latest = row["submitted_at"]
    return {"next_since": latest, "projects": dict(sorted(projects.items()))}


def sync(hub: Hub, state: dict) -> dict:
    """The state brought up to the feed's head; the same object when nothing changed."""
    rows = hub.submissions(state.get("next_since"))
    return merge(state, rows) if rows else state


def fingerprint(state: dict) -> dict[str, str]:
    """What a run depends on from the hub: every served project's files and hashes.

    This replaces the checkout fingerprint (`runner.checkout_inputs`) in hub mode.
    Projects the feed marks private are not served and so not part of it."""
    out: dict[str, str] = {}
    for project, entry in state.get("projects", {}).items():
        if entry.get("is_public", True) is False:
            continue
        for path, sha in sorted(entry.get("files", {}).items()):
            out[f"projects/{project}/{path}"] = sha
    return out


def served(state: dict) -> dict[str, dict]:
    return {
        p: e for p, e in state.get("projects", {}).items() if e.get("is_public", True) is not False
    }


def fetch_file(hub: Hub, entry: dict, path: str, required: bool = True) -> bytes | None:
    """One project file, verified against the feed's hash for it when the feed has one
    and against the route's own declared hash otherwise."""
    address = f"{entry['address'].strip('/')}/{safe_path(path)}"
    try:
        data, declared, _source = hub.read(address)
    except HubError:
        if required:
            raise
        return None
    expected = entry.get("files", {}).get(path) or declared
    if not expected:
        raise HubError(f"{address}: neither the feed nor the route declares a sha256")
    actual = sha256(data)
    if actual != expected:
        raise HubError(f"{address}: sha256 {actual} does not match declared {expected}")
    return data
