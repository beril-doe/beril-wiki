"""A compile from an empty wiki, with scripted agents in place of models.

What these guard: every page is written once from all the claims routed to it and cites
reports, never claim tags; a statement the reviewer still faults after the last round is
removed, not published; a stopped compile resumes without paying for a finished step;
and a page that states a number its cited report lacks is refused.
"""

import json
from pathlib import Path
from types import SimpleNamespace
from typing import cast

import pytest

from beril_wiki.kb import compile as compiler
from beril_wiki.kb.agents import Agent, Run
from beril_wiki.kb.store import Store
from beril_wiki.kb.tools import NOT_PLACED, REJECTIONS, Session, Tools, page_candidate
from beril_wiki.kb.workflow import Runner
from test_kb import ALPHA, BETA, BETA_QUOTE, LIMIT_QUOTE, NULL_QUOTE, YIELD_QUOTE, claim, config

REPO = Path(__file__).resolve().parents[1]
TOPICS = [{"slug": "growth", "title": "Growth", "scope": "How fast and how far cells grow."}]
EXTRACTED = {
    "alpha": [
        claim("finding", "Strain A yield was 0.42 g/g on glucose.", YIELD_QUOTE),
        claim("null", "Temperature had no detected effect on yield.", NULL_QUOTE),
        claim("caveat", "Only one strain was tested.", LIMIT_QUOTE),
    ],
    "beta": [claim("finding", "Strain B yield was 0.38 g/g on acetate.", BETA_QUOTE)],
}
OVERSTATED = "Yield is the same in every strain"


@pytest.fixture
def root(tmp_path: Path) -> Path:
    import shutil

    files = {
        "corpus/projects/alpha/REPORT.md": ALPHA,
        "corpus/projects/beta/REPORT.md": BETA,
        "knowledge/topics.json": json.dumps(TOPICS),
        "contract/AGENTS.md": "## Domain Rules\nCite everything.\n## Frontmatter\nnone\n",
    }
    for name, text in files.items():
        path = tmp_path / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    shutil.copytree(REPO / "skills", tmp_path / "skills")
    return tmp_path


