"""Offline safety and resume contracts for the subscription compiler."""

import pytest

from beril_wiki.agentic.runtime import Ledger, ReadTools, WorkflowError


def test_ledger_resume_and_global_budget(tmp_path):
    db = tmp_path / "jobs.sqlite"
    first = Ledger(db, "batch", 100, 3, 40)
    assert first.reserve("one") is None
    first.finish("one", "answer", {"input_tokens": 10, "output_tokens": 20})
    second = Ledger(db, "batch", 100, 3, 40)
    assert second.reserve("one") == "answer"
    second.reserve("two")
    second.finish("two", "answer2", {"input_tokens": 10, "output_tokens": 30})
    with pytest.raises(WorkflowError, match="budget"):
        first.reserve("three")


def test_inflight_jobs_hold_headroom_and_stale_ones_reconcile(tmp_path):
    import json

    db = tmp_path / "jobs.sqlite"
    ledger = Ledger(db, "batch", 100, 9, 20)
    ledger.reserve("crash")
    ledger.reserve("worker")  # a second worker's job is admitted while one is in flight
    with pytest.raises(WorkflowError, match="inflight=2"):
        Ledger(db, "batch", 50, 9, 20).reserve("third")
    ledger.finish("worker", "ok", {"input_tokens": 5, "output_tokens": 5})
    transcripts = tmp_path / "transcripts"
    transcripts.mkdir()
    lines = [
        {"model": "m", "content": [], "usage": {"input_tokens": 4, "output_tokens": 1}},
        {"model": "m", "content": [], "usage": {"input_tokens": 4, "output_tokens": 1}},
        {"model": "m", "content": [], "usage": {"input_tokens": 6, "output_tokens": 2}},
    ]
    (transcripts / "crash.jsonl").write_text("\n".join(json.dumps(x) for x in lines))
    ledger.reserve("silent")
    assert sorted(Ledger(db, "batch", 100, 9, 20).reconcile_stale(transcripts)) == [
        "crash",
        "silent",
    ]
    rows = dict(ledger.db.execute("SELECT key,tokens FROM jobs").fetchall())
    assert rows == {"crash": 13, "worker": 10, "silent": 20}  # repeated turn counted once
    ledger.reserve("unknown")
    with pytest.raises(WorkflowError, match="unknown token usage"):
        ledger.finish("unknown", "", None)
    with pytest.raises(WorkflowError, match="unknown usage"):
        ledger.reserve("blocked")


def test_effective_tokens_drive_admission_and_stage_ceiling(tmp_path, monkeypatch):
    db = tmp_path / "jobs.sqlite"
    ledger = Ledger(db, "batch", 1000, 9, 100, stage_budget=300)
    usage = {
        "input_tokens": 100,
        "output_tokens": 100,
        "cache_creation_input_tokens": 400,
        "cache_read_input_tokens": 3000,
    }
    monkeypatch.setenv("BERIL_AGENTIC_STAGE", "conflicts")
    ledger.reserve("one", "conflicts/a")
    ledger.finish("one", "ok", usage, cost=0.5)
    totals = ledger.totals()
    assert totals["tokens"] == 3600 and totals["effective"] == 1000 and totals["cost_usd"] == 0.5
    with pytest.raises(WorkflowError, match="budget admission refused"):
        ledger.reserve("two", "conflicts/b")
    ledger = Ledger(db, "batch", 5000, 9, 100, stage_budget=1050)
    with pytest.raises(WorkflowError, match="stage budget"):
        ledger.reserve("two", "conflicts/b")
    monkeypatch.setenv("BERIL_AGENTIC_STAGE", "topics")
    assert ledger.reserve("two", "topics/b") is None


def test_read_tools_bound_ranges_and_reject_escape(tmp_path):
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/a.md").write_text("0123456789")
    reader = ReadTools(tmp_path, limit=8)
    assert reader.read("staging/a.md", 2, 5)["text"] == "234"
    with pytest.raises(WorkflowError):
        reader.read("../outside", 0, 1)
    with pytest.raises(WorkflowError):
        reader.read("staging/a.md", -1, 3)
    with pytest.raises(WorkflowError, match="budget"):
        reader.read("staging/a.md", 0, 6)


