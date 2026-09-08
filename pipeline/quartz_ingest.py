#!/usr/bin/env python3
"""Copy the OpenKB wiki + wiki-extra pages into a Quartz content/ dir.

Adapted from the v2 compendium prototype. Transformations:
  - Native Markdown paths are remapped when collection directories combine
  - AGENTS.md, log.md, and reports/ are skipped (operational files, not content)

Usage: quartz_ingest.py <kb-root> <quartz-content-dir>
"""

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
from urllib.parse import unquote, urlsplit

import okf

SKIP = {"AGENTS.md", "log.md"}
FM = re.compile(r"^(---\n.*?\n---\n)", re.S)
BIG_FIGURE = 1_500_000  # bytes; larger images are downscaled at publish


def copy_figure(src: pathlib.Path, dst: pathlib.Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        return
    if src.stat().st_size > BIG_FIGURE and shutil.which("sips"):
        subprocess.run(["sips", "-Z", "1600", str(src), "--out", str(dst)],
                       check=False, capture_output=True)
        if dst.exists():
            return
    shutil.copy2(src, dst)


def split_paragraphs(body: str) -> list[str]:
    """Raw paragraph chunks; same inclusion rule as figures_build.paragraphs
    so placement indices line up."""
    return [c for c in re.split(r"\n\s*\n", body) if c.strip()]


def fig_src(kb: pathlib.Path, project: str, rel: str) -> pathlib.Path:
    """A figure's committed location: wiki/figures/<project>/<path-under-figures/>."""
    return kb / "wiki" / "figures" / project / re.sub(r"^figures/", "", rel)


def splice_figures(text: str, entry: dict, kb: pathlib.Path, dst_root: pathlib.Path) -> str:
    if hashlib.sha256(text.encode()).hexdigest()[:16] != entry.get("page_hash"):
        return text  # page changed since placement; figures_build will re-run
    m = FM.match(text)
    front, body = (m.group(1), text[m.end():]) if m else ("", text)
    definitions = []
    def retain_definitions(chunk: str) -> str:
        definitions.extend(m[0] for m in okf.DEFINITION.finditer(chunk))
        return okf.DEFINITION.sub("", chunk)
    pars = split_paragraphs(okf.map_prose(body, retain_definitions))
    for pl in sorted(entry["placements"], key=lambda p: -p["after_paragraph"]):
        src = fig_src(kb, pl["project"], pl["file"])
        if not src.exists():
            continue
        name = pathlib.Path(pl["file"]).name
        copy_figure(src, dst_root / "figures" / pl["project"] / name)
        block = (f"![{pl['caption']}](../figures/{pl['project']}/{name})\n"
                 f"*{pl['caption']} — from [{pl['project']}](../summaries/{pl['project']}__REPORT.md)*")
        idx = pl["after_paragraph"]
        if idx < len(pars):
            pars.insert(idx + 1, block)
    return front + "\n\n".join(pars) + "\n\n" + "".join(definitions)


def rewrite_source_figures(text: str, project: str, kb: pathlib.Path, dst_root: pathlib.Path) -> str:
    def repl(m: re.Match) -> str:
        src = fig_src(kb, project, m.group(2))
        if not src.exists():
            return m.group(1)  # drop the broken embed, keep the alt text
        name = pathlib.Path(m.group(2)).name
        copy_figure(src, dst_root / "figures" / project / name)
        return f"![{m.group(1)}](../figures/{project}/{name})"

    return re.sub(r"!\[([^\]]*)\]\((figures/[^)]+)\)", repl, text)


def single_source_entities(kb: pathlib.Path) -> set[str]:
    """Entity pages citing exactly one source: passing-mention noise at
    publish time. Filtered from the site (links downgrade to plain text); the
    wiki source keeps them, and they surface once a second doc cites them."""
    out = set()
    for f in (kb / "wiki" / "entities").glob("*.md"):
        m = FM.match(f.read_text(encoding="utf-8", errors="replace"))
        if m and len(okf.parse(f.read_text(encoding="utf-8"))[0].get("sources", [])) == 1:
            out.add(f.stem)
    return out


def concept_uptake(kb: pathlib.Path) -> dict[str, list[str]]:
    """project id -> concept stems whose pages cite it (deterministic
    reverse index; becomes the 'Feeds into' line on summary pages)."""
    up: dict[str, list[str]] = {}
    for f in sorted((kb / "wiki" / "concepts").glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for sid in okf.cited_ids(text):
            if sid and f.stem not in up.setdefault(sid, []):
                up[sid].append(f.stem)
    return up


def site_path(path: pathlib.Path, root: pathlib.Path) -> pathlib.Path:
    """Map the two canonical collections to Quartz's shared content directory."""
    rel = path.relative_to(root)
    if rel == pathlib.Path("wiki/index.md"):
        return pathlib.Path("catalog.md")
    if rel == pathlib.Path("wiki-extra/home.md"):
        return pathlib.Path("index.md")
    if rel == pathlib.Path("wiki-extra/index.md"):
        return pathlib.Path("browse.md")
    return pathlib.Path(*rel.parts[1:])


def remap_links(text: str, src: pathlib.Path,
                paths: dict[pathlib.Path, pathlib.Path],
                hidden: set[pathlib.Path] | None = None) -> str:
    """Resolve links before flattening collection roots, retaining code examples."""
    paths = {p.resolve(): target for p, target in paths.items()}
    src = src.resolve()
    def replace(url: str) -> str:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc or not parts.path:
            return url
        target = (src.parent / unquote(parts.path)).resolve()
        if target not in paths:
            return url
        rel = pathlib.Path(os.path.relpath(paths[target], paths[src].parent)).as_posix()
        return rel + ("?" + parts.query if parts.query else "") + ("#" + parts.fragment if parts.fragment else "")
    hidden = hidden or set()
    def filter_links(chunk: str) -> str:
        def keep(match: re.Match) -> str:
            target = (src.parent / unquote(urlsplit(match[2]).path)).resolve()
            return match[1][1:-2] if target in hidden else match[0]
        return okf.LINK.sub(keep, chunk)
    return okf.map_links(okf.map_prose(text, filter_links), replace)


def main() -> None:
    kb, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    skip_entities = single_source_entities(kb)
    uptake = concept_uptake(kb)
    kb = kb.resolve()
    paths = {p: site_path(p, kb)
             for root in (kb / "wiki", kb / "wiki-extra")
             for p in root.rglob("*") if p.is_file() and p.name not in SKIP}
    hidden = {kb / "wiki/entities" / f"{name}.md" for name in skip_entities}
    pl_path = kb / "state" / "figures-placements.json"
    placements = json.loads(pl_path.read_text()) if pl_path.exists() else {}
    shutil.rmtree(dst, ignore_errors=True)

    n = 0
    for root in (kb / "wiki", kb / "wiki-extra"):
        if not root.is_dir():
            continue
        for src in root.rglob("*.md"):
            rel = src.relative_to(root)
            if src.name in SKIP or rel.parts[0] == "reports":
                continue
            if root.name == "wiki" and rel.parts[0] == "entities" and src.stem in skip_entities:
                continue
            # OpenKB's catalog index steps aside for the narrative home in wiki-extra/.
            rel = paths[src]
            out = dst / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            text = src.read_text(encoding="utf-8", errors="replace")
            if rel.parts[0] == "sources" and rel.stem.endswith("__REPORT"):
                text = rewrite_source_figures(text, re.sub(r"__REPORT$", "", rel.stem), kb, dst)
            entry = placements.get(str(rel))
            if entry and entry.get("placements"):
                text = splice_figures(text, entry, kb, dst)
            text = remap_links(text, src, paths, hidden)
            # Summaries must lead to their raw report, and self-[src:] tags are
            # circular — point both at the sources/ page (the provenance hop
            # reviewers need).
            if rel.parts[0] == "summaries":
                header_lines = []
                if (root / "sources" / src.name).exists():
                    raw = f"sources/{rel.stem}"
                    header_lines.append(f"> Raw report: [{rel.stem}](../{raw}.md)")
                feeds = uptake.get(re.sub(r"__REPORT$", "", rel.stem), [])
                if feeds:
                    links = ", ".join(f"[{c}](../concepts/{c}.md)" for c in feeds)
                    header_lines.append(f"> Feeds into: {links}")
                if header_lines:
                    text = re.sub(r"^# .+$", lambda m: m.group(0) + "\n\n" + "\n".join(header_lines),
                                  text, count=1, flags=re.M)
            if rel == pathlib.Path("index.md"):
                text += '\n\n<a href="./okf-graph.html" data-router-ignore>Explore the OKF graph</a>\n'
            out.write_text(text, encoding="utf-8")
            n += 1

    images = kb / "wiki" / "sources" / "images"
    if images.is_dir():
        shutil.copytree(images, dst / "sources" / "images", dirs_exist_ok=True)
    figures = kb / "wiki" / "figures"
    if figures.is_dir():
        shutil.copytree(figures, dst / "figures", dirs_exist_ok=True)

    print(f"wrote {n} pages -> {dst}")


if __name__ == "__main__":
    main()
