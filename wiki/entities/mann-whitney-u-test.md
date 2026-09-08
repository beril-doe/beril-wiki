---
type: Method
description: Statistical method for rank-based comparisons of cofitness and pathway
  completeness
sources:
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Mann-Whitney U Test
---
# Mann-Whitney U Test

## What this entity is

The canonical name is Mann-Whitney U test, a statistical method used in the report to test whether within-module cofitness was elevated relative to background cofitness. [^fitness_modules]

Known alias: Wilcoxon rank-sum test. [^fitness_modules]

No stable external identifier is specified in the source document. [^fitness_modules]

## Key facts from fitness_modules

The report identified 1,116 stable independent-component-analysis modules across 32 organisms, with each organism represented by at least 100 experiments. [^fitness_modules]

The Mann-Whitney U test found significantly elevated within-module cofitness in 94.2% of the modules at p < 0.05. [^fitness_modules]

Across the modules, within-module mean absolute correlation was 0.34 versus 0.12 in the background, corresponding to a 2.8x correlation enrichment. [^fitness_modules]

These results support the interpretation that the ICA modules capture biologically coherent co-regulated groups, while the test evaluates enrichment of cofitness rather than assigning precise gene-level molecular functions. [^fitness_modules]

## Application in pseudomonas_carbon_ecology

The new report **refines** the method’s documented use by applying it to pathway-completeness distributions: 43 of 62 carbon pathways differed between the *Pseudomonas* s.s. and *Pseudomonas_E* groups after Benjamini-Hochberg false-discovery-rate correction at q < 0.05. [^pseudomonas_carbon_ecology] This extends the test from cofitness enrichment to nonparametric comparison of predicted metabolic capabilities, rather than contradicting its earlier use. [^pseudomonas_carbon_ecology]

The cofitness-module findings extend [cofitness-network-architecture](../concepts/cofitness-network-architecture.md), and the source summary is [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md). [^fitness_modules] The carbon-pathway application is summarized in [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md). [^pseudomonas_carbon_ecology]

## Related pages

- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — cross-project synthesis of cofitness network structure.
- [gene-essentiality](../concepts/gene-essentiality.md) — distinguishes process-level module context from gene-level function prediction.
- [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md) — summary of the source report.
- [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md) — application to carbon-pathway comparisons.

[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
