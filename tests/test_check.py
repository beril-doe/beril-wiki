#!/usr/bin/env python3
"""Self-check for check's numeric machinery (no LLM calls, no network).

uv run pytest tests/test_check.py
"""

from __future__ import annotations

import pytest

from beril_wiki import check
from beril_wiki.check import (
    NUMBER,
    derivable_numbers,
    figures_in,
    norm_num,
    numbers_in,
    prose_only,
    unsupported_numbers,
)

SOURCES = {
    "p": "covered 7,609 genes (59.3%) with OR=1.46 p=1.3e-43 and |dGC| 0.047 vs 0.038, d = 0.247",
    "q": "a second study reported 123.4% and 66 genes",
}


def test_tokenizer():
    # scientific notation must win over the decimal rule, or every p-value in the
    # corpus is verified as its mantissa alone
    assert "1.3e-43" in NUMBER.findall("p=1.3e-43")
    assert NUMBER.findall("p=1.2e-83 and p=2.0E+4") == ["1.2e-83", "2.0E+4"]
    # a decimal followed by a prose comma is still a number
    assert "0.038" in NUMBER.findall("0.047 vs 0.038, d = 0.247")
    # identifiers are not figures
    assert NUMBER.findall("PF00034 and PF13442 and GCF_000005845") == []
    # small integers stay out of scope; 4+ digits and decimals are in
    assert NUMBER.findall("3 lines of evidence") == []
    assert NUMBER.findall("7,609 genes") == ["7,609"]
    assert norm_num("7,609") == "7609" and norm_num("59.3%") == "59.3"


def test_unsupported_numbers():
    ok = "Covered 7,609 genes (59.3%) at p=1.3e-43. [src: p]"
    assert unsupported_numbers(ok, ["p"], SOURCES) == []
    # substring matching used to pass all of these against the wrong source text
    assert unsupported_numbers("Rate was 12%. [src: q]", ["q"], SOURCES) == ["12%"]
    # "66%" against a source whose only 66 is a COUNT ("66 genes") is a real
    # mismatch: small integers are out of scope, so a percentage cannot be
    # verified against one. The substring form passed this.
    assert unsupported_numbers("Share was 66%. [src: q]", ["q"], SOURCES) == ["66%"]
    assert unsupported_numbers("Found 9,999 things. [src: p]", ["p"], SOURCES) == ["9,999"]
    # a figure only needs to appear in ONE of several cited sources
    assert unsupported_numbers("Both 7,609 and 123.4%. [src: p, q]", ["p", "q"], SOURCES) == []
    # an unknown id contributes no allowed figures, and is reported separately
    assert unsupported_numbers("Claim 7,609. [src: nope]", ["nope"], SOURCES) == []


def test_link_targets_are_not_figures():
    """A wikilink target is a filename. Conflict slugs carry an 8-hex digest of
    their project set, and reading it as a figure invents a violation."""
    par = "See [[conflicts/conflict--a--b--c--57107100]] for the split. [src: p]"
    assert unsupported_numbers(par, ["p"], SOURCES) == []
    assert NUMBER.findall(prose_only("ORCID: 0000-0003-2728-7671")) == []  # identifier, not figures
    assert NUMBER.findall(prose_only("<!-- tension-hash: 9514b16e -->\nProse.")) == []  # cache key
    # an alias is prose and stays checkable
    assert "9,999" in NUMBER.findall(prose_only("[[concepts/x|the 9,999 figure]]"))


def test_unit_suffixes_and_scientific_spellings():
    """Two spellings that used to make a real figure invisible in its source."""
    assert "7.8" in numbers_in("Motility (+7.8pp) and RNA Metabolism")  # unit suffix
    assert "18.8" in numbers_in("18.8M rows")
    assert numbers_in("p = 1.77e-06") == numbers_in("p = 1.77 x 10^-6")
    assert unsupported_numbers("p = 1.3 [src: p]", ["p"], SOURCES) == ["1.3"]
    assert numbers_in("PF00034 GCF_000005845") == set()  # still no identifiers
    assert figures_in("p=1.3e-43, n=42, 42%, +7.8pp, PF00034") == {
        "1.3e-43",
        "42",
        "42%",
        "7.8",
    }


def test_derivable_numbers():
    """A page may compute across its sources: 59.3% and 7,609 are stated, and a
    claim about their difference is supportable even though it appears nowhere
    verbatim. Accepted, but reported separately -- a coincidental pair is
    possible with a large enough source pool."""
    src = {"p": "core 24.4% versus non-core 16.6% of genes"}
    par = "The core-burden excess is 7.8 percentage points. [src: p]"
    assert unsupported_numbers(par, ["p"], src) == ["7.8"]  # not verbatim
    assert derivable_numbers(par, ["p"], src) == {"7.8"}  # but 24.4 - 16.6
    # a figure with no arithmetic route stays unsupported
    par2 = "The excess is 91.4 percentage points. [src: p]"
    assert derivable_numbers(par2, ["p"], src) == set()


@pytest.mark.parametrize(
    ("source", "value"),
    [
        ("24.4% versus 16.6%", "7.8"),
        ("24.444% versus 16.6%", "7.84"),
        ("1.0 versus 3.0", "0.33"),
        ("2.6e-43 versus 2.0", "1.3e-43"),
        ("2.6e-400 versus 2.0", "1.3e-400"),
        ("1.6e-43 versus 1.3e-43", "3e-44"),
    ],
)
def test_legitimate_rounded_derivations(source, value):
    assert derivable_numbers(f"The result is {value}. [src: p]", ["p"], {"p": source}) == {value}


