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
the site. Only this module and its two dependencies (the `serve` group) go into
the image, so it imports nothing else from the package.
"""

from __future__ import annotations

import os
import pathlib
from urllib.parse import quote

from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import FileResponse, PlainTextResponse, RedirectResponse, Response
from starlette.routing import Route

# Quartz hashes its bundle names, but not static/ (the search index among it)
# or figures, so a long max-age would pin a stale index after a redeploy.
# Pages themselves are revalidated.
ASSET_CACHE = "public, max-age=300"
PAGE_CACHE = "no-cache"


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


def create_app(site_dir: str | os.PathLike[str], prefix: str = "/wiki") -> Starlette:
    root = pathlib.Path(site_dir).resolve()
    prefix = "/" + prefix.strip("/")

    def not_found() -> Response:
        page = root / "404.html"
        if page.is_file():
            return file_response(page, status_code=404)
        return PlainTextResponse("Not Found", status_code=404)

    async def healthz(request: Request) -> Response:
        return PlainTextResponse("ok")

    async def to_prefix(request: Request) -> Response:
        return RedirectResponse(prefix + "/", status_code=308)

    async def page(request: Request) -> Response:
        found = resolve(root, request.path_params["path"])
        if isinstance(found, str):
            query = request.url.query
            url = f"{prefix}/{quote(found)}" + (f"?{query}" if query else "")
            return RedirectResponse(url, status_code=308)
        return file_response(found) if found else not_found()

    async def missing(request: Request) -> Response:
        return not_found()

    return Starlette(
        routes=[
            Route("/healthz", healthz),
            Route("/", to_prefix),
            Route(prefix, to_prefix),
            Route(prefix + "/{path:path}", page, methods=["GET", "HEAD"]),
            Route("/{path:path}", missing, methods=["GET", "HEAD"]),
        ]
    )


app = create_app(
    os.environ.get("WIKI_SITE_DIR", "/srv/site"),
    os.environ.get("WIKI_PREFIX", "/wiki"),
)
