#!/usr/bin/env python3
"""Copy the OpenKB wiki + wiki-extra pages into a Quartz content/ dir.

Adapted from the v2 compendium prototype. Transformations:
  - [src: a; b] / [src: a, b] tags become wikilinks to the project summary pages
  - AGENTS.md, log.md, and reports/ are skipped (operational files, not content)

Usage: quartz_ingest.py <kb-root> <quartz-content-dir>
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys

import evidence

SRC_TAG = re.compile(r"\[src:\s*([^\]]+)\]")
FM = re.compile(r"^(---\n.*?\n---\n)", re.S)
SKIP = {"AGENTS.md", "log.md"}
# Every page says this, because a reader can land on any page. Rendered as an
# Obsidian callout (Quartz styles these natively — no custom CSS), whose title
# carries the computed evidence terms from pipeline/evidence.py when the page
# has any.
# One line, no embedded newline: the callout prefixes each line with "> ", so a
# wrapped string would put its tail outside the blockquote.
PROVENANCE = ("Compiled by pipeline from AI-conducted research reports. Not all of it "
              "has been reviewed by a scientist. See [[about|About This Wiki]].")


# Landing pages for collections that have no index.md of their own. Without
# these Quartz auto-generates a bare folder listing, which carries no
# provenance callout — the one route by which a reader could reach a published
# page that does not say how the wiki was made. Wording tracks about.md.
COLLECTION_INDEX = {
    "concepts": ("Concepts",
                 "Recurring ideas, each accumulating evidence from every project "
                 "in the corpus that speaks to it."),
    "entities": ("Entities",
                 "Specific named things: organisms, genes and pathways, compounds, "
                 "methods, and datasets. Entities cited by only one project are not "
                 "published."),
    "topics": ("Topics",
               "Hubs that cluster related concepts. Each opens with a "
               "literature-context section whose citations were verified against "
               "PubMed when it was written."),
    "conflicts": ("Conflicts",
                  "Places where projects in the corpus disagree, with the evidence "
                  "on each side and the work that would resolve it."),
    "summaries": ("Summaries",
                  "One page per research project, linking to its raw report."),
    "sources": ("Sources",
                "The raw research reports the wiki is compiled from, unedited."),
}


def write_collection_indexes(dst: pathlib.Path) -> int:
    """Give every collection a real landing page, so none is an untitled,
    unattributed auto-listing. Quartz appends its file listing below this."""
    n = 0
    for slug, (title, blurb) in COLLECTION_INDEX.items():
        d = dst / slug
        if not d.is_dir() or (d / "index.md").exists():
            continue
        # No page count here: Quartz's folder page already renders "N items
        # under this folder" directly below. A second count would be a second
        # number to keep in step, saying the same thing.
        (d / "index.md").write_text(
            f"---\ntitle: {json.dumps(title)}\n---\n"
            f"{provenance_block(None)}\n\n{blurb}\n",
            encoding="utf-8")
        n += 1
    return n


def provenance_block(evidence_terms: str | None) -> str:
    title = f"Evidence · {evidence_terms}" if evidence_terms else "Provenance"
    return f"> [!info] {title}\n> {PROVENANCE}"


def promote_title(text: str) -> str:
    """Move the page's H1 into `title:` frontmatter and drop it from the body.

    Quartz titles a page from frontmatter and falls back to the slug, so
    without this every page's heading, browser tab, explorer entry and social
    card read `antimicrobial-resistance-fitness-cost` while the real title sat
    below it in the body as a duplicate H1."""
    m = re.search(r"^# +(.+?)[ \t]*$", text, re.M)
    if not m:
        return text
    title = json.dumps(m.group(1).strip())
    text = text[:m.start()] + text[m.end():].lstrip("\n")
    fm = FM.match(text)
    if fm:  # splice into the existing block, before its closing ---
        return text[:fm.end() - 4] + f"title: {title}\n" + text[fm.end() - 4:]
    return f"---\ntitle: {title}\n---\n" + text


def insert_after_fm(text: str, block: str) -> str:
    """Put a block at the very top of the body, under any frontmatter."""
    m = FM.match(text)
    at = m.end() if m else 0
    return text[:at] + block + "\n\n" + text[at:]


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
    pars = split_paragraphs(body)
    for pl in sorted(entry["placements"], key=lambda p: -p["after_paragraph"]):
        src = fig_src(kb, pl["project"], pl["file"])
        if not src.exists():
            continue
        name = pathlib.Path(pl["file"]).name
        copy_figure(src, dst_root / "figures" / pl["project"] / name)
        block = (f"![{pl['caption']}](../figures/{pl['project']}/{name})\n"
                 f"*{pl['caption']}. From [[summaries/{pl['project']}__REPORT|{pl['project']}]].*")
        idx = pl["after_paragraph"]
        if idx < len(pars):
            pars.insert(idx + 1, block)
    return front + "\n\n".join(pars) + "\n"


def rewrite_source_figures(text: str, project: str, kb: pathlib.Path, dst_root: pathlib.Path) -> str:
    def repl(m: re.Match) -> str:
        src = fig_src(kb, project, m.group(2))
        if not src.exists():
            return m.group(1)  # drop the broken embed, keep the alt text
        name = pathlib.Path(m.group(2)).name
        copy_figure(src, dst_root / "figures" / project / name)
        return f"![{m.group(1)}](../figures/{project}/{name})"

    return re.sub(r"!\[([^\]]*)\]\((figures/[^)]+)\)", repl, text)


def linkify_src(text: str, summary_pages: dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        links = []
        for part in re.split(r"[,;]", m.group(1)):
            sid = re.sub(r"__REPORT$", "", part.strip())
            if not sid:
                continue
            page = summary_pages.get(sid)
            links.append(f"[[summaries/{page}|{sid}]]" if page else sid)
        return "<sub>src: " + ", ".join(links) + "</sub>"

    return SRC_TAG.sub(repl, text)


def _slug(s: str) -> str:
    return re.sub(r"[^a-z0-9/]+", "-", s.lower()).strip("-")


def strip_dead_wikilinks(text: str, targets: set[str]) -> str:
    """Downgrade [[links]] Quartz can't resolve to plain text.

    Quartz resolves slugified targets by full path or file basename, so both are
    accepted here. The wiki source keeps the dangling links (future compiles may
    create the targets); only the published site hides them.
    """
    by_basename: dict[str, list[str]] = {}
    for t in targets:
        by_basename.setdefault(t.rsplit("/", 1)[-1], []).append(t)

    def repl(m: re.Match) -> str:
        slug, label = _slug(m.group(1).lstrip("/")), m.group(2)
        if slug in targets:
            return m.group(0)
        hits = by_basename.get(slug.rsplit("/", 1)[-1], [])
        if len(hits) == 1:  # wrong/omitted namespace but unique page: repair the path
            return f"[[{hits[0]}|{label or m.group(1).rsplit('/', 1)[-1]}]]"
        return label or m.group(1).rsplit("/", 1)[-1].replace("-", " ")

    return re.sub(r"\[\[([^\]|#]+?)(?:\|([^\]]*))?\]\]", repl, text)


def single_source_entities(kb: pathlib.Path) -> set[str]:
    """Entity pages citing exactly one source: passing-mention noise at
    publish time. Filtered from the site (links downgrade to plain text); the
    wiki source keeps them, and they surface once a second doc cites them."""
    out = set()
    for f in (kb / "wiki" / "entities").glob("*.md"):
        m = FM.match(f.read_text(encoding="utf-8", errors="replace"))
        if m and len(re.findall(r"summaries/", m.group(1))) == 1:
            out.add(f.stem)
    return out


def concept_uptake(kb: pathlib.Path) -> dict[str, list[str]]:
    """project id -> concept stems whose pages cite it (deterministic
    reverse index; becomes the 'Feeds into' line on summary pages)."""
    up: dict[str, list[str]] = {}
    for f in sorted((kb / "wiki" / "concepts").glob("*.md")):
        text = f.read_text(encoding="utf-8", errors="replace")
        for m in SRC_TAG.finditer(text):
            for part in re.split(r"[,;]", m.group(1)):
                sid = re.sub(r"__REPORT$", "", part.strip())
                if sid and f.stem not in up.setdefault(sid, []):
                    up[sid].append(f.stem)
    return up


def main() -> None:
    kb, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    known = {
        re.sub(r"__REPORT$", "", f.stem): f.stem
        for f in (kb / "wiki" / "summaries").glob("*.md")
    }
    skip_entities = single_source_entities(kb)
    uptake = concept_uptake(kb)
    targets = {
        _slug(str(f.relative_to(root)).removesuffix(".md"))
        for root in (kb / "wiki", kb / "wiki-extra") if root.is_dir()
        for f in root.rglob("*.md")
        if not (root.name == "wiki" and f.parent.name == "entities" and f.stem in skip_entities)
    }
    targets.add("catalog")  # wiki/index.md is renamed to catalog.md below
    targets.discard("index")
    pl_path = kb / "state" / "figures-placements.json"
    placements = json.loads(pl_path.read_text()) if pl_path.exists() else {}
    conflict_srcs = evidence.conflict_sources(kb)
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
            if root.name == "wiki" and rel == pathlib.Path("index.md"):
                rel = pathlib.Path("catalog.md")
            out = dst / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            text = src.read_text(encoding="utf-8", errors="replace")
            if rel.parts[0] == "sources" and rel.stem.endswith("__REPORT"):
                text = rewrite_source_figures(text, re.sub(r"__REPORT$", "", rel.stem), kb, dst)
            entry = placements.get(str(rel))
            if entry and entry.get("placements"):
                text = splice_figures(text, entry, kb, dst)
            # Count the evidence before linkify_src rewrites [src:] tags into
            # <sub> links — after it there is nothing left to count.
            ev = evidence.label(text, rel.parts[0], conflict_srcs)
            text = linkify_src(strip_dead_wikilinks(text, targets), known)
            # Blocks that render directly under the title, in this order.
            # Provenance on every page, plus — on synthesis pages — how much of
            # the corpus stands behind it. The evidence line is computed, not
            # judged: see pipeline/evidence.py on why it is not the v1 atlas's
            # human `confidence:` field. The about page explains both, so it
            # does not carry the banner pointing at itself.
            head = [] if rel.stem == "about" else [provenance_block(ev)]
            # Summaries must lead to their raw report, and self-[src:] tags are
            # circular — point both at the sources/ page (the provenance hop
            # reviewers need).
            if rel.parts[0] == "summaries":
                nav = []
                if (root / "sources" / src.name).exists():
                    raw = f"sources/{rel.stem}"
                    text = text.replace(f"[[summaries/{rel.stem}|", f"[[{raw}|")
                    nav.append(f"> Raw report: [[{raw}|{rel.stem}]]")
                feeds = uptake.get(re.sub(r"__REPORT$", "", rel.stem), [])
                if feeds:
                    links = ", ".join(f"[[concepts/{c}]]" for c in feeds)
                    nav.append(f"> Feeds into: {links}")
                if nav:
                    head.append("\n".join(nav))
            # Title must move into frontmatter before the blocks go in, since
            # this is what removes the H1 they would otherwise sit under.
            text = promote_title(text)
            if head:
                text = insert_after_fm(text, "\n\n".join(head))
            out.write_text(text, encoding="utf-8")
            n += 1

    n += write_collection_indexes(dst)

    images = kb / "wiki" / "sources" / "images"
    if images.is_dir():
        shutil.copytree(images, dst / "sources" / "images", dirs_exist_ok=True)

    print(f"wrote {n} pages -> {dst}")


if __name__ == "__main__":
    main()