def test_chunks_and_exact_quote_validation():
    from beril_wiki.agentic.batch import chunks, validate_evidence

    text = "αβγ\n" * 20
    pieces = list(chunks(text, 13))
    assert "".join(text[a:b] for a, b in pieces) == text
    assert all(b - a <= 13 for a, b in pieces)
    validate_evidence(
        text,
        0,
        13,
        {
            "findings": [
                {"quote": "αβγ", "start": 0, "end": 3, "claim": "test", "kind": "finding"}
            ],
            "empty_reason": "",
        },
    )
    with pytest.raises(WorkflowError, match="quote"):
        validate_evidence(
            text,
            0,
            13,
            {
                "findings": [
                    {"quote": "wrong", "start": 0, "end": 3, "claim": "test", "kind": "finding"}
                ],
                "empty_reason": "",
            },
        )


def test_patch_rejects_stale_ambiguous_and_overlapping_anchors():
    from beril_wiki.agentic.batch import reconstruct
    from beril_wiki.agentic.runtime import digest

    old = "# Title\n\nAlpha.\n\nBeta."
    candidate = {"base_hash": digest(old), "edits": [{"old": "Alpha.", "new": "Gamma."}]}
    assert reconstruct(old, candidate) == "# Title\n\nGamma.\n\nBeta."
    with pytest.raises(WorkflowError, match="base"):
        reconstruct(old + " changed", candidate)
    with pytest.raises(WorkflowError, match="anchor"):
        reconstruct("aaa", {"base_hash": digest("aaa"), "edits": [{"old": "a", "new": "b"}]})


def test_source_revision_not_source_membership(tmp_path):
    from beril_wiki.agentic.batch import changed_sources

    for directory in ("staging", "wiki/sources", "wiki/summaries"):
        (tmp_path / directory).mkdir(parents=True)
    for directory in ("staging", "wiki/sources"):
        (tmp_path / directory / "a__REPORT.md").write_text("old")
    (tmp_path / "wiki/summaries/a__REPORT.md").write_text("summary")
    import json

    from beril_wiki.agentic.runtime import file_hash

    (tmp_path / "state").mkdir()
    (tmp_path / "state/hashes.json").write_text(
        json.dumps({"a__REPORT.md": file_hash(tmp_path / "staging/a__REPORT.md")})
    )
    assert changed_sources(tmp_path) == []
    (tmp_path / "staging/a__REPORT.md").write_text("new")
    assert changed_sources(tmp_path) == ["a__REPORT.md"]


def test_promotion_recovers_all_three_trees(tmp_path):
    from beril_wiki.agentic.runner import promote, recover
    from beril_wiki.agentic.runtime import manifest

    work = tmp_path / ".agentic/work"
    for folder in ("wiki", "state", "staging"):
        (tmp_path / folder).mkdir()
        (tmp_path / folder / "old").write_text("old")
        (work / folder).mkdir(parents=True)
        (work / folder / "new").write_text("new")
    before = manifest(tmp_path, ("wiki", "state", "staging"))
    promote(tmp_path, work, before)
    recover(tmp_path)
    for folder in ("wiki", "state", "staging"):
        assert (tmp_path / folder / "new").read_text() == "new"
        assert not (tmp_path / folder / "old").exists()


def test_promotion_refuses_concurrent_edit(tmp_path):
    from beril_wiki.agentic.runner import promote
    from beril_wiki.agentic.runtime import manifest

    (tmp_path / "wiki").mkdir()
    path = tmp_path / "wiki/page.md"
    path.write_text("old")
    before = manifest(tmp_path, ("wiki", "state", "staging"))
    path.write_text("user edit")
    with pytest.raises(WorkflowError, match="changed"):
        promote(tmp_path, tmp_path / ".agentic/work", before)
    assert path.read_text() == "user edit"


def test_abstracts_require_evidence_and_requested_ids():
    from beril_wiki.stages.literature import abstracts_from_xml

    raw = b"""<PubmedArticleSet>
    <PubmedArticle><MedlineCitation><PMID>1</PMID><Article><ArticleTitle>A</ArticleTitle>
    <Abstract><AbstractText>Exact evidence.</AbstractText></Abstract></Article>
    </MedlineCitation></PubmedArticle>
    <PubmedArticle><MedlineCitation><PMID>2</PMID><Article><ArticleTitle>Title only</ArticleTitle>
    </Article></MedlineCitation></PubmedArticle></PubmedArticleSet>"""
    assert set(abstracts_from_xml(raw, {"1", "2"})) == {"1"}
    assert abstracts_from_xml(raw, {"3"}) == {}


