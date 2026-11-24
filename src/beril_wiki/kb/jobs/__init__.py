"""Record jobs: the findings, labels, summaries, links and directions built on a report.

A section edit changes prose. A record job produces one structured record: a report's
headline findings, a finding's plain summary or literature label, a link between two
results, a topic's research directions. Each stage module in this package says which
jobs a run owes (``jobs``), and for each job what the writer reads (``pack``), the
checks its reply must pass (``check``) and how an accepted reply is stored
(``publish``). This module runs them the same way for every stage: a writer session
with one gated tool, a reviewer of the other vendor, at most ``rounds`` times.

The stages keep the curator's own checks and page formats, imported from
``beril_wiki.stages``, so what they write is what ``publish`` already reads. What
changes is when a job is owed. The curator re-asked a record whenever a hash of its
prompt, model or code changed. Here a record is owed when its report is ingested or
revised and the record is missing or rests on a withdrawn claim, and at no other time.
"""

from __future__ import annotations

import json
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any

from beril_wiki.kb.store import Store
from beril_wiki.kb.tools import Rejected, record_sha

if TYPE_CHECKING:
    from beril_wiki.kb.workflow import Runner

# Stage modules in the order their inputs become available.
STAGES = (
    "findings",
    "gists",
    "outcomes",
    "novelty",
    # Before links and shared, which read which topics a report's concepts sit in.
    "topics",
    "links",
    "shared",
    "conflicts",
    "directions",
    "followups",
    "literature",
    "authors",
    "figures",
)


@dataclass
class Scope:
    """What one run touched, which is all a stage may use to decide what it owes."""

    root: Path
    # One report; empty when a compile runs the stages that span the corpus.
    source: str
    reason: str  # "ingest", "revise", "refresh" or "compile"
    run: str = ""
    # Section ids accepted in this run, and page ids it created.
    edited: list[str] = field(default_factory=list)
    created: list[str] = field(default_factory=list)
    # Claim ids a revision withdrew.
    withdrawn: list[str] = field(default_factory=list)
    # Role -> model, for the "model" field the curator's state files carry.
    models: dict[str, str] = field(default_factory=dict)
    # Filled as stages run, for the stages after them.
    notes: dict[str, Any] = field(default_factory=dict)
    # Every report of a compile; empty in a one-report run.
    sources: list[str] = field(default_factory=list)

    @property
    def store(self) -> Store:
        return Store(self.root)


@dataclass
class Job:
    stage: str
    # Unique in the corpus, such as "gists/<finding id>"; names the run step.
    key: str
    # What the writer reads, as JSON.
    pack: dict
    # Returns the record as it will be stored, or raises Rejected with objections.
    check: Callable[[dict], dict]
    # Stores an accepted record. Called under the run's lock.
    publish: Callable[[dict], None]
    writer: str = "cards"
    reviewer: str = "card_review"  # "" for a job code alone can judge
    skill: str = ""  # default: wiki-<stage>
    review_skill: str = "wiki-card-review"
    # The tool set of the writer session, a key of tools.ROLES. "record" has the one
    # submit tool: the pack must then hold everything the record rests on. "card" adds
    # claims and read_source for a stage that cannot pack its evidence.
    tools: str = "record"
    # The page id this job creates, so later stages (figures) see it as new.
    creates: str = ""
    # JSON schema of the record, shown to the writer.
    schema: dict | None = None
    # A record code can build without a model, stored when the last round is still
    # refused: for a record the wiki cannot do without, such as a topic hub or the page
    # list. It is given the record the reviewer refused last (or None) and the
    # objections, so it can keep what was not faulted.
    fallback: Callable[[dict | None, list[dict]], dict] | None = None


def legacy(parse: Callable[[str], Any]) -> Callable[[dict], dict]:
    """A curator stage's ``checker`` as a job gate.

    Those checkers take the reply as text and raise ``CandidateError`` with every
    problem in one message; the gate wants a dict in and objections out.
    """
    from beril_wiki.agentic.runtime import CandidateError
    from beril_wiki.wording import MULTIPLE_TESTING, STAT_WORDS, STATS

    def check(record: dict) -> dict:
        text = json.dumps(record, ensure_ascii=False)
        try:
            value = parse(text)
        except CandidateError as exc:
            problems = exc.objections or [p.strip() for p in str(exc).split("; ") if p.strip()]
            if any("statistic" in p for p in problems):
                # The checkers say a record has statistical wording, not which words: a
                # writer in the first compile pilot used all its attempts looking.
                found = sorted(
                    {
                        m.group(0)
                        for pattern in (STATS, STAT_WORDS, MULTIPLE_TESTING)
                        for m in pattern.finditer(text)
                    }
                )
                problems.append("the statistical wording is: " + ", ".join(map(repr, found[:8])))
            raise Rejected("the record fails its checks", problems) from None
        dump = getattr(value, "model_dump", None)
        return dump() if dump else record

    return check


