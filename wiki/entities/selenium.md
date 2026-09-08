---
type: Compound
description: Selenium, a metal assessed for microbial fitness and stress specificity.
sources:
- id: metal_fitness_atlas
  resource: ../summaries/metal_fitness_atlas__REPORT.md
  title: metal fitness atlas
- id: metal_specificity
  resource: ../summaries/metal_specificity__REPORT.md
  title: metal specificity
title: Selenium
---
# Selenium

## What it is

Selenium is the canonical compound name used for the metal analyzed in the atlas. [^metal_fitness_atlas]

- Known aliases: none specified in the source.
- Stable external identifier: none provided in the source.

## Evidence from the metal fitness atlas

Selenium had 134 metal-important genes, a core fraction of 0.933, a core-fraction delta of +0.131, an odds ratio of 3.59, and p=2.9e-05. [^metal_fitness_atlas]

This core enrichment contributes to the atlas-wide finding that metal-important genes are predominantly core-genome genes rather than accessory genes, supporting the [metal-cross-resistance](../concepts/metal-cross-resistance.md) model of broadly required metal-stress functions alongside specialized resistance mechanisms. [^metal_fitness_atlas]

Selenium was classified among the essential metals, for which tolerance genes had a mean core-fraction delta of +0.148, nearly double the toxic-metal delta of +0.081; this difference was significant by one-sided Mann-Whitney U testing (U=39, p=0.015). [^metal_fitness_atlas]

Selenium had limited organism coverage: the report identifies selenium among the metals tested in only one or two organisms, so its cross-species pattern may largely reflect the biology of a small number of organisms. [^metal_fitness_atlas]

The selenium result is part of the 559-experiment, 16-metal atlas containing 383,349 gene × metal fitness records across 31 organisms. [^metal_fitness_atlas]

## Specificity across conditions

A separate classification of metal-important records found that 64 of 138 selenium-associated records (46.4%) were metal-specific: they showed significant metal fitness defects but a <5% sick rate across non-metal experiments. [^metal_specificity] This **refines** the atlas-wide core-enrichment result by separating broadly required core functions from a substantial, though not majority, fraction of selenium-associated determinants that appear condition-specific; the fraction is threshold-dependent. [^metal_specificity]

## Related pages

- [metal_fitness_atlas__REPORT](../summaries/metal_fitness_atlas__REPORT.md) — source report for the selenium fitness and conservation statistics.
- [metal_specificity__REPORT](../summaries/metal_specificity__REPORT.md) — source report for metal-specific versus general-stress classification.
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — cross-metal synthesis distinguishing core metal-stress functions from specialized resistance.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — contrasts broad metal fitness defects with condition-specific metal phenotypes.
- [pangenome-integration](../concepts/pangenome-integration.md) — connects metal fitness phenotypes with core and accessory genome structure.

[^metal_fitness_atlas]: [metal fitness atlas](../summaries/metal_fitness_atlas__REPORT.md)
[^metal_specificity]: [metal specificity](../summaries/metal_specificity__REPORT.md)