def test_recorded_batch_groups_pages_and_preserves_failed_review(tmp_path, monkeypatch):
    import json

    from beril_wiki.agentic.batch import changed_sources, compile_batch
    from beril_wiki.agentic.runtime import Runtime, digest

    for directory in ("staging", "wiki", "state", "contract", "jobs"):
        (tmp_path / directory).mkdir()
    for sid in ("a", "b"):
        (tmp_path / f"staging/{sid}__REPORT.md").write_text("The observed yield was 42%.")
    (tmp_path / "contract/AGENTS.md").write_text("Cite exact findings.")
    agent = Runtime(
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "jobs"),
            run="test",
            max_tokens=1000,
            max_jobs=20,
            reserve_tokens=10,
        )
    )
    calls = []

    def recorded(messages, step):
        calls.append(step)
        if step.startswith("extract/"):
            return json.dumps(
                {
                    "findings": [
                        {
                            "quote": "The observed yield was 42%.",
                            "start": 0,
                            "end": 27,
                            "claim": "The observed yield was 42%.",
                            "kind": "finding",
                        }
                    ],
                    "empty_reason": "",
                }
            )
        if step.startswith("batch/plan"):
            return json.dumps(
                {
                    "pages": [
                        {
                            "path": "concepts/yield.md",
                            "title": "Yield",
                            "type": "Concept",
                            "sources": [sid],
                            "reason": "Integrate yield evidence",
                        }
                        for sid in ("a", "b")
                    ],
                    "coverage": [
                        {
                            "evidence": f"{sid}:0:0",
                            "concepts": ["concepts/yield.md"],
                            "summary_only": "",
                        }
                        for sid in ("a", "b")
                    ],
                }
            )
        payload = json.loads(messages[0]["content"].split("\n")[-1])
        sources = payload["job"]["sources"]
        body = "# Yield\n\nThe observed yield was 42%. [src: " + ", ".join(sources) + "]\n\n"
        if "summaries/" in step:
            body += "## Slots Into\n\n- [[concepts/yield]] — yield evidence."
        else:
            body += "## Open Directions\n\nTest reproducibility."
        return json.dumps(
            {
                "base_hash": digest(""),
                "content": body,
                "description": "Yield evidence",
                "accounted_evidence": {
                    c["evidence"]: body.split("\n\n")[1] for c in payload["coverage"]
                },
            }
        )

    monkeypatch.setattr(agent, "ask", recorded)
    monkeypatch.setattr(agent, "review", lambda *args: None)
    compile_batch(tmp_path, agent, ["a__REPORT.md", "b__REPORT.md"])
    assert calls.count("write/concepts/yield.md") == 1
    count = len(calls)
    compile_batch(tmp_path, agent, changed_sources(tmp_path))
    assert len(calls) == count
    before = (tmp_path / "wiki/concepts/yield.md").read_text()

    # A rejected extraction cannot advance accepted source copies or mutate pages.
    def reject(*args):
        raise WorkflowError("scientific review rejected")

    monkeypatch.setattr(agent, "review", reject)
    with pytest.raises(WorkflowError, match="review rejected"):
        compile_batch(tmp_path, agent, ["a__REPORT.md"])
    assert (tmp_path / "wiki/concepts/yield.md").read_text() == before


def test_interrupted_rename_is_recoverable(tmp_path, monkeypatch):
    from beril_wiki.agentic import runner
    from beril_wiki.agentic.runtime import manifest

    work = tmp_path / ".agentic/work"
    for folder in runner.TREES:
        (tmp_path / folder).mkdir()
        (tmp_path / folder / "old").write_text("old")
        (work / folder).mkdir(parents=True)
        (work / folder / "new").write_text("new")
    real_replace = runner.os.replace

    def interrupt(src, dst):
        if Path(src) == work / "wiki":
            raise OSError("simulated power interruption")
        return real_replace(src, dst)

    from pathlib import Path

    monkeypatch.setattr(runner.os, "replace", interrupt)
    with pytest.raises(OSError, match="interruption"):
        runner.promote(tmp_path, work, manifest(tmp_path, runner.TREES))
    assert not (tmp_path / "wiki").exists()
    monkeypatch.setattr(runner.os, "replace", real_replace)
    runner.recover(tmp_path)
    assert all((tmp_path / folder / "new").exists() for folder in runner.TREES)