def evidence(store: Store, source: str) -> list[dict]:
    """A report's active claims in the shape the curator's stages read evidence in."""
    return [
        {
            "id": c["id"],
            "kind": c["kind"],
            "claim": c["text"],
            "quote": c["quote"],
            "source": source,
        }
        for c in store.claims(source)
        if c.get("status", "active") == "active"
    ]


def write_state(path: Path, state: dict) -> None:
    """A stage's state file, in the layout the curator writes (``atomic_json``)."""
    from beril_wiki.kb.store import write_text

    write_text(path, json.dumps(state, indent=2, sort_keys=True))


def forget_findings(root: Path, fids: set[str]) -> None:
    """Drop what was written about findings that changed or went away.

    A plain summary, a result type, a literature label and a link each describe one
    finding by its id. When the finding's wording changes, or its page goes, those
    records describe something the wiki no longer says; with them gone, each is owed
    again by the stage that writes it.
    """
    from beril_wiki.stages import cards, gists, links, novelty, outcomes

    if not fids:
        return
    for rel in (gists.STATE, outcomes.STATE, novelty.STATE):
        state = cards.load_state(root / rel)
        if fids & state.keys():
            write_state(root / rel, {k: v for k, v in state.items() if k not in fids})
    for fid in fids:
        (root / ".agentic" / "novelty" / f"{fid}.json").unlink(missing_ok=True)
    state = cards.load_state(root / links.STATE)
    answered = state.get("candidates", {})
    stale = [
        key
        for key in answered
        if key.startswith("pair:") and fids & set(key.removeprefix("pair:").split("|"))
    ]
    if stale:
        state["candidates"] = {k: v for k, v in answered.items() if k not in stale}
        write_state(root / links.STATE, state)


def brief(job: Job, objections: list[dict] | None) -> str:
    lines = [f"Record to write: {job.key}", "", "INPUT", json.dumps(job.pack, ensure_ascii=False)]
    if job.schema:
        lines += ["", "The record must match this JSON schema:", json.dumps(job.schema)]
    if objections:
        lines += ["", "A reviewer returned your record with these objections. Fix each:"]
        lines += [f"- {o.get('quote', '')!r}: {o['problem']}" for o in objections]
    lines += [
        "",
        "Call submit_record with the record. The session ends when it is accepted; if it "
        "is rejected, fix each objection and call it again.",
    ]
    return "\n".join(lines)


def review_brief(job: Job, record: dict, earlier: list[dict] | None) -> str:
    lines = [
        f"Record under review: {job.key}",
        f"sha of the record: {record_sha(record)}",
        "",
        "INPUT the writer was given",
        json.dumps(job.pack, ensure_ascii=False),
        "",
        "RECORD",
        json.dumps(record, ensure_ascii=False, indent=1),
    ]
    if earlier:
        lines += ["", "Your earlier objections; check only whether each is resolved:"]
        lines += [f"- {o.get('quote', '')!r}: {o['problem']}" for o in earlier]
    return "\n".join(lines)


