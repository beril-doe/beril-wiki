"""What starts model work, and the three workflows that do it.

Only three things schedule a model call:

    plan     a report whose content hash is new or differs from the one last ingested
    revise   a claim that such a report changed or no longer supports
    refresh  an operator naming sections and a reason

Editing code, a skill, configuration or a wiki page schedules nothing. Each workflow is
a short list of steps recorded in ``.agentic/runs/<run>/run.json``; a run that stops is
resumed from the first step it had not finished. Accepted results are in Git text by
then, so the run folder is disposable.
"""

from __future__ import annotations

import copy
import json
import os
import random
import re
import sys
import threading
import time
import uuid
from collections import defaultdict
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

import yaml

from beril_wiki.kb import agents, index, pages
from beril_wiki.kb.agents import Agent, Run
from beril_wiki.kb.store import (
    DIGESTS,
    HEADING,
    Busy,
    Store,
    blocks,
    checkout_lock,
    sha256,
    write_text,
)
from beril_wiki.kb.tools import Rejected, Session, Tools, finish_pending, opening, promote

SKILLS = {
    "extract": "wiki-extract",
    "curate": "wiki-curate",
    "edit": "wiki-edit",
    "review": "wiki-review",
}
# The policy the curator's pilots chose (agentic.yaml): GPT extracts and reviews, Sonnet
# plans and writes derived pages and records, Haiku writes integrated pages and labels.
DEFAULT_ROLES = {
    "extract": "gpt-6.1-sol@medium",
    "curate": "claude-sonnet-5-5@high",
    "edit": "claude-haiku-5-5@medium",
    "write": "claude-sonnet-5-5@medium",
    "review": "gpt-6-luna@high",
    "cards": "claude-sonnet-5-5@medium",
    "card_review": "gpt-6-luna@high",
    "findings_review": "gpt-6.1-sol@high",
    "labels": "claude-haiku-5-5@medium",
    "queries": "gpt-6.1-sol@medium",
    "figures": "gpt-6.1-sol@medium",
}
# Each writing role and the role that reviews it: never the same vendor.
REVIEWED_BY = {
    # A compile's glossary and page list.
    "curate": "review",
    "edit": "review",
    "write": "review",
    "cards": ("card_review", "findings_review"),
    "labels": "card_review",
}
# Page kinds whose existing sections the cheaper editor takes (see ``writer_role``).
INTEGRATED = ("concepts", "entities", "summaries")
# What a vendor says when a subscription or key has no allowance left. A bare "limit
# reached" is left out: a session that runs out of tool calls says that too.
QUOTA = re.compile(
    r"(usage|rate|session|weekly|daily|\d+.hour)[ _-]?limit|hit your limit|limit .{0,3}resets"
    r"|quota|\b429\b|too many requests|credit balance|out of credits",
    re.I,
)
# A vendor that turns away a burst of requests takes the same request a minute later.
# Measured on GPT-6.1 Sol: six sessions started together, two got "429 Too Many
# Requests", and each passed on its next attempt.
BURST = re.compile(r"\b429\b|too many requests", re.I)
SPENT = re.compile(
    r"(usage|session|weekly|daily)[ _-]?limit|hit your limit|resets|quota|credit", re.I
)
BURST_PAUSE = 60.0
# A vendor that refuses the login refuses every session, so the first one stops the run.
# Seen from the Claude Agent SDK as the whole reply "Not logged in · Please run /login".
# Matched as the start of the reply or in the harness's error, never inside a model's
# prose: a page may say that study participants were not logged in.
LOGIN_REPLY = re.compile(r"\s*not logged in\b.{0,5}please run /login", re.I)
LOGIN_ERROR = re.compile(
    r"\b401\b[^\n]{0,20}unauthori[sz]ed|invalid api key|please run /login", re.I
)


def logged_out(run: Run) -> bool:
    return not run.ok and bool(LOGIN_REPLY.match(run.text) or LOGIN_ERROR.search(run.error))


# What a session stages. A retried session starts again from what it held before.
SESSION_RESULTS = ("claims", "plan", "candidates", "reviews", "record", "covered", "note")
QUOTA_PAUSE = 900.0
# A vendor that is briefly full says so and takes the same request a minute later.
BUSY = re.compile(
    r"at capacity|overloaded|temporarily unavailable|routing discovery timed out"
    r"|\b(502|503|529)\b",
    re.I,
)
BUSY_PAUSE = 45.0
BUSY_TRIES = 6
# Sessions that failed one after another, in any stage, before the run stops: a broken
# login or a harness that cannot start fails every session the same way.
FAIL_STREAK = 10
Launch = Callable[[Agent, str, str, Tools, Path], Run]


class Stop(Exception):
    """The run cannot continue: a budget is spent or a configuration rule is broken."""


@dataclass
class Config:
    roles: dict[str, Agent]
    max_tokens: int = 3_000_000
    max_usd: float | None = None
    # USD per million tokens (input, cached input, output), for an API-equivalent
    # estimate where the harness reports no cost.
    prices: dict[str, tuple[float, float, float]] = field(default_factory=dict)
    rounds: int = 2
    timeout: float = 1200.0
    # Held for each session before it starts. A curate session measured 195,000.
    reserve_tokens: int = 250_000
    reserve_usd: float = 0.30
    max_sections: int = 12
    jobs: int = 3
    # Seconds to keep waiting when a vendor reports its quota is used up, asking again
    # every ``QUOTA_PAUSE``. Zero stops the run at once, which is what a run someone
    # is watching wants; an unattended compile sets hours.
    quota_wait: float = 0.0
    # Run the curator's deterministic stages (author stubs, titles, names, errata)
    # around the record stages. Off only where a caller does that itself.
    tidy: bool = True

    @classmethod
    def load(cls, root: Path, **overrides: Any) -> Config:
        path = root / "wiki.yaml"
        data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
        data = data or {}
        roles = {**DEFAULT_ROLES, **(data.get("roles") or {})}
        for role in list(roles):
            if overrides.get(role):
                roles[role] = overrides.pop(role)
        known = {f for f in cls.__dataclass_fields__ if f not in ("roles", "prices")}
        settings = {k: v for k, v in data.items() if k in known}
        settings |= {k: v for k, v in overrides.items() if k in known and v is not None}
        prices = {m: tuple(p) for m, p in (data.get("prices") or {}).items()}
        return cls({r: Agent.parse(s) for r, s in roles.items()}, prices=prices, **settings)

    def check(self) -> None:
        """Nothing is reviewed by the vendor that wrote it."""
        if self.jobs < 1 or self.rounds < 1:
            raise Stop("jobs and rounds must be 1 or more")
        for writer, reviewers in REVIEWED_BY.items():
            for reviewer in (reviewers,) if isinstance(reviewers, str) else reviewers:
                if self.roles[writer].provider == self.roles[reviewer].provider:
                    raise Stop(
                        f"{writer} ({self.roles[writer].model}) and {reviewer} "
                        f"({self.roles[reviewer].model}) run on the same vendor; set a "
                        "reviewer from the other vendor in wiki.yaml"
                    )
        if self.max_usd is not None:
            unpriced = sorted(
                {a.model for a in self.roles.values() if a.provider == "codex"} - set(self.prices)
            )
            if unpriced:
                raise Stop(
                    f"--max-usd needs a price for {', '.join(unpriced)} under prices in "
                    "wiki.yaml: the Codex harness reports tokens, not cost"
                )


def instructions(root: Path, skill_name: str) -> str:
    """A skill, then the wiki's editorial contract. No SDK detail in either."""
    skill = (root / "skills" / skill_name / "SKILL.md").read_text(encoding="utf-8")
    skill = pages.FRONT.sub("", skill, count=1).strip()
    contract = (root / "contract" / "AGENTS.md").read_text(encoding="utf-8")
    rules = re.search(r"^## Domain Rules.*?(?=^## Frontmatter)", contract, re.M | re.S)
    return f"{skill}\n\n# Wiki rules\n\n{rules.group(0).strip() if rules else contract}\n"


def default_launch(config: Config, run_dir: Path, usd_left: Callable[[], float | None]) -> Launch:
    def launch(agent: Agent, system: str, prompt: str, tools: Tools, work: Path) -> Run:
        from beril_wiki.kb.server import Host

        session = tools.session
        name = Path(session.path).stem if session.path else session.role
        with Host(tools) as host:
            return agents.run(
                agent,
                system,
                prompt,
                host.url,
                tools.names(),
                work,
                transcript=run_dir / f"{name}.transcript.jsonl",
                timeout=config.timeout,
                max_turns=session.calls + 8,
                # Only the Claude harness can stop itself at a spend limit.
                max_usd=usd_left(),
                stop=lambda: session.done,
            )

    return launch