def test_sdk_tool_server_and_auth_configuration(monkeypatch):
    import json
    from types import SimpleNamespace

    from claude_agent_sdk import create_sdk_mcp_server, tool

    from beril_wiki.agentic.runtime import AUTH_ENV, check_auth

    @tool("read", "read", {"path": str})
    async def read(args):
        return {"content": [{"type": "text", "text": args["path"]}]}

    assert create_sdk_mcp_server("test", tools=[read])["type"] == "sdk"

    def auth_run(*args, **kwargs):
        assert all(not kwargs["env"][key] for key in AUTH_ENV)
        return SimpleNamespace(
            returncode=0,
            stdout=json.dumps(
                {
                    "loggedIn": True,
                    "authMethod": "claude.ai",
                    "apiProvider": "firstParty",
                    "subscriptionType": "max",
                }
            ),
        )

    monkeypatch.setattr("beril_wiki.agentic.runtime.subprocess.run", auth_run)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "must-not-be-used")
    check_auth("claude")


def test_real_stage_subprocess_respects_snapshot_root(tmp_path):
    import json

    from beril_wiki.agentic.runner import run_stage

    live = tmp_path / "live"
    live.mkdir()
    (live / "wiki").mkdir()
    (live / "wiki/sentinel.md").write_text("unchanged")
    work = tmp_path / "work"
    (work / "reference/projects/demo/figures").mkdir(parents=True)
    (work / "reference/projects/demo/REPORT.md").write_text("![plot](figures/plot.png)")
    (work / "reference/projects/demo/figures/plot.png").write_bytes(b"figure")
    config = tmp_path / "config.json"
    config.write_text(json.dumps({"root": str(work)}))
    run_stage(work, config, "fetch", "stages.fetch", [])
    assert (work / "wiki/figures/demo/plot.png").read_bytes() == b"figure"
    assert (work / "staging/demo__REPORT.md").exists()
    assert list((live / "wiki").iterdir()) == [live / "wiki/sentinel.md"]


@pytest.mark.parametrize("failed_stage", ["authors", "check"])
def test_runner_stage_order_noop_and_failed_gate(tmp_path, monkeypatch, failed_stage):
    from types import SimpleNamespace

    from beril_wiki.agentic import runner
    from beril_wiki.agentic.runtime import manifest

    root, checkout = tmp_path / "repo", tmp_path / "checkout"
    for folder in (*runner.TREES, "contract"):
        (root / folder).mkdir(parents=True)
    (root / "contract/AGENTS.md").write_text("Contract")
    (checkout / "ui/config").mkdir(parents=True)
    (checkout / "ui/config/collections.yaml").write_text("collections: []")
    config = dict(cli="claude", model="test", max_tokens=100, max_jobs=5, reserve_tokens=10)
    monkeypatch.setattr(
        runner.subprocess, "run", lambda *a, **k: SimpleNamespace(stdout="test CLI")
    )
    calls = []

    def recorded_stage(work, config_path, name, module, args):
        calls.append(name)
        assert work != root
        if name == "check":
            assert "--strict" in args
        (work / "wiki" / f"{name}.md").write_text(name)

    from agentic_recording import reply

    monkeypatch.setattr(runner.Runtime, "ask", reply)
    monkeypatch.setattr(runner, "run_stage", recorded_stage)
    runner.run(root, checkout, config)
    assert calls == [
        "fetch",
        "decisions",
        "extras",
        "names-core",
        "conflicts",
        "topics",
        "literature",
        "authors",
        "names",
        "figures",
        "check",
    ]
    calls.clear()
    assert runner.run(root, checkout, config) == {"unchanged": True}
    assert calls == []
    before = manifest(root, runner.TREES)

    def fail_gate(work, config_path, name, module, args):
        recorded_stage(work, config_path, name, module, args)
        if name == failed_stage:
            from beril_wiki.agentic.runtime import CandidateError

            raise CandidateError("strict gate rejected")

    monkeypatch.setattr(runner, "run_stage", fail_gate)
    (checkout / "ui/config/collections.yaml").write_text("collections: []\n# new metadata")
    with pytest.raises(WorkflowError, match="strict gate"):
        runner.run(root, checkout, config | {"model": "changed"})
    assert manifest(root, runner.TREES) == before


def test_source_numbers_invalidates_same_length_revision():
    from beril_wiki.check import source_numbers

    assert "42" in source_numbers("revised", "42%")
    assert "56" in source_numbers("revised", "56%")
    assert "42" not in source_numbers("revised", "56%")


