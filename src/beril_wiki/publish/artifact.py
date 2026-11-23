"""Versioned site artifacts in an S3-compatible bucket, so a rebuilt wiki goes live
without a commit, an image build or a rollout.

    uv run python -m beril_wiki.publish.artifact push [--site quartz/public] [--id ID]
    uv run python -m beril_wiki.publish.artifact rollback --to ID
    uv run python -m beril_wiki.publish.artifact current
    uv run python -m beril_wiki.publish.artifact corpus DIR   # the corpus/ tree alone

`push` packs the rendered site plus the Markdown the internal API answers from
(wiki/sources, wiki/findings, wiki/directions and a fresh cards.json) as
``<prefix>/site-<id>.tar.gz`` beside ``<prefix>/site-<id>.manifest.json``, then
rewrites ``<prefix>/current.json`` to point at it. The server (beril_wiki.serve)
downloads ``current`` on start and on ``POST /wiki/_admin/reload``, unpacks it
beside the live tree and swaps. Rollback is moving the pointer.

Store configuration, from the environment on both sides:
  WIKI_ARTIFACT_ENDPOINT    S3 endpoint URL (MinIO, Ceph, AWS); ``file:///dir`` for a
                            directory store, which needs no S3 at all; or the wiki
                            server's own store routes, ``http(s)://host/wiki/_admin/store``,
                            with WIKI_RELOAD_TOKEN as the bearer (a curator job that
                            shares neither a bucket nor a volume with the server)
  WIKI_ARTIFACT_BUCKET      bucket name (ignored by the directory store)
  WIKI_ARTIFACT_PREFIX      key prefix inside the bucket (default ``wiki``)
  WIKI_ARTIFACT_ACCESS_KEY, WIKI_ARTIFACT_SECRET_KEY
  WIKI_ARTIFACT_REGION      optional, default us-east-1
  WIKI_PUBLISH_LEASE_SECONDS  how long ``<prefix>/publish.lease`` (held by push and
                            rollback) outlives a publisher that died; default 3600
  WIKI_ARTIFACT_MAX_MEMBERS, WIKI_ARTIFACT_MAX_UNPACKED_BYTES,
  WIKI_ARTIFACT_MAX_MEMBER_BYTES
                            what the server will extract from one artifact
                            (default 50000 members, 4 GiB in all, 1 GiB each)

gzip rather than zstd: the standard library reads and writes it, so the server
image carries no native extension for it, and a site of this size unpacks in
seconds either way. Only the store client (boto3, the `publish` and `serve`
groups) is imported lazily, so the server imports this module without it when
no store is configured. This module imports nothing else from the package at
import time: it ships in the server image with serve.py.
"""

from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import hashlib
import io
import json
import os
import pathlib
import re
import secrets
import shutil
import socket
import subprocess
import sys
import tarfile
import tempfile
from collections.abc import Iterable, Iterator, Mapping
from typing import Any, Protocol
from urllib.parse import quote

ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,99}$")
# A store key: slash-separated segments of safe characters, none of them `.` or `..`.
KEY_RE = re.compile(r"^[A-Za-z0-9_][A-Za-z0-9._-]*(/[A-Za-z0-9_][A-Za-z0-9._-]*)*$")
CORPUS_DIRS = ("sources", "findings", "directions")
MANIFEST_VERSION = 1


class ArtifactError(RuntimeError):
    pass


def check_key(key: str) -> str:
    """A key the directory store and the server's store routes accept: relative, no
    traversal, no hidden segments, nothing a shell or a URL would reinterpret."""
    if not KEY_RE.fullmatch(key) or len(key) > 400:
        raise ArtifactError(f"bad store key {key!r}")
    return key


# --------------------------------------------------------------------------- store


class Store(Protocol):
    """What a store must answer. `put_new` is the publish lease's primitive: create
    the key only if it does not exist, atomically, and answer False (never
    overwrite) when it does. DirStore opens with O_CREAT|O_EXCL; S3Store sends
    `If-None-Match: *` and reads PreconditionFailed as held. An HTTP store honours
    the same contract on its store routes: a PUT carrying `If-None-Match: *` is
    refused with 412 when the key exists, and `delete` is a DELETE on the key."""

    def get(self, key: str) -> bytes: ...

    def get_file(self, key: str, dest: pathlib.Path) -> None:
        """Stream the object to ``dest`` without holding it in memory."""
        ...

    def put(self, key: str, data: bytes, content_type: str) -> None: ...

    def put_new(self, key: str, data: bytes, content_type: str) -> bool: ...

    def delete(self, key: str) -> None: ...

    def exists(self, key: str) -> bool: ...


