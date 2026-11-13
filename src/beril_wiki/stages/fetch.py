#!/usr/bin/env python3
"""Sync source docs into staging/ — the pipeline's single input gateway.

Two backends fill the committed corpus (stages/corpus.py), selected by
``FETCH_BACKEND``; a common tail then stages all of it:

  local  (default) every ``projects/*/REPORT.md`` (with README.md, beril.yaml and
         the embedded figures) and the docs digests from a BERIL observatory
         checkout (``BERIL_CHECKOUT``), written under the owner ``legacy``.
  hub    BERIL's context API (stages/hub.py): the submissions feed names the
         changed projects, ``read`` supplies their files; ``BERIL_URL`` and
         ``BERIL_TOKEN``. Only projects whose revision changed are downloaded.

``corpus.stage_all`` writes ``staging/<sid>__REPORT.md`` for every indexed project
and syncs ``wiki/figures/<sid>/``, so ``changed_sources`` always sees the full set
and an incremental fetch can never read as a deletion. Other stages import
``CHECKOUT`` and ``project_readmes`` from here, so the source of project metadata
is configured in exactly one place.

    uv run python -m beril_wiki.stages.fetch [staging-dir]
"""

from __future__ import annotations

import os
import pathlib
import sys

from beril_wiki.paths import ROOT
from beril_wiki.stages import corpus, hub

CHECKOUT = pathlib.Path(
    os.environ.get("BERIL_CHECKOUT", "/Volumes/WorkSSD/Work/BERIL/BERIL-research-observatory")
)
BACKEND = os.environ.get("FETCH_BACKEND", "local")

FIG_EMBED = corpus.FIG_EMBED
DIGESTS = corpus.DIGESTS
META_FILES = ("README.md", "beril.yaml")


def embedded_figures(report: bytes) -> list[str]:
    text = report.decode("utf-8", errors="replace")
    return sorted(set(FIG_EMBED.findall(text)))


def tree_files(where: pathlib.Path) -> dict[str, bytes]:
    if not where.exists():
        return {}
    return {
        p.relative_to(where).as_posix(): p.read_bytes() for p in where.rglob("*") if p.is_file()
    }


def import_local(root: pathlib.Path, checkout: pathlib.Path | None = None) -> int:
    """Write every checkout project into corpus/legacy/<project>/ and index it."""
    checkout = checkout or CHECKOUT
    index = corpus.load_index(root)
    corpus.seed_legacy(root, index)
    n = 0
    for report in sorted(checkout.glob("projects/*/REPORT.md")):
        project = report.parent.name
        if not corpus.SAFE_ID.fullmatch(project):
            continue
        data = report.read_bytes()
        files = {"REPORT.md": data}
        for name in META_FILES:
            if (report.parent / name).exists():
                files[name] = (report.parent / name).read_bytes()
        for rel in embedded_figures(data):
            src = report.parent / "figures" / corpus.figure_rel(rel)
            if src.is_file():
                files[f"figures/{corpus.figure_rel(rel)}"] = src.read_bytes()
        sid = corpus.assign_sid(index, corpus.LEGACY, project)
        key = corpus.key_of(corpus.LEGACY, project)
        if tree_files(corpus.project_dir(root, key)) != files:
            corpus.write_project(root, key, files)
        index[key] = {
            "sid": sid,
            "revision": corpus.sha256(data),
            "submitted_at": None,
            "kind": "local",
        }
        n += 1
    docs = {
        d: (checkout / "docs" / d).read_bytes() for d in DIGESTS if (checkout / "docs" / d).exists()
    }
    if docs:
        if tree_files(corpus.project_dir(root, corpus.DOCS_KEY)) != docs:
            corpus.write_project(root, corpus.DOCS_KEY, docs)
        index[corpus.DOCS_KEY] = {
            "sid": "docs",
            "revision": corpus.sha256(b"".join(docs[d] for d in sorted(docs))),
            "submitted_at": None,
            "kind": "docs",
        }
    corpus.save_index(root, index)
    return n