def test_actual_pipeline_with_recorded_replies(tmp_path, monkeypatch):
    import json
    from pathlib import Path

    from agentic_recording import reply
    from beril_wiki.agentic.runner import run
    from beril_wiki.agentic.runtime import Runtime

    root, checkout = tmp_path / "repo", tmp_path / "observatory"
    (root / "contract").mkdir(parents=True)
    (root / "contract/AGENTS.md").write_text("Cite exact measurements; preserve caveats.")
    for sid, value in (("a", "42"), ("b", "56")):
        project = checkout / "projects" / sid
        (project / "figures").mkdir(parents=True)
        (project / "REPORT.md").write_text(f"Yield was {value}%.\n\n![Yield](figures/yield.png)")
        (project / "README.md").write_text("## Authors\n\n- Ada Example\n")
        (project / "figures/yield.png").write_bytes(b"recorded-image")
    (checkout / "ui/config").mkdir(parents=True)
    (checkout / "ui/config/collections.yaml").write_text("collections: []")
    (tmp_path / "sitecustomize.py").write_text("from agentic_recording import install\ninstall()\n")
    monkeypatch.setenv("PYTHONPATH", f"{tmp_path}:{Path(__file__).parent.resolve()}")
    steps: list[str] = []

    def counted(self, messages, step):
        steps.append(step)
        return reply(self, messages, step)

    monkeypatch.setattr(Runtime, "ask", counted)
    config = dict(cli="/usr/bin/true", model="recorded", max_tokens=100000, max_jobs=100)
    run(root, checkout, config)
    for path in (
        "concepts/yield.md",
        "summaries/a__REPORT.md",
        "topics/yield-studies.md",
        "authors/ada-example.md",
        "opportunities.md",
        "negative-results.md",
    ):
        assert (root / "wiki" / path).exists(), path
    assert list((root / "wiki/conflicts").glob("*.md"))
    assert "Literature Context" in (root / "wiki/topics/yield-studies.md").read_text()
    placement_path = root / "state/figures-placements.json"
    placements = json.loads(placement_path.read_text())
    assert placements
    assert all(p["caption"] == "Yield" for page in placements.values() for p in page["placements"])
    assert run(root, checkout, config) == {"unchanged": True}
    config = config | {"step_models": {"figures": "figure-model"}}
    steps.clear()
    run(root, checkout, config)
    assert steps == []  # figure routing does not repeat extraction or curator decisions
    assert (
        json.loads((root / "state/agentic.json").read_text())["models"]["figures"] == "figure-model"
    )
    assert run(root, checkout, config) == {"unchanged": True}
    placement_path.unlink()
    steps.clear()
    run(root, checkout, config)
    assert json.loads(placement_path.read_text()) == placements
    assert not any(step.startswith("curator/") for step in steps)


@pytest.mark.parametrize("merge", [False, True])
def test_reprocessing_unchanged_sources_keeps_retention_guard(tmp_path, monkeypatch, merge):
    import json

    from beril_wiki.agentic.batch import compile_batch
    from beril_wiki.agentic.runtime import Runtime, digest

    for folder in ("staging", "wiki/sources", "wiki/concepts", "state", "jobs", "contract"):
        (tmp_path / folder).mkdir(parents=True)
    texts = {"a": "1234 cells were observed.", "b": "Yield was 56%."}
    for sid, text in texts.items():
        for folder in ("staging", "wiki/sources"):
            (tmp_path / folder / f"{sid}__REPORT.md").write_text(text)
    path = tmp_path / "wiki/concepts/cells.md"
    path.write_text(
        "# Cells\n\n1234 cells were observed. [src: a]\n\nYield was 56%. [src: b]"
        "\n\n## Open Directions\n\nMeasure more cells."
    )
    if merge:
        (tmp_path / "wiki/concepts/other.md").write_text(path.read_text())
    agent = Runtime(
        dict(
            root=str(tmp_path),
            store=str(tmp_path / "jobs"),
            run="test",
            max_tokens=1000,
            max_jobs=20,
            reserve_tokens=10,
        )
    )

    def drop_old_number(messages, step):
        if step.startswith("extract"):
            data = json.loads(messages[0]["content"].split("\n")[-1])
            text = data["text"]
            return json.dumps(
                {
                    "findings": [
                        {
                            "quote": text,
                            "claim": text,
                            "start": 0,
                            "end": len(text),
                            "kind": "finding",
                        }
                    ],
                    "empty_reason": "",
                }
            )
        if step.startswith("batch/plan"):
            return json.dumps(
                {
                    "pages": [
                        {
                            "path": "concepts/cells.md",
                            "title": "Cells",
                            "type": "Concept",
                            "sources": ["a", "b"],
                            "reason": "Reprocess",
                            "merge_from": ["concepts/other.md"] if merge else [],
                        }
                    ],
                    "coverage": [
                        {
                            "evidence": f"{sid}:0:0",
                            "concepts": ["concepts/cells.md"],
                            "summary_only": "",
                        }
                        for sid in texts
                    ],
                }
            )
        return json.dumps(
            {
                "base_hash": digest(path.read_text()),
                "description": "Cells",
                "content": "# Cells\n\nCells were observed. [src: a]\n\nYield was 56%. [src: b]"
                "\n\n## Open Directions\n\nMeasure more cells.",
                "rewrite_reason": "shorten",
            }
        )

    monkeypatch.setattr(agent, "ask", drop_old_number)
    monkeypatch.setattr(agent, "review", lambda *args: None)
    with pytest.raises(WorkflowError, match="unchanged citations or quantities"):
        compile_batch(tmp_path, agent, ["a__REPORT.md", "b__REPORT.md"])
    assert "1234" in path.read_text()


