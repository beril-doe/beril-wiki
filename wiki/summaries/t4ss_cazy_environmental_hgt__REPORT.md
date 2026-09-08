---
type: Summary
description: Environmental T4SS–CAZy co-localization and cross-phylum HGT analysis
doc_type: short
full_text: ../sources/t4ss_cazy_environmental_hgt__REPORT.md
title: T4SS–CAZy Environmental HGT
sources:
- id: t4ss_cazy_environmental_hgt
  resource: ../sources/t4ss_cazy_environmental_hgt__REPORT.md
  title: t4ss cazy environmental hgt
---
# T4SS–CAZy Environmental HGT

## Overview

This preliminary report analyzes type IV secretion system (T4SS) and conjugative machinery in high-quality environmental metagenome-assembled genomes (MAGs), carbohydrate-active enzyme (CAZy) gene neighborhoods, and horizontal gene transfer (HGT) in GT2 glycosyltransferases. Core analyses NB01–NB04 are complete; NB05 threshold validation and NB06 manuscript figures remain pending. [^t4ss_cazy_environmental_hgt]

## Key Findings

- **T4SS prevalence:** 6,652 of 30,497 high-quality environmental MAGs (21.8%) carry T4SS or conjugative machinery, using a multi-marker definition comprising VirB4/6/8/9/10/11, VirD4, TraI/D, TrwB, and TraG. [^t4ss_cazy_environmental_hgt]
- **CAZy co-occurrence:** 92 CAZy families show elevated co-occurrence with T4SS loci at distances of ≤10 kb, although threshold validation is pending. GT2 glycosyltransferases are the top hit, occurring in 767 genomes with an average length of 5,041 bp. [^t4ss_cazy_environmental_hgt]
- **Biome enrichment:** T4SS–CAZy associations are enriched in marine sediment (OR=5.5, q<10⁻⁹⁸), barley rhizosphere (OR=10.4), and maize rhizosphere (OR=4.1). [^t4ss_cazy_environmental_hgt]
- **GT2 HGT:** The GT2 gene tree contains 77 detected HGT events, including 32 normalized high-confidence cross-phylum events. The strongest event, Node_4915, spans 8 phyla at a maximum divergence of 4.843. [^t4ss_cazy_environmental_hgt]
- **Transfer context:** CAZy genes were not detected on plasmids by ICEfinder; 12 integrative mobilizable elements (IMEs) occurred among the top 100 accumulators. T4SS-positive genomes have 10× higher mobile genetic element (MGE) density than other genomes (p<0.001), consistent with chromosomal or integrative transfer rather than plasmid mobilization. [^t4ss_cazy_environmental_hgt]
- **Robustness:** A 70/30 discovery/validation split reproduced the enrichment patterns across both sets. [^t4ss_cazy_environmental_hgt]

## NB05 HGT Characterization

Among 77 events in `Detected_HGT_Events.csv`, 65 span 2 phyla and 12 span ≥3 phyla (15.6%). Node_4915 contains 35 genes, 82.9% syntenic, spans 8 phyla—WOR-3, Desulfobacterota, Patescibacteria, Bacteroidota, Firmicutes_A, Methanobacteriota, Bdellovibrionota, and Acidobacteriota—and has Max_Divergence = 4.843. Divergence and synteny are negatively correlated (Spearman ρ = −0.615, p<0.001), with more phylogenetically distant events having lower syntenic percentage. [^t4ss_cazy_environmental_hgt]

The most-involved phyla across all detected events are Firmicutes_A (27 events), Pseudomonadota (22), Bacillota_A (19), and Actinomycetota (10). The report includes `figures/fig_nb05_hgt_scatter.png`. [^t4ss_cazy_environmental_hgt]

## GT2 Neighborhood and Metal Resistance Results

In 376 genomes, the GT2 neighborhood was parsed as a list-format region: T4SS occurred in 503 neighborhood entries and GT2 in 495, confirming syntenic co-localization at the contig level. GH23, a murein lytic transglycosylase family, was the second most common CAZy family in GT2 neighborhoods, with 106 occurrences, suggesting that cell-wall-remodeling genes cluster with GT2–T4SS syntenic loci. [^t4ss_cazy_environmental_hgt]

GT2-neighborhood MAGs (n=376) had a mean of 0.045 metal-resistance types, compared with 0.004 for non-GT2 MAGs (n=260,276; Mann–Whitney p=8.6e-27). Genomes with GT2 in T4SS-proximal neighborhoods carried 11× more metal-resistance genes, independently linking CAZy–T4SS synteny with the hypothesis that genomes serving as hubs for GT2 horizontal transfer have greater metal-resistance niche breadth. [^t4ss_cazy_environmental_hgt]

## Interpretation and Caveats

The observed T4SS co-localization with GT2 glycosyltransferase cassettes and phylogenetic incongruence in the GT2 gene tree provide positive evidence for 32 cross-phylum HGT events. The absence of plasmid-borne CAZy genes in the ICEfinder analysis, together with 10× higher MGE density in T4SS-positive genomes, is consistent with chromosomal or integrative mechanisms involving IMEs or integrative conjugative elements rather than plasmid mobilization. These results support the hypothesis that T4SS machinery mediates environmental dissemination of carbohydrate-active enzyme diversity across phylogenetically distant bacteria, but all associations are observational and require experimental validation for mechanistic confirmation. [^t4ss_cazy_environmental_hgt]

The report identifies four pending validation tasks: a synteny-threshold permutation test requiring unfiltered Spark data; BLAST validation of Node_4915 against NCBI nr; a housekeeping-gene null baseline; and biome-enrichment factorization using θ = OR(T4SS-CAZy) / [OR(T4SS) × OR(CAZy)]. [^t4ss_cazy_environmental_hgt]

## Slots Into

- [pangenome-integration](../concepts/pangenome-integration.md) — cross-phylum GT2 HGT events and the proposed chromosomal or integrative transfer route extend the corpus’s treatment of gene mobility across genomic backgrounds. [^t4ss_cazy_environmental_hgt]
- [environmental-resistome](../concepts/environmental-resistome.md) — T4SS-proximal GT2 neighborhoods are associated with 11× more metal-resistance genes, linking environmental HGT niches to resistance functions. [^t4ss_cazy_environmental_hgt]
- [metal-cross-resistance](../concepts/metal-cross-resistance.md) — the 0.045 versus 0.004 metal-resistance-type comparison provides a new association between CAZy–T4SS neighborhoods and metal-resistance breadth. [^t4ss_cazy_environmental_hgt]

[^t4ss_cazy_environmental_hgt]: [t4ss cazy environmental hgt](../sources/t4ss_cazy_environmental_hgt__REPORT.md)
