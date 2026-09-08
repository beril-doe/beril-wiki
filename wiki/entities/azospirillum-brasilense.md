---
type: Organism
description: Model bacterium used in metabolic, fitness, and ecology studies
sources:
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: bacdive_phenotype_metal_tolerance
  resource: ../summaries/bacdive_phenotype_metal_tolerance__REPORT.md
  title: bacdive phenotype metal tolerance
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: lab_field_ecology
  resource: ../summaries/lab_field_ecology__REPORT.md
  title: lab field ecology
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
title: Azospirillum brasilense
---
# Azospirillum brasilense

## Identity

- **Canonical name:** *Azospirillum brasilense*. [^annotation_gap_discovery]
- **Known alias:** `azobra`. [^annotation_gap_discovery]
- **Stable external identifier:** Not reported in `annotation_gap_discovery`. [^annotation_gap_discovery]

## Role in annotation-gap discovery

*Azospirillum brasilense* was one of 14 organisms evaluated in a study integrating metabolic-model gapfilling, Fitness Browser phenotypes, pangenome annotations, GapMind pathway evidence, and BLAST homology to assign candidate genes to gapfilled reactions. [^annotation_gap_discovery]

The study evaluated 21 gapfilled reaction-organism pairs for *Azospirillum brasilense* and resolved 13 of them, giving a resolution rate of 61.9%. [^annotation_gap_discovery]

The organism's result contributed to the cross-organism analysis of [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md), which found that 96 of 201 gapfilled enzymatic reaction-organism pairs received candidate genes with confidence scoring. [^annotation_gap_discovery]

## Evidence context

The evidence pipeline combined draft-model flux-balance analysis (FBA), a constraint-based method for predicting metabolic flux and growth, with Fitness Browser carbon-source phenotypes, pangenome conservation, pathway-completeness evidence, automated annotations, and sequence homology. [^annotation_gap_discovery]

The study used random-barcode transposon sequencing (RB-TnSeq), a method that measures genome-wide mutant fitness using barcoded transposon libraries, to obtain carbon-source fitness evidence for the selected organisms. [^annotation_gap_discovery]

These findings support [pangenome-integration](../concepts/pangenome-integration.md) by using cross-organism gene-cluster conservation as one evidence stream, and they contribute to [condition-specific-fitness](../concepts/condition-specific-fitness.md) by linking carbon-source fitness patterns to metabolic annotation gaps. [^annotation_gap_discovery]

## Role in metabolic capability-versus-dependency analysis

*Azospirillum brasilense* was one of the 7 Tier 1 organisms with matching GapMind genome data in a comparison of pathway completeness with Fitness Browser fitness evidence; only 7 of the 48 Fitness Browser organisms had matching GapMind data. [^pathway_capability_dependency] This **supports** the existing pathway-completeness context while reinforcing that the comparison is based on a small, model-organism subset rather than broad species coverage. [^pathway_capability_dependency]

The analysis distinguished genomic pathway capability from experimentally observed dependency and found that complete pathways could lack fitness defects under standard conditions, while becoming important under other tested conditions. [^pathway_capability_dependency] This **refines** the organism's GapMind evidence: its predicted pathway completeness should not be treated as proof of constitutive pathway dependence or viability essentiality. [^pathway_capability_dependency]

## Role in metal-tolerance validation and field ecology

*Azospirillum brasilense* was one of 12 organisms representing 6 unique species in a direct Fitness Browser–BacDive validation of phenotype records against genome-based metal-tolerance scores. [^bacdive_phenotype_metal_tolerance]

This refines the organism's evidence context: the validation connected its classical phenotype data to the [metal-fitness-atlas](metal-fitness-atlas.md), but the set was underpowered for broad phenotype associations because all Gram-typed organisms were Gram-negative and the single anaerobe was not interpretable. [^bacdive_phenotype_metal_tolerance] The study therefore does not establish an organism-specific metal-tolerance mechanism for *A. brasilense*; it supports using matched phenotype and genome data while motivating better-controlled, per-metal validation. [^bacdive_phenotype_metal_tolerance]

In the Oak Ridge field-ecology analysis, *Azospirillum* was detected among the 14 Fitness Browser genera found in groundwater communities and showed a marginal positive association with uranium abundance (Spearman rho=+0.20, p=0.042, q=0.077) after Benjamini–Hochberg false-discovery-rate correction. [^lab_field_ecology] This **refines** the organism's metal-tolerance evidence: the direction is consistent with greater abundance under uranium exposure, but the association did not pass the report's q<0.05 threshold and is therefore suggestive rather than established. [^lab_field_ecology] Because 16S amplicon sequencing, a marker-gene method for profiling microbial composition, resolved the field data only to genus level, this result cannot be matched confidently to *A. brasilense* at species or strain level. [^lab_field_ecology]

## Role in essential-metabolome analysis

*Azospirillum brasilense* was one of 7 organisms successfully mapped for a pilot GapMind pathway-completeness analysis, reduced from an underlying collection of 45 essential-gene organisms. [^essential_metabolome] This **supports** the existing metabolic-gapfilling evidence by adding an independent pathway-completeness context, but does not establish that any complete pathway is essential for viability. [^essential_metabolome]

GapMind, a computational pathway-completeness method, predicted 18/18 amino-acid biosynthesis pathways for *A. brasilense* (100%); this was one of 6 organisms with complete coverage in the pilot. [^essential_metabolome] The result **refines** the organism's annotation context because it is computational evidence of pathway completeness rather than experimental confirmation of pathway function or essentiality. [^essential_metabolome]

The pilot's interpretation is limited by its 7-organism sample and by possible missed non-canonical or divergent pathways, so the result should not be generalized to bacteria as a whole. [^essential_metabolome]

## Source

- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — reports the 61.9% resolution rate for *Azospirillum brasilense* and the broader annotation-gap discovery pipeline. [^annotation_gap_discovery]
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) — places *A. brasilense* among the 7 Tier 1 organisms in the pathway capability-versus-dependency analysis. [^pathway_capability_dependency]
- [bacdive_phenotype_metal_tolerance__REPORT](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md) — reports its inclusion in the direct Fitness Browser–BacDive metal-tolerance validation. [^bacdive_phenotype_metal_tolerance]
- [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md) — reports its 18/18 amino-acid pathway completeness in the GapMind pilot. [^essential_metabolome]
- [lab_field_ecology__REPORT](../summaries/lab_field_ecology__REPORT.md) — reports the genus-level Oak Ridge uranium association and its limitations. [^lab_field_ecology]

## Related concepts

- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) [^annotation_gap_discovery][^essential_metabolome]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) [^annotation_gap_discovery][^lab_field_ecology][^pathway_capability_dependency]
- [pangenome-integration](../concepts/pangenome-integration.md) [^annotation_gap_discovery]
- [gene-essentiality](../concepts/gene-essentiality.md) [^pathway_capability_dependency]
- [multi-omics-integration](../concepts/multi-omics-integration.md) [^annotation_gap_discovery]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) [^lab_field_ecology]

[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^bacdive_phenotype_metal_tolerance]: [bacdive phenotype metal tolerance](../summaries/bacdive_phenotype_metal_tolerance__REPORT.md)
[^lab_field_ecology]: [lab field ecology](../summaries/lab_field_ecology__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