@pytest.mark.parametrize(
    "case",
    ["missing_result", "missing_usage", "null_cache", "max_tokens", "api_error", "wrong_auth"],
)
def test_sdk_failure_results_are_accounted_or_blocked(tmp_path, monkeypatch, case):
    from claude_agent_sdk import ResultMessage, SystemMessage

    from beril_wiki.agentic import runtime as module

    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Contract")
    config = dict(
        root=str(tmp_path),
        store=str(tmp_path / "jobs"),
        run="test",
        model="test",
        cli="claude",
        max_tokens=1000,
        max_jobs=5,
        reserve_tokens=10,
    )
    agent = module.Runtime(config)
    monkeypatch.setattr(module, "check_auth", lambda cli: None)

    async def recorded_query(**kwargs):
        assert kwargs["options"].tools == []
        assert kwargs["options"].env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] == "32768"
        yield SystemMessage(
            subtype="init", data={"apiKeySource": "api" if case == "wrong_auth" else "none"}
        )
        if case == "missing_result":
            return
        usage = {"input_tokens": 3, "output_tokens": 5}
        if case == "null_cache":
            usage["cache_read_input_tokens"] = None
        yield ResultMessage(
            subtype="success",
            duration_ms=0,
            duration_api_ms=0,
            is_error=False,
            num_turns=1,
            session_id="recorded",
            result="answer",
            usage=None if case == "missing_usage" else usage,
            stop_reason="max_tokens" if case == "max_tokens" else "end_turn",
            api_error_status=429 if case == "api_error" else None,
        )

    monkeypatch.setattr(module, "query", recorded_query)
    with pytest.raises(WorkflowError):
        agent.ask([{"role": "user", "content": "test"}], "test")
    status, tokens = agent.ledger.db.execute("SELECT status,tokens FROM jobs").fetchone()
    if case in ("api_error", "max_tokens"):
        assert (status, tokens) == ("failed", 8)
    else:
        assert status in ("pending", "unknown") and tokens is None


def test_auth_failure_does_not_reserve_and_cached_output_survives_cli_update(tmp_path, monkeypatch):
    from beril_wiki.agentic import runtime as module

    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Contract")
    config = dict(
        root=str(tmp_path),
        store=str(tmp_path / "jobs"),
        run="test",
        model="test",
        cli="claude",
        revision="old-cli",
        max_tokens=1000,
        max_jobs=5,
        reserve_tokens=10,
    )
    agent = module.Runtime(config)

    def no_login(cli):
        raise WorkflowError("no login")

    monkeypatch.setattr(module, "check_auth", no_login)
    messages = [{"role": "user", "content": "test"}]
    with pytest.raises(WorkflowError, match="no login"):
        agent.ask(messages, "test")
    assert agent.ledger.db.execute("SELECT count(*) FROM jobs").fetchone()[0] == 0
    monkeypatch.setattr(module, "check_auth", lambda cli: None)

    async def answer(payload, key):
        agent.ledger.finish(key, "saved", {"input_tokens": 3, "output_tokens": 5})
        return "saved"

    monkeypatch.setattr(agent, "_query", answer)
    assert agent.ask(messages, "test") == "saved"
    restarted = module.Runtime(config | {"revision": "new-cli"})
    monkeypatch.setattr(module, "check_auth", no_login)
    assert restarted.ask(messages, "test") == "saved"