# Outcomes worth another try when the run resumes; everything else is settled.
TRANSIENT = ("budget", "failed", "unreviewed")
RESUMABLE = ("running", "stopped")


class Runner:
    """One run: its step record, its spend, and the way it starts an agent."""

    def __init__(
        self,
        root: Path,
        config: Config,
        workflow: str,
        subject: str,
        launch: Launch | None = None,
        pin: str = "",
    ) -> None:
        self.root, self.config = Path(root), config
        self.store = Store(self.root)
        self.pin = pin
        runs = self.root / ".agentic" / "runs"
        runs.mkdir(parents=True, exist_ok=True)
        slug = re.sub(r"[^A-Za-z0-9_.-]+", "-", subject)[:60]
        resumed = self.open_run(self.root, workflow, subject, pin)
        stamp = f"{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}"
        self.dir = resumed or runs / f"{stamp}-{workflow}-{slug}"
        self.dir.mkdir(exist_ok=True)
        self.id = self.dir.name
        self.lock = threading.Lock()
        self.held_usd = 0.0
        # Set when a vendor reports a quota or rate limit; no session starts after it.
        self.halted = ""
        # Before the record is read: this writes the outcome of any edit a dead run
        # left half applied, in this run's folder or another's.
        finish_pending(self.store)
        path = self.dir / "run.json"
        self.state: dict[str, Any] = (
            json.loads(path.read_text(encoding="utf-8"))
            if path.exists()
            else {
                "run": self.id,
                "workflow": workflow,
                "subject": subject,
                "pin": pin,
                "tokens": 0,
                "usd": 0.0,
                "steps": {},
                "sessions": [],
            }
        )
        self.state["started"] = round(time.time())
        self.state["status"] = "running"
        # What `beril-wiki status` reads to tell a working run from a dead or idle one.
        self.state |= {"pid": os.getpid(), "open": {}, "waiting": {}}
        # Sessions on record when this process took the run over: its health is judged
        # from the ones after them.
        self.state["since"] = len(self.state["sessions"])
        # What a process that died held for sessions that never reported is given back.
        self.state["tokens"] -= self.state.get("held", 0)
        self.state["held"] = 0
        self.streak = 0
        # However many thread pools a workflow nests, ``jobs`` sessions run at once.
        self.active = 0
        # Sessions each model runs at once. A vendor does not say how many it takes, so
        # a refusal lowers the model's limit to what was running and successes raise it
        # again: measured on GPT-6.1 Sol, the fifth session at once was refused.
        self.turn = threading.Condition(self.lock)
        self.limits: dict[str, int] = {}
        self.running: dict[str, int] = defaultdict(int)
        self.taken: dict[str, int] = defaultdict(int)
        self.launch = launch or default_launch(config, self.dir, self.usd_left)
        self.save()

    @staticmethod
    def open_run(root: Path, workflow: str, subject: str, pin: str) -> Path | None:
        """The newest unfinished run of this workflow on this subject and input."""
        slug = re.sub(r"[^A-Za-z0-9_.-]+", "-", subject)[:60]
        runs = Path(root) / ".agentic" / "runs"
        for path in sorted(runs.glob(f"*-{workflow}-{slug}"), reverse=True):
            record = path / "run.json"
            if not record.exists():
                continue
            state = json.loads(record.read_text(encoding="utf-8"))
            if state.get("status") in RESUMABLE and state.get("pin", "") == pin:
                return path
        return None

    def save(self) -> None:
        write_text(self.dir / "run.json", json.dumps(self.state, ensure_ascii=False, indent=1))

    def note(self, message: str) -> None:
        """A line for whoever watches the run: its log file, and standard error."""
        line = f"{time.strftime('%H:%M:%S')} {message}"
        with (self.dir / "notes.log").open("a", encoding="utf-8") as out:
            out.write(line + "\n")
        print(line, file=sys.stderr, flush=True)

    def stage(
        self, label: str, done: int | None = None, total: int | None = None, code: bool = False
    ) -> None:
        """Say what the run is on, for whoever asks its status. ``code`` marks a step
        that starts no session, such as the site's deterministic stages."""
        with self.lock:
            self.state["stage"] = {
                "label": label,
                "done": done,
                "total": total,
                "code": code,
                "at": round(time.time()),
            }
            self.save()

    def step(self, key: str, make: Callable[[], Any]) -> Any:
        """Run a step once; a resumed run reuses what the step recorded.

        A step that ended for a passing reason (no budget, a vendor outage) is not
        recorded, so the resumed run tries it again.
        """
        if key in self.state["steps"]:
            return self.state["steps"][key]
        value = make()
        if isinstance(value, dict) and value.get("status") in TRANSIENT:
            return value
        with self.lock:
            self.state["steps"][key] = value
            self.save()
        # The journal of an applied edit goes only once its outcome is on record.
        (self.dir / f"{key}.promote.json").unlink(missing_ok=True)
        return value

    def cost(self, agent: Agent, run: Run) -> float:
        if run.cost_usd is not None:
            return run.cost_usd
        price = self.config.prices.get(agent.model)
        if not price:
            return 0.0
        fresh = run.input_tokens + run.cache_write_tokens
        return (
            fresh * price[0] + run.cached_tokens * price[1] + run.output_tokens * price[2]
        ) / 1e6

    def usd_left(self) -> float | None:
        if self.config.max_usd is None:
            return None
        return max(0.01, self.config.max_usd - self.state["usd"])

    def admit(self) -> None:
        """Refuse to start a session the remaining budget could not pay for.

        A cap stops new sessions. A session already running ends at its own tool-call
        budget and timeout, so a run can pass a cap by at most what its sessions in
        flight use beyond their reservations.
        """
        c = self.config
        if self.halted:
            raise Stop(self.halted)
        if self.state["tokens"] + c.reserve_tokens > c.max_tokens:
            raise Stop(f"token budget reached: {self.state['tokens']:,} of {c.max_tokens:,} used")
        if c.max_usd is not None:
            if self.state["usd"] + self.held_usd + c.reserve_usd > c.max_usd:
                raise Stop(f"spend cap reached: USD {self.state['usd']:.2f} of {c.max_usd:.2f}")

    def enter(self, model: str) -> None:
        """Wait for a place among the run's sessions and among the model's, then hold
        the session's budget. Raises ``Stop`` when the run has halted or the budget
        cannot pay for one more session; a session that waits is charged nothing."""
        jobs = max(1, self.config.jobs)
        with self.turn:
            while True:
                self.admit()
                if self.active < jobs and self.running[model] < self.limits.get(model, jobs):
                    break
                self.turn.wait(timeout=5)
            self.active += 1
            self.running[model] += 1
            # Held until the session reports, so parallel sessions cannot both spend
            # the same remainder.
            self.state["tokens"] += self.config.reserve_tokens
            self.state["held"] += self.config.reserve_tokens
            self.held_usd += self.config.reserve_usd

    def leave(self, model: str, ok: bool, turned_away: bool) -> None:
        """Give the places back and move the model's limit. Called with the lock held."""
        jobs = max(1, self.config.jobs)
        self.active -= 1
        self.running[model] -= 1
        limit = self.limits.get(model, jobs)
        if turned_away:
            # The vendor took what is still running and no more.
            self.limits[model] = max(1, min(limit, self.running[model]))
            self.taken[model] = 0
        elif ok:
            self.taken[model] += 1
            if self.taken[model] >= limit and limit < jobs:
                self.limits[model], self.taken[model] = limit + 1, 0
        if self.limits.get(model, limit) != limit:
            self.note(f"{model} now runs {self.limits[model]} sessions at once (was {limit})")
        self.turn.notify_all()

    def dispatch(
        self,
        name: str,
        role: str,
        task: dict,
        brief: str,
        session: Session | None = None,
        budget: tuple[int, int] | None = None,
        tools: str = "",
        skill: str = "",
        check: Callable[[dict], dict] | None = None,
    ) -> tuple[Session, Run]:
        """Start one agent session. ``role`` picks the model in wiki.yaml; ``tools``
        (default: the same name) picks what the session may call, and ``skill`` its
        instructions."""
        tools = tools or role
        skill = skill or SKILLS[role]
        agent = self.config.roles[role]
        fresh = Session.start(tools, task, run=self.id)
        if budget:
            fresh.calls, fresh.chars = budget
        if session is None:
            session = fresh
        else:
            session.task, session.finished, session.rejections = task, False, {}
            session.calls, session.chars = fresh.calls, fresh.chars
            session.used_calls = session.used_chars = 0
        session.path = str(self.dir / f"{name}.json")
        # What the session held before this dispatch: a second attempt starts from it,
        # not from whatever a failed attempt staged.
        before = copy.deepcopy({f: getattr(session, f) for f in SESSION_RESULTS})
        waited, tries, bursts, attempt = 0.0, 0, 0, 0
        while True:
            attempt += 1
            try:
                # Every attempt passes the same door: the halt, the budget, a place.
                self.enter(agent.model)
            except Stop:
                with self.lock:
                    self.state["waiting"].pop(name, None)
                raise
            with self.lock:
                self.state["waiting"].pop(name, None)
                self.state["open"][name] = round(time.time())
                self.save()
            session.save()
            try:
                run = self.launch(
                    agent,
                    instructions(self.root, skill),
                    brief,
                    Tools(self.root, session, check),
                    self.dir,
                )
            except Exception as exc:
                run = Run(str(agent), error=f"{type(exc).__name__}: {exc}"[:300])
            told = f"{run.error} {run.text}"
            # A refused login is neither a limit nor a full vendor: nothing is retried.
            out = logged_out(run)
            limited = not run.ok and not out and bool(QUOTA.search(told))
            busy = not run.ok and not out and not limited and bool(BUSY.search(run.error))
            if (limited or busy) and (session.finished or session.produced):
                # The result was on file before the vendor failed; it stands.
                run.ok, run.error, limited, busy = True, "", False, False
            pause = 0.0
            if busy and tries < BUSY_TRIES:
                tries += 1
                pause = BUSY_PAUSE * tries
            elif limited:
                # A burst limit doubles its wait up to the quota's, so one that never
                # lifts is waited on like a spent allowance. Sessions refused together
                # do not all come back together.
                burst = bool(BURST.search(told)) and not SPENT.search(told)
                wait = min(BURST_PAUSE * 2**bursts, QUOTA_PAUSE) if burst else QUOTA_PAUSE
                wait += random.uniform(0, wait / 2) if burst else 0.0
                bursts += burst
                if waited + wait <= self.config.quota_wait:
                    pause = wait
                    waited += wait
            why = "is at capacity" if busy else "reports a usage or rate limit"
            with self.lock:
                again = bool(pause) and not self.halted
                self.leave(agent.model, run.ok, limited and bool(BURST.search(told)))
                # A request the vendor turned away before the model did anything used
                # nothing. Any other failure without reported usage keeps its
                # reservation, or a run of timeouts would never reach a cap.
                refused = (limited or busy) and not run.tokens and not session.used_calls
                silent = not run.ok and not run.tokens and not refused
                spent = self.config.reserve_tokens if silent else run.tokens
                self.state["tokens"] += spent - self.config.reserve_tokens
                self.state["held"] -= self.config.reserve_tokens
                self.held_usd -= self.config.reserve_usd
                unmetered = silent and run.cost_usd is None
                self.state["usd"] += self.config.reserve_usd if unmetered else self.cost(agent, run)
                self.state["sessions"].append(
                    {
                        "name": name if attempt == 1 else f"{name}#{attempt}",
                        "role": role,
                        **asdict(run),
                        "text": run.text[:300],
                        "calls": session.used_calls,
                        "chars": session.used_chars,
                        "at": round(time.time()),
                        # Asked again after a pause: not a failed session.
                        "retry": again,
                    }
                )
                self.state["open"].pop(name, None)
                if again:
                    until = round(time.time() + pause)
                    self.state["waiting"][name] = {"until": until, "why": f"{agent.model} {why}"}
                else:
                    self.streak = 0 if run.ok else self.streak + 1
                    if limited and not self.halted:
                        # Nothing is retried on another vendor or model: the run stops
                        # and says so, before a queued session can take the place.
                        self.halted = (
                            f"{agent.provider} ({agent.model}) reported a usage or rate "
                            f"limit: {(run.error or run.text)[:200]}. Nothing else was "
                            "started; run the same command again when the quota is back, "
                            "and it resumes here."
                        )
                    if out and not self.halted:
                        self.halted = (
                            f"{agent.provider} ({agent.model}) refused the login: "
                            f"{(run.text or run.error)[:200]}. Nothing else was started; "
                            "sign in again and run the same command, and it resumes here."
                        )
                    if self.streak >= FAIL_STREAK and not self.halted:
                        self.halted = (
                            f"{self.streak} sessions in a row failed, the last ({name}) "
                            f"with: {run.error[:200]}. Nothing else was started."
                        )
                self.save()
            if not again:
                break
            self.note(f"{agent.model} {why}; asking again in {pause:.0f}s ({name})")
            time.sleep(pause)
            for name_, value in copy.deepcopy(before).items():
                setattr(session, name_, value)
            session.finished, session.rejections = False, {}
            session.used_calls = session.used_chars = 0
        return session, run

    def finish(self, status: str, **summary: Any) -> dict:
        self.state["status"] = status
        self.state["summary"] = summary
        self.state |= {"open": {}, "waiting": {}}
        self.save()
        return {
            "run": self.id,
            "status": status,
            "tokens": self.state["tokens"],
            "usd": round(self.state["usd"], 4),
            **summary,
        }


