---
type: "Concept"
description: "Row-wise pandas iteration over large genomic tables has been reported to run for long periods without completing, while vectorized merges finished the same operations in seconds."
sources: ["summaries/pitfalls.md"]
---
# Row-Wise Iteration Versus Vectorized Merges in Large Genomic DataFrame Operations

Row-wise iteration means a Python-level loop that handles one row at a time, such as pandas `iterrows()` or `df.apply(..., axis=1)`. The pitfalls digest reports cases where this kind of loop, run over large genomic tables, did not finish within long observation windows, while a vectorized join finished the same operation quickly. These are individual incidents, not controlled benchmarks, so each runtime contrast below is a single reported case [src: pitfalls]. See also [[concepts/join-strategy-and-table-partitioning-cost]] and [[concepts/long-running-analysis-execution-reliability]].

## The Gene-Neighborhood Case

Stage 6 of the gene-neighborhood pipeline (NB26e) used `for _, row in focal_features.iterrows()` with a per-row groupby lookup over 27K focal features × 218K contigs. The loop ran 30+ minutes without completing [src: pitfalls].

The source gives no completed runtime for the row-wise version. It records only that the loop ran for more than 30 minutes without completing. Whether it would eventually have finished is not established [src: pitfalls].

The workaround was a vectorized merge, `pd.merge(focal_features, contig_features, on="contig_id")`, followed by a boolean filter on the merged frame. With this change the same operation completed in ~10 seconds [src: pitfalls]. This **supports** the page's central claim with a direct before/after report from one pipeline stage. The source does not say how many times each version was run [src: pitfalls].

## The Key-Pair Filtering Case

The core_gene_tradeoffs project reports a second instance of the same pattern. Filtering a 961K-row DataFrame with `df.apply(lambda r: (r['orgId'], r['locusId']) in some_set, axis=1)` was extremely slow because it iterates row-by-row in Python. Replacing it with `df.merge(keys_df, on=['orgId','locusId'], how='inner')` gave the same result in seconds instead of minutes [src: pitfalls]. This **supports** the gene-neighborhood observation in a separate analysis context. The source presents the fix as general, applying whenever a large DataFrame has to be filtered to rows matching a set of key pairs. The reported runtimes are qualitative ("seconds instead of minutes"), not exact timings [src: pitfalls].

## Generalization and Its Evidential Status

The source states a generalizable rule: never use iterrows() for >10K rows, and vectorize instead via merge plus boolean filter or numpy array operations. It also asserts that "the 1000× speedup is consistent across pandas use cases" [src: pitfalls]. This page treats the rule as practical guidance. The 1000× figure and its claimed consistency remain an unverified source assertion that the documented incidents do not demonstrate. One incident has no completed row-wise runtime, so no ratio can be computed from it, and the other reports only "seconds instead of minutes". The broader claim should therefore be read as a hypothesis, not an established finding [src: pitfalls].

## Tensions

The digest presents the 1000× speedup as consistent across pandas use cases, but its own documented cases cannot confirm that size of effect. In the gene-neighborhood case the row-wise loop ran 30+ minutes without completing, against ~10 seconds for the vectorized version. In the key-pair case the contrast is reported only as "seconds instead of minutes". Across the two cases the corpus records which way the effect goes but has not measured how large it is, and this page neither adopts nor rejects the 1000× figure [src: pitfalls].

## Open Directions

- Re-run the NB26e Stage 6 `iterrows()` loop to completion, or on stratified subsamples of focal features, and time it against the vectorized `pd.merge` version. This would replace the incomplete run with a measured ratio and test the asserted 1000× speedup [src: pitfalls].
- Time the core_gene_tradeoffs row-wise `apply` filter against the key-pair `merge` on the same DataFrame. This would replace the qualitative "seconds instead of minutes" with exact runtimes [src: pitfalls].
- Benchmark row-wise and vectorized implementations across a range of row counts that brackets the source's >10K-row threshold. This would show whether that cutoff is a real change point in cost or only a rule of thumb [src: pitfalls].
- Audit corpus notebooks for remaining `iterrows()` or `apply(axis=1)` calls over large tables, and log any that coincide with stalled or timed-out jobs. This would test whether the pattern contributes to failures discussed in [[concepts/long-running-analysis-execution-reliability]] [src: pitfalls].
