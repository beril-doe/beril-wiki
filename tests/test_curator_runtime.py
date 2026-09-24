"""Offline retrieval, replay and repair contracts for the curator runtime."""

import json

import pytest

from beril_wiki.agentic import runtime as R


def runtime(tmp_path):
    (tmp_path / "contract").mkdir(exist_ok=True)
    (tmp_path / "contract/AGENTS.md").write_text("Preserve source evidence.")
    return R.Runtime(
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "jobs"),
            run="test",
            model="test",
            cli="claude",
            max_tokens=10000,
            max_jobs=20,
            reserve_tokens=10,
        )
    )


def test_search_pagination_literal_paths_and_negative_inventory(tmp_path):
    folder = tmp_path / "wiki/concepts"
    folder.mkdir(parents=True)
    for i in range(23):
        (folder / f"p{i:02}.md").write_text("A literal [x] was observed. [src: a]")
    reader = R.EvidenceTools(tmp_path)
    first = reader.search("[x]", "wiki", 0)
    assert len(first["matches"]) == 20 and not first["exhausted"]
    second = reader.search("[x]", "wiki", first["next_offset"])
    assert len(second["matches"]) == 3 and second["exhausted"]
    assert second["matches"][0]["sources"] == ["a"]
    assert reader.search("absent", "wiki", 0)["matches"] == []
    old = R.current_dependencies(tmp_path, reader.dependencies)
    (folder / "new.md").write_text("absent")
    assert R.current_dependencies(tmp_path, reader.dependencies) != old
    with pytest.raises(R.WorkflowError):
        reader.search("x", "../", 0)
    with pytest.raises(R.WorkflowError):
        reader.search("", "wiki", 0)