class DirStore:
    """A directory standing in for a bucket (``file:///path``); for local tests and
    for a single host that shares a volume between the curator and the server."""

    def __init__(self, root: pathlib.Path) -> None:
        self.root = root

    def _path(self, key: str) -> pathlib.Path:
        p = (self.root / check_key(key)).resolve()
        if not p.is_relative_to(self.root.resolve()):
            raise ArtifactError(f"key escapes the store: {key}")
        return p

    def write(self, key: str, chunks: Iterable[bytes], limit: int | None = None) -> tuple[int, str]:
        """Stream an object in (the server's PUT route); returns (bytes, sha256). A body
        over ``limit`` leaves nothing behind."""
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(f".{p.name}.{os.getpid()}.tmp")
        h, size = hashlib.sha256(), 0
        try:
            with tmp.open("wb") as out:
                for chunk in chunks:
                    size += len(chunk)
                    if limit is not None and size > limit:
                        raise ArtifactError(f"object exceeds {limit} bytes")
                    h.update(chunk)
                    out.write(chunk)
            os.replace(tmp, p)
        finally:
            tmp.unlink(missing_ok=True)
        return size, h.hexdigest()

    def list_keys(self, prefix: str = "") -> list[str]:
        root = self.root.resolve()
        if not root.is_dir():
            return []
        keys = [
            p.relative_to(root).as_posix()
            for p in root.rglob("*")
            if p.is_file() and not p.name.startswith(".")
        ]
        return sorted(k for k in keys if k.startswith(prefix))

    def get(self, key: str) -> bytes:
        try:
            return self._path(key).read_bytes()
        except FileNotFoundError as exc:
            raise ArtifactError(f"missing object {key}") from exc

    def get_file(self, key: str, dest: pathlib.Path) -> None:
        try:
            shutil.copyfile(self._path(key), dest)
        except FileNotFoundError as exc:
            raise ArtifactError(f"missing object {key}") from exc

    def put(self, key: str, data: bytes, content_type: str) -> None:
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        tmp = p.with_name(p.name + ".tmp")
        tmp.write_bytes(data)
        os.replace(tmp, p)

    def put_new(self, key: str, data: bytes, content_type: str) -> bool:
        p = self._path(key)
        p.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        except FileExistsError:
            return False
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
        return True

    def delete(self, key: str) -> None:
        try:
            self._path(key).unlink()
        except FileNotFoundError:
            pass

    def exists(self, key: str) -> bool:
        return self._path(key).is_file()


def _s3_errors() -> tuple[type[Exception], ...]:
    from botocore.exceptions import BotoCoreError, ClientError

    return (BotoCoreError, ClientError)


def _missing(exc: Exception) -> bool:
    """A ClientError that says the object is not there, as opposed to a refusal or
    a connection failure, which must not read as "missing"."""
    code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
    return code in ("404", "NoSuchKey", "NotFound")


class S3Store:
    """Every store failure surfaces as an ArtifactError, so the server's reload and the
    CLI report it instead of a traceback or a 500."""

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
        except _s3_errors() as exc:
            if _missing(exc):
                raise ArtifactError(f"missing object {key}") from exc
            raise ArtifactError(f"store get {key}: {exc}") from exc

    def get_file(self, key: str, dest: pathlib.Path) -> None:
        try:
            with dest.open("wb") as handle:
                self.client.download_fileobj(self.bucket, key, handle)
        except _s3_errors() as exc:
            if _missing(exc):
                raise ArtifactError(f"missing object {key}") from exc
            raise ArtifactError(f"store get {key}: {exc}") from exc

    def put(self, key: str, data: bytes, content_type: str) -> None:
        try:
            self.client.put_object(Bucket=self.bucket, Key=key, Body=data, ContentType=content_type)
        except _s3_errors() as exc:
            raise ArtifactError(f"store put {key}: {exc}") from exc

    def put_new(self, key: str, data: bytes, content_type: str) -> bool:
        try:
            self.client.put_object(
                Bucket=self.bucket, Key=key, Body=data, ContentType=content_type, IfNoneMatch="*"
            )
            return True
        except _s3_errors() as exc:
            code = str(getattr(exc, "response", {}).get("Error", {}).get("Code", ""))
            if code in ("PreconditionFailed", "412"):
                return False
            raise ArtifactError(f"store put-new {key}: {exc}") from exc

    def delete(self, key: str) -> None:
        try:
            self.client.delete_object(Bucket=self.bucket, Key=key)
        except _s3_errors() as exc:
            if not _missing(exc):
                raise ArtifactError(f"store delete {key}: {exc}") from exc

    def exists(self, key: str) -> bool:
        try:
            self.client.head_object(Bucket=self.bucket, Key=key)
            return True
        except _s3_errors() as exc:
            # A denied or failed HEAD is not "missing": push's overwrite check relies
            # on this answer.
            if _missing(exc):
                return False
            raise ArtifactError(f"store head {key}: {exc}") from exc


