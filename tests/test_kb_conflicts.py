"""Check conflict scheduling, prose gates and page publication without a model."""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from beril_wiki.kb.jobs import Scope
from beril_wiki.kb.jobs.conflicts import after, jobs
from beril_wiki.kb.tools import Rejected

TENSION = (
    "Alpha found 0.42 g/g in 12,500 cultures [src: alpha]. "
    "Beta found 0.38 g/g in 9,100 cultures [src: beta]."
)
PAGE = """# Does growth yield depend on substrate?

The projects give different estimates of the biomass produced per mass of substrate.
That distinction matters when scientists choose measurements for comparing how efficiently
strains turn available carbon into growth. The estimates come from different strains on
different carbon sources. [[concepts/growth-yield]] provides the broader context for
comparing those estimates across projects.

## Evidence Sides

**Side A: Growth on glucose**

Alpha measured a growth yield of 0.42 g/g in 12,500 cultures [src: alpha]. Growth yield
is the mass of biomass produced for each mass of substrate consumed. The cultures give
a measurement for the strain and substrate in the study. They leave open how the strain
would grow if the available carbon source changed.

**Side B: Growth on acetate**

Beta measured a growth yield of 0.38 g/g in 9,100 cultures [src: beta]. This estimate
applies to the strain grown on acetate. The project measures biomass production under
its own study conditions. A comparison to the glucose estimate therefore combines
differences in the strains with differences in the carbon sources.

## Possible Reconciliations

- Hypothesis: The strains differ in how they use dissolved carbon. Differences in yield
  would then persist when both strains grow on the same substrate in the same conditions.
- Hypothesis: The substrates differ in how readily cells can use them for growth. A strain
  tested on both would then give different yields across the two growth conditions.

## Resolving Work

- Grow both strains on each substrate and measure biomass and carbon consumption. Do the
  strains differ when the growth conditions match?
- Collect biomass measurements across the growth period and compare yields at equivalent
  points in growth. Does the gap persist when the cultures are at comparable points?
- Use identical instruments to measure substrate consumption and biomass across replicates.
  How much of the difference remains with a common measurement protocol?
""".strip()


def _write(root: Path, relative: str, text: str) -> Path:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.fixture
def scope(tmp_path: Path) -> Scope:
    _write(
        tmp_path,
        "wiki/concepts/growth-yield.md",
        f"# Growth yield\n\nGrowth depends on the substrate.\n\n## Tensions\n\n{TENSION}",
    )
    _write(tmp_path, "wiki/sources/alpha__REPORT.md", "Yield was 0.42 g/g in 12,500 cultures.")
    _write(tmp_path, "wiki/sources/beta__REPORT.md", "Yield was 0.38 g/g in 9,100 cultures.")
    return Scope(
        root=tmp_path, source="alpha", reason="ingest", edited=["concepts/growth-yield#tensions"]
    )


def test_only_accepted_cross_project_tensions_owe_missing_pages(scope: Scope) -> None:
    """An unrelated edit, a single project or a standing page never schedules a job."""
    second = f"{TENSION} The studies used different substrates."
    _write(
        scope.root,
        "wiki/concepts/another.md",
        "# Another concept\n\nA second lead.\n\n## Tensions\n\n"
        f"One project [src: alpha; alpha__REPORT].\n\n{second}\n\n"
        "## Open Directions\n\nThis is not a tension [src: alpha, beta].\n",
    )
    scope.edited = ["concepts/growth-yield#lead", "entities/another#tensions"]
    assert jobs(scope) == []
    scope.edited.append("concepts/growth-yield#tensions")
    # The other concept states the same disagreement, so the page covers both, as in
    # the curator: its name depends on the whole group, whichever concept was edited.
    (merged,) = jobs(scope)
    assert "Growth depends on the substrate." in merged.pack["CONCEPT CONTEXT (framing only)"]
    assert "[source: alpha]" in merged.pack["SOURCE EXCERPTS (verification only)"]
    scope.edited.append("concepts/another#tensions")
    assert [job.key for job in jobs(scope)] == [merged.key]
    assert "another.md, Tensions paragraph 1" in merged.pack["TENSION"]
    assert TENSION in merged.pack["TENSION"] and second in merged.pack["TENSION"]
    assert "One project" not in merged.pack["TENSION"]
    assert "Open Directions" not in merged.pack["TENSION"]
    standing = _write(scope.root, f"wiki/{merged.key}.md", "# An accepted conflict\n")
    assert jobs(scope) == []

    scope.edited = ["concepts/another#tensions"]
    _write(scope.root, "wiki/concepts/another.md", "# Another concept\n\n## Tensions\n\nNone.")
    assert jobs(scope) == []
    assert standing.read_text(encoding="utf-8") == "# An accepted conflict\n"


