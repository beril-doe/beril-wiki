#!/usr/bin/env python3
"""Deterministic wiki pages OpenKB shouldn't hallucinate: authors and data collections.

Carried over from v1/v2: author pages from project README ``## Authors`` blocks
(ORCID-keyed, via people.py) and data-collection pages from ui/config/collections.yaml.
Output goes to wiki-extra/ (NOT wiki/ — OpenKB owns that tree) and is merged into
the Quartz content dir at publish time by build_quartz.sh.

    .venv/bin/python extra_pages.py          # writes wiki-extra/{authors,data}/
"""

from __future__ import annotations

import pathlib
import re

import yaml

from fetch_reports import CHECKOUT
from people import build_author_index

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
OUT = ROOT / "wiki-extra"


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def wiki_projects() -> list[str]:
    """Project ids that have (or will have) a summary page, from staging/."""
    return sorted(
        re.sub(r"__REPORT$", "", f.stem)
        for f in (ROOT / "staging").glob("*__REPORT.md")
    )


def write_authors() -> int:
    readmes = {
        p.parent.name: (p.read_text(encoding="utf-8", errors="replace"))
        for p in CHECKOUT.glob("projects/*/README.md")
        if (p.parent / "REPORT.md").exists()
    }
    index = build_author_index(readmes)
    out = OUT / "authors"
    out.mkdir(parents=True, exist_ok=True)
    known = set(wiki_projects())
    for record in index.values():
        lines = [f"# {record.name}", ""]
        if record.orcid:
            lines.append(f"ORCID: [{record.orcid}](https://orcid.org/{record.orcid})")
            lines.append("")
        lines.append(f"## Projects ({len(record.projects)})")
        lines.append("")
        for proj in record.projects:
            link = f"[[summaries/{proj}__REPORT|{proj}]]" if proj in known else proj
            lines.append(f"- {link}")
        (out / f"{slugify(record.name)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(index)


def write_collections() -> int:
    cfg = yaml.safe_load((CHECKOUT / "ui/config/collections.yaml").read_text(encoding="utf-8"))
    out = OUT / "data"
    out.mkdir(parents=True, exist_ok=True)
    projects = wiki_projects()
    # Which projects mention this collection id in their report (cheap deterministic join).
    mention: dict[str, list[str]] = {}
    for proj in projects:
        text = (ROOT / "staging" / f"{proj}__REPORT.md").read_text(encoding="utf-8", errors="replace")
        for coll in cfg["collections"]:
            if coll["id"] in text:
                mention.setdefault(coll["id"], []).append(proj)

    for coll in cfg["collections"]:
        lines = [f"# {coll['name']}", ""]
        meta = [f"Provider: {coll.get('provider', '?')}"]
        if coll.get("website"):
            meta.append(f"[Website]({coll['website']})")
        if coll.get("doi"):
            meta.append(f"DOI: [{coll['doi']}](https://doi.org/{coll['doi']})")
        lines += [" · ".join(meta), ""]
        for key, heading in (("description", "Description"), ("philosophy", "Purpose")):
            if coll.get(key):
                lines += [f"## {heading}", "", str(coll[key]).strip(), ""]
        if coll.get("scale_stats"):
            lines += ["## Scale", ""]
            lines += [f"- {k}: {v:,}" if isinstance(v, int) else f"- {k}: {v}"
                      for k, v in coll["scale_stats"].items()]
            lines.append("")
        used = mention.get(coll["id"], [])
        if used:
            lines += [f"## Used by projects ({len(used)})", ""]
            lines += [f"- [[summaries/{p}__REPORT|{p}]]" for p in used]
            lines.append("")
        (out / f"{slugify(coll['id'])}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(cfg["collections"])


def write_opportunities() -> int:
    """Aggregate every concept's ## Open Directions into one browse page."""
    lines = ["# Research Opportunities", "",
             "Concrete next analyses this corpus makes possible — every concept page's",
             "Open Directions, gathered in one place. Follow a link for the evidence.", ""]
    n = 0
    for page in sorted((ROOT / "wiki/concepts").glob("*.md")):
        text = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^## Open Directions\s*\n(.*?)(?=\n## |\Z)", text, re.M | re.S)
        if not m or not m.group(1).strip():
            continue
        h1 = re.search(r"^# (.+)$", text, re.M)
        lines += [f"## [[concepts/{page.stem}|{h1.group(1).strip() if h1 else page.stem}]]", "",
                  m.group(1).strip(), ""]
        n += 1
    (OUT / "opportunities.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return n


def write_negative_results() -> int:
    """Digest of the summaries' caveat/limitation/null-result sections, so
    collaborators can see what did not work before repeating it."""
    # [^\n]* keeps the heading match on its own line — a dot under re.S would
    # swallow the section body and capture nothing.
    pat = re.compile(r"^## [^\n]*(?:caveat|limitation|negative|null|did not work)[^\n]*\n(.*?)(?=\n## |\Z)",
                     re.M | re.S | re.I)
    lines = ["# Negative Results and Caveats", "",
             "What each project reports as limitations, null results, or abandoned",
             "analyses — read before repeating an analysis.", ""]
    n = 0
    for page in sorted((ROOT / "wiki/summaries").glob("*.md")):
        text = page.read_text(encoding="utf-8", errors="replace")
        blocks = [m.group(1).strip() for m in pat.finditer(text) if m.group(1).strip()]
        if not blocks:
            continue
        h1 = re.search(r"^# (.+)$", text, re.M)
        lines += [f"## [[summaries/{page.stem}|{h1.group(1).strip() if h1 else page.stem}]]", "",
                  "\n\n".join(blocks), ""]
        n += 1
    (OUT / "negative-results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return n


def write_indexes() -> None:
    for sub, title in (("authors", "Authors"), ("data", "Data Collections")):
        pages = sorted(p.stem for p in (OUT / sub).glob("*.md") if p.stem != "index")
        lines = [f"# {title}", ""]
        lines += [f"- [[{sub}/{s}|{s.replace('-', ' ').title()}]]" for s in pages]
        (OUT / sub / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    n_a = write_authors()
    n_c = write_collections()
    n_o = write_opportunities()
    n_n = write_negative_results()
    write_indexes()
    print(f"wrote {n_a} author pages, {n_c} collection pages, opportunities ({n_o} concepts), "
          f"negative-results ({n_n} projects) + 2 indexes -> {OUT}")