class HttpStore:
    """The wiki server's own directory store, reached through its token-guarded routes
    (``PUT/GET/HEAD <endpoint>/{key}``, ``GET <endpoint>?prefix=``; beril_wiki.serve).
    The bearer is WIKI_RELOAD_TOKEN, the same token that triggers the reload, so a
    curator job needs one secret and no bucket, volume or ``kubectl cp``.

    Every failure is an ArtifactError that names the route and, for an HTTP answer,
    the status: a 404 on PUT is a missing route, not "different bytes", and a
    timeout or a dropped connection is reported as such, never as a traceback."""

    def __init__(
        self, endpoint: str, token: str, timeout: float = 900.0, transport: Any = None
    ) -> None:
        import httpx

        if not token:
            raise ArtifactError("an http(s) WIKI_ARTIFACT_ENDPOINT needs WIKI_RELOAD_TOKEN")
        self.endpoint = endpoint.rstrip("/")
        self.timeout = timeout
        self.client = httpx.Client(
            timeout=timeout, headers={"Authorization": f"Bearer {token}"}, transport=transport
        )

    def _request(
        self,
        method: str,
        key: str | None,
        data: bytes | None = None,
        content_type: str | None = None,
        query: Mapping[str, str] | None = None,
        accept: tuple[int, ...] = (),
        headers: Mapping[str, str] | None = None,
    ) -> Any:
        """The response, with a 2xx or an `accept`ed status; anything else, including a
        transport failure, is an ArtifactError naming the route."""
        import httpx

        url = self.endpoint + (f"/{quote(check_key(key))}" if key is not None else "")
        where = f"store {method} {key or ''}".rstrip()
        headers = dict(headers or {})
        if content_type:
            headers["Content-Type"] = content_type
        try:
            r = self.client.request(method, url, content=data, headers=headers, params=query)
        except httpx.TimeoutException as exc:
            raise ArtifactError(f"{where}: no answer within {self.timeout:g}s from {url}") from exc
        except httpx.HTTPError as exc:  # refused, unresolvable, dropped mid-transfer
            raise ArtifactError(f"{where}: {type(exc).__name__}: {exc} ({url})") from exc
        if r.is_success or r.status_code in accept:
            return r
        detail = r.text[:300].strip()
        raise ArtifactError(f"{where}: HTTP {r.status_code} {detail}".rstrip())

    def get(self, key: str) -> bytes:
        r = self._request("GET", key, accept=(404,))
        if r.status_code == 404:
            raise ArtifactError(f"missing object {key}")
        return r.content

    def put(self, key: str, data: bytes, content_type: str) -> None:
        r = self._request("PUT", key, data, content_type)
        try:
            echoed = r.json().get("sha256")
        except (ValueError, AttributeError) as exc:
            raise ArtifactError(
                f"store PUT {key}: HTTP {r.status_code} with no sha256 echo; is "
                f"{self.endpoint} the wiki's /_admin/store route?"
            ) from exc
        if echoed != sha256(data):
            raise ArtifactError(f"store PUT {key}: the server stored different bytes")

    def put_new(self, key: str, data: bytes, content_type: str) -> bool:
        """The lease primitive over HTTP: `If-None-Match: *` makes the server create
        the key or answer 412 when it already exists (beril_wiki.serve)."""
        r = self._request(
            "PUT", key, data, content_type, accept=(412,), headers={"If-None-Match": "*"}
        )
        if r.status_code == 412:
            return False
        try:
            echoed = r.json().get("sha256")
        except (ValueError, AttributeError) as exc:
            raise ArtifactError(
                f"store PUT {key}: HTTP {r.status_code} with no sha256 echo; is "
                f"{self.endpoint} the wiki's /_admin/store route?"
            ) from exc
        if echoed != sha256(data):
            raise ArtifactError(f"store PUT {key}: the server stored different bytes")
        return True

    def delete(self, key: str) -> None:
        """Release a lease or drop an object; a key already gone is not an error."""
        self._request("DELETE", key, accept=(404,))

    def get_file(self, key: str, dest: pathlib.Path) -> None:
        """Stream an object to `dest` so a tarball never sits whole in memory."""
        import httpx

        url = f"{self.endpoint}/{quote(check_key(key))}"
        try:
            with self.client.stream("GET", url) as r:
                if r.status_code == 404:
                    raise ArtifactError(f"missing object {key}")
                if not r.is_success:
                    raise ArtifactError(f"store GET {key}: HTTP {r.status_code}")
                tmp = dest.with_name(dest.name + ".part")
                with tmp.open("wb") as out:
                    for chunk in r.iter_bytes():
                        out.write(chunk)
                os.replace(tmp, dest)
        except httpx.TimeoutException as exc:
            raise ArtifactError(f"store GET {key}: no answer within {self.timeout:g}s") from exc
        except httpx.HTTPError as exc:
            raise ArtifactError(f"store GET {key}: {type(exc).__name__}: {exc}") from exc

    def exists(self, key: str) -> bool:
        """True on 200, False on 404; any other answer is an error, not an absence."""
        return self._request("HEAD", key, accept=(404,)).status_code == 200

    def list_keys(self, prefix: str = "") -> list[str]:
        r = self._request("GET", None, query={"prefix": prefix})
        try:
            keys = r.json()["keys"]
        except (ValueError, KeyError, TypeError) as exc:
            raise ArtifactError(
                f"store GET ?prefix={prefix}: HTTP {r.status_code} with no key list; is "
                f"{self.endpoint} the wiki's /_admin/store route?"
            ) from exc
        return list(keys)


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
    if endpoint.startswith(("http://", "https://")) and "/_admin/store" in endpoint:
        return HttpStore(endpoint, env.get("WIKI_RELOAD_TOKEN", ""))
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

    @property
    def lease(self) -> str:
        return self._join("publish.lease")


