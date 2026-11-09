---
type: "Research direction"
description: "Why does average protein abundance across Acinetobacter strains predict which ADP1 genes are essential only fairly well? Does abundance track how strongly a gene is needed in the particular condition?"
hypothesis: "Within a single gene, abundance across growth conditions rises when that gene's loss costs more, because cells overproduce proteins whose loss would hurt growth. The genome-wide link between abundance and essentiality is mostly a between-gene effect of housekeeping genes and is weaker within genes."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Existing proteomics are averages over seven Acinetobacter strains, not ADP1 under matched conditions."
collections: []
findings: ["adp1_triple_essentiality--19478689", "adp1_deletion_phenotypes--69241676"]
conflicts: []
papers: ["39253634", "40628805", "32492430", "18319726"]
builds_on: ["findings/adp1_triple_essentiality--19478689", "findings/adp1_deletion_phenotypes--69241676"]
projects: ["adp1_deletion_phenotypes", "adp1_triple_essentiality"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Is a protein's abundance a bet on how much its loss would hurt growth?

Why does average protein abundance across Acinetobacter strains predict which ADP1 genes are essential only fairly well? Does abundance track how strongly a gene is needed in the particular condition?

## Hypothesis

Within a single gene, abundance across growth conditions rises when that gene's loss costs more, because cells overproduce proteins whose loss would hurt growth. The genome-wide link between abundance and essentiality is mostly a between-gene effect of housekeeping genes and is weaker within genes.

## Why it matters

If cells tune abundance to the cost of losing a gene, proteomics could rank conditional gene importance without making mutants. If not, the genome-wide link is only a housekeeping correlation.

## How to test it

Measure ADP1 proteomes on the eight carbon sources already phenotyped in the deletion collection. For each gene, compare abundance across carbon sources with its deletion growth defect on each. Separately compare housekeeping and non-housekeeping genes.

## What would support or refute it

Support: within-gene abundance moves with deletion cost across carbon sources. Refutation: abundance is flat across conditions or unrelated to deletion cost, leaving only the between-gene association.

## Data

Approach: experiment. Readiness: needs new measurements. Existing proteomics are averages over seven Acinetobacter strains, not ADP1 under matched conditions.

## Builds on

- Finding: [[findings/adp1_triple_essentiality--19478689|Protein expression correlates with knockout essentiality and classifies it fairly]] (Candidate novel)
- Finding: [[findings/adp1_deletion_phenotypes--69241676|A third of genes concentrate growth importance on one carbon source]] (Insufficient literature evidence)

## Closest published work

- [PMID 39253634](https://pubmed.ncbi.nlm.nih.gov/39253634/) Protein overabundance is driven by growth robustness.
- [PMID 40628805](https://pubmed.ncbi.nlm.nih.gov/40628805/) Congruence between noise and plasticity in protein expression.
- [PMID 32492430](https://pubmed.ncbi.nlm.nih.gov/32492430/) Inferring Active Metabolic Pathways from Proteomics and Essentiality Data.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 39253634 reports that most essential A. baylyi proteins are overabundant, but it does not test whether abundance tracks condition-specific cost. PMID 18319726 gives the condition-specific deletion phenotypes needed.
