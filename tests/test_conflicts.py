#!/usr/bin/env python3
"""Self-check for stages.conflicts's grouping and naming (no LLM calls).

uv run pytest tests/test_conflicts.py
"""

from __future__ import annotations

from beril_wiki.stages import conflicts as CB

SHARED = "Both report rho = 0.106 and p = 1.77e-06 and 24.4% versus 16.6%. [src: a, b]"


def test_each_multi_project_tension_paragraph_is_one_block(tmp_path, monkeypatch):
    (tmp_path / "wiki/concepts").mkdir(parents=True)
    (tmp_path / "wiki/concepts/c.md").write_text(
        "# C\n\nLead. [src: a]\n\n## Tensions\n\nFirst disagreement. [src: a] Other side. "
        "[src: b]\n\nOne project's own two analyses differ. [src: a]\n\n"
        "Second disagreement at 91.2%. [src: a, c]\n\n## Open Directions\n\n- None."
    )
    monkeypatch.setattr(CB, "ROOT", tmp_path)
    blocks = CB.tension_blocks()
    assert [(b["index"], sorted(b["projects"])) for b in blocks] == [
        (0, ["a", "b"]),
        (2, ["a", "c"]),
    ]
    groups = CB.merge_similar_groups(blocks)
    assert len(groups) == 2
    slugs = {CB.conflict_slug(g) for g in groups}
    assert len(slugs) == 2 and all(s.startswith("conflict--c--") for s in slugs)
    # The slug follows the paragraph text, so an unchanged paragraph keeps its page.
    assert {CB.conflict_slug(g) for g in CB.merge_similar_groups(CB.tension_blocks())} == slugs


def test_merge_only_on_shared_project_and_shared_figures():
    """Two paragraphs restating one disagreement become one page; a shared
    project alone or the same figures under different projects do not."""
    blocks = [
        {"concept": "x", "index": 0, "text": SHARED, "projects": {"a", "b"}},
        {"concept": "y", "index": 3, "text": SHARED, "projects": {"a", "c"}},
        {"concept": "z", "index": 1, "text": "Unrelated: 91.2% of 8,314 loci.", "projects": {"a"}},
        {"concept": "w", "index": 0, "text": SHARED, "projects": {"d", "e"}},
    ]
    groups = CB.merge_similar_groups(blocks)
    assert sorted(len(g) for g in groups) == [1, 1, 2]
    merged = next(g for g in groups if len(g) == 2)
    assert [b["concept"] for b in merged] == ["x", "y"]
    assert CB.conflict_slug(merged).startswith("conflict--x--")
