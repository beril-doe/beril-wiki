"""Offline checks for bounded batch repairs and authoritative candidate validation."""

import json

import pytest

from beril_wiki.agentic import batch
from beril_wiki.agentic.runtime import CandidateError, Runtime, WorkflowError, digest

OLD = "# Yield\n\nYield was 42%. [src: a]\n\n## Open Directions\n\nRepeat measurements."
LOSS = OLD.replace("42%", "measured")


def setup_batch(tmp_path, monkeypatch, *, bad_writes=0, bad_plan=False):
    for folder in ("staging", "wiki/sources", "wiki/concepts", "jobs", "contract"):
        (tmp_path / folder).mkdir(parents=True)
    for folder in ("staging", "wiki/sources"):
        (tmp_path / folder / "a__REPORT.md").write_text("Yield was 42%.")
    (tmp_path / "wiki/concepts/yield.md").write_text(OLD)
    agent = Runtime(
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "jobs"),
            run="test",
            max_tokens=1000,
            max_jobs=30,
            reserve_tokens=10,
        )
    )
    calls, reviews = [], []
    job = batch.PageJob(
        path="concepts/yield.md",
        title="Yield",
        type="Concept",
        sources=["a"],
        reason="Recheck yield",
    )

    def reply(messages, step):
        calls.append((step, messages))
        if step.startswith("extract/"):
            return json.dumps(
                {
                    "findings": [
                        {
                            "quote": "Yield was 42%.",
                            "start": 0,
                            "end": 14,
                            "claim": "Yield was 42%.",
                            "kind": "finding",
                        }
                    ],
                    "empty_reason": "",
                }
            )
        if step.startswith("batch/plan/"):
            coverage = [{"evidence": "a:0:0", "concepts": [job.path], "summary_only": ""}]
            return json.dumps(
                {
                    "pages": [job.model_dump()],
                    "coverage": [] if bad_plan and not step.endswith("/repair") else coverage,
                }
            )
        payload = json.loads(messages[0]["content"].split("\n")[-1])
        body = OLD
        if step.startswith("write/concepts/"):
            attempt = sum(s.startswith("write/concepts/") for s, _ in calls)
            if attempt <= bad_writes:
                body = LOSS
        else:
            body = "# Yield\n\nYield was 42%. [src: a]\n\n## Slots Into\n\n[[concepts/yield]]"
        return json.dumps(
            {
                "base_hash": payload["base_hash"],
                "description": "Yield evidence",
                "content": body,
                "rewrite_reason": "Recheck evidence",
                "accounted_evidence": {
                    c["evidence"]: body.split("\n\n")[1] for c in payload["coverage"]
                },
            }
        )

    monkeypatch.setattr(agent, "ask", reply)
    monkeypatch.setattr(agent, "review", lambda task, raw, step: reviews.append((step, raw)))
    return agent, calls, reviews, job


def test_writer_repairs_lost_quantity_once(tmp_path, monkeypatch):
    agent, calls, reviews, _ = setup_batch(tmp_path, monkeypatch, bad_writes=1)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert [s for s, _ in calls if s.startswith("write/concepts/")] == [
        "write/concepts/yield.md",
        "write/concepts/yield.md/repair",
    ]
    repair = next(m for s, m in calls if s.endswith("yield.md/repair"))
    assert "unchanged citations or quantities" in json.dumps(repair)
    assert "42%" in (tmp_path / "wiki/concepts/yield.md").read_text()
    assert [(s, b) for s, b in reviews if s.startswith("write/concepts/")] == [
        ("write/concepts/yield.md", OLD)
    ]


def test_repeated_quantity_loss_stops_without_acceptance(tmp_path, monkeypatch):
    agent, calls, reviews, _ = setup_batch(tmp_path, monkeypatch, bad_writes=2)
    with pytest.raises(WorkflowError, match="unchanged citations or quantities"):
        batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(s.startswith("write/concepts/") for s, _ in calls) == 2
    assert (tmp_path / "wiki/concepts/yield.md").read_text() == OLD
    assert not (tmp_path / "state/hashes.json").exists()
    assert not any(s.startswith("write/") for s, _ in reviews)


