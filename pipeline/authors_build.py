#!/usr/bin/env python3
"""Author-contributions stage: a factual record of each author's corpus work.

Runs after extra_pages has written the deterministic author stubs (name,
ORCID, project list). Per author (hash-cached in state/authors.json on their
name + their projects' summary texts + PROMPT_REV), one Luna call writes a
## Contributions section — what each project did and what it reported —
grounded ONLY in the corpus, with [src: project] tags. Two deterministic
repairs guard it: invalid [src:] ids are stripped (same as topics_build), and
sentences that characterise the *person* rather than the work are removed
after one violation-quoting retry. The section is spliced before ## Projects,
and extra_pages carries it across regenerations.

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
HEADING = "## Contributions"
# Bump when CONTRIB_USER or SUBJECTIVE changes: it is folded into the cache
# digest, so editing the prompt re-runs every author instead of needing
# state/authors.json to be deleted by hand.
PROMPT_REV = 2

CONTRIB_USER = """\
Write a "{heading}" section for the wiki page of: {name}

Their projects' summary pages are above. This section is a factual record of
what they worked on and what those projects reported — nothing else.

- 2-3 paragraphs, grouped by subject matter. Every sentence states what a
  project did or what it found, with exact numbers where load-bearing:
  "<project> did X and found Y."
- Do NOT characterise this person. No research interests, motivations,
  emphases, recurring themes, focus, or "research program"; no sentence of
  the form "their work suggests/centers on...". Attribute every finding to
  the project that reported it, never a disposition to the person.
- No employment, career, seniority, or personal details — this corpus only
  knows their projects.
- Ground EVERY claim in the summaries above with [src: <project_id>] tags;
  write nothing the corpus does not support.
- Link project summaries as [[summaries/<id>__REPORT]] and, sparingly,
  relevant [[concepts/...]] pages named in the summaries.

Return ONLY the section Markdown, starting with "{heading}" (no fences).
"""

# Phrasings that ascribe interests, motives or a research identity to the
# person. The corpus knows which projects someone worked on and what those
# projects reported; everything below is an inference on top of that, which is
# exactly what these pages must not carry.
SUBJECTIVE = re.compile(
    r"\b(?:research |recurring |apparent )?interests?\b"
    r"|\bresearch program\b"
    r"|\bsuggest(?:s|ed|ing)?\b"
    r"|\bcent(?:er|re)(?:s|ed)? (?:on|around)\b"
    r"|\bfocus(?:es|ed)? on\b"
    r"|\bmotivat\w+"
    r"|\bemphasi[sz]\w+"
    r"|\bappears? to\b|\bapparent(?:ly)?\b"
    r"|\brecurring theme\w*",
    re.I,
)
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[])")


def subjective_hits(section: str) -> list[str]:
    """Sentences that characterise the person rather than report the work."""
    return [s.strip() for s in SENTENCE.split(section) if SUBJECTIVE.search(s)]


def strip_subjective(section: str) -> str:
    """Deterministic repair: drop offending sentences, keep the rest.

    Mirrors topics_build's strip_bad_src fallback — a page that survives one
    retry still ships, minus the sentences that failed."""
    out = []
    for para in section.split("\n\n"):
        if para.lstrip().startswith("#"):
            out.append(para)
            continue
        kept = [s for s in SENTENCE.split(para) if not SUBJECTIVE.search(s)]
        if kept:
            out.append(" ".join(s.strip() for s in kept))
    return "\n\n".join(out)


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
        digest = hashlib.sha256(
            (f"r{PROMPT_REV}" + name + "".join(f"{k}{v}" for k, v in sorted(summaries.items()))).encode()
        ).hexdigest()[:16]
        if state.get(page.name) == digest:
            skipped += 1
            continue
        print(f"  writing contributions for {name} ({len(summaries)} project(s))")
        ctx = "\n\n---\n\n".join(f"[summary: {pid}]\n{text}" for pid, text in summaries.items())
        msgs = [{"role": "system", "content": system},
                {"role": "user", "content": f"SUMMARIES OF THIS AUTHOR'S PROJECTS:\n\n{ctx}"},
                {"role": "user", "content": CONTRIB_USER.format(name=name, heading=HEADING)}]
        try:
            section = C.llm(msgs, f"authors/{page.stem}").strip()
            hits = subjective_hits(section)
            if hits:  # one violation-quoting retry, then deterministic repair
                print(f"    ! {len(hits)} sentence(s) characterising the person — retrying")
                section = C.llm(
                    msgs + [{"role": "assistant", "content": section},
                            {"role": "user", "content":
                             "These sentences characterise the person rather than report the work:\n"
                             + "\n".join(f"- {h}" for h in hits[:8])
                             + "\n\nRewrite the whole section. State only what each project did and "
                               "what it reported. Never write what this person is interested in, "
                               "focused on, motivated by, or what their work suggests about them."}],
                    f"authors/{page.stem}/retry").strip()
                if subjective_hits(section):
                    print("    ! still characterising — stripping offending sentences")
                    section = strip_subjective(section)
        except C.PageError as e:
            print(f"    [ERROR] {e} — section skipped")
            failed += 1
            continue
        if not section.startswith(HEADING):
            section = f"{HEADING}\n\n" + section
        bad = bad_src_ids(section, set(summaries))
        if bad:
            print(f"    ! stripping invalid [src:] ids {bad}")
            section = strip_bad_src(section, set(summaries))
            section = C.downgrade_dead_links(section, C.wikilink_targets(C.REPO))

        body = re.sub(r"^## (?:Profile|Contributions)\s*\n.*?(?=\n## |\Z)", "", stub, flags=re.M | re.S)
        at = body.find("## Projects")
        at = at if at >= 0 else len(body)
        page.write_text(body[:at].rstrip() + "\n\n" + section + "\n\n" + body[at:], encoding="utf-8")
        state[page.name] = digest
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        done += 1

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(f"authors_build: {done} section(s) written, {skipped} unchanged, {failed} failed; "
          f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
