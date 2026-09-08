---
type: Method
description: Rank-based method used to test metal–gene associations
sources:
- id: soil_metal_functional_genomics
  resource: ../summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
title: Spearman correlation
---
# Spearman correlation

## What it is

**Canonical name:** Spearman correlation. **Known aliases:** Spearman’s rank correlation, Spearman’s rho (ρ). No stable external identifier is specified in the source. [^soil_metal_functional_genomics]

Spearman correlation is a rank-based statistical method used in this study to assess associations between soil metal concentrations and microbial functional gene content. [^soil_metal_functional_genomics]

## Evidence from soil metal functional genomics

The analysis applied Spearman correlation to 51,748 soil samples covering nine metals: copper, cobalt, chromium, nickel, zinc, lead, arsenic, cadmium, and mercury. [^soil_metal_functional_genomics]

Across the nine metals, the study identified 2,355 significant Cluster of Orthologous Groups (COG)–metal associations at false discovery rate (FDR) < 0.05, from 3,915 implied tests involving nine metals and 435 COGs. [^soil_metal_functional_genomics]

Chromium and lead produced the strongest signals, and transporters—including ABC and RND systems—as well as biosynthesis genes dominated the top hits. [^soil_metal_functional_genomics]

A copper-specific Spearman analysis identified 116 COGs at FDR < 0.05 using 7,566 samples with nearby KBase genomes within 10 km. [^soil_metal_functional_genomics]

The strongest positive copper associations involved cell-division and nucleotide-transport categories BQ, FQ, and FK, while the strongest negative associations involved energy-production categories DI and CE. These observational associations suggest, but do not establish, energetic trade-offs under copper stress. [^soil_metal_functional_genomics]

## Interpretation and limitations

The 2,355 discoveries represent a 60% discovery rate among the 3,915 implied tests, but co-contamination means that chromium, copper, lead, and zinc can co-vary in industrial soils, making tests non-independent. [^soil_metal_functional_genomics]

Because positive correlation among tests may make Benjamini–Hochberg FDR correction anti-conservative, the true FDR may be higher than reported. [^soil_metal_functional_genomics]

Effect sizes were not systematically reported across all 2,355 associations, and the planned audit will examine the Spearman rho distribution and flag associations with rho < 0.05. [^soil_metal_functional_genomics]

Planned validation includes partial-correlation models to distinguish metal-specific associations from generic multi-metal responses, including COG ~ Cr | Cu + Zn + Pb. [^soil_metal_functional_genomics]

The source reports that the necessary Spearman rho values are not available in a local CSV and that validation requires rerunning analyses from the `kescience_mgnify` and `kbase_ke_pangenome` Spark tables. [^soil_metal_functional_genomics]

## Related pages

- [soil_metal_functional_genomics__REPORT](../summaries/soil_metal_functional_genomics__REPORT.md)
- [environmental-resistome](../concepts/environmental-resistome.md)
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md)
- [metal-cross-resistance](../concepts/metal-cross-resistance.md)
- [environment-embedding-geography](../concepts/environment-embedding-geography.md)
- [distance-based-redundancy-analysis](distance-based-redundancy-analysis.md)
- [phylogenetic-generalized-least-squares](phylogenetic-generalized-least-squares.md)

[^soil_metal_functional_genomics]: [soil metal functional genomics](../summaries/soil_metal_functional_genomics__REPORT.md)