def test_rejected_extraction_receives_one_correction(tmp_path, monkeypatch):
    agent, calls, reviews, _ = setup_batch(tmp_path, monkeypatch)
    original = agent.review

    def strict(task, raw, step):
        original(task, raw, step)
        if step.startswith("extract/") and sum(s == step for s, _ in reviews) == 1:
            raise CandidateError("claim includes text outside its quoted span")

    monkeypatch.setattr(agent, "review", strict)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert [s for s, _ in calls if s.startswith("extract/")] == [
        "extract/a__REPORT.md/0",
        "extract/a__REPORT.md/0/repair",
    ]
    repair = next(m for s, m in calls if s == "extract/a__REPORT.md/0/repair")
    assert "outside its quoted span" in repair[-1]["content"]
    assert (tmp_path / "wiki/summaries/a__REPORT.md").exists()


def test_overlap_findings_are_left_to_the_next_chunk():
    reviews = []
    text = "Owned sentence. Overlap sentence."
    raw = json.dumps(
        {
            "findings": [
                {
                    "quote": "Owned sentence.",
                    "start": 0,
                    "end": 15,
                    "claim": "a",
                    "kind": "finding",
                },
                {
                    "quote": "Overlap sentence.",
                    "start": 10,
                    "end": 27,
                    "claim": "b",
                    "kind": "null",
                },
            ],
            "empty_reason": "",
        }
    )

    class Agent:
        def review(self, task, candidate, step):
            reviews.append(step)

    evidence = batch.accept_evidence(Agent(), [], "extract/x/0", text, 0, 16, raw)
    assert [f.quote for f in evidence.findings] == ["Owned sentence."]
    assert reviews == ["extract/x/0"]


def test_extraction_stops_after_its_corrections_are_exhausted(tmp_path, monkeypatch):
    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch)

    def reject(task, raw, step):
        if step.startswith("extract/"):
            raise CandidateError("scientific review rejected " + step)

    monkeypatch.setattr(agent, "review", reject)
    with pytest.raises(CandidateError, match="scientific review rejected"):
        batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(s.startswith("extract/") for s, _ in calls) == batch.EXTRACTION_ATTEMPTS
    assert sum(s.endswith("/repair") for s, _ in calls) == batch.EXTRACTION_ATTEMPTS - 1
    assert not any(s.startswith("batch/plan/") for s, _ in calls)


def test_missing_plan_coverage_receives_one_correction(tmp_path, monkeypatch):
    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch, bad_plan=True)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert [s for s, _ in calls if s.startswith("batch/plan/")] == [
        "batch/plan/0",
        "batch/plan/0/repair",
    ]
    assert (tmp_path / "wiki/summaries/a__REPORT.md").exists()


def test_validator_checks_authoritative_merge_inputs_and_description(tmp_path, monkeypatch):
    _, _, _, job = setup_batch(tmp_path, monkeypatch)
    (tmp_path / "wiki/concepts/absorbed.md").write_text("# Absorbed\n\nYield was 56%. [src: b]")
    (tmp_path / "staging/b__REPORT.md").write_text("Yield was 56%.")
    job.merge_from = ["concepts/absorbed.md"]
    candidate = {
        "base_hash": digest(OLD),
        "content": OLD,
        "rewrite_reason": "Merge",
        "description": "Yield",
    }
    with pytest.raises(WorkflowError, match="unchanged citations or quantities"):
        batch.validate_candidate(tmp_path, job.path, job, candidate, set(), {"concepts/yield"})
    candidate["content"] = OLD + "\n\nYield was 56%. [src: b]"
    candidate["description"] = " "
    with pytest.raises(WorkflowError, match="description"):
        batch.validate_candidate(tmp_path, job.path, job, candidate, set(), {"concepts/yield"})
    assert (tmp_path / "wiki/concepts/yield.md").read_text() == OLD


@pytest.mark.parametrize("failure", ["malformed", "unknown", "retired", "merge", "summary-merge"])
def test_invalid_plan_is_corrected_before_writing(tmp_path, monkeypatch, failure):
    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch)
    recorded = agent.ask
    if failure == "retired":
        (tmp_path / "contract/concept-decisions.yaml").write_text(
            "renames:\n  - from: retired\n    to: yield\n"
        )

    def invalid_first(messages, step):
        raw = recorded(messages, step)
        if step != "batch/plan/0":
            return raw
        if failure == "malformed":
            return "not JSON"
        plan = json.loads(raw)
        if failure == "unknown":
            plan["coverage"][0]["concepts"] = ["concepts/unknown.md"]
        elif failure == "retired":
            plan["pages"][0]["path"] = "concepts/retired.md"
        elif failure == "summary-merge":
            plan["pages"][0]["path"] = "summaries/a__REPORT.md"
            plan["pages"][0]["merge_from"] = ["concepts/yield.md"]
        else:
            plan["pages"][0]["merge_from"] = ["concepts/yield.md"]
        return json.dumps(plan)

    monkeypatch.setattr(agent, "ask", invalid_first)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert [s for s, _ in calls if s.startswith("batch/plan/")] == [
        "batch/plan/0",
        "batch/plan/0/repair",
    ]
    assert (tmp_path / "wiki/summaries/a__REPORT.md").exists()


