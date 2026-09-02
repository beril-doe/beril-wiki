---
type: "Method"
description: "Automated genome-annotation system used to build draft metabolic models"
sources: ["summaries/annotation_gap_discovery__REPORT.md"]
---
# RAST

## What this entity is

**Canonical name:** RAST automated genome-annotation system. [src: annotation_gap_discovery]

**Known alias:** RAST. [src: annotation_gap_discovery]

**Stable external identifier:** Not reported in the source document. [src: annotation_gap_discovery]

RAST is an automated genome-annotation system whose annotations were used as a basis for draft metabolic models in the annotation-gap study. [src: annotation_gap_discovery]

## Key facts from the study

Draft metabolic models for 14 Fitness Browser organisms were built from ModelSEED/RAST annotations and COBRApy, with [[entities/modelseed]] and [[entities/cobrapy]] providing related modeling components. [src: annotation_gap_discovery]

The models were evaluated with flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth. [src: annotation_gap_discovery]

Across 574 organism–carbon source combinations, baseline FBA achieved 42.5% overall accuracy, recalled 244 of 282 growth-positive conditions for a recall of 86.5%, and produced 330 false positives. [src: annotation_gap_discovery]

The report attributes systematic errors in the draft models to automated RAST annotations and describes the baseline models as overly permissive because they predicted growth on carbon sources the organisms could not use. [src: annotation_gap_discovery]

The RAST-based draft models were subsequently integrated with Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to investigate [[concepts/metabolic-model-gapfilling]] and annotation gaps. [src: annotation_gap_discovery]

## Related pages

- [[summaries/annotation_gap_discovery__REPORT]] — source summary for the annotation-gap discovery study. [src: annotation_gap_discovery]
- [[concepts/metabolic-model-gapfilling]] — concept page covering the gapfilling and model-integration findings. [src: annotation_gap_discovery]
- [[concepts/multi-omics-integration]] — concept page covering integration of model, sequence, annotation, pathway, and fitness evidence. [src: annotation_gap_discovery]
- [[entities/modelseed]] — related metabolic-model reconstruction resource. [src: annotation_gap_discovery]
- [[entities/cobrapy]] — related constraint-based modeling software. [src: annotation_gap_discovery]
- [[entities/flux-balance-analysis]] — method used to evaluate the draft models. [src: annotation_gap_discovery]
