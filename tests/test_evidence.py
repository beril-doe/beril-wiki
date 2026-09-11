"""Evidence labels: countable facts about a page, never a review claim."""

from beril_wiki.evidence import conflict_sources, label, page_sources

CONFLICTS = [{"amr_fitness_cost", "conservation_vs_fitness", "core_gene_tradeoffs"}]


def labelled(text: str, collection: str, conflicts: list[set[str]]) -> str:
    """label() for a page that must earn a line; None here is a test failure."""
    line = label(text, collection, conflicts)
    assert line is not None, (text, collection)
    return line


def test_page_sources_dedupes_and_strips_report_suffix():
    text = (
        "Finding A. [src: amr_fitness_cost] Finding B. "
        "[src: amr_fitness_cost__REPORT, metal_specificity; amr_pangenome_atlas]"
    )
    assert page_sources(text) == {"amr_fitness_cost", "metal_specificity", "amr_pangenome_atlas"}


def test_tiers():
    def tier(n):
        text = " ".join(f"Claim. [src: p{i}]" for i in range(n))
        return labelled(text, "concepts", [])

    assert "1 source project · single-source" in tier(1)
    assert "3 source projects · corroborated" in tier(3)
    assert "4 source projects · well corroborated" in tier(4)


def test_conflict_flag_needs_two_shared_sources():
    one = "Claim. [src: amr_fitness_cost] Claim. [src: metal_specificity]"
    two = "Claim. [src: amr_fitness_cost] Claim. [src: conservation_vs_fitness]"
    assert "conflict on record" not in labelled(one, "concepts", CONFLICTS)
    assert "conflict on record" in labelled(two, "concepts", CONFLICTS)


def test_conflict_pages_do_not_flag_themselves():
    two = "Claim. [src: amr_fitness_cost] Claim. [src: conservation_vs_fitness]"
    assert "conflict on record" not in labelled(two, "conflicts", CONFLICTS)


def test_literature_context_detected():
    text = "Claim. [src: p1]\n\n## Literature Context\n\nPMID stuff."
    assert "literature context" in labelled(text, "topics", [])
    # The term must not read as a review claim: a heading is all it tests.
    assert "reviewed" not in labelled(text, "topics", [])


def test_unlabelled_collections_and_uncited_pages():
    cited = "Claim. [src: p1]"
    assert label(cited, "summaries", []) is None  # 1:1 with a project already
    assert label(cited, "sources", []) is None  # the raw report *is* the source
    assert label("no citations here", "concepts", []) is None


def test_conflict_sources_reads_the_body_not_the_filename(tmp_path):
    """conflict_slug names a page after its first three projects and appends a
    digest beyond that, so the filename cannot express a larger set. The body
    cites every project in the group, so that is what must be read."""
    d = tmp_path / "wiki" / "conflicts"
    d.mkdir(parents=True)
    # Exactly what conflict_slug produces for a five-project group.
    (d / "conflict--alpha--beta--gamma--8af84dcc.md").write_text(
        "# T\n\nClaim. [src: alpha] Claim. [src: beta, gamma]\n\n"
        "Claim. [src: delta] Claim. [src: epsilon]\n"
    )
    got = conflict_sources(tmp_path)
    assert {"alpha", "beta", "gamma", "delta", "epsilon"} in got, got


def test_page_overlapping_only_unnamed_projects_still_flags(tmp_path):
    """The regression: delta and epsilon appear nowhere in the filename, so a
    page citing just those two used to miss its conflict flag."""
    d = tmp_path / "wiki" / "conflicts"
    d.mkdir(parents=True)
    (d / "conflict--alpha--beta--gamma--8af84dcc.md").write_text(
        "# T\n\nClaim. [src: alpha, beta, gamma, delta, epsilon]\n"
    )
    conflicts = conflict_sources(tmp_path)
    page = "Claim. [src: delta] Claim. [src: epsilon]"
    assert "conflict on record" in labelled(page, "concepts", conflicts)


def test_single_project_conflict_page_is_ignored(tmp_path):
    d = tmp_path / "wiki" / "conflicts"
    d.mkdir(parents=True)
    (d / "conflict--solo.md").write_text("# T\n\nClaim. [src: solo]\n")
    assert conflict_sources(tmp_path) == []


def test_label_never_claims_review():
    text = " ".join(f"Claim. [src: p{i}]" for i in range(6))
    line = labelled(text, "topics", CONFLICTS).lower()
    for word in ("confidence", "reviewed by", "verified", "approved", "accurate"):
        assert word not in line, f"label implies review: {word!r}"


if __name__ == "__main__":
    import tempfile

    test_page_sources_dedupes_and_strips_report_suffix()
    test_tiers()
    test_conflict_flag_needs_two_shared_sources()
    test_conflict_pages_do_not_flag_themselves()
    test_literature_context_detected()
    test_unlabelled_collections_and_uncited_pages()
    test_label_never_claims_review()
    import pathlib

    for fn in (
        test_conflict_sources_reads_the_body_not_the_filename,
        test_page_overlapping_only_unnamed_projects_still_flags,
        test_single_project_conflict_page_is_ignored,
    ):
        with tempfile.TemporaryDirectory() as d:
            fn(pathlib.Path(d))
    print("ok")
