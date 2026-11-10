#!/usr/bin/env python3
"""Result types: what kind of result each listed finding is, for the Results map's marks.

Per finding that publish would list (an accepted plain summary that repeats nothing, and,
for a null result, a case that measured something): Claude reads the claim, the evidence
quote, the caveat and the plain summary and names the type: positive (a pattern,
difference or link was found), negative (a difference or link was tested and not found),
inconclusive, data (it describes what a dataset holds or lacks rather than biology),
bookkeeping (it fixes the project's own list or rule) or untested (an explanation the
project never tested). The extraction tag (observation, inference, null result,
correction) misfiles both ways, so every finding is read. GPT then checks the type against
the evidence. Publish unlists bookkeeping and untested findings and keeps their pages.

Output: state/outcomes.json, joined into finding pages and cards at publish.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

from beril_wiki.agentic.runtime import CandidateError, prompt
from beril_wiki.paths import ROOT
from beril_wiki.publish.cards import SHOWN_CASES, title_of
from beril_wiki.stages import cards, classify
from beril_wiki.stages.gists import caveat_quote, statistical
from beril_wiki.stages.novelty import finding_text

STATE = Path("state/outcomes.json")
GISTS = Path("state/gists.json")
FINDINGS = Path("wiki/findings")
PROMPT_TAG = "outcomes@1"
MAX_REASON_WORDS = 30
MIN_REASON_WORDS = 4

Type = Literal["positive", "negative", "inconclusive", "data", "bookkeeping", "untested"]


class Outcome(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: Type
    reason: str


PROMPT = prompt(
    PROMPT_TAG,
    "Say what kind of result one FINDING from a microbial-biology research report is, for "
    "a scientist who browses results by kind. FINDING gives the title, the claim, the "
    "evidence quote, the caveat and its quote, the extraction tag (observation, inference, "
    "null result or correction) and the plain summary. The tag is often wrong in both "
    "directions: decide from what the evidence quote shows, not from the tag.\n"
    "Types:\n"
    "- positive: the analysis found a pattern, difference, trend, association or link, "
    "including an effect opposite to the one expected and a prediction that worked.\n"
    "- negative: the analysis tested for a difference, link or effect and found none, or a "
    "model or prediction failed to work.\n"
    "- inconclusive: the analysis ran but could not decide between the outcomes it tested.\n"
    "- data: the finding describes what a dataset, database, catalog or annotation holds or "
    "lacks (coverage, missing entries, naming, provenance), not a biological result.\n"
    "- bookkeeping: the finding only fixes the project's own error in a list, marker set, "
    "compound list or grouping rule, with no biological result of its own.\n"
    "- untested: the finding proposes an explanation or a rerun that the project did not "
    "test.\n"
    "A correction that also reports a biological result, such as a reversed association or "
    "an effect that shrank once a confounder was removed, is positive or negative by that "
    "result. A finding that reports both a missing effect and a pattern found instead is "
    "positive.\n"
    "Rules for 'reason': one plain sentence of 4 to 30 words saying what the evidence shows "
    "that decides the type. No statistics, no statistical words.\n"
    'Return only JSON {"type": "...", "reason": "..."}.\n',
)


def checker(_pack: dict) -> Callable[[str], Outcome]:
    def parse(raw: str) -> Outcome:
        reply = cards.parse_reply(raw, Outcome)
        assert isinstance(reply, Outcome)
        reason = reply.reason.strip()
        problems = []
        if not MIN_REASON_WORDS <= len(reason.split()) <= MAX_REASON_WORDS:
            problems.append(
                f"reason has {len(reason.split())} words; use {MIN_REASON_WORDS} to "
                f"{MAX_REASON_WORDS}"
            )
        if statistical(reason):
            problems.append("reason contains a statistic or statistical wording; say it in words")
        if problems:
            raise CandidateError("; ".join(problems))
        return reply.model_copy(update={"reason": reason})

    return parse


def listed(gist: dict | None, result: str) -> bool:
    """publish.cards.eligible on the state alone: what the Results page would list."""
    if not gist or gist.get("failed") or not gist.get("gist") or gist.get("repeats"):
        return False
    return result != "null result" or gist.get("case") in SHOWN_CASES


def packs(root: Path) -> dict[str, dict]:
    gists = classify.load(root / GISTS)
    out = {}
    for page in sorted((root / FINDINGS).glob("*.md")):
        fields, body = cards.read_page(page)
        gist = gists.get(page.stem)
        if not listed(gist, fields.get("result", "")):
            continue
        assert gist is not None
        finding = finding_text(fields, body) | {"caveat_quote": caveat_quote(body)}
        out[page.stem] = {
            "FINDING": {
                "title": gist.get("title") or title_of(body, page.stem),
                "claim": finding["claim"],
                "quote": finding.get("quote", ""),
                "caveat": finding.get("caveat", ""),
                "caveat_quote": finding["caveat_quote"],
                "tag": fields.get("result", ""),
                "summary": gist["gist"],
            }
        }
    return out


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count types; run nothing")
    items = packs(root)
    if args.parse_args(argv or []).status:
        return classify.status("outcomes", root / STATE, list(items))
    return classify.run("outcomes", root / STATE, items, PROMPT, PROMPT_TAG, checker)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