# Whether a run is working

# Seconds: a vendor wait longer than this, or a run with no session open and none
# finished for this long, is worth a person's look.
LONG_WAIT = 300
IDLE = 600
CODE_STEP = 4 * 3600


def turned_away(error: str) -> bool:
    return bool(QUOTA.search(error) or BUSY.search(error))


def alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def health(state: dict, now: float, running: bool, timeout: float = 1200.0) -> tuple[str, str]:
    """A verdict on a run's record and the reason: ``ok`` and ``done`` need nobody;
    ``stopped``, ``dead``, ``failing``, ``waiting``, ``stuck`` and ``idle`` do."""
    if state["status"] != "running":
        reason = str((state.get("summary") or {}).get("reason", ""))
        return state["status"], reason
    if not running:
        return "dead", f"the record says running but process {state.get('pid')} is gone"
    # Judged from the sessions of the process that holds the run now. A request a
    # vendor turned away and the run asks again is not a failed session.
    sessions = state["sessions"][state.get("since", 0) :]
    recent = [s for s in sessions if not s.get("retry", turned_away(s["error"]))][-20:]
    failed = [s for s in recent if not s["ok"]]
    if len(recent) >= 10 and 2 * len(failed) >= len(recent):
        return "failing", f"{len(failed)} of the last {len(recent)} sessions failed: " + (
            failed[-1]["error"][:160]
        )
    late = {n: w for n, w in state.get("waiting", {}).items() if w["until"] - now > LONG_WAIT}
    if late:
        name, wait = max(late.items(), key=lambda kv: kv[1]["until"])
        return "waiting", (
            f"{len(late)} sessions wait on a vendor, the last until "
            f"{time.strftime('%H:%M:%S', time.localtime(wait['until']))}: {wait['why']} ({name})"
        )
    opened = {n: t for n, t in state.get("open", {}).items() if n not in state.get("waiting", {})}
    old = {n: t for n, t in opened.items() if now - t > timeout + 120}
    if old:
        name, start = min(old.items(), key=lambda kv: kv[1])
        return "stuck", f"{name} has run for {(now - start) / 60:.0f} min"
    stage = state.get("stage") or {}
    last = max(
        [s.get("at", 0) for s in sessions[-50:]] + [state.get("started", 0), stage.get("at", 0)]
    )
    # A step in code starts no session; the site's stages may each take hours.
    quiet = CODE_STEP if stage.get("code") else IDLE
    if not opened and not state.get("waiting") and last and now - last > quiet:
        return "idle", f"no session is open and none has finished for {(now - last) / 60:.0f} min"
    return "ok", ""


# What would run, and why


def plan(root: Path) -> dict:
    """The model work the corpus calls for. Reads report hashes and nothing else."""
    db = index.connect(root)
    try:
        rows = db.execute("SELECT id, status FROM sources ORDER BY id").fetchall()
    finally:
        db.close()
    reason = {"new": "report not ingested yet", "changed": "report content changed"}
    tasks = [
        {
            "workflow": "ingest" if r["status"] == "new" else "revise",
            "source": r["id"],
            "reason": reason[r["status"]],
        }
        for r in rows
        if r["status"] in reason
    ]
    missing = [r["id"] for r in rows if r["status"] == "missing"]
    out: dict[str, Any] = {"tasks": tasks}
    if missing:
        out["missing_reports"] = missing
    # Not model work until an operator runs refresh, but never to be lost sight of.
    owed = sorted({b["target"] for b in Store(root).backlog() if b.get("withdrawn")})
    if owed:
        out["corrections_owed"] = owed
    return out


