#!/usr/bin/env python3
"""Author-contributions stage: a factual record of each author's corpus work.

Runs after stages.extras has written the deterministic author stubs (name,
ORCID, project list). Per author (hash-cached in state/authors.json on their
name + their projects' summary texts + PROMPT_REV), one Luna call writes a
## Contributions section — what each project did and what it reported —
grounded ONLY in the corpus, with [src: project] tags. Two deterministic
repairs guard it: invalid [src:] ids are stripped (same as stages.topics), and
sentences that characterise the *person* rather than the work are removed
after one violation-quoting retry. The section is spliced before ## Projects,
and stages.extras carries it across regenerations.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.authors
"""

from __future__ import annotations

import hashlib
import json
import re
import sys

from beril_wiki import compiler as C
from beril_wiki.paths import ROOT
from beril_wiki.stages.topics import bad_src_ids, strip_bad_src

PER_SUMMARY_CHARS = 5000
HEADING = "## Contributions"
# Bump when CONTRIB_USER changes: it is folded into the cache digest, so
# editing the prompt re-runs every author instead of needing
# state/authors.json cleared by hand. Loosening the subjectivity guard needs
# no bump — it cannot invalidate a page that already passed the stricter one.
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

# Two tiers, because the same verb can report a result or characterise a
# person. ALWAYS names a disposition that only makes sense about someone —
# there is no innocent reading of "their research interests" or "interested
# in". ABOUT_PERSON holds predicates that are only a problem when the sentence
# is about the author: "the project focused on metal tolerance" and "the
# results suggest a shared mechanism" are ordinary reporting and must survive,
# while "their projects focus on..." must not.
ALWAYS = re.compile(
    r"\b(?:research |recurring |apparent )?interests?\b"
    r"|\b(?:an |any )?interest in\b"
    r"|\binterested in\b"
    r"|\bresearch (?:program|programme|agenda|identity|focus)\b"
    r"|\brecurring theme\w*"
    r"|\bmotivat(?:ion|ions|ed by)\b"
    r"|\bpassionate about\b"
    r"|\bexpertise\b|\bknown for\b",
    re.I,
)
ABOUT_PERSON = re.compile(
    r"\bcent(?:er|re)(?:s|ed)? (?:on|around)\b"
    r"|\bfocus(?:es|ed|ing)? on\b"
    r"|\bsuggest(?:s|ed|ing)?\b"
    r"|\bemphasi[sz]\w+"
    r"|\bappears? to\b|\bapparent(?:ly)?\b"
    r"|\bprioriti[sz]\w+"
    r"|\b(?:devoted|dedicated|committed) to\b"
    r"|\bspecialis\w+|\bspecializ\w+"
    r"|\bworks on\b|\bstudies\b|\binvestigates\b",
    re.I,
)
# The author as the thing being described. Possessives only, never a bare
# "they"/"he"/"she": this corpus says "they" about genes, clusters and species
# far more often than about a person, and a bare pronoun flagged the factual
# sentence "...candidates for characterization because they were conserved".
# Constructions like "They are interested in X" are still caught, by ALWAYS.
# The author's own NAME counts as a subject — "Adam P. Arkin focuses on
# microbial systems" is the same claim as "his work focuses on...", and
# omitting the name was a reachable bypass. name_pattern() adds it per author.
PERSON_SUBJECT = re.compile(
    r"\b(?:their|his|her|the author'?s?|this (?:author|person|researcher)"
    r"|these projects|the corpus)\b",
    re.I,
)
SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[])")


def name_pattern(name: str) -> re.Pattern | None:
    """Match the author by full name or surname, so a sentence naming them is
    treated exactly like one that says "they"."""
    parts = [re.escape(p) for p in name.split() if len(p.rstrip(".")) > 1]
    if not parts:
        return None
    return re.compile(r"\b(?:" + re.escape(name) + r"|" + parts[-1] + r")\b", re.I)


def subjective_hits(section: str, name: str | None = None) -> list[str]:
    """Sentences that characterise the person rather than report the work."""
    who = name_pattern(name) if name else None
    out = []
    for s in SENTENCE.split(section):
        about_person = PERSON_SUBJECT.search(s) or (who and who.search(s))
        if ALWAYS.search(s) or (ABOUT_PERSON.search(s) and about_person):
            out.append(s.strip())
    return out


