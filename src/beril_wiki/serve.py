"""Serve the built site (quartz/public) under a URL prefix, as GitHub Pages does.

The container image runs this on SPIN, where the beril.kbase.us ingress routes
/wiki here without rewriting the path, so the prefix is part of every URL the
app sees. The site has to be built for that prefix (WIKI_BASE_URL=<host>/wiki).

    WIKI_SITE_DIR=quartz/public uv run uvicorn beril_wiki.serve:app --port 8080

Quartz links pages without an extension (entities/foo is entities/foo.html),
which Pages resolves implicitly; this does the same, then the site's own 404
page. The trailing slash is canonicalised as Pages does it, because page links
are relative: a folder's index.html (concepts/index.html links ../index.css)
only works at concepts/, and a page only works without the slash, so the wrong
form redirects to the right one rather than serving a page whose links leave
the site.

What is served can change without a restart. When WIKI_ARTIFACT_ENDPOINT is
set (beril_wiki.publish.artifact), the server downloads the `current` artifact
on start into WIKI_SITE_ROOT/site-<id>/ and serves it, falling back to the tree
baked into the image (WIKI_SITE_DIR) when the store is unreachable and nothing
was unpacked before; `POST /wiki/_admin/reload` with `Authorization: Bearer
$WIKI_RELOAD_TOKEN` fetches the current artifact again and swaps to it
atomically (one in-process assignment; a `current` symlink records it for the
next start). `GET /wiki/_admin/status` names the artifact being served. The
MCP tool server (beril_wiki.mcp_server) is mounted at /wiki/mcp and reads the
same artifact.

Only this module, publish/artifact.py, mcp_server.py and the `serve` dependency
group go into the image, so nothing else from the package is imported here.
"""

from __future__ import annotations

import asyncio
import contextlib
import logging
import os
import pathlib
import secrets
from collections.abc import AsyncIterator
from dataclasses import dataclass
from urllib.parse import quote

from fastapi import FastAPI, Request
from fastapi.concurrency import run_in_threadpool
from fastapi.responses import (
    FileResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
    Response,
)

from beril_wiki import mcp_server
from beril_wiki.publish import artifact

log = logging.getLogger("beril_wiki.serve")

# Quartz hashes its bundle names, but not static/ (the search index among it)
# or figures, so a long max-age would pin a stale index after a redeploy.
# Pages themselves are revalidated.
ASSET_CACHE = "public, max-age=300"
PAGE_CACHE = "no-cache"
BAKED = "baked"


def find(root: pathlib.Path, *candidates: str) -> pathlib.Path | None:
    """The first candidate that is a file under root. Never a file outside root."""
    for candidate in candidates:
        f = (root / candidate).resolve()
        if f.is_relative_to(root) and f.is_file():
            return f
    return None


def resolve(root: pathlib.Path, path: str) -> pathlib.Path | str | None:
    """The file a request path names; or, when it names one only with the other
    trailing-slash form, that form (site-relative, to redirect to); or None."""
    rel = path.strip("/")
    if not rel:
        return find(root, "index.html")
    if path.endswith("/"):
        if f := find(root, f"{rel}/index.html"):
            return f
        return rel if find(root, rel, f"{rel}.html") else None
    if f := find(root, rel, f"{rel}.html"):
        return f
    return f"{rel}/" if find(root, f"{rel}/index.html") else None


def file_response(f: pathlib.Path, status_code: int = 200) -> Response:
    cache = PAGE_CACHE if f.suffix == ".html" else ASSET_CACHE
    return FileResponse(f, status_code=status_code, headers={"Cache-Control": cache})


@dataclass(frozen=True)
class Served:
    """What the server hands out right now; replaced whole on a swap."""

    artifact: str
    root: pathlib.Path
    corpus: pathlib.Path | None
    manifest: dict

    def mcp_corpus(self) -> mcp_server.Corpus:
        return mcp_server.Corpus(self.artifact, self.root, self.corpus)


