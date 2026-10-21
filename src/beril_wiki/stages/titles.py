#!/usr/bin/env python3
"""Give every generated page the title its plan chose.

Quartz titles a page from its H1 (publish/ingest.py promotes it to frontmatter)
and falls back to the slug. The page writer's prompt never asked for an H1, so
31 pages written by the October 2026 compile published as
`foreign-dump-ingestion-fidelity` and `cohens-d`. The planner had already named
each one: the title is in the plan the curator keeps beside its ledger. This
stage writes that title as the page's H1 wherever the H1 is missing.

Deterministic and idempotent; no model call. A page with no H1 and no planned
title is left for beril_wiki.check, which fails on it.

    uv run python -m beril_wiki.stages.titles [<root>]
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

from beril_wiki.agentic.runtime import configured, runtime_config
from beril_wiki.check import FENCED, FRONTMATTER, has_title
from beril_wiki.paths import ROOT

DIRS = ("concepts", "entities", "summaries", "topics", "conflicts", "authors")


def with_title(text: str, title: str) -> str:
    """The page with `# title` as the first line of its body."""
    fm = FRONTMATTER.match(text)
    head, body = (text[: fm.end()], text[fm.end() :]) if fm else ("", text)
    return f"{head}# {title}\n\n{body.lstrip()}"


def h1_of(text: str) -> str:
    body = FENCED.sub("", FRONTMATTER.sub("", text, count=1))
    m = re.search(r"^# +(.+?)\s*$", body, re.M)
    return m.group(1).strip() if m else ""


def fallback_title(root: pathlib.Path, rel: str, old: str = "") -> str:
    """A title for a page whose plan has none: summaries and recheck jobs are titled
    with their slug. Use the page's previous H1, or for a summary its report's title."""
    if title := h1_of(old):
        return title
    report = root / "staging" / pathlib.PurePosixPath(rel).name
    if rel.startswith("summaries/") and report.exists():
        return re.sub(r"^Report:\s*", "", h1_of(report.read_text(encoding="utf-8")))
    return ""


def planned_titles(store: pathlib.Path) -> dict[str, str]:
    """Page path -> title from the curator's last plan. A recheck job is titled with
    its slug, which is no title at all, so those are dropped."""
    plan = store / "last-plan.json"
    if not plan.exists():
        return {}
    pages = json.loads(plan.read_text(encoding="utf-8")).get("pages", [])
    return {
        p["path"]: p["title"].strip()
        for p in pages
        if p.get("title", "").strip() and p["title"].strip() != pathlib.Path(p["path"]).stem
    }


def apply(root: pathlib.Path, titles: dict[str, str]) -> tuple[list[str], list[str]]:
    """Title every untitled page from its plan, or failing that its fallback title.
    Returns (titled, untitled)."""
    titled: list[str] = []
    untitled: list[str] = []
    for sub in DIRS:
        for path in sorted((root / "wiki" / sub).glob("*.md")):
            text = path.read_text(encoding="utf-8")
            if has_title(text):
                continue
            rel = f"{sub}/{path.name}"
            title = titles.get(rel) or fallback_title(root, rel)
            if not title:
                untitled.append(rel)
                continue
            path.write_text(with_title(text, title), encoding="utf-8")
            titled.append(rel)
    return titled, untitled


def main() -> int:
    root = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT
    # Inside a curator run the page tree is a candidate copy; the plan stays in the store.
    store = pathlib.Path(runtime_config()["store"]) if configured() else root / ".agentic"
    titled, untitled = apply(root, planned_titles(store))
    print(f"stages.titles: {len(titled)} page(s) titled from the plan")
    for rel in untitled:
        print(f"  WARN  {rel}: no H1 and no planned title")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
