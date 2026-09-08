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
    """conflict_slug appends a digest only for groups of MORE than three, so the
    trailing component is a hash only when it looks like one. Stripping it
    unconditionally ate a real project id from every unhashed file."""
    d = tmp_path / "wiki-extra" / "conflicts"
    d.mkdir(parents=True)
    (d / "conflict--alpha--beta--gamma--delta--8af84dcc.md").write_text("x")   # >3: hashed
    (d / "conflict--alpha--beta--gamma.md").write_text("x")                    # 3: unhashed
    (d / "conflict--solo--partner.md").write_text("x")                         # 2: unhashed
    got = conflict_sources(tmp_path)
    assert {"alpha", "beta", "gamma", "delta"} in got   # real hash dropped
    assert {"alpha", "beta", "gamma"} in got            # third id is NOT a hash
    assert {"solo", "partner"} in got                   # two-project set stays a pair


def test_two_project_conflict_can_still_flag(tmp_path):
    """A two-project conflict degraded to one project could never meet the
    two-source test in label(), so it silently flagged nothing."""
    d = tmp_path / "wiki-extra" / "conflicts"
    d.mkdir(parents=True)
    (d / "conflict--ecotype_env_reanalysis--enigma_carbon_census_1.md").write_text("x")
    conflicts = conflict_sources(tmp_path)
    page = "Claim. [src: ecotype_env_reanalysis] Claim. [src: enigma_carbon_census_1]"
    assert "conflict on record" in label(page, "concepts", conflicts)


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
    import pathlib
    for fn in (test_conflict_sources_parses_filenames, test_two_project_conflict_can_still_flag):
        with tempfile.TemporaryDirectory() as d:
            fn(pathlib.Path(d))
    print("ok")