def impact(root: Path, source: str = "", claim: str = "", section: str = "") -> dict:
    """Which sections rest on a report or a claim, or which claims a section rests on."""
    db = index.connect(root)
    try:
        if section:
            page_id, _, anchor = section.partition("#")
            rows = db.execute(
                "SELECT sc.claim, sc.how, c.source FROM section_claims sc JOIN claims c "
                "ON c.id = sc.claim WHERE sc.page = ? AND sc.anchor = ? ORDER BY sc.claim",
                (page_id, anchor),
            ).fetchall()
            return {"section": section, "claims": [dict(r) for r in rows]}
        where, arg = ("c.id = ?", claim) if claim else ("c.source = ?", source)
        rows = db.execute(
            "SELECT sc.page, sc.anchor, sc.how, count(*) AS n FROM section_claims sc "
            f"JOIN claims c ON c.id = sc.claim WHERE {where} "
            "GROUP BY sc.page, sc.anchor, sc.how ORDER BY sc.page, sc.anchor",
            (arg,),
        ).fetchall()
        cited = db.execute(
            "SELECT count(*) FROM section_sources WHERE source = ?", (source,)
        ).fetchone()[0]
    finally:
        db.close()
    sections = [
        {
            "section": f"{r['page']}#{r['anchor']}" if r["anchor"] else r["page"],
            "link": r["how"],
            "claims": r["n"],
        }
        for r in rows
    ]
    out = {"sections": sections, "pages": len({r["page"] for r in rows})}
    if source:
        out["sections_citing_report"] = cited
    return out


def lint(root: Path) -> dict:
    """Free checks on the records: nothing here calls a model or edits a file."""
    store = Store(root)
    db = index.connect(root)
    try:
        one = lambda sql, *a: db.execute(sql, a).fetchone()[0]  # noqa: E731
        orphans = [
            f"{r['page']}#{r['anchor']}"
            for r in db.execute(
                "SELECT DISTINCT sc.page, sc.anchor FROM section_claims sc WHERE sc.anchor != '' "
                "AND NOT EXISTS (SELECT 1 FROM sections s WHERE s.page = sc.page "
                "AND s.anchor = sc.anchor)"
            )
        ]
        unsupported = one(
            "SELECT count(*) FROM section_sources ss JOIN sections s ON s.id = ss.section "
            "JOIN pages p ON p.id = s.page WHERE p.kind IN ('concepts', 'entities', 'conflicts', "
            "'topics', 'summaries') AND NOT EXISTS (SELECT 1 FROM section_claims sc JOIN claims c "
            "ON c.id = sc.claim WHERE sc.page = s.page AND sc.anchor = s.anchor "
            "AND c.source = ss.source)"
        )
        report = {
            "sources": dict(
                db.execute("SELECT status, count(*) FROM sources GROUP BY 1").fetchall()
            ),
            "claims": dict(db.execute("SELECT status, count(*) FROM claims GROUP BY 1").fetchall()),
            "links": dict(
                db.execute("SELECT how, count(*) FROM section_claims GROUP BY 1").fetchall()
            ),
            "claims_without_any_link": one(
                "SELECT count(*) FROM claims WHERE status != 'retracted' AND id NOT IN "
                "(SELECT claim FROM section_claims)"
            ),
            "claims_linked_to_a_page_only": one(
                "SELECT count(DISTINCT claim) FROM section_claims WHERE claim NOT IN "
                "(SELECT claim FROM section_claims WHERE anchor != '')"
            ),
            "section_citations_without_a_linked_claim": unsupported,
            "links_to_missing_sections": orphans[:50],
            "queued_findings": len(store.backlog()),
        }
    finally:
        db.close()
    return report


# Briefs: the task message each role receives


def claim_lines(claims: list[dict], quotes: bool = False) -> str:
    lines = []
    for c in claims:
        lines.append(f"- {c['id']} [{c['kind']}] {c['text']}")
        if quotes:
            lines.append(f"  quote: {json.dumps(c['quote'], ensure_ascii=False)}")
    return "\n".join(lines)


def brief_extract(
    store: Store, source: str, spans: list[list[int]] | None, recheck: list[dict] | None = None
) -> str:
    text = store.source_text(source)
    title = HEADING.search(text)
    lines = [
        f"Report id: {source}",
        f"Title: {title.group(2) if title else source}",
        f"Length: {len(text)} characters.",
    ]
    if spans:
        ranges = ", ".join(f"{a}-{b}" for a, b in spans)
        lines.append(
            f"The report was revised. Read and extract only these character ranges: {ranges}. "
            "Claims already recorded for the unchanged parts stay as they are."
        )
        if recheck:
            lines += [
                "",
                "These claims were recorded from those ranges before the revision. For each "
                "one the text still supports exactly as worded, submit it again with the same "
                "kind, quote and text, copied character for character. Where the meaning "
                "changed, write the claim anew. Leave out a claim the text no longer "
                "supports. Then add any claim that is new.",
                claim_lines(recheck, quotes=True),
            ]
    else:
        lines.append("Read the whole report in order and extract its claims.")
    return "\n".join(lines)


def brief_curate(source: str, claims: list[dict], summary: str) -> str:
    return (
        f"Report {source} was read. Its {len(claims)} new claims are listed below.\n"
        f"The report's own summary page ({summary}) is written separately and receives every "
        "claim; do not target it. Decide which other sections of the wiki these claims "
        "change, then call propose_plan.\n\n" + claim_lines(claims)
    )


def brief_edit(
    task: dict,
    assigned: list[dict],
    objections: list[dict] | None = None,
    support: list[dict] | None = None,
) -> str:
    lines = [f"Section to edit: {task['section']}"]
    if task.get("new_page"):
        lines.append(
            f"This page does not exist yet. Title: {task['new_page']['title']}. Write its "
            "opening section: what the page is about and what the evidence shows. Call "
            "edit_section with base_sha from read_section (the section is empty)."
        )
    elif task.get("new_section"):
        lines.append(f"This section does not exist yet. Its heading will be: {task['heading']}.")
    if task.get("why"):
        lines.append(f"Why these claims belong here: {task['why']}")
    if task.get("instruction"):
        lines.append(f"Instruction: {task['instruction']}")
    if assigned:
        lines += ["", "Claims to integrate:", claim_lines(assigned, quotes=True)]
    if support:
        lines += [
            "",
            "Claims from other projects that belong on this page; use them and list them:",
            claim_lines(support, quotes=True),
        ]
    if task.get("withdrawn"):
        lines += [
            "",
            "The report was revised and no longer supports these claims as recorded. Remove or "
            "correct every statement that rests on them, and list what you remove in dropped:",
            claim_lines(task["withdrawn"], quotes=True),
        ]
    if objections:
        lines += ["", "A reviewer returned your staged text with these objections. Fix each:"]
        lines += [f"- {o.get('quote', '')!r}: {o['problem']}" for o in objections]
    return "\n".join(lines)


def brief_review(candidate: dict, old: str, claims: list[dict], earlier: list[dict] | None) -> str:
    lines = [
        f"Section: {candidate['section']}",
        f"sha of the new text: {candidate['sha']}",
        "",
        "OLD TEXT",
        old or "(the section is new)",
        "",
        "NEW TEXT",
        candidate["body"],
        "",
        "Claims the new text rests on:",
        claim_lines(claims, quotes=True) or "(none listed)",
    ]
    if candidate["declined"]:
        lines += ["", "Assigned claims the editor declined:"]
        lines += [f"- {d.get('claim')}: {d.get('reason')}" for d in candidate["declined"]]
    if candidate["dropped"]:
        lines += ["", "Removed from the old text:"]
        lines += [f"- {d.get('text')}: {d.get('reason')}" for d in candidate["dropped"]]
    if earlier:
        lines += ["", "Your earlier objections; check only whether each is resolved:"]
        lines += [f"- {o.get('quote', '')!r}: {o['problem']}" for o in earlier]
    return "\n".join(lines)


# Shared steps


def summary_page(store: Store, source: str) -> str:
    plain = f"summaries/{source}"
    return plain if source in DIGESTS or store.page_path(plain).exists() else f"{plain}__REPORT"


def front_matter(kind: str, source: str, new: dict) -> str:
    fields: dict[str, Any] = {"type": new["type"], "description": new.get("description", "")}
    suffix = "" if source in DIGESTS else "__REPORT"
    if kind == "summaries":
        fields |= {"doc_type": "short", "full_text": f"sources/{source}{suffix}.md"}
    else:
        fields["sources"] = [f"summaries/{source}{suffix}.md"]
    body = "".join(f"{k}: {json.dumps(v, ensure_ascii=False)}\n" for k, v in fields.items())
    return f"---\n{body}---\n"


def source_state(root: Path, source: str) -> str:
    """new, changed, current or missing, as ``plan`` sees the report; '' if unknown."""
    db = index.connect(root)
    try:
        row = db.execute("SELECT status FROM sources WHERE id = ?", (source,)).fetchone()
    finally:
        db.close()
    return row["status"] if row else ""