def strip_subjective(section: str, name: str | None = None) -> str:
    """Deterministic repair: drop offending sentences, keep the rest.

    Mirrors stages.topics's strip_bad_src fallback — a page that survives one
    retry still ships, minus the sentences that failed."""
    out = []
    for para in section.split("\n\n"):
        if para.lstrip().startswith("#"):
            out.append(para)
            continue
        kept = [s for s in SENTENCE.split(para) if not subjective_hits(s, name)]
        if kept:
            out.append(" ".join(s.strip() for s in kept))
    return "\n\n".join(out)


def author_projects(stub: str) -> list[str]:
    return re.findall(r"\[\[summaries/([\w.-]+?)__REPORT(?:\|[^\]]*)?\]\]", stub)


def main() -> int:
    authors_dir = ROOT / "wiki" / "authors"
    if not authors_dir.is_dir():
        print("stages.authors: no author stubs yet — run stages.extras first")
        return 0
    system = C.SYSTEM.format(contract=(ROOT / "contract" / "AGENTS.md").read_text(encoding="utf-8"))
    state_path = ROOT / "state" / "authors.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    done = skipped = failed = 0
    for page in sorted(authors_dir.glob("*.md")):
        if page.stem == "index":
            continue
        stub = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^# (.+)$", stub, re.M)
        name = m.group(1).strip() if m else page.stem
        projects = author_projects(stub)
        if not projects:
            continue
        summaries = {}
        for pid in projects:
            sp = ROOT / "wiki" / "summaries" / f"{pid}__REPORT.md"
            if sp.exists():
                summaries[pid] = C.parse_fm(sp.read_text(encoding="utf-8", errors="replace"))[1][
                    :PER_SUMMARY_CHARS
                ]
        if not summaries:
            continue
        digest = hashlib.sha256(
            (
                f"r{PROMPT_REV}" + name + "".join(f"{k}{v}" for k, v in sorted(summaries.items()))
            ).encode()
        ).hexdigest()[:16]
        if state.get(page.name) == digest:
            skipped += 1
            continue
        print(f"  writing contributions for {name} ({len(summaries)} project(s))")
        ctx = "\n\n---\n\n".join(f"[summary: {pid}]\n{text}" for pid, text in summaries.items())
        msgs = [
            {"role": "system", "content": system},
            {"role": "user", "content": f"SUMMARIES OF THIS AUTHOR'S PROJECTS:\n\n{ctx}"},
            {"role": "user", "content": CONTRIB_USER.format(name=name, heading=HEADING)},
        ]
        try:
            section = C.llm(msgs, f"authors/{page.stem}").strip()
            hits = subjective_hits(section, name)
            if hits:  # one violation-quoting retry, then deterministic repair
                print(f"    ! {len(hits)} sentence(s) characterising the person — retrying")
                section = C.llm(
                    msgs
                    + [
                        {"role": "assistant", "content": section},
                        {
                            "role": "user",
                            "content": "These sentences characterise the person rather than "
                            "report the work:\n"
                            + "\n".join(f"- {h}" for h in hits[:8])
                            + "\n\nRewrite the whole section. State only what each project did and "
                            "what it reported. Never write what this person is interested in, "
                            "focused on, motivated by, or what their work suggests about them.",
                        },
                    ],
                    f"authors/{page.stem}/retry",
                ).strip()
                if subjective_hits(section, name):
                    print("    ! still characterising — stripping offending sentences")
                    section = strip_subjective(section, name)
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
            section = C.downgrade_dead_links(section, C.wikilink_targets(ROOT))

        body = re.sub(
            r"^## (?:Profile|Contributions)\s*\n.*?(?=\n## |\Z)", "", stub, flags=re.M | re.S
        )
        at = body.find("## Projects")
        at = at if at >= 0 else len(body)
        page.write_text(
            body[:at].rstrip() + "\n\n" + section + "\n\n" + body[at:], encoding="utf-8"
        )
        state[page.name] = digest
        state_path.write_text(json.dumps(state, indent=1, sort_keys=True))
        done += 1

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    print(
        f"stages.authors: {done} section(s) written, {skipped} unchanged, {failed} failed; "
        f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)"
    )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
