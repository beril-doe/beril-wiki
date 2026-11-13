"""Versioned site artifacts in an S3-compatible bucket, so a rebuilt wiki goes live
without a commit, an image build or a rollout.

    uv run python -m beril_wiki.publish.artifact push [--site quartz/public] [--id ID]
    uv run python -m beril_wiki.publish.artifact rollback --to ID
    uv run python -m beril_wiki.publish.artifact current
    uv run python -m beril_wiki.publish.artifact corpus DIR   # the corpus/ tree alone

`push` packs the rendered site plus the Markdown the MCP tools answer from
(wiki/sources, wiki/findings, wiki/directions and a fresh cards.json) as
``<prefix>/site-<id>.tar.gz`` beside ``<prefix>/site-<id>.manifest.json``, then
rewrites ``<prefix>/current.json`` to point at it. The server (beril_wiki.serve)
downloads ``current`` on start and on ``POST /wiki/_admin/reload``, unpacks it
beside the live tree and swaps. Rollback is moving the pointer.

Store configuration, from the environment on both sides:
  WIKI_ARTIFACT_ENDPOINT    S3 endpoint URL (MinIO, Ceph, AWS); or ``file:///dir``
                            for a directory store, which needs no S3 at all
  WIKI_ARTIFACT_BUCKET      bucket name (ignored by the directory store)
  WIKI_ARTIFACT_PREFIX      key prefix inside the bucket (default ``wiki``)
  WIKI_ARTIFACT_ACCESS_KEY, WIKI_ARTIFACT_SECRET_KEY
  WIKI_ARTIFACT_REGION      optional, default us-east-1

gzip rather than zstd: the standard library reads and writes it, so the server
image carries no native extension for it, and a site of this size unpacks in
seconds either way. Only the store client (boto3, the `publish` and `serve`
groups) is imported lazily, so the server imports this module without it when
no store is configured. This module imports nothing else from the package at
import time: it ships in the server image with serve.py.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from collections.abc import Mapping
from typing import Any, Protocol

ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")
CORPUS_DIRS = ("sources", "findings", "directions")
MANIFEST_VERSION = 1


class ArtifactError(RuntimeError):
    pass


# --------------------------------------------------------------------------- store


class Store(Protocol):
    def get(self, key: str) -> bytes: ...

    def put(self, key: str, data: bytes, content_type: str) -> None: ...

    def exists(self, key: str) -> bool: ...


class DirStore:
    """A directory standing in for a bucket (``file:///path``); for local tests and
    for a single host that shares a volume between the curator and the server."""

    def __init__(self, root: pathlib.Path) -> None:
        self.root = root

    def _path(self, key: str) -> pathlib.Path:
        p = (self.root / key).resolve()
        if not p.is_relative_to(self.root.resolve()):
            raise ArtifactError(f"key escapes the store: {key}")
        return p

    def get(self, key: str) -> bytes:
        try:
            return self._path(key).read_bytes()
        except FileNotFoundError as exc:
            raise ArtifactError(f"missing object {key}") from exc

    def put(self, key: str, data: bytes, content_type: str) -> None:
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(p.name + ".tmp")
        tmp.write_bytes(data)
        os.replace(tmp, p)

    def exists(self, key: str) -> bool:
        return self._path(key).is_file()


class S3Store:
    def __init__(
        self, endpoint: str, bucket: str, access_key: str, secret_key: str, region: str
    ) -> None:
        import boto3
        from botocore.config import Config

        self.bucket = bucket
        self.client = boto3.client(
            "s3",
            endpoint_url=endpoint,
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region,
            config=Config(s3={"addressing_style": "path"}, retries={"max_attempts": 3}),
        )

    def get(self, key: str) -> bytes:
        try:
            return self.client.get_object(Bucket=self.bucket, Key=key)["Body"].read()
        except self.client.exceptions.NoSuchKey as exc:
            raise ArtifactError(f"missing object {key}") from exc

    def put(self, key: str, data: bytes, content_type: str) -> None:
        self.client.put_object(Bucket=self.bucket, Key=key, Body=data, ContentType=content_type)

    def exists(self, key: str) -> bool:
        try:
            self.client.head_object(Bucket=self.bucket, Key=key)
            return True
        except self.client.exceptions.ClientError:
            return False


def configured(env: Mapping[str, str] | None = None) -> bool:
    env = os.environ if env is None else env
    return bool(env.get("WIKI_ARTIFACT_ENDPOINT"))


def store_from_env(env: Mapping[str, str] | None = None) -> Store:
    env = os.environ if env is None else env
    endpoint = env.get("WIKI_ARTIFACT_ENDPOINT", "")
    if not endpoint:
        raise ArtifactError("WIKI_ARTIFACT_ENDPOINT is not set")
    if endpoint.startswith("file://"):
        return DirStore(pathlib.Path(endpoint.removeprefix("file://")))
    missing = [
        k
        for k in ("WIKI_ARTIFACT_BUCKET", "WIKI_ARTIFACT_ACCESS_KEY", "WIKI_ARTIFACT_SECRET_KEY")
        if not env.get(k)
    ]
    if missing:
        raise ArtifactError(f"artifact store needs {', '.join(missing)}")
    return S3Store(
        endpoint,
        env["WIKI_ARTIFACT_BUCKET"],
        env["WIKI_ARTIFACT_ACCESS_KEY"],
        env["WIKI_ARTIFACT_SECRET_KEY"],
        env.get("WIKI_ARTIFACT_REGION", "us-east-1"),
    )


def prefix_from_env(env: Mapping[str, str] | None = None) -> str:
    env = os.environ if env is None else env
    return env.get("WIKI_ARTIFACT_PREFIX", "wiki").strip("/")


class Keys:
    def __init__(self, prefix: str) -> None:
        self.prefix = prefix.strip("/")

    def _join(self, name: str) -> str:
        return f"{self.prefix}/{name}" if self.prefix else name

    def tarball(self, artifact_id: str) -> str:
        return self._join(f"site-{check_id(artifact_id)}.tar.gz")

    def manifest(self, artifact_id: str) -> str:
        return self._join(f"site-{check_id(artifact_id)}.manifest.json")

    @property
    def current(self) -> str:
        return self._join("current.json")


def check_id(artifact_id: str) -> str:
    if not ID_RE.fullmatch(artifact_id):
        raise ArtifactError(f"bad artifact id {artifact_id!r}")
    return artifact_id


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------- pack


def count_pages(site: pathlib.Path) -> int:
    return sum(1 for _ in site.rglob("*.html"))


def new_id(root: pathlib.Path, now: dt.datetime | None = None) -> str:
    """UTC timestamp plus the accepted run's fingerprint prefix (or the git commit)."""
    now = now or dt.datetime.now(dt.UTC)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    agentic = root / "state/agentic.json"
    tag = ""
    if agentic.exists():
        tag = json.loads(agentic.read_text(encoding="utf-8")).get("fingerprint", "")[:8]
    if not tag:
        r = subprocess.run(
            ["git", "-C", str(root), "rev-parse", "--short=8", "HEAD"],
            capture_output=True,
            text=True,
        )
        tag = r.stdout.strip() if r.returncode == 0 else "local"
    return f"{stamp}-{tag}"


def build_manifest(
    root: pathlib.Path, site: pathlib.Path, artifact_id: str, base_url: str | None
) -> dict:
    agentic_path = root / "state/agentic.json"
    agentic = json.loads(agentic_path.read_text(encoding="utf-8")) if agentic_path.exists() else {}
    sources = {p.name: sha256(p.read_bytes()) for p in sorted((root / "wiki/sources").glob("*.md"))}
    return {
        "version": MANIFEST_VERSION,
        "id": artifact_id,
        "created_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "page_count": count_pages(site),
        "base_url": base_url,
        "git_commit": os.environ.get("BERIL_WIKI_GIT_COMMIT") or _git_commit(root),
        "agentic": {k: agentic.get(k) for k in ("fingerprint", "revision", "contract") if agentic},
        "sources": sources,
    }


def _git_commit(root: pathlib.Path) -> str | None:
    r = subprocess.run(
        ["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True
    )
    return r.stdout.strip() or None if r.returncode == 0 else None


def corpus_files(root: pathlib.Path) -> dict[str, bytes]:
    """The Markdown and records the MCP tools answer from, as archive members."""
    out: dict[str, bytes] = {}
    for folder in CORPUS_DIRS:
        for p in sorted((root / "wiki" / folder).glob("*.md")):
            out[f"corpus/{folder}/{p.name}"] = p.read_bytes()
    try:
        from beril_wiki.publish import cards
        from beril_wiki.publish.cards.export import export

        out["corpus/cards.json"] = json.dumps(export(cards.Corpus(root)), indent=1).encode()
    except Exception as exc:  # the corpus may have no records yet
        print(f"artifact: no cards.json ({exc})", file=sys.stderr)
    return out


def write_corpus(root: pathlib.Path, dest: pathlib.Path) -> int:
    """The corpus/ tree as files, for the image's baked fallback (scripts/build_quartz.sh)."""
    if dest.exists():
        shutil.rmtree(dest)
    files = corpus_files(root)
    for name, data in files.items():
        target = dest / name.removeprefix("corpus/")
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return len(files)


def pack(root: pathlib.Path, site: pathlib.Path, manifest: dict) -> bytes:
    """site/ (the rendered pages), corpus/ (Markdown + cards.json), manifest.json."""
    if not (site / "index.html").is_file():
        raise ArtifactError(f"{site} holds no built site (no index.html)")
    buf = io.BytesIO()
    with tarfile.open(fileobj=buf, mode="w:gz", compresslevel=6) as tar:

        def add_bytes(name: str, data: bytes) -> None:
            info = tarfile.TarInfo(name)
            info.size = len(data)
            info.mtime = 0
            info.mode = 0o644
            tar.addfile(info, io.BytesIO(data))

        add_bytes("manifest.json", json.dumps(manifest, indent=1).encode())
        for path in sorted(site.rglob("*")):
            if path.is_symlink():
                raise ArtifactError(f"symlink in site: {path}")
            if path.is_file():
                add_bytes(f"site/{path.relative_to(site).as_posix()}", path.read_bytes())
        for name, data in corpus_files(root).items():
            add_bytes(name, data)
    return buf.getvalue()


def push(
    store: Store,
    keys: Keys,
    root: pathlib.Path,
    site: pathlib.Path,
    artifact_id: str | None = None,
    base_url: str | None = None,
) -> dict:
    artifact_id = check_id(artifact_id or new_id(root))
    if store.exists(keys.tarball(artifact_id)):
        raise ArtifactError(f"artifact {artifact_id} already exists; artifacts are immutable")
    manifest = build_manifest(root, site, artifact_id, base_url)
    data = pack(root, site, manifest)
    manifest["tarball_sha256"] = sha256(data)
    manifest["tarball_bytes"] = len(data)
    store.put(keys.tarball(artifact_id), data, "application/gzip")
    store.put(
        keys.manifest(artifact_id), json.dumps(manifest, indent=1).encode(), "application/json"
    )
    pointer = point(store, keys, artifact_id, manifest)
    return pointer


def point(store: Store, keys: Keys, artifact_id: str, manifest: dict | None = None) -> dict:
    """Rewrite current.json; the tarball and manifest must already exist."""
    if manifest is None:
        if not store.exists(keys.tarball(artifact_id)):
            raise ArtifactError(f"no artifact {artifact_id} in the store")
        manifest = json.loads(store.get(keys.manifest(artifact_id)))
    previous = None
    if store.exists(keys.current):
        previous = json.loads(store.get(keys.current)).get("id")
    pointer = {
        "id": artifact_id,
        "tarball": keys.tarball(artifact_id),
        "manifest": keys.manifest(artifact_id),
        "sha256": manifest.get("tarball_sha256"),
        "page_count": manifest.get("page_count"),
        "updated_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "previous": previous,
    }
    store.put(keys.current, json.dumps(pointer, indent=1).encode(), "application/json")
    return pointer


def current(store: Store, keys: Keys) -> dict:
    try:
        return json.loads(store.get(keys.current))
    except ArtifactError as exc:
        raise ArtifactError("no current artifact is published") from exc


# -------------------------------------------------------------------- unpack (server)


def verify_manifest(unpacked: pathlib.Path, artifact_id: str) -> dict:
    manifest_path = unpacked / "manifest.json"
    if not manifest_path.is_file():
        raise ArtifactError("artifact has no manifest.json")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("id") != artifact_id:
        raise ArtifactError(f"manifest id {manifest.get('id')!r} is not {artifact_id!r}")
    site = unpacked / "site"
    if not (site / "index.html").is_file():
        raise ArtifactError("artifact site has no index.html")
    pages = count_pages(site)
    if manifest.get("page_count") != pages:
        raise ArtifactError(f"manifest says {manifest.get('page_count')} pages, found {pages}")
    return manifest


def unpack(data: bytes, dest: pathlib.Path, artifact_id: str, expected_sha: str | None) -> dict:
    """Extract into ``dest`` (replacing any partial earlier attempt) and verify."""
    if expected_sha and sha256(data) != expected_sha:
        raise ArtifactError("tarball sha256 does not match current.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=f".site-{artifact_id}.", dir=dest.parent))
    try:
        with tarfile.open(fileobj=io.BytesIO(data), mode="r:gz") as tar:
            tar.extractall(tmp, filter="data")
        manifest = verify_manifest(tmp, artifact_id)
        if dest.exists():
            shutil.rmtree(dest)
        os.replace(tmp, dest)
    except BaseException:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    return manifest


def sync(store: Store, keys: Keys, site_root: pathlib.Path) -> tuple[str, pathlib.Path, dict]:
    """Make the current artifact present under ``site_root/site-<id>/``; download only
    when it is not. Returns (id, unpacked dir, manifest)."""
    pointer = current(store, keys)
    artifact_id = check_id(pointer["id"])
    dest = site_root / f"site-{artifact_id}"
    site_root.mkdir(parents=True, exist_ok=True)
    if dest.is_dir():
        try:
            return artifact_id, dest, verify_manifest(dest, artifact_id)
        except ArtifactError:
            shutil.rmtree(dest)
    data = store.get(pointer["tarball"])
    manifest = unpack(data, dest, artifact_id, pointer.get("sha256"))
    return artifact_id, dest, manifest


def prune(site_root: pathlib.Path, keep: set[str]) -> list[str]:
    """Remove unpacked artifacts other than ``keep``; the store keeps every version."""
    removed = []
    for d in site_root.glob("site-*"):
        if d.is_dir() and d.name.removeprefix("site-") not in keep:
            shutil.rmtree(d)
            removed.append(d.name)
    return removed


# ----------------------------------------------------------------------------- CLI


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("push", help="pack the built site and make it current")
    p.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    p.add_argument("--site", type=pathlib.Path, default=None, help="default <root>/quartz/public")
    p.add_argument("--id", dest="artifact_id", default=None)
    p.add_argument("--base-url", default=os.environ.get("WIKI_BASE_URL"))
    r = sub.add_parser("rollback", help="point current at an earlier artifact")
    r.add_argument("--to", required=True, dest="artifact_id")
    sub.add_parser("current", help="print current.json")
    c = sub.add_parser("corpus", help="write the corpus/ tree (no store needed)")
    c.add_argument("dest", type=pathlib.Path)
    c.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    args = parser.parse_args(argv)
    if args.command == "corpus":
        n = write_corpus(args.root.resolve(), args.dest.resolve())
        print(f"artifact: wrote {n} corpus file(s) -> {args.dest}")
        return 0
    try:
        store, keys = store_from_env(), Keys(prefix_from_env())
        if args.command == "push":
            root = args.root.resolve()
            site = (args.site or root / "quartz/public").resolve()
            result: Any = push(store, keys, root, site, args.artifact_id, args.base_url)
        elif args.command == "rollback":
            result = point(store, keys, args.artifact_id)
        else:
            result = current(store, keys)
    except ArtifactError as exc:
        print(f"artifact: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
