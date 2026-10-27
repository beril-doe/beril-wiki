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


def card_corpus(kb):
    import json

    from beril_wiki.stages import cards

    wiki = kb / "wiki"
    (wiki / "concepts").mkdir(parents=True)
    (wiki / "concepts/gap.md").write_text(
        "# Gap\n\nDark genes. [src: a]\n\n## Open Directions\n\n"
        "- Recompute the stress rates per experiment. [src: a]\n"
        "- Test whether dark genes encode transporters. [src: a]\n"
    )
    (kb / "contract").mkdir(parents=True)
    (kb / "contract/cards.yaml").write_text("topics: [dark-matter]\nreports: [a]\n")
    (wiki / "conflicts").mkdir()
    (wiki / "conflicts/conflict--gap--1234abcd.md").write_text("# Tension\n\nSide [src: a, b]\n")
    (wiki / "summaries").mkdir()
    (wiki / "summaries/a__REPORT.md").write_text("# Report A\n\nText.\n")
    (wiki / "index.md").write_text("# Home\n\nWelcome.\n")
    cards.write_page(
        wiki / "findings/a--1a2b3c4d.md",
        {
            "type": "Finding",
            "description": "Dark genes were depleted.",
            "source": "a",
            "result": "observation",
        },
        "# Dark genes are depleted\n\nDark genes were depleted. [src: a]\n\n"
        "## Evidence\n\n> Quote. [src: a]\n",
    )
    cards.write_page(
        wiki / "directions/transport--abc123.md",
        {
            "type": "Research direction",
            "description": "Do dark genes move nutrients?",
            "hypothesis": "They encode transporters.",
            "approach": "lakehouse analysis",
            "readiness": "needs compute",
            "readiness_basis": "Data exists.",
            "collections": ["kbase-ke-pangenome"],
            "findings": ["a--1a2b3c4d"],
            "conflicts": ["conflict--gap--1234abcd"],
            "builds_on": ["findings/a--1a2b3c4d", "conflicts/conflict--gap--1234abcd"],
            "topics": ["dark-matter"],
        },
        "# Dark genes as nutrient transporters\n\nDo dark genes move nutrients?\n\n"
        "## Hypothesis\n\nThey encode transporters.\n\n## How to test it\n\nCofitness.\n\n"
        "## What would support or refute it\n\nCofitness with transporters.\n",
    )
    (kb / "state").mkdir()
    (kb / "state/curator-topics.json").write_text(
        json.dumps({"groups": [{"title": "Dark Matter", "concepts": ["gap"]}]})
    )
    (kb / "state/novelty.json").write_text(
        json.dumps(
            {
                "a--1a2b3c4d": {
                    "label": "Candidate novel",
                    "retrieved_on": "2026-10-23",
                    "queries": ["dark genes"],
                    "retrieved": 12,
                    "closest": [{"pmid": "111", "title": "Paper", "relation": "related"}],
                    "difference": "Adds archaea.",
                    "agreed": True,
                    "agree_model": "gpt-6.1-sol",
                }
            }
        )
    )


def publish(kb, dst, monkeypatch, preview):
    import sys

    from beril_wiki.publish import ingest

    if preview:
        monkeypatch.setenv("WIKI_PREVIEW", "1")
    else:
        monkeypatch.delenv("WIKI_PREVIEW", raising=False)
    monkeypatch.setattr(sys, "argv", ["ingest", str(kb), str(dst)])
    ingest.main()


def test_ingest_hides_records_without_preview(tmp_path, monkeypatch):
    card_corpus(tmp_path / "kb")
    publish(tmp_path / "kb", tmp_path / "out", monkeypatch, preview=False)
    assert not (tmp_path / "out/findings").exists()
    assert not (tmp_path / "out/directions").exists()
    assert not (tmp_path / "out/data-issues").exists()
    assert not (tmp_path / "out/cards.json").exists()
    assert (tmp_path / "out/concepts/gap.md").exists()


def test_ingest_preview_merges_label_and_topics(tmp_path, monkeypatch):
    import json

    card_corpus(tmp_path / "kb")
    publish(tmp_path / "kb", tmp_path / "out", monkeypatch, preview=True)
    finding = (tmp_path / "out/findings/a--1a2b3c4d.md").read_text()
    assert 'label: "Candidate novel"' in finding and 'topics: ["dark-matter"]' in finding
    assert "## Literature check" in finding and "retrieved from PubMed on 2026-10-23" in finding
    assert "[PMID 111](https://pubmed.ncbi.nlm.nih.gov/111/)" in finding
    assert "Confirmed independently by gpt-6.1-sol" in finding
    assert "[[conflicts/conflict--gap--1234abcd|Tension]]" in finding
    assert "[[directions/transport--abc123|Dark genes as nutrient transporters]]" in finding
    assert PROVENANCE.split(".")[0] in finding
    direction = (tmp_path / "out/directions/transport--abc123.md").read_text()
    assert "beril_prompt:" in direction and "brief:" in direction
    assert "Hypothesis: They encode transporters." in direction
    assert (tmp_path / "out/directions/index.md").exists()
    issues = (tmp_path / "out/data-issues/a.md").read_text()
    assert "Recompute the stress rates" in issues and "transporters" not in issues
    assert "[[concepts/gap|Gap]] (Open Directions)" in issues
    summary = (tmp_path / "out/summaries/a.md").read_text()
    assert "[[data-issues/a|1 proposal(s) for the report's maintainers]]" in summary
    export = json.loads((tmp_path / "out/cards.json").read_text())
    assert export["findings"][0]["label"] == "Candidate novel"
    assert export["research_directions"][0]["readiness"] == "needs compute"
    assert export["data_issues"] == {"a": ["Recompute the stress rates per experiment. [src: a]"]}


def test_finding_topics_are_the_reports_main_topics(tmp_path):
    import json

    from beril_wiki.publish.cards import Corpus

    wiki = tmp_path / "wiki"
    (wiki / "concepts").mkdir(parents=True)
    for stem in ("a1", "a2", "a3", "b1"):
        (wiki / "concepts" / f"{stem}.md").write_text(f"# {stem}\n\nText. [src: r]\n")
    (tmp_path / "state").mkdir()
    (tmp_path / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Main", "concepts": ["a1", "a2", "a3"]},
                    {"title": "Side", "concepts": ["b1"]},
                ]
            }
        )
    )
    assert Corpus(tmp_path).topics_of("r") == ["main"]