def test_multiple_planning_batches_group_destination_once(tmp_path, monkeypatch):
    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch)
    recorded = agent.ask
    original_batches = batch.planning_batches

    def two_findings(messages, step):
        raw = recorded(messages, step)
        data = json.loads(raw)
        if step.startswith("extract/"):
            data["findings"] *= 2
        if step.startswith("batch/plan/"):
            data["coverage"][0]["evidence"] = "a:0:" + step.rsplit("/", 1)[1]
        return json.dumps(data)

    monkeypatch.setattr(agent, "ask", two_findings)
    monkeypatch.setattr(batch, "planning_batches", lambda items: original_batches(items, 160))
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert [s for s, _ in calls if s.startswith("batch/plan/")] == ["batch/plan/0", "batch/plan/1"]
    assert sum(s.startswith("write/concepts/") for s, _ in calls) == 1
    saved = json.loads((agent.store / "last-plan.json").read_text())
    assert len(saved["coverage"]) == 2
    assert saved["pages"][0]["reason"] == "Recheck yield; Recheck yield"


def test_scientific_rejection_uses_same_single_correction(tmp_path, monkeypatch):
    agent, calls, reviews, _ = setup_batch(tmp_path, monkeypatch)

    def review(task, body, step):
        reviews.append((step, body))
        if step == "write/concepts/yield.md" and sum(s == step for s, _ in reviews) == 1:
            raise CandidateError("clarify measurement uncertainty")

    monkeypatch.setattr(agent, "review", review)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(s.startswith("write/concepts/") for s, _ in calls) == 2
    assert sum(s == "write/concepts/yield.md" for s, _ in reviews) == 2


def test_tool_success_does_not_skip_final_validation(tmp_path, monkeypatch):
    agent, calls, reviews, _ = setup_batch(tmp_path, monkeypatch, bad_writes=2)
    generate = agent.generate

    def generate_with_tool(messages, step, accept, *, validator=None, context=None, attempts=2):
        if step == "write/concepts/yield.md":
            before = list(reviews)
            assert validator is not None and context is not None
            candidate = {
                "base_hash": digest(OLD),
                "description": "Yield",
                "edits": [],
                "no_change_reason": "Evidence retained",
                "accounted_evidence": {"a:0:0": "Yield was 42%. [src: a]"},
            }
            assert validator(json.dumps(candidate)) == OLD
            assert reviews == before
            assert context["job"]["path"] == "concepts/yield.md"
            assert context["revised"] == []
            assert context["baselines"]["concepts/yield.md"] == digest(OLD)
        return generate(
            messages, step, accept, validator=validator, context=context, attempts=attempts
        )

    monkeypatch.setattr(agent, "generate", generate_with_tool)
    with pytest.raises(CandidateError, match="unchanged citations or quantities"):
        batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(s.startswith("write/concepts/") for s, _ in calls) == 2
    assert (tmp_path / "wiki/concepts/yield.md").read_text() == OLD


def test_source_read_failure_is_not_repaired(tmp_path, monkeypatch):
    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch)
    generate = agent.generate

    def generate_with_failed_read(
        messages, step, accept, *, validator=None, context=None, attempts=2
    ):
        if step.startswith("write/"):

            def failed_read(root):
                raise OSError("source unavailable")

            monkeypatch.setattr(batch.C, "load_sources", failed_read)
        return generate(
            messages, step, accept, validator=validator, context=context, attempts=attempts
        )

    monkeypatch.setattr(agent, "generate", generate_with_failed_read)
    with pytest.raises(OSError, match="source unavailable"):
        batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(s.startswith("write/") for s, _ in calls) == 1
    assert (tmp_path / "wiki/concepts/yield.md").read_text() == OLD


