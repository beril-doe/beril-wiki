"""Reader wording and the publish-time joins for result and question pages."""

import json
import re

from beril_wiki.publish import cards
from beril_wiki.publish.cards import Corpus, finding_page
from test_reader_pages import card_corpus

FID = "a--1a2b3c4d"


def set_state(kb, name, data):
    (kb / "state" / name).write_text(json.dumps(data))


def build(tmp_path, with_extras=True):
    kb = tmp_path / "kb"
    card_corpus(kb)
    page = kb / "wiki/findings" / f"{FID}.md"
    fields, _ = cards.split(page.read_text())
    body = (
        "# P < 0.001 for depleted dark genes\n\nDark genes were depleted. [src: a]\n\n"
        "## Key figures\n\n- **12%**: dark genes [src: a]\n\n"
        "## Evidence\n\n> Quote text. [src: a]\n\nFrom the report [[summaries/a__REPORT]].\n\n"
        "## Caveat\n\nOnly one organism. [src: a]\n\n"
        "## Other caveats in this report\n\n- Small sample. [src: a]\n- Old annotations. [src: a]\n"
    )
    page.write_text(cards.join(fields, body))
    return kb


def headings(text):
    return re.findall(r"^## (.+)$", text, re.M)


def test_finding_page_orders_sections_for_readers(tmp_path):
    kb = build(tmp_path)
    set_state(kb, "gists.json", {FID: {"gist": "Dark genes are rare here.", "case": ""}})
    page = finding_page(FID, Corpus(kb))
    body = cards.split(page)[1]
    assert headings(body) == [
        "What the report measured",
        "Limits",
        "Compared with published work",
        "Open questions that build on this",
        "Related conflicts",
    ]
    lines = body.splitlines()
    assert lines[0].startswith("# ")
    assert body.index("Dark genes are rare here.") < body.index("## What the report measured")
    assert "## Caveat" not in body and "## Literature check" not in body
    assert "Quote text." in body and "Small sample." in body and "Old annotations." in body
    assert body.rstrip().endswith("From the report [[summaries/a__REPORT]].")


def test_plain_title_replaces_a_statistical_title(tmp_path):
    kb = build(tmp_path)
    assert "# P < 0.001 for depleted dark genes" in finding_page(FID, Corpus(kb))
    set_state(
        kb, "gists.json", {FID: {"gist": "g", "title": "Few modules hold up after correction"}}
    )
    page = finding_page(FID, Corpus(kb))
    assert "# Few modules hold up after correction" in page
    assert "P < 0.001" not in cards.split(page)[1]


def test_a_failed_summary_is_not_published(tmp_path):
    """A rewrite that failed keeps its old text in state, but the card shows the title only."""
    kb = build(tmp_path)
    old = {"gist": "Dark genes showed no significant defects.", "case": "", "failed": True}
    set_state(kb, "gists.json", {FID: old})
    c = Corpus(kb)
    assert not cards.eligible(c, FID)
    page = finding_page(FID, c)
    assert "no significant defects" not in page


def test_chip_only_for_informative_pipeline_labels(tmp_path):
    kb = build(tmp_path)
    entry = json.loads((kb / "state/novelty.json").read_text())[FID]

    def fields_for(**change):
        set_state(kb, "novelty.json", {FID: entry | change})
        page = finding_page(FID, Corpus(kb))
        return cards.split(page)

    f, _ = fields_for()
    assert f["chip"] == "No close match in PubMed abstracts"
    assert "2026-10-23" in f["chip_note"]
    for label in ("Insufficient literature evidence", "Not assessed"):
        f, _ = fields_for(label=label)
        assert f["chip"] == "" and f["chip_note"] == ""
    f, body = fields_for(override="checked by hand")
    assert f["chip"] == "" and f["chip_note"] == ""
    assert "A person set this label" in body
    f, body = fields_for(label="Not assessed", override="wrong match")
    assert "A person withdrew the pipeline's label: wrong match" in body


