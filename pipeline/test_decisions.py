"""The decisions manifest must be idempotent: already-applied decisions are
silent no-ops, so a rebuild from a fresh clone reaches the same concept set."""
import pathlib, sys, tempfile
sys.path.insert(0, "pipeline")
import consolidate_concepts as cc

with tempfile.TemporaryDirectory() as d:
    root = pathlib.Path(d)
    (root / "wiki" / "concepts").mkdir(parents=True)
    (root / "contract").mkdir()
    (root / cc.DECISIONS).write_text(
        "renames:\n  - from: old-slug\n    to: new-slug\n"
        "merges:\n  - loser: gone\n    survivor: kept\n")
    (root / "wiki" / "concepts" / "new-slug.md").write_text("# already renamed\n")
    (root / "wiki" / "concepts" / "kept.md").write_text("# survivor\n")
    # Both decisions already applied: no failures, nothing touched, no LLM call.
    fails = cc.apply_decisions(root, {}, "", {}, root / "state.json")
    assert fails == [], fails
    assert (root / "wiki" / "concepts" / "new-slug.md").exists()
    assert not (root / "wiki" / "concepts" / "old-slug.md").exists()

with tempfile.TemporaryDirectory() as d:
    root = pathlib.Path(d)
    (root / "wiki" / "concepts").mkdir(parents=True)
    (root / "contract").mkdir()
    (root / cc.DECISIONS).write_text("renames:\n  - from: missing\n    to: also-missing\nmerges:\n")
    fails = cc.apply_decisions(root, {}, "", {}, root / "state.json")
    assert len(fails) == 1 and "neither page exists" in fails[0], fails

print("ok")
