"""The corpus line on the home page must be counted in code, not transcribed.

It was written by the LLM that generates the home page, and that page is only
regenerated when a topic hub changes — so a concept merge left "93 concepts"
on the front page against 92 real ones.
"""

import pathlib
import tempfile

from beril_wiki.stages import topics as tb


def _corpus(root, n_concepts=3, n_entities=2, n_single=1, n_summaries=4, n_topics=2):
    for d in ("wiki/concepts", "wiki/entities", "wiki/summaries", "wiki/topics"):
        (root / d).mkdir(parents=True, exist_ok=True)
    for i in range(n_concepts):
        (root / "wiki/concepts" / f"c{i}.md").write_text("x")
    # Entities citing one project are hidden at publish and must not be counted.
    for i in range(n_entities):
        (root / "wiki/entities" / f"e{i}.md").write_text(
            '---\nsources: ["summaries/a__REPORT.md", "summaries/b__REPORT.md"]\n---\n'
        )
    for i in range(n_single):
        (root / "wiki/entities" / f"s{i}.md").write_text(
            '---\nsources: ["summaries/a__REPORT.md"]\n---\n'
        )
    for i in range(n_summaries):
        (root / "wiki/summaries" / f"p{i}__REPORT.md").write_text("x")
    (root / "wiki/summaries/discoveries.md").write_text("x")
    for i in range(n_topics):
        (root / "wiki/topics" / f"t{i}.md").write_text("x")


def test_counts_published_entities_only():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        _corpus(root)
        s = tb.corpus_stats(root)
        assert "3 concepts" in s, s
        assert "2 entities" in s, s  # the single-source one is hidden
        assert "4 project reports + 1 cross-project digests" in s, s
        assert "2 topics" in s, s


def test_refresh_rewrites_a_stale_line_and_is_idempotent():
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        _corpus(root)
        idx = root / "index.md"
        idx.write_text(
            "# Home\n\n## Corpus\n\n999 project reports + 0 cross-project digests, "
            "93 concepts, 336 entities, 9 topics\n\n## Browse\n\n- x\n"
        )
        assert tb.refresh_corpus_line(idx, tb.corpus_stats(root)) is True
        text = idx.read_text()
        assert "3 concepts" in text and "93 concepts" not in text, text
        assert "## Browse" in text, "must not clobber the rest of the page"
        assert tb.refresh_corpus_line(idx, tb.corpus_stats(root)) is False


def test_uncited_figures_flags_only_numeric_paragraphs_without_a_tag():
    page = (
        "# T\n\nAbout 200,000 genes were scored.\n\nYield was 42%. [src: a]\n\nNo numbers here.\n"
        "\n## Where to Go Deeper\n\n- [[concepts/a]] — the 14-metal table.\n"
    )
    flagged = tb.uncited_figures(page)
    assert len(flagged) == 1 and "200,000" in flagged[0]


def test_link_missing_members_appends_unlinked_concepts():
    concepts = {
        "a": {"title": "A", "desc": "What A argues."},
        "b": {"title": "B", "desc": ""},
    }
    page = "# T\n\nBody [[concepts/a]].\n\n## Where to Go Deeper\n\n- [[concepts/a]] — read.\n"
    fixed = tb.link_missing_members(page, ["a", "b"], concepts)
    assert fixed.count("[[concepts/b]]") == 1 and "— B" in fixed
    assert fixed.index("[[concepts/b]]") > fixed.index("## Where to Go Deeper")
    assert tb.link_missing_members(fixed, ["a", "b"], concepts) == fixed
    no_section = "# T\n\nBody.\n"
    assert "## Where to Go Deeper\n\n- [[concepts/a]] — What A argues." in tb.link_missing_members(
        no_section, ["a"], concepts
    )


def test_conflict_lead_is_title_and_lead_only():
    page = (
        "<!-- tension-hash: 9514b16e -->\n# A tension\n\nThe lead paragraph. [src: a]\n\n"
        "## Evidence Sides\n\n**Side.** Yield was 42%. [src: a]\n"
    )
    lead = tb.conflict_lead(page)
    assert lead == "# A tension\nThe lead paragraph. [src: a]"
    assert "Evidence Sides" not in lead and "tension-hash" not in lead
