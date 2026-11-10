"""The model-job machinery the six card stages share.

The card stages (headlines, novelty, directions, gists, links and shared) each write
only their own records, so the pages Topics and Literature own keep their
fingerprints. Their model replies are JSON, checked in code before any reviewer
reads them. This module runs those jobs: one per item in a worker pool, with code
checks, an open review and closed verifications, salvage of a reply that did not
converge, and a failure record per item. Reading pages and records is in
beril_wiki.records; the wording rules are in beril_wiki.wording.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel, ValidationError

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import (
    Issue,
    PageFailure,
    parallel,
    record_failure,
    record_salvage,
    strict_pages,
    workers,
)
from beril_wiki.agentic.runtime import (
    CARD_EFFORT,
    CONTENT_FLAG,
    CandidateError,
    JobFailed,
    Refused,
    Runtime,
    configured,
    digest,
    file_hash,
    model_policy,
    runtime,
)
from beril_wiki.check import figures_in, prose_only
from beril_wiki.records import source_path, title_of

T = TypeVar("T")
M = TypeVar("M", bound=BaseModel)
I = TypeVar("I")  # noqa: E741

# A verifier objection that opens "Issue 3 remains: ..." restates issue 3 of its list.
RESTATED = re.compile(r"^\W*issue\s+#?(\d+)\b", re.I)
RESOLVED = " [restates an issue listed among these notes]"


def require_runtime(stage: str) -> bool:
    """These stages run only under the agentic runtime: they key cached jobs, record
    failures and check vendors through it, which the legacy CBORG path cannot."""
    if configured():
        return True
    print(f"stages.{stage}: needs the agentic runtime (agentic run); nothing written")
    return False


def load_state(path: Path) -> dict:
    """A stage's state file, or an empty state before the stage first saves one."""
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def each_job(
    items: list[I], step: Callable[[I], str], job: Callable[[I, Runtime], T]
) -> Iterator[tuple[I, T | PageFailure]]:
    """Run `job` on each item in the worker pool and yield each result as it finishes.

    Each job gets its own runtime, since a ledger connection belongs to the thread that
    opened it. An item whose reply does not converge, or whose content a model refuses,
    comes back as its PageFailure, already recorded under its step and printed; any
    other error stops the stage. The caller clears a converged item's failure after it
    saves the item, so a run stopped between the two still lists the item as failed."""

    def run(item: I) -> T:
        agent = runtime()
        try:
            return job(item, agent)
        except CandidateError as exc:
            raise failure(step(item), exc, agent) from exc

    for item, result in parallel(items, run, workers()):
        if isinstance(result, PageFailure):
            record_failure(step(item), result)
            print(f"  [FAILED] {step(item)}: {result}")
        yield item, result


def exit_code(failed: int) -> int:
    """A stage's exit status: failed items stop the run only under --strict-pages."""
    return 1 if failed and strict_pages() else 0


def source_evidence(store: Path, root: Path, sids: list[str]) -> dict[str, list[dict]]:
    """Accepted evidence records per report, from the newest snapshot extracted from
    the report's current text. A report with no such snapshot is left out: records
    from an older text could quote passages the report no longer contains."""
    wanted = {
        sid: file_hash(source_path(root, sid)) for sid in sids if source_path(root, sid).exists()
    }
    found: dict[str, list[dict]] = {}
    blobs = sorted((store / "evidence").glob("*.json"), key=lambda p: -p.stat().st_mtime)
    for blob in blobs:
        if len(found) == len(wanted):
            break
        data = json.loads(blob.read_text(encoding="utf-8"))
        hashes: dict[str, set[str]] = {}
        for entry in data.get("coverage", []):
            hashes.setdefault(entry["source"], set()).add(entry["sha256"])
        for sid, current in wanted.items():
            if sid not in found and hashes.get(f"{sid}__REPORT.md") == {current}:
                found[sid] = [f for f in data["findings"] if f["source"] == sid]
    return found


def finding_id(sid: str, quote: str) -> str:
    """Stable across re-extraction: keyed on the quoted text, not chunk offsets."""
    norm = re.sub(r"\s+", " ", quote).strip().lower()
    return f"{sid}--{hashlib.sha256(norm.encode()).hexdigest()[:8]}"