def test_search_job_reuses_cache_and_invalidates_added_deleted_files(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    (tmp_path / "wiki/concepts").mkdir(parents=True)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    calls = []

    async def answer(payload, key, model):
        reader = R.EvidenceTools(tmp_path)
        result = json.dumps(reader.search("quartz", "wiki", 0))
        calls.append(key)
        agent.ledger.finish(
            key, result, {"input_tokens": 2, "output_tokens": 3}, dependencies=reader.dependencies
        )
        return result

    monkeypatch.setattr(agent, "_query", answer)
    task = [{"role": "user", "content": "Find quartz"}]
    assert agent.ask(task, "curator/topics") == agent.ask(task, "curator/topics")
    assert len(calls) == 1
    path = tmp_path / "wiki/concepts/quartz.md"
    path.write_text("quartz")
    assert json.loads(agent.ask(task, "curator/topics"))["matches"]
    path.unlink()
    assert json.loads(agent.ask(task, "curator/topics"))["matches"] == []
    # Restoring a previously seen exact inventory can reuse its negative result.
    assert len(calls) == 2 and agent.ledger.totals()["tokens"] == 10


def test_generation_repairs_once_and_never_retries_operational_error(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    calls = []

    def ask(task, step):
        calls.append((task, step))
        return "good" if step.endswith("/repair") else "bad"

    def accept(raw):
        if raw != "good":
            raise R.CandidateError("Missing exact measurement")
        return raw

    monkeypatch.setattr(agent, "ask", ask)
    assert agent.generate([], "write/test", accept) == "good"
    assert len(calls) == 2 and "Missing exact measurement" in str(calls[-1][0])
    calls.clear()

    def fail(raw):
        raise R.CandidateError("still wrong")

    with pytest.raises(R.CandidateError):
        agent.generate([], "write/test", fail)
    assert len(calls) == 2
    calls.clear()

    def budget(task, step):
        calls.append(step)
        raise R.WorkflowError("budget admission refused")

    monkeypatch.setattr(agent, "ask", budget)
    with pytest.raises(R.WorkflowError, match="budget"):
        agent.generate([], "write/test", accept)
    assert calls == ["write/test"]


def test_refused_job_is_reissued_on_the_model_that_answers_it(tmp_path, monkeypatch):
    from claude_agent_sdk import ResultMessage, SystemMessage

    agent = runtime(tmp_path)
    models = []
    welcomed = "extract/a/32000"

    def result(text):
        return ResultMessage(
            subtype="success",
            duration_ms=1,
            duration_api_ms=1,
            is_error=False,
            num_turns=1,
            session_id="s",
            total_cost_usd=0.1,
            usage={"input_tokens": 1, "output_tokens": 1},
            result=text,
        )

    def query(*, prompt, options):
        models.append(options.model)
        refusing = options.model == "claude-opus-5-5" and agent._step != welcomed

        async def stream():
            yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
            if refusing:
                yield SystemMessage(
                    subtype="model_refusal_fallback",
                    data={
                        "original_model": "claude-opus-5-5",
                        "fallback_model": "claude-opus-5",
                        "api_refusal_category": "bio",
                    },
                )
                yield result("")
            else:
                yield result("on 5.5" if agent._step == welcomed else "findings")

        return stream()

    monkeypatch.setattr(R, "query", query)
    monkeypatch.setitem(agent.config, "model", "claude-opus-5-5")

    # One chunk of this source is written by the configured model before anything is
    # refused, so there is work worth keeping when the source is later flagged.
    assert agent.ask([{"role": "user", "content": "welcome"}], welcomed) == "on 5.5"
    assert models == ["claude-opus-5-5"]

    models.clear()
    assert agent.ask([{"role": "user", "content": "extract"}], "extract/a/0") == "findings"
    assert models == ["claude-opus-5-5", "claude-opus-5"]
    rows = agent.ledger.db.execute(
        "SELECT model, status, error FROM jobs WHERE step='extract/a/0' ORDER BY rowid"
    ).fetchall()
    assert [(m, st) for m, st, _ in rows] == [
        ("claude-opus-5-5", "rejected"),
        ("claude-opus-5", "done"),
    ]
    assert "refused on claude-opus-5-5 [bio]" in rows[0][2]

    # A refusal must never block a later run, nor be paid for a second time.
    models.clear()
    assert agent.ask([{"role": "user", "content": "extract"}], "extract/a/0") == "findings"
    assert models == []

    # A safeguard refuses the text, not the prompt, so the source's other jobs skip
    # the attempt that is already known to be refused.
    assert agent.ask([{"role": "user", "content": "more"}], "extract/a/16000") == "findings"
    assert models == ["claude-opus-5"]

    # A different source is untouched and still gets the configured model first.
    models.clear()
    assert agent.ask([{"role": "user", "content": "other"}], "extract/b/0") == "findings"
    assert models[0] == "claude-opus-5-5"

    # Work the configured model already did is never discarded to buy it again on the
    # other one, even though its source is now flagged: no job is issued at all.
    models.clear()
    assert agent.ask([{"role": "user", "content": "welcome"}], welcomed) == "on 5.5"
    assert models == []


def test_verification_keeps_unresolved_objections_and_adds_only_new_defects(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    asked = []

    def reply(messages, step):
        asked.append((step, messages[0]["content"]))
        return '{"resolved": [1], "open": ["repair inverted the direction"]}'

    monkeypatch.setattr(agent, "ask", reply)
    still = agent.verify([{"role": "user", "content": "task"}], "cand", ["a", "b"], "extract/r/0")
    assert still == ["a", "repair inverted the direction"]
    assert asked[0][0] == "extract/r/0/verify"
    assert '"issues_raised"' in asked[0][1] and "do not review it again" in asked[0][1]


def test_merge_candidates_keep_independent_review_and_one_repair(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "runtime", lambda: agent)
    calls = []

    def ask(task, step):
        calls.append(step)
        if step.endswith("/science-review"):
            return json.dumps(
                {
                    "accepted": "bad" not in str(task),
                    "issues": ["unsupported claim"] if "bad" in str(task) else [],
                }
            )
        return "good" if step.endswith("/repair") else "bad"

    monkeypatch.setattr(agent, "ask", ask)
    assert R.text_completion([], "merge/entity") == "good"
    assert calls == [
        "merge/entity",
        "merge/entity/science-review",
        "merge/entity/repair",
        "merge/entity/science-review",
    ]
    calls.clear()
    monkeypatch.setattr(agent, "ask", lambda messages, step: calls.append(step) or "not JSON")
    with pytest.raises(R.WorkflowError, match="verdict"):
        R.text_completion([], "merge/entity")
    assert calls == ["merge/entity", "merge/entity/science-review"]
    calls.clear()
    assert R.text_completion([], "figures/x", review=False) == "not JSON"
    assert calls == ["figures/x"]


@pytest.mark.parametrize("step", ["merge/a/retry", "merge/a/retention", "merge/a/retention/retry"])
def test_legacy_retry_gets_review_without_another_repair(tmp_path, monkeypatch, step):
    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "runtime", lambda: agent)
    calls = []

    def ask(task, name):
        calls.append(name)
        return (
            '{"accepted": false, "issues": ["unsupported"]}'
            if name.endswith("science-review")
            else "candidate"
        )

    monkeypatch.setattr(agent, "ask", ask)
    with pytest.raises(R.CandidateError):
        R.text_completion([], step)
    assert calls == [step, step + "/science-review"]


def test_sdk_validation_tool_is_bound_only_to_writer(tmp_path, monkeypatch):
    from claude_agent_sdk import ResultMessage, SystemMessage

    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/a.md").write_bytes(b"value \xff end")
    original_server = R.create_sdk_mcp_server
    exposed = {}

    def server(name, *, tools):
        exposed.clear()
        exposed.update({t.name: t for t in tools})
        return original_server(name, tools=tools)

    monkeypatch.setattr(R, "create_sdk_mcp_server", server)

    async def query(**kwargs):
        yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
        read = await exposed["read_evidence"].handler(
            {"path": "staging/a.md", "start": 0, "end": 11}
        )
        assert json.loads(read["content"][0]["text"])["text"] == "value \ufffd end"
        invalid = await exposed["read_evidence"].handler(
            {"path": "wiki/\0.md", "start": 0, "end": 1}
        )
        assert invalid["is_error"]
        if agent._step.startswith("write/"):
            found = await exposed["search_evidence"].handler(
                {"query": "value", "scope": "staging", "offset": 0}
            )
            assert (
                json.loads(found["content"][0]["text"])["matches"][0]["text"] == "value \ufffd end"
            )
            with monkeypatch.context() as patch:

                def fail(*args):
                    raise ValueError("invalid text")

                patch.setattr(R.EvidenceTools, "search", fail)
                error = await exposed["search_evidence"].handler(
                    {"query": "value", "scope": "staging", "offset": 0}
                )
                assert error["is_error"]
            assert set(exposed) == {"read_evidence", "search_evidence", "validate_candidate"}
            verdict = await exposed["validate_candidate"].handler({"candidate": "bad"})
            assert not json.loads(verdict["content"][0]["text"])["valid"]
            verdict = await exposed["validate_candidate"].handler({"candidate": "good"})
            assert json.loads(verdict["content"][0]["text"])["valid"]
        else:
            assert set(exposed) == {"read_evidence"}
        yield ResultMessage(
            subtype="success",
            duration_ms=0,
            duration_api_ms=0,
            is_error=False,
            num_turns=1,
            session_id="fixture",
            result="good",
            usage={"input_tokens": 2, "output_tokens": 3},
        )

    def validate(raw):
        if raw != "good":
            raise R.CandidateError("wrong value")

    monkeypatch.setattr(R, "query", query)
    assert (
        agent.generate(
            [], "write/test", lambda raw: raw, validator=validate, context={"base": "authoritative"}
        )
        == "good"
    )
    assert agent.ask([], "extract/test") == "good"
    assert agent._validator is None


def test_search_ignores_unsearched_assets_and_bounds_long_snippets(tmp_path):
    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "wiki/concepts/a.md").write_text("z" * 100 + "x" * 200 + "z" * 100)
    reader = R.EvidenceTools(tmp_path)
    result = reader.search("x" * 200)
    assert len(result["matches"][0]["text"]) <= 200
    before = R.current_dependencies(tmp_path, reader.dependencies)
    for folder, name in (("figures", "a.png"), ("sources", "a.md")):
        (tmp_path / "wiki" / folder).mkdir()
        (tmp_path / "wiki" / folder / name).write_bytes(b"irrelevant")
    assert R.current_dependencies(tmp_path, reader.dependencies) == before


def test_large_collection_context_is_bounded_and_retrievable():
    pages: dict[str, str] = {
        f"wiki/summaries/project-{i}__REPORT.md": "μ yield and caveats. " * 1000 for i in range(100)
    }
    previews = R.page_contexts(pages)
    assert len(json.dumps(previews).encode("utf-8")) <= 160_000
    assert set(previews) == set(pages)
    for path, preview in previews.items():
        prefix = preview.split("\n[TRUNCATED:")[0]
        assert pages[path].startswith(prefix)
        assert path in preview and f"offset {len(prefix)}" in preview


@pytest.mark.parametrize(
    ("step", "role"),
    [
        ("curator/topics/repair", "planning"),
        ("extract/a/0", "extraction"),
        ("batch/plan/0/repair", "planning"),
        ("write/concepts/a.md/repair", "writing"),
        ("lit/a/section", "writing"),
        ("conflicts/a/review", "review"),
        ("topics/a/patch/2", "writing"),
        ("topics/a/patch/2/review", "review"),
        ("topics/a/patch/2/verify", "review"),
        ("topics/a/patch/2/verify/again", "review"),
        ("lit/a/queries/repair", "queries"),
        ("figures/topics/a.md", "figures"),
        ("write/concepts/a.md/repair/science-review", "review"),
        ("authors/queries/retry", "writing"),
        # A reviewer retry must stay on the reviewer, not fall through to writing.
        ("conflicts/a/review/again", "review"),
        ("topics/a/patch/1/review/again", "review"),
    ],
)
def test_model_routes_cover_repairs_and_reviews(step, role):
    config = {"model": "default", "step_models": {role: "selected"}}
    assert R.model_for(config, step) == "selected"
    assert R.model_for({"model": "default"}, step) == "default"


def test_model_cache_and_sdk_selection_share_one_budget(tmp_path, monkeypatch):
    from claude_agent_sdk import ResultMessage, SystemMessage

    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    models = []

    async def query(**kwargs):
        models.append(kwargs["options"].model)
        yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
        yield ResultMessage(
            subtype="success",
            duration_ms=0,
            duration_api_ms=0,
            is_error=False,
            num_turns=1,
            session_id="recorded",
            result="answer",
            usage={"input_tokens": 3, "output_tokens": 5},
            stop_reason="end_turn",
        )

    monkeypatch.setattr(R, "query", query)
    messages = [{"role": "user", "content": "check"}]
    agent.ask(messages, "write/concepts/a.md")
    routed = R.Runtime(agent.config | {"step_models": {"review": "reviewer"}})
    routed.ask(messages, "write/concepts/a.md")  # unchanged writer is cached
    routed.ask(messages, "write/concepts/a.md/science-review")
    routed.ask(messages, "write/concepts/a.md/repair")
    assert models == ["test", "reviewer", "test"]
    assert routed.ledger.totals()["tokens"] == 24
    assert [
        r[0] for r in routed.ledger.db.execute("SELECT model FROM jobs ORDER BY rowid")
    ] == models
    limited = R.Runtime(routed.config | {"max_tokens": 30, "step_models": {"review": "another"}})
    with pytest.raises(R.WorkflowError, match="budget admission refused"):
        limited.ask(messages, "write/concepts/a.md/science-review")
    assert len(models) == 3


def test_model_changes_invalidate_only_relevant_stage_policy(tmp_path):
    from beril_wiki.agentic.curator import stage_revision

    config = {"model": "strong"}
    figure = config | {"step_models": {"figures": "small"}}
    query = config | {"step_models": {"queries": "small"}}
    review = config | {"step_models": {"review": "other"}}
    baseline = {
        s: stage_revision(tmp_path, s, config)
        for s in ("topics", "literature", "authors", "conflicts", "figures")
    }
    for stage, rev in baseline.items():
        assert (stage_revision(tmp_path, stage, figure) != rev) == (stage == "figures")
        assert (stage_revision(tmp_path, stage, query) != rev) == (stage == "literature")
        assert (stage_revision(tmp_path, stage, review) != rev) == (stage != "figures")
    assert R.model_signature(config) == "strong"
    assert R.model_signature(config | {"step_models": {"writing": "strong"}}) == "strong"


@pytest.mark.parametrize(
    "overrides", [["unknown=x"], ["review="], ["review"], ["review=a", "review=b"]]
)
def test_cli_rejects_invalid_model_overrides(tmp_path, monkeypatch, overrides):
    import sys

    from beril_wiki.agentic import __main__ as cli

    args = [
        "agentic",
        "--root",
        str(tmp_path),
        "run",
        "--model",
        "default",
        "--max-tokens",
        "100",
        "--max-jobs",
        "3",
        "--cli",
        "unused",
    ]
    for value in overrides:
        args += ["--step-model", value]
    monkeypatch.setattr(sys, "argv", args)
    monkeypatch.setattr(cli, "run", lambda *a: pytest.fail("invalid config reached runner"))
    assert cli.main() == 1


@pytest.mark.parametrize("use_yaml", [False, True])
def test_cli_passes_explicit_model_policy(tmp_path, monkeypatch, use_yaml):
    import sys

    from beril_wiki.agentic import __main__ as cli

    if use_yaml:
        (tmp_path / "agentic.yaml").write_text("model: old\nstep_models: {writing: old-writer}")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "agentic",
            "--root",
            str(tmp_path),
            "run",
            "--model",
            "strong",
            "--max-tokens",
            "100",
            "--max-jobs",
            "3",
            "--cli",
            "unused",
            "--step-model",
            "figures=small",
            "--step-model",
            "review=reviewer",
        ],
    )
    configs = []
    monkeypatch.setattr(cli, "run", lambda root, checkout, config, staged: configs.append(config))
    assert cli.main() == 0
    assert configs[0]["step_models"] == {"figures": "small", "review": "reviewer"}
    assert configs[0]["model"] == "strong"
    assert configs[0]["workers"] == 4 and configs[0]["strict_pages"] is False


