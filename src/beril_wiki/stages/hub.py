"""Read project files from BERIL's context API, never from OpenViking directly.

The wiki runs off-cluster and reaches the observatory's projects only through two
BERIL routes, with a BERIL personal access token (``BERIL_URL``, ``BERIL_TOKEN``):

  GET /api/context/submissions?after=<n>&kind=approved,seeded,docs&limit=<n>
      the "changed since" feed: one row per complete submission, in the order
      they completed, each naming the owner, the project, its revision (sha256
      of REPORT.md), ``submitted_at`` and every file with its sha256;
      ``next_after`` continues. A submission whose figures arrived last
      completes after a newer one, so a project's revisions can come out of
      order: the newest ``submitted_at`` wins. ``kind: docs`` rows carry the
      central digests (owner ``beril``, project ``docs``).
  GET /api/context/read?address=<owner>/<project>/<path>
      one allowlisted file (REPORT.md, README.md, beril.yaml, CORRECTIONS.md,
      REFUTATION_<n>.md, figures/**). Asked for as raw bytes so what the wiki
      hashes and quotes is byte-exact.

``beril_wiki.corpus pull-hub`` drives this client: it keeps the feed cursor in
``corpus/manifest.json`` and writes what it downloads into ``corpus/``. Every
download is checked against the sha256 the feed declared for the path (or, for a
file the feed does not list, the one the route itself declares) and refused on
mismatch.
"""

from __future__ import annotations

import base64
import hashlib
import os
import re
from datetime import UTC, datetime
from typing import Any

import httpx

FEED_PAGE = 200
KINDS = "approved,seeded,docs"
SAFE_PATH = re.compile(r"^(?:[A-Za-z0-9_.-]+/)*[A-Za-z0-9_.-]+$")
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


class HubError(RuntimeError):
    """A hub read that must stop the pull: no token, a refused file, a bad hash."""


def settings() -> tuple[str, str]:
    url = os.environ.get("BERIL_URL", "").rstrip("/")
    token = os.environ.get("BERIL_TOKEN", "")
    if not url or not token:
        raise HubError("corpus pull-hub needs BERIL_URL and BERIL_TOKEN")
    return url, token


def safe_path(path: str) -> str:
    if not SAFE_PATH.fullmatch(path) or ".." in path.split("/"):
        raise HubError(f"unsafe project path {path!r}")
    return path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


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
            headers={"Authorization": f"Bearer {token}", "User-Agent": "beril-wiki/corpus"},
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

    def submissions(
        self, after: int | None, limit: int = FEED_PAGE
    ) -> tuple[list[dict], int | None]:
        """Every feed row after ``after``, in feed order, following
        ``next_after``; and the cursor to resume from (``after`` itself when
        nothing is new)."""
        rows: list[dict] = []
        seen: set[int | None] = set()
        while True:
            params: dict[str, Any] = {"kind": KINDS, "limit": limit}
            if after is not None:
                params["after"] = after
            r = self.client.get("/api/context/submissions", params=params)
            if r.status_code != 200:
                raise HubError(f"submissions feed: HTTP {r.status_code} {r.text[:200]}")
            body = r.json()
            page = body.get("submissions") or []
            rows.extend(page)
            following = body.get("next_after")
            if not page or following is None or following == after or following in seen:
                break
            seen.add(after)
            after = following
        return rows, (following if page and following is not None else after)

    def read(self, address: str) -> tuple[bytes, str | None]:
        """A file's exact bytes and the sha256 the route declares for them."""
        r = self.client.get(
            "/api/context/read",
            params={"address": address},
            headers={"Accept": "application/octet-stream"},
        )
        if r.status_code != 200:
            raise HubError(f"read {address}: HTTP {r.status_code} {r.text[:200]}")
        if r.headers.get("content-type", "").startswith("application/json"):
            # A server that answers JSON regardless: decode per its own encoding field.
            body = r.json()
            raw = body.get("content", "")
            data = (
                base64.b64decode(raw) if body.get("encoding") == "base64" else raw.encode("utf-8")
            )
            return data, body.get("sha256")
        return r.content, r.headers.get("x-content-sha256")

    def fetch(self, address: str, expected: str | None) -> bytes:
        """``address`` verified against ``expected`` (the feed's hash) or, when the
        feed did not list the file, against the hash the route declares."""
        data, declared = self.read(address)
        expected = expected or declared
        if not expected:
            raise HubError(f"{address}: neither the feed nor the route declares a sha256")
        if (actual := sha256(data)) != expected:
            raise HubError(f"{address}: sha256 {actual} does not match declared {expected}")
        return data


def submitted(entry: dict) -> datetime:
    """A feed row's (or manifest entry's) ``submitted_at``; the earliest
    instant when it has none, so anything dated wins over it."""
    value = entry.get("submitted_at")
    if not value:
        return datetime.min.replace(tzinfo=UTC)
    when = datetime.fromisoformat(str(value))
    return when if when.tzinfo else when.replace(tzinfo=UTC)


def latest(rows: list[dict]) -> dict[tuple[str, str], dict]:
    """The newest row per (owner, project) by ``submitted_at`` (the later
    feed row on a tie), with every name and path checked. Feed order is
    completion order, so the last row for a project need not be its newest."""
    out: dict[tuple[str, str], dict] = {}
    for row in rows:
        owner, project = str(row.get("owner_orcid") or ""), str(row.get("project") or "")
        if not SAFE_NAME.fullmatch(owner) or not SAFE_NAME.fullmatch(project):
            raise HubError(f"feed names an unsafe owner/project {owner!r}/{project!r}")
        files = {safe_path(f["path"]): f["sha256"] for f in row.get("files", [])}
        address = str(row.get("address") or f"{owner}/{project}").strip("/")
        if safe_path(address) != f"{owner}/{project}":
            raise HubError(f"feed address {address!r} is not {owner}/{project}")
        kept = out.get((owner, project))
        if kept is None or submitted(row) >= submitted(kept):
            out[(owner, project)] = row | {"files": files, "address": address}
    return out
