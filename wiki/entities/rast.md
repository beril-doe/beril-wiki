---
type: Method
description: Automated genome-annotation system used to build draft metabolic models
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
title: RAST
---
# RAST

## What this entity is

**Canonical name:** RAST automated genome-annotation system. [^annotation_gap_discovery]

**Known alias:** RAST. [^annotation_gap_discovery]

**Stable external identifier:** Not reported in the source document. [^annotation_gap_discovery]

RAST is an automated genome-annotation system whose annotations were used as a basis for draft metabolic models in the annotation-gap study. [^annotation_gap_discovery]

## Key facts from the study

Draft metabolic models for 14 Fitness Browser organisms were built from ModelSEED/RAST annotations and COBRApy, with [modelseed](modelseed.md) and [cobrapy](cobrapy.md) providing related modeling components. [^annotation_gap_discovery]

The models were evaluated with flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth. [^annotation_gap_discovery]

Across 574 organism–carbon source combinations, baseline FBA achieved 42.5% overall accuracy, recalled 244 of 282 growth-positive conditions for a recall of 86.5%, and produced 330 false positives. [^annotation_gap_discovery]

The report attributes systematic errors in the draft models to automated RAST annotations and describes the baseline models as overly permissive because they predicted growth on carbon sources the organisms could not use. [^annotation_gap_discovery]

The RAST-based draft models were subsequently integrated with Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to investigate [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) and annotation gaps. [^annotation_gap_discovery]

## Related pages

- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — source summary for the annotation-gap discovery study. [^annotation_gap_discovery]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — concept page covering the gapfilling and model-integration findings. [^annotation_gap_discovery]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — concept page covering integration of model, sequence, annotation, pathway, and fitness evidence. [^annotation_gap_discovery]
- [modelseed](modelseed.md) — related metabolic-model reconstruction resource. [^annotation_gap_discovery]
- [cobrapy](cobrapy.md) — related constraint-based modeling software. [^annotation_gap_discovery]
- [flux-balance-analysis](flux-balance-analysis.md) — method used to evaluate the draft models. [^annotation_gap_discovery]

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
