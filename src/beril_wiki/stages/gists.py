#!/usr/bin/env python3
"""Plain summaries: one or two sentences per finding, for readers who skip statistics.

Per finding in wiki/findings: Claude writes a gist from the committed finding page and
its report title; code rejects statistics, figures the claim, quote and caveat never
state, banned wording and a wrong null-result case; GPT then checks faithfulness. A
finding whose stored title is itself a statistic also gets a plain replacement title.
A refusal or an unconverged record fails only that finding and keeps its previous gist
in state for recovery; publish shows a failed finding's title only.
A gist accepted under an earlier prompt in LEGACY_TAGS stays current while its finding is
unchanged and it passes this prompt's code checks; the rest are written again.

Output: state/gists.json, joined into finding pages and cards at publish.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

from beril_wiki.agentic.prose import (
    PageFailure,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, model_policy, prompt
from beril_wiki.paths import ROOT
from beril_wiki.publish.cards import STATS, title_of
from beril_wiki.stages import cards
from beril_wiki.stages.links import STAT_WORDS
from beril_wiki.stages.novelty import finding_text

STATE = Path("state/gists.json")
FINDINGS = Path("wiki/findings")
PROMPT_TAG = "gists@3"
# gists@3 changed only rules that failed gists broke; gists that passed gists@2 are kept.
LEGACY_TAGS = ("gists@2",)
MAX_GIST_WORDS = 45
MIN_GIST_WORDS = 6
MAX_TITLE_WORDS = 12
MAX_SENTENCES = 2
BANNED = re.compile(r"\b(novel|first|breakthrough|confirms|caveats?|limitations?|however)\b", re.I)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
NULL_RESULT = "null result"
MAX_NUMBERS = 1
# A standalone number: "68.9%", "14,768", "-1.55"; not the digits in "16S", "K-12" or "GT2".
NUMBER = re.compile(r"(?<![\w.])(?<!\w-)-?\d[\d,]*(?:\.\d+)?%?(?![\w-])")
MULTIPLE_TESTING = re.compile(r"\bmultiple[- ]testing\b", re.I)


def statistical(text: str) -> bool:
    """A statistic or statistical wording, such as 'significant' or 'multiple-testing'."""
    return any(p.search(text) for p in (STATS, STAT_WORDS, MULTIPLE_TESTING))


Case = Literal["measured absence", "inconclusive test", "missing data", "unperformed analysis", ""]


class Gist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gist: str
    case: Case
    title: str = ""


PROMPT = prompt(
    PROMPT_TAG,
    "Write a plain-language summary of one FINDING from a microbial-biology research "
    "report, for a microbiologist who does not read statistics. The FINDING gives the "
    "claim, its quantities, the evidence quote, the caveat and the caveat quote.\n"
    "Rules for 'gist': one or two sentences, at most 45 words. Lead with what was seen, "
    "in biological terms, and why a microbiologist would find it interesting. Name the "
    "organisms or the environment when the FINDING states them; when it states neither, "
    "say what kind of genes, genomes or samples it covers, and never invent an organism "
    "or an environment. Write for a scientist who should want to read on.\n"
    "Do not state caveats, limitations or 'however' clauses, and do not repeat or "
    "paraphrase the caveat: the finding page shows limits separately under 'Limits', so "
    "leaving them out of the gist is intended and is not an omission. Qualify only with "
    "the hedge words the claim itself warrants, such as 'suggests', 'in these genomes' or "
    "'in these samples'.\n"
    "Prefer plain biological words over method names: say 'growth models' rather than "
    "'flux-balance analysis' and 'gene-knockout screens' rather than 'TnSeq'; keep a "
    "method name only when the finding is about the method. Use at most one number, and "
    "only when it conveys a plain magnitude, such as a percent or a count of genes; never "
    "list figures; '14,768 genes' and '68.9%' are two numbers. Use no statistics: no "
    "p-values, correlation coefficients, AUC, FDR, test names or powers of ten, and no "
    "statistical words such as 'significant', 'statistically', 'effect size', 'power' or "
    "'multiple-testing correction'; say what was seen instead. Use no figure that the "
    "claim, the evidence quote or the caveat does not state, and copy a figure exactly "
    "as they give it, with its percent sign or decimals. Never write 'novel', 'first', "
    "'breakthrough', 'confirms', 'caveat', 'limitation' or 'however'. Make no claim about people.\n"
    "Rules for 'case': when the FINDING's result is 'null result', set 'case' to the one "
    "that fits the quote: 'measured absence' (the analysis ran and found nothing), "
    "'inconclusive test' (it ran but could not settle the question), 'missing data' (the "
    "data needed were not available) or 'unperformed analysis' (the analysis was not "
    "run). State that case in the gist in words, and write 'no detectable' only for a "
    "measured absence. For every other result set 'case' to an empty string.\n"
    "Rules for 'title': when TITLE_NEEDS_PLAIN is true, the stored title contains "
    "statistics or statistical words; give a plain replacement title of at most 12 words "
    "with neither and no new figures. When it is false, leave 'title' as an empty string.\n"
    'Return only JSON {"gist": "...", "case": "...", "title": "..."}.\n',
)


def words(text: str) -> int:
    return len(text.split())


def caveat_quote(body: str) -> str:
    """The blockquote lines under `## Caveat`, source tags removed."""
    section = re.search(r"^## Caveat\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    if not section:
        return ""
    quoted = [
        re.sub(r"\s*\[src: [^\]]+\]", "", line[1:]).strip()
        for line in section.group(1).splitlines()
        if line.startswith(">")
    ]
    return " ".join(q for q in quoted if q)


def report_title(root: Path, sid: str) -> str:
    """The report's H1, from its summary page, else the report id."""
    for name in (f"{sid}__REPORT.md", f"{sid}.md"):
        path = root / "wiki" / "summaries" / name
        if path.exists():
            return title_of(path.read_text(encoding="utf-8", errors="replace"), sid)
    return sid


