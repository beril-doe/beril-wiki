---
type: Organism
description: AMR-variable bacterial pathogen with extensive accessory resistance
sources:
- id: amr_environmental_resistome
  resource: ../summaries/amr_environmental_resistome__REPORT.md
  title: amr environmental resistome
- id: amr_pangenome_atlas
  resource: ../summaries/amr_pangenome_atlas__REPORT.md
  title: amr pangenome atlas
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: discoveries
  resource: ../summaries/discoveries.md
  title: discoveries
- id: metabolic_capability_dependency
  resource: ../summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
title: Klebsiella pneumoniae
---
# Klebsiella pneumoniae

## Identity

**Canonical name:** Klebsiella pneumoniae. [^amr_environmental_resistome]

**Known alias:** *K. pneumoniae*. [^amr_environmental_resistome]

**Stable external identifier:** No stable external identifier was reported in the source document. [^amr_environmental_resistome]

## Evidence across AMR studies

The environmental resistome study analyzed 13,637 *Klebsiella pneumoniae* genomes and identified 1,115 AMR gene clusters. [^amr_environmental_resistome] Of these clusters, 7 were classified as core and 1,108 as accessory, with accessory AMR accounting for 99% of the clusters. [^amr_environmental_resistome] The species was clinical-dominant at 80% in the study's environmental representation analysis. [^amr_environmental_resistome] Only 7 of 1,115 clusters being core illustrates extensive accessory AMR variation in this clinically dominated species. [^amr_environmental_resistome]

The pan-bacterial atlas **supports** this organism-level pattern: Klebsiella led all reported genera at 206 AMR clusters per species, placing it among the strongest AMR hotspots in the 27,690-species analysis. [^amr_pangenome_atlas] The atlas therefore **refines** the earlier case study by showing that Klebsiella's high and predominantly accessory AMR burden is also evident at broader pangenome scale, while the genus-level value is an average rather than a species-specific measurement. [^amr_pangenome_atlas]

The metabolic capability study **supports and refines** the pangenome interpretation: among well-sampled pathogens with more than 2,500 genomes, *K. pneumoniae* was reported as the most open pangenome, with 99.05% open genes and 0.95% core genes. [^metabolic_capability_dependency] This is a species-level pangenome result distinct from the AMR-cluster measurements, but it is consistent with extensive accessory genomic variation. [^metabolic_capability_dependency]

The within-species strain-variation analysis further **supports** the interpretation of structured AMR heterogeneity: its *K. pneumoniae* case-study UMAP showed visible environmental structuring, although the broader environment–ecotype relationship was not established because the available tests were underpowered. [^amr_strain_variation] Because *K. pneumoniae* exceeded the 500-genome cap, it was excluded from that study's ANI–AMR Mantel analysis, so no phylogenetic-signal estimate was reported for this species. [^amr_strain_variation]

The discoveries synthesis **supports** the original cluster count and accessory-resistance interpretation, again reporting 1,115 AMR clusters across 13,637 *K. pneumoniae* genomes, with only 7 classified as core. [^discoveries] It also places this species within a broader finding that clinical species had 68% accessory AMR versus 43% in soil species, although that comparison is not a species-specific estimate. [^discoveries]

The discoveries synthesis additionally reports that Klebsiella was the only PhageFoundry species with both SNIPE defense-system evidence and the ManX-family PTS domain: it had 1 DUF4041 annotation across 3 proteins and 4,619 PTS_EIIC annotations. [^discoveries] This is a defense/transport annotation result rather than evidence that these features explain the AMR burden.

These results provide an organism-level case study for [environmental-resistome](../concepts/environmental-resistome.md), supporting the conclusion that clinical representation is associated with high AMR diversity and predominantly accessory resistance. [^amr_environmental_resistome]

The case study was assembled from the [kbase-ke-pangenome](kbase-ke-pangenome.md) collection using [amrfinderplus](amrfinderplus.md)-focused AMR annotation. [^amr_environmental_resistome]

## Related pages

- [amr_environmental_resistome__REPORT](../summaries/amr_environmental_resistome__REPORT.md) — source report containing the environmental resistome analysis. [^amr_environmental_resistome]
- [amr_pangenome_atlas__REPORT](../summaries/amr_pangenome_atlas__REPORT.md) — pan-bacterial atlas reporting Klebsiella's genus-level AMR hotspot status. [^amr_pangenome_atlas]
- [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md) — within-species AMR variation, ecotype, and environmental-structuring analysis. [^amr_strain_variation]
- [metabolic_capability_dependency__REPORT](../summaries/metabolic_capability_dependency__REPORT.md) — metabolic capability, dependency, pangenome openness, and ecotype analysis. [^metabolic_capability_dependency]
- [discoveries](../summaries/discoveries.md) — cross-project synthesis confirming the AMR cluster pattern and reporting Klebsiella defense/transport annotations. [^discoveries]
- [environmental-resistome](../concepts/environmental-resistome.md) — cross-project synthesis of environment-structured AMR diversity. [^amr_environmental_resistome]
- [pangenome-integration](../concepts/pangenome-integration.md) — pangenome-scale analysis of core and accessory AMR composition. [^amr_environmental_resistome]
- [amrfinderplus](amrfinderplus.md) — AMR annotation resource used in the study. [^amr_environmental_resistome]
- [kbase-ke-pangenome](kbase-ke-pangenome.md) — pangenome collection underlying the analysis. [^amr_environmental_resistome]
- [snipe-defense-system](snipe-defense-system.md) — defense-system annotation reported in the discoveries synthesis. [^discoveries]

[^amr_environmental_resistome]: [amr environmental resistome](../summaries/amr_environmental_resistome__REPORT.md)
[^amr_pangenome_atlas]: [amr pangenome atlas](../summaries/amr_pangenome_atlas__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../summaries/metabolic_capability_dependency__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^discoveries]: [discoveries](../summaries/discoveries.md)