def test_an_edited_tension_retires_the_page_of_its_old_wording(scope: Scope) -> None:
    """The page is named after the paragraph: without retirement the old and the new
    statement of one disagreement would both stay published."""
    out = scope.root / "wiki/conflicts"
    old = _write(scope.root, "wiki/conflicts/conflict--growth-yield--00000000.md", "old wording")
    other = _write(scope.root, "wiki/conflicts/conflict--untouched--11111111.md", "another")
    (job,) = jobs(scope)

    after(scope, {job.key: {"status": "rejected"}})
    assert old.exists(), "kept while its replacement was not accepted"

    job.publish({"page": "# The new wording"})
    after(scope, {job.key: {"status": "accepted"}})
    assert sorted(p.name for p in out.glob("*.md")) == sorted([other.name, f"{job.key[10:]}.md"])


@pytest.mark.parametrize(
    ("old", "new", "objection"),
    [
        ("## Evidence Sides", "## Findings", "missing required heading '## Evidence Sides'"),
        ("## Resolving Work", "## Followup", "missing required heading '## Resolving Work'"),
        ("## Possible Reconciliations", "## Ideas", "missing required heading"),
        (
            PAGE.split("**Side A: Growth on glucose**\n\n", 1)[1].split("**Side B:", 1)[0],
            "",
            "this side has no evidence under it",
        ),
        ("[src: beta]", "[src: invented]", "not a project id the input cites"),
        ("0.42 g/g", "0.99 g/g", "figure does not appear in the input"),
        ("0.42 g/g", "0.38 g/g", "figure appears in none of the cited sources"),
        ("[[concepts/growth-yield]]", "[[concepts/missing]]", "targets a page that does not exist"),
    ],
)
def test_job_refuses_page_errors_before_review(scope: Scope, old: str, new: str, objection: str):
    """A required heading, empty side, citation, figure or link error blocks the record."""
    (job,) = jobs(scope)
    with pytest.raises(Rejected) as refused:
        job.check({"page": PAGE.replace(old, new)})
    assert objection in "\n".join(refused.value.objections)


def test_publish_uses_the_curator_path_and_hash_without_overwriting(scope: Scope) -> None:
    """Accepted Markdown has the curator's filename and hash, and replay preserves state."""
    (job,) = jobs(scope)
    digest = hashlib.sha256(TENSION.encode()).hexdigest()
    assert job.key == f"conflicts/conflict--growth-yield--{digest[:8]}"
    assert (job.writer, job.reviewer) == ("write", "review")
    record = job.check({"page": PAGE})
    job.publish(record)
    path = scope.root / f"wiki/{job.key}.md"
    assert path.read_text(encoding="utf-8") == f"<!-- tension-hash: {digest[:16]} -->\n{PAGE}\n"
    path.write_text("# Existing accepted page\n", encoding="utf-8")
    job.publish(record)
    assert path.read_text(encoding="utf-8") == "# Existing accepted page\n"
    assert jobs(scope) == []
