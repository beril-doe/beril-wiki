"""The committed corpus: every source the wiki compiles from, keyed by owner.

``corpus/<owner_orcid>/<project>/`` holds a project's ``REPORT.md``, ``README.md``,
``beril.yaml`` and the ``figures/`` its report embeds; ``corpus/beril/docs/`` holds
the two central digests. ``corpus/index.json`` maps ``"<owner>/<project>"`` to
``{sid, revision, submitted_at, kind}``.

Both fetch backends write here (the hub from BERIL's feed, the local backend from
a checkout under the owner ``legacy``) and then ``stage_all`` copies every indexed
report into ``staging/<sid>__REPORT.md`` and its figures into
``wiki/figures/<sid>/``. The runner compares the whole of ``staging/`` with
``wiki/sources/``, so a partial staging would read as deletions; staging all of
the corpus every time is what keeps an incremental fetch safe.

Source ids. BERIL project slugs are unique per owner only, and a ``[src: id]``
must never change once pages cite it, so the index assigns each project's sid
once:

1. an entry for ``(owner, project)`` keeps its sid forever;
2. else a ``legacy/<project>`` entry (a source integrated before owners were
   known) is claimed: the sid is the slug and the entry is re-keyed to the owner;
3. else the slug, when no other entry already uses it as a sid;
4. else ``<slug>__<orcid>``.

``seed_legacy`` pins the existing ``wiki/sources`` under rule 2's ``legacy``
owner, so seeding the feed re-integrates nothing.
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import shutil

INDEX = "index.json"
LEGACY = "legacy"
DOCS_KEY = "beril/docs"
DIGESTS = ("discoveries.md", "pitfalls.md")
FIG_EMBED = re.compile(r"!\[[^\]]*\]\((figures/[^)]+)\)")
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_.-]*$")


class CorpusError(RuntimeError):
    pass


def check_id(value: str, what: str) -> str:
    if not SAFE_ID.fullmatch(value) or value in (".", ".."):
        raise CorpusError(f"unsafe {what} {value!r}")
    return value


def figure_rel(rel: str) -> str:
    """The path under figures/ a report embeds; refuses one that leaves the tree."""
    out = re.sub(r"^figures/", "", rel)
    parts = pathlib.PurePosixPath(out).parts
    if not parts or ".." in parts or out.startswith("/") or any(p == "." for p in parts):
        raise CorpusError(f"unsafe figure reference {rel!r}")
    return out


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def corpus_dir(root: pathlib.Path) -> pathlib.Path:
    return root / "corpus"


def project_dir(root: pathlib.Path, key: str) -> pathlib.Path:
    owner, _, project = key.partition("/")
    return corpus_dir(root) / check_id(owner, "owner") / check_id(project, "project")


def load_index(root: pathlib.Path) -> dict[str, dict]:
    path = corpus_dir(root) / INDEX
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return dict(data.get("projects", {}))


def save_index(root: pathlib.Path, index: dict[str, dict]) -> None:
    path = corpus_dir(root) / INDEX
    path.parent.mkdir(parents=True, exist_ok=True)
    body = {"projects": dict(sorted(index.items()))}
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(body, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def key_of(owner: str, project: str) -> str:
    return f"{check_id(owner, 'owner')}/{check_id(project, 'project')}"


def assign_sid(index: dict[str, dict], owner: str, project: str) -> str:
    """The sid for (owner, project), assigning and re-keying the index as the module
    docstring describes. Mutates ``index``."""
    key = key_of(owner, project)
    if key in index:
        return index[key]["sid"]
    legacy = f"{LEGACY}/{project}"
    if owner != LEGACY and legacy in index:
        entry = index.pop(legacy)
        index[key] = entry
        return entry["sid"]
    taken = {e["sid"] for e in index.values()}
    sid = project if project not in taken else f"{project}__{owner}"
    if sid in taken:
        raise CorpusError(f"sid {sid!r} is already assigned")
    index[key] = {"sid": sid, "revision": None, "submitted_at": None, "kind": None}
    return sid


def seed_legacy(root: pathlib.Path, index: dict[str, dict]) -> int:
    """Pin every accepted source without an index entry as a legacy project."""
    taken = {e["sid"] for e in index.values()}
    added = 0
    for report in sorted((root / "wiki/sources").glob("*__REPORT.md")):
        sid = report.name.removesuffix("__REPORT.md")
        if sid in taken or not SAFE_ID.fullmatch(sid):
            continue
        index[f"{LEGACY}/{sid}"] = {
            "sid": sid,
            "revision": sha256(report.read_bytes()),
            "submitted_at": None,
            "kind": "legacy",
        }
        taken.add(sid)
        added += 1
    return added


def write_project(
    root: pathlib.Path, key: str, files: dict[str, bytes], replace: bool = True
) -> pathlib.Path:
    """Write a project's files under corpus/<owner>/<project>/, dropping files no longer
    supplied when ``replace`` is set."""
    where = project_dir(root, key)
    if replace and where.exists():
        shutil.rmtree(where)
    for rel, data in files.items():
        parts = pathlib.PurePosixPath(rel).parts
        if not parts or ".." in parts or rel.startswith("/"):
            raise CorpusError(f"unsafe corpus path {rel!r}")
        target = where / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    return where


def stage_all(root: pathlib.Path, staging: pathlib.Path) -> tuple[int, int]:
    """Stage every indexed report (or, for a legacy entry without corpus files, its
    accepted copy under wiki/sources) and sync the figures. Returns (docs, figures)."""
    index = load_index(root)
    staging.mkdir(parents=True, exist_ok=True)
    figroot = root / "wiki" / "figures"
    n = nf = 0
    for key, entry in sorted(index.items()):
        if key == DOCS_KEY:
            continue
        sid = check_id(entry["sid"], "sid")
        where = project_dir(root, key)
        report = where / "REPORT.md"
        if not report.exists():
            legacy = root / "wiki/sources" / f"{sid}__REPORT.md"
            if not legacy.exists():
                raise CorpusError(f"{key}: no REPORT.md in corpus and no accepted source")
            shutil.copy2(legacy, staging / f"{sid}__REPORT.md")
            n += 1
            continue
        shutil.copy2(report, staging / f"{sid}__REPORT.md")
        n += 1
        text = report.read_text(encoding="utf-8", errors="replace")
        for rel in sorted(set(FIG_EMBED.findall(text))):
            src = where / "figures" / figure_rel(rel)
            if not src.is_file():
                continue
            dst = figroot / sid / figure_rel(rel)
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                nf += 1
    docs = project_dir(root, DOCS_KEY) if DOCS_KEY in index else None
    for digest in DIGESTS:
        candidates = [docs / digest] if docs else []
        candidates.append(root / "wiki/sources" / digest)
        for src in candidates:
            if src.exists():
                shutil.copy2(src, staging / digest)
                n += 1
                break
    return n, nf
