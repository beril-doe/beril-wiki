---
type: Compound
description: Arginine evidence across fitness, utilization, pathway, and community
  datasets
sources:
- id: fw300_metabolic_consistency
  resource: ../summaries/fw300_metabolic_consistency__REPORT.md
  title: fw300 metabolic consistency
- id: nmdc_community_metabolic_ecology
  resource: ../summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
title: Arginine
---
# Arginine

## What this entity is

Arginine is the canonical compound name used in the reports and is treated as an amino-acid substrate and metabolite. [^fw300_metabolic_consistency]

- Known aliases: none reported in the source documents. [^fw300_metabolic_consistency][^nmdc_community_metabolic_ecology]
- Stable external identifier: none reported in the source documents. [^fw300_metabolic_consistency][^nmdc_community_metabolic_ecology]

## Key facts

Arginine increased in the Web of Microbes exometabolome of *Pseudomonas* FW300-N2E3. [^fw300_metabolic_consistency]

Fitness Browser data associated arginine growth with 270 genes having significant fitness effects. [^fw300_metabolic_consistency]

BacDive utilization data showed that 40/48 *P. fluorescens* strains utilized arginine, corresponding to 83%. [^fw300_metabolic_consistency]

GapMind predicted a complete arginine pathway for FW300-N2E3. [^fw300_metabolic_consistency]

The report identifies arginine as one of three gold-standard cases of four-way consistency across WoM production, Fitness Browser growth, BacDive utilization, and GapMind pathway prediction. [^fw300_metabolic_consistency]

Arginine was among the metabolites with the largest fitness landscapes in the analysis, alongside carnitine and alanine, while tryptophan had 231 significant genes. [^fw300_metabolic_consistency]

At community scale, arginine biosynthetic completeness was negatively associated with ambient arginine intensity (r = −0.297, q = 0.049, n = 80), remaining one of two pathways significant after Benjamini-Hochberg false-discovery-rate correction. [^nmdc_community_metabolic_ecology]

This community result **supports** the earlier experimental and utilization evidence that connects arginine metabolism across datasets, while **refining** the FW300-N2E3 species-level GapMind result into a community-weighted observation. [^nmdc_community_metabolic_ecology][^fw300_metabolic_consistency]

In the Soil-only analysis, the association remained directionally consistent but lost FDR significance (r = −0.264, q = 0.117, n = 78); excluding the 6-sample second study gave arginine r = −0.264, p = 0.019, n = 78. [^nmdc_community_metabolic_ecology]

The negative association is interpreted as weak support for community-scale Black Queen Hypothesis dynamics, with arginine synthesis reported to require 26 ATP equivalents; expression and abiotic controls remain unresolved. [^nmdc_community_metabolic_ecology]

Across the broader capability–dependency analysis, arginine biosynthesis had all-gene GapMind completeness of 0.613 and core-only completeness of 0.472, an exact accessory-dependent gap of 0.141. This **refines** the complete FW300-N2E3 pathway result by showing that, across species, arginine pathway completeness can depend partly on genes outside the universally conserved core; the analysis does not demonstrate metabolite exchange. [^pathway_capability_dependency]

This accessory-dependent pathway evidence **supports** linking arginine to [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) and [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md), while the FW300-N2E3 result remains a species-level case of experimentally supported completeness. [^pathway_capability_dependency][^fw300_metabolic_consistency]

The arginine evidence supports integration across [web-of-microbes](web-of-microbes.md), [kescience-fitnessbrowser](kescience-fitnessbrowser.md), and [bacdive](bacdive.md) through [multi-omics-integration](../concepts/multi-omics-integration.md) and [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md). [^fw300_metabolic_consistency]

The arginine result also contributes to [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) because its complete GapMind prediction agreed with experimental growth data, and **extends** that concept to community-weighted pathway completeness. [^fw300_metabolic_consistency][^nmdc_community_metabolic_ecology]

## Source

- [fw300_metabolic_consistency__REPORT](../summaries/fw300_metabolic_consistency__REPORT.md) — metabolic consistency analysis for FW300-N2E3. [^fw300_metabolic_consistency]
- [nmdc_community_metabolic_ecology__REPORT](../summaries/nmdc_community_metabolic_ecology__REPORT.md) — NMDC community pathway-completeness and metabolomics analysis. [^nmdc_community_metabolic_ecology]
- [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md) — pathway capability, dependency, accessory completeness, and pangenome analysis. [^pathway_capability_dependency]

[^fw300_metabolic_consistency]: [fw300 metabolic consistency](../summaries/fw300_metabolic_consistency__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../summaries/nmdc_community_metabolic_ecology__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
