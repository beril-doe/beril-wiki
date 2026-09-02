---
type: "Compound"
description: "Arginine evidence across fitness, utilization, pathway, and community datasets"
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Arginine

## What this entity is

Arginine is the canonical compound name used in the reports and is treated as an amino-acid substrate and metabolite. [src: fw300_metabolic_consistency]

- Known aliases: none reported in the source documents. [src: fw300_metabolic_consistency, nmdc_community_metabolic_ecology]
- Stable external identifier: none reported in the source documents. [src: fw300_metabolic_consistency, nmdc_community_metabolic_ecology]

## Key facts

Arginine increased in the Web of Microbes exometabolome of *Pseudomonas* FW300-N2E3. [src: fw300_metabolic_consistency]

Fitness Browser data associated arginine growth with 270 genes having significant fitness effects. [src: fw300_metabolic_consistency]

BacDive utilization data showed that 40/48 *P. fluorescens* strains utilized arginine, corresponding to 83%. [src: fw300_metabolic_consistency]

GapMind predicted a complete arginine pathway for FW300-N2E3. [src: fw300_metabolic_consistency]

The report identifies arginine as one of three gold-standard cases of four-way consistency across WoM production, Fitness Browser growth, BacDive utilization, and GapMind pathway prediction. [src: fw300_metabolic_consistency]

Arginine was among the metabolites with the largest fitness landscapes in the analysis, alongside carnitine and alanine, while tryptophan had 231 significant genes. [src: fw300_metabolic_consistency]

At community scale, arginine biosynthetic completeness was negatively associated with ambient arginine intensity (r = −0.297, q = 0.049, n = 80), remaining one of two pathways significant after Benjamini-Hochberg false-discovery-rate correction. [src: nmdc_community_metabolic_ecology]

This community result **supports** the earlier experimental and utilization evidence that connects arginine metabolism across datasets, while **refining** the FW300-N2E3 species-level GapMind result into a community-weighted observation. [src: nmdc_community_metabolic_ecology, fw300_metabolic_consistency]

In the Soil-only analysis, the association remained directionally consistent but lost FDR significance (r = −0.264, q = 0.117, n = 78); excluding the 6-sample second study gave arginine r = −0.264, p = 0.019, n = 78. [src: nmdc_community_metabolic_ecology]

The negative association is interpreted as weak support for community-scale Black Queen Hypothesis dynamics, with arginine synthesis reported to require 26 ATP equivalents; expression and abiotic controls remain unresolved. [src: nmdc_community_metabolic_ecology]

Across the broader capability–dependency analysis, arginine biosynthesis had all-gene GapMind completeness of 0.613 and core-only completeness of 0.472, an exact accessory-dependent gap of 0.141. This **refines** the complete FW300-N2E3 pathway result by showing that, across species, arginine pathway completeness can depend partly on genes outside the universally conserved core; the analysis does not demonstrate metabolite exchange. [src: pathway_capability_dependency]

This accessory-dependent pathway evidence **supports** linking arginine to [[concepts/gene-function-acquisition-depth]] and [[concepts/metabolic-model-gapfilling]], while the FW300-N2E3 result remains a species-level case of experimentally supported completeness. [src: pathway_capability_dependency, fw300_metabolic_consistency]

The arginine evidence supports integration across [[entities/web-of-microbes]], [[entities/kescience-fitnessbrowser]], and [[entities/bacdive]] through [[concepts/multi-omics-integration]] and [[concepts/cross-tenant-data-bridging]]. [src: fw300_metabolic_consistency]

The arginine result also contributes to [[concepts/metabolic-model-gapfilling]] because its complete GapMind prediction agreed with experimental growth data, and **extends** that concept to community-weighted pathway completeness. [src: fw300_metabolic_consistency, nmdc_community_metabolic_ecology]

## Source

- [[summaries/fw300_metabolic_consistency__REPORT]] — metabolic consistency analysis for FW300-N2E3. [src: fw300_metabolic_consistency]
- [[summaries/nmdc_community_metabolic_ecology__REPORT]] — NMDC community pathway-completeness and metabolomics analysis. [src: nmdc_community_metabolic_ecology]
- [[summaries/pathway_capability_dependency__REPORT]] — pathway capability, dependency, accessory completeness, and pangenome analysis. [src: pathway_capability_dependency]
