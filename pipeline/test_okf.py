"""Run with uv run python pipeline/test_okf.py; no network or model calls."""
from pathlib import Path
from tempfile import TemporaryDirectory

import okf
import compile as C
import wiki_check as W
import topics_build as T
import authors_build as A
import consolidate_concepts as CC
import figures_build as F


def test_native_round_trip():
    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        for name in ("wiki/concepts", "wiki/summaries", "wiki/sources", "wiki-extra/topics"):
            (root / name).mkdir(parents=True)
        report = root / "wiki/sources/a__REPORT.md"
        report.write_text("# Report\n\nValue 24.4%.\n")
        summary = root / "wiki/summaries/a__REPORT.md"
        summary.write_text("# Summary\n\nValue 24.4%. [src: a]\n")
        path = root / "wiki/concepts/x.md"
        legacy = ('---\ntype: Concept\ncustom: retained\nsources: [summaries/a__REPORT.md]\n---\n'
                  '# X\n\nValue 24.4%. [src: a]\n\n## Open Directions\n\nPlan 50.5%. [src: a]\n\n'
                  '[Summary](../summaries/a__REPORT.md) and [[topics/hub|Topic]].\n\n'
                  'Ordinary note.[^note]\n\n[^note]: Personal explanation.\n\n'
                  '```markdown\n[src: fake] [[fake]]\n```\n\n`[src: inline]`\n')
        native = okf.normalize(legacy, path)
        path.write_text(native)
        (root / "wiki-extra/topics/hub.md").write_text(okf.normalize("# Hub\n", root / "wiki-extra/topics/hub.md"))
        summary.write_text(okf.normalize(summary.read_text(), summary))
        report.write_text(okf.normalize(report.read_text(), report))
        fields, content = okf.parse(native)
        assert fields["custom"] == "retained"
        assert fields["sources"] == [{"id": "a", "resource": "../summaries/a__REPORT.md", "title": "a"}]
        assert "[Topic](../../wiki-extra/topics/hub.md)" in content
        assert "[^a]: [a](../summaries/a__REPORT.md)" in content
        assert "[src: fake] [[fake]]" in content and "`[src: inline]`" in content
        assert "[^note]: Personal explanation." in content
        assert okf.normalize(native, path) == native
        assert okf.cited_ids(native) == ["a"]
        assert {sid for p in W.paragraphs(native) for sid in W.cited_ids(p)} == {"a"}
        assert C.validate_page(native, {"a": "24.4%"}, set(), check_links=False) == []
        assert okf.validate(root) == [], okf.validate(root)
        assert "../sources/a__REPORT.md" in summary.read_text()
        assert T.parse_page(path)["sources"] == {"a"}
        assert F.cited_projects(native, {"a", "fake"}) == ["a"]
        assert C.canonical_sources(content, fields["sources"]) == fields["sources"]
        assert A.author_projects('[A](../../wiki/summaries/a__REPORT.md)') == ["a"]


def test_link_rewrite():
    native = '[Claim](../concepts/old.md#evidence)\n\n```md\n[Code](../concepts/old.md)\n```\n'
    actual = CC.rewrite_concept_links(native, "old", "new")
    assert actual.startswith('[Claim](../concepts/new.md#evidence)')
    assert '[Code](../concepts/old.md)' in actual
    assert okf.map_links('`[x](old.md)` and [x](old.md)', lambda u: "new.md") == '`[x](old.md)` and [x](new.md)'


def test_metadata_and_reserved_pages():
    path = Path("/tmp/wiki/concepts/x.md")
    valid = "---\ntype: Concept\nsources:\n- resource: https://example.org/paper\n  custom: retained\n---\n# X\n"
    assert okf.normalize(valid, path) == valid
    duplicate = "---\ntype: Concept\nsources:\n- {id: a, resource: a.md}\n- {id: a, resource: b.md}\n---\n# X\n"
    try:
        okf.normalize(duplicate, path)
    except ValueError:
        pass
    else:
        raise AssertionError("duplicate sources silently lost")
    index = okf.normalize("# Index\n", Path("/tmp/wiki/index.md"))
    assert index == "# Index\n"
    log = okf.normalize("# Operations Log\n\n## [2026-09-01 12:00:00] ingest | a.md\n\n## [2026-09-02 12:00:00] ingest | b.md\n", Path("/tmp/wiki/log.md"))
    assert log.index("## 2026-09-02") < log.index("## 2026-09-01")
    assert "- [2026-09-01 12:00:00] ingest | a.md" in log
    assert okf.normalize(log, Path("/tmp/wiki/log.md")) == log
    with TemporaryDirectory() as tmp:
        page = Path(tmp) / "wiki" / "concepts" / "x.md"
        page.parent.mkdir(parents=True)
        original = "---\ntype: Concept\ncustom: kept\n---\n# X\n\nClaim.[^note]\n\n[^note]: An unrelated note.\n"
        page.write_text(original)
        okf.write(page, "# X\n\nClaim.[^note]\n")
        assert "custom: kept" in page.read_text() and "[^note]: An unrelated note." in page.read_text()
        before = page.read_bytes()
        try:
            okf.write(page, "---\ntype: []\n---\n# Invalid\n")
        except ValueError:
            pass
        else:
            raise AssertionError("invalid metadata accepted")
        assert page.read_bytes() == before


if __name__ == "__main__":
    test_native_round_trip()
    test_link_rewrite()
    test_metadata_and_reserved_pages()
    print("test_okf: all checks passed")