def test_literature_provenance_is_collapsed_not_dropped(tmp_path):
    kb = build(tmp_path)
    body = cards.split(finding_page(FID, Corpus(kb)))[1]
    assert cards.CHIP_NOTE.format(date="2026-10-23") in body
    assert "[PMID 111](https://pubmed.ncbi.nlm.nih.gov/111/)" in body
    details = body.split("<details><summary>How this was checked</summary>")[1].split("</details>")[
        0
    ]
    assert "dark genes" in details and "papers with abstracts were compared" in details
    assert "Confirmed independently by gpt-6.1-sol" in details


def test_direction_page_uses_reader_words(tmp_path):
    kb = tmp_path / "kb"
    card_corpus(kb)
    page = kb / "wiki/directions/transport--abc123.md"
    fields, body = cards.split(page.read_text())
    body += (
        "\n## Data\n\nApproach: lakehouse analysis. Readiness: needs compute. Data exists.\n\n"
        "## Builds on\n\n"
        "- Finding: [[findings/a--1a2b3c4d|Dark]] (Candidate novel)\n"
        "- Finding: [[findings/b--00000000|Other]] (Insufficient literature evidence)\n"
    )
    page.write_text(cards.join(fields, body))
    fields, text = cards.split(cards.direction_page("transport--abc123", Corpus(kb)))
    assert "Approach: Analysis of existing data. Needs: Analysis to build. Data exists." in text
    assert "|Dark]] (No close match in PubMed abstracts)" in text
    assert "|Other]]\n" in text and "(Insufficient" not in text
    assert fields["need"] == "build" and fields["need_text"] == "Analysis to build"
    assert fields["approach_text"] == "Analysis of existing data"
    assert fields["topic"] == "dark-matter"


def make_picks_corpus(tmp_path, specs, broad=True):
    """specs: (fid, project, result, topic concepts) with a gist per entry. With `broad`,
    every project also feeds a last-sorting second topic, as home picks require."""
    kb = tmp_path / "kb"
    (kb / "state").mkdir(parents=True)
    wiki = kb / "wiki"
    (wiki / "findings").mkdir(parents=True)
    (wiki / "concepts").mkdir()
    groups = {}
    gists = {}
    for fid, project, result, topic, case in specs:
        (wiki / "findings" / f"{fid}.md").write_text(
            cards.join({"source": project, "result": result}, f"# {fid}\n\nClaim.\n")
        )
        groups.setdefault(topic, set())
        gists[fid] = {"gist": f"Gist {fid}", "case": case}
    for i, topic in enumerate(groups):
        for project in {s[1] for s in specs if s[3] == topic}:
            stem = f"c{i}-{project}"
            (wiki / "concepts" / f"{stem}.md").write_text(f"# {stem}\n\nText. [src: {project}]\n")
            groups[topic].add(stem)
    if broad:
        groups["zz broad"] = set()
        for project in {s[1] for s in specs}:
            stem = f"broad-{project}"
            (wiki / "concepts" / f"{stem}.md").write_text(f"# {stem}\n\nText. [src: {project}]\n")
            groups["zz broad"].add(stem)
    set_state(
        kb,
        "curator-topics.json",
        {"groups": [{"title": t, "concepts": sorted(c)} for t, c in groups.items()]},
    )
    set_state(kb, "gists.json", gists)
    return kb


def test_home_skips_projects_in_one_topic(tmp_path):
    specs = [
        ("a1", "pa", "observation", "alpha", ""),
        ("b1", "pb", "observation", "beta", ""),
    ]
    assert cards.home_picks(Corpus(make_picks_corpus(tmp_path, specs, broad=False))) == []
    assert cards.home_picks(Corpus(make_picks_corpus(tmp_path / "b", specs))) == ["a1", "b1"]