def write_page(path: Path, fields: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(C.fm_block(fields) + body.strip() + "\n", encoding="utf-8")


def read_page(path: Path) -> tuple[dict, str]:
    return C.parse_fm(path.read_text(encoding="utf-8"))


def collections(root: Path) -> dict[str, str]:
    """Collection page stem -> its title, from wiki/data/."""
    out = {}
    for path in sorted((root / "wiki/data").glob("*.md")):
        if path.stem != "index":
            out[path.stem] = title_of(path.read_text(encoding="utf-8"), path.stem)
    return out


def collection_id(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def new_figures(text: str, pool: str) -> list[str]:
    """Figures in text that the pool never states, small integer counts included."""
    have = figures_in(prose_only(pool))
    return sorted(n for n in figures_in(prose_only(text)) if n not in have)


def in_quote(value: str, quote: str) -> bool:
    """Whether a key figure's value appears in the quote as a whole figure or phrase."""
    if figures_in(value):
        return not new_figures(value, quote)
    return re.search(rf"(?<!\w){re.escape(value.strip())}(?!\w)", quote) is not None


def policy(config: dict, roles: tuple[str, ...] = ("cards", "review", "queries")) -> str:
    """The models a card record was judged with: a change re-judges it, as a change
    to the curator's stage revision does for the stages that predate these."""
    chosen = model_policy(config)
    return digest([[chosen[r] for r in roles], CARD_EFFORT])


def parse_reply(raw: str, model: type[M]) -> M:
    """A JSON reply as the stage's schema; a malformed one is the model's to correct."""
    try:
        try:
            value = C.parse_json_reply(raw)
        except ValueError:
            # A reply that repeats its JSON object: read the first one whole.
            start = raw.find("{")
            if start < 0:
                raise
            value, _ = json.JSONDecoder().raw_decode(raw[start:])
        return model.model_validate(value)
    except (ValueError, ValidationError) as exc:
        raise CandidateError(f"reply does not match the schema: {str(exc)[:3000]}") from exc


def asked(
    messages: list[dict],
    step: str,
    parse: Callable[[str], T],
    attempts: int = 3,
    agent: Runtime | None = None,
) -> T:
    """One job whose reply code checks, with corrections; no reviewer."""
    return (agent or runtime()).generate(messages, step, parse, attempts=attempts)


def reviewed(
    messages: list[dict],
    step: str,
    parse: Callable[[str], T],
    attempts: int = 4,
    agent: Runtime | None = None,
    salvage: Callable[[T, list[tuple[str, T]]], tuple[T, list[str]] | None] | None = None,
) -> T:
    """Code checks first, then one open review by the reviewer role and a closed
    verification of each repair, as extraction does (batch.EvidenceAcceptor).

    `salvage` may rescue a job that did not converge from the last candidate a
    reviewer judged. It gets that candidate and each open objection paired with the
    candidate the objection was raised against, since a repair can reorder items and
    "headline 2" names an item of the reply the reviewer read. It returns what
    survives plus what it removed, or None to fail."""
    agent = agent or runtime()
    pending: list[str] = []
    judged: list[T] = []  # the last candidate a reviewer gave a verdict on
    raised: dict[str, T] = {}  # objection -> the candidate it was raised against
    refers: dict[str, str] = {}  # "issue 3 remains: ..." -> the issue it restates

    def accept(raw: str) -> T:
        nonlocal pending
        value = parse(raw)
        judged[:] = [value]
        if not pending:
            try:
                agent.review(messages, raw, step)
            except CandidateError as exc:
                pending = exc.objections or [str(exc)[:2000]]
                for objection in pending:
                    raised.setdefault(objection, value)
                raise
        else:
            before, pending = pending, agent.verify(messages, raw, pending, step)
            for objection in pending:
                raised.setdefault(objection, value)
                # The verifier numbers the issues it was given from 0.
                m = RESTATED.match(objection)
                if objection not in before and m and int(m[1]) < len(before):
                    refers.setdefault(objection, before[int(m[1])])
            if pending:
                raise CandidateError(
                    f"objections still open on {step}: {json.dumps(pending)}", pending
                )
        return value

    def attempt() -> T:
        try:
            return agent.generate(messages, step, accept, attempts=attempts)
        except CandidateError:
            notes: list[tuple[str, T]] = []
            for objection in pending if judged else []:
                # A restatement may name its item only in the issue it restates.
                chain = [objection]
                while chain[-1] in refers and refers[chain[-1]] not in chain:
                    chain.append(refers[chain[-1]])
                if len(chain) > 1:
                    chain[0] += RESOLVED
                notes += [(o, raised.get(o, judged[0])) for o in chain if o not in dict(notes)]
            rescued = salvage(judged[0], notes) if salvage and notes else None
            if rescued is None:
                raise
            value, removed = rescued
            issues = [Issue(category="unsupported", note=o[:2000]) for o in pending]
            print(
                f"  [SALVAGED] {step} dropped {len(removed)} item(s) the reviewer still objects to"
            )
            record_salvage(step, issues, removed, list(agent.jobs))
            return value

    # Outside salvage: a refused verification gave no verdict on the repair.
    return content_refusal_fails_item(step, attempt)


def restates(objection: str) -> bool:
    """A restatement whose original issue is also among the salvage notes."""
    return objection.endswith(RESOLVED)


def content_refusal_fails_item(step: str, call: Callable[[], T]) -> T:
    """A model that refuses the content on its fallback too fails this one item, as
    an unsupported candidate does; a transport or auth failure still stops the stage."""
    try:
        return call()
    except Refused as exc:
        raise CandidateError(f"{step}: content refused: {exc}"[:2000]) from exc
    except JobFailed as exc:
        if CONTENT_FLAG not in str(exc):
            raise
        raise CandidateError(f"{step}: content refused: {exc}"[:2000]) from exc


def failure(step: str, exc: Exception, agent: Runtime | None = None) -> PageFailure:
    """A record that did not converge, in the shape failures.json already holds."""
    jobs = list(agent.jobs) if agent is not None else []
    return PageFailure(step, [Issue(category="unsupported", note=str(exc)[:2000])], jobs)