def check_id(artifact_id: str) -> str:
    if not ID_RE.fullmatch(artifact_id):
        raise ArtifactError(f"bad artifact id {artifact_id!r}")
    return artifact_id


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------- lease

LEASE_SECONDS_ENV = "WIKI_PUBLISH_LEASE_SECONDS"
LEASE_SECONDS = 3600


def lease_seconds(env: Mapping[str, str] | None = None) -> int:
    env = os.environ if env is None else env
    return int(env.get(LEASE_SECONDS_ENV) or LEASE_SECONDS)


def _parse_time(value: Any) -> dt.datetime | None:
    try:
        when = dt.datetime.fromisoformat(str(value))
    except (TypeError, ValueError):
        return None
    return when if when.tzinfo else when.replace(tzinfo=dt.UTC)


def _read_lease(store: Store, keys: Keys) -> dict:
    try:
        held = json.loads(store.get(keys.lease))
    except (ArtifactError, ValueError):
        return {}
    return held if isinstance(held, dict) else {}


@contextlib.contextmanager
def publish_lease(
    store: Store, keys: Keys, operation: str, artifact_id: str, seconds: int | None = None
) -> Iterator[dict]:
    """Hold `<prefix>/publish.lease` for the block: the one publisher allowed to move
    `current` (push or rollback) at a time, across hosts sharing the store. The key is
    created exclusively (Store.put_new) with a JSON body naming the holder, the
    operation, the artifact and when the lease expires (WIKI_PUBLISH_LEASE_SECONDS,
    default 3600). A lease another publisher holds refuses this one; an expired one,
    left by a host that died, is taken over. Released on success or failure."""
    seconds = lease_seconds() if seconds is None else seconds
    holder = f"{socket.gethostname()}:{os.getpid()}:{secrets.token_hex(4)}"
    now = dt.datetime.now(dt.UTC)
    body = {
        "holder": holder,
        "operation": operation,
        "artifact_id": artifact_id,
        "acquired_at": now.isoformat(timespec="seconds"),
        "expires_at": (now + dt.timedelta(seconds=seconds)).isoformat(timespec="seconds"),
    }
    data = json.dumps(body, indent=1).encode()
    if not store.put_new(keys.lease, data, "application/json"):
        held = _read_lease(store, keys)
        expires = _parse_time(held.get("expires_at"))
        if expires is None or expires > now:
            until = expires.isoformat(timespec="seconds") if expires else "an unknown time"
            raise ArtifactError(
                f"another publisher holds {keys.lease} ({held.get('holder', 'unknown')}: "
                f"{held.get('operation', '?')} {held.get('artifact_id', '?')}, until {until}); "
                f"current will not move. Retry when it has finished, or remove the lease "
                f"if that host is gone"
            )
        store.delete(keys.lease)  # stale: its holder died with it
        if not store.put_new(keys.lease, data, "application/json"):
            raise ArtifactError(
                f"{keys.lease} had expired but another publisher took it first; retry later"
            )
    try:
        yield body
    finally:
        try:
            if _read_lease(store, keys).get("holder") == holder:
                store.delete(keys.lease)
        except ArtifactError as exc:
            print(f"artifact: lease not released ({exc}); it expires on its own", file=sys.stderr)


