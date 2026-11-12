---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1, why do transposon-insertion fitness calls disagree so strongly with complete-deletion essentiality in rich medium? Do insertions leave partly functional gene products, or does something else explain the mismatch?"
hypothesis: "Genes lethal when fully deleted but tolerated by transposon insertion carry their insertions mostly near the 3' end or between domains, leaving a truncated protein that still works. Insertions in the same genes placed early in the coding sequence should reproduce the lethality."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Both assay datasets exist for ADP1, but insertion-level positions and the early-insertion strains are not confirmed as available in the lakehouse."
collections: []
findings: ["adp1_triple_essentiality--b191b064", "adp1_triple_essentiality--73c3cad3"]
conflicts: []
papers: ["18319726", "25968644", "41006282"]
builds_on: ["findings/adp1_triple_essentiality--b191b064", "findings/adp1_triple_essentiality--73c3cad3"]
projects: ["adp1_triple_essentiality"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do partly working truncated proteins let transposon screens miss knockout-lethal ADP1 genes?

In Acinetobacter baylyi ADP1, why do transposon-insertion fitness calls disagree so strongly with complete-deletion essentiality in rich medium? Do insertions leave partly functional gene products, or does something else explain the mismatch?

## Hypothesis

Genes lethal when fully deleted but tolerated by transposon insertion carry their insertions mostly near the 3' end or between domains, leaving a truncated protein that still works. Insertions in the same genes placed early in the coding sequence should reproduce the lethality.

## Why it matters

Transposon screens underpin essential-gene lists across many bacteria. If truncation is the main cause of misses, essential-gene catalogues are systematically biased toward genes with tolerable C-terminal truncations, and screens could be redesigned to account for this.

## How to test it

Using the ADP1 rich-medium datasets, map each insertion position and the retained protein domains for genes lethal when deleted but called dispensable by transposon screening. Compare against genes where the two assays agree. Then build a small set of early-position insertions and full deletions for about 20 discordant genes and compare growth in rich medium.

## What would support or refute it

Support: discordant genes have insertions concentrated late in the gene or after the key domains, and early insertions are lethal. Refute: insertion positions look like those of concordant genes and early insertions are also tolerated, which points to other explanations such as fitness costs without lethality.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Both assay datasets exist for ADP1, but insertion-level positions and the early-insertion strains are not confirmed as available in the lakehouse.

## Builds on

- Finding: [[findings/adp1_triple_essentiality--b191b064|RB-TnSeq thresholds all disagree with knockout essentiality in rich medium]] (Insufficient literature evidence)
- Finding: [[findings/adp1_triple_essentiality--73c3cad3|Continuous fitness predicts knockout essentiality; essentiality fraction does worse than random]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 41006282](https://pubmed.ncbi.nlm.nih.gov/41006282/) Accurate prediction of gene deletion phenotypes with Flux Cone Learning.

PMID 18319726 built the ADP1 deletion collection but did not examine why transposon screens disagree with it, and PMID 25968644 describes the transposon method without testing partial-function insertions.
