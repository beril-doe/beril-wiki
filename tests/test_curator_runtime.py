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

    async def answer(payload, key):
        reader = R.EvidenceTools(tmp_path)
        result = json.dumps(reader.search("quartz", "wiki", 0))
        calls.append(key)
        agent.ledger.finish(
            key, result, {"input_tokens": 2, "output_tokens": 3}, dependencies=reader.dependencies
        )
        return result

    monkeypatch.setattr(agent, "_query", answer)
    task = [{"role": "user", "content": "Find quartz"}]
    assert agent.ask(task, "curator/decision/0") == agent.ask(task, "curator/decision/0")
    assert len(calls) == 1
    path = tmp_path / "wiki/concepts/quartz.md"
    path.write_text("quartz")
    assert json.loads(agent.ask(task, "curator/decision/0"))["matches"]
    path.unlink()
    assert json.loads(agent.ask(task, "curator/decision/0"))["matches"] == []
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


def test_derived_prose_repair_gets_independent_review(tmp_path, monkeypatch):
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
    assert R.text_completion([], "topics/test") == "good"
    assert len(calls) == 4


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


def test_scientific_review_routing_ignores_words_inside_slugs(monkeypatch):
    from beril_wiki import compiler

    monkeypatch.setenv("BERIL_AGENTIC_CONFIG", "configured")
    calls = []
    monkeypatch.setattr(
        R, "text_completion", lambda messages, step, review=True: calls.append(review) or "{}"
    )
    for step in (
        "lit/plant-x/review",
        "merge/plant-cell",
        "authors/alex-judge",
        "a/plan",
        "lit/plant-x/queries",
        "a/enrich-plan",
        "merge-judge/a+b",
    ):
        compiler.llm([], step)
    assert calls == [True, True, True, False, False, False, False]


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


def test_malformed_review_does_not_spend_author_repair(tmp_path, monkeypatch):
    agent = runtime(tmp_path)
    monkeypatch.setattr(R, "runtime", lambda: agent)
    calls = []
    monkeypatch.setattr(agent, "ask", lambda messages, step: calls.append(step) or "not JSON")
    with pytest.raises(R.WorkflowError, match="verdict"):
        R.text_completion([], "topics/test")
    assert calls == ["topics/test", "topics/test/science-review"]


def test_large_collection_context_is_bounded_and_retrievable():
    pages: dict[str, str] = {
        f"wiki/summaries/project-{i}__REPORT.md": "μ yield and caveats. " * 1000 for i in range(100)
    }
    previews = R.page_contexts(pages)
    assert len(json.dumps(previews).encode("utf-8")) <= 160_000
    assert set(previews) == set(pages)
    for path, preview in previews.items():
        prefix = preview.split("\n[PREVIEW ONLY:")[0]
        assert pages[path].startswith(prefix)
        assert path in preview and f"offset {len(prefix)}" in preview


@pytest.mark.parametrize(
    "step",
    [
        "merge/a/retry",
        "merge/a/retention",
        "merge/a/retention/retry",
        "topics/a/retry-citations",
        "topics/a/retry-numbers",
    ],
)
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