# ---------------------------------------------------------------------------- pack


def count_pages(site: pathlib.Path) -> int:
    return sum(1 for _ in site.rglob("*.html"))


GATES = ("check_strict", "theme_typecheck", "check_site")
GATE_FILE = "gate-results.json"


def site_digest(site: pathlib.Path) -> str:
    """One hash over the built site's paths and bytes, so gate results can be tied to
    exactly the tree they ran against."""
    h = hashlib.sha256()
    for path in sorted(site.rglob("*")):
        if path.is_file():
            h.update(path.relative_to(site).as_posix().encode())
            h.update(b"\0")
            h.update(sha256(path.read_bytes()).encode())
            h.update(b"\n")
    return h.hexdigest()


def corpus_digest(root: pathlib.Path) -> str:
    """One hash over what corpus_files() packs beside the site, so the gate record is
    tied to the sources a push ships as well as to the rendered tree: `check
    --strict` ran against the live wiki/, and a stale build of the site must not be
    published with newer sources."""
    h = hashlib.sha256()
    for name, data in sorted(corpus_files(root).items()):
        h.update(name.encode())
        h.update(b"\0")
        h.update(sha256(data).encode())
        h.update(b"\n")
    return h.hexdigest()


def gate_commands(root: pathlib.Path, site: pathlib.Path) -> dict[str, list[str]]:
    """The three checks CI runs before it publishes; a push needs all of them green."""
    return {
        "check_strict": [sys.executable, "-m", "beril_wiki.check", str(root), "--strict"],
        "theme_typecheck": ["npm", "--prefix", str(root / "theme"), "run", "typecheck"],
        "check_site": [str(root / "scripts/check_site.sh"), str(site)],
    }


def run_gates(root: pathlib.Path, site: pathlib.Path) -> dict:
    """Run the gates, recording each result; never raises on a failed gate."""
    results: dict[str, Any] = {}
    for name, command in gate_commands(root, site).items():
        try:
            r = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=1800)
            passed, tail = r.returncode == 0, (r.stdout + r.stderr)[-2000:]
        except (OSError, subprocess.TimeoutExpired) as exc:
            passed, tail = False, str(exc)
        results[name] = {"passed": passed, "output": tail.strip()}
        print(f"gate {name}: {'passed' if passed else 'FAILED'}", file=sys.stderr)
    return {
        "ran_at": dt.datetime.now(dt.UTC).isoformat(timespec="seconds"),
        "site_digest": site_digest(site),
        "corpus_digest": corpus_digest(root),
        "results": results,
    }


def gates_passed(gate: dict) -> list[str]:
    """The gates that did not pass (empty when all three did)."""
    results = gate.get("results", {})
    return [name for name in GATES if not results.get(name, {}).get("passed")]


