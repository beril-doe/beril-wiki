"""Evidence labels: countable facts about a page, never a review claim."""

from evidence import conflict_sources, label, page_sources

CONFLICTS = [{"amr_fitness_cost", "conservation_vs_fitness", "core_gene_tradeoffs"}]


def test_page_sources_dedupes_and_strips_report_suffix():
    text = ("Finding A. [src: amr_fitness_cost] Finding B. "
            "[src: amr_fitness_cost__REPORT, metal_specificity; amr_pangenome_atlas]")
    assert page_sources(text) == {"amr_fitness_cost", "metal_specificity", "amr_pangenome_atlas"}


def test_tiers():
    def tier(n):
        text = " ".join(f"Claim. [src: p{i}]" for i in range(n))
        return label(text, "concepts", [])
    assert "1 source project · single-source" in tier(1)
    assert "3 source projects · corroborated" in tier(3)
    assert "4 source projects · well corroborated" in tier(4)


def test_conflict_flag_needs_two_shared_sources():
    one = "Claim. [src: amr_fitness_cost] Claim. [src: metal_specificity]"
    two = "Claim. [src: amr_fitness_cost] Claim. [src: conservation_vs_fitness]"
    assert "conflict on record" not in label(one, "concepts", CONFLICTS)
    assert "conflict on record" in label(two, "concepts", CONFLICTS)


def test_conflict_pages_do_not_flag_themselves():
    two = "Claim. [src: amr_fitness_cost] Claim. [src: conservation_vs_fitness]"
    assert "conflict on record" not in label(two, "conflicts", CONFLICTS)


def test_literature_review_detected():
    text = "Claim. [src: p1]\n\n## Literature Context\n\nPMID stuff."
    assert "literature-reviewed" in label(text, "topics", [])


def test_unlabelled_collections_and_uncited_pages():
    cited = "Claim. [src: p1]"
    assert label(cited, "summaries", []) is None   # 1:1 with a project already
    assert label(cited, "sources", []) is None     # the raw report *is* the source
    assert label("no citations here", "concepts", []) is None


def test_conflict_sources_parses_filenames(tmp_path):
    d = tmp_path / "wiki-extra" / "conflicts"
    d.mkdir(parents=True)
    (d / "conflict--alpha--beta--gamma--8af84dcc.md").write_text("x")
    (d / "conflict--solo--deadbeef.md").write_text("x")
    got = conflict_sources(tmp_path)
    assert {"alpha", "beta", "gamma"} in got          # trailing hash dropped
    assert {"solo"} in got


def test_label_never_claims_review():
    text = " ".join(f"Claim. [src: p{i}]" for i in range(6))
    line = label(text, "topics", CONFLICTS).lower()
    for word in ("confidence", "reviewed by", "verified", "approved", "accurate"):
        assert word not in line, f"label implies review: {word!r}"


if __name__ == "__main__":
    import tempfile
    test_page_sources_dedupes_and_strips_report_suffix()
    test_tiers()
    test_conflict_flag_needs_two_shared_sources()
    test_conflict_pages_do_not_flag_themselves()
    test_literature_review_detected()
    test_unlabelled_collections_and_uncited_pages()
    test_label_never_claims_review()
    with tempfile.TemporaryDirectory() as d:
        import pathlib
        test_conflict_sources_parses_filenames(pathlib.Path(d))
    print("ok")
