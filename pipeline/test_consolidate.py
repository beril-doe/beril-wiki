#!/usr/bin/env python3
"""Self-check for consolidate_concepts.py's deterministic logic (no LLM calls).

    uv run python pipeline/test_consolidate.py
"""

from __future__ import annotations

from consolidate_concepts import (
    backmerge_candidates,
    body_src_ids,
    both_mature,
    cosine,
    merge_candidates,
    rewrite_concept_links,
    sid_of,
    unit,
)

PAGE = """---
type: "Concept"
sources: ["summaries/proj_a__REPORT.md", "summaries/proj_b__REPORT.md"]
---
# Title

The assay covered 7,609 genes. [src: proj_a]

See also [[summaries/proj_b__REPORT]].

## Literature Context

Related work exists. [PMID 123](url) [src: proj_z]
"""


def test_body_src_ids():
    # frontmatter lists two projects; only proj_a is actually cited in prose,
    # and Literature Context (external papers) is excluded by paragraphs()
    assert body_src_ids(PAGE) == {"proj_a"}
    assert body_src_ids("Claim. [src: a__REPORT, b]") == {"a", "b"}
    assert sid_of("proj_a__REPORT") == "proj_a" and sid_of("pitfalls") == "pitfalls"


def test_cosine():
    a, b = unit([3.0, 4.0]), unit([3.0, 4.0])
    assert abs(cosine(a, b) - 1.0) < 1e-9
    assert abs(cosine(unit([1.0, 0.0]), unit([0.0, 2.0]))) < 1e-9


def _concepts(*cited):
    return [{"stem": f"c{i}", "cited": set(c), "fm": {"sources": []}} for i, c in enumerate(cited)]


def test_merge_candidates():
    m1 = {"m1": [unit([1.0, 0.0]), unit([0.99, 0.14]), unit([0.0, 1.0])]}
    # c0/c1 are near-identical, c2 is orthogonal -> c0/c1 ranks first
    cs = _concepts("a", "b", "c")
    assert [(i, j) for _, _, i, j in merge_candidates(cs, m1, 1, mature=4)] == [(0, 1)]
    # both mature -> skipped even though they are near-identical
    assert merge_candidates(_concepts("abcd", "efgh", "c"), m1, 1, mature=4) == []
    # one mature, one thin -> still in scope (shard absorbed into a hub)
    assert [(i, j) for _, _, i, j in
            merge_candidates(_concepts("abcd", "b", "c"), m1, 1, mature=4)] == [(0, 1)]
    # UNION across models: a second model whose top pair is (0,2) contributes it
    # even though model 1 ranks that pair last. This is the recall fix -- one
    # model buried a confirmed duplicate at rank 518 of 11,628.
    two = {"m1": m1["m1"], "m2": [unit([1.0, 0.0]), unit([0.0, 1.0]), unit([0.99, 0.14])]}
    got = {(i, j) for _, _, i, j in merge_candidates(cs, two, 1, mature=4)}
    assert got == {(0, 1), (0, 2)}


def test_backmerge_candidates():
    cs = [{"stem": "thin", "cited": {"proj_a"}, "fm": {"sources": ["summaries/proj_a__REPORT.md"]}},
          {"stem": "hub", "cited": set("abcd"), "fm": {"sources": []}}]
    cvecs = [unit([1.0, 0.0]), unit([1.0, 0.0])]
    ss = [{"stem": "proj_a__REPORT", "sid": "proj_a", "rel": "summaries/proj_a__REPORT.md"},
          {"stem": "proj_b__REPORT", "sid": "proj_b", "rel": "summaries/proj_b__REPORT.md"},
          {"stem": "proj_c__REPORT", "sid": "proj_c", "rel": "summaries/proj_c__REPORT.md"}]
    svecs = [unit([1.0, 0.0]), unit([0.99, 0.14]), unit([0.0, 1.0])]
    got = backmerge_candidates(cs, cvecs, ss, svecs, 0.85, topk=2, mature=4)
    # the mature concept is not offered anything; proj_a is already integrated,
    # proj_c is below threshold -> only thin+proj_b survives
    assert [(cs[i]["stem"], ss[j]["sid"]) for _, i, j in got] == [("thin", "proj_b")]


def test_both_mature():
    """Regression: phase_merge re-keys a pair through the redirect map when one
    side was already merged away. Checking maturity only at candidate-generation
    time let a (thin, mature) pair become (mature, mature) after re-keying, and
    it merged a 28-project concept into a 32-project one. Both call sites now
    share this predicate, so the rule cannot hold in one place and not the other."""
    thin, hub, other_hub = set("ab"), set("abcdefgh"), set("ijklmnop")
    assert both_mature(hub, other_hub, 4) is True      # never merge two hubs
    assert both_mature(thin, hub, 4) is False          # shard into hub is fine
    assert both_mature(thin, thin, 4) is False
    # the exact shape of the bug: a thin page redirected onto a hub
    redirected = hub                                    # 'thin' merged into 'hub' earlier
    assert both_mature(redirected, other_hub, 4) is True
    # boundary: mature is inclusive
    assert both_mature(set("abcd"), set("efgh"), 4) is True
    assert both_mature(set("abc"), set("efgh"), 4) is False


def test_rewrite_concept_links():
    text = ("Prose about [[concepts/loser]] and [[concepts/loser|the old name]].\n"
            "- [[concepts/survivor]] — reason\n"
            "- [[concepts/loser]] — reason\n"
            "- [[concepts/survivor]] — reason\n"
            "Untouched: [[concepts/loser-adjacent]] and [[entities/loser]].\n")
    out = rewrite_concept_links(text, "loser", "survivor")
    assert "[[concepts/loser]]" not in out
    assert "[[concepts/survivor|the old name]]" in out
    # the line that became an exact duplicate is dropped, one copy kept
    assert out.count("- [[concepts/survivor]] — reason\n") == 1
    # a longer slug sharing the prefix, and another namespace, are left alone
    assert "[[concepts/loser-adjacent]]" in out and "[[entities/loser]]" in out
    assert rewrite_concept_links("nothing here", "loser", "survivor") == "nothing here"


def test_padding_gate():
    """The v3 regression: a rewrite that name-drops the project without citing
    it must not count as evidence. This is the check phase_backmerge applies."""
    padded = "# T\n\nOld claim. [src: proj_a]\n\nSee also: [[summaries/proj_b__REPORT]]\n"
    real = "# T\n\nOld claim. [src: proj_a]\n\nThis **refines** it: n=42. [src: proj_b]\n"
    assert "proj_b" not in body_src_ids(padded)      # discarded
    assert "proj_b" in body_src_ids(real)            # accepted
    # and neither may drop the citation the page already had
    assert "proj_a" in body_src_ids(padded) and "proj_a" in body_src_ids(real)


if __name__ == "__main__":
    test_body_src_ids()
    test_cosine()
    test_merge_candidates()
    test_both_mature()
    test_backmerge_candidates()
    test_rewrite_concept_links()
    test_padding_gate()
    print("test_consolidate: all checks passed")
