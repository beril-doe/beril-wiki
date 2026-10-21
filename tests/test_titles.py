"""stages.titles and the check that backs it (no LLM calls, no network)."""

from __future__ import annotations

import json

from beril_wiki.check import has_title
from beril_wiki.stages.titles import apply, planned_titles, with_title

FM = '---\ntype: "Compound"\ndescription: "A sugar."\n---\n'


def test_has_title_reads_the_body_only():
    assert has_title(FM + "# Rhamnose\n\nA sugar.")
    assert not has_title(FM + "Rhamnose is a sugar.\n\n## Uses\n\nGrowth.")
    assert not has_title("---\ntitle: x\n# not a heading\n---\nBody.")


def test_with_title_keeps_frontmatter_first():
    assert (
        with_title(FM + "\nRhamnose is a sugar.", "Rhamnose")
        == FM + "# Rhamnose\n\nRhamnose is a sugar."
    )
    assert with_title("Body.", "T") == "# T\n\nBody."


def test_planned_titles_drop_slug_titles(tmp_path):
    plan = {
        "pages": [
            {"path": "entities/cohens-d.md", "title": "Cohen's d"},
            {"path": "entities/acds.md", "title": "acds"},
            {"path": "entities/blank.md", "title": " "},
        ]
    }
    (tmp_path / "last-plan.json").write_text(json.dumps(plan))
    assert planned_titles(tmp_path) == {"entities/cohens-d.md": "Cohen's d"}
    assert planned_titles(tmp_path / "missing") == {}


def test_apply_titles_untitled_pages_once(tmp_path):
    entities = tmp_path / "wiki/entities"
    entities.mkdir(parents=True)
    (entities / "cohens-d.md").write_text(FM + "Cohen's d is an effect size.")
    (entities / "nitrate.md").write_text(FM + "# Nitrate\n\nAn anion.")
    (entities / "orphan.md").write_text(FM + "No plan names this page.")
    titles = {"entities/cohens-d.md": "Cohen's d", "entities/nitrate.md": "Other"}
    assert apply(tmp_path, titles) == (["entities/cohens-d.md"], ["entities/orphan.md"])
    assert (
        entities / "cohens-d.md"
    ).read_text() == FM + "# Cohen's d\n\nCohen's d is an effect size."
    assert (entities / "nitrate.md").read_text() == FM + "# Nitrate\n\nAn anion."
    assert apply(tmp_path, titles) == ([], ["entities/orphan.md"])


def test_a_comment_in_a_code_block_is_not_a_title():
    assert not has_title(FM + "Run it:\n\n```bash\n# run the analysis\necho done\n```\n")
    assert has_title(FM + "# Rhamnose\n\n```bash\n# run\n```\n")


def test_a_summary_without_a_plan_title_takes_its_reports_title(tmp_path):
    (tmp_path / "wiki/summaries").mkdir(parents=True)
    (tmp_path / "staging").mkdir()
    (tmp_path / "staging/proj__REPORT.md").write_text("# Report: Metal Fitness Atlas\n\nBody.")
    (tmp_path / "wiki/summaries/proj__REPORT.md").write_text(FM + "A summary.")
    assert apply(tmp_path, {}) == (["summaries/proj__REPORT.md"], [])
    assert "# Metal Fitness Atlas\n" in (tmp_path / "wiki/summaries/proj__REPORT.md").read_text()


def test_a_title_with_extra_spaces_counts_and_is_not_doubled(tmp_path):
    # Publish promotes "#  Title" too, so the gate and the backfill must accept it.
    assert has_title(FM + "#  Rhamnose\n\nA sugar.")
    (tmp_path / "wiki/entities").mkdir(parents=True)
    page = tmp_path / "wiki/entities/rhamnose.md"
    page.write_text(FM + "#  Rhamnose\n\nA sugar.")
    assert apply(tmp_path, {"entities/rhamnose.md": "Rhamnose"}) == ([], [])
    assert page.read_text().count("# ") == 1
