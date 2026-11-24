"""The stateful pipeline on a two-report wiki, with scripted agents in place of models.

What these guard: an edit that loses or invents a figure is refused, a rejected edit
leaves the page as it was, a revised report reaches only the section its changed claim
supports, and nothing but a report's content schedules model work.
"""

import json
import shutil
from pathlib import Path

import pytest

from beril_wiki.kb import importer, index, jobs, pages, tools, workflow
from beril_wiki.kb.agents import Agent, Run
from beril_wiki.kb.jobs import findings as findings_jobs
from beril_wiki.kb.jobs import gists as gists_jobs
from beril_wiki.kb.store import Store, block_of, blocks, checkout_lock, sha256
from beril_wiki.kb.tools import BUDGETS, Session, Tools, cite_in_front, rehome_figures

REPO = Path(__file__).resolve().parents[1]
ALPHA = """# Report: Alpha Growth Study

## Key Findings

Strain A reached a growth yield of 0.42 g/g on glucose in 12,500 cultures.

No effect of temperature on yield was detected across 3,300 cultures.

## Limitations

Only one strain was tested in this study.
"""
BETA = """# Report: Beta Acetate Study

## Key Findings

Strain B reached a growth yield of 0.38 g/g on acetate in 9,100 cultures.
"""
CONCEPT = """---
type: "Concept"
description: "Growth yield across projects."
sources: ["summaries/beta__REPORT.md"]
---
# Growth Yield

Beta measured a yield of 0.38 g/g on acetate [src: beta].

## Tensions

None recorded yet.

## Open Directions

- Compare substrates under one protocol.
"""
BETA_QUOTE = "Strain B reached a growth yield of 0.38 g/g on acetate in 9,100 cultures."
YIELD_QUOTE = "Strain A reached a growth yield of 0.42 g/g on glucose in 12,500 cultures."
LIMIT_QUOTE = "Only one strain was tested in this study."
NULL_QUOTE = "No effect of temperature on yield was detected across 3,300 cultures."
LEAD = "concepts/growth-yield#lead"
YIELD_TEXT = "Strain A yield was 0.42 g/g on glucose."
NULL_TEXT = "Temperature had no detected effect on yield."


def claim(kind: str, text: str, quote: str) -> dict:
    return {"kind": kind, "text": text, "quote": quote}


GOOD = (
    "Beta measured a yield of 0.38 g/g on acetate [src: beta]. Alpha **supports** a similar "
    "range: 0.42 g/g on glucose in 12,500 cultures [src: alpha]."
)


@pytest.fixture(autouse=True)
def no_pubmed(monkeypatch):
    """PubMed finds nothing: the scripted runs never reach the network."""
    from beril_wiki.kb.jobs import novelty as novelty_jobs

    monkeypatch.setattr(novelty_jobs, "retrieve", lambda *args: ({}, "2026-11-23"))


@pytest.fixture
def root(tmp_path: Path) -> Path:
    files = {
        "corpus/projects/alpha/REPORT.md": ALPHA,
        "corpus/projects/beta/REPORT.md": BETA,
        "wiki/concepts/growth-yield.md": CONCEPT,
        "wiki/summaries/beta__REPORT.md": "# Beta Acetate Study\n\nA summary [src: beta].\n",
        "wiki/sources/beta__REPORT.md": BETA,
        "contract/AGENTS.md": "## Domain Rules\nCite everything.\n## Frontmatter\nnone\n",
    }
    for name, text in files.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    shutil.copytree(REPO / "skills", tmp_path / "skills")
    store = Store(tmp_path)
    heading, block = block_of(BETA, BETA.find(BETA_QUOTE))
    store.write_claims(
        "beta",
        [
            {
                "id": "beta:0:0",
                "kind": "finding",
                "text": "Strain B yield was 0.38 g/g on acetate in 9,100 cultures.",
                "quote": BETA_QUOTE,
                "start": BETA.find(BETA_QUOTE),
                "end": BETA.find(BETA_QUOTE) + len(BETA_QUOTE),
                "heading": heading,
                "block": block,
                "status": "active",
            }
        ],
    )
    store.write_sources(
        {
            "beta": {
                "id": "beta",
                "sha256": sha256(BETA),
                "blocks": [h for _, _, h in blocks(BETA)],
            }
        }
    )
    store.write_sidecar(
        "concepts/growth-yield", {"sections": {"lead": {"claims": {"beta:0:0": "number"}}}}
    )
    return tmp_path


def config(**overrides) -> workflow.Config:
    reviewers = ("review", "card_review", "findings_review")
    roles = {r: "claude-y" if r in reviewers else "gpt-x" for r in workflow.DEFAULT_ROLES}
    # The deterministic stages start four interpreters; test_kb_authors covers them.
    made = workflow.Config({r: Agent.parse(m) for r, m in roles.items()}, jobs=1, tidy=False)
    for name, value in overrides.items():
        setattr(made, name, value)
    return made


def body(text: str, anchor: str) -> str:
    section = pages.parse(text).section(anchor)
    assert section is not None, anchor
    return section.body