def import_hub(root: pathlib.Path, client: hub.Hub | None = None) -> int:
    """Download every project the feed reports at a new revision into corpus/, verifying
    each file's sha256, and index it. Returns the number of projects updated."""
    own = client is None
    client = client or hub.Hub()
    index = corpus.load_index(root)
    corpus.seed_legacy(root, index)
    updated = 0
    try:
        state = hub.sync(client, hub.load_state(root))
        for entry in state.get("projects", {}).values():
            owner, project, kind = entry["owner_orcid"], entry["project"], entry.get("kind")
            if kind == "docs":
                index_key, sid, anchor = corpus.DOCS_KEY, "docs", next(iter(entry["files"]), "")
            else:
                sid = corpus.assign_sid(index, owner, project)
                index_key, anchor = corpus.key_of(owner, project), "REPORT.md"
            current = index.get(index_key, {})
            if (
                current.get("revision") == entry.get("revision")
                and (corpus.project_dir(root, index_key) / anchor).exists()
            ):
                continue
            files: dict[str, bytes] = {}
            if kind == "docs":
                for path in entry["files"]:
                    data = hub.fetch_file(client, entry, path)
                    assert data is not None
                    files[path] = data
            else:
                report = hub.fetch_file(client, entry, "REPORT.md")
                assert report is not None
                files["REPORT.md"] = report
                for name in META_FILES:
                    data = hub.fetch_file(client, entry, name, required=False)
                    if data is not None:
                        files[name] = data
                for rel in embedded_figures(report):
                    data = hub.fetch_file(client, entry, rel, required=False)
                    if data is not None:
                        files[f"figures/{corpus.figure_rel(rel)}"] = data
            corpus.write_project(root, index_key, files)
            index[index_key] = {
                "sid": sid,
                "revision": entry.get("revision"),
                "submitted_at": entry.get("submitted_at"),
                "kind": kind,
            }
            updated += 1
        corpus.save_index(root, index)
        hub.save_state(root, state)
    finally:
        if own:
            client.close()
    return updated


def fetch(staging: pathlib.Path = ROOT / "staging", client: hub.Hub | None = None) -> int:
    root = staging.parent
    if BACKEND == "local":
        import_local(root)
    elif BACKEND == "hub":
        updated = import_hub(root, client)
        print(f"hub: {updated} project(s) at a new revision")
    else:
        raise SystemExit(f"stages.fetch: unknown FETCH_BACKEND {BACKEND!r}")
    n, nf = corpus.stage_all(root, staging)
    if nf:
        print(f"synced {nf} figure(s) -> {root / 'wiki' / 'figures'}")
    return n


def fetch_local(staging: pathlib.Path) -> int:
    import_local(staging.parent)
    return corpus.stage_all(staging.parent, staging)[0]


def fetch_hub(staging: pathlib.Path, client: hub.Hub | None = None) -> int:
    import_hub(staging.parent, client)
    return corpus.stage_all(staging.parent, staging)[0]


def project_readmes(root: pathlib.Path = ROOT) -> dict[str, str]:
    """sid -> README text for every indexed project whose corpus files carry one; in
    local mode a project the corpus lacks falls back to the checkout."""
    out: dict[str, str] = {}
    for key, entry in corpus.load_index(root).items():
        if key == corpus.DOCS_KEY:
            continue
        path = corpus.project_dir(root, key) / "README.md"
        if path.exists():
            out[entry["sid"]] = path.read_text(encoding="utf-8", errors="replace")
        elif BACKEND == "local":
            fallback = CHECKOUT / "projects" / entry["sid"] / "README.md"
            if fallback.exists() and (fallback.parent / "REPORT.md").exists():
                out[entry["sid"]] = fallback.read_text(encoding="utf-8", errors="replace")
    return out


def collections_config() -> pathlib.Path:
    """The collections metadata: the checkout's copy in local mode when it has one,
    otherwise the copy committed at contract/collections.yaml."""
    if BACKEND == "local" and (CHECKOUT / "ui/config/collections.yaml").exists():
        return CHECKOUT / "ui/config/collections.yaml"
    return ROOT / "contract" / "collections.yaml"


def main() -> None:
    dest = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "staging"
    try:
        print(f"staged {fetch(dest)} docs -> {dest}")
    except (hub.HubError, corpus.CorpusError) as exc:
        raise SystemExit(f"stages.fetch: {exc}") from exc


if __name__ == "__main__":
    main()