class Site:
    """The swappable served tree, plus the artifact store that can replace it."""

    def __init__(
        self,
        baked: Served,
        site_root: pathlib.Path | None,
        store: artifact.Store | None,
        keys: artifact.Keys | None,
    ) -> None:
        self.baked = baked
        self.current = baked
        self.site_root = site_root
        self.store, self.keys = store, keys
        self._corpus: mcp_server.Corpus | None = None
        self.swap_lock = asyncio.Lock()

    @property
    def corpus(self) -> mcp_server.Corpus:
        c = self._corpus
        if c is None or c.artifact != self.current.artifact:
            c = self._corpus = self.current.mcp_corpus()
        return c

    @property
    def configured(self) -> bool:
        return self.store is not None and self.keys is not None and self.site_root is not None

    @staticmethod
    def unpacked(artifact_id: str, where: pathlib.Path, manifest: dict) -> Served:
        corpus = where / "corpus"
        return Served(artifact_id, where / "site", corpus if corpus.is_dir() else None, manifest)

    def sync(self) -> Served:
        """Download (if needed), verify and swap to the store's current artifact."""
        assert self.store and self.keys and self.site_root
        artifact_id, where, manifest = artifact.sync(self.store, self.keys, self.site_root)
        served = self.unpacked(artifact_id, where, manifest)
        previous = self.current
        self.current = served  # one assignment: a request sees the old tree or the new one
        self.point(where)
        artifact.prune(self.site_root, {artifact_id, previous.artifact})
        return served

    def point(self, where: pathlib.Path) -> None:
        """Record the served artifact as the `current` symlink, atomically."""
        assert self.site_root
        link = self.site_root / "current"
        tmp = self.site_root / f".current.{os.getpid()}.{secrets.token_hex(4)}"
        tmp.symlink_to(where.name)
        os.replace(tmp, link)

    def restore(self) -> Served | None:
        """The artifact the last run left behind the `current` symlink, if still whole."""
        if not self.site_root:
            return None
        link = self.site_root / "current"
        if not link.is_symlink():
            return None
        where = (self.site_root / os.readlink(link)).resolve()
        artifact_id = where.name.removeprefix("site-")
        try:
            manifest = artifact.verify_manifest(where, artifact_id)
        except (artifact.ArtifactError, OSError):
            return None
        self.current = self.unpacked(artifact_id, where, manifest)
        return self.current

    def startup(self) -> None:
        if not self.configured:
            return
        try:
            served = self.sync()
            log.info(
                "serving artifact %s (%s pages)", served.artifact, served.manifest.get("page_count")
            )
        except Exception as exc:  # the store may be down; serve what we have
            restored = self.restore()
            if restored:
                log.warning("artifact store unavailable (%s); serving %s", exc, restored.artifact)
            else:
                log.warning("artifact store unavailable (%s); serving the baked site", exc)