def check_gate(gate: dict | None, root: pathlib.Path, site: pathlib.Path) -> dict:
    """The gate record a push may carry into its manifest, or an ArtifactError."""
    if not gate:
        raise ArtifactError("no gate results: run the gates (`artifact gate`) before pushing")
    failed = gates_passed(gate)
    if failed:
        raise ArtifactError(f"gate(s) failed: {', '.join(failed)}; current will not move")
    if gate.get("site_digest") != site_digest(site):
        raise ArtifactError("gate results are for a different build of the site; rerun the gates")
    if gate.get("corpus_digest") != corpus_digest(root):
        raise ArtifactError(
            "gate results are for different sources than the checkout holds; rerun the gates"
        )
    return {
        "ran_at": gate.get("ran_at"),
        "site_digest": gate["site_digest"],
        "corpus_digest": gate["corpus_digest"],
        **{name: True for name in GATES},
    }


def manifest_gates_ok(manifest: dict) -> bool:
    gates = manifest.get("gates") or {}
    return all(gates.get(name) is True for name in GATES)


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
    """The Markdown and records the internal API answers from, as archive members."""
    out: dict[str, bytes] = {}
    for folder in CORPUS_DIRS:
        for p in sorted((root / "wiki" / folder).glob("*.md")):
            out[f"corpus/{folder}/{p.name}"] = p.read_bytes()
    vectors = root / "search/section-vectors.jsonl"
    if vectors.is_file():
        out["corpus/section-vectors.jsonl"] = vectors.read_bytes()
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
    gate: dict | None = None,
    history: bool = True,
    history_push: bool = True,
) -> dict:
    """Pack, upload, record the promotion on the history branch, push that record,
    then point `current`, all under the store's publish lease. Refuses without a
    gate record showing all three checks passed on this exact site and these
    sources, so `current` never moves to a site CI would reject; a promotion the
    history branch did not record, or whose record `origin` rejected (another host
    published first), is not made live either, since rollback to it would be
    refused or the audit trail would fork. `history_push=False` keeps the record
    local, for a checkout without `origin` or offline use."""
    artifact_id = check_id(artifact_id or new_id(root))
    with publish_lease(store, keys, "push", artifact_id):
        if store.exists(keys.tarball(artifact_id)):
            raise ArtifactError(f"artifact {artifact_id} already exists; artifacts are immutable")
        gates = check_gate(gate, root, site)
        manifest = build_manifest(root, site, artifact_id, base_url)
        manifest["gates"] = gates
        data = pack(root, site, manifest)
        manifest["tarball_sha256"] = sha256(data)
        manifest["tarball_bytes"] = len(data)
        store.put(keys.tarball(artifact_id), data, "application/gzip")
        store.put(
            keys.manifest(artifact_id), json.dumps(manifest, indent=1).encode(), "application/json"
        )
        commit = None
        if history:
            commit = _record_and_push(root, artifact_id, history_push)
        pointer = point(store, keys, artifact_id, manifest)
    if commit:
        pointer["history_commit"] = commit
    return pointer


def _record_and_push(root: pathlib.Path, artifact_id: str, history_push: bool) -> str:
    """Record on `history`, then push the branch and tag to `origin` when the
    checkout has one; a rejected push undoes the record, so a retry starts clean."""
    from beril_wiki.publish import history as H

    stays = "the uploaded artifact stays in the store"
    previous = H.ref(root, f"refs/heads/{H.BRANCH}")
    try:
        commit = H.record(root, artifact_id, fetch=history_push)
    except H.HistoryError as exc:
        raise ArtifactError(
            f"history not recorded, so current will not move to {artifact_id} ({stays}): {exc}"
        ) from exc
    if history_push and H.has_remote(root):
        try:
            H.push_remote(root, artifact_id)
        except H.HistoryError as exc:
            try:
                H.unrecord(root, artifact_id, previous)
            except H.HistoryError as undo:
                raise ArtifactError(
                    f"history push rejected ({exc}) and the local record was not undone "
                    f"({undo}); current will not move to {artifact_id} ({stays})"
                ) from undo
            raise ArtifactError(
                f"history push rejected, so current will not move to {artifact_id} "
                f"({stays}; the local record was undone): {exc}"
            ) from exc
    return commit


