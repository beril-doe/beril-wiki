"""The outcomes and followups stages: one label per record, checked by code, then a reviewer."""

import json
from pathlib import Path

import pytest

import card_fakes
from beril_wiki import lakehouse
from beril_wiki.agentic import curator
from beril_wiki.agentic.runtime import CONTENT_FLAG, CandidateError, JobFailed, digest
from beril_wiki.stages import cards, followups, outcomes
from card_fakes import FakeAgent, install

FID = "a--1a2b3c4d"
STEP = f"outcomes/{FID}"
REASON = "The evidence shows no difference in fitness cost between the mechanisms."
QID = "does-x-do-y--abc123"
QSTEP = f"followups/{QID}"


def finding(root, fid=FID, result="null result"):
    cards.write_page(
        root / "wiki/findings" / f"{fid}.md",
        {"type": "Finding", "description": "No cost difference.", "result": result, "source": "a"},
        "# No cost difference\n\nNo cost difference. [src: a]\n\n## Evidence\n\n"
        "> Costs were equal across mechanisms. [src: a]\n",
    )


def gists_state(root, entries):
    path = root / "state/gists.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(entries))


def reply(type_="negative", reason=REASON):
    return json.dumps({"type": type_, "reason": reason})


def run(tmp_path, monkeypatch, replies, **kwargs):
    agent = FakeAgent(tmp_path / "store", {STEP: [], f"{STEP}/repair": []} | replies, **kwargs)
    install(monkeypatch, agent)
    assert outcomes.main(tmp_path) == 0
    path = tmp_path / "state/outcomes.json"
    return (json.loads(path.read_text()) if path.exists() else {}), agent


@pytest.fixture
def listed(tmp_path):
    finding(tmp_path)
    gists_state(tmp_path, {FID: {"gist": "Costs did not differ.", "case": "measured absence"}})


def test_accepted_type_is_saved_and_reviewed(tmp_path, monkeypatch, listed):
    state, agent = run(tmp_path, monkeypatch, {STEP: [reply()]})
    assert state[FID]["type"] == "negative" and state[FID]["reason"] == REASON
    assert state[FID]["input"] and agent.asked == [STEP, f"{STEP}/science-review"]
    sent = json.loads(agent.sent[STEP].split("\n")[-1])
    assert sent["FINDING"]["tag"] == "null result" and sent["FINDING"]["summary"]


def test_unchanged_finding_costs_nothing(tmp_path, monkeypatch, listed):
    run(tmp_path, monkeypatch, {STEP: [reply()]})
    state, agent = run(tmp_path, monkeypatch, {})
    assert agent.asked == [] and state[FID]["type"] == "negative"


def test_findings_publish_would_not_list_are_not_asked(tmp_path, monkeypatch):
    finding(tmp_path)
    finding(tmp_path, "a--repeat01", result="observation")
    finding(tmp_path, "a--missing1")
    gists_state(
        tmp_path,
        {
            "a--repeat01": {"gist": "Same again.", "repeats": FID},
            "a--missing1": {"gist": "No data.", "case": "missing data"},
            FID: {"gist": "Failed rewrite.", "failed": True},
        },
    )
    state, agent = run(tmp_path, monkeypatch, {})
    assert state == {} and agent.asked == []


def test_reason_rules_go_back_to_the_writer():
    parse = outcomes.checker({})
    assert parse(reply()).type == "negative"
    stats = reply(reason="The difference was significant (p = 0.01).")
    for bad in (reply(reason="Too short."), stats):
        with pytest.raises(CandidateError):
            parse(bad)
    with pytest.raises(CandidateError):
        parse(reply(type_="correction"))


def test_refusal_fails_one_finding_only(tmp_path, monkeypatch, listed, capsys):
    refusal = JobFailed(f"Codex turn failed: {CONTENT_FLAG}")
    state, _ = run(tmp_path, monkeypatch, {STEP: [reply()]}, review_error={STEP: refusal})
    assert state[FID] == {"failed": True}
    assert f"[FAILED] {STEP}" in capsys.readouterr().out


def question(root):
    card_fakes.lakehouse(root)
    cards.write_page(
        root / "wiki/directions" / f"{QID}.md",
        {
            "type": "Research direction",
            "hypothesis": "X drives Y.",
            "approach": "analysis then experiment",
            "readiness_basis": "Genomes exist; growth assays are new.",
            "projects": ["a"],
            "databases": ["kescience.fitnessbrowser"],
            "tables": ["kescience.fitnessbrowser.experiment"],
        },
        "# Does X do Y?\n\n## How to test it\n\nScreen genomes, then grow the strains.\n\n"
        "## What would support or refute it\n\nSupport: growth differs.\n",
    )


QREASON = "Growth assays on strains decide it."
QTABLES = ["kescience.fitnessbrowser.experiment"]


