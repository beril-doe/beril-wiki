"""Offline safety and resume contracts for the subscription compiler."""

import pytest

from beril_wiki.agentic.runtime import Ledger, ReadTools, WorkflowError
from beril_wiki.check import all_paragraphs


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


def test_usd_cap_counts_every_run_and_open_paid_jobs(tmp_path):
    db = tmp_path / "jobs.sqlite"
    usage = {"input_tokens": 1, "output_tokens": 1}
    caps = {"links": 1.0}
    first = Ledger(db, "run-a", 10**9, 99, 1, usd_caps=caps, usd_reserve=0.4)
    first.reserve("a", "links/p1", "claude-sonnet-5-5")
    first.finish("a", "ok", usage, cost=0.25)
    # A resumed run under a new id still sees the first run's spend.
    second = Ledger(db, "run-b", 10**9, 99, 1, usd_caps=caps, usd_reserve=0.4)
    second.reserve("b", "links/p2", "claude-sonnet-5-5")  # 0.25 + 0.4 * 1 <= 1.0
    with pytest.raises(WorkflowError, match="USD cap admission refused: links"):
        # 0.25 spent + 0.4 for b in flight + 0.4 for this job > 1.0
        second.reserve("c", "links/p3", "claude-sonnet-5-5")
    # Reviewers on the subscription and other stages are not capped.
    assert second.reserve("r", "links/p3/science-review", "gpt-6.1-sol") is None
    assert second.reserve("g", "gists/x", "claude-sonnet-5-5") is None
    # A finished paid job with no recorded cost keeps counting its reserve.
    second.finish("b", "ok", usage)
    with pytest.raises(WorkflowError, match="open=1"):
        second.reserve("c", "links/p3", "claude-sonnet-5-5")
    assert second.stage_usd("links") == 0.25
    with pytest.raises(ValueError):
        Ledger(db, "run-c", 10, 9, 1, usd_caps={"links": 0})
    for bad in ({"links": float("nan")}, {"links": float("inf")}):
        with pytest.raises(ValueError):
            Ledger(db, "run-c", 10, 9, 1, usd_caps=bad)
    with pytest.raises(ValueError):
        Ledger(db, "run-c", 10, 9, 1, usd_caps=caps, usd_reserve=float("nan"))


def test_usd_cap_counts_claude_aliases(tmp_path):
    """A Claude model named by alias is served and billed like a claude- ID."""
    ledger = Ledger(tmp_path / "j.sqlite", "r", 10**9, 99, 1, usd_caps={"links": 1.0})
    ledger.reserve("a", "links/p1", "sonnet")
    ledger.finish("a", "ok", {"input_tokens": 1, "output_tokens": 1}, cost=0.9)
    with pytest.raises(WorkflowError, match="USD cap"):
        ledger.reserve("b", "links/p2", "sonnet")


def test_usd_and_codex_caps_refuse_admission_per_backend(tmp_path):
    ledger = Ledger(
        tmp_path / "jobs.sqlite",
        "pilot",
        10**9,
        99,
        10,
        caps={"max_usd": 5, "max_codex_tokens": 10**6},
    )
    usage = {"input_tokens": 10, "output_tokens": 10}
    ledger.reserve("a", "write/x", "claude-sonnet-5-5")
    ledger.finish("a", "ok", usage, cost=3.5)
    with pytest.raises(WorkflowError, match="Claude USD"):
        ledger.reserve("b", "write/y", "claude-haiku-5-5")  # 3.5 spent + 2 held > 5
    ledger.reserve("c", "write/x/science-review", "gpt-6.1-sol")
    ledger.finish("c", "ok", {"input_tokens": 600_000, "output_tokens": 100_000})
    with pytest.raises(WorkflowError, match="Codex tokens"):
        ledger.reserve("d", "write/y/science-review", "gpt-6.1-sol")
    # A pending job counts at its hold: a page session holds its whole session budget,
    # so a job admitted near the edge cannot carry the run past the cap.
    capped = Ledger(tmp_path / "held.sqlite", "pilot", 10**9, 99, 10, caps={"max_usd": 9})
    capped.reserve("s1", "write/a", "claude-sonnet-5-5", hold=8.0)
    with pytest.raises(WorkflowError, match="Claude USD 8.00 spent or held"):
        capped.reserve("s2", "write/b", "claude-sonnet-5-5")
    # A job that ends without a reported cost keeps its hold rather than counting as 0.
    capped.finish("s1", "", usage, "interrupted: killed")
    assert capped.db.execute("SELECT cost FROM jobs WHERE key='s1'").fetchone() == (8.0,)
    # Another run, or no model named, is not held to this run's caps.
    assert Ledger(tmp_path / "jobs.sqlite", "other", 10**9, 99, 10).reserve("e", "x") is None