def rollback(store: Store, keys: Keys, root: pathlib.Path, artifact_id: str) -> dict:
    """Move `current` back and restore the working checkout to that promotion."""
    from beril_wiki.publish import history as H

    if not H.ref(root, f"refs/tags/{H.tag_of(artifact_id)}"):
        raise ArtifactError(f"no history tag for {artifact_id}; refusing to roll back")
    if not store.exists(keys.tarball(artifact_id)):
        raise ArtifactError(f"no artifact {artifact_id} in the store")
    try:
        # One lock across replacing the trees and moving the pointer: a run that
        # started in between would promote on top of a half-restored checkout. The
        # trees go first, but their predecessors are kept aside until `current` has
        # moved: a pointer write that fails puts them back, so the served artifact
        # and the curator's inputs never disagree.
        with publish_lease(store, keys, "rollback", artifact_id), H.held_lock(root):
            pending = H.stage_restore(root, artifact_id)
            try:
                pointer = point(store, keys, artifact_id)
            except ArtifactError as exc:
                try:
                    pending.undo()
                except H.HistoryError as undo:
                    raise ArtifactError(
                        f"current was not moved ({exc}) and the checkout, restored to "
                        f"{artifact_id}, could not be put back: {undo}"
                    ) from undo
                raise ArtifactError(
                    f"current was not moved ({exc}); the checkout was put back, so both "
                    f"still stand at the previous promotion"
                ) from exc
            restored = pending.keep()
    except H.HistoryError as exc:
        raise ArtifactError(str(exc)) from exc
    pointer["restored_commit"] = restored
    return pointer


def point_current(store: Store, keys: Keys, artifact_id: str) -> dict:
    """Move `current` to an artifact already in the store, under the publish lease:
    what a retried publish does once the artifact and its history tag exist."""
    with publish_lease(store, keys, "point", artifact_id):
        return point(store, keys, artifact_id)


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
    if not manifest_gates_ok(manifest):
        raise ArtifactError("manifest does not record all three gates passing; refusing it")
    return manifest


UNPACK_LIMITS = {
    "WIKI_ARTIFACT_MAX_MEMBERS": 50_000,
    "WIKI_ARTIFACT_MAX_UNPACKED_BYTES": 4 * 1024**3,
    "WIKI_ARTIFACT_MAX_MEMBER_BYTES": 1024**3,
}


def unpack_limits(env: Mapping[str, str] | None = None) -> dict[str, int]:
    env = os.environ if env is None else env
    return {name: int(env.get(name) or default) for name, default in UNPACK_LIMITS.items()}


