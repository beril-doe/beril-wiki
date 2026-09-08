"""Publishing preserves native OKF paths and source attribution, without a model."""

import pathlib
import tempfile
import hashlib

from quartz_ingest import remap_links, site_path, splice_figures


def test_remap():
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        topic = root / "wiki-extra/topics/topic.md"
        concept = root / "wiki/concepts/concept.md"
        home = root / "wiki-extra/home.md"
        paths = {p: site_path(p, root) for p in (topic, concept, home)}
        text = ("[Evidence](../../wiki/concepts/concept.md#results)\n"
                "[Home](../home.md)\n`[example](../../wiki/concepts/concept.md)`\n"
                "[External](https://example.org/a.md)\n")
        result = remap_links(text, topic, paths)
        assert "[Evidence](../concepts/concept.md#results)" in result
        assert "[Home](../index.md)" in result
        assert "`[example](../../wiki/concepts/concept.md)`" in result
        assert "https://example.org/a.md" in result
        assert site_path(home, root) == pathlib.Path("index.md")
        assert site_path(root / "wiki/index.md", root) == pathlib.Path("catalog.md")
        assert remap_links("[Hidden](../../wiki/concepts/concept.md)", topic, paths,
                           {concept.resolve()}) == "Hidden"
        figure = root / "wiki/figures/p/a.png"
        figure.parent.mkdir(parents=True)
        figure.write_bytes(b"image")
        text = "---\ntype: Topic\n---\n# Topic\n\nFirst [^p]\n\n[^p]: [P](../summaries/p.md)\n\nLast\n"
        entry = {"page_hash": hashlib.sha256(text.encode()).hexdigest()[:16],
                 "placements": [{"after_paragraph": 2, "project": "p", "file": "a.png", "caption": "Figure"}]}
        result = splice_figures(text, entry, root, root / "output")
        assert result.index("Last") < result.index("![Figure]") < result.index("[^p]:")
        assert result.count("[^p]:") == 1


if __name__ == "__main__":
    test_remap()
    print("test_quartz_ingest: passed")