def test_one_hour_cache_writes_count_at_their_price():
    from beril_wiki.agentic.runtime import effective_tokens

    usage = {"input_tokens": 0, "output_tokens": 0, "cache_creation_input_tokens": 1000}
    assert effective_tokens(usage) == 1250
    split = usage | {"cache_creation": {"ephemeral_1h_input_tokens": 600}}
    assert effective_tokens(split) == 600 * 2 + 400 * 1.25
    # A split larger than the total it splits is malformed: charge the plain weight.
    assert effective_tokens(usage | {"cache_creation": {"ephemeral_1h_input_tokens": 5000}}) == 1250


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
    from beril_wiki.agentic.runtime import CandidateError

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
    snapped = validate_evidence(
        text,
        0,
        13,
        {
            "findings": [
                {"quote": "βγ\n", "start": 0, "end": 3, "claim": "test", "kind": "finding"}
            ],
            "empty_reason": "",
        },
    )
    assert (snapped.findings[0].start, snapped.findings[0].end) == (1, 4)
    with pytest.raises(CandidateError, match="kind"):
        validate_evidence(
            text,
            0,
            13,
            {
                "findings": [
                    {
                        "quote": "\u03b1\u03b2\u03b3",
                        "start": 0,
                        "end": 3,
                        "claim": "t",
                        "kind": "dataset",
                    }
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

    from beril_wiki.agentic import batch
    from beril_wiki.agentic.batch import Coverage, PageJob, Plan, changed_sources, compile_batch
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
                    c["evidence"]: all_paragraphs(body).index(body.split("\n\n")[1])
                    for c in payload["coverage"]
                },
            }
        )

    monkeypatch.setattr(agent, "ask", recorded)
    plan = Plan(
        pages=[
            PageJob(
                path="concepts/yield.md",
                title="Yield",
                type="Concept",
                sources=[sid],
                reason="Integrate yield evidence",
            )
            for sid in ("a", "b")
        ],
        coverage=[
            Coverage(evidence=f"{sid}:0:0", concepts=["concepts/yield.md"], summary_only="")
            for sid in ("a", "b")
        ],
    )
    # Routing has its own tests; this one is about grouping and failed reviews.
    monkeypatch.setattr(batch, "route_plan", lambda root, agent, findings: plan)
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
        "headlines",
        "novelty",
        "directions",
        "gists",
        "links",
        "shared",
        "outcomes",
        "followups",
        "titles",
        "names",
        "errata",
        "figures",
        "check",
    ]
    calls.clear()
    assert runner.run(root, checkout, config) == {"unchanged": True}
    assert calls == []
    # A model change no longer reruns derived stages; a changed input does.
    (root / "wiki/summaries").mkdir(exist_ok=True)
    (root / "wiki/summaries/new__REPORT.md").write_text("A new summary.")
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


def test_older_revision_scheme_and_model_change_adopt_accepted_wiki(tmp_path, monkeypatch):
    """A state accepted under the previous revision scheme, then a new writing model,
    must neither re-integrate sources nor rerun derived stages or force figures."""
    import json
    from types import SimpleNamespace

    from beril_wiki.agentic import runner
    from beril_wiki.agentic.curator import curate as runner_curate

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
        calls.append((name, tuple(args)))
        (work / "wiki" / f"{name}.md").write_text(name)

    from agentic_recording import reply

    monkeypatch.setattr(runner.Runtime, "ask", reply)
    monkeypatch.setattr(runner, "run_stage", recorded_stage)
    runner.run(root, checkout, config)
    # Re-stamp the accepted state as a scheme-4 state: every revision formula differs.
    state_path = root / "state/agentic.json"
    state = json.loads(state_path.read_text())
    state.update(revision="scheme-4", revision_scheme=4, figure_revision="scheme-4")
    state["fingerprint"] = "scheme-4"
    for snapshot in state["editorial"].values():
        snapshot["semantic"] = "scheme-4"
    state_path.write_text(json.dumps(state))
    integrated = []
    monkeypatch.setattr(
        runner, "curate", lambda *a, **k: integrated.append(a[2]) or runner_curate(*a, **k)
    )
    for policy in (config, config | {"step_models": {"writing": "other", "planning": "other"}}):
        calls.clear()
        integrated.clear()
        runner.run(root, checkout, policy)
        names = [name for name, _ in calls]
        assert not {"conflicts", "topics", "literature", "authors"} & set(names), names
        assert ("figures", ("--force",)) not in calls
        assert integrated == [[]]
        state = json.loads(state_path.read_text())
        assert state["revision_scheme"] == runner.REVISION_SCHEME


def test_plan_compares_a_scheme_4_state_as_the_next_run_adopts_it(tmp_path):
    """plan lists no stage the next run would adopt rather than rerun."""
    import json

    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import curator as C
    from beril_wiki.agentic.runner import REVISION_SCHEME

    for folder in ("state", "contract", "wiki"):
        (tmp_path / folder).mkdir()
    (tmp_path / "contract/AGENTS.md").write_text("Contract")
    (tmp_path / "agentic.yaml").write_text("model: m\n")
    stages = ("conflicts", "authors")
    editorial = {n: C.stage_snapshot(tmp_path, n) | {"semantic": "scheme-4"} for n in stages}
    state = {"version": 2, "revision_scheme": 4, "editorial": editorial}
    path = tmp_path / "state/agentic.json"
    path.write_text(json.dumps(state))
    assert not set(stages) & set(cli.plan(tmp_path)["pending_editorial"])
    # The same snapshots accepted under the current scheme are stale.
    path.write_text(json.dumps(state | {"revision_scheme": REVISION_SCHEME}))
    assert set(stages) <= set(cli.plan(tmp_path)["pending_editorial"])


def test_a_recorded_contract_change_is_not_adopted(tmp_path, monkeypatch):
    """Adoption keeps the accepted wiki only under the contract it was written to."""
    import json
    from types import SimpleNamespace

    from beril_wiki.agentic import runner

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
        (work / "wiki" / f"{name}.md").write_text(name)

    from agentic_recording import reply

    monkeypatch.setattr(runner.Runtime, "ask", reply)
    monkeypatch.setattr(runner, "run_stage", recorded_stage)
    runner.run(root, checkout, config)
    state_path = root / "state/agentic.json"
    state = json.loads(state_path.read_text())
    assert state["contract"]
    state.update(revision_scheme=4, fingerprint="old")
    state_path.write_text(json.dumps(state))
    (root / "contract/AGENTS.md").write_text("A new rule.")
    calls.clear()
    runner.run(root, checkout, config)
    assert {"conflicts", "topics", "literature", "authors"} <= set(calls)