def checker(finding: dict, title: str, count_numbers: bool = True) -> Callable[[str], Gist]:
    """Parse and code-check a reply; every problem goes back to the writer.

    `count_numbers=False` skips the number count, which gists@2 left to the reviewer, so
    a kept gists@2 gist is rewritten only for statistics, not for a second figure."""
    pool = " ".join(str(finding.get(k, "")) for k in ("claim", "quote", "caveat", "caveat_quote"))
    needs_title = statistical(title)
    is_null = finding.get("result") == NULL_RESULT

    def text_problems(label: str, text: str) -> list[str]:
        out = []
        if statistical(text):
            out.append(f"{label} contains a statistic or statistical wording; say it in words")
        if extra := cards.new_figures(text, pool):
            out.append(f"{label} uses figures the claim, quote and caveat never state: {extra}")
        if banned := BANNED.search(text):
            out.append(
                f"{label} uses '{banned.group(0)}'; the page shows limits separately, "
                "so leave caveats out"
            )
        return out

    def parse(raw: str) -> Gist:
        reply = cards.parse_reply(raw, Gist)
        assert isinstance(reply, Gist)
        problems = []
        gist = reply.gist.strip()
        if not MIN_GIST_WORDS <= words(gist) <= MAX_GIST_WORDS:
            problems.append(
                f"gist has {words(gist)} words; use {MIN_GIST_WORDS} to {MAX_GIST_WORDS}"
            )
        if len(SENTENCE_END.split(gist)) > MAX_SENTENCES:
            problems.append(f"gist must be at most {MAX_SENTENCES} sentences")
        problems += text_problems("gist", gist)
        if count_numbers and (count := len(NUMBER.findall(gist))) > MAX_NUMBERS:
            problems.append(f"gist uses {count} numbers; keep at most {MAX_NUMBERS}")
        if is_null and not reply.case:
            problems.append("a null result needs a case")
        if not is_null and reply.case:
            problems.append("case applies to null results only; leave it empty")
        new_title = reply.title.strip()
        if needs_title:
            if not new_title:
                problems.append("the stored title contains statistics; give a plain title")
            else:
                if words(new_title) > MAX_TITLE_WORDS:
                    problems.append(
                        f"title has {words(new_title)} words; use at most {MAX_TITLE_WORDS}"
                    )
                problems += text_problems("title", new_title)
        elif new_title:
            problems.append("the stored title is plain; leave title empty")
        if problems:
            raise CandidateError("; ".join(problems))
        return reply.model_copy(update={"gist": gist, "title": new_title})

    return parse


