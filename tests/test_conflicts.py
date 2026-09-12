#!/usr/bin/env python3
"""Self-check for stages.conflicts's grouping and naming (no LLM calls).

uv run pytest tests/test_conflicts.py
"""

from __future__ import annotations

from beril_wiki.stages import conflicts as CB


def test_conflict_slug():
    """The slug must be unique to the COMPLETE project set. Naming after the
    first three ids let two groups sharing those three overwrite one file, and
    because the existing-hash map is read once, the survivor alternated between
    them on every otherwise-unchanged run."""
    assert CB.conflict_slug(("a", "b", "c")) == "conflict--a--b--c"  # short sets stay readable
    long_a = CB.conflict_slug(("a", "b", "c", "d"))
    long_b = CB.conflict_slug(("a", "b", "c", "e"))
    assert long_a.startswith("conflict--a--b--c--") and long_a != long_b
    assert CB.conflict_slug(("a", "b", "c", "d")) == long_a  # stable across runs


def test_merge_similar_groups(monkeypatched=None):
    """One disagreement reaching two project sets is one page, not two --
    but only when the groups also share a project, since these pages share a
    template and the median unrelated pair already sits near 0.79."""
    shared = "Both report rho = 0.106 and p = 1.77e-06 and 24.4% versus 16.6%."
    groups = {
        ("a", "b"): [{"text": shared, "projects": {"a", "b"}}],
        ("a", "c"): [{"text": shared, "projects": {"a", "c"}}],  # same figures, shares 'a'
        ("x", "y"): [{"text": "Unrelated: 91.2% of 8,314 loci.", "projects": {"x", "y"}}],
    }
    # threshold 1.1 disables the similarity path, isolating the evidence rule
    out = CB.merge_similar_groups(groups, 1.1)
    assert len(out) == 2, out
    assert ("a", "b", "c") in out and len(out[("a", "b", "c")]) == 2
    assert ("x", "y") in out

    # no shared project -> never merged, however alike the text
    apart = {
        ("a", "b"): [{"text": shared, "projects": {"a", "b"}}],
        ("c", "d"): [{"text": shared, "projects": {"c", "d"}}],
    }
    assert len(CB.merge_similar_groups(apart, 1.1)) == 2