def test_budget_run_keeps_one_cap_across_bases(tmp_path, monkeypatch):
    """A refresh onto a moved main changes the input digest, which named a new ledger
    run and let the earlier spend stop counting against the cap. Each invocation gets
    its own max_jobs and max_tokens: a resume on the same inputs counted the earlier
    attempts' jobs and tokens, which the person cannot raise, against them."""
    import json
    from types import SimpleNamespace

    from beril_wiki.agentic import runner

    root, checkout = tmp_path / "repo", tmp_path / "checkout"
    for folder in (*runner.TREES, "contract"):
        (root / folder).mkdir(parents=True)
    (root / "contract/AGENTS.md").write_text("Contract")
    (checkout / "ui/config").mkdir(parents=True)
    (checkout / "ui/config/collections.yaml").write_text("collections: []")
    config: dict[str, object] = {"cli": "claude", "model": "test", "max_tokens": 12}
    config |= {"max_jobs": 1, "reserve_tokens": 10, "max_usd": 30.0, "budget_run": "wiki/p"}
    monkeypatch.setattr(
        runner.subprocess, "run", lambda *a, **k: SimpleNamespace(stdout="test CLI")
    )
    seen = []

    def recorded_stage(work, config_path, name, module, args):
        (work / "wiki" / f"{name}.md").write_text(name)
        if name != "fetch":
            return
        stored = json.loads(config_path.read_text())
        ledger = runner.Runtime(stored).ledger
        key = f"job-{len(seen)}"
        try:
            ledger.reserve(key, "write/x", "claude-sonnet-5-5")
        except WorkflowError as exc:
            seen.append((stored["run"], stored["run_inputs"], str(exc)))
            return
        ledger.finish(key, "ok", {"input_tokens": 3, "output_tokens": 2}, cost=costs.pop(0))
        with pytest.raises(WorkflowError, match="jobs=1, effective=5"):
            ledger.reserve(key + "-more", "write/y", "claude-sonnet-5-5")
        seen.append((stored["run"], stored["run_inputs"], "admitted"))
        if len(seen) == 1:
            raise WorkflowError("stopped before acceptance")

    from agentic_recording import reply

    monkeypatch.setattr(runner.Runtime, "ask", reply)
    monkeypatch.setattr(runner, "run_stage", recorded_stage)
    costs = [20.0, 9.0]
    with pytest.raises(WorkflowError, match="stopped"):
        runner.run(root, checkout, config)
    # A resume of the stopped run, on the same snapshot.
    runner.run(root, checkout, config)
    (root / "wiki/other.md").write_text("another project merged to main\n")
    runner.run(root, checkout, config)
    (first, first_inputs, a), (second, second_inputs, b), (third, third_inputs, c) = seen
    assert first == second == third == "wiki/p"
    assert first_inputs == second_inputs != third_inputs
    assert (a, b) == ("admitted", "admitted")
    assert "Claude USD 29.00" in c


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

    from beril_wiki.agentic import batch
    from beril_wiki.agentic.batch import Coverage, PageJob, Plan, compile_batch
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
    plan = Plan(
        pages=[
            PageJob(
                path="concepts/cells.md",
                title="Cells",
                type="Concept",
                sources=["a", "b"],
                reason="Reprocess",
                merge_from=["concepts/other.md"] if merge else [],
            )
        ],
        coverage=[
            Coverage(evidence=f"{sid}:0:0", concepts=["concepts/cells.md"], summary_only="")
            for sid in texts
        ],
    )
    # The router proposes no merges; a merge plan reaches the writer this way only.
    monkeypatch.setattr(batch, "route_plan", lambda root, agent, findings: plan)
    monkeypatch.setattr(agent, "review", lambda *args: None)
    compile_batch(tmp_path, agent, ["a__REPORT.md", "b__REPORT.md"])
    # The guard holds: the page keeps its number, the failure is recorded, the run goes on.
    assert "1234" in path.read_text()
    failures = json.loads((agent.store / "failures.json").read_text())
    assert "unchanged citations or quantities" in failures["concepts/cells.md"]["issues"][0]["note"]


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

    async def answer(payload, key, model):
        agent.ledger.finish(key, "saved", {"input_tokens": 3, "output_tokens": 5})
        return "saved"

    monkeypatch.setattr(agent, "_query", answer)
    assert agent.ask(messages, "test") == "saved"
    restarted = module.Runtime(config | {"revision": "new-cli"})
    monkeypatch.setattr(module, "check_auth", no_login)
    assert restarted.ask(messages, "test") == "saved"


def test_large_hub_previews_keep_retrieval_references():
    from beril_wiki.agentic.runtime import page_context

    context = "\n".join(page_context(f"wiki/concepts/page-{i}.md", "x" * 62000) for i in range(9))
    assert len(context.encode()) < 100000
    assert context.count("TRUNCATED") == 9
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
    compiler.llm([], "merge/entity")
    assert calls == [("figures/test", False), ("test/queries", False), ("merge/entity", True)]


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
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "retry"])
    assert cli.main() == 1  # nothing named
    (tmp_path / ".agentic/failures.json").write_text(
        json.dumps({"conflicts/x": {"step": "conflicts/x", "issues": [], "jobs": [key]}})
    )
    monkeypatch.setattr(
        sys, "argv", ["agentic", "--root", str(tmp_path), "retry", "--page", "conflicts/y"]
    )
    assert cli.main() == 1  # unknown page
    (tmp_path / "state").mkdir()
    (tmp_path / "state/agentic.json").write_text(
        json.dumps({"fingerprint": "current", "editorial": {"conflicts": {}, "topics": {}}})
    )
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "retry", "--all-failed"])
    assert cli.main() == 0
    accepted = json.loads((tmp_path / "state/agentic.json").read_text())
    assert "fingerprint" not in accepted and accepted["editorial"] == {"topics": {}}
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "status"])
    assert cli.main() == 0
    restarted = module.Runtime(config)

    async def answer(payload, new_key, model):
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
        assert "read_evidence" not in kwargs["messages"][1]["content"]
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


