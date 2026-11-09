---
type: "Research direction"
description: "In Acinetobacter baylyi ADP1 rich medium, why do genes that cannot be fully deleted often tolerate transposon insertions? Is it because partly functional truncated proteins survive?"
hypothesis: "Genes lethal when fully deleted but tolerant of transposon insertion carry their insertions mostly near the end of the gene or outside essential protein domains, so a partly functional product remains. Genes with a different pattern of discordance do not."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The decisive step needs new truncation strains and growth measurements, and insertion-level ADP1 transposon data may also not be loaded in the lakehouse."
collections: []
findings: ["adp1_triple_essentiality--b191b064", "adp1_triple_essentiality--73c3cad3"]
conflicts: []
papers: ["18319726", "25968644", "29463657", "25112473"]
builds_on: ["findings/adp1_triple_essentiality--b191b064", "findings/adp1_triple_essentiality--73c3cad3"]
projects: ["adp1_triple_essentiality"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do truncated proteins explain genes lethal when deleted but tolerant of transposon insertion?

In Acinetobacter baylyi ADP1 rich medium, why do genes that cannot be fully deleted often tolerate transposon insertions? Is it because partly functional truncated proteins survive?

## Hypothesis

Genes lethal when fully deleted but tolerant of transposon insertion carry their insertions mostly near the end of the gene or outside essential protein domains, so a partly functional product remains. Genes with a different pattern of discordance do not.

## Why it matters

Transposon screens are the standard way to call essential genes across bacteria. If truncation rescue is common, essential gene sets and the minimal-gene-set picture built from them are systematically too small for some gene classes.

## How to test it

For the ADP1 genes lethal as complete deletions but dispensable by transposon sequencing, map insertion positions against protein domains and gene ends, and compare with genes where both methods agree. Then build truncation alleles for a handful of these genes, delete the tail or domain, and test whether growth in rich medium survives.

## What would support or refute it

Support: discordant genes show insertions concentrated in tails or non-essential regions, and tail-truncated alleles grow. Refutation: insertions fall throughout the gene and truncations are lethal, which would point to other causes such as differences in conditions or fitness effects short of lethality.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The decisive step needs new truncation strains and growth measurements, and insertion-level ADP1 transposon data may also not be loaded in the lakehouse.

## Builds on

- Finding: [[findings/adp1_triple_essentiality--b191b064|RB-TnSeq thresholds all disagree with knockout essentiality in rich medium]] (Insufficient literature evidence)
- Finding: [[findings/adp1_triple_essentiality--73c3cad3|Continuous fitness predicts knockout essentiality; essentiality fraction does worse than random]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 29463657](https://pubmed.ncbi.nlm.nih.gov/29463657/) The Essential Genome of Escherichia coli K-12.
- [PMID 25112473](https://pubmed.ncbi.nlm.nih.gov/25112473/) Towards an informative mutant phenotype for every bacterial gene.

PMID 18319726 built the ADP1 complete deletion collection and PMID 25968644 introduced barcoded transposon fitness. Neither explains the disagreement between the two assays gene by gene.