class Script:
    """Stands in for the vendor harness: each role makes the tool calls a model would."""

    def __init__(
        self, body: str = GOOD, verdicts: tuple[str, ...] = ("accept",), stubborn: bool = False
    ) -> None:
        self.body = body
        # A stubborn editor answers a reviewer's objections with the same text.
        self.stubborn = stubborn
        # An extractor that skims submits claims without reading the report.
        self.skims = False
        self.verdicts = list(verdicts)
        self.roles: list[str] = []
        self.replies: list[dict] = []
        self.extracted = [
            claim("finding", YIELD_TEXT, YIELD_QUOTE),
            claim("null", NULL_TEXT, NULL_QUOTE),
        ]

    def __call__(self, agent: Agent, system: str, prompt: str, tools: Tools, work: Path) -> Run:
        role = tools.session.role
        self.roles.append(role)
        call = tools.call
        if role == "extract":
            if not self.skims:
                call("read_source", source=tools.session.task["source"])
            self.replies.append(call("submit_claims", claims=self.extracted))
        elif role == "curate":
            ids = tools.session.task["claims"]
            self.replies.append(
                call(
                    "propose_plan",
                    targets=[{"section": LEAD, "claims": ids[:1], "why": "adds a second yield"}],
                    skipped=[{"claims": ids[1:], "reason": "summary"}] if ids[1:] else [],
                )
            )
        elif role == "edit":
            section = tools.session.task["section"]
            read = call("read_section", section=section)
            body = self.body if section == LEAD else f"A summary [src: alpha]. {self.body}"
            if "A reviewer returned" in prompt and not self.stubborn:
                body += " The two used different substrates [src: alpha, beta]."
            self.replies.append(
                call(
                    "edit_section",
                    section=section,
                    base_sha=read["sha"],
                    body=body,
                    claims=tools.session.task["claims"][:1],
                    declined=[
                        {"claim": c, "reason": "not needed here"}
                        for c in tools.session.task["claims"][1:]
                    ],
                )
            )
        elif role == "review":
            task = tools.session.task
            read = call("read_section", section=task["section"])
            verdict = self.verdicts.pop(0) if self.verdicts else "accept"
            objections = [{"quote": "", "problem": "the range is not similar"}]
            call(
                "review",
                section=task["section"],
                sha=read["sha"],
                verdict=verdict,
                objections=objections if verdict == "revise" else [],
            )
        elif role in ("card", "record"):
            key, _, rest = prompt.removeprefix("Record to write: ").partition("\n")
            pack = json.JSONDecoder().raw_decode(rest[rest.index("{") :])[0]
            self.replies.append(call("submit_record", record=self.record(key, pack)))
        elif role in ("card_review", "verdict"):
            task = tools.session.task
            call("review", section=task["section"], sha=task["sha"], verdict="accept")
        call("finish", note="done")
        return Run(str(agent), ok=True, input_tokens=1000, output_tokens=100)

    @staticmethod
    def record(key: str, pack: dict) -> dict:
        """What a careful model would submit for one record job."""
        if key.startswith("findings/"):
            finding, caveat = pack["FINDINGS"][0], pack["CAVEATS"][0]
            headline = {
                "evidence": finding["id"],
                "result": "observation",
                "title": "Strain A grows efficiently on glucose",
                "claim": "Strain A reached a growth yield of 0.42 g/g on glucose.",
                "quantities": [{"value": "0.42", "what": "growth yield", "unit": "g/g"}],
                "caveat_evidence": caveat["id"],
                "caveat": "Only one strain was tested in this study.",
            }
            return {"headlines": [headline]}
        if key.startswith("gists/"):
            gist = "Strain A turned glucose into biomass efficiently in these cultures."
            return {"gist": gist, "case": "", "title": "", "repeats": ""}
        if key.startswith("outcomes/"):
            return {"type": "positive", "reason": "The strain turned glucose into biomass."}
        assert key.startswith("novelty/") and key.endswith("/queries"), key
        return {"queries": ["growth yield glucose"]}


def test_sections_round_trip_and_replace_keeps_other_bytes():
    page = pages.parse(CONCEPT)
    assert [s.anchor for s in page.sections] == ["lead", "tensions", "open-directions"]
    for section in page.sections:
        assert pages.replace(CONCEPT, section.anchor, section.body) == CONCEPT
    edited = pages.replace(CONCEPT, "tensions", "Alpha and beta disagree.")
    assert edited.replace("Alpha and beta disagree.", "None recorded yet.") == CONCEPT
    twice = pages.parse("# T\n\n## Notes\n\na\n\n## Notes\n\nb\n\n```\n## not a heading\n```\n")
    assert [s.anchor for s in twice.sections] == ["lead", "notes", "notes-2"]


def test_only_report_content_schedules_work(root: Path):
    assert workflow.plan(root)["tasks"] == [
        {"workflow": "ingest", "source": "alpha", "reason": "report not ingested yet"}
    ]
    script = Script()
    with pytest.raises(workflow.Stop, match="needs a changed report"):
        workflow.revise(root, "alpha", config(), script)
    assert workflow.ingest(root, "alpha", config(), script)["status"] == "done"
    assert workflow.plan(root) == {"tasks": []}
    # A report that is current is not read again, whichever command asks.
    calls = len(script.roles)
    for run in (workflow.ingest, workflow.revise):
        with pytest.raises(workflow.Stop, match="alpha is current"):
            run(root, "alpha", config(), script)
    assert len(script.roles) == calls
    # Editing a skill, the configuration or an accepted page schedules nothing.
    (root / "skills/wiki-edit/SKILL.md").write_text("changed", encoding="utf-8")
    (root / "wiki.yaml").write_text("roles: {edit: gpt-other}\n", encoding="utf-8")
    page = root / "wiki/concepts/growth-yield.md"
    page.write_text(page.read_text(encoding="utf-8") + "\nA hand edit.\n", encoding="utf-8")
    assert workflow.plan(root) == {"tasks": []}
    report = root / "corpus/projects/alpha/REPORT.md"
    report.write_text(ALPHA.replace("0.42", "0.47"), encoding="utf-8")
    assert workflow.plan(root)["tasks"] == [
        {"workflow": "revise", "source": "alpha", "reason": "report content changed"}
    ]