def test_figure_pages_place_in_parallel_workers(tmp_path, monkeypatch):
    import json
    import threading
    import time
    from types import SimpleNamespace

    from beril_wiki.stages import figures as F

    (tmp_path / "wiki/topics").mkdir(parents=True)
    (tmp_path / "state").mkdir()
    for name in ("a", "b", "c", "d"):
        (tmp_path / f"wiki/topics/{name}.md").write_text("# Yield\n\nYield. [src: a]")
    monkeypatch.setattr(F, "ROOT", tmp_path)
    monkeypatch.setattr(F, "STATE", tmp_path / "state")
    monkeypatch.setattr(F, "workers", lambda: 3)
    monkeypatch.setattr(
        F,
        "build_manifest",
        lambda: {"a": [{"file": "figures/a.png", "caption": "Yield", "context": "Yield"}]},
    )
    monkeypatch.setattr(F.sys, "argv", ["figures"])
    threads = []

    def answer(**kwargs):
        threads.append(threading.current_thread().name)
        time.sleep(0.05)
        text = json.dumps({"placements": [{"figure": 0, "after_paragraph": 0}]})
        return SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=text))])

    monkeypatch.setattr(F, "completion", answer)
    F.main()
    assert len(threads) == 4 and len(set(threads)) > 1
    placements = json.loads((F.STATE / "figures-placements.json").read_text())
    assert sorted(placements) == ["topics/a.md", "topics/b.md", "topics/c.md", "topics/d.md"]
    assert not list(F.STATE.glob("*.tmp"))


def test_links_to_pages_never_written_keep_their_label(tmp_path):
    from beril_wiki.agentic.runner import unlink_missing

    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "wiki/concepts/kept.md").write_text("See [[concepts/kept]].")
    page = tmp_path / "wiki/concepts/a.md"
    page.write_text(
        "Links [[concepts/kept]], [[concepts/never-written|the lost page]] and [[entities/gone]]."
    )
    unlink_missing(tmp_path)
    assert page.read_text() == "Links [[concepts/kept]], the lost page and gone."


def test_stored_content_flag_replays_as_that_jobs_failure(tmp_path):
    from beril_wiki.agentic.runtime import JobFailed

    db = tmp_path / "jobs.sqlite"
    ledger = Ledger(db, "batch", 1000, 9, 20)
    ledger.reserve("flagged")
    ledger.finish(
        "flagged",
        "",
        {"input_tokens": 20, "output_tokens": 0},
        "flagged for possible biological risk",
    )
    ledger.reserve("broken")
    ledger.finish("broken", "", {"input_tokens": 20, "output_tokens": 0}, "Codex transport failed")
    with pytest.raises(JobFailed, match="biological risk"):
        ledger.reserve("flagged")
    with pytest.raises(WorkflowError, match="inspect saved job") as caught:
        ledger.reserve("broken")
    assert not isinstance(caught.value, JobFailed)


def test_pilot_usd_cap_counts_claude_aliases(tmp_path):
    """Review finding K: a Claude model named by alias counts against a pilot's USD cap."""
    ledger = Ledger(tmp_path / "jobs.sqlite", "pilot", 10**9, 99, 10, caps={"max_usd": 3})
    ledger.reserve("a", "write/x", "sonnet")
    ledger.finish("a", "ok", {"input_tokens": 1, "output_tokens": 1}, cost=2.5)
    with pytest.raises(WorkflowError, match="Claude USD 2.50"):
        ledger.reserve("b", "write/y", "sonnet")


def test_an_unmeasured_codex_job_keeps_its_hold_under_a_cap(tmp_path):
    """Review finding J: reconciling a killed Codex job charges its hold, not less."""
    caps = {"max_codex_tokens": 450_000}
    ledger = Ledger(tmp_path / "jobs.sqlite", "pilot", 10**9, 99, 50_000, caps=caps)
    ledger.reserve("a", "write/x/science-review", "gpt-6-luna")
    ledger.reconcile_stale(tmp_path / "transcripts")
    with pytest.raises(WorkflowError, match="Codex tokens 400000"):
        ledger.reserve("b", "write/y/science-review", "gpt-6-luna")


SOURCES = ("a__REPORT.md", "discoveries.md", "pitfalls.md")


def admission_base(tmp_path):
    """A settled wiki repository: project `a` is integrated from the corpus committed at
    HEAD, and the accepted state owes no editorial stage. Returns it and a checkout
    copied from that corpus."""
    import json
    import shutil
    import subprocess

    from beril_wiki import corpus
    from beril_wiki.agentic import curator as C
    from beril_wiki.agentic import runner
    from beril_wiki.agentic.runtime import contract_manifest, digest, file_hash, manifest
    from beril_wiki.stages.fetch import fetch_local

    root = tmp_path / "repo"
    source = root / "corpus"
    files = {
        "projects/a/README.md": "# A\n\n## Authors\n\n- Ada\n",
        "projects/a/REPORT.md": "# A report\n\nYield was 42%.\n",
        "ui/config/collections.yaml": "collections: []\n",
        "docs/discoveries.md": "# Discoveries\n",
        "docs/pitfalls.md": "# Pitfalls\n",
    }
    for rel, text in {
        **files,
        "contract/AGENTS.md": "Contract",
        "agentic.yaml": "model: m\n",
        "wiki/concepts/c.md": "# C\n",
        "wiki/sources/a__REPORT.md": files["projects/a/REPORT.md"],
        "wiki/sources/discoveries.md": files["docs/discoveries.md"],
        "wiki/sources/pitfalls.md": files["docs/pitfalls.md"],
        **{f"wiki/summaries/{n}": "# Summary\n" for n in SOURCES},
    }.items():
        path = (source if rel in files else root) / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    corpus.save(
        {
            "version": 1,
            "shared": {rel: corpus.sha256(source / rel) for rel in corpus.SHARED},
            "projects": {"a": corpus.entry(source / "projects/a", "workbench")},
        },
        source,
    )
    fetch_local(root / "staging", source)
    state = root / "state"
    state.mkdir()
    (state / "hashes.json").write_text(
        json.dumps({n: file_hash(root / "staging" / n) for n in SOURCES})
    )
    (state / "curator-topics.json").write_text(
        json.dumps(
            {
                "version": 1,
                "reason": "One group",
                "groups": [{"title": "C studies", "concepts": ["c"]}],
                "concepts": manifest(root, ("wiki/concepts",)),
            }
        )
    )
    (state / "agentic.json").write_text(
        json.dumps(
            {
                "version": 2,
                "revision": runner.scientific_revision(root),
                "revision_scheme": runner.REVISION_SCHEME,
                "contract": digest(contract_manifest(root)),
                "core_outputs": manifest(root, runner.CORE_OUTPUTS),
                "editorial": {name: C.stage_snapshot(root, name) for name in C.EDITORIAL},
            }
        )
    )
    git = ["git", "-C", str(root), "-c", "user.name=t", "-c", "user.email=t@example.org"]
    subprocess.run([*git, "init", "-q"], check=True)
    subprocess.run([*git, "add", "-A"], check=True)
    subprocess.run([*git, "commit", "-qm", "base"], check=True)
    checkout = tmp_path / "checkout"
    shutil.copytree(source, checkout)
    return root, checkout


