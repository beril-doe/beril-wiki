#!/usr/bin/env python3
"""Follow-up needs: what someone must do to answer each open question.

Per research direction in wiki/directions: Claude reads the question, its hypothesis, how
to test it, what would support or refute it and the readiness note, with a directory of the
lakehouse catalog (state/lakehouse/) and the catalog tables matched to the question. It names
what the deciding test needs: existing (tables the catalog lists can decide it, perhaps with
a new analysis; the reply names them), outside (data not found in the catalog's tenants that
exists elsewhere or can be gathered without lab or field work) or experiment (only a new lab
or field measurement can decide it). It also says whether an analysis of lakehouse data comes
first in an experiment question, and whether the records leave it unclear that the data can
be found or joined. The direction's own `approach` and `readiness` fields grade a first step
or a hope and misfile both ways, so every question is read. Code checks every named table
against the catalog, then GPT checks the answer against the question. `--status` compares the
saved answers with today's packs and calls no model.

Output: state/followups.json, joined into question pages and cards at publish.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from beril_wiki import lakehouse
from beril_wiki.agentic.runtime import CandidateError, prompt
from beril_wiki.lakehouse import Catalog, absence_claims
from beril_wiki.paths import ROOT
from beril_wiki.records import title_of
from beril_wiki.stages import cards, classify
from beril_wiki.wording import statistical

STATE = Path("state/followups.json")
DIRECTIONS = Path("wiki/directions")
PROMPT_TAG = "followups@2"
MAX_FOLLOWUP_TABLES = 12
MATCHED_TABLES = 20
BERDL = re.compile(r"\bBERDL\b", re.I)
MAX_REASON_WORDS = 30
MIN_REASON_WORDS = 4
SECTIONS = ("How to test it", "What would support or refute it")
_SECTION_KEYS = tuple(x.lower().replace(" ", "_") for x in SECTIONS)

Need = Literal["existing", "outside", "experiment"]


class Followup(BaseModel):
    model_config = ConfigDict(extra="forbid")
    need: Need
    first_step_existing: bool
    data_unclear: bool
    reason: str
    tables: list[str] = Field(default_factory=list, max_length=MAX_FOLLOWUP_TABLES)


PROMPT = prompt(
    PROMPT_TAG,
    "Decide what someone who takes up one OPEN QUESTION from a microbiology wiki must do to "
    "answer it. QUESTION gives its title, hypothesis, how to test it, what would support or "
    "refute it, the planned approach and a note on what data exist. The KBase Data Lakehouse "
    "is the shared database the projects queried. DIRECTION_TABLES lists the catalog tables "
    "the question's direction names. DATABASES is a directory of the lakehouse catalog: each "
    "database it covers with its first table names. TABLES lists catalog tables matched to "
    "this question, with their columns and sample values. The catalog covers only some of the "
    "lakehouse: a value, column or table missing from DATABASES or TABLES is unknown, not "
    "absent, and a table marked columns_truncated, complete false or basis sample holds more "
    "than is shown. Never claim the lakehouse lacks data; say the catalog did not show it. "
    "The planned approach and the note are often wrong in both directions: decide from the "
    "test and from what would support or refute the hypothesis.\n"
    "Rules for 'need', by the test that decides the hypothesis:\n"
    "- existing: tables the catalog lists can support or refute it; a new analysis may need "
    "to be written. Name those tables in 'tables'.\n"
    "- outside: the data was not found in the catalog's tenants and already exists elsewhere "
    "or can be gathered without new lab or field work, such as public genomes, metagenomes, "
    "another study's measurements or registered samples not yet loaded.\n"
    "- experiment: only a new lab or field measurement can decide it.\n"
    "Choose outside or experiment from what the test needs, never because a table is missing "
    "from DATABASES or TABLES. When a later experiment would only confirm what existing or "
    "outside data can already decide, choose existing or outside.\n"
    "Rules for 'first_step_existing': true only when need is experiment and an analysis of "
    "lakehouse data comes first and narrows what the experiment tests; otherwise false. When "
    "it is true, 'tables' names the tables that first analysis reads.\n"
    "Rules for 'data_unclear': true when the note or the test leaves it unresolved whether "
    "the data needed can be found or joined; otherwise false.\n"
    f"Rules for 'tables': at most {MAX_FOLLOWUP_TABLES} tables, each written "
    "<database>.<table>, only tables that exist in the catalog; empty when need is outside, "
    "or experiment with no analysis first.\n"
    "Rules for 'reason': one plain sentence of 4 to 30 words naming what decides the "
    "hypothesis and what it needs. Write the KBase Data Lakehouse or the lakehouse, never "
    "BERDL. No statistics, no statistical words.\n"
    'Return only JSON {"need": "...", "first_step_existing": false, "data_unclear": false, '
    '"reason": "...", "tables": ["<database>.<table>"]}.\n',
)


def _is_table(cat: Catalog, name: str) -> bool:
    row = cat.exists(name)
    return row is not None and "table" in row


def checker(pack: dict, cat: Catalog) -> Callable[[str], Followup]:
    """Return the code check for one followup reply.

    Parameters
    ----------
    pack : dict
        The question's pack (unused: names are checked against the whole catalog, so a
        table the match left out still counts).
    cat : Catalog
        The lakehouse catalog.

    Returns
    -------
    Callable[[str], Followup]
        A parser that raises ``CandidateError`` listing every problem, else returns the
        reply with its reason stripped and its tables in canonical dotted form.
    """

    def parse(raw: str) -> Followup:
        reply = cards.parse_reply(raw, Followup)
        assert isinstance(reply, Followup)
        reason = reply.reason.strip()
        problems = []
        if reply.first_step_existing and reply.need != "experiment":
            problems.append("first_step_existing applies only when need is experiment")
        if bad := [t for t in reply.tables if not _is_table(cat, t)]:
            problems.append(f"tables {bad} are not in the lakehouse catalog")
        if reply.need == "existing" and not reply.tables:
            problems.append("need existing names no table; name the tables that decide it")
        if reply.need == "experiment" and reply.first_step_existing and not reply.tables:
            problems.append(
                "first_step_existing names no table; name the tables the first analysis reads"
            )
        if not MIN_REASON_WORDS <= len(reason.split()) <= MAX_REASON_WORDS:
            problems.append(
                f"reason has {len(reason.split())} words; use {MIN_REASON_WORDS} to "
                f"{MAX_REASON_WORDS}"
            )
        if statistical(reason):
            problems.append("reason contains a statistic or statistical wording; say it in words")
        if BERDL.search(reason):
            problems.append("reason names BERDL; write the KBase Data Lakehouse")
        if hits := absence_claims(reason):
            problems.append(
                f"reason says the lakehouse lacks data ({hits}); say the catalog did not show it"
            )
        if problems:
            raise CandidateError("; ".join(problems))
        names = [cat.canonical(t) for t in reply.tables]
        tables = list(dict.fromkeys(n for n in names if n))
        return reply.model_copy(update={"reason": reason, "tables": tables})

    return parse


def section(body: str, heading: str) -> str:
    m = re.search(rf"^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)", body, re.M | re.S)
    return re.sub(r"\s+", " ", m.group(1)).strip() if m else ""


def packs(root: Path, cat: Catalog) -> dict[str, dict]:
    """Return each direction's pack: its question, its tables, the directory and matched tables.

    Parameters
    ----------
    root : Path
        The checkout.
    cat : Catalog
        The lakehouse catalog.

    Returns
    -------
    dict[str, dict]
        Direction slug to the JSON pack sent with the prompt.
    """
    out = {}
    for page in sorted((root / DIRECTIONS).glob("*.md")):
        fields, body = cards.read_page(page)
        question = {
            "title": title_of(body, page.stem),
            "hypothesis": fields.get("hypothesis", ""),
            **{s.lower().replace(" ", "_"): section(body, s) for s in SECTIONS},
            "approach": fields.get("approach", ""),
            "data_note": fields.get("readiness_basis", ""),
        }
        text = " ".join(
            [question["title"], question["hypothesis"], *(question[k] for k in _SECTION_KEYS)]
        )
        named = fields.get("tables") or []
        out[page.stem] = {
            "QUESTION": question,
            "DIRECTION_TABLES": named,
            "DATABASES": cat.directory(),
            "TABLES": cat.matched(text, fields.get("projects") or [], MATCHED_TABLES, tables=named),
        }
    return out


def main(root: Path = ROOT, argv: list[str] | None = None) -> int:
    args = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    args.add_argument("--status", action="store_true", help="count answers; run nothing")
    status = args.parse_args(argv or []).status
    cat = lakehouse.load(root)
    if cat.empty:
        print("stages.followups: no lakehouse catalog; run stages.lakehouse first", file=sys.stderr)
        return 1
    items = packs(root, cat)

    def parse(pack: dict) -> Callable[[str], Followup]:
        return checker(pack, cat)

    if status:
        policy = cards.policy(classify.status_config(root), ("labels", "card_review"))
        return classify.status("followups", root / STATE, items, PROMPT_TAG, parse, policy)
    return classify.run("followups", root / STATE, items, PROMPT, PROMPT_TAG, parse)


if __name__ == "__main__":
    sys.exit(main(argv=sys.argv[1:]))