def test_source_decoding_matches_tools_and_preserves_original_bytes(tmp_path, monkeypatch):
    from beril_wiki.agentic.runtime import ReadTools

    agent, calls, _, _ = setup_batch(tmp_path, monkeypatch)
    raw = b"Yield was 42%.\nA caveat with \xff."
    (tmp_path / "staging/a__REPORT.md").write_bytes(raw)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    extracted = json.loads(
        next(task for step, task in calls if step.startswith("extract/"))[0]["content"].split("\n")[
            -1
        ]
    )["text"]
    read = ReadTools(tmp_path).read("staging/a__REPORT.md", 0, len(extracted))
    assert extracted == read["text"] == raw.decode("utf-8", errors="replace")
    assert (tmp_path / "wiki/sources/a__REPORT.md").read_bytes() == raw


@pytest.mark.parametrize("absorbed", [False, True])
def test_cocited_unchanged_measurement_survives_revision(tmp_path, monkeypatch, absorbed):
    _, _, _, job = setup_batch(tmp_path, monkeypatch)
    original = OLD.replace("[src: a]", "[src: a, b]")
    (tmp_path / "staging/a__REPORT.md").write_text("Yield was 56%.")
    (tmp_path / "staging/b__REPORT.md").write_text("Yield was 42%.")
    if absorbed:
        (tmp_path / "wiki/concepts/absorbed.md").write_text(original)
        job.merge_from = ["concepts/absorbed.md"]
        original = "# Yield\n\n## Open Directions\n\nRepeat measurements."
    (tmp_path / "wiki/concepts/yield.md").write_text(original)
    body = "# Yield\n\nYield was 56%. [src: a]\n\nEarlier measurements exist. [src: b]"
    body += "\n\n## Open Directions\n\nRepeat measurements."
    candidate = {
        "base_hash": digest(original),
        "description": "Revised yield",
        "content": body,
        "rewrite_reason": "Correct revised source",
    }
    with pytest.raises(CandidateError, match="unchanged citations or quantities"):
        batch.validate_candidate(tmp_path, job.path, job, candidate, {"a"}, {"concepts/yield"})
    candidate["content"] = body.replace("Earlier measurements exist.", "Earlier yield was 42%.")
    assert (
        batch.validate_candidate(tmp_path, job.path, job, candidate, {"a"}, {"concepts/yield"})
        == candidate["content"]
    )


def test_quantity_cited_only_to_revised_source_can_change(tmp_path, monkeypatch):
    _, _, _, job = setup_batch(tmp_path, monkeypatch)
    (tmp_path / "staging/a__REPORT.md").write_text("Yield was 56%.")
    candidate = {
        "base_hash": digest(OLD),
        "description": "Revised yield",
        "content": OLD.replace("42%", "56%"),
        "rewrite_reason": "Correct revised source",
    }
    assert (
        batch.validate_candidate(tmp_path, job.path, job, candidate, {"a"}, {"concepts/yield"})
        == candidate["content"]
    )


@pytest.mark.parametrize("failure", ["missing", "unknown", "absent", "wrong-source"])
def test_assigned_evidence_requires_cited_candidate_passages(tmp_path, monkeypatch, failure):
    _, _, _, job = setup_batch(tmp_path, monkeypatch)
    passage = "Yield was 42%. [src: a]"
    body = OLD + "\n\nNo benefit was observed. [src: b]"
    (tmp_path / "staging/b__REPORT.md").write_text("No benefit was observed.")
    candidate = {
        "base_hash": digest(OLD),
        "description": "Yield",
        "content": body,
        "rewrite_reason": "Integrate",
        "accounted_evidence": {"a:0:0": passage},
    }
    assigned = [{"id": "a:0:0", "source": "a", "claim": "Yield was 42%.", "kind": "finding"}]
    if failure == "missing":
        candidate.pop("accounted_evidence")
    elif failure == "unknown":
        candidate["accounted_evidence"]["a:0:1"] = passage
    elif failure == "absent":
        candidate["accounted_evidence"]["a:0:0"] = "A missing caveat. [src: a]"
    else:
        candidate["accounted_evidence"]["a:0:0"] = "No benefit was observed. [src: b]"
    with pytest.raises(CandidateError, match="assigned evidence"):
        batch.validate_candidate(
            tmp_path, job.path, job, candidate, set(), {"concepts/yield"}, assigned=assigned
        )