def add_project(checkout, pid, report="# New report\n\nGrowth was 7%.\n"):
    from beril_wiki import corpus

    project = checkout / "projects" / pid
    project.mkdir(parents=True, exist_ok=True)
    (project / "README.md").write_text(f"# {pid}\n\n## Authors\n\n- Ada\n")
    (project / "REPORT.md").write_text(report)
    manifest = corpus.load(checkout)
    manifest["projects"][pid] = corpus.entry(project, "workbench")
    corpus.save(manifest, checkout)


def ledger_rows(root):
    import sqlite3

    path = root / ".agentic/jobs.sqlite"
    if not path.exists():
        return None
    with sqlite3.connect(path) as db:
        return db.execute("SELECT key,status FROM jobs ORDER BY rowid").fetchall()


def test_expect_source_admits_one_added_report(tmp_path):
    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import runner
    from beril_wiki.agentic.runtime import manifest

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    before = manifest(root, (*runner.TREES, "contract"))
    verdict = cli.plan(root, checkout, "b")
    assert verdict["admitted"], verdict["reasons"]
    assert verdict["changed_sources"] == ["b__REPORT.md"]
    assert verdict["base_pending"] == [] and verdict["invalidation"] is None
    # The import stages a new source, which the per-source stages then owe.
    assert "conflicts" in verdict["pending_editorial"]
    assert manifest(root, (*runner.TREES, "contract")) == before
    assert not (root / ".agentic").exists()
    assert set(cli.plan(root)) == {"changed_sources", "pending_editorial"}


def test_expect_source_admits_a_readme_only_update(tmp_path):
    from beril_wiki import corpus
    from beril_wiki.agentic import __main__ as cli

    root, checkout = admission_base(tmp_path)
    (checkout / "projects/a/README.md").write_text("# A\n\n## Authors\n\n- Ada\n- Grace\n")
    manifest = corpus.load(checkout)
    manifest["projects"]["a"] = corpus.entry(checkout / "projects/a", "workbench")
    corpus.save(manifest, checkout)
    verdict = cli.plan(root, checkout, "a")
    assert verdict["admitted"], verdict["reasons"]
    assert verdict["changed_sources"] == []


def test_expect_source_plans_the_authors_stage_a_readme_change_makes_due(tmp_path):
    """A run's curator runs extras before anything else, so an added author rewrites
    the author pages and the authors stage spends; the plan must list it."""
    import json
    import subprocess

    from beril_wiki import corpus
    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import curator as C
    from beril_wiki.agentic.admission import write_extras

    root, checkout = admission_base(tmp_path)
    # Settle the base as a run leaves it: extras wrote its pages, then the snapshot.
    write_extras(root, root / "corpus")
    path = root / "state/agentic.json"
    state = json.loads(path.read_text())
    state["editorial"] = {n: C.stage_snapshot(root, n) for n in C.EDITORIAL}
    path.write_text(json.dumps(state))
    git = ["git", "-C", str(root), "-c", "user.name=t", "-c", "user.email=t@example.org"]
    subprocess.run([*git, "add", "-A"], check=True)
    subprocess.run([*git, "commit", "-qm", "extras"], check=True)
    assert "authors" not in cli.plan(root, checkout, "a")["pending_editorial"]
    (checkout / "projects/a/README.md").write_text("# A\n\n## Authors\n\n- Ada\n- Grace\n")
    manifest = corpus.load(checkout)
    manifest["projects"]["a"] = corpus.entry(checkout / "projects/a", "workbench")
    corpus.save(manifest, checkout)
    verdict = cli.plan(root, checkout, "a")
    assert verdict["admitted"], verdict["reasons"]
    assert "authors" in verdict["pending_editorial"]


def adopted_revision(root, checkout):
    import json

    path = root / "state/agentic.json"
    state = json.loads(path.read_text())
    path.write_text(json.dumps(state | {"revision": "older", "revision_scheme": 4}))


def current_revision(root, checkout):
    import json

    path = root / "state/agentic.json"
    path.write_text(json.dumps(json.loads(path.read_text()) | {"revision": "older"}))


def second_report(root, checkout):
    add_project(checkout, "c")


def edited_concept(root, checkout):
    (root / "wiki/concepts/c.md").write_text("# C\n\nEdited by hand.\n")


def expired_labels(root, checkout):
    import json

    (root / "state/novelty.json").write_text(json.dumps({"f1": {"retrieved_on": "2020-01-01"}}))


def stale_stage(root, checkout):
    import json

    path = root / "state/agentic.json"
    state = json.loads(path.read_text())
    del state["editorial"]["authors"]
    path.write_text(json.dumps(state))