def test_cli_loads_committed_policy_without_model_flag(tmp_path, monkeypatch):
    import sys
    from pathlib import Path

    from beril_wiki.agentic import __main__ as cli

    policy = (Path(__file__).parents[1] / "agentic.yaml").read_text()
    (tmp_path / "agentic.yaml").write_text(policy)
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "agentic",
            "--root",
            str(tmp_path),
            "run",
            "--max-tokens",
            "100",
            "--max-jobs",
            "3",
            "--cli",
            "unused",
        ],
    )
    configs = []
    monkeypatch.setattr(cli, "run", lambda root, checkout, config, staged: configs.append(config))
    assert cli.main() == 0
    assert R.model_policy(configs[0]) == {
        role: "claude-opus-5-5" if role in R.CORE_MODEL_ROLES else "claude-sonnet-5"
        for role in R.MODEL_ROLES
    }
    # Replacement file paths resolve against the chosen root, and a role flag wins.
    (tmp_path / "custom.yaml").write_text("model: alternate\nstep_models: {review: specialist}")
    for path in (Path("custom.yaml"), tmp_path / "custom.yaml"):
        selected = R.model_policy(cli.load_models(tmp_path, path, None, ["review=override"]))
        assert selected["review"] == "override"
        assert selected["writing"] == "alternate"


