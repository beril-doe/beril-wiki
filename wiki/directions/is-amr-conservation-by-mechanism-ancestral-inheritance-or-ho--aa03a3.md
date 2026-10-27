---
type: "Research direction"
description: "Resistance mechanism does not predict knockout fitness cost, yet it strongly predicts core versus accessory status. Do mechanism classes differ in ancestral inheritance versus horizontal acquisition?"
hypothesis: "Mechanism classes that are mostly core (intrinsic efflux, chromosomal beta-lactamases) are distributed congruently with species phylogeny, whereas mostly non-core classes (blaTEM, tet(C), ant(2'')-Ia) are patchy across relatives. Baseline cost adds no explanatory power for either pattern."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Mechanism labels, core status and fitness exist, but a phylogenetic-patchiness measure per AMR cluster must be built."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser"]
findings: ["amr_fitness_cost--104baecc", "amr_fitness_cost--67395444", "amr_fitness_cost--95a8021f", "amr_pangenome_atlas--9947286c"]
conflicts: ["conflict--pangenome-conservation-fitness-decoupling--8173d997"]
papers: ["25861385", "39353488", "20208551", "35873140"]
builds_on: ["findings/amr_fitness_cost--104baecc", "findings/amr_fitness_cost--67395444", "findings/amr_fitness_cost--95a8021f", "findings/amr_pangenome_atlas--9947286c", "conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997"]
projects: ["amr_fitness_cost", "amr_pangenome_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Is AMR conservation by mechanism ancestral inheritance or horizontal transfer, independent of baseline cost?

Resistance mechanism does not predict knockout fitness cost, yet it strongly predicts core versus accessory status. Do mechanism classes differ in ancestral inheritance versus horizontal acquisition?

## Hypothesis

Mechanism classes that are mostly core (intrinsic efflux, chromosomal beta-lactamases) are distributed congruently with species phylogeny, whereas mostly non-core classes (blaTEM, tet(C), ant(2'')-Ia) are patchy across relatives. Baseline cost adds no explanatory power for either pattern.

## Why it matters

It would show that the pangenome distribution of resistance is set by evolutionary origin and transfer rather than by lab-measurable carriage cost. That changes how resistance spread is predicted from genomes.

## How to test it

In the Pangenome Collection, classify AMR clusters by mechanism (the amr_fitness_cost classes: efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) and measure phylogenetic patchiness, meaning presence across distant genera within a clade versus congruence with the species tree. Compare patchiness across mechanisms, with species-stratified models of core status that include genome count. Then test whether Fitness Browser baseline fitness adds any information. Treat the antibiotic-challenged benefit of an AMR gene as a separate quantity from baseline carriage cost. Core calls are imprecise because the median is 9 genomes per species.

## What would support or refute it

Support: core-biased mechanisms show tree-congruent distributions, non-core mechanisms show patchy ones, and baseline cost adds nothing. Refute: patchiness is similar across mechanisms, or the mechanism effect (chi-squared 69.3) disappears under genome-count stratification.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Mechanism labels, core status and fitness exist, but a phylogenetic-patchiness measure per AMR cluster must be built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/amr_fitness_cost--104baecc|Fitness cost does not vary by resistance mechanism]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--67395444|Resistance mechanism predicts conservation status though not fitness cost]] (Candidate novel)
- Finding: [[findings/amr_fitness_cost--95a8021f|Core and accessory AMR genes show identical fitness]] (Candidate novel)
- Finding: [[findings/amr_pangenome_atlas--9947286c|Core versus accessory status of AMR genes depends on resistance mechanism]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--pangenome-conservation-fitness-decoupling--8173d997|Do AMR genes of different pangenome prevalence carry different fitness costs?]]

## Closest published work

- [PMID 25861385](https://pubmed.ncbi.nlm.nih.gov/25861385/) The fitness costs of antibiotic resistance mutations.
- [PMID 39353488](https://pubmed.ncbi.nlm.nih.gov/39353488/) Distribution of tetracyclines and sulfonamides resistance genes around a smallholder pig farm: Modeling and attribution.
- [PMID 20208551](https://pubmed.ncbi.nlm.nih.gov/20208551/) Antibiotic resistance and its cost: is it possible to reverse resistance?
- [PMID 35873140](https://pubmed.ncbi.nlm.nih.gov/35873140/) Comparative Genomic Analysis of the Human Pathogen Wohlfahrtiimonas Chitiniclastica Provides Insight Into the Identification of Antimicrobial Resistance Genotypes and Potential Virulence Traits.

PMID 25861385 and PMID 20208551 address resistance cost by drug class, and PMID 39353488 infers cost differences from spread; none tests whether mechanism predicts conservation through ancestry versus transfer. PMID 35873140 shows only a single-species core/accessory split.