def unchanged(runner: Runner, source: str) -> None:
    """Stop when the report on disk is no longer the one this run started from."""
    if sha256(runner.store.source_text(source)) != runner.pin:
        raise Stop(
            f"{source} changed while the run was in progress; nothing more was recorded. "
            "Run `beril-wiki plan` and start again."
        )


def extract(
    runner: Runner,
    source: str,
    spans: list[list[int]] | None = None,
    recheck: list[dict] | None = None,
) -> list[dict]:
    """Run the extractor and write the claims that passed its gate.

    Only a session that ran to its own ``finish`` counts: a timeout halfway through a
    report would otherwise pass for a complete reading, and ``revise`` would retract
    the claims the extractor never reached.
    """
    store = runner.store
    length = len(store.source_text(source))
    assigned = spans or [[0, length]]
    reading = sum(b - a for a, b in assigned)
    # One read and one submit per 12,000 characters, with room to resubmit.
    budget = (max(40, 2 * (reading // 12_000 + 1) + 10), max(400_000, 2 * reading + 100_000))

    def make() -> list[dict]:
        task = {"source": source, "spans": spans}
        session, run = runner.dispatch(
            "extract",
            "extract",
            task,
            brief_extract(store, source, spans, recheck),
            budget=budget,
        )
        if not (run.ok and session.finished):
            reason = run.error or "the extractor stopped before calling finish"
            raise Stop(f"extraction did not complete ({reason}); no claim was recorded")
        unread = uncovered(assigned, session.covered)
        if unread:
            ranges = ", ".join(f"{a}-{b}" for a, b in unread[:6])
            raise Stop(f"the extractor never read characters {ranges}; no claim was recorded")
        unchanged(runner, source)
        return [{**c, "added": date.today().isoformat()} for c in session.claims]

    # Recorded first, then written: writing is repeatable, so a crash between the two
    # is repaired here on resume without a second extraction.
    added = runner.step("extract", make)
    have = {c["id"] for c in store.claims(source)}
    missing = [c for c in added if c["id"] not in have]
    if missing:
        store.write_claims(source, [*store.claims(source), *missing])
    return added


def uncovered(spans: list[list[int]], read: list[list[int]]) -> list[list[int]]:
    """The parts of the assigned ranges that no read returned."""
    out = []
    for a, b in spans:
        at = a
        for start, end in sorted(read):
            if end <= at or start >= b:
                continue
            if start > at:
                out.append([at, start])
            at = max(at, end)
        if at < b:
            out.append([at, b])
    return out


def writer_role(task: dict) -> str:
    """An existing section of an integrated page goes to the cheaper editor. A page
    that does not exist yet has no text to anchor it and goes to the writer, as does
    every other kind of page."""
    kind = task["section"].split("/")[0]
    return "edit" if kind in INTEGRATED and not task.get("new_page") else "write"


def edit_target(runner: Runner, key: str, task: dict, claims_by_id: dict[str, dict]) -> dict:
    """One section: edit, cross-vendor review, at most ``rounds`` times, then promote."""
    config = runner.config

    def make() -> dict:
        assigned = lookup(runner.root, task.get("claims", []), claims_by_id)
        support = lookup(runner.root, task.get("support", []), claims_by_id)
        session: Session | None = None
        # What the reviewer said last time survives a stop, so a resumed run cannot
        # send the same refused text for a fresh opinion.
        progress = runner.state.setdefault("progress", {}).get(key, {})
        objections: list[dict] | None = progress.get("objections")
        refused = progress.get("refused", "")
        for round_ in range(progress.get("round", 0) + 1, config.rounds + 1):
            try:
                session, run = runner.dispatch(
                    f"{key}-edit{round_}",
                    writer_role(task),
                    task,
                    brief_edit(task, assigned, objections, support),
                    session,
                    tools="edit",
                    skill="wiki-edit",
                )
            except Stop as exc:
                return {"status": "budget", "detail": str(exc)}
            candidate = session.candidates.get(task["section"])
            if candidate is None:
                return {
                    "status": "declined" if run.ok else "failed",
                    "detail": session.note or run.error,
                }
            if candidate["sha"] == refused:
                # The editor staged nothing new, so the text the reviewer returned
                # must not go back for a second opinion.
                break
            old = Tools(runner.root, session)._current(task["section"])["accepted"]
            evidence = lookup(runner.root, candidate["claims"], claims_by_id)
            review_task = {
                "section": task["section"],
                "sha": candidate["sha"],
                "candidate": candidate["body"],
            }
            try:
                reviewed, review_run = runner.dispatch(
                    f"{key}-review{round_}",
                    "review",
                    review_task,
                    brief_review(candidate, old, evidence, objections),
                )
            except Stop as exc:
                return {"status": "budget", "detail": str(exc)}
            verdict = reviewed.reviews.get(task["section"])
            if verdict is None:
                return {"status": "unreviewed", "detail": review_run.error or "no verdict given"}
            if verdict["verdict"] == "accept":
                outcome = {
                    "status": "accepted",
                    "rounds": round_,
                    "sha": candidate["sha"],
                    "claims": candidate["claims"],
                    "declined": candidate["declined"],
                }
                try:
                    with runner.lock:
                        promote(
                            runner.store,
                            session,
                            task["section"],
                            writer=str(config.roles[writer_role(task)]),
                            reviewer=str(config.roles["review"]),
                            journal=runner.dir / f"{key}.promote.json",
                            record={"key": key, "outcome": outcome},
                        )
                except Rejected as exc:
                    return {"status": "stale", "detail": str(exc)}
                return outcome
            objections, refused = verdict["objections"], candidate["sha"]
            with runner.lock:
                runner.state["progress"][key] = {
                    "round": round_,
                    "objections": objections,
                    "refused": refused,
                }
                runner.save()
        return {"status": "rejected", "detail": [o["problem"] for o in objections or []]}

    return runner.step(key, make)


def lookup(root: Path, ids: list[str], known: dict[str, dict]) -> list[dict]:
    """Claims by id, from the run's own report first and the index for the rest."""
    missing = [c for c in ids if c not in known]
    found: dict[str, dict] = {}
    if missing:
        db = index.connect(root)
        try:
            marks = ",".join("?" * len(missing))
            rows = db.execute(f"SELECT * FROM claims WHERE id IN ({marks})", missing)
            found = {r["id"]: dict(r) for r in rows}
        finally:
            db.close()
    return [known.get(c) or found[c] for c in ids if c in known or c in found]


def queue_rows(
    run: str, source: str, target: str, claim_ids: list[str], reason: str, withdrawn: bool = False
) -> list[dict]:
    """Backlog rows. A ``withdrawn`` row is a correction still owed: the section may
    state a result its report no longer supports."""
    today = date.today().isoformat()
    rows = []
    for claim in claim_ids:
        row = {
            "id": f"{claim}>{target}",
            "claim": claim,
            "source": source,
            "target": target,
            "reason": reason,
            "added": today,
            "run": run,
        }
        rows.append(row | ({"withdrawn": True} if withdrawn else {}))
    return rows


def target_key(section: str) -> str:
    return f"edit-{sha256(section)[:8]}-{re.sub(r'[^a-z0-9]+', '-', section)[-50:]}"


def run_targets(
    runner: Runner, source: str | None, targets: list[dict], claims_by_id: dict
) -> dict:
    """Edit every target, a few at a time, and queue what was not accepted.

    ``source`` is the report being read; ``refresh`` passes None because its claims are
    already queued or already on the page.
    """
    # Named by section alone, so a resumed run finds each section's recorded outcome
    # whatever order the targets come in.
    keys = [target_key(t["section"]) for t in targets]
    with ThreadPoolExecutor(max_workers=max(1, runner.config.jobs)) as pool:
        outcomes = list(
            pool.map(
                lambda kt: edit_target(runner, kt[0], kt[1], claims_by_id),
                zip(keys, targets, strict=True),
            )
        )
    queued: list[dict] = []
    counts: dict[str, int] = defaultdict(int)
    for target, outcome in zip(targets, outcomes, strict=True):
        status = outcome["status"]
        counts[status] += 1
        owed = [c["id"] for c in target.get("withdrawn", [])]
        if status == "accepted":
            if source:
                # Also the rows an earlier attempt at this section left when it failed.
                settled = [*owed, *target.get("claims", [])]
                runner.store.unqueue(source, {f"{c}>{target['section']}" for c in settled})
            # A summary page takes what it needs from the whole report; what it leaves
            # out is not a finding waiting for a home.
            if target["section"].startswith("summaries/"):
                continue
            left = [str(d.get("claim")) for d in outcome.get("declined", [])]
            queued += queue_rows(
                runner.id, source or "", target["section"], left, "declined by the editor"
            )
            continue
        if status == "declined" and not owed:
            continue
        reason = f"{status}: {str(outcome.get('detail', ''))[:200]}"
        queued += queue_rows(
            runner.id, source or "", target["section"], list(target.get("claims", [])), reason
        )
        # The old statement is still on the page; this row keeps the correction owed.
        queued += queue_rows(runner.id, source or "", target["section"], owed, reason, True)
    if queued and source:
        runner.store.queue(source, queued)
    return {
        "outcomes": dict(counts),
        "queued": len(queued),
        "sections": [
            {"section": t["section"], **o} for t, o in zip(targets, outcomes, strict=True)
        ],
    }


def stage_reports(store: Store, source: str) -> None:
    """Fill ``staging/`` with the reports the wiki has read, plus the one in hand.

    The curator's deterministic stages take "the projects that have a summary page"
    from that folder. It is gitignored scratch, rebuilt here on every run.
    """
    staging = store.root / "staging"
    staging.mkdir(exist_ok=True)
    wanted = {}
    read = store.sources()
    for sid in sorted({*read, source} - {""}):
        path = store.source_path(sid)
        # Another report edited since it was read is staged as the wiki last read it:
        # its revision is no run's accepted text yet, and the checks must not see it.
        mirror = store.root / "wiki" / "sources" / f"{sid}__REPORT.md"
        if sid != source and mirror.exists() and path.exists():
            if read.get(sid, {}).get("sha256") != sha256(path.read_text(encoding="utf-8")):
                path = mirror
        if path.exists():
            wanted[f"{sid}.md" if sid in DIGESTS else f"{sid}__REPORT.md"] = path
    for stale in staging.glob("*.md"):
        if stale.name not in wanted:
            stale.unlink()
    for name, path in wanted.items():
        text = path.read_text(encoding="utf-8")
        target = staging / name
        if not target.exists() or target.read_text(encoding="utf-8") != text:
            write_text(target, text)


def tidy(runner: Runner, source: str) -> dict:
    """The curator's deterministic stages: author and data stubs, page titles, the
    platform's name, recorded errata. No model; safe to repeat."""
    from beril_wiki.agentic.runtime import WorkflowError
    from beril_wiki.kb import finishers

    if not runner.config.tidy:
        return {}
    stage_reports(runner.store, source)
    try:
        with runner.lock:
            return finishers.finish(runner.root)
    except WorkflowError as exc:
        raise Stop(f"a deterministic stage failed: {exc}") from None


def run_records(
    runner: Runner,
    source: str,
    reason: str,
    result: dict,
    targets: list[dict],
    withdrawn: list[str] | None = None,
    stages: tuple[str, ...] | None = None,
) -> dict:
    """Everything owed after a run's section edits: the record stages (findings,
    labels, links, directions ...), the deterministic stages, then figures, which must
    see each page in its final form."""
    from beril_wiki.kb import jobs

    accepted = {s["section"] for s in result["sections"] if s["status"] == "accepted"}
    scope = jobs.Scope(
        root=runner.root,
        source=source,
        reason=reason,
        run=runner.id,
        edited=sorted(accepted),
        created=sorted(
            t["section"].split("#")[0]
            for t in targets
            if t.get("new_page") and t["section"] in accepted
        ),
        withdrawn=list(withdrawn or []),
        models={role: agent.model for role, agent in runner.config.roles.items()},
    )
    tidy(runner, source)
    before = tuple(name for name in stages or jobs.STAGES if name != "figures")
    summary = jobs.run_all(runner, scope, before)
    if any(counts.get("budget") for counts in summary.values()):
        return summary
    tidy(runner, source)
    return summary | jobs.run_all(runner, scope, ("figures",))


def unfinished(runner: Runner, result: dict, records: dict | None = None) -> str:
    """Why a run cannot be called done, or "" when it can.

    A stopped run keeps its record, and the same command resumes it: steps that ended
    for a passing reason run again and every other step is reused.
    """
    counts = [result["outcomes"], *(records or {}).values()]
    if runner.halted:
        return runner.halted
    if any(c.get("budget") for c in counts):
        return "budget reached; run the same command with a higher cap to resume"
    # A section that fails leaves its claims in the backlog. A record has no such
    # queue, so the run stays open until its session has an answer.
    waiting = sum(c.get(s, 0) for c in counts[1:] for s in ("failed", "unreviewed"))
    if waiting:
        return (
            f"{waiting} record job(s) ended with no answer (a session failed or gave no "
            "verdict); run the same command again to retry them"
        )
    return ""


def record_source(runner: Runner, source: str) -> None:
    """Mark the report as read at the revision this run started from."""
    unchanged(runner, source)
    store = runner.store
    text = store.source_text(source)
    rows = store.sources()
    rows[source] = {
        "id": source,
        "sha256": runner.pin,
        "claims": sum(1 for c in store.claims(source) if c.get("status", "active") == "active"),
        "blocks": [h for _, _, h in blocks(text)],
        "ingested": date.today().isoformat(),
        "run": runner.id,
    }
    store.write_sources(rows)


def mirror_report(store: Store, source: str) -> None:
    """The published copy of a report under wiki/sources, byte for byte."""
    if source in DIGESTS:
        return
    target = store.root / "wiki" / "sources" / f"{source}__REPORT.md"
    text = store.source_text(source)
    if not target.exists() or target.read_text(encoding="utf-8") != text:
        write_text(target, text)


def supersede(root: Path, workflow: str, source: str, pin: str) -> None:
    """Close unfinished runs on an older revision of this report.

    Their report bytes are gone, so they cannot resume. A revision that had already
    withdrawn claims but not yet listed the sections to correct gets those corrections
    queued here, so the newer run cannot mark the report current while a page still
    states them.
    """
    store = Store(root)
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "-", source)[:60]
    for path in sorted((Path(root) / ".agentic" / "runs").glob(f"*-{workflow}-{slug}")):
        record = path / "run.json"
        if not record.exists():
            continue
        state = json.loads(record.read_text(encoding="utf-8"))
        if state.get("status") not in RESUMABLE or state.get("pin", "") == pin:
            continue
        steps = state.get("steps", {})
        withdrawn = steps.get("settle", {}).get("withdrawn", [])
        if withdrawn and "targets" not in steps:
            db = index.connect(root)
            try:
                marks = ",".join("?" * len(withdrawn))
                links = db.execute(
                    f"SELECT page, anchor, claim FROM section_claims WHERE claim IN ({marks})",
                    withdrawn,
                ).fetchall()
            finally:
                db.close()
            rows: list[dict] = []
            for link in links:
                target = f"{link['page']}#{link['anchor']}" if link["anchor"] else link["page"]
                rows += queue_rows(
                    state["run"], source, target, [link["claim"]], "superseded revision", True
                )
            if rows:
                store.queue(source, rows)
        state["status"] = "superseded"
        write_text(record, json.dumps(state, ensure_ascii=False, indent=1))


def begin(
    root: Path, workflow: str, source: str, config: Config, launch: Launch | None, state: str
) -> Runner:
    """Admit a report workflow: the right source state, or a run of it to resume."""
    config.check()
    store = Store(root)
    if not store.source_path(source).exists():
        raise Stop(f"no report for {source!r} under corpus/")
    pin = sha256(store.source_text(source))
    supersede(root, workflow, source, pin)
    if Runner.open_run(root, workflow, source, pin) is None:
        found = source_state(root, source)
        if found != state:
            hint = {
                "current": "it matches the hash last ingested, so there is nothing to read",
                "new": "use `beril-wiki ingest`",
                "changed": "use `beril-wiki revise`",
            }.get(found, "run `beril-wiki plan`")
            raise Stop(
                f"{workflow} needs a {state} report; {source} is {found or 'unknown'}: {hint}"
            )
    return Runner(root, config, workflow, source, launch, pin)


# Workflows


def ingest(root: Path, source: str, config: Config, launch: Launch | None = None) -> dict:
    """Read a new report into the wiki: extract, place, edit under caps, review."""
    try:
        with checkout_lock(root):
            return _ingest(begin(root, "ingest", source, config, launch, "new"), source)
    except Busy as exc:
        raise Stop(str(exc)) from None


def _ingest(runner: Runner, source: str) -> dict:
    store = runner.store
    try:
        mirror_report(store, source)
        new_claims = extract(runner, source)
        claims_by_id = {c["id"]: c for c in store.claims(source)}
        if not claims_by_id:
            raise Stop("the extractor recorded no claims; the report was not ingested")
        summary = summary_page(store, source)

        def choose() -> dict:
            targets: list[dict] = []
            queued_by_plan: list[dict] = []
            if new_claims:

                def curate() -> dict:
                    task = {"claims": [c["id"] for c in new_claims], "source": source}
                    session, run = runner.dispatch(
                        "curate", "curate", task, brief_curate(source, new_claims, summary)
                    )
                    if session.plan is None:
                        raise Stop(f"the curator proposed no plan: {run.error or session.note}")
                    return session.plan

                plan_ = runner.step("curate", curate)
                for target in plan_["targets"]:
                    kind = target["page"].split("/")[0]
                    task = {k: target[k] for k in ("section", "claims", "why") if k in target}
                    if target.get("new_page"):
                        new = target["new_page"]
                        task["support"] = target.get("support", [])
                        task["new_page"] = {
                            "title": new["title"],
                            "front": front_matter(kind, source, new),
                        }
                    elif target.get("new_section"):
                        task |= {"new_section": True, "heading": target["heading"]}
                    targets.append(task)
                for item in plan_["queued"]:
                    queued_by_plan += queue_rows(
                        runner.id, source, item["target"], item["claims"], item["reason"]
                    )
                for item in plan_["skipped"]:
                    if str(item.get("reason", "")).startswith("queue"):
                        queued_by_plan += queue_rows(
                            runner.id, source, "", item.get("claims", []), str(item["reason"])
                        )
            if not store.page_path(summary).exists():
                text = store.source_text(source)
                title = HEADING.search(text)
                name = re.sub(r"^Report:\s*", "", title.group(2)) if title else source
                described = {"type": "Summary", "description": f"Summary of the project {name}."}
                targets.insert(
                    0,
                    {
                        "section": f"{summary}#{pages.LEAD}",
                        "claims": [c for c, row in claims_by_id.items() if row["kind"] != "figure"][
                            :120
                        ],
                        "why": "Summarize the project for a reader who has not seen the report.",
                        "new_page": {
                            "title": name,
                            "front": front_matter("summaries", source, described),
                        },
                    },
                )
            return {"targets": targets, "queued": queued_by_plan}

        # Recorded, so a resumed run edits the sections the first attempt chose.
        chosen = runner.step("targets", choose)
        targets, queued_by_plan = chosen["targets"], chosen["queued"]
        if queued_by_plan:
            store.queue(source, queued_by_plan)
        result = run_targets(runner, source, targets, claims_by_id)
        why = unfinished(runner, result)
        if why:
            return runner.finish("stopped", claims=len(new_claims), **result, reason=why)
        if source not in DIGESTS and not store.page_path(summary).exists():
            # Findings, author pages and data pages all link to the summary. Without
            # it they would publish dead links, so nothing more is written, and the
            # next attempt writes the summary afresh.
            key = target_key(f"{summary}#{pages.LEAD}")
            with runner.lock:
                runner.state["steps"].pop(key, None)
                runner.state.get("progress", {}).pop(key, None)
            return runner.finish(
                "stopped",
                claims=len(new_claims),
                **result,
                reason="the summary page was not accepted, so nothing that links to it was "
                "written; run the same command again to retry it",
            )
        records = run_records(runner, source, "ingest", result, chosen["targets"])
        why = unfinished(runner, result, records)
        if why:
            return runner.finish(
                "stopped", claims=len(new_claims), **result, records=records, reason=why
            )
        result["records"] = records
        record_source(runner, source)
        return runner.finish(
            "done", claims=len(new_claims), **result, queued_by_plan=len(queued_by_plan)
        )
    except Stop as exc:
        return runner.finish("stopped", reason=str(exc))


def carry_forward(store: Store, source: str) -> dict:
    """Sort a revised report's claims without a model: which carry forward untouched,
    and which sit in a block of the report that changed or lost their quote."""
    text = store.source_text(source)
    known = set(store.sources().get(source, {}).get("blocks", []))
    current = blocks(text)
    kept, affected = [], []
    for claim in store.claims(source):
        if claim.get("status", "active") == "retracted":
            kept.append(claim)
            continue
        at = text.find(claim["quote"])
        block = next((h for a, b, h in current if a <= at < b), "") if at >= 0 else ""
        moved = {"start": at, "end": at + len(claim["quote"])} if at >= 0 else {}
        if at >= 0 and block in known:
            kept.append({**claim, **moved, "status": "active"})
            continue
        # The quote is gone, or it survives inside a block whose other text changed:
        # a table header or a denominator beside it may no longer mean the same.
        # Both wait as "recheck" until settle has seen what was extracted again, so
        # running this twice gives the same answer.
        kept.append({**claim, **moved, "status": "recheck"})
        affected.append(claim["id"])
    store.write_claims(source, kept)
    changed = [[a, b] for a, b, h in current if h not in known]
    return {"affected": affected, "carried": len(kept) - len(affected), "changed": changed}


CONTENT_WORD = re.compile(r"[a-z][a-z0-9-]{3,}")


def same_statement(old: str, new: str) -> bool:
    """Whether a re-extracted claim is the old claim again.

    Only the same words count. Code cannot tell a paraphrase from a changed condition
    or a reversed direction ("increased" against "decreased" share every other word),
    so anything else is treated as a new claim and the old one as withdrawn. The
    extractor is shown the old claims and told to repeat the wording of those that
    still hold.
    """
    return " ".join(old.lower().split()) == " ".join(new.lower().split())


def settle(rows: list[dict], affected: list[str], new_claims: list[dict]) -> dict:
    """Match re-extracted claims to the ones under recheck. Reads only; see
    ``apply_settlement``.

    A new claim with the same quote, kind and wording confirms the old claim, which
    keeps its id and its links; the new one is a duplicate. An old claim nothing
    confirms is withdrawn, and the new claims that remain are fresh evidence.
    """
    confirmed: list[str] = []
    duplicates: list[str] = []
    for claim in rows:
        if claim["id"] not in affected:
            continue
        twin = next(
            (
                n
                for n in new_claims
                if n["id"] not in duplicates
                and (n["quote"], n["kind"]) == (claim["quote"], claim["kind"])
                and same_statement(claim["text"], n["text"])
            ),
            None,
        )
        if twin:
            confirmed.append(claim["id"])
            duplicates.append(twin["id"])
    return {
        "confirmed": confirmed,
        "withdrawn": [c for c in affected if c not in confirmed],
        "fresh": [c["id"] for c in new_claims if c["id"] not in duplicates],
        "duplicates": duplicates,
    }


def apply_settlement(store: Store, source: str, outcome: dict) -> None:
    """Write a settlement to the claims file. Repeating it changes nothing, so it runs
    after the outcome is on record and again on every resume."""
    out = []
    for claim in store.claims(source):
        if claim["id"] in outcome["duplicates"]:
            continue
        if claim["id"] in outcome["confirmed"]:
            claim = {**claim, "status": "active"}
        elif claim["id"] in outcome["withdrawn"] and claim.get("status") != "retracted":
            claim = {**claim, "status": "retracted", "retired": date.today().isoformat()}
        out.append(claim)
    store.write_claims(source, out)


def stale_sections(root: Path, source: str, withdrawn: list[dict]) -> dict[str, list[str]]:
    """Sections citing a report that appear to state one of its withdrawn claims.

    A paragraph matches a claim when it cites the report, repeats every figure the
    claim states and shares a third of its words. The figure may still occur elsewhere
    in the revised report for another result, so that is not grounds to skip the
    section. Returns section id -> matching withdrawn claim ids. No model call.
    """
    from beril_wiki.check import cited_ids, numbers_in, paragraphs

    wanted = {
        c["id"]: (numbers_in(c["text"]), set(CONTENT_WORD.findall(c["text"].lower())))
        for c in withdrawn
    }
    wanted = {c: (figures, words) for c, (figures, words) in wanted.items() if figures}
    if not wanted:
        return {}
    out: dict[str, list[str]] = {}
    db = index.connect(root)
    try:
        rows = db.execute(
            "SELECT s.id, s.body FROM section_sources ss JOIN sections s ON s.id = ss.section "
            "JOIN pages p ON p.id = s.page WHERE ss.source = ? AND p.kind != 'sources'",
            (source,),
        ).fetchall()
    finally:
        db.close()
    for row in rows:
        hits: list[str] = []
        for par in paragraphs(row["body"]):
            if source not in cited_ids(par):
                continue
            stated = numbers_in(par)
            said = set(CONTENT_WORD.findall(par.lower()))
            for claim, (figures, words) in wanted.items():
                shared = len(words & said) / len(words) if words else 0.0
                if figures <= stated and shared >= 0.3 and claim not in hits:
                    hits.append(claim)
        if hits:
            out[row["id"]] = hits
    return out


def revise(root: Path, source: str, config: Config, launch: Launch | None = None) -> dict:
    """Bring the wiki in line with a revised report, touching only what its changes reach.

    A claim whose quote and surrounding block are unchanged carries forward at no cost.
    Blocks of the report that changed are extracted again, and each section that rests
    on a claim the revision withdrew gets one edit, a hub or entity lead included: a
    withdrawn result is corrected wherever it is stated.
    """
    try:
        with checkout_lock(root):
            return _revise(begin(root, "revise", source, config, launch, "changed"), source)
    except Busy as exc:
        raise Stop(str(exc)) from None


def _revise(runner: Runner, source: str) -> dict:
    store, config, root = runner.store, runner.config, runner.root
    try:
        if "blocks" not in store.sources().get(source, {}):
            raise Stop(
                f"{source} has no block baseline in knowledge/sources.jsonl, so a revision "
                "cannot tell which parts changed; it was read from an older copy of the report"
            )
        mirror_report(store, source)
        carried = runner.step("carry", lambda: carry_forward(store, source))
        under_recheck = [c for c in store.claims(source) if c["id"] in carried["affected"]]
        new_claims = (
            extract(runner, source, carried["changed"], under_recheck) if carried["changed"] else []
        )
        settled = runner.step(
            "settle", lambda: settle(store.claims(source), carried["affected"], new_claims)
        )
        apply_settlement(store, source, settled)
        all_claims = {c["id"]: c for c in store.claims(source)}
        fresh = [all_claims[c] for c in settled["fresh"]]
        withdrawn_claims = [all_claims[c] for c in settled["withdrawn"]]

        def choose() -> dict:
            by_heading: dict[str, list[dict]] = defaultdict(list)
            for claim in fresh:
                by_heading[claim.get("heading", "")].append(claim)
            db = index.connect(root)
            try:
                marks = ",".join("?" * len(settled["withdrawn"])) or "''"
                links = db.execute(
                    f"SELECT page, anchor, claim FROM section_claims WHERE claim IN ({marks}) "
                    "AND anchor != ''",
                    settled["withdrawn"],
                ).fetchall()
            finally:
                db.close()
            per_section: dict[str, list[str]] = defaultdict(list)
            for row in links:
                per_section[f"{row['page']}#{row['anchor']}"].append(row["claim"])
            # Links are inferred for most of the corpus, so a section can state a
            # withdrawn result without being linked to its claim; those are edited too.
            for section, old_ids in stale_sections(root, source, withdrawn_claims).items():
                per_section[section] = sorted(set(per_section[section]) | set(old_ids))
            targets, placed = [], set()
            for section, old_ids in sorted(per_section.items()):
                headings = {all_claims[c].get("heading", "") for c in old_ids}
                offered = [c for h in sorted(headings) for c in by_heading.get(h, [])]
                # A renamed or split heading leaves no match; the editor then sees what
                # the changed parts of the report now say and takes what replaces the old.
                offered = offered or fresh[:15]
                placed |= {c["id"] for c in offered}
                targets.append(
                    {
                        "section": section,
                        "claims": [c["id"] for c in offered],
                        "withdrawn": [all_claims[c] for c in old_ids],
                        "why": "The report was revised where this section's evidence comes from.",
                    }
                )
            rows: list[dict] = []
            # A withdrawn claim known only to sit somewhere on a page: no section could
            # be found for it, so the correction is recorded as owed on that page.
            reached = {
                (t["section"].split("#")[0], c["id"]) for t in targets for c in t["withdrawn"]
            }
            db = index.connect(root)
            try:
                loose = db.execute(
                    f"SELECT page, claim FROM section_claims WHERE claim IN ({marks}) "
                    "AND anchor = ''",
                    settled["withdrawn"],
                ).fetchall()
            finally:
                db.close()
            for row in loose:
                if (row["page"], row["claim"]) not in reached:
                    rows += queue_rows(
                        runner.id, source, row["page"], [row["claim"]], "no section found", True
                    )
            # Every correction is on record as owed before any edit starts, so a run that
            # dies here, or a later revision that supersedes it, cannot lose one. Each
            # row is cleared when its section's edit is accepted.
            for n, target in enumerate(targets):
                owed = [w["id"] for w in target["withdrawn"]]
                why = "revision pending" if n < config.max_sections else "cap"
                rows += queue_rows(runner.id, source, target["section"], owed, why, True)
                if n >= config.max_sections:
                    rows += queue_rows(runner.id, source, target["section"], target["claims"], why)
            unplaced = [c["id"] for c in fresh if c["id"] not in placed]
            rows += queue_rows(runner.id, source, "", unplaced, "queue: new in a revision")
            if rows:
                store.queue(source, rows)
            return {
                "targets": targets[: config.max_sections],
                "over": len(targets[config.max_sections :]),
            }

        # Recorded, so a resumed run edits the sections the first attempt chose.
        chosen = runner.step("targets", choose)
        result = run_targets(runner, source, chosen["targets"], all_claims)
        why = unfinished(runner, result)
        if why:
            return runner.finish("stopped", **result, reason=why)
        records = run_records(
            runner, source, "revise", result, chosen["targets"], settled["withdrawn"]
        )
        result["records"] = records
        why = unfinished(runner, result, records)
        if why:
            return runner.finish("stopped", **result, reason=why)
        record_source(runner, source)
        return runner.finish(
            "done",
            carried=carried["carried"],
            confirmed=len(settled["confirmed"]),
            withdrawn=len(settled["withdrawn"]),
            new_claims=len(fresh),
            changed_blocks=len(carried["changed"]),
            sections_over_cap=chosen["over"],
            **result,
        )
    except Stop as exc:
        return runner.finish("stopped", reason=str(exc))


def refresh(
    root: Path,
    sections: list[str],
    instruction: str,
    config: Config,
    launch: Launch | None = None,
) -> dict:
    """Re-edit named sections for a stated reason. The only way a rule change reaches
    accepted prose, and it runs only when an operator asks. It also settles what is
    queued for those sections: findings to place and corrections still owed."""
    config.check()
    if len(sections) > config.max_sections:
        raise Stop(f"{len(sections)} sections named; --max-sections is {config.max_sections}")
    sections = list(dict.fromkeys(sections))
    try:
        with checkout_lock(root):
            subject = sha256("|".join(sections) + instruction)[:10]
            return _refresh(Runner(root, config, "refresh", subject, launch), sections, instruction)
    except Busy as exc:
        raise Stop(str(exc)) from None


def _refresh(runner: Runner, sections: list[str], instruction: str) -> dict:
    store = runner.store
    try:
        db = index.connect(runner.root)
        try:
            claims_by_id = {r["id"]: dict(r) for r in db.execute("SELECT * FROM claims")}
        finally:
            db.close()
        waiting = store.backlog()
        targets = []
        for section in sections:
            # A correction owed on the page as a whole is offered to each of its sections.
            here = (section, section.split("#")[0])
            rows = [b for b in waiting if b.get("target") in here and b["claim"] in claims_by_id]
            targets.append(
                {
                    "section": section,
                    "claims": [b["claim"] for b in rows if not b.get("withdrawn")],
                    "withdrawn": [claims_by_id[b["claim"]] for b in rows if b.get("withdrawn")],
                    "instruction": instruction,
                }
            )
        result = run_targets(runner, None, targets, claims_by_id)
        for outcome in result["sections"]:
            if outcome["status"] != "accepted":
                continue
            settled: dict[str, set[str]] = defaultdict(set)
            used = set(outcome.get("claims", []))
            for row in waiting:
                # A correction owed on the whole page stays queued: one section's
                # edit does not show the statement is gone from the others. So does a
                # finding the editor declined: it still has no home.
                if row.get("target") != outcome["section"]:
                    continue
                if row.get("withdrawn") or row["claim"] in used:
                    settled[row["source"]].add(row["id"])
            for source, ids in settled.items():
                store.unqueue(source, ids)
        why = unfinished(runner, result)
        if why:
            return runner.finish("stopped", **result, reason=why)
        # A refresh has no report of its own, so only the stages that follow an edited
        # page are owed: a new conflict page, a hub's literature context, figures.
        result["records"] = run_records(
            runner, "", "refresh", result, targets, stages=("conflicts", "literature", "figures")
        )
        why = unfinished(runner, result, result["records"])
        if why:
            return runner.finish("stopped", **result, reason=why)
        return runner.finish("done", **result)
    except Stop as exc:
        return runner.finish("stopped", reason=str(exc))


def describe(result: dict) -> str:
    lines = [f"run {result['run']}: {result['status']}"]
    if result.get("reason"):
        lines.append(f"  {result['reason']}")
    lines.append(f"  {result['tokens']:,} tokens, USD {result['usd']:.2f} reported or estimated")
    for item in result.get("sections", []):
        detail = opening(str(item.get("detail", "")), 90)
        lines.append(f"  {item['status']:<10} {item['section']} {detail}")
    for stage, counts in (result.get("records") or {}).items():
        tally = ", ".join(f"{n} {status}" for status, n in sorted(counts.items()))
        lines.append(f"  {stage:<10} {tally}")
    return "\n".join(lines)
