"""The subjectivity guard on author pages: it must catch the phrasings the
pre-rev-2 prompt produced, and leave factual contribution prose alone."""

import json

from beril_wiki.stages.authors import subjective_hits

# Real sentences from the rev-1 pages (wiki/authors/), which asserted
# what a named person is interested in rather than what their projects found.
CHARACTERISING = [
    "Their work therefore suggests a research program focused on testing when "
    "laboratory measurements predict conservation or field ecology.",
    "Recurring interests include context-dependent gene essentiality and conditional fitness.",
    "Taken together, their projects center on quantitative integration of "
    "experimental fitness with genome evolution.",
    "The emphasis on low-MSA-depth core proteins suggests an interest in "
    "prioritizing conserved but structurally isolated proteins.",
    "The corpus therefore suggests research interests in microbial ecology.",
]

# Factual reporting: what a project did, what it measured, what it found.
FACTUAL = [
    "The project mapped resistance across 27,690 pangenome species and found "
    "that 30.3% of AMR genes were core versus 46.8% of the baseline. "
    "[src: amr_pangenome_atlas]",
    "Across approximately 194,000 genes from 43 bacteria, essential genes were "
    "82% core while always-neutral genes were 66% core. "
    "[src: fitness_effects_conservation]",
    "It integrated TnSeq, flux-balance analysis, and proteomics, reporting "
    "73.8% concordance among 866 genes. [src: adp1_triple_essentiality]",
]


# Ordinary reporting that the first version of the guard wrongly flagged: the
# verbs are about a project or a result, not about a person. Flagging these let
# strip_subjective() delete source-backed sentences and cache the result.
FACTUAL_WITH_SHARED_VERBS = [
    "The project focused on metal tolerance across 14 metals. [src: metal_specificity]",
    "The results suggest a shared mechanism rather than independent acquisition. "
    "[src: amr_strain_variation]",
    "The analysis centered on 4,770 species with both marker types. "
    "[src: prophage_amr_comobilization]",
    "Enrichment was apparent in the auxiliary genome at 2.2x. [src: amr_pangenome_atlas]",
]


def test_passes_factual_prose_using_the_same_verbs():
    for s in FACTUAL_WITH_SHARED_VERBS:
        assert not subjective_hits(s), f"false positive: {s}"


def test_still_catches_those_verbs_about_a_person():
    for s in [
        "Their projects center on quantitative integration of fitness data.",
        "The corpus therefore suggests they prioritise annotation quality.",
        "Their work focuses on subsurface ecology.",
    ]:
        assert subjective_hits(s), f"missed: {s}"


def test_catches_characterising_sentences():
    for s in CHARACTERISING:
        assert subjective_hits(s), f"missed: {s}"


def test_passes_factual_reporting():
    for s in FACTUAL:
        assert not subjective_hits(s), f"false positive: {s}"


def test_removed_author_page_is_deleted(tmp_path, monkeypatch):
    from beril_wiki.stages import extras

    checkout = tmp_path / "checkout"
    readmes = {"p1": "Alice Smith", "p2": "Bob Jones"}
    for pid, author in readmes.items():
        (checkout / "projects" / pid).mkdir(parents=True)
        (checkout / "projects" / pid / "REPORT.md").write_text("r\n")
        (checkout / "projects" / pid / "README.md").write_text(
            f"# {pid}\n\n## Authors\n- {author}\n"
        )
    (tmp_path / "staging").mkdir()
    (tmp_path / "state").mkdir()
    monkeypatch.setattr(extras, "CHECKOUT", checkout)
    monkeypatch.setattr(extras, "ROOT", tmp_path)
    monkeypatch.setattr(extras, "OUT", tmp_path / "wiki")
    authors = tmp_path / "wiki/authors"
    extras.write_authors()
    (authors / "index.md").write_text("index\n")
    state = tmp_path / "state/authors.json"
    state.write_text(json.dumps({"alice-smith.md": "h1", "bob-jones.md": "h2"}))

    (checkout / "projects/p2/README.md").write_text("# p2\n\n## Authors\n- Alicia Smith\n")
    extras.write_authors()

    assert sorted(p.name for p in authors.glob("*.md")) == [
        "alice-smith.md",
        "alicia-smith.md",
        "index.md",
    ]
    assert json.loads(state.read_text()) == {"alice-smith.md": "h1"}