def status(root: Path = ROOT) -> int:
    """Print accepted, failed and pending counts; touches neither the runtime nor state."""
    path = root / STATE
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    ids = [page.stem for page in (root / FINDINGS).glob("*.md")]
    entries = [state.get(fid) for fid in ids]
    failed = sum(1 for e in entries if e and e.get("failed"))
    accepted = sum(1 for e in entries if e and not e.get("failed"))
    pending = sum(1 for e in entries if not e)
    print(f"gists: {accepted} accepted, {failed} failed, {pending} pending, {len(ids)} total")
    return 0


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count gists; run nothing")
    if args.parse_args(argv or []).status:
        return status(root)
    if not cards.require_runtime("gists"):
        return 0
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    config = cards.runtime().config
    policy = cards.policy(config, ("cards", "review"))
    writer = model_policy(config)["cards"]
    findings: dict[str, tuple[dict, str, str]] = {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        finding = finding_text(fields, body) | {"caveat_quote": caveat_quote(body)}
        heading = title_of(body, "")
        findings[page.stem] = (finding, heading, report_title(root, finding["report"]))

    def kept(prev: dict, finding: dict, heading: str, report: str) -> bool:
        legacy = {digest([finding, heading, report, tag, policy]) for tag in LEGACY_TAGS}
        if prev.get("failed") or prev.get("input") not in legacy:
            return False
        stored = {k: prev.get(k, "") for k in ("gist", "case", "title")}
        try:
            checker(finding, heading, count_numbers=False)(json.dumps(stored))
        except CandidateError:
            return False
        return True

    todo = []
    for fid, (finding, heading, report) in findings.items():
        key = digest([finding, heading, report, PROMPT_TAG, policy])
        prev = state.get(fid, {})
        if prev.get("input") == key and not prev.get("failed"):
            continue
        if kept(prev, finding, heading, report):
            continue
        todo.append((fid, finding, heading, report, key))

    def write(item: tuple) -> dict:
        fid, finding, heading, report, _ = item
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        pack = json.dumps(
            {
                "FINDING": finding | {"title": heading, "report_title": report},
                "TITLE_NEEDS_PLAIN": statistical(heading),
            },
            ensure_ascii=False,
        )
        try:
            reply = cards.reviewed(
                [{"role": "user", "content": PROMPT + pack}],
                f"gists/{fid}",
                checker(finding, heading),
                agent=mine,
            )
        except CandidateError as exc:
            raise cards.failure(f"gists/{fid}", exc, mine) from exc
        return {"gist": reply.gist, "case": reply.case, "title": reply.title}

    done = failed = 0
    for (fid, *_, key), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"gists/{fid}", result)
            print(f"  [FAILED] gists/{fid}: {result}")
            state[fid] = (state.get(fid) or {}) | {"failed": True}
            continue
        state[fid] = {"input": key, **result, "model": writer}
        # Saved per gist, so a run stopped by its budget keeps what it finished.
        atomic_json(state_path, dict(sorted(state.items())))
        record_failure(f"gists/{fid}", None)
        done += 1
    for fid in [f for f in state if f not in findings]:
        state.pop(fid)
    atomic_json(state_path, dict(sorted(state.items())))
    prune_failures("gists/", {f"gists/{fid}" for fid in findings})
    print(f"gists: {done} written, {len(findings) - len(todo)} current, {failed} failed")
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
