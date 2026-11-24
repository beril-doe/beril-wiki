"""Topic membership and literature records in a temporary wiki, with no live calls."""

import json
from dataclasses import replace
from pathlib import Path

import pytest

from beril_wiki.agentic.runtime import manifest
from beril_wiki.kb.jobs import Scope, literature, run_all, run_jobs, topics
from beril_wiki.kb.tools import Rejected
from beril_wiki.kb.workflow import Runner
from beril_wiki.records import topic_groups
from test_kb import Script, config
from test_kb import root as root

HUB = (
    "# Growth Research\n\nGrowth studies in bacterial cultures.\n\n"
    "## Where to Go Deeper\n\n- [[concepts/growth-yield]]\n"
)
QUERIES = ["bacterial growth research", "growth yield in acetate cultures"]
SECTION = (
    "## Literature Context\n\n"
    + "The authors found growth varied across tested conditions and strains in laboratory culture. "
    * 12
    + "[PMID 12345](https://pubmed.ncbi.nlm.nih.gov/12345/)\n\n"
    + "This corpus extends these observations by comparing growth across different substrates. "
    * 13
).rstrip()


@pytest.fixture
def hub(root: Path) -> Path:
    """Make a hub and an unrelated incumbent group in the reader's layout."""
    page = root / "wiki/topics/growth-research.md"
    page.parent.mkdir()
    page.write_text(HUB, encoding="utf-8")
    (page.parent / "sampling.md").write_text(
        '---\ndescription: "Study design."\n---\n# Sampling\n\nSampling lead.\n',
        encoding="utf-8",
    )
    state = root / topics.STATE
    state.parent.mkdir(exist_ok=True)
    state.write_text(
        json.dumps(
            {
                "version": 1,
                "reason": "Keep established topics.",
                "concepts": manifest(root, ("wiki/concepts",)),
                "groups": [
                    {"title": "Growth Research", "concepts": ["growth-yield"]},
                    {"title": "Sampling", "concepts": ["sampling"]},
                ],
            }
        ),
        encoding="utf-8",
    )
    return page


def test_topics_only_adds_created_members_and_refreshes_counts_without_a_job(
    root: Path, hub: Path
) -> None:
    home = root / "wiki/index.md"
    home.write_text("# Home\n\n## Corpus\n\nOld count.\n\n## Other\n\nKeep.\n", encoding="utf-8")
    scope = Scope(root, "alpha", "ingest", "test", created=["concepts/growth-yield"])
    assert topics.jobs(scope) == []
    (root / "wiki/summaries/alpha__REPORT.md").write_text("# Alpha\n", encoding="utf-8")
    topics.after(scope, {})
    assert "2 project reports + 0 cross-project digests, 1 concepts" in home.read_text()
    assert "## Other\n\nKeep." in home.read_text()

    (root / "wiki/concepts/growth.md").write_text(
        '---\ndescription: "Variation in culture."\n---\n# Growth\n\nThe concept lead.\n',
        encoding="utf-8",
    )
    scope.created.append("concepts/growth")
    (job,) = topics.jobs(scope)
    assert (job.writer, job.reviewer) == ("curate", "")
    assert job.pack == {
        "CONCEPT": {
            "title": "Growth",
            "description": "Variation in culture.",
            "lead": "The concept lead.",
        },
        "TOPICS": {
            "growth-research": {
                "title": "Growth Research",
                "description": "Growth studies in bacterial cultures.",
            },
            "sampling": {"title": "Sampling", "description": "Study design."},
        },
    }
    for wrong in (
        {"topic": "new-topic", "reason": "It fits."},
        {"topic": "growth-research", "reason": "It fits. It measures growth."},
    ):
        with pytest.raises(Rejected):
            job.check(wrong)
    job.publish(job.check({"topic": "", "reason": "No topic fits."}))
    assert "growth" not in topic_groups(root)["growth-research"]
    job.publish(job.check({"topic": "growth-research", "reason": "It describes growth."}))

    assert topic_groups(root) == {
        "growth-research": {"growth", "growth-yield"},
        "sampling": {"sampling"},
    }
    saved = json.loads((root / topics.STATE).read_text(encoding="utf-8"))
    assert saved["concepts"] == manifest(root, ("wiki/concepts",))
    assert saved["version"] == 1 and saved["reason"] == "Keep established topics."
    assert hub.read_text() == HUB + "- [[concepts/growth]] — Variation in culture.\n\n"
    assert topics.jobs(scope) == []


class LiteratureScript(Script):
    """Submit known query and section records through the ordinary job tools."""

    @staticmethod
    def record(key: str, pack: dict) -> dict:
        if key.endswith("/queries"):
            return {"queries": QUERIES}
        assert set(pack["CANDIDATE PAPERS"]) == {"12345"}
        return {"section": SECTION}


def test_literature_resumes_queries_rejects_bad_evidence_and_splices_once(
    root: Path, hub: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    script = LiteratureScript()
    runner = Runner(root, config(), "ingest", "alpha", launch=script)
    scope = Scope(root, "alpha", "ingest", runner.id)
    assert literature.query_jobs(scope) == literature.section_jobs(scope) == []
    scope.edited = ["topics/growth-research#lead", "topics/growth-research#where-to-go-deeper"]
    calls = []

    def fetch(queries: list[str]) -> dict[str, str]:
        calls.append(queries)
        return {} if queries == QUERIES else {"12345": "Growth varies with culture conditions."}

    monkeypatch.setattr(literature, "fetch_candidates", fetch)
    query_phase, section_phase = literature.PHASES
    (query,) = query_phase(scope)
    assert (query.writer, query.reviewer) == ("queries", "")
    with pytest.raises(Rejected):
        query.check({"queries": ["growth[Title]", "culture"]})
    assert section_phase(scope) == [] and calls == []
    run_jobs(runner, [query])

    runner = Runner(root, config(), "ingest", "alpha", launch=script)
    assert runner.id == scope.run
    resumed = replace(scope, notes={})
    assert query_phase(resumed) == []
    (section,) = section_phase(resumed)
    assert (section.writer, section.reviewer) == ("write", "review")
    with pytest.raises(Rejected) as bad_pmid:
        section.check({"section": SECTION.replace("12345", "99999")})
    assert "PMID 99999 is not a candidate" in " ".join(bad_pmid.value.objections)
    with pytest.raises(Rejected) as too_short:
        section.check({"section": "## Literature Context\n\nA short section."})
    assert "write 300-500 words" in " ".join(too_short.value.objections)
    assert section.check({"section": "NONE"}) == {"section": "NONE"}

    state = root / literature.STATE
    state.write_text('{"old-topic.md": "old-value"}', encoding="utf-8")
    assert run_all(runner, resumed, stages=("literature",)) == {"literature": {"accepted": 1}}
    assert calls == [QUERIES, ["Growth Research bacteria", "Growth Research"]]
    assert script.roles == ["card", "card", "card_review"]
    assert hub.read_text() == HUB.replace("\n## Where", f"\n{SECTION}\n\n## Where")
    assert json.loads(state.read_text()) == {
        "growth-research.md": f"kb:{runner.id}",
        "old-topic.md": "old-value",
    }
    later = replace(resumed, run="later-run", reason="revise", notes={})
    assert query_phase(later) == section_phase(later) == []