def test_planning_batches_and_overlapping_anchors():
    from beril_wiki.agentic.batch import planning_batches, reconstruct
    from beril_wiki.agentic.runtime import digest

    findings = [{"id": str(i), "claim": "evidence", "quote": "q" * 1000} for i in range(10)]
    batches = planning_batches(findings, 100)
    assert len(batches) > 1
    assert [f["id"] for batch in batches for f in batch] == [str(i) for i in range(10)]
    assert all("quote" not in f for batch in batches for f in batch)
    with pytest.raises(WorkflowError, match="overlap"):
        reconstruct(
            "abcdef",
            {
                "base_hash": digest("abcdef"),
                "edits": [{"old": "abc", "new": "X"}, {"old": "bcd", "new": "Y"}],
            },
        )


def test_large_hub_previews_keep_retrieval_references():
    from beril_wiki.agentic.runtime import page_context

    context = "\n".join(page_context(f"wiki/concepts/page-{i}.md", "x" * 62000) for i in range(9))
    assert len(context.encode()) < 100000
    assert context.count("PREVIEW ONLY") == 9
    assert "wiki/concepts/page-8.md has 62000 characters" in context


def test_downstream_sdk_routing_skips_api_and_mechanical_review(monkeypatch):
    import litellm

    from beril_wiki import compiler
    from beril_wiki.agentic import runtime as module

    monkeypatch.setenv("BERIL_AGENTIC_CONFIG", "enabled")

    def no_api(**kwargs):
        raise AssertionError("API called")

    monkeypatch.setattr(litellm, "completion", no_api)
    calls = []

    def sdk(messages, step, review=True):
        calls.append((step, review))
        return "{}"

    monkeypatch.setattr(module, "text_completion", sdk)
    module.completion(messages=[], step="figures/test", review=False)
    compiler.llm([], "test/queries")
    assert calls == [("figures/test", False), ("test/queries", False)]


def test_reconcile_and_explicit_retry_keep_prior_charge(tmp_path, monkeypatch):
    import json
    import sys

    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import runtime as module

    (tmp_path / "contract").mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Contract")
    config = dict(
        root=str(tmp_path),
        store=str(tmp_path / ".agentic"),
        run="test",
        model="test",
        cli="claude",
        max_tokens=100,
        max_jobs=3,
        reserve_tokens=20,
    )
    agent = module.Runtime(config)
    (tmp_path / ".agentic/config.json").write_text(json.dumps(config))
    monkeypatch.setattr(module, "check_auth", lambda cli: None)

    async def crash(*args):
        raise WorkflowError("interrupted")

    monkeypatch.setattr(agent, "_query", crash)
    messages = [{"role": "user", "content": "test"}]
    with pytest.raises(WorkflowError):
        agent.ask(messages, "test")
    key = agent.ledger.db.execute("SELECT key FROM jobs").fetchone()[0]
    monkeypatch.setattr(
        sys, "argv", ["agentic", "--root", str(tmp_path), "account", "--job", key, "--tokens", "50"]
    )
    assert cli.main() == 0
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "retry", "--job", key])
    assert cli.main() == 0
    restarted = module.Runtime(config)

    async def answer(payload, new_key):
        assert new_key != key
        restarted.ledger.finish(new_key, "answer", {"input_tokens": 3, "output_tokens": 5})
        return "answer"

    monkeypatch.setattr(restarted, "_query", answer)
    assert restarted.ask(messages, "test") == "answer"
    assert restarted.ledger.totals()["tokens"] == 58


@pytest.mark.parametrize("refuse_first", [False, True])
def test_entity_merges_reresolve_transitive_pairs_and_continue(tmp_path, monkeypatch, refuse_first):
    import sys

    from beril_wiki.stages import entities

    for folder in ("contract", "staging", "state", "wiki"):
        (tmp_path / folder).mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Contract")
    (tmp_path / "staging/a__REPORT.md").write_text("evidence")
    alive = [
        {
            "stem": name,
            "type": "organism",
            "sources": count,
            "key": "same",
            "slug_key": name,
            "ids": {"taxid:2"},
            "aliases": set(),
        }
        for name, count in (("first", 3), ("second", 2), ("third", 1))
    ]
    calls = []

    def merge(root, loser, survivor, *args, **kwargs):
        assert loser in {p["stem"] for p in alive}
        calls.append((loser, survivor))
        if refuse_first and len(calls) == 1:
            return False
        alive[:] = [p for p in alive if p["stem"] != loser]
        return True

    monkeypatch.setattr(entities, "ROOT", tmp_path)
    monkeypatch.setattr(entities, "load", lambda root: list(alive))
    monkeypatch.setattr(entities, "apply_merge", merge)
    monkeypatch.setattr(sys, "argv", ["entities", "--root", str(tmp_path), "--apply"])
    assert entities.main() == int(refuse_first)
    assert len(calls) == 2
    assert len(alive) == (2 if refuse_first else 1)


