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
    from card_fakes import lakehouse

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
            "databases": ["kescience.fitnessbrowser"],
            "tables": ["kescience.fitnessbrowser.experiment"],
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
    lakehouse(kb)
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


def publish(kb, dst, monkeypatch):
    import sys

    from beril_wiki.publish import ingest

    monkeypatch.setattr(sys, "argv", ["ingest", str(kb), str(dst)])
    ingest.main()


ABOUT = (
    "# About This Wiki\n\n- *Analyze existing data*: matched in the catalog of "
    "<!-- lakehouse-date -->.\n- *Add outside data*: not found in the "
    "[<!-- lakehouse-tenants --> tenants the catalog covers](#lakehouse-coverage).\n\n"
    "<!-- lakehouse-coverage -->\n\n## License\n\nText.\n"
)


def test_ingest_merges_label_and_topics(tmp_path, monkeypatch):
    import json

    kb = tmp_path / "kb"
    card_corpus(kb)
    manifest_bytes = b'{"projects": {}, "shared": {}, "version": 1}\n'
    (kb / "corpus").mkdir()
    (kb / "corpus/manifest.json").write_bytes(manifest_bytes)
    (kb / "wiki/about.md").write_text(ABOUT)
    (kb / "wiki/data").mkdir()
    (kb / "wiki/data/phagefoundry.md").write_text("# PhageFoundry Browsers\n\nCurated.\n")
    catalog = kb / "state/lakehouse/catalog.jsonl"
    rows = [json.loads(line) for line in catalog.read_text().splitlines()]
    for row in rows:
        if (row["database"], row["table"]) == ("kescience.bacdive", "strain"):
            row["description"] = "See [[x]] and <script>a</script> | pipe"
            row["columns"].append(["before\n\n<img src=x onerror=alert(2)>\n\nafter", "string"])
    catalog.write_text("".join(json.dumps(r) + "\n" for r in rows))
    # A database the direction names without a table still gets a page.
    page = kb / "wiki/directions/transport--abc123.md"
    text = page.read_text()
    page.write_text(
        text.replace(
            'databases: ["kescience.fitnessbrowser"]',
            'databases: ["kescience.fitnessbrowser", "kbase.ke_pangenome"]',
        )
    )
    assert "kbase.ke_pangenome" in page.read_text()
    tables = [
        "kescience.bacdive.strain",
        "phagefoundry.acinetobacter_genome_browser.browser_gene",
    ]
    (kb / "state/followups.json").write_text(
        json.dumps(
            {
                "transport--abc123": {
                    "need": "existing",
                    "first_step_existing": False,
                    "data_unclear": False,
                    "reason": "The strain table can decide it.",
                    "tables": tables,
                }
            }
        )
    )
    publish(kb, tmp_path / "out", monkeypatch)
    finding = (tmp_path / "out/findings/a--1a2b3c4d.md").read_text()
    assert 'label: "Candidate novel"' in finding and 'topics: ["dark-matter"]' in finding
    assert "## Compared with published work" in finding and "retrieved on 2026-10-23" in finding
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
    assert (tmp_path / "out/corpus-manifest.json").read_bytes() == manifest_bytes
    assert export["research_directions"][0]["readiness"] == "needs compute"
    assert export["data_issues"] == {"a": ["Recompute the stress rates per experiment. [src: a]"]}
    # The cited database without a curated page gets one, and the catalog's free text on
    # it renders as text (Review Focus 3).
    page = (tmp_path / "out/data/kescience-bacdive.md").read_text()
    assert PROVENANCE.split(".")[0] in page and "11 November 2026" in page
    assert "`strain`" in page and "97,334 rows" in page
    assert r"See \[\[x\]\] and \<script\>a\</script\> \| pipe" in page
    assert "<script>" not in page and "[[x]]" not in page
    # A column name with blank lines and HTML stays one line of escaped text.
    assert r"strain\_id, before \<img src=x onerror=alert(2)\> after" in page
    assert page.count("<img") == page.count(r"\<img") == 1 and "<img" not in direction
    # The source reads in reader words, not as a pipeline id.
    assert "(hub catalog export)" in page and "packet-2026-11-11" not in page
    assert (tmp_path / "out/data/kbase-ke-pangenome.md").is_file()
    assert "kbase.ke_pangenome" in export["research_directions"][0]["databases"]
    # The question page keeps both database links, the atlas table's unknown row count
    # (Review Focus 5), the hedge and the coverage link.
    assert "[[data/kescience-bacdive|kescience.bacdive]] · `strain` · 97,334 rows" in direction
    assert "[[data/phagefoundry|PhageFoundry Browsers]] · `browser_gene` · " in direction
    assert "row count unknown · schema only, May 2026" in direction
    assert "An AI model matched this question to these tables" in direction
    assert "[[about#lakehouse-coverage|" in direction
    assert 'follow: "existing"' in direction
    # A curated route keeps its own page; no generated page replaces it.
    assert "Curated." in (tmp_path / "out/data/phagefoundry.md").read_text()
    about = (tmp_path / "out/about.md").read_text()
    assert "## Lakehouse coverage" in about
    assert "- KBase: hub catalog export, 2026-11-11" in about and "- KE Science:" in about
    assert "other tenants this catalog does not cover" in about
    assert "[2 tenants the catalog covers](#lakehouse-coverage)" in about
    assert "<!-- lakehouse-" not in about and "BERDL" not in about
    assert export["research_directions"][0]["tables"] == [
        "kescience.fitnessbrowser.experiment",
        *tables,
    ]
    from beril_wiki.publish.cards.corpus import split

    index, _ = split((tmp_path / "out/directions/index.md").read_text())
    assert index["follow_order"][-1] == "unchecked"
    assert "11 November 2026" in index["follow_notes"]["existing"]


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