def create_app(
    site_dir: str | os.PathLike[str],
    prefix: str = "/wiki",
    *,
    corpus_dir: str | os.PathLike[str] | None = None,
    site_root: str | os.PathLike[str] | None = None,
    store: artifact.Store | None = None,
    keys: artifact.Keys | None = None,
    reload_token: str | None = None,
    sync_on_start: bool = True,
) -> FastAPI:
    baked_root = pathlib.Path(site_dir).resolve()
    corpus = pathlib.Path(corpus_dir).resolve() if corpus_dir else None
    baked = Served(BAKED, baked_root, corpus if corpus and corpus.is_dir() else None, {})
    site = Site(baked, pathlib.Path(site_root).resolve() if site_root else None, store, keys)
    prefix = "/" + prefix.strip("/")
    mcp = mcp_server.create_mcp(lambda: site.corpus)

    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI) -> AsyncIterator[None]:
        if sync_on_start:
            await run_in_threadpool(site.startup)
        async with mcp.session_manager.run():
            yield

    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)
    app.state.site = site

    def not_found() -> Response:
        page = site.current.root / "404.html"
        if page.is_file():
            return file_response(page, status_code=404)
        return PlainTextResponse("Not Found", status_code=404)

    async def healthz() -> Response:
        return PlainTextResponse("ok")

    async def to_prefix() -> Response:
        return RedirectResponse(prefix + "/", status_code=308)

    async def status() -> Response:
        served = site.current
        m = served.manifest
        return JSONResponse(
            {
                "artifact": served.artifact,
                "created_at": m.get("created_at"),
                "page_count": m.get("page_count"),
                "git_commit": m.get("git_commit") or os.environ.get("BERIL_WIKI_GIT_COMMIT"),
                "store": site.configured,
                "corpus": served.corpus is not None,
            }
        )

    async def reload(request: Request) -> Response:
        if not reload_token or not site.configured:
            return JSONResponse({"error": "reload is not configured"}, status_code=503)
        header = request.headers.get("authorization", "")
        scheme, _, token = header.partition(" ")
        if scheme.lower() != "bearer" or not secrets.compare_digest(token, reload_token):
            return JSONResponse({"error": "unauthorized"}, status_code=401)
        previous = site.current.artifact
        async with site.swap_lock:
            try:
                served = await run_in_threadpool(site.sync)
            except (artifact.ArtifactError, OSError) as exc:
                return JSONResponse({"error": str(exc), "artifact": previous}, status_code=502)
        return JSONResponse(
            {
                "artifact": served.artifact,
                "previous": previous,
                "page_count": served.manifest.get("page_count"),
                "changed": served.artifact != previous,
            }
        )

    async def to_mcp() -> Response:
        # The mount answers at the slash form; 308 keeps the method and body.
        return RedirectResponse(prefix + "/mcp/", status_code=308)

    async def page(request: Request, path: str) -> Response:
        found = resolve(site.current.root, path)
        if isinstance(found, str):
            query = request.url.query
            url = f"{prefix}/{quote(found)}" + (f"?{query}" if query else "")
            return RedirectResponse(url, status_code=308)
        return file_response(found) if found else not_found()

    async def missing(path: str) -> Response:
        return not_found()

    app.add_api_route("/healthz", healthz, methods=["GET"])
    app.add_api_route("/", to_prefix, methods=["GET"])
    app.add_api_route(prefix, to_prefix, methods=["GET"])
    app.add_api_route(prefix + "/_admin/status", status, methods=["GET"])
    app.add_api_route(prefix + "/_admin/reload", reload, methods=["POST"])
    # Mounted before the catch-all so /wiki/mcp is the tool server, not a page lookup.
    app.add_api_route(prefix + "/mcp", to_mcp, methods=["GET", "POST", "DELETE"])
    app.mount(prefix + "/mcp", mcp.streamable_http_app())
    app.add_api_route(prefix + "/{path:path}", page, methods=["GET", "HEAD"])
    app.add_api_route("/{path:path}", missing, methods=["GET", "HEAD"])
    return app


def app_from_env() -> FastAPI:
    store = keys = None
    if artifact.configured():
        try:
            store, keys = artifact.store_from_env(), artifact.Keys(artifact.prefix_from_env())
        except artifact.ArtifactError as exc:
            log.warning("artifact store ignored: %s", exc)
    return create_app(
        os.environ.get("WIKI_SITE_DIR", "/srv/site"),
        os.environ.get("WIKI_PREFIX", "/wiki"),
        corpus_dir=os.environ.get("WIKI_CORPUS_DIR", "/srv/corpus"),
        site_root=os.environ.get("WIKI_SITE_ROOT", "/srv/artifacts"),
        store=store,
        keys=keys,
        reload_token=os.environ.get("WIKI_RELOAD_TOKEN") or None,
    )


app = app_from_env()
