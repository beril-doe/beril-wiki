---
type: "Gene_Or_Pathway"
description: "Type IV secretion system markers and machinery involved in microbial transfer."
sources: ["summaries/plant_microbiome_ecotypes__REPORT.md", "summaries/t4ss_cazy_environmental_hgt__REPORT.md"]
---
# Type IV Secretion System

## What this entity is

**Canonical name:** Type IV secretion system. [src: plant_microbiome_ecotypes]

**Known aliases:** T4SS; VirB/VirD4 and conjugative machinery marker sets. [src: plant_microbiome_ecotypes] [src: t4ss_cazy_environmental_hgt]

**Stable external identifier:** Not specified in the source reports. [src: plant_microbiome_ecotypes] [src: t4ss_cazy_environmental_hgt]

Type IV secretion system markers represent a secretion-system or conjugative-transfer capability in genomic analyses. [src: plant_microbiome_ecotypes] The environmental HGT analysis used a multi-marker definition comprising VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB, and TraG. [src: t4ss_cazy_environmental_hgt]

## Key facts

The refined plant-interaction marker panel used KEGG module gating that required at least three genes for a T4SS-positive classification. [src: plant_microbiome_ecotypes] T4SS classifications changed minimally when the initial 91-marker panel was reduced to 17 plant-specific markers and stricter pathway-gating rules were applied. [src: plant_microbiome_ecotypes] Across plant-associated genomes, T4SS genes had a 48.5% singleton fraction, placing a substantial portion of the marker signal in accessory rather than shared gene content. [src: plant_microbiome_ecotypes]

The environmental survey detected T4SS or conjugative machinery in 6,652 of 30,497 high-quality environmental MAGs (21.8%). [src: t4ss_cazy_environmental_hgt] This **refines** the plant-associated marker results by showing that T4SS detection also captures a substantial capability across environmental MAGs. [src: t4ss_cazy_environmental_hgt]

Ninety-two CAZy families showed elevated co-occurrence with T4SS loci at distances of ≤10 kb, pending threshold validation; GT2 glycosyltransferases were the top hit, occurring in 767 genomes with an average length of 5,041 bp. [src: t4ss_cazy_environmental_hgt] Marine sediment, barley rhizosphere, and maize rhizosphere showed enrichment for T4SS–CAZy associations with OR=5.5, q<10⁻⁹⁸; OR=10.4; and OR=4.1, respectively. [src: t4ss_cazy_environmental_hgt]

The report treats T4SS and related secretion functions as context-dependent markers because they can contribute to colonization, interbacterial competition, beneficial symbiosis, or pathogenicity. [src: plant_microbiome_ecotypes] The refined marker framework classified 878 of 1,115 plant-associated species, or 78.7%, as dual-nature, meaning that they carried both beneficial and pathogenic marker signals; T4SS was one component of the marker framework rather than evidence by itself of pathogenicity. [src: plant_microbiome_ecotypes] The broader binary-presence scheme classified 15,474 of 25,660 species, or 60.3%, as dual-nature when they carried at least one plant-growth-promotion marker and at least one pathogenic marker, illustrating that marker presence alone produces a broad categorical class. [src: plant_microbiome_ecotypes]

Gene presence does not establish T4SS expression or phenotype; RNA-seq or experimental validation is needed to determine whether beneficial and pathogenic marker sets are co-expressed under the same conditions. [src: plant_microbiome_ecotypes] The environmental report likewise supports an observational interpretation: its 70/30 discovery/validation split reproduced enrichment patterns, but mechanistic transfer remains experimentally unconfirmed. [src: t4ss_cazy_environmental_hgt]

T4SS detection depended on InterProScan because 12 of 22 audited marker Pfams were absent from the bakta_pfam_domains table, with the missing set dominated by T3SS, T4SS, and T6SS components. [src: plant_microbiome_ecotypes] The refined cohort pipeline therefore used InterProScan for secretion-system detection, and the report states that the annotation-table limitation did not affect its biological assignments. [src: plant_microbiome_ecotypes]

In the environmental data, GT2 neighborhoods provided contig-level support for syntenic co-localization: among 376 parsed genomes, T4SS occurred in 503 neighborhood entries and GT2 in 495. [src: t4ss_cazy_environmental_hgt] GH23 was the second most common CAZy family in these neighborhoods, with 106 occurrences, suggesting that cell-wall-remodeling genes cluster with GT2–T4SS loci. [src: t4ss_cazy_environmental_hgt]

The GT2 gene tree contained 77 detected HGT events, including 32 normalized high-confidence cross-phylum events; the strongest, Node_4915, spanned 8 phyla with Max_Divergence = 4.843. [src: t4ss_cazy_environmental_hgt] Divergence and synteny were negatively correlated (Spearman ρ = −0.615, p<0.001), with more distant events having lower syntenic percentage. [src: t4ss_cazy_environmental_hgt] These findings **support** a possible environmental role for T4SS-associated transfer while retaining the hypothesis that T4SS machinery mediates CAZy dissemination rather than establishing that mechanism. [src: t4ss_cazy_environmental_hgt]

CAZy genes were not detected on plasmids by ICEfinder; 12 integrative mobilizable elements occurred among the top 100 accumulators, and T4SS-positive genomes had 10× higher mobile genetic element density than other genomes (p<0.001). [src: t4ss_cazy_environmental_hgt] This **refines** the interpretation of T4SS from a general capability marker toward a possible chromosomal or integrative-transfer context rather than plasmid mobilization. [src: t4ss_cazy_environmental_hgt]

## Interpretation and links

T4SS marker status should be interpreted as a genomic capability signal, not as a categorical label for beneficial or pathogenic behavior. [src: plant_microbiome_ecotypes] T4SS-proximal GT2 neighborhoods had 11× more metal-resistance genes; GT2-neighborhood MAGs had a mean of 0.045 metal-resistance types versus 0.004 for non-GT2 MAGs (n=376 and n=260,276; Mann–Whitney p=8.6e-27). [src: t4ss_cazy_environmental_hgt] This **supports** links to [[concepts/environmental-resistome]] and [[concepts/metal-cross-resistance]], but the association does not establish causation. [src: t4ss_cazy_environmental_hgt]

This entity contributes to [[concepts/ecotype-environment-gene-content]] by linking plant-associated genomic content to compartment and host context. [src: plant_microbiome_ecotypes] It contributes to [[concepts/pangenome-integration]] through the distinction between core and singleton marker content and the cross-phylum GT2 HGT results. [src: plant_microbiome_ecotypes] [src: t4ss_cazy_environmental_hgt] It also contributes to [[concepts/condition-specific-fitness]], because functional activity requires validation under defined plant-associated conditions rather than inference from gene presence alone. [src: plant_microbiome_ecotypes]

The source documents are summarized at [[summaries/plant_microbiome_ecotypes__REPORT]] and [[summaries/t4ss_cazy_environmental_hgt__REPORT]]. [src: plant_microbiome_ecotypes] [src: t4ss_cazy_environmental_hgt]