@pytest.mark.parametrize("value", ["1e-99", "1.3", "0.000001", "1e-400", "1.3 x 10^-99"])
def test_scientific_values_do_not_supply_mantissas_or_tiny_derivations(value):
    sources = {"p": "The study measured p = 1.3e-43 and q = 2.6e-43."}
    claim = f"The study measured p = {value}. [src: p]"
    assert unsupported_numbers(claim, ["p"], sources) == [value]
    assert derivable_numbers(claim, ["p"], sources) == set()


@pytest.mark.parametrize("value", ["1.3e-43", "13e-44", "1.30E-43", "1.3 x 10^-43", "1.3 × 10^-43"])
def test_equivalent_scientific_notation(value):
    assert unsupported_numbers(f"p = {value}. [src: p]", ["p"], SOURCES) == []


@pytest.mark.parametrize(
    ("superscript", "ascii_value"),
    [
        ("7.9×10⁻¹⁰²", "7.9×10^-102"),
        ("1.4×10⁻¹⁵⁷", "1.4×10^-157"),
        ("2.6×10⁻¹⁹", "2.6×10^-19"),
        ("7.6 × 10⁻²²", "7.6×10^-22"),
        ("6.1 × 10⁻³⁹", "6.1×10^-39"),
        ("7.8 × 10⁻⁷", "7.8×10^-7"),
    ],
)
def test_unicode_scientific_notation(superscript, ascii_value):
    assert NUMBER.findall(superscript) == [superscript]
    assert numbers_in(superscript) == numbers_in(ascii_value)
    for source, value in ((superscript, ascii_value), (ascii_value, superscript)):
        assert unsupported_numbers(f"p = {value}. [src: p]", ["p"], {"p": source}) == []


@pytest.mark.parametrize(
    ("source", "value"),
    [
        ("1.3e-43", "1e-99"),
        ("7.9×10⁻¹⁰²", "7.9×10^-99"),
        ("7.9×10⁻¹⁰²", "7.9×10⁻⁹⁹"),
    ],
)
def test_strict_check_rejects_an_invented_scientific_value(
    tmp_path, monkeypatch, capsys, source, value
):
    for relative, body in (
        ("sources/p__REPORT.md", f"The study measured p = {source}."),
        ("concepts/c.md", f"The study measured p = {value}. [src: p]"),
    ):
        path = tmp_path / "wiki" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"# Report\n\n{body}\n")
    monkeypatch.setattr(check.sys, "argv", ["check", str(tmp_path), "--strict"])
    assert check.main() == 1
    assert f"number {value!r} not found" in capsys.readouterr().out


@pytest.mark.parametrize(
    ("source_value", "value", "valid"),
    [
        ("1.3e-43", "1.3e-43", True),
        ("1.3e-43", "1.3", False),
        ("1.3e-43", "43", False),
        ("1.3e-43", "-43", False),
        ("1.3e-43", "1.3e-99", False),
        ("1.3e-43", "1.30E-43", False),
        ("1.3 x 10^-43", "1.3 x 10^-43", True),
        ("1.3 x 10^-43", "43", False),
        ("1.3×10⁻⁴³", "1.3×10⁻⁴³", True),
        ("1.3×10⁻⁴³", "1.3", False),
    ],
)
def test_strict_card_gate_preserves_complete_scientific_values(
    tmp_path, monkeypatch, source_value, value, valid
):
    from beril_wiki.agentic.runtime import CandidateError
    from beril_wiki.stages import cards, headlines

    source = f"The measured signal was {source_value}."
    caveat = "The measurement needs replication."
    records = [
        {"id": "a:0:0", "kind": "finding", "quote": source},
        {"id": "a:0:1", "kind": "caveat", "quote": caveat},
    ]
    headline = headlines.Headline(
        evidence="a:0:0",
        result="observation",
        title="Measured signal",
        claim=f"The measured signal was {value}.",
        quantities=[headlines.Quantity(value=value, what="measured signal")],
        caveat_evidence="a:0:1",
        caveat=caveat,
    )
    accepted = True
    try:
        headlines.checker(records)(headlines.Reply(headlines=[headline]).model_dump_json())
    except CandidateError:
        accepted = False
    fid, fields, body = headlines.render("a", headline, records, "2026-11-14", "fixture")
    cards.write_page(tmp_path / "wiki/findings" / f"{fid}.md", fields, body)
    report = source + "\n\n" + caveat
    for relative, text in (
        ("sources/a__REPORT.md", report),
        ("summaries/a__REPORT.md", "# Summary\n"),
    ):
        path = tmp_path / "wiki" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
    errors = check.card_errors(tmp_path, {"a": report})
    monkeypatch.setattr(check.sys, "argv", ["check", str(tmp_path), "--strict"])
    strict_exit = check.main()
    assert (accepted, not errors, strict_exit == 0) == (valid, valid, valid)
    if not valid:
        assert any(f"key figure {value!r}" in error for error in errors)


def test_numbers_in():
    assert numbers_in("0.047 vs 0.038, d = 0.247") == {"0.047", "0.038", "0.247"}
