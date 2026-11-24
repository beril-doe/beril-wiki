"""Check author records and run the deterministic finishers on a scratch wiki."""

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

from beril_wiki.agentic.runtime import WorkflowError
from beril_wiki.kb import finishers
from beril_wiki.kb.jobs import Scope, authors
from beril_wiki.kb.tools import Rejected
from test_kb import ALPHA, BETA, YIELD_QUOTE

ALPHA_LINK = "[[summaries/alpha__REPORT|alpha]]"
BETA_LINK = "[[summaries/beta__REPORT|beta]]"
CONTRIBUTION = (
    f"## Contributions\n\nAlpha measured growth on glucose. {YIELD_QUOTE} [src: alpha].\n\n"
    "Beta assessed growth on acetate [src: beta]."
)


def put(root: Path, name: str, text: str) -> None:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


@pytest.fixture
def author_root(tmp_path: Path) -> Path:
    for source, report in (("alpha", ALPHA), ("beta", BETA)):
        put(tmp_path, f"wiki/sources/{source}__REPORT.md", report)
        put(tmp_path, f"wiki/summaries/{source}__REPORT.md", report)
    put(
        tmp_path,
        "wiki/authors/alex-example.md",
        "# Alex Example\n\nORCID: 0000-0000-0000-0001\n\n"
        "## Profile\n\nBeta assessed growth on acetate [src: beta].\n\n"
        f"## Projects (2)\n\n- {ALPHA_LINK}\n- {BETA_LINK}\n",
    )
    put(
        tmp_path,
        "wiki/authors/blair-example.md",
        f"# Blair Example\n\n## Contributions\n\nAn old link: {ALPHA_LINK}.\n\n"
        "## Projects (1)\n\n- beta\n",
    )
    put(
        tmp_path,
        "state/authors.json",
        json.dumps({"alex-example.md": "legacy", "blair-example.md": "unrelated"}),
    )
    return tmp_path


def test_new_report_owes_only_its_authors_and_publishes_the_legacy_layout(author_root: Path):
    scope = Scope(author_root, "alpha", "ingest", run="first")
    blair = author_root / "wiki/authors/blair-example.md"
    untouched = blair.read_bytes()
    assert authors.jobs(Scope(author_root / "no-stubs", "alpha", "ingest")) == []
    (job,) = authors.jobs(scope)
    assert (job.key, job.writer, job.reviewer) == ("authors/alex-example", "write", "review")
    assert job.pack["AUTHOR"] == "Alex Example"
    assert ALPHA in job.pack["SUMMARIES"] and BETA in job.pack["SUMMARIES"]
    job.publish(job.check({"section": CONTRIBUTION}))
    alex = author_root / "wiki/authors/alex-example.md"
    assert alex.read_text(encoding="utf-8") == (
        f"# Alex Example\n\nORCID: 0000-0000-0000-0001\n\n{CONTRIBUTION}\n\n"
        f"## Projects (2)\n\n- {ALPHA_LINK}\n- {BETA_LINK}\n"
    )
    assert blair.read_bytes() == untouched
    assert json.loads((author_root / "state/authors.json").read_text(encoding="utf-8")) == {
        "alex-example.md": "kb:first",
        "blair-example.md": "unrelated",
    }
    assert authors.jobs(Scope(author_root, "alpha", "ingest", run="second")) == []
    assert [j.key for j in authors.jobs(Scope(author_root, "beta", "ingest"))] == [
        "authors/blair-example"
    ]
    assert authors.jobs(Scope(author_root, "alpha", "revise")) == []
    assert [
        j.key for j in authors.jobs(Scope(author_root, "alpha", "revise", withdrawn=["alpha:1"]))
    ] == ["authors/alex-example"]


