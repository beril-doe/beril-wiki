---
type: "Research direction"
description: "Are genes that are costly in the lab yet core in the pangenome kept by purifying selection in conditions the lab omits, or is the pattern produced by gene length, callability and shared ancestry?"
hypothesis: "A substantial share of the 28,017 costly-and-conserved genes give benefit under soil, biofilm or host-like conditions. Their burden and core status are not explained by gene length or insertion callability."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The covariate analysis uses existing data, but the natural-proxy conditions are not in the Fitness Browser."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["conservation_fitness_synthesis--b05bd909", "conservation_fitness_synthesis--d115e8ed", "core_gene_tradeoffs--c29ab7fa", "field_vs_lab_fitness--d31622df", "fitness_effects_conservation--6e6a4a45"]
conflicts: ["conflict--laboratory-fitness-versus-natural-selection--239d08e3"]
papers: ["22761588", "29769716", "38948139", "25894004"]
builds_on: ["findings/conservation_fitness_synthesis--b05bd909", "findings/conservation_fitness_synthesis--d115e8ed", "findings/core_gene_tradeoffs--c29ab7fa", "findings/field_vs_lab_fitness--d31622df", "findings/fitness_effects_conservation--6e6a4a45", "conflicts/conflict--laboratory-fitness-versus-natural-selection--239d08e3"]
projects: ["conservation_fitness_synthesis", "conservation_vs_fitness", "core_gene_tradeoffs", "field_vs_lab_fitness", "fitness_effects_conservation"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do costly but conserved genes persist because natural environments reward them?

Are genes that are costly in the lab yet core in the pangenome kept by purifying selection in conditions the lab omits, or is the pattern produced by gene length, callability and shared ancestry?

## Hypothesis

A substantial share of the 28,017 costly-and-conserved genes give benefit under soil, biofilm or host-like conditions. Their burden and core status are not explained by gene length or insertion callability.

## Why it matters

It would separate real trade-offs from measurement artifacts. That decides whether lab fitness can be used to infer selection in nature.

## How to test it

First, add gene length, insertion density and phylogeny as covariates in per-organism models of core status for the costly-conserved and costly-dispensable classes. In DvH, adding length raised CV-AUC from 0.517-0.548 to 0.645. Then run RB-TnSeq (random barcode transposon sequencing) in a few Fitness Browser organisms under soil-extract, biofilm and host-mimic conditions. Test whether genes with fit>1 in rich media shift to fit<-1, focusing on motility (+7.8pp) and RNA metabolism (+12.9pp), where the core-burden excess is largest.

## What would support or refute it

Support: the burden excess persists after covariates and many burdensome core genes become important in natural-proxy conditions. Refute: the excess vanishes after length and callability adjustment, or the genes stay dispensable in the new conditions.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The covariate analysis uses existing data, but the natural-proxy conditions are not in the Fitness Browser.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/conservation_fitness_synthesis--b05bd909|Lab-costly but conserved genes suggest purifying selection in nature]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--d115e8ed|The core-burden excess is driven by specific functional categories]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--c29ab7fa|Trade-off genes are enriched among core genes]] (Insufficient literature evidence)
- Finding: [[findings/field_vs_lab_fitness--d31622df|Gene length is judged a stronger predictor of core status than fitness]] (Insufficient literature evidence)
- Finding: [[findings/fitness_effects_conservation--6e6a4a45|Core genes are more often beneficial to delete than auxiliary genes]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--laboratory-fitness-versus-natural-selection--239d08e3|Does the essential-gene conservation gradient survive adjustment for gene length and scope?]]

## Closest published work

- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 25894004](https://pubmed.ncbi.nlm.nih.gov/25894004/) Evolutionary Conservation of Bacterial Essential Metabolic Genes across All Bacterial Culture Media.

PMID 38948139 links fitness genes to core membership in one rich medium and PMID 25894004 notes condition dependence; neither tests whether lab-costly core genes pay off in natural-proxy conditions.
