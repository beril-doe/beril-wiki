---
type: "Research direction"
description: "Transposon-based essentiality calls in Acinetobacter baylyi ADP1 agree poorly with complete-knockout calls in rich medium, with low recall and precision. Do insertions in knockout-essential genes leave partly working proteins?"
hypothesis: "Knockout-essential genes that the transposon screen calls dispensable have insertions concentrated near the 3' end or between domains, and truncated versions of such genes support growth when constructed directly."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Insertion positions are not shown in the catalog, and viability of truncation alleles requires new strain construction."
databases: []
tables: []
findings: ["adp1_triple_essentiality--b191b064"]
conflicts: []
papers: ["18319726", "25968644", "29463657"]
builds_on: ["findings/adp1_triple_essentiality--b191b064"]
projects: ["adp1_triple_essentiality"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do transposon insertions miss essential genes because truncated proteins keep function?

Transposon-based essentiality calls in Acinetobacter baylyi ADP1 agree poorly with complete-knockout calls in rich medium, with low recall and precision. Do insertions in knockout-essential genes leave partly working proteins?

## Hypothesis

Knockout-essential genes that the transposon screen calls dispensable have insertions concentrated near the 3' end or between domains, and truncated versions of such genes support growth when constructed directly.

## Why it matters

Support would show that insertion-based essentiality maps under-call essentials that tolerate truncation, and would mark the domains needed for viability. Refutation would push explanations toward condition differences or insertion-mapping error.

## How to test it

For ADP1, take genes that complete knockouts show to be essential in rich medium but that the transposon screen calls dispensable. Map their insertion positions relative to domain boundaries. Then build C-terminal truncations or domain-deletion alleles for a sample of them, with full-gene deletions as controls, and measure growth in the same rich medium.

## What would support or refute it

Support: insertions cluster in tolerated tail regions and the truncation alleles are viable. Refute: insertions are spread through the gene, or truncations that remove the same region are lethal, so the discordance has another cause.

## Data

Approach: experiment. Readiness: needs new measurements. Insertion positions are not shown in the catalog, and viability of truncation alleles requires new strain construction.

## Builds on

- Finding: [[findings/adp1_triple_essentiality--b191b064|RB-TnSeq thresholds all disagree with knockout essentiality in rich medium]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 29463657](https://pubmed.ncbi.nlm.nih.gov/29463657/) The Essential Genome of Escherichia coli K-12.

PMID 18319726 built the complete ADP1 deletion collection and PMID 25968644 introduced barcoded transposon fitness. Neither tests whether partial gene products explain disagreement between the two assays.
