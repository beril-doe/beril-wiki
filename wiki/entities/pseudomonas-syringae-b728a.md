---
type: Organism
description: Pseudomonas syringae B728a in co-fitness and pangenome analyses
sources:
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Pseudomonas syringae B728a
---
# Pseudomonas syringae B728a

## What this entity is

**Canonical name:** Pseudomonas syringae B728a. [^cofitness_coinheritance]

**Known alias:** SyringaeB728a. [^cofitness_coinheritance]

**Stable external identifier:** Not supplied in this report. [^cofitness_coinheritance]

## Key facts

Pseudomonas syringae B728a was one of the 9 organisms included in the primary co-fitness and pangenome co-occurrence analysis. [^cofitness_coinheritance]

The dataset contained 126 genomes, 4,999 pangenome clusters, and 371,004 co-fitness pairs for this organism. [^cofitness_coinheritance]

Its cofit pairs had a delta phi of +0.006, with 129,385 cofit pairs evaluated, mean phi of 0.049 for cofit pairs, mean phi of 0.043 for prevalence-matched random pairs, and a two-sided Mann–Whitney p-value of 2.9e-4. [^cofitness_coinheritance]

This result supports the [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) conclusion that pairwise co-fitness can show a positive but weak relationship with gene co-occurrence across pangenomes. [^cofitness_coinheritance]

The analysis mapped co-fitness pairs from [kescience-fitnessbrowser](kescience-fitnessbrowser.md) to pangenome cluster pairs and evaluated binary genome-by-cluster presence vectors using phi coefficients. [^cofitness_coinheritance]

The organism contributed to an analysis that generated 10 prevalence-matched random pairs per cofit pair, with each cluster’s prevalence matched independently within a tolerance of +/-5%. [^cofitness_coinheritance]

These data contribute to [pangenome-integration](../concepts/pangenome-integration.md), which links laboratory fitness measurements with pangenome presence–absence variation. [^cofitness_coinheritance]

The study integrated Fitness Browser, KBase pangenome, phylogenetic-distance, independent-component-analysis module, and SEED annotation data through Spark and linked files, contributing to [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^cofitness_coinheritance]

A separate metabolic capability–dependency analysis included Pseudomonas syringae strains among the organisms with the highest reported proportions of latent, fitness-neutral complete pathways. [^metabolic_capability_dependency] This **refines** the co-fitness result by showing that B728a’s broader pangenome context can also be examined through the distinction between encoded capability and experimentally measured dependency; the report does not provide a B728a-specific latent fraction. [^metabolic_capability_dependency]

## Source

- [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) — Study summary containing the organism-level co-fitness and co-occurrence results. [^cofitness_coinheritance]
- [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md) — Study summary of metabolic capability, dependency, pangenome openness, and ecotype analyses. [^metabolic_capability_dependency]

[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