@pytest.mark.parametrize(
    "contents",
    [
        "",
        "[]",
        "model: [",
        "model: 123",
        "model: ''",
        "model: valid\nmodels: {}",
        "model: valid\nstep_models: null",
        "model: valid\nstep_models: {typo: valid}",
        "model: valid\nstep_models: {review: 123}",
    ],
)
def test_invalid_yaml_model_policy_stops(tmp_path, contents):
    from beril_wiki.agentic.__main__ import load_models

    (tmp_path / "agentic.yaml").write_text(contents)
    with pytest.raises(R.WorkflowError):
        load_models(tmp_path, None, None, [])


def test_missing_policy_requires_explicit_model(tmp_path):
    from pathlib import Path

    from beril_wiki.agentic.__main__ import load_models

    with pytest.raises(R.WorkflowError, match="model must"):
        load_models(tmp_path, None, None, [])
    assert load_models(tmp_path, None, "explicit", []) == {"model": "explicit", "step_models": {}}
    with pytest.raises(FileNotFoundError):
        load_models(tmp_path, Path("missing.yaml"), "explicit", [])


@pytest.mark.parametrize("legacy", [False, True])
def test_model_change_preserves_interrupted_run_charges(tmp_path, monkeypatch, legacy):
    from types import SimpleNamespace

    from beril_wiki.agentic import runner

    root, checkout = tmp_path / "repo", tmp_path / "observatory"
    for folder in (*runner.TREES, "contract"):
        (root / folder).mkdir(parents=True)
    (checkout / "ui/config").mkdir(parents=True)
    (checkout / "ui/config/collections.yaml").write_text("collections: []")
    config = dict(cli="unused", model="first", max_tokens=40, max_jobs=5, reserve_tokens=30)
    monkeypatch.setattr(runner.subprocess, "run", lambda *a, **k: SimpleNamespace(stdout="test"))
    if legacy:
        store = root / ".agentic"
        store.mkdir()
        run_id = R.digest(
            [runner.fingerprint(root), runner.checkout_inputs(checkout), "first", False]
        )
        (store / "config.json").write_text(json.dumps(config | {"run": run_id}))
    runs = []

    def stopped_stage(work, config_path, name, module, args):
        saved = json.loads(config_path.read_text())
        agent = R.Runtime(saved)
        runs.append(saved["run"])
        agent.ledger.reserve(saved["model"], "extract/a/0", saved["model"])
        agent.ledger.finish(
            saved["model"], "saved extraction", {"input_tokens": 10, "output_tokens": 10}
        )
        raise R.WorkflowError("interrupted after paid work")

    monkeypatch.setattr(runner, "run_stage", stopped_stage)
    with pytest.raises(R.WorkflowError, match="interrupted"):
        runner.run(root, checkout, config)
    with pytest.raises(R.WorkflowError, match="budget admission refused"):
        runner.run(root, checkout, config | {"model": "second", "step_models": {"review": "third"}})
    assert len(runs) == 2 and runs[0] == runs[1]
    saved = json.loads((root / ".agentic/config.json").read_text())
    assert R.Runtime(saved).ledger.totals()["tokens"] == 20