def run_job(runner: Runner, job: Job) -> dict:
    """Write, review and store one record; a failure leaves what was stored before."""
    from beril_wiki.kb.workflow import Stop

    step = f"job-{job.key}"

    def note(entry: dict) -> None:
        runner.state.setdefault("progress", {})[step] = entry
        runner.save()

    def make() -> dict:
        saved = runner.state.setdefault("progress", {}).get(step, {})
        if "accepted" in saved:
            # The run died between the reviewer's accept and the end of publish. The
            # stores are written whole, so writing them again is safe, and the record
            # is not paid for twice.
            with runner.lock:
                job.publish(saved["accepted"])
            status = "fallback" if saved.get("fallback") else "accepted"
            return {"status": status, "rounds": saved.get("round", 1), "creates": job.creates}
        # What the reviewer said last time survives a stop, so a resumed run cannot
        # send the same refused record for a fresh opinion.
        objections: list[dict] | None = saved.get("objections")
        refused = saved.get("refused", "")
        # The refused record goes with its objections: the fallback keeps what the
        # reviewer did not fault in it, also after a stop.
        last: dict | None = saved.get("record")
        exhausted = False
        name = job.key.replace("/", "-")[-80:]
        for round_ in range(saved.get("round", 0) + 1, runner.config.rounds + 1):
            try:
                session, run = runner.dispatch(
                    f"{name}-write{round_}",
                    job.writer,
                    {"key": job.key},
                    brief(job, objections),
                    tools=job.tools,
                    skill=job.skill or f"wiki-{job.stage}",
                    check=job.check,
                )
            except Stop as exc:
                return {"status": "budget", "detail": str(exc)}
            if runner.halted:
                return {"status": "budget", "detail": runner.halted}
            record = session.record
            if record is None and session.exhausted:
                # Every attempt failed the checks. That is an answer, not an outage:
                # asking again on resume would buy the same refusals. The reviewer's
                # objections to the round before stay as they are for the fallback.
                exhausted = True
                break
            # With no reviewer to read it, a record from a session that broke off is
            # not taken: the writer may have been about to correct it.
            if record is None or not (job.reviewer or run.ok):
                return {"status": "failed", "detail": session.note or run.error or "no record"}
            sha = record_sha(record)
            if sha == refused:
                break
            if job.reviewer:
                task = {"section": job.key, "sha": sha, "candidate": json.dumps(record)}
                try:
                    reviewed, review_run = runner.dispatch(
                        f"{name}-review{round_}",
                        job.reviewer,
                        task,
                        review_brief(job, record, objections),
                        tools="verdict",
                        skill=job.review_skill,
                    )
                except Stop as exc:
                    return {"status": "budget", "detail": str(exc)}
                if runner.halted:
                    return {"status": "budget", "detail": runner.halted}
                verdict = reviewed.reviews.get(job.key)
                if verdict is None:
                    return {"status": "unreviewed", "detail": review_run.error or "no verdict"}
                if verdict["verdict"] != "accept":
                    objections, refused, last = verdict["objections"], sha, record
                    with runner.lock:
                        note(
                            {
                                "round": round_,
                                "objections": objections,
                                "refused": refused,
                                "record": record,
                            }
                        )
                    continue
            with runner.lock:
                note({"round": round_, "accepted": record})
                job.publish(record)
            return {"status": "accepted", "rounds": round_, "creates": job.creates}
        detail = [o["problem"] for o in objections or []]
        if exhausted:
            detail.append("no record passed the checks")
        if job.fallback is None:
            return {"status": "rejected", "detail": detail}
        record = job.fallback(last, objections or [])
        with runner.lock:
            note({"round": runner.config.rounds, "accepted": record, "fallback": True})
            job.publish(record)
        return {"status": "fallback", "detail": detail, "creates": job.creates}

    return runner.step(step, make)


def run_jobs(runner: Runner, jobs: list[Job]) -> dict[str, dict]:
    with ThreadPoolExecutor(max_workers=max(1, runner.config.jobs)) as pool:
        outcomes = list(pool.map(lambda job: run_job(runner, job), jobs))
    return {job.key: outcome for job, outcome in zip(jobs, outcomes, strict=True)}


def run_all(runner: Runner, scope: Scope, stages: tuple[str, ...] = STAGES) -> dict:
    """Every stage in order. A stage sees what the stages before it stored."""
    import importlib

    summary: dict[str, dict] = {}
    for name in stages:
        if not scope.source:
            runner.stage(f"records for the corpus: {name}")
        module = importlib.import_module(f"beril_wiki.kb.jobs.{name}")
        # A stage whose later jobs read its earlier ones (queries, then labels) lists
        # its steps in PHASES; each sees what the one before it stored.
        outcomes: dict[str, dict] = {}
        # A stage whose jobs must each see what the one before it stored (a topic's
        # directions are checked against every other topic's) says so with SERIAL.
        serial = bool(getattr(module, "SERIAL", False)) and scope.reason == "compile"
        for phase in getattr(module, "PHASES", None) or (module.jobs,):
            owed = phase(scope)
            while serial and owed:
                job = owed[0]
                outcomes[job.key] = run_job(runner, job)
                if outcomes[job.key]["status"] == "budget":
                    break
                owed = [j for j in phase(scope) if j.key not in outcomes]
            outcomes |= run_jobs(runner, owed) if owed and not serial else {}
            if any(o["status"] == "budget" for o in outcomes.values()):
                break
        # Read from the run's record, so a resumed run still knows the pages an
        # earlier attempt created when their jobs are no longer owed.
        with runner.lock:
            # Another report's worker records its steps while this one reads.
            steps = dict(runner.state["steps"])
        scope.created += sorted(
            {
                str(outcome["creates"])
                for key, outcome in steps.items()
                if key.startswith(f"job-{name}/")
                and isinstance(outcome, dict)
                and outcome.get("creates")
            }
            - set(scope.created)
        )
        after = getattr(module, "after", None)
        if after:
            with runner.lock:
                after(scope, outcomes)
        counts: dict[str, int] = {}
        for outcome in outcomes.values():
            counts[outcome["status"]] = counts.get(outcome["status"], 0) + 1
        if counts:
            summary[name] = counts
        scope.notes[name] = outcomes
        if counts.get("budget"):
            break
    return summary
