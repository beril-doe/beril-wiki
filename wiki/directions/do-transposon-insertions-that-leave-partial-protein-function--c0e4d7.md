---
type: "Research direction"
description: "Why do transposon screening and complete gene deletion call different genes essential in Acinetobacter baylyi ADP1, and does tolerance of partly working proteins explain the gap?"
hypothesis: "Genes that deletion calls essential but transposon screening calls dispensable carry insertions concentrated at gene ends or between domains, so truncated proteins keep enough function to grow."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The catalog did not show ADP1 insertion positions or deletion calls as tables, and partial alleles would need to be built; Fitness Browser tables support only the cross-organism comparison."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.genefitness"]
findings: ["adp1_triple_essentiality--3264ac68", "adp1_triple_essentiality--1473af9a", "acinetobacter_adp1_explorer--6f19fce6"]
conflicts: []
papers: ["18319726", "25374488", "25968644"]
builds_on: ["findings/adp1_triple_essentiality--3264ac68", "findings/adp1_triple_essentiality--1473af9a", "findings/acinetobacter_adp1_explorer--6f19fce6"]
projects: ["acinetobacter_adp1_explorer", "adp1_triple_essentiality"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do transposon insertions that leave partial protein function explain disagreement with clean deletions in ADP1?

Why do transposon screening and complete gene deletion call different genes essential in Acinetobacter baylyi ADP1, and does tolerance of partly working proteins explain the gap?

## Hypothesis

Genes that deletion calls essential but transposon screening calls dispensable carry insertions concentrated at gene ends or between domains, so truncated proteins keep enough function to grow.

## Why it matters

If true, transposon essentiality calls would be known to undercall genes with separable domains, and fitness from such screens should not be read as lethality without insertion-position checks.

## How to test it

Take the ADP1 genes where deletion says essential but transposon screening says dispensable (211 genes) and the reverse set (293 genes). Map insertion positions inside each gene. As a cross-organism comparison, use Fitness Browser gene coordinates and fitness values to see whether essential-like genes with weak fitness effects are short or have insertions only near gene ends. Then build partial alleles for a panel of the first group and test growth on the knockout-collection medium.

## What would support or refute it

Support: insertions in the first group sit near the 3' end or in linker regions, and partial alleles grow. Refute: insertions are spread evenly and partial alleles fail, which would point to condition or noise differences instead.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The catalog did not show ADP1 insertion positions or deletion calls as tables, and partial alleles would need to be built; Fitness Browser tables support only the cross-organism comparison.

## Builds on

- Finding: [[findings/adp1_triple_essentiality--3264ac68|RB-TnSeq systematically disagrees with knockout essentiality in ADP1]] (Insufficient literature evidence)
- Finding: [[findings/adp1_triple_essentiality--1473af9a|Continuous fitness predicts essentiality; essentiality fraction is worse than random]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--6f19fce6|FBA and TnSeq essentiality calls agree for most ADP1 genes]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

18319726 built the ADP1 deletion collection and 25374488 profiled it with multiomics; neither tests whether insertion position explains disagreement with transposon calls.
