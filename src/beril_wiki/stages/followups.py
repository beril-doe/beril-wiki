#!/usr/bin/env python3
"""Follow-up needs: what someone must do to answer each open question.

Per research direction in wiki/directions: Claude reads the question, its hypothesis, how
to test it, what would support or refute it and the readiness note, and names what the
deciding test needs: existing (data already in BERDL can decide it, perhaps with a new
analysis), outside (data BERDL lacks but that exists or can be gathered without lab or
field work) or experiment (only a new lab or field measurement can decide). It also says
whether an analysis of BERDL data comes first in an experiment question, and whether the
records leave it unclear that the data can be found or joined. The direction's own
`approach` and `readiness` fields grade a first step or a hope and misfile both ways, so
every question is read. GPT then checks the answer against the question.

Output: state/followups.json, joined into question pages and cards at publish.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict

from beril_wiki.agentic.runtime import CandidateError, prompt
from beril_wiki.paths import ROOT
from beril_wiki.publish.cards import title_of
from beril_wiki.stages import cards, classify
from beril_wiki.stages.gists import statistical

STATE = Path("state/followups.json")
DIRECTIONS = Path("wiki/directions")
PROMPT_TAG = "followups@1"
MAX_REASON_WORDS = 30
MIN_REASON_WORDS = 4
SECTIONS = ("How to test it", "What would support or refute it")

Need = Literal["existing", "outside", "experiment"]


class Followup(BaseModel):
    model_config = ConfigDict(extra="forbid")
    need: Need
    first_step_existing: bool
    data_unclear: bool
    reason: str


PROMPT = prompt(
    PROMPT_TAG,
    "Decide what someone who takes up one OPEN QUESTION from a microbiology wiki must do to "
    "answer it. QUESTION gives its title, hypothesis, how to test it, what would support or "
    "refute it, the planned approach and a note on what data exist. BERDL is the shared "
    "database the projects queried; COLLECTIONS lists the BERDL collections the question "
    "names. The planned approach and the note are often wrong in both directions: decide "
    "from the test and from what would support or refute the hypothesis.\n"
    "Rules for 'need', by the test that decides the hypothesis:\n"
    "- existing: data already in BERDL can support or refute it; a new analysis may need "
    "to be written.\n"
    "- outside: deciding it needs data BERDL does not hold but that already exists or can "
    "be gathered without new lab or field work, such as public genomes, metagenomes, "
    "another study's measurements or registered samples not yet loaded.\n"
    "- experiment: only a new lab or field measurement can decide it.\n"
    "When a later experiment would only confirm what existing or outside data can already "
    "decide, choose existing or outside.\n"
    "Rules for 'first_step_existing': true only when need is experiment and an analysis of "
    "BERDL data comes first and narrows what the experiment tests; otherwise false.\n"
    "Rules for 'data_unclear': true when the note or the test leaves it unresolved whether "
    "the data needed can be found or joined; otherwise false.\n"
    "Rules for 'reason': one plain sentence of 4 to 30 words naming what decides the "
    "hypothesis and what it needs. No statistics, no statistical words.\n"
    'Return only JSON {"need": "...", "first_step_existing": false, "data_unclear": false, '
    '"reason": "..."}.\n',
)


def checker(_pack: dict) -> Callable[[str], Followup]:
    def parse(raw: str) -> Followup:
        reply = cards.parse_reply(raw, Followup)
        assert isinstance(reply, Followup)
        reason = reply.reason.strip()
        problems = []
        if reply.first_step_existing and reply.need != "experiment":
            problems.append("first_step_existing applies only when need is experiment")
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


def section(body: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def packs(root: Path) -> dict[str, dict]:
    out = {}
    for page in sorted((root / DIRECTIONS).glob("*.md")):
        fields, body = cards.read_page(page)
        out[page.stem] = {
            "QUESTION": {
                "title": title_of(body, page.stem),
                "hypothesis": fields.get("hypothesis", ""),
                **{s.lower().replace(" ", "_"): section(body, s) for s in SECTIONS},
                "approach": fields.get("approach", ""),
                "data_note": fields.get("readiness_basis", ""),
            },
            "COLLECTIONS": fields.get("collections") or [],
        }
    return out


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count answers; run nothing")
    items = packs(root)
    if args.parse_args(argv or []).status:
        return classify.status("followups", root / STATE, list(items))
    return classify.run("followups", root / STATE, items, PROMPT, PROMPT_TAG, checker)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
