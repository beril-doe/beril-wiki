"""Smoke-check the pinned reference viewer adapter with a tiny native corpus."""
import pathlib
import tempfile
from unittest.mock import patch

import okf_tools


def test_graph():
    project = pathlib.Path(__file__).resolve().parent.parent
    source = okf_tools.upstream(project, "GoogleCloudPlatform/open-knowledge-format", okf_tools.VIEWER_REV)
    with tempfile.TemporaryDirectory() as tmp:
        root = pathlib.Path(tmp)
        concept = root / "wiki/concepts/a.md"
        topic = root / "wiki-extra/topics/b.md"
        for p in (concept, topic):
            p.parent.mkdir(parents=True, exist_ok=True)
        concept.write_text('---\ntype: Concept\ntitle: A\nresource: javascript:alert(1)\n---\n# A\n</script><script>alert(1)</script>\n')
        topic.write_text('---\ntype: Topic\ntitle: B\n---\n# B\n[Evidence](../../wiki/concepts/a.md)\n')
        out = root / "public/graph.html"
        with patch.object(okf_tools, "upstream", return_value=source):
            data = okf_tools.graph(root, out)
        assert {n["data"]["id"] for n in data["nodes"]} == {"wiki/concepts/a", "wiki-extra/topics/b"}
        assert data["edges"][0]["data"]["target"] == "wiki/concepts/a"
        assert not data["nodes"][0]["data"]["resource"]
        assert "[Evidence](/wiki/concepts/a.md)" in data["bodies"]["wiki-extra/topics/b"]
        html = out.read_text()
        assert "</script><script>alert(1)</script>" not in html
        assert "DOMPurify.sanitize(html)" in html
        assert not (root / "build/okf").exists()


if __name__ == "__main__":
    test_graph()
    print("test_okf_tools: passed")
