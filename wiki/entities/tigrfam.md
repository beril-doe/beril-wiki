---
type: Dataset
description: TIGRFam annotation dataset used for fitness-module predictions
sources:
- id: fitness_modules
  resource: ../summaries/fitness_modules__REPORT.md
  title: fitness modules
title: TIGRFam
---
# TIGRFam

## What this entity is

**Canonical name:** TIGRFam.  
**Known aliases:** None stated in the source.  
**Stable external identifier:** None reported in the source. [^fitness_modules]

TIGRFam was one of the annotation sources used alongside KEGG, SEED, and PFam to generate function predictions from fitness modules. [^fitness_modules]

## Key facts from fitness_modules

The report used TIGRFam enrichment to support function predictions for hypothetical proteins across 32 organisms, contributing to a total of 6,691 predictions. [^fitness_modules]

Of the 6,691 hypothetical-protein predictions, 2,455 were family-backed predictions, representing 37% of the total and carrying cross-organism conservation support; the source does not provide a TIGRFam-specific count within these categories. [^fitness_modules]

TIGRFam was applied in a workflow where [independent component analysis](independent-component-analysis.md) identified process-level fitness modules, while sequence-based ortholog transfer remained substantially stronger for predicting specific molecular functions. [^fitness_modules]

The report cautions that module-based predictions should be interpreted as biological-process context rather than definitive gene-level function assignments, because Module-ICA had less than 1% strict precision for KEGG KO assignments. [^fitness_modules]

## Related pages

- [fitness_modules__REPORT](../summaries/fitness_modules__REPORT.md) — source summary for the TIGRFam-enabled fitness-module analysis. [^fitness_modules]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — cofitness modules and their process-level annotation context. [^fitness_modules]
- [pangenome-integration](../concepts/pangenome-integration.md) — cross-organism ortholog alignment and conserved module families. [^fitness_modules]

[^fitness_modules]: [fitness modules](../summaries/fitness_modules__REPORT.md)