def test_digests_publish_as_titled_archives(tmp_path, monkeypatch):
    card_corpus(tmp_path / "kb")
    (tmp_path / "kb/wiki/summaries/pitfalls.md").write_text(
        '---\ntype: "Summary"\ndescription: "Gotchas."\n---\n# Common Pitfalls\n\nText.\n'
    )
    publish(tmp_path / "kb", tmp_path / "out", monkeypatch)
    page = (tmp_path / "out/summaries/pitfalls.md").read_text()
    assert 'type: "Archive"' in page and 'title: "Earlier pitfalls"' in page
    assert "Common Pitfalls" not in page
    # The wiki file keeps its own title and type; only the published copy changes.
    assert "# Common Pitfalls" in (tmp_path / "kb/wiki/summaries/pitfalls.md").read_text()


def test_all_pages_lists_every_published_page_by_kind(tmp_path):
    from beril_wiki.publish.ingest import write_all_pages

    def page(rel, title, extra=""):
        path = tmp_path / f"{rel}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\n{extra}title: {title}\n---\nBody [[concepts/b]].\n")

    page("topics/t", '"Topic T"')
    page("topics/index", '"Topics"')
    page("concepts/b", '"Beta"')
    page("concepts/a", '"alpha"')
    page("entities/nife", '"[NiFe]-hydrogenase"')
    page("summaries/r", '"Report R"', 'type: "Project report"\n')
    page("summaries/pitfalls", '"Earlier pitfalls"', 'type: "Archive"\n')
    page("sources/r", '"Raw R"')
    page("sources/index", '"Raw reports"')
    page("guide", '"How to read this wiki"')
    assert write_all_pages(tmp_path, "> [!info] Provenance\n> x") == 1
    text = (tmp_path / "catalog.md").read_text()
    assert text.startswith('---\ntitle: "All pages"\ntype: "Index"\n---')
    assert "Every page on the site, by kind." in text
    heads = [line[3:] for line in text.splitlines() if line.startswith("## ")]
    assert heads == [
        "Topics",
        "Concepts",
        "Entities",
        "Project reports",
        "Raw reports",
        "Archives and site pages",
    ]
    raw = text.split("## Raw reports")[1].split("## ")[0]
    assert "[[sources/r|Raw R]]" in raw and "sources/index" not in raw
    assert "[Topics](#topics) · [Concepts](#concepts)" in text
    # Titles sort without regard to case; index pages and archives stay out of their kinds.
    assert text.index("[[concepts/a|alpha]]") < text.index("[[concepts/b|Beta]]")
    assert "[[topics/index" not in text and "2 pages." in text and "1 page." in text
    assert "[\\[NiFe\\]-hydrogenase](entities/nife)" in text
    reports = text.split("## Project reports")[1].split("## ")[0]
    assert "summaries/r" in reports and "pitfalls" not in reports
    site = text.split("## Archives and site pages")[1]
    assert "[[summaries/pitfalls|Earlier pitfalls]]" in site and "[[guide|" in site
    assert "[[sources/index|Raw reports]]" in site
    # Titles only: no description, so no source tag can reach the page.
    assert "Body" not in text and "[src:" not in text


def test_guide_counts_only_project_reports(tmp_path):
    """The two archives share summaries/ but are not project reports."""
    (tmp_path / "summaries").mkdir()
    (tmp_path / "summaries/r.md").write_text('---\ntype: "Project report"\n---\nx')
    (tmp_path / "summaries/pitfalls.md").write_text('---\ntype: "Archive"\n---\nx')
    write_reader_pages(tmp_path)
    assert "| [Project report](summaries/) | 1 |" in (tmp_path / "guide.md").read_text()