def failed_on_main(root, entries, links=()):
    """Save `entries` ({store: {key: entry}}) as main's card state, and settle the
    accepted snapshot so only the failures are owed."""
    import json

    from beril_wiki.agentic import curator as C
    from beril_wiki.stages import cards

    for store, data in (({"links": {}} if links else {}) | entries).items():
        saved = {"candidates": data, "links": list(links)} if store == "links" else data
        (root / f"state/{store}.json").write_text(json.dumps(saved))
    for fid in {f for x in links for f in (x["a"], x["b"])}:
        fields = {"type": "Finding", "description": "Growth fell.", "source": fid[:1]}
        cards.write_page(root / f"wiki/findings/{fid}.md", fields, "# Growth fell\n")
    path = root / "state/agentic.json"
    state = json.loads(path.read_text())
    state["editorial"] = {n: C.stage_snapshot(root, n) for n in C.EDITORIAL}
    path.write_text(json.dumps(state))


def failed_gist_of_b(root, checkout):
    failed_on_main(root, {"gists": {"b--1a2b3c4d": {"failed": True}}})


def failed_link_naming_b(root, checkout):
    failed_on_main(root, {"links": {"ref:a>b": {"failed": True}}})


SHARED_LINK = {"a": "a--1a2b3c4d", "b": "b--5e6f7a8b", "level": "finding"}
SHARED_LINK |= {"type": "same result", "label": "Both saw growth fall"}


def failed_group_with_b(root, checkout):
    from beril_wiki.stages.shared import group_id

    gid = group_id(["a--1a2b3c4d", "b--5e6f7a8b"])
    failed_on_main(root, {"shared": {gid: {"input": "", "failed": True}}}, [SHARED_LINK])


def unknown_job(root, checkout):
    ledger = Ledger(root / ".agentic/jobs.sqlite", "earlier", 100, 5, 10)
    ledger.reserve("conflicts/x")
    with pytest.raises(WorkflowError, match="unknown token usage"):
        ledger.finish("conflicts/x", "", None)


def other_manifest_entry(root, checkout):
    from beril_wiki import corpus

    manifest = corpus.load(checkout)
    manifest["projects"]["a"]["origin"] = "v1@elsewhere"
    corpus.save(manifest, checkout)


def other_readme(root, checkout):
    (checkout / "projects/a/README.md").write_text("# A\n\n## Authors\n\n- Someone else\n")


def test_expect_source_adopts_an_older_revision_scheme(tmp_path):
    from beril_wiki.agentic import __main__ as cli

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    adopted_revision(root, checkout)
    verdict = cli.plan(root, checkout, "b")
    assert verdict["admitted"], verdict["reasons"]


@pytest.mark.parametrize(
    ("mutate", "reason"),
    [
        (second_report, "c__REPORT.md"),
        (edited_concept, "accepted core_outputs"),
        (current_revision, "accepted revision"),
        (expired_labels, "novelty labels"),
        (stale_stage, "main owes editorial stages: authors"),
        (failed_gist_of_b, "failed card entries of b: gists:b--1a2b3c4d"),
        (failed_link_naming_b, "failed card entries of b: links:ref:a>b"),
        (failed_group_with_b, "failed card entries of b: shared:g-"),
        (unknown_job, "conflicts/x"),
        (other_manifest_entry, "manifest.json differs from HEAD outside projects/b: projects/a"),
        (other_readme, "projects/a/README.md"),
    ],
)
def test_expect_source_refuses_work_beyond_one_project(tmp_path, mutate, reason):
    from beril_wiki.agentic import __main__ as cli

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    mutate(root, checkout)
    rows = ledger_rows(root)
    verdict = cli.plan(root, checkout, "b")
    assert not verdict["admitted"]
    assert any(reason in r for r in verdict["reasons"]), verdict["reasons"]
    assert ledger_rows(root) == rows


def test_expect_source_leaves_other_projects_failed_entries_to_maintenance(tmp_path):
    """Main's failed entries of other projects, or of a topic, are not a researcher's to
    pay for, so they are listed for maintenance and do not refuse."""
    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.stages.shared import group_id

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    link = SHARED_LINK | {"b": "z--5e6f7a8b"}
    gid = group_id(["a--1a2b3c4d", "z--5e6f7a8b"])
    failed_on_main(
        root,
        {
            "gists": {"a--1a2b3c4d": {"failed": True}, "a--99999999": {"gist": "Kept."}},
            "links": {"pair:a--1a2b3c4d|z--5e6f7a8b": {"failed": True}},
            "shared": {gid: {"input": "", "failed": True}},
            "followups": {"does-growth-fall--1a2b3c": {"failed": True}},
            "directions": {"dark-matter": {"input": "k", "reply": {}, "failed": True}},
        },
        [link],
    )
    verdict = cli.plan(root, checkout, "b")
    assert verdict["admitted"], verdict["reasons"]
    assert verdict["maintenance_failed"] == [
        "gists:a--1a2b3c4d",
        "links:pair:a--1a2b3c4d|z--5e6f7a8b",
        f"shared:{gid}",
        "followups:does-growth-fall--1a2b3c",
        "directions:dark-matter",
    ]


def test_expect_source_cli_exits_on_refusal_before_run(tmp_path, monkeypatch, capsys):
    import json
    import sys

    from beril_wiki.agentic import __main__ as cli

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    add_project(checkout, "c")
    common = ["agentic", "--root", str(root)]
    plan = [*common, "plan", "--checkout", str(checkout), "--expect-source", "b", "--json"]
    lines = tmp_path / "progress.jsonl"
    monkeypatch.setenv("BERIL_WIKI_PROGRESS", "")  # restored after the CLI exports it
    monkeypatch.setattr(sys, "argv", [*plan, "--progress", str(lines)])
    assert cli.main() == 1
    verdict = json.loads(capsys.readouterr().out)
    assert not verdict["admitted"]
    start, end = (json.loads(line) for line in lines.read_text().splitlines())
    assert (start["event"], start["expect_source"]) == ("plan_start", "b")
    assert (end["event"], end["admitted"], end["reasons"]) == (
        "plan_end",
        False,
        verdict["reasons"],
    )
    monkeypatch.setattr(cli, "run", lambda *a, **k: pytest.fail("run started"))
    flags = ["--max-tokens", "10", "--max-jobs", "1", "--cli", "claude", "--model", "m"]
    run = [*common, "run", *flags, "--checkout", str(checkout), "--expect-source", "b"]
    monkeypatch.setattr(sys, "argv", run)
    assert cli.main() == 1
    assert "c__REPORT.md" in capsys.readouterr().out


