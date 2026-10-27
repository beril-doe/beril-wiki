#!/usr/bin/env python3
"""Headline findings: at most six per report, each a record a reader can act on.

For every report in contract/cards.yaml, the model chooses up to 4 observations or
inferences and up to 2 null results or corrections from the report's accepted
evidence records, and restates each with its key figures and the caveat that
travels with it. Code checks every figure against the record's verbatim quote
before the reviewer reads the reply. Each headline becomes wiki/findings/<id>.md;
the literature label is the novelty stage's and joins the page at publish.

Hash-cached per report in state/headlines.json. A report whose evidence snapshot
does not match its current text is skipped, and its previous pages stay.

    uv run python -m beril_wiki.agentic run ...   (runs as a curator stage)
"""

from __future__ import annotations

import datetime
import json
import re
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from beril_wiki.agentic.prose import (
    PLATFORM,
    PageFailure,
    parallel,
    prune_failures,
    record_failure,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import CandidateError, atomic_json, digest, file_hash, prompt
from beril_wiki.paths import ROOT
from beril_wiki.stages import cards

OUT = Path("wiki/findings")
STATE = Path("state/headlines.json")
MAX_FINDINGS = 4  # observations and inferences per report
MAX_NULLS = 2  # null results and corrections per report
OTHER_CAVEATS = 5
TITLE_WORDS = 12
# Bump when render() changes: pages re-render from the cached replies at no cost.
RENDER = "finding-page@4"
Result = Literal["observation", "inference", "null result", "correction"]


class Quantity(BaseModel):
    model_config = ConfigDict(extra="forbid")
    value: str = Field(min_length=1, max_length=80)
    what: str = Field(min_length=1, max_length=300)
    unit: str = Field(default="", max_length=60)
    denominator: str = Field(default="", max_length=300)
    scope: str = Field(default="", max_length=300)


class Headline(BaseModel):
    model_config = ConfigDict(extra="forbid")
    evidence: str
    result: Result
    title: str = Field(min_length=3, max_length=120)
    claim: str = Field(min_length=10, max_length=700)
    quantities: list[Quantity] = Field(max_length=4)
    caveat_evidence: str
    caveat: str = Field(min_length=10, max_length=500)


class Reply(BaseModel):
    model_config = ConfigDict(extra="forbid")
    headlines: list[Headline]


PROMPT = prompt(
    "headlines@1",
    "Choose the headline findings of one research report, for a scientist deciding what "
    "to investigate next. From FINDINGS choose at most "
    f"{MAX_FINDINGS} observations or inferences that most change what is known: prefer a "
    "measured effect, a large scope, or a direction a reader would not assume. Choose at "
    f"most {MAX_NULLS} null results or corrections that close an avenue or correct an "
    "earlier claim. A null result must be a record of kind null and is reported as null. "
    "A correction is a finding that, by its own quote, revises an earlier result or an "
    "assumption. Prefer fewer headlines to weak ones; restating method or data inventory "
    "is not a finding.\n"
    "For each headline give: evidence (the record id); result (observation, inference, "
    "null result or correction; an inference is a conclusion the report draws rather than "
    "measures); title (at most 12 words, no figures); claim (one sentence restating the "
    "record, qualified exactly as its quote qualifies it: organism, dataset, threshold, "
    "denominator, and 'suggests' where the report infers; every figure copied exactly from "
    "the quote); quantities (up to 4 key figures, each with value copied exactly from the "
    "quote, what it measures, and unit, denominator and scope where the quote gives them, "
    "else empty strings); caveat_evidence (the id of the CAVEATS record that most limits "
    "this claim) and caveat (one sentence restating it, figures copied exactly). "
    "Never add a confidence label or a claim about a person. " + PLATFORM + "\n"
    f"Return only JSON matching {json.dumps(Reply.model_json_schema())}.\n",
)


def pack(sid: str, title: str, records: list[dict]) -> dict:
    keep = lambda kinds: [  # noqa: E731
        {"id": r["id"], "kind": r["kind"], "claim": r["claim"], "quote": r["quote"]}
        for r in records
        if r["kind"] in kinds
    ]
    return {
        "report": sid,
        "title": title,
        "FINDINGS": keep(("finding", "null")),
        "CAVEATS": keep(("caveat",)),
    }


def checker(records: list[dict]) -> Callable[[str], Reply]:
    """Code-side checks on a reply; each failure goes back to the model to correct."""
    by_id = {r["id"]: r for r in records}

    def parse(raw: str) -> Reply:
        reply = cards.parse_reply(raw, Reply)
        assert isinstance(reply, Reply)
        problems: list[str] = []
        seen: set[str] = set()
        for n, h in enumerate(reply.headlines):
            record = by_id.get(h.evidence)
            if record is None or record["kind"] not in ("finding", "null"):
                problems.append(f"headline {n}: evidence {h.evidence!r} is not a FINDINGS id")
                continue
            if h.evidence in seen:
                problems.append(f"headline {n}: evidence {h.evidence!r} is used twice")
            seen.add(h.evidence)
            if (record["kind"] == "null") != (h.result == "null result"):
                problems.append(
                    f"headline {n}: result 'null result' must match a record of kind null"
                )
            quote = record["quote"]
            if bad := cards.new_figures(h.claim, quote):
                problems.append(f"headline {n}: claim figures {bad} are not in the quote")
            if bad := cards.new_figures(h.title, ""):
                problems.append(f"headline {n}: the title carries figures {bad}")
            if len(h.title.split()) > TITLE_WORDS:
                problems.append(f"headline {n}: the title has more than {TITLE_WORDS} words")
            for q in h.quantities:
                text = " ".join((q.value, q.what, q.unit, q.denominator, q.scope))
                if bad := cards.new_figures(text, quote):
                    problems.append(f"headline {n}: quantity figures {bad} are not in the quote")
                elif not cards.in_quote(q.value, quote):
                    problems.append(f"headline {n}: quantity value {q.value!r} is not in the quote")
            caveat = by_id.get(h.caveat_evidence)
            if caveat is None or caveat["kind"] != "caveat":
                problems.append(f"headline {n}: caveat_evidence is not a CAVEATS id")
            elif bad := cards.new_figures(h.caveat, caveat["quote"]):
                problems.append(f"headline {n}: caveat figures {bad} are not in its quote")
        main = sum(h.result in ("observation", "inference") for h in reply.headlines)
        nulls = len(reply.headlines) - main
        if main > MAX_FINDINGS:
            problems.append(f"{main} observations or inferences; at most {MAX_FINDINGS}")
        if nulls > MAX_NULLS:
            problems.append(f"{nulls} null results or corrections; at most {MAX_NULLS}")
        if not reply.headlines:
            problems.append("no headline chosen; the report has findings")
        if problems:
            raise CandidateError("; ".join(problems))
        return reply

    return parse


def short_id(evidence: str) -> str:
    """The ":chunk:index" part of a record id, as reviewers abbreviate it."""
    return evidence[evidence.index(":") :] if ":" in evidence else evidence


def named_headlines(reply: Reply, objection: str) -> set[int]:
    """Indexes of the headlines an objection names, by record id (whole or as ":0:6"),
    title or "headline N". Reviewers count from 0 or 1, so a number names both
    candidates: dropping an extra headline costs coverage, never fidelity."""
    text = objection.lower()
    hits = {
        n
        for n, h in enumerate(reply.headlines)
        if h.evidence.lower() in text
        or h.title.lower() in text
        or re.search(rf"(?<![\w:]){re.escape(short_id(h.evidence))}(?![\d:])", text)
    }
    for number in re.findall(r"\bheadline\s+(\d+)\b", text):
        k = int(number)
        hits |= {i for i in (k - 1, k) if i < len(reply.headlines)}
    return hits


def salvager(
    records: list[dict],
) -> Callable[[Reply, list[tuple[str, Reply]]], tuple[Reply, list[str]] | None]:
    """Keep the headlines no open objection names; fail if an objection names none.

    Each objection is read against the reply it was raised on, and the headlines it
    names are dropped from the final reply by record id, which a repair cannot
    renumber. An objection that names nothing could be about any headline, so then
    nothing is published."""
    parse = checker(records)

    def rescue(reply: Reply, notes: list[tuple[str, Reply]]) -> tuple[Reply, list[str]] | None:
        named: set[str] = set()
        for objection, seen in notes:
            hits = named_headlines(seen, objection)
            if not hits and cards.restates(objection):
                continue
            if not hits:
                return None
            named |= {seen.headlines[i].evidence for i in hits}
        keep = [h for h in reply.headlines if h.evidence not in named]
        if not keep:
            return None
        try:
            kept = parse(Reply(headlines=keep).model_dump_json())
        except CandidateError:
            return None
        return kept, sorted(named)

    return rescue


def one_line(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def carries_unit(value: str, unit: str) -> bool:
    """Whether the value already shows its unit, as "28.7%" does for "percent"."""
    unit = unit.strip().lower()
    return not unit or value.endswith(unit) or ("%" in value and unit in ("%", "percent"))


def render(sid: str, h: Headline, records: list[dict], first_added: str, source_hash: str):
    """The finding page: frontmatter for the cards, prose a reader can verify."""
    by_id = {r["id"]: r for r in records}
    record, caveat = by_id[h.evidence], by_id[h.caveat_evidence]
    fid = cards.finding_id(sid, record["quote"])
    fields = {
        "type": "Finding",
        "description": h.claim,
        "finding_id": fid,
        "result": h.result,
        "source": sid,
        "quantities": [q.model_dump() for q in h.quantities],
        "caveat": h.caveat,
        "first_added": first_added,
        "source_hash": source_hash,
    }
    tag = f"[src: {sid}]"
    lines = [f"# {h.title}", "", f"{h.claim} {tag}"]
    if h.quantities:
        lines += ["", "## Key figures", ""]
        for q in h.quantities:
            extra = "; ".join(
                f"{k} {v}" for k, v in (("denominator", q.denominator), ("scope", q.scope)) if v
            )
            unit = "" if carries_unit(q.value, q.unit) else f" {q.unit}"
            lines.append(f"- **{q.value}{unit}**: {q.what}{f' ({extra})' if extra else ''} {tag}")
    lines += [
        "",
        "## Evidence",
        "",
        f"> {one_line(record['quote'])} {tag}",
        "",
        f"From the report [[summaries/{sid}__REPORT]].",
        "",
        "## Caveat",
        "",
        f"{h.caveat} {tag}",
        "",
        f"> {one_line(caveat['quote'])} {tag}",
    ]
    # An extractor's restatement can carry its own arithmetic, which the report never states.
    others = [
        r
        for r in records
        if r["kind"] == "caveat"
        and r["id"] != caveat["id"]
        and not cards.new_figures(r["claim"], r["quote"])
    ]
    if others:
        lines += ["", "## Other caveats in this report", ""]
        lines += [f"- {one_line(r['claim'])} {tag}" for r in others[:OTHER_CAVEATS]]
    return fid, fields, "\n".join(lines)


def report_title(root: Path, sid: str) -> str:
    text = cards.source_path(root, sid).read_text(encoding="utf-8", errors="replace")
    m = re.search(r"^# +(.+)$", text, re.M)
    return m.group(1).strip() if m else sid


def pages_of(out: Path, sid: str) -> list[Path]:
    return sorted(out.glob(f"{sid}--*.md"))


def main(root: Path = ROOT) -> int:
    if not cards.require_runtime("headlines"):
        return 0
    scope = cards.load_scope(root)
    reports = scope.reports if scope else []
    out = root / OUT
    out.mkdir(parents=True, exist_ok=True)
    state_path = root / STATE
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    agent = cards.runtime()
    evidence = cards.source_evidence(agent.store, root, reports)

    todo = []
    accepted: list[tuple[str, list[dict], str, Reply]] = []
    for sid in reports:
        if sid not in evidence:
            print(f"  headlines/{sid}: no evidence extracted from the current text; skipped")
            continue
        records = evidence[sid]
        body = pack(sid, report_title(root, sid), records)
        messages = [{"role": "user", "content": PROMPT + json.dumps(body)}]
        # The models are part of the key: a new cards or review model re-judges.
        key = digest([messages, cards.policy(agent.config, ("cards", "review"))])
        saved = state.get(sid, {})
        on_disk = {p.name: file_hash(p) for p in pages_of(out, sid)}
        if saved.get("input") == key and saved.get("reply"):
            # The accepted reply is kept, so a page edited by hand or a new render
            # is rewritten from it without a model call.
            if saved.get("render") != RENDER or saved.get("pages") != on_disk:
                accepted.append((sid, records, key, Reply.model_validate(saved["reply"])))
            continue
        todo.append((sid, records, messages, key))

    def write(item: tuple) -> Reply:
        sid, records, messages, _ = item
        mine = cards.runtime()  # a ledger connection belongs to the thread that opened it
        try:
            return cards.reviewed(
                messages,
                f"headlines/{sid}",
                checker(records),
                agent=mine,
                salvage=salvager(records),
            )
        except CandidateError as exc:
            raise cards.failure(f"headlines/{sid}", exc, mine) from exc

    today = datetime.date.today().isoformat()
    written = failed = 0

    def publish(sid: str, records: list[dict], key: str, result: Reply) -> None:
        previous = {p.stem: cards.read_page(p)[0] for p in pages_of(out, sid)}
        source_hash = file_hash(cards.source_path(root, sid))
        names = set()
        for h in result.headlines:
            fid = cards.finding_id(sid, next(r for r in records if r["id"] == h.evidence)["quote"])
            first = previous.get(fid, {}).get("first_added", today)
            fid, fields, body = render(sid, h, records, first, source_hash)
            cards.write_page(out / f"{fid}.md", fields, body)
            names.add(f"{fid}.md")
        for stale in pages_of(out, sid):
            if stale.name not in names:
                stale.unlink()
        state[sid] = {
            "input": key,
            "render": RENDER,
            "reply": result.model_dump(),
            "pages": {p.name: file_hash(p) for p in pages_of(out, sid)},
        }
        atomic_json(state_path, state)
        record_failure(f"headlines/{sid}", None)
        print(f"  wrote {len(names)} finding(s) for {sid}")

    for sid, records, key, reply in accepted:
        publish(sid, records, key, reply)
    for (sid, records, _, key), result in parallel(todo, write, workers()):
        if isinstance(result, PageFailure):
            failed += 1
            record_failure(f"headlines/{sid}", result)
            print(f"  [FAILED] headlines/{sid}: {result}")
            continue
        publish(sid, records, key, result)
        written += 1

    retired = 0
    for page in sorted(out.glob("*.md")):
        if page.stem.split("--", 1)[0] not in reports:
            page.unlink()
            retired += 1
    for sid in [s for s in state if s not in reports]:
        state.pop(sid)
    atomic_json(state_path, state)
    prune_failures("headlines/", {f"headlines/{sid}" for sid in reports})
    print(
        f"headlines: {written} report(s) written, {len(reports) - len(todo)} unchanged or "
        f"skipped, {failed} failed, {retired} page(s) retired"
    )
    return 1 if failed and strict_pages() else 0


if __name__ == "__main__":
    sys.exit(main())
