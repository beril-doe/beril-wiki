---
type: Method
description: Exact test for categorical enrichment, depletion, and association
sources:
- id: metal_resistance_global_biogeography
  resource: ../summaries/metal_resistance_global_biogeography__REPORT.md
  title: metal resistance global biogeography
- id: pgp_pangenome_ecology
  resource: ../summaries/pgp_pangenome_ecology__REPORT.md
  title: pgp pangenome ecology
- id: prophage_amr_comobilization
  resource: ../summaries/prophage_amr_comobilization__REPORT.md
  title: prophage amr comobilization
- id: conservation_vs_fitness
  resource: ../summaries/conservation_vs_fitness__REPORT.md
  title: conservation vs fitness
title: Fisher's exact test
---
# Fisher's exact test

## What this entity is

**Canonical name:** Fisher's exact test. [^metal_resistance_global_biogeography]

**Type:** Method. [^metal_resistance_global_biogeography]

**Known aliases:** Fisher's exact tests. [^metal_resistance_global_biogeography]

**Stable external identifier:** None reported in the source. [^metal_resistance_global_biogeography]

## Key facts from the documents

Fisher's exact tests evaluate categorical enrichment and depletion. They were used for metal-resistance patterns in a 5° global grid containing **289 cells with at least 5 MAGs**. With Benjamini–Hochberg false discovery rate (BH FDR) correction, the analysis identified **11 significant hotspots** with **OR>2** and **q<0.05**, plus **3 coldspots** with **OR<0.5** and **q<0.05**. [^metal_resistance_global_biogeography]

The top hotspot was the Atacama/Andean region of Chile at **lat=-25°, lon=-70°**, with **21.8% prevalence**, **OR=9.83**, **q=7.6e-12**, and **n=101 MAGs**. Eastern and central USA clusters at **lat=40°, lon=-80° and -90°** had **OR=7.9** and **6.3**, respectively; an East/Southeast Asia cluster at **lat=25–30°, lon=105–120°** had **OR=4.4–5.9**. [^metal_resistance_global_biogeography]

Biome-stratified tests compared each biome with the global baseline and applied BH FDR correction. Soil showed **5.8% prevalence**, **OR=5.05**, and **q=1.8e-82** among **7,939 MAGs**; rhizosphere showed **1.9% prevalence**, **OR=0.66**, and **q=0.30 (NS)** among **422 MAGs**; marine samples showed **1.2% prevalence**, **OR=0.20**, and **q=9.2e-80** among **13,995 MAGs**. [^metal_resistance_global_biogeography]

The PGP pangenome analysis used the same exact-test framework for categorical gene co-occurrence and environmental comparisons: eight of 10 focal-gene pairs remained significant after BH-FDR correction, including positive pqqC × acdS association (**OR = 7.24**, **n = 286**, **q = 1.2e-83**) and negative nifH × hcnC association (**OR = 0.23**, **q = 5.8e-29**). [^pgp_pangenome_ecology] This **supports** using the method for discrete ecological enrichment and depletion beyond metal resistance. [^pgp_pangenome_ecology]

The PGP analysis also found acdS enrichment in soil/rhizosphere species (**OR = 7.02**, **q = 5.1e-62**) and nifH depletion (**OR = 0.60**, **q = 5.5e-08**), while a Fisher test linked ipdC to complete tryptophan biosynthesis (**OR = 2.81**, **p = 6.3e-10**). [^pgp_pangenome_ecology] These findings **refine** the biome-level use case by showing that exact tests can compare gene-pair associations and environment-stratified species prevalences, although the soil-specific ipdC reversal is hypothesis-generating. [^pgp_pangenome_ecology]

The conservation-versus-fitness analysis applied Fisher's exact test to essential-gene status versus pangenome conservation, finding that essential genes were **86.1% core** versus **81.2%** for non-essential genes, with a median **odds ratio of 1.56**; **18 of 33 organisms** showed significant enrichment after BH-FDR correction at **q < 0.05**. [^conservation_vs_fitness] This **supports** the method's use for testing modest categorical conservation effects, while the study's single-condition RB-TnSeq essentiality calls and variable pangenome coverage **refine** interpretation of the resulting associations. [^conservation_vs_fitness]

The prophage–AMR analysis applied Fisher's exact test to compare accessory status: AMR genes within 10 genes of a prophage marker were **67.6% accessory**, versus **65.5%** for distal AMR genes, with **OR=1.10**, one-sided **p=0.005**, and bootstrap 95% confidence interval **[1.024, 1.185]**. [^prophage_amr_comobilization] This **supports** the method's sensitivity to modest categorical effects, while the **2.1 percentage point** difference and threshold-dependent odds ratios (**0.78** at 3 genes, **0.92** at 5, **1.10** at 10, **1.19** at 15, and **1.28** at 50) **refine** interpretation: statistical significance need not imply a large or consistently replicated effect. [^prophage_amr_comobilization]

These results contribute to [environmental-resistome](../concepts/environmental-resistome.md), which synthesizes geographic and biome-level patterns in environmental metal resistance. They also relate to [environment-embedding-geography](../concepts/environment-embedding-geography.md), because sampling-effort correction is necessary before regional hotspot patterns can be interpreted. The conservation result contributes to [gene-essentiality](../concepts/gene-essentiality.md) and [pangenome-integration](../concepts/pangenome-integration.md) by testing essentiality against core-genome membership. The method is related to [benjamini-hochberg-fdr](benjamini-hochberg-fdr.md), the multiple-testing correction used with the reported tests.

Complete source contexts are summarized in [metal_resistance_global_biogeography__REPORT](../summaries/metal_resistance_global_biogeography__REPORT.md), [pgp_pangenome_ecology__REPORT](../summaries/pgp_pangenome_ecology__REPORT.md), [prophage_amr_comobilization__REPORT](../summaries/prophage_amr_comobilization__REPORT.md), and [conservation_vs_fitness__REPORT](../summaries/conservation_vs_fitness__REPORT.md).

[^metal_resistance_global_biogeography]: [metal resistance global biogeography](../summaries/metal_resistance_global_biogeography__REPORT.md)
[^pgp_pangenome_ecology]: [pgp pangenome ecology](../summaries/pgp_pangenome_ecology__REPORT.md)
[^conservation_vs_fitness]: [conservation vs fitness](../summaries/conservation_vs_fitness__REPORT.md)
[^prophage_amr_comobilization]: [prophage amr comobilization](../summaries/prophage_amr_comobilization__REPORT.md)