def test_home_picks_are_distinct_and_skip_missing_data_nulls(tmp_path):
    specs = [
        ("a1", "pa", "null result", "alpha", "missing data"),
        ("a2", "pa", "observation", "alpha", ""),
        ("a3", "pb", "observation", "alpha", ""),
        ("b1", "pc", "observation", "beta", ""),
        ("c1", "pd", "observation", "gamma", ""),
        ("c2", "pe", "null result", "gamma", "unperformed analysis"),
    ]
    kb = make_picks_corpus(tmp_path, specs)
    c = Corpus(kb)
    picks = cards.home_picks(c)
    projects = [c.findings[f][0]["source"] for f in picks]
    assert len(set(picks)) == len(set(projects)) == 3
    for f in picks:
        assert c.gists[f]["case"] not in ("missing data", "unperformed analysis")
    assert picks == ["a2", "b1", "c1"]  # a3 shares a2's topic
    # Only two eligible findings: two picks.
    kb2 = make_picks_corpus(tmp_path / "two", specs[:2])
    assert cards.home_picks(Corpus(kb2)) == ["a2"]
    two = [("x1", "px", "observation", "t1", ""), ("y1", "py", "observation", "t2", "")]
    assert len(cards.home_picks(Corpus(make_picks_corpus(tmp_path / "three", two)))) == 2


def test_home_picks_and_ranks_reach_frontmatter_and_export(tmp_path):
    specs = [
        ("a1", "pa", "observation", "alpha", ""),
        ("a2", "pb", "observation", "alpha", ""),
        ("b1", "pc", "observation", "beta", ""),
        ("c1", "pd", "correction", "gamma", ""),
    ]
    c = Corpus(make_picks_corpus(tmp_path, specs))
    assert cards.home_picks(c) == ["a1", "b1", "c1"]
    assert cards.topic_picks(c, "alpha") == ["a1", "a2"]
    fields, _ = cards.split(finding_page("c1", c))
    assert fields["home_rank"] == 3 and fields["topic_ranks"]["gamma"] == 1
    fields, _ = cards.split(finding_page("a2", c))
    assert "home_rank" not in fields and fields["topic_ranks"]["alpha"] == 2
    assert cards.export(c)["home"] == ["a1", "b1", "c1"]


def test_index_blurbs_use_reader_words():
    assert cards.INDEXES["findings"] == (
        "Results",
        "Results from the project reports, one per card.",
    )
    assert cards.INDEXES["directions"] == (
        "Open questions",
        "Questions the project results leave open, by topic and by what answering them needs.",
    )


def test_home_ranks_by_distance_from_pubmed_then_links_to_other_projects(tmp_path):
    specs = [
        ("a1", "pa", "observation", "alpha", ""),
        ("b1", "pb", "observation", "beta", ""),
        ("c1", "pc", "observation", "gamma", ""),
        ("d1", "pd", "null result", "delta", "measured absence"),
        ("e1", "pe", "observation", "delta", ""),
        ("f1", "pf", "observation", "zeta", ""),
    ]
    kb = make_picks_corpus(tmp_path, specs)
    novel = {"label": "Candidate novel"}
    set_state(
        kb,
        "novelty.json",
        {"d1": novel, "e1": novel, "f1": novel, "c1": {"label": "Extends retrieved work"}},
    )
    link = {"level": "finding", "type": "same result", "label": "Same"}
    set_state(kb, "links.json", {"links": [link | {"a": "f1", "b": "a1"}]})
    # f1 links to another project; e1 is a result where d1 is a null in the same topic;
    # c1 builds on PubMed work, ahead of a1 and b1, which were never compared.
    assert cards.home_picks(Corpus(kb)) == ["f1", "e1", "c1"]


def test_topic_picks_swap_in_a_null_or_correction(tmp_path):
    specs = [
        ("a1", "pa", "observation", "alpha", ""),
        ("a2", "pb", "observation", "alpha", ""),
        ("a3", "pc", "observation", "alpha", ""),
        ("a4", "pa", "null result", "alpha", "measured absence"),
        ("a5", "pd", "null result", "alpha", "measured absence"),
    ]
    c = Corpus(make_picks_corpus(tmp_path, specs))
    # a4 shares project pa with a1, so a5 is the first usable null.
    assert cards.topic_picks(c, "alpha") == ["a1", "a2", "a5"]


