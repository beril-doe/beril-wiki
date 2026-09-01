#!/usr/bin/env python3
"""Self-check for compile.py's deterministic logic (no LLM calls).

    uv run python pipeline/test_compile.py
"""

from __future__ import annotations

import pathlib
import tempfile

from compile import (
    downgrade_dead_links,
    fm_block,
    fm_entity_type,
    normalize_plan,
    parse_fm,
    parse_json_reply,
    validate_page,
)

SOURCES = {"proj_a": "The assay covered 7,609 genes and 59.3% of records.", "proj_b": "n=42"}
TARGETS = {"concepts/gene-essentiality", "summaries/proj_a__REPORT"}


def test_json():
    assert parse_json_reply('```json\n{"a": 1}\n```') == {"a": 1}
    assert parse_json_reply('Sure! {"content": "x"} done') == {"content": "x"}


def test_validate():
    ok = ("# T\n\nCovers 7,609 genes (59.3%). [src: proj_a]\n\n"
          "Links [[concepts/gene-essentiality]]. [src: proj_a]\n\n## Slots Into\n\n- [[concepts/gene-essentiality]] — x")
    assert validate_page(ok, SOURCES, TARGETS, require_slots=True) == []
    assert any("unknown source id" in v for v in validate_page("Claim. [src: nope]", SOURCES, TARGETS))
    assert any("no [src:] citation" in v for v in validate_page("Found 7,609 genes.", SOURCES, TARGETS))
    assert any("not found in cited source" in v for v in validate_page("Found 8,888 genes. [src: proj_a]", SOURCES, TARGETS))
    assert any("does not exist" in v for v in validate_page("See [[concepts/made-up]]. [src: proj_a]", SOURCES, TARGETS))
    assert validate_page("See [[concepts/made-up]]. [src: proj_a]", SOURCES, TARGETS, check_links=False) == []
    assert any("Slots Into" in v for v in validate_page("Fine. [src: proj_a]", SOURCES, TARGETS, require_slots=True))
    # numbers in a comma-grouped source still resolve after normalization
    assert validate_page("It found 7609 genes. [src: proj_a]", SOURCES, TARGETS) == []


def test_links_and_fm():
    text = "Keep [[concepts/gene-essentiality]], drop [[concepts/ghost|Ghost Idea]] and [[concepts/other-ghost]]."
    out = downgrade_dead_links(text, TARGETS)
    assert "[[concepts/gene-essentiality]]" in out and "[[concepts/ghost" not in out
    assert "Ghost Idea" in out and "other ghost" in out

    fm, body = parse_fm(fm_block({"type": "Summary", "description": 'has "quotes"', "sources": ["a.md"]}) + "body\n")
    assert fm == {"type": "Summary", "description": 'has "quotes"', "sources": ["a.md"]} and body == "body\n"
    assert fm_entity_type("gene_or_pathway") == "Gene_Or_Pathway"


def test_plan():
    with tempfile.TemporaryDirectory() as td:
        root = pathlib.Path(td)
        (root / "wiki" / "concepts").mkdir(parents=True)
        (root / "wiki" / "entities").mkdir(parents=True)
        (root / "wiki" / "concepts" / "gene-essentiality.md").write_text("x")
        plan = normalize_plan({
            "concepts": {
                "create": [{"name": "gene-essentiality", "title": "GE"},           # exists -> update
                           {"name": "new idea!", "title": "NI", "justification": "closest page is X; wrong because Y"},
                           {"name": "unjustified", "title": "U"}],                 # rejected
                "update": [{"name": "phantom", "title": "P"}],                     # missing -> create
            },
            "entities": {"create": [{"name": "bacdive", "title": "BacDive", "type": "not-a-type"}]},
        }, root)
        assert [c["name"] for c in plan["concepts"]["update"]] == ["gene-essentiality"]
        assert sorted(c["name"] for c in plan["concepts"]["create"]) == ["new-idea", "phantom"]
        assert plan["entities"]["create"][0]["type"] == "other"


if __name__ == "__main__":
    test_json()
    test_validate()
    test_links_and_fm()
    test_plan()
    print("test_compile: all checks passed")
