---
type: "Method"
description: "Python framework for constructing and analyzing constraint-based metabolic models"
sources: ["summaries/annotation_gap_discovery__REPORT.md"]
---
# COBRApy

## What this entity is

**Canonical name:** COBRApy. [src: annotation_gap_discovery]

**Type:** Method. [src: annotation_gap_discovery]

**Known aliases:** No additional alias was reported in the source. [src: annotation_gap_discovery]

**Stable external identifier:** None was reported in the source. [src: annotation_gap_discovery]

COBRApy is a Python framework used to construct and analyze constraint-based metabolic models, including models evaluated with flux-balance analysis (FBA), a method for predicting metabolic flux and growth. [src: annotation_gap_discovery]

## Use in annotation-gap discovery

The study used COBRApy with ModelSEED and RAST annotations to build draft metabolic models for 14 Fitness Browser organisms across 18 carbon sources. [src: annotation_gap_discovery]

Across 574 organism–carbon-source combinations, baseline FBA achieved 42.5% overall accuracy, with recall of 86.5% (244 of 282 growth-positive conditions correctly predicted) and precision of 42.5% (244 of 574 growth predictions correct). [src: annotation_gap_discovery]

The baseline models produced 330 false positives, and conditional gapfilling for 38 false-negative cases added 219 reactions: 201 enzymatic, 14 transport, and 12 exchange, averaging 5.8 reactions per case. [src: annotation_gap_discovery]

The gapfilling workflow used default ModelSEED gapfilling alongside COBRApy-based model analysis; the report cautions that gapfilling is non-unique because multiple valid reaction sets may solve a false-negative case, and that minimizing the number of added reactions does not guarantee biological optimality. [src: annotation_gap_discovery]

For validation, 23 gene-protein-reaction (GPR) rules—formal links between genes and reactions—were inserted into SBML models for high- and medium-confidence candidates. [src: annotation_gap_discovery]

Gene-knockout simulations produced zero wildtype growth on minimal carbon-source media, but this validation was inconclusive because the models required the gapfilled reactions themselves to grow on those carbon sources, making the knockout test circular. [src: annotation_gap_discovery]

## Relation to the wider study

COBRApy provided the model-construction and FBA analysis layer in an evidence-triangulation pipeline that combined metabolic-model gapfilling with [[entities/modelseed]], [[entities/rast]], [[entities/tnseq]], pangenome annotations, GapMind pathway evidence, and BLAST homology. [src: annotation_gap_discovery]

This use of COBRApy supports [[concepts/metabolic-model-gapfilling]] by supplying the computational models in which 201 enzymatic reaction–organism gaps were evaluated and 96 (47.8%) received candidate gene assignments. [src: annotation_gap_discovery]

The model-based knockout analysis also relates to [[concepts/gene-essentiality]], while the study's overall results are summarized in [[summaries/annotation_gap_discovery__REPORT]]. [src: annotation_gap_discovery]