def qreply(need="experiment", first=True, unclear=False, reason=QREASON, tables=QTABLES):
    return json.dumps(
        {
            "need": need,
            "first_step_existing": first,
            "data_unclear": unclear,
            "reason": reason,
            "tables": tables,
        }
    )


def test_followup_is_saved_with_the_question_sections(tmp_path, monkeypatch, capsys):
    question(tmp_path)
    agent = FakeAgent(tmp_path / "store", {QSTEP: [qreply()]})
    install(monkeypatch, agent)
    assert followups.main(tmp_path) == 0
    state = json.loads((tmp_path / "state/followups.json").read_text())
    assert state[QID]["need"] == "experiment" and state[QID]["first_step_existing"] is True
    sent = json.loads(agent.sent[QSTEP].split("\n")[-1])
    assert sent["QUESTION"]["how_to_test_it"] == "Screen genomes, then grow the strains."
    assert sent["DIRECTION_TABLES"] == ["kescience.fitnessbrowser.experiment"]
    assert sent["TABLES"][0]["table"] == "kescience.fitnessbrowser.experiment"
    assert "Other tenants exist" in sent["DATABASES"]
    assert state[QID]["tables"] == ["kescience.fitnessbrowser.experiment"]
    # --status keys with agentic.yaml; this one names the model the fake run used.
    monkeypatch.delenv("BERIL_AGENTIC_CONFIG", raising=False)
    (tmp_path / "agentic.yaml").write_text(f"model: {agent.config['model']}\n")
    capsys.readouterr()
    assert followups.main(tmp_path, ["--status"]) == 0
    assert "1 current, 0 stale" in capsys.readouterr().out
    page = tmp_path / "wiki/directions" / f"{QID}.md"
    page.write_text(page.read_text().replace("X drives Y.", "X drives Z."))
    assert followups.main(tmp_path, ["--status"]) == 1
    assert "1 stale" in capsys.readouterr().out


def test_first_step_only_for_experiments(tmp_path):
    card_fakes.lakehouse(tmp_path)
    parse = followups.checker({}, lakehouse.load(tmp_path))
    assert parse(qreply()).first_step_existing
    with pytest.raises(CandidateError, match="only when need is experiment"):
        parse(qreply(need="existing"))
    assert parse(qreply(need="outside", first=False, unclear=True, tables=[])).data_unclear
    with pytest.raises(CandidateError, match="names no table"):
        parse(qreply(need="existing", first=False, tables=[]))
    with pytest.raises(CandidateError, match="names BERDL"):
        parse(qreply(reason="BERDL holds the growth data for it."))


def test_label_stages_are_registered_after_their_inputs(tmp_path):
    for name, dep in (("outcomes", "gists"), ("followups", "directions")):
        assert name in curator.CARD_STAGES and curator.EDITORIAL[name][2] == (dep,)
        assert curator.EDITORIAL[name][3] is None
    assert curator.stage_revision(tmp_path, "outcomes") != curator.stage_revision(
        tmp_path, "followups"
    )


def test_a_failed_label_is_saved_before_a_budget_stop(tmp_path, monkeypatch, listed):
    """A failure followed by another item's budget stop still marks the old label failed,
    so publish falls back and the retry carries the objections."""
    from beril_wiki.agentic.prose import Issue, PageFailure
    from beril_wiki.agentic.runtime import WorkflowError
    from beril_wiki.stages import classify

    path = tmp_path / "state/outcomes.json"
    path.write_text(json.dumps({FID: {"input": "old", "type": "negative", "reason": REASON}}))

    def stopped(items, fn, count):
        issue = Issue(category="unsupported", note="Replacement rejected")
        yield items[0], PageFailure(STEP, [issue], ["job"])
        raise WorkflowError("budget admission refused")

    install(monkeypatch, FakeAgent(tmp_path / "store", {}))
    monkeypatch.setattr(classify, "parallel", stopped)
    monkeypatch.setattr(classify, "record_failure", lambda *args: None)
    with pytest.raises(WorkflowError):
        outcomes.main(tmp_path)
    saved = json.loads(path.read_text())[FID]
    assert saved["failed"] is True and saved["type"] == "negative"


ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.parametrize(
    ("stage", "state"),
    [
        (outcomes, "outcomes"),
        (followups, "followups"),
    ],
)
def test_the_committed_policy_keeps_the_accepted_labels(stage, state):
    """A default run reuses every accepted label: the model policy in agentic.yaml is the
    one the labels were judged with, so no run buys them again."""
    from beril_wiki.agentic.__main__ import load_models

    saved = json.loads((ROOT / f"state/{state}.json").read_text())
    policy = cards.policy(load_models(ROOT, None, None, []), ("labels", "card_review"))
    packs = stage.packs(ROOT, lakehouse.load(ROOT)) if stage is followups else stage.packs(ROOT)
    stale = [
        item
        for item, pack in packs.items()
        if item in saved
        and not saved[item].get("failed")
        and saved[item].get("input") != digest([pack, stage.PROMPT_TAG, policy])
    ]
    assert saved and not stale