def test_figure_cache_tracks_candidates_and_missing_results(tmp_path, monkeypatch):
    import json
    from types import SimpleNamespace

    from beril_wiki.stages import figures as F

    for folder in ("wiki/sources", "wiki/figures/a", "wiki/summaries", "state"):
        (tmp_path / folder).mkdir(parents=True)
    report = tmp_path / "wiki/sources/a__REPORT.md"
    report.write_text("![Original](figures/plot.png)")
    (tmp_path / "wiki/figures/a/plot.png").write_bytes(b"synthetic-image")
    (tmp_path / "wiki/summaries/a__REPORT.md").write_text("# Yield\n\nMeasured yield. [src: a]")
    monkeypatch.setattr(F, "ROOT", tmp_path)
    monkeypatch.setattr(F, "STATE", tmp_path / "state")
    monkeypatch.setattr(F, "configured", lambda: True)
    monkeypatch.setattr(F.sys, "argv", ["figures"])
    calls = []

    def completion(**kwargs):
        assert '"caption"' not in kwargs["messages"][0]["content"]
        assert "Incomplete paragraph previews" in kwargs["messages"][1]["content"]
        calls.append(kwargs)
        return SimpleNamespace(
            choices=[
                SimpleNamespace(
                    message=SimpleNamespace(
                        content=json.dumps(
                            {"placements": [{"figure": 0, "after_paragraph": 1}] * 3}
                        )
                    )
                )
            ]
        )

    monkeypatch.setattr(F, "completion", completion)
    F.main()
    F.main()
    assert len(calls) == 1
    stored = json.loads((tmp_path / "state/figures-placements.json").read_text())
    assert len(stored["summaries/a__REPORT.md"]["placements"]) == 2
    report.write_text("![Revised](figures/plot.png)")
    F.main()
    assert len(calls) == 2
    placements = tmp_path / "state/figures-placements.json"
    assert (
        json.loads(placements.read_text())["summaries/a__REPORT.md"]["placements"][0]["caption"]
        == "Revised"
    )
    placements.unlink()
    F.main()
    assert len(calls) == 3


def test_figure_failures_and_queue_preservation(tmp_path, monkeypatch):
    import json
    from types import SimpleNamespace

    from beril_wiki.stages import figures as F

    (tmp_path / "wiki/topics").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    for name in ("a", "b"):
        (tmp_path / f"wiki/topics/{name}.md").write_text("# Yield\n\nYield. [src: a]")
    monkeypatch.setattr(F, "ROOT", tmp_path)
    monkeypatch.setattr(F, "STATE", tmp_path / "state")
    monkeypatch.setattr(F, "configured", lambda: True)
    monkeypatch.setattr(
        F,
        "build_manifest",
        lambda: {"a": [{"file": "figures/a.png", "caption": "Yield", "context": "Yield"}]},
    )
    monkeypatch.setattr(F.sys, "argv", ["figures"])
    flags = True

    def answer(**kwargs):
        text = json.dumps({"placements": [], "csv_flags": [kwargs["step"]] if flags else []})
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text))])

    monkeypatch.setattr(F, "completion", answer)
    F.main()
    path = tmp_path / "wiki/topics/a.md"
    path.write_text(path.read_text() + "\nChanged.")
    F.main()
    queue = F.STATE / "figures-csv-queue.md"
    assert "topics/b.md" in queue.read_text()
    (tmp_path / "wiki/topics/b.md").unlink()
    flags = False
    path.write_text(path.read_text() + "\nAgain.")
    F.main()
    assert not queue.exists()
    placements = F.STATE / "figures-placements.json"
    assert "topics/b.md" not in json.loads(placements.read_text())
    before = placements.read_text()
    for bad in (
        "not JSON",
        "{}",
        '{"placements": [{"figure": -1, "after_paragraph": 0}]}',
        '{"placements": [{"figure": true, "after_paragraph": 0}]}',
    ):
        monkeypatch.setattr(
            F,
            "completion",
            lambda response=bad, **kw: SimpleNamespace(
                choices=[SimpleNamespace(message=SimpleNamespace(content=response))]
            ),
        )
        (F.STATE / "figures-state.json").unlink(missing_ok=True)
        with pytest.raises(WorkflowError):
            F.main()
        assert placements.read_text() == before
