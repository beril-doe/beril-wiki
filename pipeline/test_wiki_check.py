#!/usr/bin/env python3
"""Self-check for wiki_check's numeric machinery (no LLM calls, no network).

    uv run python pipeline/test_wiki_check.py
"""

from __future__ import annotations

from wiki_check import (NUMBER, derivable_numbers, norm_num, numbers_in, prose_only,
                        unsupported_numbers)

SOURCES = {"p": "covered 7,609 genes (59.3%) with OR=1.46 p=1.3e-43 and |dGC| 0.047 vs 0.038, d = 0.247",
           "q": "a second study reported 123.4% and 66 genes"}


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
    assert NUMBER.findall(prose_only("ORCID: 0000-0003-2728-7671")) == []   # identifier, not figures
    assert NUMBER.findall(prose_only("<!-- tension-hash: 9514b16e -->\nProse.")) == []  # cache key
    # an alias is prose and stays checkable
    assert "9,999" in NUMBER.findall(prose_only("[[concepts/x|the 9,999 figure]]"))


def test_unit_suffixes_and_mantissas():
    """Two spellings that used to make a real figure invisible in its source."""
    assert "7.8" in numbers_in("Motility (+7.8pp) and RNA Metabolism")     # unit suffix
    assert "18.8" in numbers_in("18.8M rows")
    assert numbers_in("p = 1.77e-06") >= {"1.77e-06", "1.77"}              # mantissa too
    assert numbers_in("PF00034 GCF_000005845") == set()                    # still no identifiers


def test_derivable_numbers():
    """A page may compute across its sources: 59.3% and 7,609 are stated, and a
    claim about their difference is supportable even though it appears nowhere
    verbatim. Accepted, but reported separately -- a coincidental pair is
    possible with a large enough source pool."""
    src = {"p": "core 24.4% versus non-core 16.6% of genes"}
    par = "The core-burden excess is 7.8 percentage points. [src: p]"
    assert unsupported_numbers(par, ["p"], src) == ["7.8"]     # not verbatim
    assert derivable_numbers(par, ["p"], src) == {"7.8"}       # but 24.4 - 16.6
    # a figure with no arithmetic route stays unsupported
    par2 = "The excess is 91.4 percentage points. [src: p]"
    assert derivable_numbers(par2, ["p"], src) == set()


def test_numbers_in():
    assert numbers_in("0.047 vs 0.038, d = 0.247") == {"0.047", "0.038", "0.247"}


if __name__ == "__main__":
    test_tokenizer()
    test_unsupported_numbers()
    test_link_targets_are_not_figures()
    test_unit_suffixes_and_mantissas()
    test_derivable_numbers()
    test_numbers_in()
    print("test_wiki_check: all checks passed")