@pytest.mark.parametrize(
    ("body", "objection"),
    [
        ("Alex Example focuses on growth [src: alpha].", "characterises the person"),
        ("Alpha measured growth [src: unknown].", "not a project id"),
        ("Alpha measured 0.97 g/g [src: alpha].", "does not appear in the input"),
        ("Alpha measured 0.38 g/g [src: alpha].", "none of the cited sources"),
        ("Alpha measured growth [src: alpha].\n\n## Projects\n\nOther", "submit one section"),
    ],
    ids=["subjective", "citation", "unseen-figure", "figure-from-wrong-report", "extra-section"],
)
def test_author_job_refuses_violations_of_the_legacy_gate(
    author_root: Path, body: str, objection: str
):
    (job,) = authors.jobs(Scope(author_root, "alpha", "ingest"))
    with pytest.raises(Rejected) as stopped:
        job.check({"section": f"## Contributions\n{body}"})
    assert objection in " ".join(stopped.value.objections)


@pytest.fixture
def checkout(tmp_path: Path) -> Path:
    put(tmp_path, "reference/ui/config/collections.yaml", "collections: []\n")
    put(tmp_path, "reference/projects/alpha/README.md", "## Authors\n\n- Alex Example\n")
    put(tmp_path, "reference/projects/alpha/REPORT.md", ALPHA)
    put(tmp_path, "staging/alpha__REPORT.md", ALPHA)
    put(
        tmp_path,
        "wiki/summaries/alpha__REPORT.md",
        "Alpha measured growth in BERDL [src: alpha].\n",
    )
    put(
        tmp_path,
        "contract/errata.yaml",
        "- source: alpha\n  contains: [measured growth]\n  note: The study used glucose.\n",
    )
    return tmp_path


def test_finish_creates_stubs_before_title_naming_and_errata_and_reports_changes(
    checkout: Path, monkeypatch: pytest.MonkeyPatch
):
    for key in ("OPENAI_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CBORG_API_KEY", "BERIL_AGENTIC_CONFIG"):
        monkeypatch.setenv(key, "test-placeholder")
    run = subprocess.run
    called: list[str] = []

    def launch(command: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
        env = kwargs["env"]
        assert (
            not {"OPENAI_API_KEY", "ANTHROPIC_AUTH_TOKEN", "CBORG_API_KEY", "BERIL_AGENTIC_CONFIG"}
            & env.keys()
        )
        assert env["BERIL_WIKI_ROOT"] == str(checkout)
        assert env["BERIL_CHECKOUT"] == str(checkout / "reference")
        assert kwargs["cwd"] == checkout
        assert command[:2] == [sys.executable, "-m"]
        stage = command[2].rsplit(".", 1)[-1]
        assert command[3:] == ([] if stage == "extras" else [str(checkout)])
        called.append(stage)
        return run(command, **kwargs)

    monkeypatch.setattr(finishers.subprocess, "run", launch)
    expected_order = ["extras", "titles", "names", "errata"]
    assert finishers.finish(checkout) == dict.fromkeys(expected_order, True)
    assert called == expected_order
    stub = checkout / "wiki/authors/alex-example.md"
    assert (
        stub.read_text(encoding="utf-8") == f"# Alex Example\n\n## Projects (1)\n\n- {ALPHA_LINK}\n"
    )
    assert [j.key for j in authors.jobs(Scope(checkout, "alpha", "ingest"))] == [
        "authors/alex-example"
    ]
    summary = (checkout / "wiki/summaries/alpha__REPORT.md").read_text(encoding="utf-8")
    assert summary.startswith("# Alpha Growth Study\n\n")
    assert "in the KBase Data Lakehouse" in summary
    assert "> **Erratum.** The study used glucose. [src: alpha]" in summary
    assert finishers.finish(checkout) == dict.fromkeys(expected_order, False)


def test_finish_propagates_the_failed_stage_and_its_tail(checkout: Path):
    (checkout / "reference").rename(checkout / "corpus")
    put(checkout, "contract/errata.yaml", "bad: data\n")
    with pytest.raises(WorkflowError, match=r"(?s)stage errata failed \(exit 1\).*expected a list"):
        finishers.finish(checkout)
