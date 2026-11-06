"""Shared pieces of the finding, literature-label and research-direction stages.

The stages headlines, novelty and directions each write only their own records, so
the pages Topics and Literature own keep their fingerprints. Their model replies
are JSON, checked here in code before any reviewer reads them.
"""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Callable
from pathlib import Path
from typing import Literal, TypeVar

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

from beril_wiki import compiler as C
from beril_wiki.agentic.prose import Issue, PageFailure, record_salvage
from beril_wiki.agentic.runtime import (
    CARD_EFFORT,
    CONTENT_FLAG,
    CandidateError,
    JobFailed,
    Refused,
    Runtime,
    WorkflowError,
    configured,
    digest,
    file_hash,
    model_policy,
    runtime,
)
from beril_wiki.check import figures_in, prose_only
from beril_wiki.stages.topics import slugify

T = TypeVar("T")
M = TypeVar("M", bound=BaseModel)

SCOPE = "contract/cards.yaml"
DECISIONS = "contract/novelty-decisions.yaml"
# A verifier objection that opens "Issue 3 remains: ..." restates issue 3 of its list.
RESTATED = re.compile(r"^\W*issue\s+#?(\d+)\b", re.I)
RESOLVED = " [restates an issue listed among these notes]"
ITEM = re.compile(r"^(?:[-*]|\d+[.)])\s+(.*)$")


class Scope(BaseModel):
    model_config = ConfigDict(extra="forbid")
    topics: list[str] | Literal["all"] = []
    reports: list[str] | Literal["all"] = []


class Resolved(BaseModel):
    topics: list[str]
    reports: list[str]


def load_scope(root: Path) -> Resolved | None:
    """The topics and reports in scope, or None when the file is absent.

    "all" means every report under wiki/sources and every topic in the curator's
    topic decision, read at each run so new reports join without an edit.
    """
    path = root / SCOPE
    if not path.exists():
        return None
    try:
        scope = Scope.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")) or {})
    except (ValidationError, yaml.YAMLError) as exc:
        raise WorkflowError(f"invalid {SCOPE}: {exc}") from exc
    reports = scope.reports
    if reports == "all":
        reports = sorted(
            p.name.removesuffix("__REPORT.md") for p in (root / "wiki/sources").glob("*__REPORT.md")
        )
    topics = sorted(topic_groups(root)) if scope.topics == "all" else scope.topics
    return Resolved(topics=topics, reports=reports)


def require_runtime(stage: str) -> bool:
    """These stages run only under the agentic runtime: they key cached jobs, record
    failures and check vendors through it, which the legacy CBORG path cannot."""
    if configured():
        return True
    print(f"stages.{stage}: needs the agentic runtime (agentic run); nothing written")
    return False


def source_path(root: Path, sid: str) -> Path:
    return root / "wiki" / "sources" / f"{sid}__REPORT.md"


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


def topic_concepts(root: Path, slug: str) -> list[str]:
    """The concept stems a topic hub gathers, from the curator's topic decision."""
    path = root / "state" / "curator-topics.json"
    if not path.exists():
        return []
    groups = json.loads(path.read_text(encoding="utf-8")).get("groups", [])
    return next((sorted(g["concepts"]) for g in groups if slugify(g["title"]) == slug), [])


def bullets(text: str, heading: re.Pattern[str]) -> list[str]:
    """List items under every heading the pattern matches, continuation lines joined."""
    out: list[str] = []
    lines = text.splitlines()
    inside = False
    level = 0
    for line in lines:
        h = re.match(r"^(#{1,6})\s+(.*)$", line)
        if h:
            if inside and len(h.group(1)) <= level:
                inside = False
            if not inside and heading.search(h.group(2)):
                inside, level = True, len(h.group(1))
            continue
        if not inside:
            continue
        m = ITEM.match(line.strip()) if line[:1] not in (" ", "\t") else None
        if m:
            out.append(m.group(1).strip())
        elif line.strip() and out and line[:1] in (" ", "\t"):
            out[-1] += " " + line.strip()
    return out


