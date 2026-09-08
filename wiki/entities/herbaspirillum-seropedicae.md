---
type: Organism
description: Herbaspirillum seropedicae evaluated for annotation-gap resolution.
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
title: Herbaspirillum seropedicae
---
# Herbaspirillum seropedicae

## Identity

**Canonical name:** Herbaspirillum seropedicae. [^annotation_gap_discovery]

**Known alias:** HerbieS. [^annotation_gap_discovery]

**Stable external identifier:** No stable external identifier was reported in the source document. [^annotation_gap_discovery]

Herbaspirillum seropedicae is an organism used in the cross-source annotation-gap evaluation described in [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md). [^annotation_gap_discovery]

## Role in annotation-gap discovery

The study evaluated Herbaspirillum seropedicae across gapfilled metabolic-model reactions, carbon-source fitness measurements from [kescience-fitnessbrowser](kescience-fitnessbrowser.md), pangenome annotations, [gapmind](gapmind.md) pathway evidence, and sequence homology. [^annotation_gap_discovery]

Its analysis included 17 gapfilled reaction-organism pairs, of which 10 were resolved, yielding a resolution rate of 58.8%. [^annotation_gap_discovery]

This organism was one of 14 organisms selected because they had rich carbon-source random-barcode transposon sequencing (RB-TnSeq) data, a method for measuring genome-wide mutant fitness with barcoded transposon libraries. [^annotation_gap_discovery]

The organism-level result contributed to the study's cross-organism evidence triangulation framework, which combined [modelseed](modelseed.md) gapfilling, [cobrapy](cobrapy.md)-based flux-balance analysis, fitness evidence, pangenome conservation, gene annotations, and BLAST homology. [^annotation_gap_discovery]

## Interpretation

Herbaspirillum seropedicae had a higher annotation-gap resolution rate than the study-wide overall rate of 47.8%, although the source did not establish that this difference was statistically significant. [^annotation_gap_discovery]

The study associated higher resolution in some organisms with better-annotated reference genomes and stronger Fitness Browser coverage, but it did not provide an organism-specific causal analysis for Herbaspirillum seropedicae. [^annotation_gap_discovery]

## Related pages

- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — source report describing the organism's annotation-gap evaluation. [^annotation_gap_discovery]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — cross-organism gapfilling and candidate-gene assignment framework. [^annotation_gap_discovery]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — carbon-source-specific fitness evidence used in the analysis. [^annotation_gap_discovery]
- [pangenome-integration](../concepts/pangenome-integration.md) — pangenome conservation evidence used for candidate assignment. [^annotation_gap_discovery]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — integration of sequence, annotation, fitness, pathway, and model evidence. [^annotation_gap_discovery]

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
