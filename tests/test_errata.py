#!/usr/bin/env python3
"""Errata: a source's own error is shown beside every claim that repeats it, and
nowhere else. No LLM calls, no network.

uv run pytest tests/test_errata.py
"""

from __future__ import annotations

import pathlib

import pytest

from beril_wiki import check
from beril_wiki.stages import errata as E

ENTRY = {
    "source": "bacdive",
    "contains": ["38.4%", "27,702"],
    "note": "The report reuses 38.4% for a second denominator; 5,647 of 27,702 is one fifth.",
}
WRONG = "Species matching recovered 5,647 of 27,702 species (38.4%). [src: bacdive]"
RIGHT = "The bridge matched 37,368 of 97,334 strains (38.4%). [src: bacdive]"
OTHER = "A different report matched 5,647 of 27,702 species (38.4%). [src: elsewhere]"


def page(*pars: str) -> str:
    return "---\ntype: concept\n---\n# Title\n\n" + "\n\n".join(pars) + "\n"


def test_matches_only_the_wrong_pairing_from_the_named_source():
    assert E.matches(WRONG, ENTRY, None)
    assert not E.matches(RIGHT, ENTRY, None)  # same figure, correct denominator
    assert not E.matches(OTHER, ENTRY, None)  # same figures, different source
    # a summary page is its own source, so it needs no [src:] tag
    assert E.matches(WRONG.replace(" [src: bacdive]", ""), ENTRY, "bacdive")
    assert not E.matches(WRONG.replace(" [src: bacdive]", ""), ENTRY, "another")


def test_apply_places_the_erratum_under_the_claim_and_is_idempotent():
    text = page(RIGHT, WRONG, "Closing words.")
    once = E.apply(text, [ENTRY], None)
    assert once.count(E.MARK) == 1
    blocks = once.split("\n\n")
    assert blocks[blocks.index(WRONG) + 1].startswith(E.MARK)  # directly under the claim
    assert "[src: bacdive]" in blocks[blocks.index(WRONG) + 1]
    assert once.startswith("---\ntype: concept\n---\n")  # frontmatter kept
    assert E.apply(once, [ENTRY], None) == once  # second pass changes nothing
    assert E.apply(page(RIGHT), [ENTRY], None) == page(RIGHT)  # untouched page returns as-is


def test_editing_the_note_replaces_the_old_callout():
    stale = E.apply(page(WRONG), [ENTRY], None)
    revised = E.apply(stale, [ENTRY | {"note": "A corrected note."}], None)
    assert revised.count(E.MARK) == 1 and "A corrected note." in revised
    assert "20.4%" not in revised


def test_erratum_passes_the_checker_it_sits_under():
    """No exemption: the callout is checked like the claim above it."""
    sources = {"bacdive": "matched 37,368 of 97,334 (38.4%) and 5,647 of 27,702 species"}
    text = E.callout(ENTRY)
    assert check.unsupported_numbers(text, check.cited_ids(text), sources) == []


def test_load_rejects_a_bad_entry(tmp_path: pathlib.Path):
    (tmp_path / "wiki/summaries").mkdir(parents=True)
    (tmp_path / "wiki/summaries/bacdive__REPORT.md").write_text("# x\n")
    (tmp_path / "wiki/sources").mkdir()
    (tmp_path / "wiki/sources/bacdive__REPORT.md").write_text("5,647 of 27,702 (38.4%)\n")
    (tmp_path / "contract").mkdir()
    good = "- source: bacdive\n  contains: ['38.4%']\n  note: n\n"
    (tmp_path / "contract/errata.yaml").write_text(good)
    assert len(E.load(tmp_path)) == 1
    (tmp_path / "contract/errata.yaml").write_text(good.replace("bacdive", "nope"))
    with pytest.raises(ValueError, match="unknown source"):
        E.load(tmp_path)
    (tmp_path / "contract/errata.yaml").write_text("- source: bacdive\n  note: n\n")
    with pytest.raises(ValueError, match="needs exactly"):
        E.load(tmp_path)
    (tmp_path / "contract/errata.yaml").write_text(
        "- source: bacdive\n  contains: ['38.4%']\n  note: the true figure is 20.4%\n"
    )
    with pytest.raises(ValueError, match="does not"):
        E.load(tmp_path)


def test_errata_never_restamps_figure_placements(tmp_path: pathlib.Path, monkeypatch):
    """A callout is a new paragraph, so placement indices after it moved: the stage must
    leave the cached hash stale for the figures stage to recompute, not certify it."""
    import json
    import sys

    from beril_wiki.stages import errata as E

    for d in ("wiki/concepts", "wiki/summaries", "wiki/sources", "contract", "state"):
        (tmp_path / d).mkdir(parents=True)
    (tmp_path / "wiki/summaries/bacdive__REPORT.md").write_text("# s\n")
    (tmp_path / "wiki/sources/bacdive__REPORT.md").write_text("5,647 of 27,702 (38.4%)\n")
    (tmp_path / "contract/errata.yaml").write_text(
        "- source: bacdive\n  contains: ['38.4%', '27,702']\n  note: one fifth\n"
    )
    (tmp_path / "wiki/concepts/x.md").write_text(f"# X\n\n{WRONG}\n")
    placements = tmp_path / "state/figures-placements.json"
    placements.write_text(json.dumps({"concepts/x.md": {"page_hash": "stale", "index": 1}}))
    monkeypatch.setattr(sys, "argv", ["errata", str(tmp_path)])
    assert E.main() == 0
    assert E.MARK in (tmp_path / "wiki/concepts/x.md").read_text()
    assert json.loads(placements.read_text())["concepts/x.md"]["page_hash"] == "stale"