@pytest.mark.parametrize("failure", ["omitted", "misrepresented"])
def test_concept_assignments_survive_writing_validation_and_review(tmp_path, monkeypatch, failure):
    agent, calls, _, job = setup_batch(tmp_path, monkeypatch)
    text = "Yield was 42%. No benefit was observed. Conditions were uncontrolled."
    (tmp_path / "staging/a__REPORT.md").write_text(text)
    (tmp_path / "staging/b__REPORT.md").write_text("An unrelated study.")
    claims = ["Yield was 42%.", "No benefit was observed.", "Conditions were uncontrolled."]
    assignments = [job.path, "concepts/limits.md", "concepts/limits.md"]
    inspected = []

    def replies(messages, step):
        if step.startswith("extract/"):
            return json.dumps(
                {
                    "findings": [
                        {
                            "quote": claim,
                            "claim": claim,
                            "start": text.index(claim),
                            "end": text.index(claim) + len(claim),
                            "kind": kind,
                        }
                        for claim, kind in zip(claims, ["finding", "null", "caveat"], strict=True)
                    ],
                    "empty_reason": "",
                }
            )
        if step.startswith("batch/plan/"):
            return json.dumps(
                {
                    "pages": [
                        job.model_dump(),
                        job.model_dump() | {"path": assignments[1], "sources": ["b"]},
                    ],
                    "coverage": [
                        {"evidence": f"a:0:{i}", "concepts": [path], "summary_only": ""}
                        for i, path in enumerate(assignments)
                    ],
                }
            )
        payload = json.loads(messages[0]["content"].split("\n")[-1])
        calls.append((step, messages))
        path = payload["job"]["path"]
        ids = [
            f"a:0:{i}"
            for i, dest in enumerate(assignments)
            if dest == path or path.startswith("summaries/")
        ]
        assert [entry["evidence"] for entry in payload["coverage"]] == ids
        evidence = {e["id"]: e for e in payload["evidence"]}
        assert set(ids) <= evidence.keys()
        account = {eid: evidence[eid]["claim"] + " [src: a]" for eid in ids}
        body = "# Evidence\n\n" + "\n\n".join(account.values())
        body += (
            "\n\n## Slots Into\n\n[[concepts/yield]]"
            if path.startswith("summaries/")
            else "\n\n## Open Directions\n\nRepeat measurements."
        )
        # The null result must not disappear even if the caveat cites the same source.
        if path == assignments[1] and not step.endswith("/repair"):
            body = body.replace(account.pop("a:0:1") + "\n\n", "")
            if failure == "misrepresented":
                account["a:0:1"] = account["a:0:2"]
        return json.dumps(
            {
                "base_hash": payload["base_hash"],
                "description": "Evidence",
                "content": body,
                "rewrite_reason": "Integrate",
                "accounted_evidence": account,
            }
        )

    def review(task, body, step):
        if not step.startswith("write/"):
            return
        payload = json.loads(task[0]["content"].split("\n")[-1])
        expected = {c["evidence"] for c in payload["coverage"]}
        account = json.loads(task[-1]["content"].split("\n")[-1])
        assert set(account) == expected
        assert all(passage in body for passage in account.values())
        inspected.append(step)
        if "a:0:1" in account and claims[1] not in account["a:0:1"]:
            raise CandidateError("assigned null result is missing from its mapped paragraph")

    generate = agent.generate

    def check_bound_tool(messages, step, accept, *, validator=None, context=None, attempts=2):
        if step == "write/concepts/limits.md":
            assert context is not None and validator is not None
            assert {f["id"] for f in context["assigned"]} == {"a:0:1", "a:0:2"}
            payload = json.loads(messages[0]["content"].split("\n")[-1])
            assert payload["job"]["sources"] == ["a", "b"]
            with pytest.raises(CandidateError, match="assigned evidence"):
                validator(
                    json.dumps(
                        {
                            "base_hash": digest(""),
                            "description": "Limits",
                            "content": "# Limits\n\nConditions were uncontrolled. [src: a]\n\n"
                            "## Open Directions\n\nRepeat measurements.",
                        }
                    )
                )
        return generate(
            messages, step, accept, validator=validator, context=context, attempts=attempts
        )

    monkeypatch.setattr(agent, "ask", replies)
    monkeypatch.setattr(agent, "review", review)
    monkeypatch.setattr(agent, "generate", check_bound_tool)
    batch.compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert sum(step.startswith("write/concepts/limits.md") for step, _ in calls) == 2
    assert inspected.count("write/concepts/limits.md") == (2 if failure == "misrepresented" else 1)
    assert all(claim in (tmp_path / "wiki/concepts/limits.md").read_text() for claim in claims[1:])
