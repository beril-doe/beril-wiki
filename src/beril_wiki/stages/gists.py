#!/usr/bin/env python3
"""Plain summaries: one or two sentences per finding, for readers who skip statistics.

Per finding in wiki/findings: Claude writes a gist from the committed finding page, its
report title, the report's other caveats and the other findings from the same report;
code rejects statistics, jargon, figures the claim, quote and caveat never state, banned
wording, a wrong null-result case and a repeat of a finding that is not earlier in the
report; GPT then checks faithfulness, including that the gist claims no more than the
measurement and its limits allow. A finding whose stored title holds a statistic or
jargon also gets a plain replacement title. A gist may mark its finding as repeating an
earlier one from the same report; publish then leaves it off the lists. A refusal or an
unconverged record fails only that finding and keeps its previous gist in state for
recovery; publish shows a failed finding's title only. The next run asks a failed
finding again with the objections that rejected it.

Output: state/gists.json, joined into finding pages and cards at publish.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Callable, Sequence
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

from beril_wiki.agentic.prose import PageFailure, failures_path, prune_failures, record_failure
from beril_wiki.agentic.runtime import (
    CandidateError,
    Runtime,
    atomic_json,
    digest,
    model_policy,
    prompt,
)
from beril_wiki.paths import ROOT
from beril_wiki.records import (
    FINDINGS,
    caveat_quote,
    finding_text,
    report_caveats,
    summary_title,
    title_of,
)
from beril_wiki.stages import cards
from beril_wiki.wording import GIST_BANNED, JARGON, statistical, words

STATE = Path("state/gists.json")
PROMPT_TAG = "gists@4"
MAX_GIST_WORDS = 45
MIN_GIST_WORDS = 6
MAX_TITLE_WORDS = 12
MAX_SENTENCES = 2
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
NULL_RESULT = "null result"
MAX_NUMBERS = 1
# The check allows one number past the prompt's limit: a reviewer asking for a specific
# figure and the code refusing a second one sent drafts back and forth until they failed.
CHECK_NUMBERS = 2
# A standalone number: "68.9%", "14,768", "-1.55"; not the digits in "16S", "K-12" or "GT2".
NUMBER = re.compile(r"(?<![\w.])(?<!\w-)-?\d[\d,]*(?:\.\d+)?%?(?![\w-])")
Case = Literal["measured absence", "inconclusive test", "missing data", "unperformed analysis", ""]


class Gist(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gist: str
    case: Case
    title: str = ""
    repeats: str = ""


PROMPT = prompt(
    PROMPT_TAG,
    "Write a plain-language summary of one FINDING from a microbial-biology research "
    "report, for a microbiologist who does not read statistics. The FINDING gives the "
    "claim, its quantities, the evidence quote, the caveat and the caveat quote. "
    "REPORT_CAVEATS lists the report's other caveats. SIBLINGS lists the other findings "
    "from the same report, and EARLIER names the ones listed before this finding.\n"
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
    "Claim no more than the measurement shows, even though the limits stay off the card: "
    "a prediction stays a prediction ('predicted pathways are less complete', not 'has "
    "lost'); a correlation is not a cause; a comparison with other genes or with an "
    "average is relative ('less costly to lose than other genes'), not an absolute effect "
    "('imposes a burden'); and say nothing about history, ancestry or mechanism that the "
    "finding did not test. When the caveat, the caveat quote or a REPORT_CAVEATS entry says "
    "the result is an artifact, circular, true by construction, from one study or not a "
    "refutation, state it only as strongly as those limits leave it. When a SIBLINGS "
    "finding states the opposite of this one, say in plain words that the report gives "
    "both results.\n"
    "Prefer plain biological words over method names: say 'growth models' rather than "
    "'flux-balance analysis' and 'gene-knockout screens' rather than 'TnSeq'; keep a "
    "method name only when the finding is about the method. Name no annotation system, "
    "database, statistical procedure or internal code (no SEED, COG, KEGG, GapMind, ICA, "
    "PERMANOVA, Procrustes, Mantel, 'Black Queen', 'preregistered', Tier A, notebook or "
    "hypothesis codes such as NB03 or H2, or genome-database names with a suffix such as "
    "Pseudomonas_E); say what they stand for. Use at most one number, and "
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
    "statistics, statistical words or jargon; give a plain replacement title of at most "
    "12 words with none of them and no new figures. When it is false, leave 'title' as an "
    "empty string.\n"
    "Rules for 'repeats': when an EARLIER finding reports the same result from the same "
    "analysis in other words, set 'repeats' to its id; otherwise leave it empty. A "
    "different result from the same analysis (another gene group, condition or direction) "
    "is not a repeat.\n"
    'Return only JSON {"gist": "...", "case": "...", "title": "...", "repeats": "..."}.\n',
)
# Sent only when this finding's last attempt failed, so the retry is a new question rather
# than a replay of the jobs that failed; the cache key and PROMPT stay as they were.
RETRY = (
    "\nLAST_ATTEMPT gives the objections that rejected the previous gist for this "
    "finding. Write one that meets them and keeps every rule above.\n"
)


def last_objections(step: str) -> str:
    """Why the last attempt at `step` failed, from the run's failure list."""
    path = failures_path()
    if path is None or not path.exists():
        return ""
    entry = json.loads(path.read_text(encoding="utf-8")).get(step) or {}
    notes = [i["note"].split("unsupported: ", 1)[-1] for i in entry.get("issues", [])]
    return " ".join(notes)[:1500]


