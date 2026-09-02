---
type: "Organism"
description: "AMR-variable bacterial pathogen with extensive accessory resistance"
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_pangenome_atlas__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md", "summaries/metabolic_capability_dependency__REPORT.md"]
---
# Klebsiella pneumoniae

## Identity

**Canonical name:** Klebsiella pneumoniae. [src: amr_environmental_resistome]

**Known alias:** *K. pneumoniae*. [src: amr_environmental_resistome]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: amr_environmental_resistome]

## Evidence across AMR studies

The environmental resistome study analyzed 13,637 *Klebsiella pneumoniae* genomes and identified 1,115 AMR gene clusters. [src: amr_environmental_resistome] Of these clusters, 7 were classified as core and 1,108 as accessory, with accessory AMR accounting for 99% of the clusters. [src: amr_environmental_resistome] The species was clinical-dominant at 80% in the study's environmental representation analysis. [src: amr_environmental_resistome] Only 7 of 1,115 clusters being core illustrates extensive accessory AMR variation in this clinically dominated species. [src: amr_environmental_resistome]

The pan-bacterial atlas **supports** this organism-level pattern: Klebsiella led all reported genera at 206 AMR clusters per species, placing it among the strongest AMR hotspots in the 27,690-species analysis. [src: amr_pangenome_atlas] The atlas therefore **refines** the earlier case study by showing that Klebsiella's high and predominantly accessory AMR burden is also evident at broader pangenome scale, while the genus-level value is an average rather than a species-specific measurement. [src: amr_pangenome_atlas]

The metabolic capability study **supports and refines** the pangenome interpretation: among well-sampled pathogens with more than 2,500 genomes, *K. pneumoniae* was reported as the most open pangenome, with 99.05% open genes and 0.95% core genes. [src: metabolic_capability_dependency] This is a species-level pangenome result distinct from the AMR-cluster measurements, but it is consistent with extensive accessory genomic variation. [src: metabolic_capability_dependency]

The within-species strain-variation analysis further **supports** the interpretation of structured AMR heterogeneity: its *K. pneumoniae* case-study UMAP showed visible environmental structuring, although the broader environment–ecotype relationship was not established because the available tests were underpowered. [src: amr_strain_variation] Because *K. pneumoniae* exceeded the 500-genome cap, it was excluded from that study's ANI–AMR Mantel analysis, so no phylogenetic-signal estimate was reported for this species. [src: amr_strain_variation]

The discoveries synthesis **supports** the original cluster count and accessory-resistance interpretation, again reporting 1,115 AMR clusters across 13,637 *K. pneumoniae* genomes, with only 7 classified as core. [src: discoveries] It also places this species within a broader finding that clinical species had 68% accessory AMR versus 43% in soil species, although that comparison is not a species-specific estimate. [src: discoveries]

The discoveries synthesis additionally reports that Klebsiella was the only PhageFoundry species with both SNIPE defense-system evidence and the ManX-family PTS domain: it had 1 DUF4041 annotation across 3 proteins and 4,619 PTS_EIIC annotations. [src: discoveries] This is a defense/transport annotation result rather than evidence that these features explain the AMR burden.

These results provide an organism-level case study for [[concepts/environmental-resistome]], supporting the conclusion that clinical representation is associated with high AMR diversity and predominantly accessory resistance. [src: amr_environmental_resistome]

The case study was assembled from the [[entities/kbase-ke-pangenome]] collection using [[entities/amrfinderplus]]-focused AMR annotation. [src: amr_environmental_resistome]

## Related pages

- [[summaries/amr_environmental_resistome__REPORT]] — source report containing the environmental resistome analysis. [src: amr_environmental_resistome]
- [[summaries/amr_pangenome_atlas__REPORT]] — pan-bacterial atlas reporting Klebsiella's genus-level AMR hotspot status. [src: amr_pangenome_atlas]
- [[summaries/amr_strain_variation__REPORT]] — within-species AMR variation, ecotype, and environmental-structuring analysis. [src: amr_strain_variation]
- [[summaries/metabolic_capability_dependency__REPORT]] — metabolic capability, dependency, pangenome openness, and ecotype analysis. [src: metabolic_capability_dependency]
- [[summaries/discoveries]] — cross-project synthesis confirming the AMR cluster pattern and reporting Klebsiella defense/transport annotations. [src: discoveries]
- [[concepts/environmental-resistome]] — cross-project synthesis of environment-structured AMR diversity. [src: amr_environmental_resistome]
- [[concepts/pangenome-integration]] — pangenome-scale analysis of core and accessory AMR composition. [src: amr_environmental_resistome]
- [[entities/amrfinderplus]] — AMR annotation resource used in the study. [src: amr_environmental_resistome]
- [[entities/kbase-ke-pangenome]] — pangenome collection underlying the analysis. [src: amr_environmental_resistome]
- [[entities/snipe-defense-system]] — defense-system annotation reported in the discoveries synthesis. [src: discoveries]
