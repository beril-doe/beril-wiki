"""Copy embedded report figures and place them on eligible pages this run touched."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path, PurePosixPath

from beril_wiki.agentic.runtime import CandidateError
from beril_wiki.corpus import FIG_EMBED, figure_destination
from beril_wiki.kb.jobs import Job, Scope, legacy, write_state
from beril_wiki.kb.store import DIGESTS, sha256, write_text
from beril_wiki.kb.tools import adopt_legacy_state
from beril_wiki.records import source_path
from beril_wiki.stages import cards, figures

MANIFEST = Path("state/figures-manifest.json")
PLACEMENTS = Path("state/figures-placements.json")
STATE = Path("state/figures-state.json")


def _publish_manifest(scope: Scope, projects: set[str]) -> dict[str, list[dict]]:
    """Sync the embedded assets and update the manifest for the selected reports."""
    root, store = scope.root, scope.store
    path = root / MANIFEST
    manifest = cards.load_state(path)
    updated = manifest.copy()
    for project in sorted(projects):
        report = source_path(root, project)
        vendored = store.source_path(project)
        if not report.is_file():
            report = vendored
        if not report.is_file():
            continue
        candidates = []
        text = report.read_text(encoding="utf-8", errors="replace")
        for paragraph in figures.paragraphs(text):
            for embed in FIG_EMBED.finditer(paragraph):
                rel = embed.group(1)
                if ".." in PurePosixPath(rel).parts:
                    continue
                src = vendored.parent / rel
                dst = root / "wiki/figures" / figure_destination(project, rel)
                if src.is_file() and (not dst.is_file() or dst.read_bytes() != src.read_bytes()):
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                if dst.is_file():
                    caption = embed[0][2 : embed[0].index("](")]
                    context = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", paragraph).strip()[:400]
                    candidates.append({"file": rel, "caption": caption, "context": context})
        if candidates:
            updated[project] = candidates
        else:
            updated.pop(project, None)
    if updated != manifest or (projects and not path.exists()):
        write_state(path, updated)
    return updated


def _drop_withdrawn(root: Path, manifest: dict[str, list[dict]], keys: set[str]) -> None:
    """Remove placements of figures their report no longer embeds.

    An edited page keeps its placements (``rehome_figures`` moves them with their
    paragraphs), so a figure a revision took out of the report would stay published.
    """
    path = root / PLACEMENTS
    saved = cards.load_state(path)
    changed = False
    for key in sorted(keys & saved.keys()):
        entry = saved[key]
        kept = [
            p
            for p in entry.get("placements", [])
            if any(fig["file"] == p["file"] for fig in manifest.get(p["project"], []))
        ]
        if len(kept) != len(entry.get("placements", [])):
            saved[key] = entry | {"placements": kept}
            changed = True
    if changed:
        write_state(path, saved)


def _job(scope: Scope, page_id: str, text: str, candidates: list[dict]) -> Job:
    max_place = figures.MAX_PLACE[page_id.split("/", 1)[0]]
    paragraphs = figures.paragraphs(text)
    limit = min(1200, 80_000 // max(1, len(paragraphs)))
    page_hash = sha256(text)[:16]

    def parse(raw: str) -> dict:
        # The curator inlines this gate inside main's per-page model call.
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise CandidateError("invalid placement schema or indices")
        placements = data.get("placements")
        flags = data.get("csv_flags", [])
        if not (
            isinstance(placements, list)
            and isinstance(flags, list)
            and all(isinstance(flag, str) for flag in flags)
            and all(
                isinstance(item, dict)
                and type(item.get("figure")) is int
                and 0 <= item["figure"] < len(candidates)
                and type(item.get("after_paragraph")) is int
                and 0 <= item["after_paragraph"] < len(paragraphs)
                for item in placements
            )
        ):
            raise CandidateError("invalid placement schema or indices")
        return data

    gate = legacy(parse)

    def check(record: dict) -> dict:
        data = gate(record)
        placed = []
        for placement in data["placements"][:max_place]:
            candidate = candidates[placement["figure"]]
            placed.append(
                {
                    "after_paragraph": placement["after_paragraph"],
                    "project": candidate["project"],
                    "file": candidate["file"],
                    "caption": candidate["caption"][:300],
                }
            )
        return {
            "page_hash": page_hash,
            "placements": placed,
            "csv_flags": [flag[:300] for flag in data.get("csv_flags", [])[:3]],
        }

    def publish(record: dict) -> None:
        key = f"{page_id}.md"
        state_path = scope.root / STATE
        placements_path = scope.root / PLACEMENTS
        write_state(state_path, cards.load_state(state_path) | {key: f"kb:{scope.run}"})
        write_state(placements_path, cards.load_state(placements_path) | {key: record})
        adopt_legacy_state(scope.store, page_id, text)

    return Job(
        stage="figures",
        key=f"figures/{page_id}",
        pack={
            "MAX_PLACE": max_place,
            "PAGE_PARAGRAPHS": [
                paragraph if len(paragraph) <= limit else paragraph[:limit] + " […]"
                for paragraph in paragraphs
            ],
            "CANDIDATE_FIGURES": [
                c | {"caption": c["caption"][:300], "context": c["context"][:200]}
                for c in candidates
            ],
        },
        check=check,
        publish=publish,
        writer="figures",
        reviewer="",
    )


def jobs(scope: Scope) -> list[Job]:
    """Publish the deterministic manifest, then queue one job per owed page."""
    root, store = scope.root, scope.store
    suffix = "__REPORT"
    corpus = scope.reason == "compile" and not scope.source
    if corpus:
        projects = set(scope.sources) - set(DIGESTS)
        touched = {
            f"{kind}/{path.stem}"
            for kind in figures.MAX_PLACE
            for path in (root / "wiki" / kind).glob("*.md")
            if path.stem != "index"
        }
    else:
        projects = set(store.corpus_sources()) - set(DIGESTS)
        projects.update(
            path.stem.removesuffix(suffix) for path in (root / "wiki/sources").glob("*__REPORT.md")
        )
        touched = set(scope.created) | {section.split("#", 1)[0] for section in scope.edited}
    # A raw report needs its figures even when no page needs new placements.
    wanted = projects.copy() if corpus else {scope.source} & projects
    saved = cards.load_state(root / PLACEMENTS)
    todo = []
    for page_id in sorted(touched):
        kind, _, slug = page_id.partition("/")
        page = store.page_path(page_id)
        if kind not in figures.MAX_PLACE or not page.is_file():
            continue
        text = page.read_text(encoding="utf-8", errors="replace")
        if kind == "summaries":
            project = slug.removesuffix(suffix)
            sources = [project] if not corpus or project in projects else []
        else:
            sources = figures.cited_projects(text, projects)
        wanted.update(sources)
        if saved.get(f"{page_id}.md", {}).get("page_hash") != sha256(text)[:16]:
            todo.append((page_id, text, sources))

    manifest = _publish_manifest(scope, wanted)
    _drop_withdrawn(root, manifest, {f"{page_id}.md" for page_id in touched})
    owed = []
    for page_id, text, sources in todo:
        candidates = [
            {"project": project, **fig}
            for project in sources
            for fig in manifest.get(project, [])[:6]
        ][: figures.MAX_CANDIDATES]
        # As in the curator: a page whose reports embed no figure has nothing to place.
        if candidates:
            owed.append(_job(scope, page_id, text, candidates))
    return owed


def after(scope: Scope, outcomes: dict[str, dict]) -> None:
    """The review queue of pages flagged as needing a chart, as the curator writes it."""
    saved = cards.load_state(scope.root / PLACEMENTS)
    flagged = {key: item["csv_flags"] for key, item in saved.items() if item.get("csv_flags")}
    queue = scope.root / "state" / "figures-csv-queue.md"
    if not flagged:
        queue.unlink(missing_ok=True)
        return
    lines = [
        "# CSV / visualization review queue",
        "",
        "Pages the placement pass flagged as needing a chart for evidence with no figure.",
        "",
    ]
    for key, flags in sorted(flagged.items()):
        lines += [f"## {key}", *(f"- {flag}" for flag in flags), ""]
    text = "\n".join(lines)
    if not queue.exists() or queue.read_text(encoding="utf-8") != text:
        write_text(queue, text)
