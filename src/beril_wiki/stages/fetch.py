#!/usr/bin/env python3
"""Sync source docs into staging/ — the pipeline's single input gateway.

Two backends behind one function, selected by ``FETCH_BACKEND``:
  local  (default) copy REPORT.md per project + the discoveries/pitfalls
         digests from a BERIL observatory checkout (``BERIL_CHECKOUT``).
  hub    BERIL's context API (stages/hub.py): the submissions feed names the
         projects, ``read`` supplies REPORT.md, beril.yaml, README.md and the
         figures the report embeds; ``BERIL_URL`` and ``BERIL_TOKEN``.

Both write the same layout, so nothing downstream knows which ran:
``staging/<project>__REPORT.md``, ``wiki/figures/<project>/<rel>``, and for the
hub ``reference/projects/<project>/{README.md,beril.yaml}``, the place the
curator snapshots a checkout's inputs to. Other stages import ``CHECKOUT`` and
``project_readmes`` from here, so the source of project metadata is configured
in exactly one place. The two central digests (docs/discoveries.md,
docs/pitfalls.md) are not project files and the hub has no route for them: the
hub backend takes them from the checkout when one is present and otherwise
re-stages the accepted copies under wiki/sources, since both archives stopped
changing in May 2026.

    uv run python -m beril_wiki.stages.fetch [staging-dir]
"""

from __future__ import annotations

import os
import pathlib
import re
import shutil
import sys

from beril_wiki.paths import ROOT
from beril_wiki.stages import hub

CHECKOUT = pathlib.Path(
    os.environ.get("BERIL_CHECKOUT", "/Volumes/WorkSSD/Work/BERIL/BERIL-research-observatory")
)
BACKEND = os.environ.get("FETCH_BACKEND", "local")


FIG_EMBED = re.compile(r"!\[[^\]]*\]\((figures/[^)]+)\)")


def fetch_local(staging: pathlib.Path) -> int:
    staging.mkdir(parents=True, exist_ok=True)
    figroot = staging.parent / "wiki" / "figures"
    n = nf = 0
    for report in sorted(CHECKOUT.glob("projects/*/REPORT.md")):
        text = report.read_text(encoding="utf-8", errors="replace")
        shutil.copy2(report, staging / f"{report.parent.name}__REPORT.md")
        n += 1
        # Figures referenced by the report travel with the wiki repo, so the
        # site is fully renderable from a clone; the checkout is fetch-only.
        for rel in set(FIG_EMBED.findall(text)):
            src = report.parent / rel
            if not src.exists():
                continue
            dst = figroot / report.parent.name / re.sub(r"^figures/", "", rel)
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                nf += 1
    for digest in ("discoveries.md", "pitfalls.md"):
        src = CHECKOUT / "docs" / digest
        if src.exists():
            shutil.copy2(src, staging / digest)
            n += 1
    if nf:
        print(f"synced {nf} figure(s) -> {figroot}")
    return n


DIGESTS = ("discoveries.md", "pitfalls.md")


def figure_rel(rel: str) -> str:
    """The figure path under wiki/figures/<project>/; refuses one that leaves the tree."""
    out = re.sub(r"^figures/", "", rel)
    parts = pathlib.PurePosixPath(out).parts
    if not parts or ".." in parts or out.startswith("/"):
        raise SystemExit(f"stages.fetch: unsafe figure reference {rel!r}")
    return out


def hub_reference(root: pathlib.Path) -> pathlib.Path:
    """Where the hub backend keeps per-project metadata files (README.md, beril.yaml)."""
    return root / "reference" / "projects"


def fetch_hub(staging: pathlib.Path, client: hub.Hub | None = None) -> int:
    """Stage every public project the feed has reported, verifying each file's sha256."""
    root = staging.parent
    staging.mkdir(parents=True, exist_ok=True)
    figroot = root / "wiki" / "figures"
    reference = hub_reference(root)
    own = client is None
    client = client or hub.Hub()
    n = nf = 0
    try:
        state = hub.sync(client, hub.load_state(root))
        for project, entry in hub.served(state).items():
            report = hub.fetch_file(client, entry, "REPORT.md")
            assert report is not None
            (staging / f"{project}__REPORT.md").write_bytes(report)
            n += 1
            meta = reference / project
            meta.mkdir(parents=True, exist_ok=True)
            for name in ("beril.yaml", "README.md"):
                data = hub.fetch_file(client, entry, name, required=False)
                if data is not None:
                    (meta / name).write_bytes(data)
                elif (meta / name).exists():
                    (meta / name).unlink()
            text = report.decode("utf-8", errors="replace")
            for rel in sorted(set(FIG_EMBED.findall(text))):
                dst = figroot / project / figure_rel(rel)
                declared = entry.get("files", {}).get(rel)
                if declared and dst.exists() and hub.sha256(dst.read_bytes()) == declared:
                    continue
                data = hub.fetch_file(client, entry, rel, required=False)
                if data is None:
                    continue
                if not dst.exists() or dst.read_bytes() != data:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(data)
                    nf += 1
        for digest in DIGESTS:
            for src in (CHECKOUT / "docs" / digest, root / "wiki" / "sources" / digest):
                if src.exists():
                    shutil.copy2(src, staging / digest)
                    n += 1
                    break
        hub.save_state(root, state)
    finally:
        if own:
            client.close()
    if nf:
        print(f"synced {nf} figure(s) -> {figroot}")
    return n


def project_readmes(root: pathlib.Path = ROOT) -> dict[str, str]:
    """Project id -> README text for every project that has a report.

    Local: the checkout. Hub: the copies fetch_hub kept beside the run; a staged
    project whose README was not kept is read from the hub on demand."""
    if BACKEND == "local":
        return {
            p.parent.name: p.read_text(encoding="utf-8", errors="replace")
            for p in CHECKOUT.glob("projects/*/README.md")
            if (p.parent / "REPORT.md").exists()
        }
    staged = sorted(
        re.sub(r"__REPORT$", "", f.stem) for f in (root / "staging").glob("*__REPORT.md")
    )
    out: dict[str, str] = {}
    missing: list[str] = []
    for project in staged:
        path = hub_reference(root) / project / "README.md"
        if path.exists():
            out[project] = path.read_text(encoding="utf-8", errors="replace")
        else:
            missing.append(project)
    if missing:
        state = hub.load_state(root)
        with hub.Hub() as client:
            for project in missing:
                entry = state.get("projects", {}).get(project)
                if entry is None:
                    continue
                data = hub.fetch_file(client, entry, "README.md", required=False)
                if data is not None:
                    out[project] = data.decode("utf-8", errors="replace")
    return out


def collections_config() -> pathlib.Path:
    """The collections metadata: the checkout's copy in local mode when it has one,
    otherwise the copy committed at contract/collections.yaml."""
    if BACKEND == "local" and (CHECKOUT / "ui/config/collections.yaml").exists():
        return CHECKOUT / "ui/config/collections.yaml"
    return ROOT / "contract" / "collections.yaml"


def fetch(staging: pathlib.Path = ROOT / "staging") -> int:
    if BACKEND == "local":
        return fetch_local(staging)
    if BACKEND == "hub":
        return fetch_hub(staging)
    raise SystemExit(f"stages.fetch: unknown FETCH_BACKEND {BACKEND!r}")


def main() -> None:
    dest = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "staging"
    try:
        print(f"staged {fetch(dest)} docs -> {dest}")
    except hub.HubError as exc:
        raise SystemExit(f"stages.fetch: {exc}") from exc


if __name__ == "__main__":
    main()
