"""The decisions manifest must be idempotent: already-applied decisions are
silent no-ops, so a rebuild from a fresh clone reaches the same concept set."""

import pathlib

from beril_wiki.stages import consolidate as cc


def _corpus(root: pathlib.Path, manifest: str) -> None:
    (root / "wiki" / "concepts").mkdir(parents=True)
    (root / "contract").mkdir()
    (root / cc.DECISIONS).write_text(manifest)


def test_applied_decisions_are_silent_noops(tmp_path: pathlib.Path) -> None:
    _corpus(
        tmp_path,
        "renames:\n  - from: old-slug\n    to: new-slug\n"
        "merges:\n  - loser: gone\n    survivor: kept\n",
    )
    (tmp_path / "wiki" / "concepts" / "new-slug.md").write_text("# already renamed\n")
    (tmp_path / "wiki" / "concepts" / "kept.md").write_text("# survivor\n")
    # Both decisions already applied: no failures, nothing touched, no LLM call.
    fails = cc.apply_decisions(tmp_path, {}, "", {}, tmp_path / "state.json")
    assert fails == [], fails
    assert (tmp_path / "wiki" / "concepts" / "new-slug.md").exists()
    assert not (tmp_path / "wiki" / "concepts" / "old-slug.md").exists()


def test_rename_with_neither_page_is_reported(tmp_path: pathlib.Path) -> None:
    _corpus(tmp_path, "renames:\n  - from: missing\n    to: also-missing\nmerges:\n")
    fails = cc.apply_decisions(tmp_path, {}, "", {}, tmp_path / "state.json")
    assert len(fails) == 1 and "neither page exists" in fails[0], fails
