"""The guide and Ask pages the publish step writes alongside the corpus."""

from beril_wiki.publish.ingest import PROVENANCE, READER_KINDS, write_reader_pages


def test_guide_counts_published_pages_per_kind(tmp_path):
    (tmp_path / "concepts").mkdir()
    for name in ("a", "b", "index"):
        (tmp_path / "concepts" / f"{name}.md").write_text("x")
    assert write_reader_pages(tmp_path) == 2
    guide = (tmp_path / "guide.md").read_text()
    assert "| [Concept](concepts/) | 2 |" in guide
    # Every kind gets a row, even one with nothing published yet.
    assert all(f"| [{label}]({folder}/) |" in guide for label, folder, *_ in READER_KINDS)


def test_ask_page_says_what_it_needs(tmp_path):
    write_reader_pages(tmp_path)
    ask = (tmp_path / "ask.md").read_text()
    assert ask.startswith('---\ntitle: "Ask the wiki"\n---')
    assert "JavaScript" in ask and "CBORG key" in ask


def test_both_pages_carry_the_provenance_callout(tmp_path):
    # .github/workflows/pages.yml refuses to publish a page without it.
    write_reader_pages(tmp_path)
    for name in ("guide.md", "ask.md"):
        assert PROVENANCE.split(".")[0] in (tmp_path / name).read_text()