def test_display_topic_is_the_most_citing_main_topic(tmp_path):
    kb = build(tmp_path)
    wiki = kb / "wiki/concepts"
    for stem in ("x1", "x2"):
        (wiki / f"{stem}.md").write_text(f"# {stem}\n\nClaim. [src: a]\n")
    (kb / "state/curator-topics.json").write_text(
        json.dumps(
            {
                "groups": [
                    {"title": "Alpha", "concepts": ["gap"]},
                    {"title": "Zeta", "concepts": ["x1", "x2"]},
                ]
            }
        )
    )
    c = Corpus(kb)
    assert c.topics_of("a") == ["alpha", "zeta"]
    # Alphabetical first would be alpha; zeta's concepts cite the report twice.
    assert c.display_topic("a") == "zeta"
    (wiki / "x2.md").write_text("# x2\n\nNo citation.\n")
    assert Corpus(kb).display_topic("a") == "alpha"  # a tie goes alphabetically


def test_compare_text_names_unlabelled_results():
    assert cards.compare_text(None) == cards.NOT_COMPARED
    assert cards.compare_text({"label": cards.NOT_ASSESSED, "override": "x"}) == cards.NOT_COMPARED
    assert cards.compare_text({"label": "Insufficient literature evidence"}) == (
        "Too little published evidence to compare"
    )
    assert cards.compare_text({"label": "Candidate novel"}) == "No close match in PubMed abstracts"


def test_readiness_explanations_and_check_notes_use_reader_words(tmp_path):
    """F6: free text a stage wrote never shows pipeline terms to readers."""
    kb = build(tmp_path)
    page = kb / "wiki/directions/transport--abc123.md"
    fields, body = cards.split(page.read_text())
    fields["readiness_basis"] = "The census exists, but the join needs compute."
    page.write_text(cards.join(fields, body + "\nApproach: lakehouse analysis. Readiness: x. "))
    out = cards.direction_page("transport--abc123", Corpus(kb))
    published, text = cards.split(out)
    assert published["readiness_basis"] == "The census exists, but the join needs a new analysis."
    assert "needs compute" not in text and "lakehouse analysis" not in text
    entry = {
        "label": "Extends retrieved work",
        "retrieved_on": "2026-10-23",
        "judge_model": "claude-sonnet-5-5",
        "agree_model": "gpt-6.1-sol",
        "judged_label": "Candidate novel",
        "agreed": False,
        "difference": "No retrieved paper reports it.",
        "closest": [{"pmid": "1", "title": "T", "relation": "related"}],
    }
    section = cards.literature_section(entry)
    assert "Candidate novel" not in section
    assert "No close match in PubMed abstracts" in section
    # F4: the unconfirmed judge's difference and papers argued for the rejected label.
    assert "No retrieved paper reports it." not in section and "PMID 1" not in section


def test_report_titles_drop_markdown_emphasis(tmp_path):
    """P3d: a footer shows the report title as plain text."""
    kb = build(tmp_path)
    (kb / "wiki/summaries/a__REPORT.md").write_text("# *Bacteroides* stress report\n\nText.\n")
    assert Corpus(kb).report_title("a") == "Bacteroides stress report"


def cross_corpus(tmp_path):
    """Two projects, a question citing both, a related-result link and a shared group."""
    kb = build(tmp_path)
    (kb / "wiki/sources").mkdir(parents=True, exist_ok=True)
    for sid in ("a", "b", "c"):
        (kb / "wiki/sources" / f"{sid}__REPORT.md").write_text(f"# Report {sid}\n")
        (kb / "wiki/summaries" / f"{sid}__REPORT.md").write_text(f"# Report {sid.upper()}\n")
    (kb / "wiki/concepts/other.md").write_text("# O\n\nText. [src: a, b]\n")
    set_state(
        kb,
        "curator-topics.json",
        {
            "groups": [
                {"title": "Dark Matter", "concepts": ["gap"]},
                {"title": "Other", "concepts": ["other"]},
            ]
        },
    )
    (kb / "wiki/concepts/gap.md").write_text("# Gap\n\nDark genes. [src: a, b]\n")
    other = "b--5e6f7a8b"
    (kb / "wiki/findings" / f"{other}.md").write_text(
        cards.join(
            {"source": "b", "result": "observation", "description": "Dark genes were rare."},
            "# Dark genes are rare in b\n\nClaim. [src: b]\n",
        )
    )
    page = kb / "wiki/directions/transport--abc123.md"
    fields, body = cards.split(page.read_text())
    page.write_text(cards.join(fields | {"findings": [FID, other]}, body))
    return kb, other


