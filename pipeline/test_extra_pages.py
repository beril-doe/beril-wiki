"""Regenerate aggregate pages after native migration without model calls."""
from pathlib import Path
import re
from tempfile import TemporaryDirectory
from unittest.mock import patch

import extra_pages as E
import okf


def test_native_aggregate_replay():
    with TemporaryDirectory() as directory:
        root = Path(directory)
        for name in ("wiki/concepts", "wiki/entities", "wiki/summaries", "wiki/sources", "wiki-extra"):
            (root / name).mkdir(parents=True)
        (root / "wiki/sources/p__REPORT.md").write_text("# Report\n\nMeasured 24.4%.\n")
        (root / "wiki/entities/item.md").write_text("# Item\n")
        (root / "wiki/summaries/p__REPORT.md").write_text(
            "# Summary\n\nMeasured 24.4%. [src: p]\n\n## Limitations\n\n"
            "Limited [[entities/item|Item]] coverage. [src: p]\n")
        for name in ("first", "second"):
            (root / f"wiki/concepts/{name}.md").write_text(
                f"# {name.title()}\n\nMeasured 24.4%. [src: p]\n\n## Open Directions\n\n"
                "Follow [[summaries/p__REPORT|the report]]. [src: p]\n\n"
                "Note.[^note]\n\n[^note]: [External note](https://example.org/paper).\n")
        okf.upgrade(root)
        with patch.object(E, "ROOT", root), patch.object(E, "OUT", root / "wiki-extra"):
            assert E.write_opportunities() == 2
            assert E.write_negative_results() == 1
            first = {p: p.read_bytes() for p in (root / "wiki-extra").glob("*.md")}
            E.write_opportunities()
            E.write_negative_results()
        assert all(p.read_bytes() == text for p, text in first.items())
        assert okf.validate(root) == [], okf.validate(root)
        opportunities = (root / "wiki-extra/opportunities.md").read_text()
        assert "[the report](../wiki/summaries/p__REPORT.md)" in opportunities
        assert opportunities.count("[^note]:") == 1
        assert opportunities.count("[^p]:") == 1
        for p in (root / "wiki-extra").glob("*.md"):
            definitions = re.findall(r"^\[\^([^\]]+)\]:", p.read_text(), re.M)
            assert len(definitions) == len(set(definitions))


if __name__ == "__main__":
    test_native_aggregate_replay()
    print("test_extra_pages: all checks passed")