class Script:
    """Each session makes the one call a model would."""

    def __init__(self, verdicts: tuple[str, ...] = (), fail_at: int = 10**6) -> None:
        self.verdicts = list(verdicts)
        self.fail_at = fail_at
        self.started: list[str] = []

    def __call__(self, agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        role, task = kit.session.role, kit.session.task
        self.started.append(role)
        if len(self.started) > self.fail_at:
            return Run(str(agent), error="connection reset")
        if role == "claims":
            reply = kit.call("submit_claims", claims=EXTRACTED[task["source"]])
            assert reply["ok"] and "done" in reply, reply
        elif role == "record":
            key = prompt.removeprefix("Record to write: ").partition("\n")[0]
            reply = kit.call("submit_record", record=self.record(key))
            assert reply["ok"], reply
        elif role == "page":
            lines = [f"{task['claims'][t]['text']} [{t}]" for t in task["new"]]
            concept = task["page"].startswith("concepts/")
            # The whole lead of a concept page is the sentence the reviewer faults.
            lead = f"{OVERSTATED} [{task['new'][0]}]." if concept else lines[0]
            body = f"{lead}\n\n## Key Findings\n\n" + "\n".join(f"- {x}" for x in lines)
            if task.get("part"):
                # One section of a long summary: no lead of its own, no ## heading.
                body = "\n\n".join(lines)
            if concept:
                body += "\n\n## Open Directions\n\n- Compare substrates under one protocol."
            reply = kit.call("write_page", body=body, declined=[])
            assert reply["ok"], reply
        elif role == "verdict":
            verdict = "accept"
            if task["section"].startswith("concepts/") and self.verdicts:
                verdict = self.verdicts.pop(0)
            faults = [{"quote": OVERSTATED, "problem": "no claim says this"}]
            kit.call(
                "review",
                section=task["section"],
                sha=task["sha"],
                verdict=verdict,
                objections=faults if verdict == "revise" else [],
            )
        return Run(str(agent), ok=True, input_tokens=1000, output_tokens=100)

    @staticmethod
    def record(key: str) -> dict:
        stage, _, rest = key.partition("/")
        if stage == "propose":
            ids = [f"n{n}" for n in range(len(EXTRACTED[rest]))]
            page = {"title": f"Growth yield, {len(ids)} claims", "scope": "Yield per gram of feed."}
            return {"concepts": [{**page, "topic": "growth", "claims": ids}], "entities": []}
        if stage == "consolidate":
            return {
                "pages": [
                    {
                        "title": "Growth Yield",
                        "scope": "Biomass made per gram of substrate, across strains.",
                        "topic": "growth",
                        "members": ["K1", "K2"],
                    }
                ],
                "dropped": [],
            }
        return {"routes": []}


def test_a_compile_writes_each_page_once_and_resumes_without_paying_twice(root: Path):
    # The reviewer faults one sentence of the concept page in both rounds.
    script = Script(verdicts=("revise", "revise"), fail_at=7)
    first = compiler.compile_corpus(root, config(), launch=script, records=False)
    assert first["status"] == "stopped", first
    before = len(script.started)
    script.fail_at = 10**6
    result = compiler.compile_corpus(root, config(), launch=script, records=False)
    assert result["reason"] == "pages written; record stages not run", result
    # The extractions, proposals, page list and first routing were on record; only the
    # routing that failed ran again.
    resumed = script.started[before:]
    assert "claims" not in resumed and resumed.count("record") == 1, resumed

    concept = (root / "wiki/concepts/growth-yield.md").read_text(encoding="utf-8")
    assert "[src: alpha]" in concept and "[src: beta]" in concept and "[C" not in concept
    assert "0.42 g/g" in concept and "0.38 g/g" in concept
    assert 'sources: ["summaries/alpha__REPORT.md", "summaries/beta__REPORT.md"]' in concept
    # What the reviewer still faulted after the last round is not published.
    assert OVERSTATED not in concept and result["pages"]["struck"] == 1
    # The struck sentence was the whole lead, so the page's description stands in for it.
    assert "\nBiomass made per gram of substrate, across strains.\n\n## Key Findings" in concept
    linked = Store(root).sidecar("concepts/growth-yield")["sections"]
    assert {"alpha:n0", "beta:n0"} <= {c for s in linked.values() for c in s["claims"]}
    assert (root / "wiki/summaries/alpha__REPORT.md").exists()
    assert result["pages"]["accepted"] == 3 and result["pages"]["claims_used"] == 8


def test_a_long_report_is_summarised_part_by_part_from_all_of_its_claims(root: Path, monkeypatch):
    """Past three passes a summary is an overview and one section for each part of the
    report. Every claim reaches a writer, no session sees the whole page, and a second
    run asks for none of it again."""
    monkeypatch.setattr(compiler, "SECTIONED", 2)
    monkeypatch.setattr(compiler, "PART_CLAIMS", 2)
    script = Script()
    briefs: dict[str, list[str]] = {"page": [], "verdict": []}

    def launch(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        briefs.setdefault(kit.session.role, []).append(prompt)
        if kit.session.role == "page" and len(briefs["page"]) == 1:
            # A writer that answers with the page as text and calls no tool.
            return Run(str(agent), ok=True, text="The page, as a reply.")
        return script(agent, system, prompt, kit, work)

    result = compiler.compile_corpus(root, config(), launch=launch, records=False)
    assert result["pages"]["accepted"] == 3, result
    # The writer that only replied was asked once more, with its reply, to submit it.
    assert sum("YOUR UNSUBMITTED REPLY\nThe page, as a reply." in b for b in briefs["page"]) == 1
    page = (root / "wiki/summaries/alpha__REPORT.md").read_text(encoding="utf-8")
    # The overview, then the report's two sections in its order; a report section
    # named like one of the page's own gets a name that says what it is.
    heads = ["## Key Findings", "## Report section: Key Findings", "## Limitations"]
    assert [page.index(h) for h in heads] == sorted(page.index(h) for h in heads), page
    assert "Only one strain was tested. [src: alpha]" in page and page.count("0.42 g/g") == 3
    linked = Store(root).sidecar("summaries/alpha__REPORT")["sections"]
    assert set(linked["limitations"]["claims"]) == {"alpha:n2"}
    sessions = len(script.started)
    compiler.compile_corpus(root, config(), launch=script, records=False)
    assert len(script.started) == sessions
    # A part on record for other claims than the plan now gives it is written again:
    # its text would otherwise be linked to claims it was not written from.
    run = next((root / ".agentic/runs").glob("*/run.json"))
    state = json.loads(run.read_text(encoding="utf-8"))
    state["steps"]["page-summaries/alpha__REPORT-p100"]["of"] = "another cut"
    run.write_text(json.dumps(state), encoding="utf-8")
    compiler.compile_corpus(root, config(), launch=script, records=False)
    assert script.started[sessions:] == ["page", "verdict"]
    # A short last part joins the one before it, and every claim is still in one part.
    monkeypatch.setattr(compiler, "PART_CLAIMS", 10)
    claims = [{"id": f"n{n}", "start": n} for n in range(21)]
    parts = compiler.report_parts(claims, "no headings")
    assert [len(rows) for _, rows in parts] == [10, 11]
    assert [c for _, rows in parts for c in rows] == claims


def test_a_run_of_refused_pages_stops_the_compile_and_a_retry_writes_them(root: Path, monkeypatch):
    """A fault in a skill or a check refuses page after page. The run stops at the first
    few instead of paying for the whole list, and writes them again once told to."""
    monkeypatch.setattr(compiler, "CANARY", 2)
    monkeypatch.setattr(compiler, "each", lambda runner, items, work: [work(i) for i in items])

    class Untagged(Script):
        def __call__(self, agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
            if kit.session.role != "page":
                return super().__call__(agent, system, prompt, kit, work)
            self.started.append("page")
            # Refused as often as a session may try: an answer, not an outage.
            for _ in range(REJECTIONS):
                kit.call(
                    "write_page", body=f"{OVERSTATED}, in all the strains ever tested.", declined=[]
                )
            return Run(str(agent), ok=True, input_tokens=1000, output_tokens=100)

    stopped = compiler.compile_corpus(root, config(), launch=(bad := Untagged()), records=False)
    assert stopped["status"] == "stopped" and "2 of the last 2 page passes" in stopped["reason"], (
        stopped
    )
    # The third page was never sent to a model.
    assert bad.started.count("page") == 2, bad.started
    again = compiler.compile_corpus(root, config(), launch=bad, records=False)
    assert bad.started.count("page") == 3, "a refused page is not written again unasked"
    assert again["pages"]["rejected"] == 3, again
    fixed = compiler.compile_corpus(root, config(), launch=Script(), records=False, retry=True)
    assert fixed["pages"]["accepted"] == 3, fixed
    # A pass accepted after a refused one built on the page that pass left, so a retry
    # writes both again; another page keeps its record.
    steps = {
        "page-concepts/a-p0": {"status": "accepted"},
        "page-concepts/a-p1": {"status": "rejected"},
        "page-concepts/a-p2": {"status": "accepted"},
        "page-concepts/b-p0": {"status": "accepted"},
    }
    held = cast(Runner, SimpleNamespace(state={"steps": steps}, dir=root, save=lambda: None))
    assert compiler.forget_refused_pages(held) == 2
    assert sorted(steps) == ["page-concepts/a-p0", "page-concepts/b-p0"]


def test_a_merge_the_reviewer_refused_is_undone_when_the_page_list_is_given_up(root: Path):
    """The reviewer refuses the merge of two candidates and the second writer fails its
    checks on every attempt. The list that is kept holds only merges nobody faulted, so
    the two candidates stay two pages."""
    script = Script()
    asked: list[str] = []

    def launch(agent: Agent, system: str, prompt: str, kit: Tools, work: Path) -> Run:
        role, task = kit.session.role, kit.session.task
        key = prompt.removeprefix("Record to write: ").partition("\n")[0]
        if role == "record" and key.startswith("consolidate/"):
            asked.append(key)
            if len(asked) > 1:
                for _ in range(REJECTIONS):
                    assert not kit.call("submit_record", record={"pages": [{"title": "x"}]})["ok"]
                return Run(str(agent), ok=True)
        if role == "verdict" and task["section"].startswith("consolidate/"):
            fault = {"quote": "Growth Yield", "problem": "K1 and K2 answer different questions"}
            kit.call(
                "review",
                section=task["section"],
                sha=task["sha"],
                verdict="revise",
                objections=[fault],
            )
            return Run(str(agent), ok=True)
        return script(agent, system, prompt, kit, work)

    result = compiler.compile_corpus(root, config(), launch=launch, records=False)
    assert len(asked) == 2 and result["catalog"]["pages"] == 2, result
    # The report with one claim on the question is too thin for a page of its own.
    assert result["pages"]["too_thin"] == 1 and result["pages"]["accepted"] == 3, result
    # What no page cites is on record, read from the pages as published.
    uncited = json.loads((root / "knowledge/routes/uncited.json").read_text(encoding="utf-8"))
    assert result["pages"]["claims_on_no_page"] == sum(len(ids) for ids in uncited.values())


def test_a_page_is_refused_for_an_unsupported_number_or_an_untagged_statement(root: Path):
    task = {
        "page": "concepts/growth-yield",
        "claims": {"C1": {"id": "alpha:n0", "source": "alpha", "text": "x", "quote": YIELD_QUOTE}},
        "kept": [],
        "links": [],
        "required": ["Open Directions"],
    }
    good = "Strain A reached 0.42 g/g on glucose [C1].\n\n## Open Directions\n\n- Test acetate."
    candidate, problems = page_candidate(Store(root), task, good, [])
    assert not problems and candidate["rendered"].startswith("Strain A reached 0.42 g/g")
    assert "[src: alpha]" in candidate["rendered"] and candidate["sections"] == {
        "lead": ["alpha:n0"]
    }

    wrong = good.replace("0.42", "0.47")
    assert any("figures not found" in p for p in page_candidate(Store(root), task, wrong, [])[1])
    bare = good.replace(" [C1]", "")
    faults = page_candidate(Store(root), task, bare, [])[1]
    assert any("no claim tag" in p for p in faults) and any("neither cited" in p for p in faults)
    # A page whose statements all hold but which leaves a claim out is refused twice,
    # then taken with that claim on record as not placed: the pass is not thrown away.
    two = task | {"claims": task["claims"] | {"C2": task["claims"]["C1"] | {"id": "alpha:n1"}}}
    kit = Tools(root, Session.start("page", two))
    assert [kit.call("write_page", body=good, declined=[])["ok"] for _ in range(3)] == [
        False,
        False,
        True,
    ]
    assert kit.session.candidates["concepts/growth-yield"]["declined"] == [
        {"claim": "C2", "reason": NOT_PLACED}
    ]
    linked = good.replace("glucose", "[[concepts/glucose]]")
    assert any("wikilinks" in p for p in page_candidate(Store(root), task, linked, [])[1])
    # A table row and a bullet that opens with a link state results like any sentence.
    for dressed in ("| Strain A | 0.47 g/g [C1] |", "- [[concepts/x]] reached 0.47 g/g [C1]"):
        body = good.replace("\n\n## Open", f"\n\n{dressed}\n\n## Open")
        faults = page_candidate(Store(root), task | {"links": ["concepts/x"]}, body, [])[1]
        assert any("figures not found" in p for p in faults), dressed
    # A tag in a heading or in the section that proposes work supports no statement.
    moved = "Strain A grew.\n\n## Open Directions\n\n- Test acetate [C1]."
    assert any("neither cited" in p for p in page_candidate(Store(root), task, moved, [])[1])
    # Text right under a heading, with no blank line, is read like any other.
    under = good.replace(
        "\n\n## Open", "\n\n## Results\n### By strain\nIt was 0.47 g/g [C1].\n\n## Open"
    )
    assert any("figures not found" in p for p in page_candidate(Store(root), task, under, [])[1])
    # A fence left open would turn the sections after it into code no check reads.
    fenced = good.replace("\n\n## Open", "\n\n```\nraw\n\n## Open")
    assert any("code fence" in p for p in page_candidate(Store(root), task, fenced, [])[1])
    # Two headings that come to one anchor would share a record, and so would "Lead".
    for extra in ("## Results\n\nA [C1].\n\n## Results?\n\nB [C1].", "## Lead\n\nA [C1]."):
        faults = page_candidate(
            Store(root), task, good.replace("## Open", f"{extra}\n\n## Open"), []
        )[1]
        assert any("repeated" in p or "headed Lead" in p for p in faults), (extra, faults)
    # A blank draft is refused like any other and uses up an attempt.
    blank = Tools(root, Session.start("page", task))
    assert not blank.call("write_page", body="  ", declined=[])["ok"]
    assert blank.session.rejections["concepts/growth-yield"] == 1


def test_strike_removes_the_faulted_statement_with_its_tag_and_nothing_else():
    body = (
        "Lead sentence [C1].\n\n## Results\nYield rose. [C2] Faulted statement here [C3]. "
        "Kept sentence [C4].\n\n- First item [C5].\n- Faulted item [C6].\n\n## Empty\n\n"
        "Only faulted [C7].\n\n## Open Directions\n\n- Next."
    )
    struck = compiler.strike(body, ["Faulted statement", "Faulted item", "Only faulted"])
    assert struck is not None
    assert "[C3]" not in struck and "[C6]" not in struck and "## Empty" not in struck
    # The tag that closes the sentence before stays with that sentence.
    assert "Yield rose. [C2] Kept sentence [C4]." in struck and "- First item [C5]." in struck
    # A passage that runs across two statements takes both; one in a heading cannot go.
    assert "[C4]" not in (compiler.strike(body, ["here [C3]. Kept"]) or "")
    assert compiler.strike(body, ["Results"]) is None and compiler.strike(body, ["absent"]) is None