def test_ingest_edits_one_section_and_records_its_evidence(root: Path):
    before = (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8")
    script = Script()
    result = workflow.ingest(root, "alpha", config(), script)
    assert result["status"] == "done", result
    after = (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8")
    assert body(after, "lead") == GOOD
    for untouched in ("tensions", "open-directions"):
        assert body(after, untouched) == body(before, untouched)
    assert '"summaries/alpha__REPORT.md"' in pages.parse(after).front
    store = Store(root)
    links = store.sidecar("concepts/growth-yield")["sections"]["lead"]
    assert links["claims"] == {"alpha:n0": "edit", "beta:0:0": "number"}
    assert (
        links["stamp"]["writer"] == "gpt-x@medium"
        and links["stamp"]["reviewer"] == "claude-y@medium"
    )
    assert [c["id"] for c in store.claims("alpha")] == ["alpha:n0", "alpha:n1"]
    assert store.sources()["alpha"]["sha256"] == sha256(ALPHA)
    assert (root / "wiki/sources/alpha__REPORT.md").read_text(encoding="utf-8") == ALPHA
    assert (root / "wiki/summaries/alpha__REPORT.md").exists()
    assert script.roles == ["extract", "curate", "edit", "review", "edit", "review"]


def test_ingest_writes_a_finding_page_and_its_plain_summary(root: Path, monkeypatch):
    script = Script()
    script.extracted.append(claim("caveat", "Only one strain was tested.", LIMIT_QUOTE))
    result = workflow.ingest(root, "alpha", config(), script)
    assert result["status"] == "done", result
    assert result["records"] == {
        "findings": {"accepted": 1},
        "gists": {"accepted": 1},
        "outcomes": {"accepted": 1},
        "novelty": {"accepted": 1},
    }
    (page,) = (root / "wiki/findings").glob("alpha--*.md")
    text = page.read_text(encoding="utf-8")
    assert text.startswith('---\ntype: "Finding"') and "## Caveat" in text and YIELD_QUOTE in text
    gists = json.loads((root / "state/gists.json").read_text(encoding="utf-8"))
    assert gists[page.stem]["gist"].startswith("Strain A turned glucose")
    # PubMed returned nothing, so the label needs no judging model.
    label = json.loads((root / "state/novelty.json").read_text(encoding="utf-8"))[page.stem]
    assert label["label"] == "Insufficient literature evidence" and label["queries"]
    # A second pass owes nothing: the records stand until their evidence changes.
    scope = jobs.Scope(root=root, source="alpha", reason="ingest")
    assert findings_jobs.jobs(scope) == [] and gists_jobs.jobs(scope) == []
    # A figure the quote does not state is refused before any reviewer reads it.
    wrong = Script.record(
        "findings/alpha",
        findings_jobs.jobs(jobs.Scope(root=root, source="alpha", reason="refresh"))[0].pack,
    )
    wrong["headlines"][0]["claim"] = "Strain A reached a growth yield of 0.97 g/g on glucose."
    gate = findings_jobs.jobs(jobs.Scope(root=root, source="alpha", reason="refresh"))[0].check
    with pytest.raises(tools.Rejected) as refused:
        gate(wrong)
    assert "not in the quote" in " ".join(refused.value.objections)
    # A report too large for one session is read from a bounded set that still holds a
    # result and the caveat a headline needs.
    whole = findings_jobs.jobs(jobs.Scope(root=root, source="alpha", reason="refresh"))[0].pack
    monkeypatch.setattr(findings_jobs, "PACK_CHARS", 1)
    less = findings_jobs.jobs(jobs.Scope(root=root, source="alpha", reason="refresh"))[0].pack
    assert len(whole["FINDINGS"]) > 1 and len(less["FINDINGS"]) == len(less["CAVEATS"]) == 1


def test_submit_claims_keeps_only_verbatim_quotes(root: Path):
    tools = Tools(root, Session.start("extract", {"source": "alpha"}))
    reply = tools.call(
        "submit_claims",
        claims=[
            claim("finding", YIELD_TEXT, YIELD_QUOTE),
            claim("finding", YIELD_TEXT, YIELD_QUOTE.replace("0.42", "0.43")),
            claim("opinion", YIELD_TEXT, YIELD_QUOTE),
            claim("finding", YIELD_TEXT.replace("0.42", "0.97"), YIELD_QUOTE),
        ],
    )
    assert reply["accepted"] == 1 and len(reply["rejected"]) == 3
    assert "figures the quote does not contain (0.97)" in reply["rejected"][2]
    assert tools.session.claims[0]["id"] == "alpha:n0"
    assert tools.session.claims[0]["heading"] == "Key Findings"
    assert tools.call("read_source", source="beta")["ok"] is False
    # A quote must lie wholly inside the part of the report the session was given.
    limited = Tools(root, Session.start("extract", {"source": "alpha", "spans": [[0, 60]]}))
    outside = limited.call("submit_claims", claims=[claim("finding", YIELD_TEXT, YIELD_QUOTE)])
    assert outside["accepted"] == 0 and "outside the part" in outside["rejected"][0]
    # A report id is joined into a path, so only ids the corpus holds are read.
    assert Tools(root).call("read_source", source="../projects/alpha")["ok"] is False


def edit(root: Path, body: str, **kwargs) -> dict:
    store = Store(root)
    if not store.claims("alpha"):
        heading, block = block_of(ALPHA, ALPHA.find(YIELD_QUOTE))
        store.write_claims(
            "alpha",
            [
                {
                    "id": "alpha:n0",
                    "kind": "finding",
                    "text": "Yield 0.42 g/g.",
                    "quote": YIELD_QUOTE,
                    "start": ALPHA.find(YIELD_QUOTE),
                    "end": 0,
                    "heading": heading,
                    "block": block,
                    "status": "active",
                }
            ],
        )
    session = kwargs.pop("session", None) or Session.start(
        "edit", {"section": LEAD, "claims": ["alpha:n0"]}
    )
    tools = Tools(root, session)
    sha = tools.call("read_section", section=LEAD)["sha"]
    args = {"section": LEAD, "base_sha": sha, "body": body, "claims": ["alpha:n0"], **kwargs}
    return tools.call("edit_section", **args)


@pytest.mark.parametrize(
    ("body", "kwargs", "objection"),
    [
        ("Alpha reports 0.42 g/g on glucose [src: alpha].", {}, "missing from the new text"),
        (GOOD.replace("0.42", "0.44"), {}, "not found in the reports this paragraph cites"),
        (GOOD.replace("[src: alpha]", "[src: gamma]"), {}, "unknown reports"),
        (GOOD + " See [[concepts/missing-page]].", {}, "do not exist"),
        (GOOD, {"claims": []}, "neither used"),
        (GOOD + "\n\n## Extra\n\nMore.", {}, "must not contain"),
        (GOOD, {"base_sha": "stale"}, "base_sha is stale"),
        (GOOD + "\n\n```\nunclosed", {}, "changes the sections after it"),
        (GOOD + "\n\n   ```\nindented and unclosed", {}, "changes the sections after it"),
        # 0.38 is in the old section, but for beta: alpha's report does not contain it.
        (GOOD + "\n\nAlpha also saw 0.38 g/g [src: alpha].", {}, "not found in the reports"),
        (GOOD, {"section": "../README#lead"}, "is not a section id"),
        # Seen live: a doubly escaped argument arrives as one paragraph with "\\n" in it.
        (GOOD + "\\n\\nA second paragraph [src: alpha].", {}, "backslash and n"),
    ],
)
def test_edit_gate_refuses(root: Path, body: str, kwargs: dict, objection: str):
    reply = edit(root, body, **kwargs)
    assert reply["ok"] is False
    assert objection in json.dumps(reply)
    assert (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8") == CONCEPT


def test_a_declared_drop_passes_and_three_rejections_end_the_section(root: Path):
    body = "Alpha reports 0.42 g/g on glucose in 12,500 cultures [src: alpha]."
    dropped = [{"text": "0.38 beta", "reason": "superseded by the test"}]
    assert edit(root, body, dropped=dropped)["ok"] is True
    # The page's source list follows the edit: alpha joins it and beta leaves.
    front = pages.parse(cite_in_front(pages.replace(CONCEPT, "lead", body), CONCEPT)).front
    assert '["summaries/alpha__REPORT.md"]' in front
    session = Session.start("edit", {"section": LEAD, "claims": ["alpha:n0"]})
    for _ in range(3):
        assert edit(root, "Nothing cited 9.99.", session=session)["ok"] is False
    assert "rejected 3 times" in edit(root, GOOD, session=session)["error"]


def test_reading_budget_stops_reads_but_lets_the_agent_finish(root: Path):
    session = Session.start("curate", {"claims": []})
    session.calls = 2
    tools = Tools(root, session)
    assert tools.call("outline", page="concepts/growth-yield")["ok"] is True
    assert tools.call("outline", page="concepts/growth-yield")["ok"] is True
    refused = tools.call("outline", page="concepts/growth-yield")
    assert refused["ok"] is False and "budget exhausted" in refused["error"]
    assert tools.call("finish", note="out of budget")["ok"] is True
    assert tools.call("outline", page="concepts/growth-yield")["error"].startswith("this session")
    packed = {"record", "verdict", "page", "claims"}
    assert (
        set(BUDGETS)
        == set(workflow.SKILLS) | {"reader", "maintain", "card", "card_review"} | packed
    )


def test_a_reviewer_is_held_to_a_verdict_and_a_decorated_one_counts(root: Path):
    task = {"section": LEAD, "sha": "abc", "candidate": "New text."}
    reviewer = Tools(root, Session.start("review", task))
    early = reviewer.call("finish", note="looks fine")
    assert early["ok"] is False and "record your verdict" in early["error"]
    hedged = reviewer.call("review", section=LEAD, sha="abc", verdict="Accept once fixed.")
    assert hedged["ok"] is False and "single word" in hedged["error"]
    doubt = [{"quote": "New text.", "problem": "unsupported"}]
    mixed = reviewer.call("review", section=LEAD, sha="abc", verdict="accept", objections=doubt)
    assert mixed["ok"] is False and "takes no objections" in mixed["error"]
    said = reviewer.call("review", section=LEAD, sha="abc", verdict="Accept.")
    # The verdict is what the session was for, so the reply also ends it.
    assert said["recorded"] == "accept" and "session is over" in said["done"]
    assert reviewer.call("finish", note="accepted")["ok"] is True


def test_two_rejected_rounds_leave_the_page_and_queue_the_claim(root: Path):
    script = Script(verdicts=("accept", "revise", "revise"))
    result = workflow.ingest(root, "alpha", config(), script)
    assert result["outcomes"] == {"accepted": 1, "rejected": 1}
    assert (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8") == CONCEPT
    queued = Store(root).backlog("alpha")
    rejected = [q for q in queued if q["target"] == LEAD]
    assert [q["claim"] for q in rejected] == ["alpha:n0"]
    assert rejected[0]["reason"].startswith("rejected: ")


def test_budget_stop_resumes_and_retries_only_what_did_not_finish(root: Path):
    script = Script()
    # Each scripted session reports 1,100 tokens: the cap admits extract, curate and
    # the first edit, then refuses that edit's review and the second section.
    tight = config(max_tokens=3_400, reserve_tokens=1_000)
    stopped = workflow.ingest(root, "alpha", tight, script)
    assert stopped["status"] == "stopped" and stopped["outcomes"] == {"budget": 2}
    assert script.roles == ["extract", "curate", "edit"]
    resumed = workflow.ingest(root, "alpha", config(), script)
    assert resumed["status"] == "done" and resumed["run"] == stopped["run"]
    assert resumed["outcomes"] == {"accepted": 2}
    assert script.roles.count("extract") == 1 and script.roles.count("curate") == 1


def test_a_crash_between_page_and_sidecar_is_finished_on_resume(root: Path, monkeypatch):
    def crash(*args):
        monkeypatch.undo()
        raise RuntimeError("killed after the page was written")

    monkeypatch.setattr(tools, "rehome_figures", crash)
    script = Script()
    with pytest.raises(RuntimeError, match="killed"):
        workflow.ingest(root, "alpha", config(), script)
    assert not Store(root).sidecar_path("summaries/alpha__REPORT").exists()
    edits = script.roles.count("edit")
    assert workflow.ingest(root, "alpha", config(), script)["outcomes"] == {"accepted": 2}
    stamp = Store(root).sidecar("summaries/alpha__REPORT")["sections"]["lead"]["stamp"]
    assert stamp["reviewer"] == "claude-y@medium"
    # The half-applied section was completed from its journal, not written again.
    assert script.roles.count("edit") == edits


def test_an_extraction_that_did_not_read_the_report_records_nothing(root: Path):
    script = Script()
    script.skims = True
    result = workflow.ingest(root, "alpha", config(), script)
    assert result["status"] == "stopped" and "never read characters 0-" in result["reason"]
    assert Store(root).claims("alpha") == [] and "alpha" not in Store(root).sources()


LIMIT = Run("", error="Claude run ended: You've hit your limit · resets 9pm")
LOGGED_OUT = Run(
    "",
    error="Exception: Claude Code returned an error result: success",
    text="Not logged in · Please run /login",
)


@pytest.mark.parametrize(
    ("nth", "refusal", "reason"),
    [
        (1, LIMIT, "usage or rate limit"),
        (2, LIMIT, "usage or rate limit"),
        (1, LOGGED_OUT, "refused the login"),
    ],
)
def test_a_vendor_quota_error_stops_the_run_and_starts_nothing_else(
    root: Path, nth: int, refusal: Run, reason: str, monkeypatch
):
    """Whichever session meets the limit, the last of the run included, the run stops
    and the report is not marked as read. A vendor that is logged out stops it too."""
    script = Script()
    pauses: list[float] = []
    monkeypatch.setattr(workflow.time, "sleep", pauses.append)

    def launch(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        if kit.session.role == "review" and script.roles.count("review") == nth - 1:
            script.roles.append("review")
            return Run(str(agent), error=refusal.error, text=refusal.text)
        return script(agent, system, prompt, kit, work)

    stopped = workflow.ingest(root, "alpha", config(), launch)
    assert stopped["status"] == "stopped" and reason in stopped["reason"]
    assert "alpha" not in Store(root).sources()
    # Nothing was started after the review that hit the limit.
    assert script.roles == ["extract", "curate", "edit", "review", "edit", "review"][: 2 + 2 * nth]
    # A burst the vendor turned away is asked again within minutes, on the same model;
    # only a spent allowance waits the long pause.
    refusals = ["exceeded retry limit, last status: 429 Too Many Requests"] * 2

    def burst(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        if kit.session.role == "review" and refusals:
            return Run(str(agent), error=f"Codex turn failed: {refusals.pop()}")
        return script(agent, system, prompt, kit, work)

    resumed = workflow.ingest(root, "alpha", config(quota_wait=3600.0), burst)
    assert resumed["status"] == "done" and resumed["run"] == stopped["run"]
    assert len(pauses) == 2 and 60 <= pauses[0] <= 90 and 120 <= pauses[1] <= 180, pauses
    # A session that ran out of tool calls is not a vendor limit.
    assert not workflow.QUOTA.search("maximum tool-call limit reached")
    # A reply that mentions a login in passing is not a refused login, and a refused
    # login is one even when the error beside it reads like a full vendor.
    prose = "The participants were not logged in when recording started."
    assert not workflow.logged_out(Run("", error="error_max_turns", text=prose))
    assert workflow.logged_out(Run("", error="status 503", text=LOGGED_OUT.text))


def test_sessions_refused_and_failing_side_by_side_leak_no_place_and_no_budget(
    root: Path, monkeypatch
):
    """Eight threads, sixty sessions, a vendor that turns some away and some that
    crash. Afterwards every place is free, nothing is held, and the run's tokens are
    the sum of what its sessions reported."""
    from concurrent.futures import ThreadPoolExecutor

    monkeypatch.setattr(workflow.time, "sleep", lambda seconds: None)
    seen: dict[str, int] = {}
    most = [0]

    def launch(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        n = int(prompt)
        seen[prompt] = seen.get(prompt, 0) + 1
        most[0] = max(most[0], runner.active)
        if n % 7 == 0 and seen[prompt] < 3:
            return Run(str(agent), error="Codex turn failed: last status: 429 Too Many Requests")
        if n % 13 == 0 and seen[prompt] < 2:
            # A vendor outage of a few minutes: the same session is asked again.
            return Run(str(agent), error="Codex turn failed: workspace routing discovery timed out")
        if n % 11 == 0:
            raise RuntimeError("harness crashed")
        return Run(str(agent), ok=True, input_tokens=100, output_tokens=10)

    runner = workflow.Runner(root, config(jobs=4, quota_wait=10**6), "probe", "limits", launch)

    def one(n: int) -> bool:
        return runner.dispatch(f"s{n}", "extract", {"source": "alpha"}, str(n))[1].ok

    with ThreadPoolExecutor(max_workers=8) as pool:
        done = list(pool.map(one, range(1, 61)))
    assert done.count(False) == 5 and most[0] <= 4, (done.count(False), most)
    assert runner.active == 0 and not any(runner.running.values()) and not runner.halted
    assert abs(runner.held_usd) < 1e-9 and not runner.state["open"] and not runner.state["waiting"]
    used = sum(s["input_tokens"] + s["output_tokens"] for s in runner.state["sessions"])
    # A crash reports no usage and keeps what was held for it.
    assert runner.state["tokens"] == used + 5 * config().reserve_tokens
    assert runner.state["held"] == 0
    # The vendor's refusals lowered the model's limit, and successes raised it again.
    assert 1 <= runner.limits["gpt-x"] <= 4


def test_status_tells_a_working_run_from_one_that_needs_someone():
    now = 10_000.0
    ok = {"ok": True, "error": "", "at": now - 20}
    bad = {"ok": False, "error": "TimeoutError: no reply", "at": now - 20}
    state = {"status": "running", "pid": 1, "sessions": [ok] * 12, "open": {"a": now - 60}}
    health = workflow.health
    assert health(state, now, True) == ("ok", "")
    assert health(state, now, False)[0] == "dead"
    assert health(state | {"sessions": [ok] * 6 + [bad] * 6}, now, True)[0] == "failing"
    # A vendor that turns requests away is waited on; that is not the run failing.
    busy = bad | {"error": "Codex turn failed: last status: 429 Too Many Requests"}
    assert health(state | {"sessions": [ok] * 6 + [busy] * 9}, now, True)[0] == "ok"
    # A short vendor pause is the run working; a long one is worth a look.
    brief = {"b": {"until": now + 90, "why": "gpt-x reports a usage or rate limit"}}
    assert health(state | {"waiting": brief}, now, True)[0] == "ok"
    brief["b"]["until"] = now + 900
    assert health(state | {"waiting": brief}, now, True)[0] == "waiting"
    assert health(state | {"open": {"a": now - 1500}}, now, True)[0] == "stuck"
    quiet = state | {"open": {}, "sessions": [ok | {"at": now - 700}]}
    assert health(quiet, now, True)[0] == "idle"
    assert health(state | {"status": "done"}, now, False)[0] == "done"


def test_a_rejected_summary_stops_the_run_before_anything_links_to_it(root: Path):
    # The summary is the first section edited; a stubborn editor fails both rounds.
    script = Script(verdicts=("revise", "revise"), stubborn=True)
    script.extracted.append(claim("caveat", "Only one strain was tested.", LIMIT_QUOTE))
    stopped = workflow.ingest(root, "alpha", config(), script)
    assert stopped["status"] == "stopped" and "summary page was not accepted" in stopped["reason"]
    # A finding page links to its report's summary; none was written without one.
    assert "records" not in stopped and not list((root / "wiki/findings").glob("alpha--*.md"))
    resumed = workflow.ingest(root, "alpha", config(), Script())
    assert resumed["status"] == "done" and resumed["run"] == stopped["run"]
    assert (root / "wiki/summaries/alpha__REPORT.md").exists()
    assert resumed["records"]["findings"] == {"accepted": 1}


def test_a_revision_retires_what_was_written_about_a_withdrawn_finding(root: Path):
    """The headline, its plain summary and its literature label go with the claim, even
    when the replacement fails; the run then stays open until the replacement lands."""
    first = Script()
    first.extracted.append(claim("caveat", "Only one strain was tested.", LIMIT_QUOTE))
    assert workflow.ingest(root, "alpha", config(), first)["status"] == "done"
    (old,) = (root / "wiki/findings").glob("alpha--*.md")
    # A second headline that rests only on the caveat, which the revision keeps.
    headlines_path = root / "state/headlines.json"
    saved = json.loads(headlines_path.read_text("utf-8"))
    kept = dict(saved["alpha"]["reply"]["headlines"][0])
    kept["evidence"] = kept["caveat_evidence"]
    saved["alpha"]["reply"]["headlines"].append(kept)
    survivor = old.with_name("alpha--5eed5eed.md")
    survivor.write_text(old.read_text("utf-8"), encoding="utf-8")
    saved["alpha"]["pages"][survivor.name] = "sha"
    headlines_path.write_text(json.dumps(saved), encoding="utf-8")
    revised = ALPHA.replace("0.42 g/g on glucose in 12,500", "0.47 g/g on glucose in 12,500")
    (root / "corpus/projects/alpha/REPORT.md").write_text(revised, encoding="utf-8")
    script = Script(body=GOOD.replace("0.42", "0.47"))
    script.extracted = [
        claim("finding", YIELD_TEXT.replace("0.42", "0.47"), YIELD_QUOTE.replace("0.42", "0.47"))
    ]
    # The scripted headline still says 0.42, which the new quote does not contain.
    stopped = workflow.revise(root, "alpha", config(), script)
    assert stopped["status"] == "stopped" and "1 record job(s)" in stopped["reason"], stopped
    assert not old.exists() and survivor.exists()
    assert list(json.loads(headlines_path.read_text("utf-8"))["alpha"]["pages"]) == [survivor.name]
    for name in ("gists", "novelty", "outcomes"):
        assert old.stem not in json.loads((root / f"state/{name}.json").read_text("utf-8"))

    class Corrected(Script):
        @staticmethod
        def record(key: str, pack: dict) -> dict:
            record = Script.record(key, pack)
            if key.startswith("findings/"):
                record = json.loads(json.dumps(record).replace("0.42", "0.47"))
            return record

    # Everything but the record stages is on record, so only they run again.
    resumed = workflow.revise(root, "alpha", config(), Corrected())
    assert resumed["status"] == "done" and resumed["run"] == stopped["run"], resumed
    (new,) = (root / "wiki/findings").glob("alpha--*.md")
    assert new.stem != old.stem and "0.47" in new.read_text(encoding="utf-8")
    assert new.stem in json.loads((root / "state/gists.json").read_text("utf-8"))


def test_a_record_job_keeps_a_refusal_and_an_accepted_record_across_a_stop(root: Path):
    stored: list[dict] = []
    started: list[str] = []

    def agent_giving(verdict: str, fail_after: int = 99):
        def launch(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
            started.append(kit.session.role)
            if len(started) > fail_after:
                return Run(str(agent), error="connection reset")
            if kit.session.role == "record":
                kit.call("submit_record", record={"gist": "the same words"})
            else:
                task = kit.session.task
                problems = [{"quote": "", "problem": "too strong"}] if verdict == "revise" else []
                kit.call(
                    "review",
                    section=task["section"],
                    sha=task["sha"],
                    verdict=verdict,
                    objections=problems,
                )
            kit.call("finish", note="")
            return Run(str(agent), ok=True, input_tokens=1)

        return launch

    def job(key: str, publish) -> jobs.Job:
        return jobs.Job(stage="gists", key=key, pack={}, check=lambda r: r, publish=publish)

    # Refused in round one, then the writer's session dies. The resumed run must not
    # send the same refused record to a reviewer that knows nothing of the refusal.
    runner = workflow.Runner(root, config(), "ingest", "alpha", agent_giving("revise", 2))
    assert jobs.run_job(runner, job("gists/a", stored.append))["status"] == "failed"
    runner = workflow.Runner(root, config(), "ingest", "alpha", agent_giving("accept"))
    assert jobs.run_job(runner, job("gists/a", stored.append))["status"] == "rejected"
    assert stored == []

    # Accepted, then the run dies while the record is being stored: the resumed run
    # stores the reviewed record again and pays for no session.
    def dies_once(record: dict) -> None:
        stored.append(record)
        if len(stored) == 1:
            raise OSError("disk full")

    with pytest.raises(OSError):
        jobs.run_job(runner, job("gists/b", dies_once))
    del started[:]
    runner = workflow.Runner(root, config(), "ingest", "alpha", agent_giving("accept"))
    assert jobs.run_job(runner, job("gists/b", dies_once))["status"] == "accepted"
    assert started == [] and stored == [{"gist": "the same words"}] * 2


def test_one_writer_per_checkout(root: Path):
    with checkout_lock(root), pytest.raises(workflow.Stop, match="owns this checkout"):
        workflow.ingest(root, "alpha", config(), Script())


def test_writer_and_reviewer_must_be_different_vendors(root: Path):
    same = config()
    same.roles["review"] = Agent.parse("gpt-z")
    with pytest.raises(workflow.Stop, match="same vendor"):
        workflow.ingest(root, "alpha", same, Script())


def test_revise_edits_only_the_section_the_changed_claim_supports(root: Path):
    workflow.ingest(root, "alpha", config(), Script())
    summary_before = (root / "wiki/summaries/beta__REPORT.md").read_text(encoding="utf-8")
    # A page that states the old figure but was never linked to the claim behind it.
    unlinked = root / "wiki/entities/strain-a.md"
    unlinked.parent.mkdir()
    unlinked.write_text("# Strain A\n\nIts yield was 0.42 g/g [src: alpha].\n", encoding="utf-8")
    revised = ALPHA.replace("0.42 g/g on glucose in 12,500", "0.47 g/g on glucose in 12,500")
    # The old value survives elsewhere in the report, for a different result.
    revised += "\n## Pilot\n\nA pilot batch of another strain gave 0.42 g/g.\n"
    (root / "corpus/projects/alpha/REPORT.md").write_text(revised, encoding="utf-8")
    script = Script(body=GOOD.replace("0.42", "0.47"))
    script.extracted = [
        claim("null", NULL_TEXT, NULL_QUOTE),
        claim("finding", YIELD_TEXT.replace("0.42", "0.47"), YIELD_QUOTE.replace("0.42", "0.47")),
    ]
    store = Store(root)
    sorted_ = workflow.carry_forward(store, "alpha")
    # The limitations block did not change; both findings share the block that did.
    assert sorted_["affected"] == ["alpha:n0", "alpha:n1"] and len(sorted_["changed"]) == 2
    result = workflow.revise(root, "alpha", config(), script)
    assert result["status"] == "done", result
    assert (result["confirmed"], result["withdrawn"], result["new_claims"]) == (1, 1, 1)
    status = {c["id"]: c["status"] for c in store.claims("alpha")}
    assert status == {"alpha:n0": "retracted", "alpha:n1": "active", "alpha:n3": "active"}
    # n2 confirmed n1 and was dropped; the next claim must not take a number in use.
    later = Tools(root, Session.start("extract", {"source": "alpha"}))
    quote = "A pilot batch of another strain gave 0.42 g/g."
    later.call("submit_claims", claims=[claim("finding", "A pilot batch gave 0.42 g/g.", quote)])
    assert later.session.claims[0]["id"] == "alpha:n4"
    edited = {s["section"] for s in result["sections"]}
    assert edited == {LEAD, "summaries/alpha__REPORT#lead", "entities/strain-a#lead"}
    assert "0.42" not in unlinked.read_text(encoding="utf-8")
    lead = body((root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8"), "lead")
    assert "0.47" in lead and "0.42" not in lead
    links = store.sidecar("concepts/growth-yield")["sections"]["lead"]["claims"]
    assert links == {"alpha:n3": "edit", "beta:0:0": "number"}
    assert (root / "wiki/summaries/beta__REPORT.md").read_text(encoding="utf-8") == summary_before
    assert workflow.plan(root) == {"tasks": []}
    # Applying the recorded settlement again, as a resumed run does, changes nothing.
    record = json.loads((root / ".agentic/runs" / result["run"] / "run.json").read_text("utf-8"))
    before = store.claims("alpha")
    workflow.apply_settlement(store, "alpha", record["steps"]["settle"])
    assert store.claims("alpha") == before
    assert not workflow.same_statement("Treatment increased growth.", "Treatment decreased growth.")


def test_a_newer_revision_inherits_the_corrections_an_unfinished_one_owed(root: Path, monkeypatch):
    workflow.ingest(root, "alpha", config(), Script())
    report = root / "corpus/projects/alpha/REPORT.md"
    report.write_text(ALPHA.replace("0.42", "0.47"), encoding="utf-8")
    second = Script(body=GOOD.replace("0.42", "0.47"))
    second.extracted = [
        claim("finding", YIELD_TEXT.replace("0.42", "0.47"), YIELD_QUOTE.replace("0.42", "0.47")),
        claim("null", NULL_TEXT, NULL_QUOTE),
    ]

    def crash(*args):
        raise RuntimeError("killed after the claims were settled")

    monkeypatch.setattr(workflow, "stale_sections", crash)
    with pytest.raises(RuntimeError, match="killed"):
        workflow.revise(root, "alpha", config(), second)
    monkeypatch.undo()
    # The report is corrected again before anyone resumes; the first revision's
    # report text is gone, and the page still states the figure it withdrew.
    report.write_text(ALPHA.replace("0.42", "0.48"), encoding="utf-8")
    third = Script(body=GOOD.replace("0.42", "0.48"))
    third.extracted = [
        claim("finding", YIELD_TEXT.replace("0.42", "0.48"), YIELD_QUOTE.replace("0.42", "0.48")),
        claim("null", NULL_TEXT, NULL_QUOTE),
    ]
    assert workflow.revise(root, "alpha", config(), third)["status"] == "done"
    assert "0.42" in body((root / "wiki/concepts/growth-yield.md").read_text("utf-8"), "lead")
    assert LEAD in workflow.plan(root)["corrections_owed"]


def test_a_correction_that_fails_review_stays_owed_until_refresh_settles_it(root: Path):
    workflow.ingest(root, "alpha", config(), Script())
    revised = ALPHA.replace("0.42 g/g on glucose in 12,500", "0.47 g/g on glucose in 12,500")
    (root / "corpus/projects/alpha/REPORT.md").write_text(revised, encoding="utf-8")
    script = Script(body=GOOD.replace("0.42", "0.47"), verdicts=("revise",), stubborn=True)
    script.extracted = [
        claim("finding", YIELD_TEXT.replace("0.42", "0.47"), YIELD_QUOTE.replace("0.42", "0.47")),
        claim("null", NULL_TEXT, NULL_QUOTE),
    ]
    result = workflow.revise(root, "alpha", config(), script)
    assert result["status"] == "done" and result["outcomes"] == {"rejected": 1, "accepted": 1}
    # The returned text came back unchanged, so no reviewer was asked a second time.
    assert script.roles.count("review") == 2
    assert "0.42" in body((root / "wiki/concepts/growth-yield.md").read_text("utf-8"), "lead")
    owed = [q["claim"] for q in Store(root).backlog("alpha") if q.get("withdrawn")]
    assert owed == ["alpha:n0"]
    assert workflow.plan(root) == {"tasks": [], "corrections_owed": [LEAD]}
    fixed = Script(body=GOOD.replace("0.42", "0.47"))
    assert workflow.refresh(root, [LEAD], "apply the revision", config(), fixed)["outcomes"] == {
        "accepted": 1
    }
    assert "0.42" not in body((root / "wiki/concepts/growth-yield.md").read_text("utf-8"), "lead")
    assert workflow.plan(root) == {"tasks": []}


BOTH = ["alpha:n0", "alpha:n1"]
PLANS = {
    "placed more than once": (
        [{"section": LEAD, "claims": BOTH}],
        [{"claims": ["alpha:n1"], "reason": "summary"}],
    ),
    "already a target": (
        [{"section": LEAD, "claims": BOTH[:1]}, {"section": LEAD, "claims": BOTH[1:]}],
        [],
    ),
    "not edited from a plan": ([{"section": "summaries/beta__REPORT#lead", "claims": BOTH}], []),
    "kind concepts or entities": (
        [{"new_page": {"kind": "conflicts", "title": "Yield"}, "claims": BOTH}],
        [],
    ),
    "support must list claims": (
        [
            {
                "new_page": {"kind": "concepts", "title": "Yield Limits"},
                "claims": BOTH,
                "support": ["gamma:0:0"],
            }
        ],
        [],
    ),
    "needs new_page.type": (
        [
            {
                "new_page": {"kind": "entities", "title": "Strain A"},
                "claims": BOTH,
                "support": ["beta:0:0"],
            }
        ],
        [],
    ),
}


@pytest.mark.parametrize("objection", PLANS)
def test_plan_gate_refuses(root: Path, objection: str):
    targets, skipped = PLANS[objection]
    workflow.ingest(root, "alpha", config(), Script())
    session = Session.start("curate", {"claims": ["alpha:n0", "alpha:n1"]})
    reply = Tools(root, session).call("propose_plan", targets=targets, skipped=skipped)
    assert reply["ok"] is False and objection in json.dumps(reply)


def test_a_new_page_needs_a_second_project_and_takes_its_claims(root: Path):
    workflow.ingest(root, "alpha", config(), Script())
    session = Session.start("curate", {"claims": ["alpha:n0", "alpha:n1"]})
    new = {"new_page": {"kind": "concepts", "title": "Yield Limits"}, "claims": ["alpha:n0"]}
    skip = [{"claims": ["alpha:n1"], "reason": "summary"}]
    alone = Tools(root, session).call("propose_plan", targets=[new], skipped=skip)
    assert alone["targets"] == 0 and "needs two projects" in alone["queued"][0]
    backed = Tools(root, session).call(
        "propose_plan", targets=[{**new, "support": ["beta:0:0"]}], skipped=skip
    )
    assert backed["targets"] == 1 and session.plan is not None
    assert session.plan["targets"][0]["support"] == ["beta:0:0"]
    assert session.plan["targets"][0]["new_page"]["type"] == "Concept"


def test_import_writes_block_baselines_and_refuses_to_run_twice(root: Path, tmp_path: Path):
    shutil.rmtree(root / "knowledge")
    legacy = tmp_path / "legacy"
    (legacy / "evidence").mkdir(parents=True)
    at = BETA.find(BETA_QUOTE)
    finding = {"id": "beta:0:0", "source": "beta", "kind": "finding", "quote": BETA_QUOTE,
               "claim": "Strain B yield was 0.38 g/g on acetate.",
               "start": at, "end": at + len(BETA_QUOTE)}  # fmt: skip
    coverage = [{"source": "beta__REPORT.md", "sha256": sha256(BETA)}]
    evidence = {"findings": [finding], "coverage": coverage}
    (legacy / "evidence" / "a.json").write_text(json.dumps(evidence), encoding="utf-8")
    routing = [{"evidence": "beta:0:0", "concepts": ["concepts/growth-yield.md"]}]
    (legacy / "last-plan.json").write_text(json.dumps({"coverage": routing}), encoding="utf-8")
    assert importer.run(root, legacy)["claims"] == 1
    store = Store(root)
    assert store.sources()["beta"]["blocks"] == [h for _, _, h in blocks(BETA)]
    assert store.sidecar("concepts/growth-yield")["sections"]["lead"]["claims"] == {
        "beta:0:0": "number"
    }
    assert (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8") == CONCEPT
    with pytest.raises(SystemExit, match="already holds records"):
        importer.run(root, legacy)


def test_refresh_edits_named_sections_and_nothing_schedules_it(root: Path):
    workflow.ingest(root, "alpha", config(), Script())
    better = GOOD.replace("a similar range", "the same range")
    result = workflow.refresh(root, [LEAD], "say the ranges match", config(), Script(body=better))
    assert result["outcomes"] == {"accepted": 1}
    assert (
        body((root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8"), "lead") == better
    )
    assert Store(root).backlog() == [] and workflow.plan(root) == {"tasks": []}
    # Two findings wait for the section; the editor uses one and declines the other.
    store = Store(root)
    store.queue("alpha", workflow.queue_rows("r", "alpha", LEAD, ["alpha:n1", "alpha:n0"], "cap"))
    workflow.refresh(root, [LEAD], "place what is queued", config(), Script(body=GOOD + " More."))
    assert [q["claim"] for q in store.backlog()] == ["alpha:n1"]
    with pytest.raises(workflow.Stop, match="max-sections"):
        workflow.refresh(root, [LEAD] * 13, "too many", config(), Script())


def test_index_rebuilds_itself_and_search_finds_by_alias_and_text(root: Path):
    tools = Tools(root)
    found = tools.call("search", query="acetate yield")
    assert found["sections"][0]["section"] == LEAD
    assert tools.call("search", query="Growth Yield")["pages"][0]["page"] == "concepts/growth-yield"
    index.db_path(root).unlink()
    outline = tools.call("outline", page="concepts/growth-yield")
    assert [s["claims"] for s in outline["sections"]] == [1, 0, 0]
    assert workflow.impact(root, claim="beta:0:0")["sections"][0]["section"] == LEAD


def test_publish_lists_a_queued_finding_on_its_page_and_not_an_owed_correction(root: Path):
    from beril_wiki.publish.ingest import queued_findings

    workflow.ingest(root, "alpha", config(), Script())
    store = Store(root)
    assert queued_findings(root) == {}
    store.queue("alpha", workflow.queue_rows("r", "alpha", LEAD, ["alpha:n1"], "cap"))
    store.queue("alpha", workflow.queue_rows("r", "alpha", LEAD, ["alpha:n0"], "cap", True))
    assert queued_findings(root) == {"concepts/growth-yield.md": [f"- {NULL_TEXT} [src: alpha]"]}


def test_figures_follow_their_paragraph_through_an_edit(root: Path):
    import hashlib

    store = Store(root)
    old = CONCEPT
    new = pages.replace(CONCEPT, "lead", GOOD + "\n\nA second paragraph [src: beta].")
    state = root / "state/figures-placements.json"
    state.parent.mkdir()
    entry = {
        "page_hash": hashlib.sha256(old.encode()).hexdigest()[:16],
        "placements": [{"after_paragraph": 3, "file": "figures/a.png", "project": "beta"}],
    }
    state.write_text(json.dumps({"concepts/growth-yield.md": entry}), encoding="utf-8")
    rehome_figures(store, "concepts/growth-yield", old, new)
    moved = json.loads(state.read_text(encoding="utf-8"))["concepts/growth-yield.md"]
    # "None recorded yet." was paragraph 3 and is paragraph 4 after the lead grew by one.
    assert moved["placements"][0]["after_paragraph"] == 4
    assert moved["page_hash"] == hashlib.sha256(new.encode()).hexdigest()[:16]