def plain_title(title: str) -> bool:
    return not statistical(title) and not JARGON.search(title)


def checker(finding: dict, title: str, earlier: Sequence[str] = ()) -> Callable[[str], Gist]:
    """Parse and code-check a reply; every problem goes back to the writer.

    `earlier` names the findings of the same report a gist may repeat: only those listed
    before this one, so two findings never mark each other."""
    pool = " ".join(str(finding.get(k, "")) for k in ("claim", "quote", "caveat", "caveat_quote"))
    needs_title = not plain_title(title)
    is_null = finding.get("result") == NULL_RESULT

    def text_problems(label: str, text: str) -> list[str]:
        out = []
        if statistical(text):
            out.append(f"{label} contains a statistic or statistical wording; say it in words")
        if extra := cards.new_figures(text, pool):
            out.append(f"{label} uses figures the claim, quote and caveat never state: {extra}")
        if jargon := JARGON.search(text):
            out.append(f"{label} uses '{jargon.group(0)}'; say what it stands for in plain words")
        if banned := GIST_BANNED.search(text):
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
        if (count := len(NUMBER.findall(gist))) > CHECK_NUMBERS:
            problems.append(f"gist uses {count} numbers; keep at most {MAX_NUMBERS}")
        if is_null and not reply.case:
            problems.append("a null result needs a case")
        if not is_null and reply.case:
            problems.append("case applies to null results only; leave it empty")
        new_title = reply.title.strip()
        if needs_title:
            if not new_title:
                problems.append(
                    "the stored title contains statistics or jargon; give a plain title"
                )
            else:
                if words(new_title) > MAX_TITLE_WORDS:
                    problems.append(
                        f"title has {words(new_title)} words; use at most {MAX_TITLE_WORDS}"
                    )
                problems += text_problems("title", new_title)
        elif new_title:
            problems.append("the stored title is plain; leave title empty")
        repeats = reply.repeats.strip()
        if repeats and repeats not in earlier:
            problems.append(
                f"repeats names {repeats!r}, which is not an EARLIER finding of this report"
            )
        if problems:
            raise CandidateError("; ".join(problems))
        return reply.model_copy(update={"gist": gist, "title": new_title, "repeats": repeats})

    return parse


def status(root: Path = ROOT) -> int:
    """Print accepted, failed and pending counts; touches neither the runtime nor state."""
    state = cards.load_state(root / STATE)
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
    state = cards.load_state(state_path)
    config = cards.runtime().config
    policy = cards.policy(config, ("cards", "review"))
    writer = model_policy(config)["cards"]
    findings: dict[str, tuple[dict, str, str]] = {}
    caveats: dict[str, list[str]] = {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        finding = finding_text(fields, body) | {"caveat_quote": caveat_quote(body)}
        heading = title_of(body, "")
        findings[page.stem] = (finding, heading, summary_title(root, finding["report"]))
        caveats[page.stem] = report_caveats(body)
    by_report: dict[str, list[str]] = {}
    for fid, (finding, _, _) in findings.items():
        by_report.setdefault(finding["report"], []).append(fid)

    def pack_of(fid: str) -> dict:
        finding, heading, report = findings[fid]
        siblings = sorted(f for f in by_report[finding["report"]] if f != fid)
        return {
            "FINDING": finding | {"title": heading, "report_title": report},
            "TITLE_NEEDS_PLAIN": not plain_title(heading),
            "REPORT_CAVEATS": caveats[fid],
            "SIBLINGS": [
                {"id": f, "title": findings[f][1], "claim": findings[f][0]["claim"]}
                for f in siblings
            ],
            "EARLIER": [f for f in siblings if f < fid],
        }

    def passes(fid: str, prev: dict, pack: dict) -> bool:
        finding, heading, _ = findings[fid]
        stored = {k: prev.get(k, "") for k in ("gist", "case", "title", "repeats")}
        try:
            checker(finding, heading, pack["EARLIER"])(json.dumps(stored))
        except CandidateError:
            return False
        return True

    todo = []
    for fid in findings:
        # A sibling's change can make this gist a repeat or contradict it, so it reruns.
        pack = pack_of(fid)
        key = digest([pack, PROMPT_TAG, policy])
        prev = state.get(fid, {})
        # A saved gist stays while its input is unchanged and today's checks accept it,
        # so a tightened rule re-asks only the gists it now rejects.
        if prev.get("input") == key and not prev.get("failed") and passes(fid, prev, pack):
            continue
        todo.append((fid, pack, key, last_objections(f"gists/{fid}") if prev.get("failed") else ""))

    def write(item: tuple, agent: Runtime) -> dict:
        fid, pack, _, objections = item
        finding, heading, _ = findings[fid]
        sent = pack | {"LAST_ATTEMPT": objections} if objections else pack
        content = PROMPT + json.dumps(sent, ensure_ascii=False) + (RETRY if objections else "")
        reply = cards.reviewed(
            [{"role": "user", "content": content}],
            f"gists/{fid}",
            checker(finding, heading, pack["EARLIER"]),
            agent=agent,
        )
        return {
            "gist": reply.gist,
            "case": reply.case,
            "title": reply.title,
            "repeats": reply.repeats,
        }

    done = failed = 0
    for (fid, _, key, _), result in cards.each_job(todo, lambda item: f"gists/{item[0]}", write):
        if isinstance(result, PageFailure):
            failed += 1
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
    return cards.exit_code(failed)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
