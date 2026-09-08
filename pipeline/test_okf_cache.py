"""Format migration retains matching caches and does not bless stale results."""
import json
from pathlib import Path
import tempfile

from okf_cache import digest, rekey


def test_rekey():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "state").mkdir()
        page = root / "wiki/summaries/p__REPORT.md"
        stale = root / "wiki/summaries/stale__REPORT.md"
        before = {page: "---\ntype: Summary\n---\n# P\nClaim [src: p]\n", stale: "old"}
        after = {page: "---\ntype: Summary\n---\n# P\nClaim [^p]\n\n[^p]: P\n", stale: "new"}
        cache = root / "state/enrich.json"
        cache.write_text(json.dumps({page.name: digest(before[page]), stale.name: "previous-input"}))
        placements = root / "state/figures-placements.json"
        placements.write_text(json.dumps({"summaries/p__REPORT.md": {"page_hash": digest(before[page]), "placements": [{"after_paragraph": 1}]}}))
        rekey(root, before, after)
        assert json.loads(cache.read_text()) == {page.name: digest(after[page]), stale.name: "previous-input"}
        assert json.loads(placements.read_text())["summaries/p__REPORT.md"] == {"page_hash": digest(after[page]), "placements": [{"after_paragraph": 1}]}
        once = cache.read_bytes()
        rekey(root, after, after)
        assert cache.read_bytes() == once


if __name__ == "__main__":
    test_rekey()
    print("test_okf_cache: passed")