def test_expect_source_tells_the_card_stages_which_project_runs(tmp_path, monkeypatch):
    """The card stages leave other projects' failed entries only when the run's config
    names the project; without it they re-ask every one."""
    import sys

    from beril_wiki.agentic import __main__ as cli

    root, checkout = admission_base(tmp_path)
    add_project(checkout, "b")
    seen = {}
    monkeypatch.setattr(cli, "run", lambda root, checkout, config, staged: seen.update(config))
    flags = ["--max-tokens", "10", "--max-jobs", "1", "--cli", "claude", "--model", "m"]
    run = ["agentic", "--root", str(root), "run", *flags, "--checkout", str(checkout)]
    monkeypatch.setattr(sys, "argv", [*run, "--expect-source", "b"])
    assert cli.main() == 0
    assert seen["expect_source"] == "b"
    seen.clear()
    monkeypatch.setattr(sys, "argv", run)
    assert cli.main() == 0
    assert "expect_source" not in seen


STAGE_DRIVER = """
import sys
from pathlib import Path

from beril_wiki.agentic import __main__ as cli
from beril_wiki.agentic import runner

d = Path(sys.argv[1])
inert = ["/bin/sh", "-c", f"echo $$ > {d}/stage.pid; exec sleep 300"]


def run(root, checkout, config, staged):
    runner._run_stage(d, {"PATH": "/usr/bin:/bin"}, d / "stage.log", inert, "inert", 600)


cli.run = run
sys.argv = ["agentic", "--root", str(d), "run", "--max-tokens", "10", "--max-jobs", "1"]
sys.argv += ["--cli", "claude", "--model", "m"]
sys.exit(cli.main())
"""


def test_sigterm_to_run_kills_the_stage_group(tmp_path):
    """Cancel sends SIGTERM to the runner; a stage runs in its own session, so only
    run_stage's cleanup can stop it."""
    import contextlib
    import os
    import signal
    import subprocess
    import sys
    import time

    driver = tmp_path / "driver.py"
    driver.write_text(STAGE_DRIVER)
    runner = subprocess.Popen(
        [sys.executable, str(driver), str(tmp_path)], start_new_session=True, cwd=tmp_path
    )
    pidfile = tmp_path / "stage.pid"
    stage = None
    try:
        deadline = time.monotonic() + 30
        while not (pidfile.exists() and pidfile.read_text().strip()):
            assert runner.poll() is None and time.monotonic() < deadline, "stage never started"
            time.sleep(0.05)
        stage = int(pidfile.read_text())
        os.killpg(runner.pid, signal.SIGTERM)
        assert runner.wait(timeout=20) == 143
        with pytest.raises(ProcessLookupError):
            os.kill(stage, 0)
    finally:
        for pid in (runner.pid, stage):
            if pid is not None:
                with contextlib.suppress(ProcessLookupError, PermissionError):
                    os.killpg(pid, signal.SIGKILL)
        runner.wait()


def test_retry_failed_jobs_reissues_all_but_content_refusals(tmp_path, monkeypatch, capsys):
    """A job interrupted by Cancel ends as failed, and reserve refuses a failed key on
    every resume until something moves it to the retry path. A hard kill leaves its job
    pending, which retry charges and re-issues too instead of failing the next Resume."""
    import json
    import sys

    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic.runtime import CONTENT_FLAG

    store = tmp_path / ".agentic"
    store.mkdir()
    config: dict[str, object] = {"root": str(tmp_path), "store": str(store), "run": "r"}
    config |= {"cli": "claude", "max_tokens": 10**6, "max_jobs": 9, "reserve_tokens": 10}
    (store / "config.json").write_text(json.dumps(config))
    ledger = Ledger(store / "jobs.sqlite", "r", 10**6, 9, 10)
    usage = {"input_tokens": 1, "output_tokens": 1}
    for key, error in (("cut", "interrupted"), ("flagged", f"{CONTENT_FLAG} refusal"), ("ok", "")):
        ledger.reserve(key, "write/x")
        ledger.finish(key, "out", usage, error=error)
    ledger.reserve("killed", "write/x")
    with pytest.raises(WorkflowError, match="job cut: failed"):
        ledger.reserve("cut", "write/x")
    monkeypatch.setattr(sys, "argv", ["agentic", "--root", str(tmp_path), "retry", "--failed-jobs"])
    assert cli.main() == 0
    out = capsys.readouterr().out
    assert "retry: cut" in out and "retry: killed" in out
    rows = dict(ledger.db.execute("SELECT key,status FROM jobs").fetchall())
    assert rows == {"cut": "rejected", "flagged": "failed", "ok": "done", "killed": "rejected"}
    assert cli.main() == 0
    assert "no failed jobs" in capsys.readouterr().out


