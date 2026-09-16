#!/usr/bin/env python3
"""Author-contributions stage: a factual record of each author's corpus work.

Runs after stages.extras has written the deterministic author stubs (name,
ORCID, project list). Per author (hash-cached in state/authors.json on their
name + their projects' summary texts + PROMPT_REV), one packed prompt writes a
## Contributions section — what each project did and what it reported —
grounded ONLY in the corpus, with [src: project] tags. agentic.prose gates
it (invalid [src:] ids, unsupported figures, sentences that characterise the
*person* rather than the work), reviews it and patches it by paragraph; a
section that does not converge is recorded as a failure and the stub keeps
its previous text. The section is spliced before ## Projects, and
stages.extras carries it across regenerations.

    OPENAI_API_KEY=$CBORG_API_KEY OPENAI_BASE_URL=https://api.cborg.lbl.gov \
        uv run python -m beril_wiki.stages.authors
"""

from __future__ import annotations

import hashlib
import json
import re
import sys

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import (
    NO_PREAMBLE,
    PLATFORM,
    Contract,
    Issue,
    PageFailure,
    derived_page,
    excerpts,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import atomic_json, configured
from beril_wiki.check import source_ids
from beril_wiki.paths import ROOT

PER_SUMMARY_CHARS = 5000
HEADING = "## Contributions"
# Bump when the contract changes: it is folded into the cache digest, so
# editing the prompt re-runs every author instead of needing
# state/authors.json cleared by hand. Loosening the subjectivity guard needs
# no bump — it cannot invalidate a page that already passed the stricter one.
PROMPT_REV = 3

CONTRACT = Contract(
    rules=(
        "Write 2-4 paragraphs grouped by subject matter; every sentence states what a project "
        "did or what it found, with exact figures where load-bearing: '<project> did X and "
        "found Y.'",
        f"Begin with the heading '{HEADING}' and write nothing before it.",
        "Ground every claim in the SUMMARIES with [src: <project id>] tags naming only this "
        "author's projects; write nothing the summaries do not support, copy figures exactly, "
        "and keep each summary's caveats and null results as stated.",
        "Do not characterise the person: no research interests, motivations, emphases, "
        "recurring themes, focus, expertise or 'their work suggests'; attribute every finding "
        "to the project that reported it. No employment, career, seniority or personal "
        "details; this corpus only knows their projects.",
        "Link project summaries as [[summaries/<id>__REPORT]] and, sparingly, "
        "[[concepts/<stem>]] pages the summaries name.",
        NO_PREAMBLE.format(first=f"'{HEADING}'"),
        PLATFORM,
    ),
    first=HEADING,
)

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


def author_projects(stub: str) -> list[str]:
    return re.findall(r"\[\[summaries/([\w.-]+?)__REPORT(?:\|[^\]]*)?\]\]", stub)


def main() -> int:
    authors_dir = ROOT / "wiki" / "authors"
    if not authors_dir.is_dir():
        print("stages.authors: no author stubs yet — run stages.extras first")
        return 0
    src_texts = source_ids(ROOT)
    state_path = ROOT / "state" / "authors.json"
    state_path.parent.mkdir(exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {}

    todo = []
    skipped = 0
    for page in sorted(authors_dir.glob("*.md")):
        if page.stem == "index":
            continue
        stub = page.read_text(encoding="utf-8", errors="replace")
        m = re.search(r"^# (.+)$", stub, re.M)
        name = m.group(1).strip() if m else page.stem
        summaries = {}
        for pid in author_projects(stub):
            sp = ROOT / "wiki" / "summaries" / f"{pid}__REPORT.md"
            if sp.exists():
                text = C.parse_fm(sp.read_text(encoding="utf-8", errors="replace"))[1]
                summaries[pid] = text if configured() else text[:PER_SUMMARY_CHARS]
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
        todo.append((page, stub, name, summaries, digest))

    def write(item: tuple) -> str:
        page, _, name, summaries, _ = item

        def characterising(parts: list[str]) -> list[Issue]:
            return [
                Issue(
                    paragraph=i,
                    category="unsupported",
                    quote=hit[:300],
                    note="characterises the person; state what the project did or found",
                )
                for i, part in enumerate(parts)
                for hit in subjective_hits(part, name)
            ]

        pack = "SUMMARIES OF THIS AUTHOR'S PROJECTS:\n\n" + excerpts(
            {f"summaries/{pid}__REPORT": text for pid, text in summaries.items()}, 100_000
        )
        return derived_page(
            f"authors/{page.stem}",
            CONTRACT,
            f"Write the '{HEADING}' section for the wiki page of: {name}. This section is a "
            "factual record of what they worked on and what those projects reported.",
            pack,
            allowed="\n".join(summaries.values()),
            sources=src_texts,
            valid_ids=set(summaries),
            targets=C.wikilink_targets(ROOT),
            extra=characterising,
        )

    done = failed = 0
    for (page, stub, name, summaries, digest), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"authors/{page.name}", result)
            print(f"  [FAILED] authors/{page.stem}: {result}")
            continue
        body = re.sub(
            r"^## (?:Profile|Contributions)\s*\n.*?(?=\n## |\Z)", "", stub, flags=re.M | re.S
        )
        at = body.find("## Projects")
        at = at if at >= 0 else len(body)
        page.write_text(body[:at].rstrip() + "\n\n" + result + "\n\n" + body[at:], encoding="utf-8")
        state[page.name] = digest
        atomic_json(state_path, state)
        record_failure(f"authors/{page.name}", None)
        done += 1
        print(f"  wrote contributions for {name} ({len(summaries)} project(s))")
    prune_failures("authors/", {f"authors/{p.name}" for p in authors_dir.glob("*.md")})

    est = C._usage["in"] * C.PRICE_IN + C._usage["out"] * C.PRICE_OUT
    usage = (
        "usage recorded in the shared agentic ledger"
        if configured()
        else f"tokens in={C._usage['in']} out={C._usage['out']} (~${est:.2f} est)"
    )
    print(
        f"stages.authors: {done} section(s) written, {skipped} unchanged, {failed} failed; " + usage
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