SRC = re.compile(r"\[src:\s*([^\]]+)\]")
FORWARD = re.compile(r"^(Open Directions|Resolving Work)$")
REPORT_FORWARD = re.compile(r"Future Directions|Experimental Recommendations|Next Steps", re.I)
DIGESTS = ("discoveries", "pitfalls")
# Work that repeats, corrects or tidies an existing analysis. It belongs to the people
# who maintain the reports, not on the pages a scientist reads to choose a project.
REANALYSIS = re.compile(
    r"\b(?:re-?(?:comput|run|analy[sz]|count|deriv|estimat|scor|test|fit|build|process"
    r"|annotat|classif|examin|evaluat|quantif|check|tabulat)\w*|recount\w*|reconcil\w*"
    r"|audit\w*|harmoni[sz]\w*|standardi[sz]\w*|repeat\w*|trace\s+the|correct\s+the"
    r"|align\s+(?:the\s+)?(?:denominator|threshold|definition|count)s?)\b",
    re.I,
)


def is_reanalysis(text: str) -> bool:
    """Whether a proposal's opening clause asks to redo or tidy existing work."""
    lead = " ".join(re.sub(r"\*\*", "", text).split()[:14])
    return REANALYSIS.search(lead) is not None


def projects_in(text: str) -> list[str]:
    out: list[str] = []
    for tag in SRC.finditer(text):
        for part in re.split(r"[,;]", tag.group(1)):
            sid = re.sub(r"__REPORT$", "", part.strip())
            if sid and sid not in out:
                out.append(sid)
    return out


def forward_bullets(root: Path, topic: str, reports: list[str]) -> list[dict]:
    """Every forward-looking bullet the topic's pages and in-scope reports carry."""
    concepts = topic_concepts(root, topic)
    items: list[dict] = []

    def add(page: str, section: str, text: str, projects: list[str]) -> None:
        items.append(
            {"id": f"b{len(items)}", "page": page, "section": section, "text": text}
            | {"projects": projects or projects_in(text)}
        )

    for stem in concepts:
        path = root / "wiki/concepts" / f"{stem}.md"
        if path.exists():
            for text in bullets(path.read_text(encoding="utf-8"), FORWARD):
                add(f"concepts/{stem}", "Open Directions", text, [])
    for path in sorted((root / "wiki/conflicts").glob("conflict--*.md")):
        if path.stem.split("--")[1] in concepts:
            body = path.read_text(encoding="utf-8")
            sides = projects_in(body)
            for text in bullets(body, FORWARD):
                add(f"conflicts/{path.stem}", "Resolving Work", text, projects_in(text) or sides)
    for sid in reports:
        path = source_path(root, sid)
        if path.exists():
            for text in bullets(path.read_text(encoding="utf-8"), REPORT_FORWARD):
                add(f"sources/{sid}__REPORT", "Future Directions", text, [sid])
    return items


def collections(root: Path) -> dict[str, str]:
    """Collection page stem -> its title, from wiki/data/."""
    out = {}
    for path in sorted((root / "wiki/data").glob("*.md")):
        if path.stem != "index":
            m = re.search(r"^# +(.+)$", path.read_text(encoding="utf-8"), re.M)
            out[path.stem] = m.group(1).strip() if m else path.stem
    return out


def collection_id(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def main_topics(
    sid: str, groups: dict[str, set[str]], concept_cites: dict[str, set[str]]
) -> list[str]:
    """The topics a report mainly feeds: those whose concepts cite it at least half
    as often as its most-citing topic does. Counting every topic with one citing
    concept put most reports in most topics, so topic filters selected nothing."""
    counts = {
        slug: sum(sid in concept_cites.get(c, set()) for c in concepts)
        for slug, concepts in groups.items()
    }
    top = max(counts.values(), default=0)
    return sorted(slug for slug, n in counts.items() if n and 2 * n >= top)


def topic_groups(root: Path) -> dict[str, set[str]]:
    path = root / "state" / "curator-topics.json"
    groups = json.loads(path.read_text(encoding="utf-8")).get("groups", []) if path.exists() else []
    return {slugify(g["title"]): set(g["concepts"]) for g in groups}


def concept_citations(root: Path) -> dict[str, set[str]]:
    return {
        p.stem: set(projects_in(p.read_text(encoding="utf-8", errors="replace")))
        for p in (root / "wiki/concepts").glob("*.md")
    }


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