def test_read_clamps_end_to_document_length(tmp_path):
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/a.md").write_text("short text")
    reader = R.ReadTools(tmp_path)
    piece = reader.read("staging/a.md", 0, 99_999)
    assert piece["text"] == "short text" and piece["end"] == piece["length"] == 10
    with pytest.raises(R.WorkflowError, match="beyond document length"):
        reader.read("staging/a.md", 10, 11)


def test_error_result_usage_is_recorded_when_cli_exits_nonzero(tmp_path, monkeypatch):
    from claude_agent_sdk import ProcessError, ResultMessage, SystemMessage

    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)

    async def query(**kwargs):
        yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
        yield ResultMessage(
            subtype="error_max_turns",
            duration_ms=0,
            duration_api_ms=0,
            is_error=True,
            num_turns=13,
            session_id="recorded",
            result="",
            usage={"input_tokens": 3, "output_tokens": 5, "cache_read_input_tokens": 40},
            stop_reason="tool_use",
        )
        raise ProcessError("Claude Code returned an error result: max turns", exit_code=1)

    monkeypatch.setattr(R, "query", query)
    with pytest.raises(R.WorkflowError, match="error_max_turns"):
        agent.ask([{"role": "user", "content": "check"}], "write/concepts/a.md/science-review")
    assert agent.ledger.db.execute("SELECT status, tokens FROM jobs").fetchall() == [("failed", 48)]