def test_run_caps_reach_the_ledger(tmp_path, monkeypatch):
    import sys

    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic.runtime import Runtime

    captured = {}
    monkeypatch.setattr(cli, "run", lambda root, checkout, config, staged: captured.update(config))
    common = ["agentic", "--root", str(tmp_path), "run", "--max-tokens", "10000000"]
    common += ["--max-jobs", "99", "--cli", "claude", "--model", "m"]
    caps = ["--max-usd", "3", "--max-codex-tokens", "500000", "--budget-run", "wiki/p"]
    monkeypatch.setattr(sys, "argv", [*common, *caps])
    assert cli.main() == 0
    assert captured["budget_run"] == "wiki/p"
    store = tmp_path / ".agentic"
    ledger = Runtime(captured | {"root": str(tmp_path), "store": str(store), "run": "r"}).ledger
    usage = {"input_tokens": 1, "output_tokens": 1}
    ledger.reserve("a", "write/x", "claude-sonnet-5-5")
    ledger.finish("a", "ok", usage, cost=2.5)
    with pytest.raises(WorkflowError, match="Claude USD 2.50"):
        ledger.reserve("b", "write/y", "claude-sonnet-5-5")
    ledger.reserve("c", "write/x/science-review", "gpt-6.1-sol")
    with pytest.raises(WorkflowError, match="Codex tokens 400000"):
        ledger.reserve("d", "write/y/science-review", "gpt-6.1-sol")
    # A cap that compares false against every spend would admit everything.
    monkeypatch.setattr(sys, "argv", [*common, "--max-usd", "nan"])
    assert cli.main() == 1


# Recorded replies that pass through the real Runtime.ask, so each job is reserved and
# finished in the ledger as a model job would be.
LEDGER_RECORDING = """
import json

from beril_wiki.agentic import runtime

real_ask = runtime.Runtime.ask
from agentic_recording import install, reply

install()
runtime.Runtime.ask = real_ask
runtime.check_auth = lambda cli: None


async def recorded_query(self, payload, key, model):
    output = reply(self, json.loads(payload), self._step)
    self.ledger.finish(key, output, {"input_tokens": 10, "output_tokens": 10}, cost=0.01)
    return output


runtime.Runtime._query = recorded_query
"""


def test_progress_lines_cover_stages_and_jobs(tmp_path, monkeypatch):
    import json
    import sqlite3
    import sys
    from pathlib import Path

    from agentic_recording import reply
    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import runtime

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
    (tmp_path / "sitecustomize.py").write_text(LEDGER_RECORDING)
    monkeypatch.setenv("PYTHONPATH", f"{tmp_path}:{Path(__file__).parent.resolve()}")

    async def recorded_query(self, payload, key, model):
        output = reply(self, json.loads(payload), self._step)
        self.ledger.finish(key, output, {"input_tokens": 10, "output_tokens": 10}, cost=0.01)
        return output

    monkeypatch.setattr(runtime.Runtime, "_query", recorded_query)
    monkeypatch.setattr(runtime, "check_auth", lambda cli: None)
    lines = tmp_path / "progress.jsonl"
    monkeypatch.setenv("BERIL_WIKI_PROGRESS", "")  # restored after the CLI exports it
    argv = ["agentic", "--root", str(root), "run", "--max-tokens", "10000000"]
    argv += ["--max-jobs", "1000", "--cli", "/usr/bin/true", "--model", "recorded"]
    monkeypatch.setattr(
        sys, "argv", [*argv, "--checkout", str(checkout), "--progress", "progress.jsonl"]
    )
    monkeypatch.chdir(tmp_path)
    assert cli.main() == 0
    events = [json.loads(line) for line in lines.read_text().splitlines()]
    assert all(e["source"] == "wiki" and e["ts"] for e in events)
    staged = [(e["event"], e["stage"]) for e in events if e["event"].startswith("stage_")]
    names = [stage for event, stage in staged if event == "stage_start"]
    assert staged == [(event, n) for n in names for event in ("stage_start", "stage_end")]
    assert names[0] == "fetch" and names[-1] == "check" and "figures" in names
    assert all(e["ok"] for e in events if e["event"] == "stage_end")
    db = sqlite3.connect(root / ".agentic/jobs.sqlite")
    (finished,) = db.execute("SELECT count(*) FROM jobs WHERE status!='pending'").fetchone()
    jobs = [e for e in events if e["event"] == "job"]
    assert finished and len(jobs) == finished
    assert max(e["jobs"] for e in jobs) == finished
    # Stage subprocesses inherit the file, and the curator's own jobs run in the runner.
    assert {e["stage"] for e in jobs} > {""}
    last = [e for e in events if e["event"] == "stage_end"][-1]
    assert last["jobs"] == finished and last["usd"] == round(0.01 * finished, 4)
    assert last["codex_tokens"] == 0 and last["failed_pages"] == 0


def test_check_auth_reports_each_login(tmp_path, monkeypatch, capsys):
    import json
    import sys

    from beril_wiki.agentic import __main__ as cli
    from beril_wiki.agentic import codex, runtime

    class Session:
        def __init__(self, store):
            self.client = "client"

        def close(self):
            pass

    def no_codex_login(client):
        raise WorkflowError("a ChatGPT subscription login is required for Codex; no API key")

    readme = tmp_path / "README.md"
    readme.write_text("## Authors\n\n- Ada Example\n- Bo Example\n")
    monkeypatch.setattr(codex, "CodexSession", Session)
    monkeypatch.setattr(runtime, "check_auth", lambda cli: None)
    monkeypatch.setattr(codex, "check_auth", lambda client: None)
    argv = ["agentic", "--root", str(tmp_path), "check-auth", "--cli", "claude"]
    monkeypatch.setattr(sys, "argv", [*argv, "--authors", str(readme)])
    assert cli.main() == 0
    assert json.loads(capsys.readouterr().out) == {"claude": "ok", "codex": "ok", "authors": 2}
    monkeypatch.setattr(codex, "check_auth", no_codex_login)
    assert cli.main() == 1
    report = json.loads(capsys.readouterr().out)
    assert report["claude"] == "ok" and "ChatGPT subscription" in report["codex"]
    monkeypatch.setattr(codex, "check_auth", lambda client: None)
    monkeypatch.setattr(sys, "argv", [*argv, "--authors", str(tmp_path / "missing.md")])
    assert cli.main() == 1
    assert isinstance(json.loads(capsys.readouterr().out)["authors"], str)
    assert not (tmp_path / ".agentic").exists()