def test_degenerate_picture_without_link_or_shared_state(tmp_path):
    kb = build(tmp_path)
    c = Corpus(kb)
    data = cards.picture_data(c)
    assert data["links"] == [] and data["shared"] == []
    assert data["compare_order"][-1] == cards.NOT_COMPARED
    set_state(kb, "novelty.json", {})
    fields, _ = cards.split(finding_page(FID, Corpus(kb)))
    assert fields["compare_text"] == cards.NOT_COMPARED


def test_question_links_come_from_the_question_records(tmp_path):
    kb, other = cross_corpus(tmp_path)
    c = Corpus(kb)
    (q,) = [x for x in cards.links_index(c) if x["family"] == "q"]
    assert {q["a"], q["b"]} == {FID, other} and q["questions"] == [
        "Dark genes as nutrient transporters"
    ]
    fields, _ = cards.split(cards.direction_page("transport--abc123", c))
    assert [p["source"] for p in fields["cross"]] == ["a", "b"]
    assert fields["cross"][1]["results"] == [{"id": other, "title": "Dark genes are rare in b"}]
    assert fields["home_question_rank"] == 1 and len(fields["cross_topics"]) == 2


def test_links_with_a_missing_end_are_dropped(tmp_path):
    kb, other = cross_corpus(tmp_path)
    records = [
        {"a": FID, "b": other, "level": "finding", "type": "same result", "label": "Same thing"},
        {"a": FID, "b": "gone--00000000", "level": "finding", "type": "same result", "label": "x"},
        {"a": "a", "b": "b", "level": "project", "type": "corrects it", "label": "Fixes markers"},
        {"a": "a", "b": "missing", "level": "project", "type": "audits it", "label": "y"},
    ]
    set_state(kb, "links.json", {"links": records})
    got = cards.links_index(Corpus(kb))
    assert sorted((x["family"], x.get("label", "")) for x in got if x["family"] != "q") == [
        ("p", "Fixes markers"),
        ("r", "Same thing"),
    ]
    assert cards.picture_data(Corpus(kb))["project_titles"] == {"a": "Report A", "b": "Report B"}


def test_shared_groups_need_living_members_two_projects_and_two_topics(tmp_path):
    kb, other = cross_corpus(tmp_path)
    group = {
        "members": [FID, other],
        "relation": "same result",
        "lanes": {FID: "Dark genes in a", other: "Dark genes in b"},
    } | {k: f"{k} text" for k in ("title", "sentence", "question", "how")}
    set_state(kb, "shared.json", {"g-1": group, "g-2": group | {"members": [FID, "gone--1"]}})
    # Without a current related-result link joining the members, nothing is published.
    assert cards.shared_index(Corpus(kb)) == []
    link = {"a": FID, "b": other, "level": "finding", "type": "same result", "label": "Same"}
    set_state(kb, "links.json", {"links": [link]})
    (g,) = cards.shared_index(Corpus(kb))
    assert g["id"] == "g-1" and "home_rank" not in g and g["sources"] == ["a", "b"]
    assert g["relation"] == "Same result in each project" and len(g["topics"]) == 2
    assert [m["lane"] for m in g["members"]] == ["Dark genes in a", "Dark genes in b"]
    set_state(kb, "shared.json", {"g-1": group | {"failed": True}})
    assert cards.shared_index(Corpus(kb)) == []
    # A links refresh that changed how the results relate retires the old text.
    link |= {"type": "one measures what the other cannot", "label": "A measures what B cannot"}
    set_state(kb, "links.json", {"links": [link]})
    set_state(kb, "shared.json", {"g-1": group})
    assert cards.shared_index(Corpus(kb)) == []


def test_export_leaves_out_papers_an_unconfirmed_label_rested_on(tmp_path):
    """F4, agents' export: the rejected judge's closest papers are not shipped."""
    kb = build(tmp_path)
    set_state(
        kb,
        "novelty.json",
        {
            FID: {
                "label": "Extends retrieved work",
                "agreed": False,
                "closest": [{"pmid": "1", "title": "T", "relation": "related"}],
            }
        },
    )
    (row,) = [x for x in cards.export(Corpus(kb))["findings"] if x["id"] == FID]
    assert row["closest"] == []
