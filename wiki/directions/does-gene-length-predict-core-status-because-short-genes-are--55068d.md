---
type: "Research direction"
description: "Gene length predicts whether a gene is core better than laboratory fitness does. Is that because short genes are recent arrivals, or only because short genes get fewer transposon insertions?"
hypothesis: "Short genes are enriched among recent gains, so length predicts core status through gene age even where insertions are plentiful. Among genes of similar estimated age, length adds little."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Family taxonomic breadth must be computed from cluster membership and is not a ready table."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome", "kbase-uniref"]
findings: ["field_vs_lab_fitness--d31622df", "field_vs_lab_fitness--73215ec1"]
conflicts: ["conflict--transposon-callability-bias--4e810812"]
papers: ["38977308", "37065130", "29769716", "36097170"]
builds_on: ["findings/field_vs_lab_fitness--d31622df", "findings/field_vs_lab_fitness--73215ec1", "conflicts/conflict--transposon-callability-bias--4e810812"]
projects: ["field_vs_lab_fitness", "metal_specificity"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Does gene length predict core status because short genes are young?

Gene length predicts whether a gene is core better than laboratory fitness does. Is that because short genes are recent arrivals, or only because short genes get fewer transposon insertions?

## Hypothesis

Short genes are enriched among recent gains, so length predicts core status through gene age even where insertions are plentiful. Among genes of similar estimated age, length adds little.

## Why it matters

It separates a real evolutionary pattern, that new genes are short and short-lived, from a measurement artifact. That changes whether fitness data can say anything about conservation.

## How to test it

In Fitness Browser organisms linked to the Pangenome Collection, estimate gene age from the taxonomic breadth of each gene's family, using UniRef Clusters membership and pangenome species placement. Fit core status on length, age and insertion density together, and ask whether length still predicts core status among genes with dense insertion coverage and matched age.

## What would support or refute it

Support: the length effect vanishes or shrinks within age bins, and age tracks length. Refutation: length keeps predicting core status within age bins and with dense coverage, pointing to a length-linked selection pressure.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Family taxonomic breadth must be computed from cluster membership and is not a ready table.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/field_vs_lab_fitness--d31622df|Gene length is judged a stronger predictor of core status than fitness]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--73215ec1|No significant correlation between module field activity and conservation]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--transposon-callability-bias--4e810812|Does Excluding Putative Essential Genes Raise or Lower the Baseline Core Fraction?]]

## Closest published work

- [PMID 38977308](https://pubmed.ncbi.nlm.nih.gov/38977308/) Large-scale investigation of species-specific orphan genes in the human gut microbiome elucidates their evolutionary origins.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.

PMID 38977308 compares orphan and conserved genes on codon use and disorder but not length against core status. PMID 37065130 profiled Desulfovibrio vulgaris Hildenborough fitness at scale without testing this.
