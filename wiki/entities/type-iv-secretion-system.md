---
type: Gene_Or_Pathway
description: Type IV secretion system markers and machinery involved in microbial
  transfer.
sources:
- id: plant_microbiome_ecotypes
  resource: ../summaries/plant_microbiome_ecotypes__REPORT.md
  title: plant microbiome ecotypes
- id: t4ss_cazy_environmental_hgt
  resource: ../summaries/t4ss_cazy_environmental_hgt__REPORT.md
  title: t4ss cazy environmental hgt
title: Type IV Secretion System
---
# Type IV Secretion System

## What this entity is

**Canonical name:** Type IV secretion system. [^plant_microbiome_ecotypes]

**Known aliases:** T4SS; VirB/VirD4 and conjugative machinery marker sets. [^plant_microbiome_ecotypes] [^t4ss_cazy_environmental_hgt]

**Stable external identifier:** Not specified in the source reports. [^plant_microbiome_ecotypes] [^t4ss_cazy_environmental_hgt]

Type IV secretion system markers represent a secretion-system or conjugative-transfer capability in genomic analyses. [^plant_microbiome_ecotypes] The environmental HGT analysis used a multi-marker definition comprising VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB, and TraG. [^t4ss_cazy_environmental_hgt]

## Key facts

The refined plant-interaction marker panel used KEGG module gating that required at least three genes for a T4SS-positive classification. [^plant_microbiome_ecotypes] T4SS classifications changed minimally when the initial 91-marker panel was reduced to 17 plant-specific markers and stricter pathway-gating rules were applied. [^plant_microbiome_ecotypes] Across plant-associated genomes, T4SS genes had a 48.5% singleton fraction, placing a substantial portion of the marker signal in accessory rather than shared gene content. [^plant_microbiome_ecotypes]

The environmental survey detected T4SS or conjugative machinery in 6,652 of 30,497 high-quality environmental MAGs (21.8%). [^t4ss_cazy_environmental_hgt] This **refines** the plant-associated marker results by showing that T4SS detection also captures a substantial capability across environmental MAGs. [^t4ss_cazy_environmental_hgt]

Ninety-two CAZy families showed elevated co-occurrence with T4SS loci at distances of ≤10 kb, pending threshold validation; GT2 glycosyltransferases were the top hit, occurring in 767 genomes with an average length of 5,041 bp. [^t4ss_cazy_environmental_hgt] Marine sediment, barley rhizosphere, and maize rhizosphere showed enrichment for T4SS–CAZy associations with OR=5.5, q<10⁻⁹⁸; OR=10.4; and OR=4.1, respectively. [^t4ss_cazy_environmental_hgt]

The report treats T4SS and related secretion functions as context-dependent markers because they can contribute to colonization, interbacterial competition, beneficial symbiosis, or pathogenicity. [^plant_microbiome_ecotypes] The refined marker framework classified 878 of 1,115 plant-associated species, or 78.7%, as dual-nature, meaning that they carried both beneficial and pathogenic marker signals; T4SS was one component of the marker framework rather than evidence by itself of pathogenicity. [^plant_microbiome_ecotypes] The broader binary-presence scheme classified 15,474 of 25,660 species, or 60.3%, as dual-nature when they carried at least one plant-growth-promotion marker and at least one pathogenic marker, illustrating that marker presence alone produces a broad categorical class. [^plant_microbiome_ecotypes]

Gene presence does not establish T4SS expression or phenotype; RNA-seq or experimental validation is needed to determine whether beneficial and pathogenic marker sets are co-expressed under the same conditions. [^plant_microbiome_ecotypes] The environmental report likewise supports an observational interpretation: its 70/30 discovery/validation split reproduced enrichment patterns, but mechanistic transfer remains experimentally unconfirmed. [^t4ss_cazy_environmental_hgt]

T4SS detection depended on InterProScan because 12 of 22 audited marker Pfams were absent from the bakta_pfam_domains table, with the missing set dominated by T3SS, T4SS, and T6SS components. [^plant_microbiome_ecotypes] The refined cohort pipeline therefore used InterProScan for secretion-system detection, and the report states that the annotation-table limitation did not affect its biological assignments. [^plant_microbiome_ecotypes]

In the environmental data, GT2 neighborhoods provided contig-level support for syntenic co-localization: among 376 parsed genomes, T4SS occurred in 503 neighborhood entries and GT2 in 495. [^t4ss_cazy_environmental_hgt] GH23 was the second most common CAZy family in these neighborhoods, with 106 occurrences, suggesting that cell-wall-remodeling genes cluster with GT2–T4SS loci. [^t4ss_cazy_environmental_hgt]

The GT2 gene tree contained 77 detected HGT events, including 32 normalized high-confidence cross-phylum events; the strongest, Node_4915, spanned 8 phyla with Max_Divergence = 4.843. [^t4ss_cazy_environmental_hgt] Divergence and synteny were negatively correlated (Spearman ρ = −0.615, p<0.001), with more distant events having lower syntenic percentage. [^t4ss_cazy_environmental_hgt] These findings **support** a possible environmental role for T4SS-associated transfer while retaining the hypothesis that T4SS machinery mediates CAZy dissemination rather than establishing that mechanism. [^t4ss_cazy_environmental_hgt]

CAZy genes were not detected on plasmids by ICEfinder; 12 integrative mobilizable elements occurred among the top 100 accumulators, and T4SS-positive genomes had 10× higher mobile genetic element density than other genomes (p<0.001). [^t4ss_cazy_environmental_hgt] This **refines** the interpretation of T4SS from a general capability marker toward a possible chromosomal or integrative-transfer context rather than plasmid mobilization. [^t4ss_cazy_environmental_hgt]

## Interpretation and links

T4SS marker status should be interpreted as a genomic capability signal, not as a categorical label for beneficial or pathogenic behavior. [^plant_microbiome_ecotypes] T4SS-proximal GT2 neighborhoods had 11× more metal-resistance genes; GT2-neighborhood MAGs had a mean of 0.045 metal-resistance types versus 0.004 for non-GT2 MAGs (n=376 and n=260,276; Mann–Whitney p=8.6e-27). [^t4ss_cazy_environmental_hgt] This **supports** links to [environmental-resistome](../concepts/environmental-resistome.md) and [metal-cross-resistance](../concepts/metal-cross-resistance.md), but the association does not establish causation. [^t4ss_cazy_environmental_hgt]

This entity contributes to [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) by linking plant-associated genomic content to compartment and host context. [^plant_microbiome_ecotypes] It contributes to [pangenome-integration](../concepts/pangenome-integration.md) through the distinction between core and singleton marker content and the cross-phylum GT2 HGT results. [^plant_microbiome_ecotypes] [^t4ss_cazy_environmental_hgt] It also contributes to [condition-specific-fitness](../concepts/condition-specific-fitness.md), because functional activity requires validation under defined plant-associated conditions rather than inference from gene presence alone. [^plant_microbiome_ecotypes]

The source documents are summarized at [plant_microbiome_ecotypes__REPORT](../summaries/plant_microbiome_ecotypes__REPORT.md) and [t4ss_cazy_environmental_hgt__REPORT](../summaries/t4ss_cazy_environmental_hgt__REPORT.md). [^plant_microbiome_ecotypes] [^t4ss_cazy_environmental_hgt]

[^plant_microbiome_ecotypes]: [plant microbiome ecotypes](../summaries/plant_microbiome_ecotypes__REPORT.md)
[^t4ss_cazy_environmental_hgt]: [t4ss cazy environmental hgt](../summaries/t4ss_cazy_environmental_hgt__REPORT.md)
