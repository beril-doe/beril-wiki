"""Extract evidence once and integrate a source batch once per destination page."""

from __future__ import annotations

import json
import re
import shutil
import threading
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, ValidationError

from beril_wiki import compiler as C
from beril_wiki.agentic.runtime import (
    CandidateError,
    Runtime,
    WorkflowError,
    atomic_json,
    digest,
    file_hash,
)
from beril_wiki.check import cited_ids, paragraphs
from beril_wiki.stages.consolidate import body_src_ids, load_decisions, page_numbers, repoint_links


class Finding(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    quote: str = Field(min_length=1)
    start: int = Field(ge=0)
    end: int = Field(gt=0)
    claim: str = Field(min_length=1, max_length=1000)
    kind: Literal["finding", "caveat", "null", "entity", "figure"]


class Evidence(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    findings: list[Finding]
    empty_reason: str


class PageJob(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    path: str
    title: str = Field(min_length=1)
    type: str
    sources: list[str]
    reason: str = Field(min_length=1)
    merge_from: list[str] = Field(default_factory=list)


class Coverage(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    evidence: str
    concepts: list[str]
    summary_only: str


class Plan(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    pages: list[PageJob]
    coverage: list[Coverage]


# Extraction answers are structured (quote, claim), so each review narrows the objections;
# three corrections are the same allowance derived pages get before salvage.
EXTRACTION_ATTEMPTS = 4


def chunks(text: str, size: int = 16_000) -> Iterator[tuple[int, int]]:
    if size <= 0:
        raise ValueError("chunk size must be positive")
    for start in range(0, len(text), size):
        yield start, min(start + size, len(text))


def validate_evidence(text: str, start: int, end: int, obj: dict) -> Evidence:
    try:
        evidence = Evidence.model_validate(obj)
    except ValidationError as exc:
        # A schema violation is the model's mistake, not the run's: name it and let the
        # correction round fix it, as an invalid plan or page candidate already does.
        raise CandidateError(str(exc)) from exc
    if not evidence.findings and not evidence.empty_reason.strip():
        raise CandidateError("empty extraction must explain why no scientific evidence exists")
    for index, finding in enumerate(evidence.findings):
        if text[finding.start : finding.end] != finding.quote:
            # Offsets are advisory: the quote is located verbatim, nearest the model's guess.
            pattern = re.escape(finding.quote)
            hits = [m.start() + start for m in re.finditer(pattern, text[start:end])]
            if not hits:
                raise CandidateError(
                    f"finding {index} quote is not verbatim source text: {finding.quote[:160]!r}"
                )
            finding.start = min(hits, key=lambda hit: abs(hit - finding.start))
            finding.end = finding.start + len(finding.quote)
        if not (start <= finding.start < finding.end <= end):
            raise CandidateError(f"finding {index} quote lies outside offsets {start}-{end}")
    return evidence


class EvidenceAcceptor:
    """Validate one extraction chunk; review it once, then verify each repair.

    The reviewer sees the host-located findings the chunk owns, so offsets and
    overlap are never objections. Its first verdict is the open review; after a
    repair it is only asked whether those objections are closed."""

    def __init__(
        self, agent: Runtime, messages: list[dict], step: str, text: str, start: int, end: int
    ) -> None:
        self.agent, self.messages, self.step = agent, messages, step
        self.text, self.start, self.end = text, start, end
        self.pending: list[str] = []
        self.evidence: Evidence | None = None

    def __call__(self, raw: str) -> Evidence:
        evidence = validate_evidence(self.text, self.start, len(self.text), C.parse_json_reply(raw))
        # A quote located in the overlap belongs to the next chunk, which starts there.
        evidence.findings = [f for f in evidence.findings if f.start < self.end]
        self.evidence = evidence
        candidate = evidence.model_dump_json()
        if not self.pending:
            try:
                self.agent.review(self.messages, candidate, self.step)
            except CandidateError as exc:
                self.pending = exc.objections
                raise
        else:
            self.pending = self.agent.verify(self.messages, candidate, self.pending, self.step)
            if self.pending:
                raise CandidateError(
                    f"objections still open on {self.step}: {json.dumps(self.pending)}",
                    self.pending,
                )
        return evidence


def changed_sources(root: Path) -> list[str]:
    """Adopt byte-identical existing sources; never adopt source membership alone."""
    staged = {p.name: p for p in (root / "staging").glob("*.md")}
    removed = {p.name for p in (root / "wiki/sources").glob("*.md")} - staged.keys()
    if removed:
        raise WorkflowError(f"source deletion requires explicit retraction: {sorted(removed)}")
    changed = []
    success_path = root / "state/hashes.json"
    success = json.loads(success_path.read_text(encoding="utf-8")) if success_path.exists() else {}
    for name, path in sorted(staged.items()):
        old = root / "wiki/sources" / name
        if not old.exists() or not (root / "wiki/summaries" / name).exists():
            changed.append(name)
        elif file_hash(old) != file_hash(path) or success.get(name) != file_hash(path):
            changed.append(name)
    return changed


def sid_for(name: str) -> str:
    return re.sub(r"__REPORT$", "", Path(name).stem)


def page_path(value: str) -> str:
    if not re.fullmatch(r"(?:concepts|entities|summaries)/[a-zA-Z0-9_-]+\.md", value):
        raise CandidateError(f"invalid page destination {value!r}")
    return value


def reconstruct(old: str, candidate: dict) -> str:
    if candidate.get("base_hash") != digest(old):
        raise CandidateError("candidate base hash is stale")
    full = candidate.get("content")
    edits = candidate.get("edits", [])
    if full is not None:
        if not isinstance(full, str) or edits or (old and not candidate.get("rewrite_reason")):
            raise CandidateError("full rewrite requires a reason and cannot include patches")
        return full
    if not old or not isinstance(edits, list):
        raise CandidateError("new page requires full content")
    if not edits and not candidate.get("no_change_reason"):
        raise CandidateError("unchanged candidate requires a no_change_reason")
    spans = []
    for edit in edits:
        if not isinstance(edit, dict):
            raise CandidateError("patch must be an object")
        anchor, replacement = edit.get("old"), edit.get("new")
        if not isinstance(anchor, str) or not anchor or old.count(anchor) != 1:
            raise CandidateError("patch anchor is missing or ambiguous")
        if not isinstance(replacement, str):
            raise CandidateError("replacement must be text")
        at = old.index(anchor)
        spans.append((at, at + len(anchor), replacement))
    spans.sort()
    if any(a[1] > b[0] for a, b in zip(spans, spans[1:], strict=False)):
        raise CandidateError("patch anchors overlap")
    for start, end, replacement in reversed(spans):
        old = old[:start] + replacement + old[end:]
    return old


def candidate_json(raw: str) -> dict:
    try:
        return C.parse_json_reply(raw)
    except ValueError as exc:
        raise CandidateError(str(exc)) from exc


def validate_candidate(
    root: Path,
    path: str,
    job: PageJob,
    candidate: dict,
    revised: set[str],
    targets: set[str],
    *,
    assigned: list[dict] | None = None,
) -> str:
    """Reconstruct and check a bound candidate without changing any files."""
    page_path(path)
    if path != job.path or path.removesuffix(".md") not in targets:
        raise CandidateError("candidate destination is not in the bound plan")
    target = root / "wiki" / path
    old = C.parse_fm(target.read_text(encoding="utf-8"))[1] if target.exists() else ""
    absorbed = [
        C.parse_fm((root / "wiki" / page_path(p)).read_text(encoding="utf-8"))[1]
        for p in job.merge_from
    ]
    sources = C.load_sources(root)
    body = reconstruct(old, candidate).strip()
    description = candidate.get("description")
    if not isinstance(description, str) or not description.strip():
        raise CandidateError("candidate needs a nonempty description")
    if body.startswith("---"):
        raise CandidateError("agent emitted host-owned frontmatter")
    violations = C.validate_page(
        body, sources, targets, require_slots=path.startswith("summaries/")
    )
    if path.startswith("concepts/") and "## Open Directions" not in body:
        violations.append("concept lacks Open Directions")
    if violations:
        raise CandidateError(f"{path}: {violations}")
    retained = "\n\n".join(par for page in [old, *absorbed] for par in paragraphs(page))
    # A co-cited paragraph may contain unchanged evidence. Retain its quantities
    # conservatively; only exclusively revised-source paragraphs are exempt.
    unchanged_evidence = "\n\n".join(
        par for par in paragraphs(retained) if not cited_ids(par) or set(cited_ids(par)) - revised
    )
    if not body_src_ids(retained) - revised <= body_src_ids(body) or not page_numbers(
        unchanged_evidence
    ) <= page_numbers(body):
        raise CandidateError(f"{path}: candidate loses unchanged citations or quantities")
    expected = {f["id"]: f["source"] for f in assigned or []}
    accounted = candidate.get("accounted_evidence", {})
    if not isinstance(accounted, dict) or set(accounted) != set(expected):
        raise CandidateError(f"{path}: assigned evidence IDs must be accounted for exactly")
    cited_passages = paragraphs(body)
    for eid, source in expected.items():
        passage = accounted[eid]
        if (
            not isinstance(passage, str)
            or passage not in cited_passages
            or source not in cited_ids(passage)
        ):
            raise CandidateError(f"{path}: assigned evidence {eid} needs an exact cited paragraph")
    return body


def briefs(root: Path) -> list[dict]:
    result = []
    for group in ("concepts", "entities", "summaries"):
        for p in sorted((root / "wiki" / group).glob("*.md")):
            fm, body = C.parse_fm(p.read_text(encoding="utf-8"))
            result.append(
                {
                    "path": f"{group}/{p.name}",
                    "description": fm.get("description", ""),
                    "type": fm.get("type", ""),
                    "sources": sorted(body_src_ids(body)),
                    "length": len(p.read_text(encoding="utf-8")),
                    "headings": re.findall(r"^## .+$", body, re.M),
                }
            )
    return result


def planning_batches(findings: list[dict], limit: int = 100_000) -> list[list[dict]]:
    """Partition compact evidence; quotes stay in saved records and original sources."""
    batches: list[list[dict]] = [[]]
    size = 0
    for finding in findings:
        item = {k: v for k, v in finding.items() if k != "quote"}
        weight = len(json.dumps(item).encode())
        if weight > limit:
            raise WorkflowError("one evidence record exceeds the planning budget")
        if batches[-1] and size + weight > limit:
            batches.append([])
            size = 0
        batches[-1].append(item)
        size += weight
    return batches


def plan_jobs(
    root: Path,
    plan: Plan,
    findings: list[dict],
    sources: dict[str, str],
    listing: list[dict],
    names: list[str],
) -> tuple[dict[str, PageJob], dict[str, str]]:
    """Validate cumulative coverage and group each destination before generation."""
    jobs: dict[str, PageJob] = {}
    decisions = load_decisions(root)
    retired = {f"concepts/{row['from']}.md" for row in decisions["renames"]}
    retired |= {f"concepts/{row['loser']}.md" for row in decisions["merges"]}
    for job in plan.pages:
        page_path(job.path)
        if job.path in retired:
            raise CandidateError(f"planner recreated a retired concept: {job.path}")
        if not set(job.sources) <= sources.keys() or not job.sources:
            raise CandidateError(f"unknown or missing planned sources: {job.path}")
        if job.path.startswith("entities/") and job.type.lower() not in C.ENTITY_TYPES:
            raise CandidateError(f"invalid entity type: {job.type}")
        if job.merge_from and not job.path.startswith("concepts/"):
            raise CandidateError(f"only concepts can have merge inputs: {job.path}")
        if job.path in jobs:
            previous = jobs[job.path]
            if previous.type.lower() != job.type.lower():
                raise CandidateError(f"conflicting duplicate page jobs: {job.path}")
            previous.sources = sorted(set(previous.sources + job.sources))
            previous.merge_from = sorted(set(previous.merge_from + job.merge_from))
            previous.reason += "; " + job.reason
        else:
            jobs[job.path] = job.model_copy(deep=True)
    covered = [c.evidence for c in plan.coverage]
    if len(covered) != len(set(covered)) or set(covered) != {f["id"] for f in findings}:
        raise CandidateError("planner omitted or duplicated evidence coverage")
    finding_sources = {f["id"]: f["source"] for f in findings}
    for item in plan.coverage:
        if not item.concepts and not item.summary_only.strip():
            raise CandidateError("evidence lacks concept coverage or summary-only justification")
        if any(p not in jobs or not p.startswith("concepts/") for p in item.concepts):
            raise CandidateError("evidence coverage names an unscheduled concept")
        for path in item.concepts:
            jobs[path].sources = sorted(set(jobs[path].sources) | {finding_sources[item.evidence]})
    changed = {sid_for(name) for name in names}
    for item in listing:
        affected = set(item["sources"]) & changed
        planned_losers = {loser for j in jobs.values() for loser in j.merge_from}
        if affected and item["path"] in planned_losers:
            survivor = next(j for j in jobs.values() if item["path"] in j.merge_from)
            survivor.sources = sorted(set(survivor.sources) | affected)
        elif affected and item["path"] not in jobs:
            jobs[item["path"]] = PageJob(
                path=item["path"],
                title=Path(item["path"]).stem,
                type=str(item["type"]),
                sources=sorted(affected),
                reason="Recheck every claim citing the revised source version",
            )
    for name in names:
        path = f"summaries/{name}"
        jobs[path] = PageJob(
            path=path,
            title=Path(name).stem,
            type="Summary",
            sources=[sid_for(name)],
            reason="Summarize all findings, caveats/nulls; end with Slots Into",
        )

    losers = {}
    for job in jobs.values():
        for loser in job.merge_from:
            page_path(loser)
            if (
                not loser.startswith("concepts/")
                or not job.path.startswith("concepts/")
                or loser == job.path
                or loser in losers
                or loser in jobs
                or not (root / "wiki" / loser).is_file()
            ):
                raise CandidateError(f"conflicting or invalid merge loser: {loser}")
            losers[loser] = job.path
    return jobs, losers


_GAP_LOCK = threading.Lock()


def record_extraction_gap(store: Path, step: str, objections: list[str]) -> None:
    """Evidence a chunk never captured; this is where a human finds what is missing."""
    path = store / "extraction-gaps.json"
    with _GAP_LOCK:
        data = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        data[step] = objections
        atomic_json(path, data)


def assemble_evidence(
    root: Path, tasks: list[tuple[str, str, int, int]], extracted: dict[int, Evidence]
) -> tuple[list[dict], list[dict]]:
    """Findings and coverage in task order, never completion order.

    Evidence ids and the manifest digest key the work that follows, so a parallel
    stage must produce exactly what the sequential one did."""
    findings: list[dict] = []
    manifest: list[dict] = []
    for index, (name, text, start, end) in enumerate(tasks):
        evidence = extracted[index]
        ids = []
        for position, item in enumerate(evidence.findings):
            eid = f"{sid_for(name)}:{start}:{position}"
            ids.append(eid)
            findings.append(item.model_dump() | {"id": eid, "source": sid_for(name)})
        manifest.append(
            {
                "source": name,
                "sha256": file_hash(root / "staging" / name),
                "start": start,
                "end": end,
                "context_end": min(end + 1000, len(text)),
                "evidence": ids,
                "empty_reason": evidence.empty_reason,
            }
        )
    return findings, manifest


def compile_batch(root: Path, agent: Runtime, names: list[str]) -> None:
    if not names:
        return
    sources = C.load_sources(root)
    revised = {
        sid_for(name)
        for name in names
        if (root / "wiki/sources" / name).exists()
        and file_hash(root / "staging" / name) != file_hash(root / "wiki/sources" / name)
    }
    tasks: list[tuple[str, str, int, int]] = []
    for name in names:
        text = (root / "staging" / name).read_text(encoding="utf-8", errors="replace")
        if not text.strip():
            raise WorkflowError(f"empty source {name}")
        tasks.extend((name, text, start, end) for start, end in chunks(text))

    def extract_chunk(agent: Runtime, task: tuple[str, str, int, int]) -> Evidence:
        name, text, start, end = task
        context_end = min(end + 1000, len(text))
        instruction = (
            "Extract reusable scientific findings, caveats, null/negative results, named "
            "entities, and figure references. Include exact verbatim supporting quotes, "
            "preserving numbers, units, denominators and uncertainty, with your best GLOBAL "
            "character offsets; the host locates each quote exactly and rejects only "
            "quotes that are not verbatim source text, so never omit evidence over offsets. "
            "Quotes must start in the ownership range and may end in the supplied overlap. "
            "Retrieve an intact passage if a sentence extends beyond the overlap. "
            "Do not silently omit evidence. You have at most "
            f"{max(1, agent.config.get('max_turns', 6) - 1)} tool turns and 100KB of "
            "reads in total; always finish with the JSON. "
            f"Return JSON matching {json.dumps(Evidence.model_json_schema())}.\n"
            + json.dumps(
                {
                    "source": name,
                    "start": start,
                    "end": end,
                    "context_end": context_end,
                    "length": len(text),
                    "text": text[start:context_end],
                }
            )
        )
        messages = [{"role": "user", "content": instruction}]
        step = f"extract/{name}/{start}"
        acceptor = EvidenceAcceptor(agent, messages, step, text, start, end)
        try:
            return agent.generate(messages, step, acceptor, attempts=EXTRACTION_ATTEMPTS)
        except CandidateError as exc:
            # Corrections are spent and the quotes that are here are valid; what the
            # reviewer still wants is evidence the model would not add. Keep the chunk
            # and record the gap, rather than ending a compilation over one chunk of
            # many. A page failure is recorded the same way and the stage continues.
            if acceptor.evidence is None or not acceptor.evidence.findings:
                raise
            record_extraction_gap(agent.store, step, acceptor.pending or [str(exc)])
            return acceptor.evidence

    # Chunks are independent, so they fan out; each worker needs its own Runtime because
    # a ledger connection belongs to one thread. Results are assembled in task order, so
    # evidence ids and the manifest digest do not depend on which chunk finished first.
    # The agent's own config, not the environment: integration runs in the parent
    # process, where BERIL_AGENTIC_CONFIG is set only for the stage subprocesses.
    count = int(agent.config.get("workers", 1))
    if count > 1:

        def extract_in_worker(task: tuple[str, str, int, int]) -> Evidence:
            # Built here, not at submit time: a ledger connection may only be used by
            # the thread that opened it, and submitting from the main thread opens it there.
            return extract_chunk(Runtime(agent.config), task)

        with ThreadPoolExecutor(max_workers=count) as pool:
            pending = {pool.submit(extract_in_worker, task): i for i, task in enumerate(tasks)}
            extracted = {pending[done]: done.result() for done in as_completed(pending)}
    else:
        extracted = {i: extract_chunk(agent, task) for i, task in enumerate(tasks)}

    findings, extraction_manifest = assemble_evidence(root, tasks, extracted)
    evidence_dir = agent.store / "evidence"
    evidence_dir.mkdir(exist_ok=True)
    (evidence_dir / f"{digest(extraction_manifest)}.json").write_text(
        json.dumps({"coverage": extraction_manifest, "findings": findings}, indent=2)
    )
    listing = briefs(root)
    all_findings = findings
    plan = Plan(pages=[], coverage=[])
    planned_findings: list[dict] = []
    for index, findings in enumerate(planning_batches(all_findings)):
        planning = [
            {
                "role": "user",
                "content": "Plan one integration batch, grouping changes by destination. "
                "Extend rather than "
                "duplicate concepts. Include missing concept coverage and thin-concept back-merge "
                "from old summaries, canonical entities, and consolidation of the same evidence. "
                "Read complete pages/source passages when briefs do not establish this. Preserve "
                "contradictions under Tensions; end concepts with Open Directions. Only concepts "
                "can have merge_from; code resolves entity identity separately. "
                "Never recreate retired identities in the manifest. Give every evidence ID "
                "one coverage entry, naming scheduled concept paths or a concrete reason it "
                "belongs only in its summary. Every page needs sources and a concrete "
                "change rationale. "
                "Sources may include older projects when actual evidence supports a back-merge. "
                "Entries marked planned are upcoming destinations, not files yet; extend them "
                "rather than creating aliases. "
                f"Return JSON matching {json.dumps(Plan.model_json_schema())}.\n"
                + json.dumps(
                    {
                        "changed": names,
                        "findings": findings,
                        "existing": listing,
                        "identity_decisions": (root / "contract/concept-decisions.yaml").read_text(
                            encoding="utf-8"
                        )
                        if (root / "contract/concept-decisions.yaml").exists()
                        else "",
                    }
                ),
            }
        ]
        planned_findings.extend(findings)

        def accept_plan(raw: str) -> Plan:
            try:
                partial = Plan.model_validate(candidate_json(raw))
            except ValidationError as exc:
                raise CandidateError(str(exc)) from exc
            combined = Plan(
                pages=plan.pages + partial.pages, coverage=plan.coverage + partial.coverage
            )
            plan_jobs(root, combined, planned_findings, sources, listing, names)
            return partial

        partial = agent.generate(planning, f"batch/plan/{index}", accept_plan)
        plan.pages.extend(partial.pages)
        plan.coverage.extend(partial.coverage)
        known_paths = {item["path"] for item in listing}
        listing.extend(
            {
                "path": job.path,
                "description": job.reason,
                "type": job.type,
                "sources": job.sources,
                "planned": True,
            }
            for job in partial.pages
            if job.path not in known_paths
        )
    findings = all_findings
    jobs, losers = plan_jobs(root, plan, findings, sources, listing, names)
    targets = (C.wikilink_targets(root) | {p.removesuffix(".md") for p in jobs}) - {
        p.removesuffix(".md") for p in losers
    }
    (agent.store / "last-plan.json").write_text(
        json.dumps(
            {
                "pages": [j.model_dump() for j in jobs.values()],
                "coverage": [c.model_dump() for c in plan.coverage],
            },
            indent=2,
        )
    )
    for path, job in sorted(jobs.items()):
        target = root / "wiki" / path
        fm, old = C.parse_fm(target.read_text(encoding="utf-8")) if target.exists() else ({}, "")
        absorbed = {
            p: C.parse_fm((root / "wiki" / p).read_text(encoding="utf-8"))[1]
            for p in job.merge_from
        }
        relevant = [f for f in findings if f["source"] in job.sources]
        relevant_ids = {f["id"] for f in relevant}
        coverage = [
            c.model_dump()
            for c in plan.coverage
            if path in c.concepts or (path.startswith("summaries/") and c.evidence in relevant_ids)
        ]
        assigned_ids = {c["evidence"] for c in coverage}
        assigned = [f for f in relevant if f["id"] in assigned_ids]
        task = [
            {
                "role": "user",
                "content": "Apply the planned scientific change once, "
                "integrating assigned evidence. "
                "Preserve claims, citation IDs, exact quantities, caveats and contradictions; "
                "correct claims invalidated by a revised source. Retrieve original evidence "
                "for old sources and whenever support is unclear. Call validate_candidate "
                "on your JSON before returning it. A source ID maps to "
                "staging/<id>__REPORT.md "
                "except discoveries.md and pitfalls.md. No YAML. Use unique exact anchored patches "
                "for existing pages; full content is allowed for new pages or justified "
                "restructuring. "
                "Keep summaries complete and end with Slots Into linking planned concepts. "
                'Return JSON {"base_hash": "...", "description": "one sentence", '
                '"edits": [{"old": "exact anchor", "new": "replacement"}]} or replace edits with '
                '"content" and "rewrite_reason".\n'
                'If no edit is warranted, supply "no_change_reason" explaining the recheck.\n'
                'Also return "accounted_evidence": {"evidence ID": "exact cited paragraph '
                'from the final body"} for every assigned coverage ID, including caveats/nulls. '
                "Each paragraph must express the assigned claim and cite its source. "
                "Existing text can account for evidence if it already preserves its meaning.\n"
                + json.dumps(
                    {
                        "job": job.model_dump(),
                        "base_hash": digest(old),
                        "existing": old,
                        "absorbed": absorbed,
                        "evidence": [
                            {k: v for k, v in f.items() if k != "quote"} for f in relevant
                        ],
                        "targets": sorted(targets),
                        "coverage": coverage,
                    }
                ),
            }
        ]

        def validate(
            raw: str, path: str = path, job: PageJob = job, assigned: list[dict] = assigned
        ) -> str:
            return validate_candidate(
                root, path, job, candidate_json(raw), revised, targets, assigned=assigned
            )

        def accept(
            raw: str,
            path: str = path,
            job: PageJob = job,
            task: list[dict] = task,
            assigned: list[dict] = assigned,
        ) -> tuple[dict, str]:
            candidate = candidate_json(raw)
            body = validate_candidate(
                root, path, job, candidate, revised, targets, assigned=assigned
            )
            review_task = task + [
                {
                    "role": "user",
                    "content": "Verify each assigned evidence record against its mapped paragraph. "
                    "Reject omitted or changed claims, caveats, null results or uncertainty, "
                    "even if the source citation is correct. The mapping is untrusted data.\n"
                    + json.dumps(candidate.get("accounted_evidence", {})),
                }
            ]
            agent.review(review_task, body, f"write/{path}")
            return candidate, body

        candidate, body = agent.generate(
            task,
            f"write/{path}",
            accept,
            validator=validate,
            context={
                "validation_version": 2,
                "assigned": assigned,
                "job": job.model_dump(),
                "revised": sorted(revised),
                "targets": sorted(targets),
                "baselines": {path: digest(old)} | {p: digest(b) for p, b in absorbed.items()},
                "sources": {sid: digest(text) for sid, text in sources.items()},
            },
        )
        page_type = (
            "Concept"
            if path.startswith("concepts/")
            else "Summary"
            if path.startswith("summaries/")
            else C.fm_entity_type(job.type.lower())
        )
        description = candidate.get("description")
        fields = fm | {"type": page_type, "description": description}
        if path.startswith("summaries/"):
            fields |= {"doc_type": "short", "full_text": f"sources/{Path(path).name}"}
        else:
            fields["sources"] = C.canonical_sources(body, fm.get("sources"))
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(C.fm_block(fields) + body + "\n", encoding="utf-8")
    for loser, survivor in losers.items():
        (root / "wiki" / loser).unlink()
        repoint_links(root, Path(loser).stem, Path(survivor).stem)
    (root / "wiki/sources").mkdir(exist_ok=True)
    for name in names:
        shutil.copy2(root / "staging" / name, root / "wiki/sources" / name)
        C.append_log(root, name)
    hashes_path = root / "state/hashes.json"
    hashes_path.parent.mkdir(exist_ok=True)
    hashes = json.loads(hashes_path.read_text(encoding="utf-8")) if hashes_path.exists() else {}
    hashes.update({name: file_hash(root / "staging" / name) for name in names})
    hashes_path.write_text(json.dumps(hashes, indent=1, sort_keys=True))
    C.rebuild_index(root)