def file_sha256(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def check_store_manifest(manifest: dict, artifact_id: str, pointer: dict) -> dict:
    """The manifest the store holds beside the tarball, checked before the tarball is
    read: a writer who can put objects must not get a tarball extracted on the
    strength of a manifest that would be refused anyway."""
    if manifest.get("id") != artifact_id:
        raise ArtifactError(f"manifest id {manifest.get('id')!r} is not {artifact_id!r}")
    if not isinstance(manifest.get("page_count"), int):
        raise ArtifactError("manifest has no page count")
    if not manifest_gates_ok(manifest):
        raise ArtifactError("manifest does not record all three gates passing; refusing it")
    expected = pointer.get("sha256")
    if expected and manifest.get("tarball_sha256") != expected:
        raise ArtifactError("manifest tarball sha256 does not match current.json")
    return manifest


def unpack(
    tarball: pathlib.Path,
    dest: pathlib.Path,
    artifact_id: str,
    expected_sha: str | None,
    manifest: dict | None = None,
    limits: dict[str, int] | None = None,
) -> dict:
    """Extract the downloaded tarball into ``dest`` (replacing any partial earlier
    attempt) and verify. The sha256 is checked on the file before anything is
    extracted; members are extracted one at a time, regular files and directories
    only, and the count, each member's size and the total (as the headers declare
    them, which `filter="data"` holds the extraction to) are capped, so a
    compressed archive cannot fill the volume. A trip removes the partial tree."""
    limits = limits or unpack_limits()
    if expected_sha and file_sha256(tarball) != expected_sha:
        raise ArtifactError("tarball sha256 does not match current.json")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix=f".site-{artifact_id}.", dir=dest.parent))
    try:
        with tarfile.open(tarball, mode="r:gz") as tar:
            members = total = 0
            for member in tar:
                members += 1
                if members > limits["WIKI_ARTIFACT_MAX_MEMBERS"]:
                    raise ArtifactError(f"artifact has more than {members - 1} members")
                if not (member.isfile() or member.isdir()):
                    raise ArtifactError(f"{member.name}: not a regular file or directory")
                if member.size > limits["WIKI_ARTIFACT_MAX_MEMBER_BYTES"]:
                    raise ArtifactError(f"{member.name}: {member.size} bytes exceeds the cap")
                total += member.size
                if total > limits["WIKI_ARTIFACT_MAX_UNPACKED_BYTES"]:
                    raise ArtifactError(f"artifact unpacks past {total - member.size} bytes")
                tar.extract(member, tmp, filter="data")
        found = verify_manifest(tmp, artifact_id)
        if manifest is not None:
            for key in ("id", "page_count", "gates"):
                if found.get(key) != manifest.get(key):
                    raise ArtifactError(f"the tarball's manifest differs from the store's: {key}")
        if dest.exists():
            shutil.rmtree(dest)
        os.replace(tmp, dest)
    except BaseException:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    return found


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
    manifest = check_store_manifest(
        json.loads(store.get(keys.manifest(artifact_id))), artifact_id, pointer
    )
    with tempfile.TemporaryDirectory(prefix=f".download-{artifact_id}.", dir=site_root) as tmp:
        tarball = pathlib.Path(tmp) / "site.tar.gz"
        store.get_file(keys.tarball(artifact_id), tarball)
        manifest = unpack(tarball, dest, artifact_id, pointer.get("sha256"), manifest)
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
    p.add_argument(
        "--gate-results",
        type=pathlib.Path,
        default=None,
        help="gate record written by `artifact gate` (default <root>/quartz/gate-results.json)",
    )
    p.add_argument("--run-gates", action="store_true", help="run the three gates now")
    p.add_argument("--no-history", action="store_true", help="do not record on the history branch")
    p.add_argument(
        "--no-history-push",
        action="store_true",
        help="record on the history branch but do not push it to origin first (offline use)",
    )
    g = sub.add_parser("gate", help="run check --strict, the theme typecheck and check_site")
    g.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    g.add_argument("--site", type=pathlib.Path, default=None)
    g.add_argument("--out", type=pathlib.Path, default=None)
    r = sub.add_parser("rollback", help="point current at an earlier artifact and restore it")
    r.add_argument("--to", required=True, dest="artifact_id")
    r.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    sub.add_parser("current", help="print current.json")
    c = sub.add_parser("corpus", help="write the corpus/ tree (no store needed)")
    c.add_argument("dest", type=pathlib.Path)
    c.add_argument("--root", type=pathlib.Path, default=pathlib.Path.cwd())
    args = parser.parse_args(argv)
    if args.command == "corpus":
        n = write_corpus(args.root.resolve(), args.dest.resolve())
        print(f"artifact: wrote {n} corpus file(s) -> {args.dest}")
        return 0
    if args.command == "gate":
        root = args.root.resolve()
        site = (args.site or root / "quartz/public").resolve()
        gate = run_gates(root, site)
        out = args.out or root / "quartz" / GATE_FILE
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(gate, indent=1))
        failed = gates_passed(gate)
        verdict = "all passed" if not failed else "FAILED: " + ", ".join(failed)
        print(f"artifact: gates {verdict}; {out}")
        return 1 if failed else 0
    try:
        store, keys = store_from_env(), Keys(prefix_from_env())
        if args.command == "push":
            root = args.root.resolve()
            site = (args.site or root / "quartz/public").resolve()
            if args.run_gates:
                gate: dict | None = run_gates(root, site)
            else:
                gate_path = args.gate_results or root / "quartz" / GATE_FILE
                gate = json.loads(gate_path.read_text()) if gate_path.exists() else None
            result: Any = push(
                store,
                keys,
                root,
                site,
                args.artifact_id,
                args.base_url,
                gate,
                history=not args.no_history,
                history_push=not args.no_history_push,
            )
        elif args.command == "rollback":
            result = rollback(store, keys, args.root.resolve(), args.artifact_id)
        else:
            result = current(store, keys)
    except ArtifactError as exc:
        print(f"artifact: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
