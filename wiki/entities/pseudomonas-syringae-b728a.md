---
type: "Organism"
description: "Pseudomonas syringae B728a in co-fitness and pangenome analyses"
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
---
# Pseudomonas syringae B728a

## What this entity is

**Canonical name:** Pseudomonas syringae B728a. [src: cofitness_coinheritance]

**Known alias:** SyringaeB728a. [src: cofitness_coinheritance]

**Stable external identifier:** Not supplied in this report. [src: cofitness_coinheritance]

## Key facts

Pseudomonas syringae B728a was one of the 9 organisms included in the primary co-fitness and pangenome co-occurrence analysis. [src: cofitness_coinheritance]

The dataset contained 126 genomes, 4,999 pangenome clusters, and 371,004 co-fitness pairs for this organism. [src: cofitness_coinheritance]

Its cofit pairs had a delta phi of +0.006, with 129,385 cofit pairs evaluated, mean phi of 0.049 for cofit pairs, mean phi of 0.043 for prevalence-matched random pairs, and a two-sided Mann–Whitney p-value of 2.9e-4. [src: cofitness_coinheritance]

This result supports the [[concepts/cofitness-network-architecture]] conclusion that pairwise co-fitness can show a positive but weak relationship with gene co-occurrence across pangenomes. [src: cofitness_coinheritance]

The analysis mapped co-fitness pairs from [[entities/kescience-fitnessbrowser]] to pangenome cluster pairs and evaluated binary genome-by-cluster presence vectors using phi coefficients. [src: cofitness_coinheritance]

The organism contributed to an analysis that generated 10 prevalence-matched random pairs per cofit pair, with each cluster’s prevalence matched independently within a tolerance of +/-5%. [src: cofitness_coinheritance]

These data contribute to [[concepts/pangenome-integration]], which links laboratory fitness measurements with pangenome presence–absence variation. [src: cofitness_coinheritance]

The study integrated Fitness Browser, KBase pangenome, phylogenetic-distance, independent-component-analysis module, and SEED annotation data through Spark and linked files, contributing to [[concepts/cross-tenant-data-bridging]]. [src: cofitness_coinheritance]

A separate metabolic capability–dependency analysis included Pseudomonas syringae strains among the organisms with the highest reported proportions of latent, fitness-neutral complete pathways. [src: metabolic_capability_dependency] This **refines** the co-fitness result by showing that B728a’s broader pangenome context can also be examined through the distinction between encoded capability and experimentally measured dependency; the report does not provide a B728a-specific latent fraction. [src: metabolic_capability_dependency]

## Source

- [[summaries/cofitness_coinheritance__REPORT]] — Study summary containing the organism-level co-fitness and co-occurrence results. [src: cofitness_coinheritance]
- [[summaries/metabolic_capability_dependency__REPORT]] — Study summary of metabolic capability, dependency, pangenome openness, and ecotype analyses. [src: metabolic_capability_dependency]