def test_timed_out_job_is_charged_from_its_turns(tmp_path, monkeypatch):
    from claude_agent_sdk import AssistantMessage, SystemMessage

    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)

    async def query(**kwargs):
        yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
        usage = {"input_tokens": 7, "output_tokens": 2, "cache_read_input_tokens": 30}
        yield AssistantMessage(content=[], model="test", usage=usage)
        yield AssistantMessage(content=[], model="test", usage=usage)
        raise TimeoutError("job clock")

    monkeypatch.setattr(R, "query", query)
    with pytest.raises(R.WorkflowError, match="job clock"):
        agent.ask([{"role": "user", "content": "check"}], "topics/a")
    status, tokens, effective, error = agent.ledger.db.execute(
        "SELECT status, tokens, effective, error FROM jobs"
    ).fetchone()
    assert (status, tokens, effective) == ("failed", 39, 12) and "interrupted" in error
    assert agent.ledger.reserve("next") is None


def test_system_messages_join_the_cached_system_prompt(tmp_path, monkeypatch):
    from claude_agent_sdk import ResultMessage, SystemMessage

    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    seen = {}

    async def query(**kwargs):
        seen["system"] = kwargs["options"].system_prompt
        async for message in kwargs["prompt"]:
            seen["user"] = message["message"]["content"]
        yield SystemMessage(subtype="init", data={"apiKeySource": "none"})
        yield ResultMessage(
            subtype="success",
            duration_ms=0,
            duration_api_ms=0,
            is_error=False,
            num_turns=1,
            session_id="recorded",
            result="answer",
            usage={"input_tokens": 3, "output_tokens": 5},
            stop_reason="end_turn",
        )

    monkeypatch.setattr(R, "query", query)
    messages = [
        {"role": "system", "content": "EVIDENCE PACK"},
        {"role": "user", "content": "TASK ONLY"},
    ]
    assert agent.ask(messages, "conflicts/a") == "answer"
    assert seen["system"].endswith("Preserve source evidence.\n\nEVIDENCE PACK")
    assert "EVIDENCE PACK" not in seen["user"] and "TASK ONLY" in seen["user"]


def test_tool_free_jobs_key_on_their_prompt_only(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    (tmp_path / "staging").mkdir()
    source = tmp_path / "staging/report__REPORT.md"
    source.write_text("old")
    monkeypatch.setattr(R, "check_auth", lambda cli: None)
    calls = []

    async def answer(payload, key, model):
        calls.append(key)
        agent.ledger.finish(key, "ok", {"input_tokens": 1, "output_tokens": 1})
        return "ok"

    monkeypatch.setattr(agent, "_query", answer)
    task = [{"role": "user", "content": "about report"}]
    agent.ask(task, "conflicts/a")
    source.write_text("revised")
    agent.ask(task, "conflicts/a")  # packed job: the source text was never in its prompt
    agent.ask(task, "extract/report/0")
    source.write_text("revised again")
    agent.ask(task, "extract/report/0")  # tool-using job: the source is its evidence
    assert len(calls) == 3
