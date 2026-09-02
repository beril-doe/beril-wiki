#!/usr/bin/env python3
"""Author-profile stage: hub-style synthesis of each author's corpus work.

Runs after extra_pages has written the deterministic author stubs (name,
ORCID, project list). Per author (hash-cached in state/authors.json on their
name + their projects' summary texts), one Luna call writes a ## Profile
section — contributions, recurring themes, apparent research interests —
grounded ONLY in the corpus, with [src: project] tags; invalid ids are
stripped deterministically (same repair as topics_build). The section is
spliced before ## Projects, and extra_pages carries it across regenerations.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python pipeline/authors_build.py
"""

from __future__ import annotations

import hashlib
import json
import pathlib
import re
import sys

import compile as C
from topics_build import bad_src_ids, strip_bad_src

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
PER_SUMMARY_CHARS = 5000

PROFILE_USER = """\
Write a "## Profile" section for the wiki page of author: {name}

Their projects' summary pages are above. Requirements:
- 2-3 paragraphs: what this author's projects investigated and found (their
  concrete contributions, with exact numbers where load-bearing), the
  recurring themes across their projects, and the research interests those
  themes suggest — phrased as inference from the corpus ("their projects
  center on..."), never as biography.
- Ground EVERY claim in the summaries above with [src: <project_id>] tags;
  write nothing the corpus does not support. No employment, career, or
  personal details — this corpus only knows their projects.
- Link project summaries as [[summaries/<id>__REPORT]] and, sparingly,
  relevant [[concepts/...]] pages named in the summaries.

Return ONLY the section Markdown, starting with "## Profile" (no fences).
"""


def author_projects(stub: str) -> list[str]:
    return re.findall(r"\[\[summaries/([\w.-]+?)__REPORT(?:\|[^\]]*)?\]\]", stub)


def main() -> int:
    authors_dir = ROOT / "wiki-extra" / "authors"
    if not authors_dir.is_dir():
        print("authors_build: no author stubs yet — run extra_pages first")
        return 0
    system = C.SYSTEM.format(contract=(C.REPO / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = ROOT / "state" / "authors.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    done = skipped = failed = 0
    for page in sorted(authors_dir.glob("*.md")):
        if page.stem == "index":
            continue
        stub = page.read_text(encoding="utf-8", errors="replace")
        name = (re.search(r"^# (.+)$", stub, re.M) or [None, page.stem]).group(1).strip()
        projects = author_projects(stub)
        if not projects:
            continue
        summaries = {}
        for pid in projects:
            sp = ROOT / "wiki" / "summaries" / f"{pid}__REPORT.md"
            if sp.exists():
                summaries[pid] = C.parse_fm(sp.read_text(encoding="utf-8", errors="replace"))[1][:PER_SUMMARY_CHARS]
        if not summaries:
            continue
        digest = hashlib.sha256((name + "".join(f"{k}{v}" for k, v in sorted(summaries.items()))).encode()).hexdigest()[:16]
        if state.get(page.name) == digest:
            skipped += 1
            continue
        print(f"  profiling {name} ({len(summaries)} project(s))")
        ctx = "\n\n---\n\n".join(f"[summary: {pid}]\n{text}" for pid, text in summaries.items())
        try:
            section = C.llm(
                [{"role": "system", "content": system},
                 {"role": "user", "content": f"SUMMARIES OF THIS AUTHOR'S PROJECTS:\n\n{ctx}"},
                 {"role": "user", "content": PROFILE_USER.format(name=name)}],
                f"authors/{page.stem}").strip()
        except C.PageError as e:
            print(f"    [ERROR] {e} — profile skipped")
            failed += 1
            continue
        if not section.startswith("## Profile"):
            section = "## Profile\n\n" + section
        bad = bad_src_ids(section, set(summaries))
        if bad:
            print(f"    ! stripping invalid [src:] ids {bad}")
            section = strip_bad_src(section, set(summaries))

        body = re.sub(r"^## Profile\s*\n.*?(?=\n## |\Z)", "", stub, flags=re.M | re.S)
        at = body.find("## Projects")
        at = at if at >= 0 else len(body)
        page.write_text(body[:at].rstrip() + "\n\n" + section + "\n\n" + body[at:], encoding="utf-8")
        state[page.name] = digest
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        done += 1

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(f"authors_build: {done} profile(s) written, {skipped} unchanged, {failed} failed; "
          f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
