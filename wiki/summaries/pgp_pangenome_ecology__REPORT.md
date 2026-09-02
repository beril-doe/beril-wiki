---
type: "Summary"
description: "Pangenome-scale analysis of PGP gene ecology, co-occurrence, and inheritance"
doc_type: "short"
full_text: "sources/pgp_pangenome_ecology__REPORT.md"
---
# PGP Gene Distribution Across Environments & Pangenomes

## Overview

This report analyzes plant-growth-promoting (PGP) gene distribution, co-occurrence, environmental enrichment, and core/accessory status across the BERDL pangenome. Among 27,702 total species, 11,272 carried at least one of 13 PGP gene markers; the analysis included 32,736 PGP gene clusters, 27,690 species with GapMind pathway scores, and 291,279 genomes with isolation-source metadata. [src: pgp_pangenome_ecology]

## Key Findings

### PGP co-occurrence and ecological guilds

Eight of 10 focal-gene pairs were significantly associated after Benjamini–Hochberg false-discovery-rate (BH-FDR) correction: five pairs showed positive co-occurrence and three showed negative co-occurrence. The strongest positive association was pqqC × acdS, with OR = 7.24, n = 286 co-occurring species, and q = 1.2e-83. pqqC also co-occurred significantly with hcnC (OR = 1.91) and ipdC (OR = 1.55), forming a putative rhizosphere-effectiveness module. [src: pgp_pangenome_ecology]

nifH was negatively associated with hcnC (OR = 0.23, q = 5.8e-29) and pqqC (OR = 0.57, q = 2.9e-19), and showed no significant association with ipdC (OR = 1.13, q = 0.54). These results support ecological separation between diazotrophs and pqqC/acdS-bearing rhizobacteria, with the classical PGPB suite appearing primarily non-diazotrophic in this dataset. [src: pgp_pangenome_ecology]

Only 157 species (1.4%) carried at least three focal traits. The most common multi-trait genotype was pqqC + acdS (n = 153), followed by nifH + pqqC (n = 225), although nifH and pqqC were negatively associated overall. [src: pgp_pangenome_ecology]

### Environmental enrichment

Comparing 1,039 soil/rhizosphere species with 10,233 species from other environments, acdS, pqqC, and hcnC were significantly enriched in soil after BH-FDR correction. acdS prevalence was 15.8% in soil/rhizosphere species versus 2.6% in other species (OR = 7.02, q = 5.1e-62); pqqC prevalence was 43.8% versus 21.2% (OR = 2.90, q = 2.8e-53); and hcnC prevalence was 11.3% versus 6.4% (OR = 1.85, q = 6.1e-08). [src: pgp_pangenome_ecology]

nifH was depleted in soil-classified species, with prevalence of 12.9% in soil/rhizosphere species versus 19.7% in other species (OR = 0.60, q = 5.5e-08). ipdC was not significantly enriched in the raw comparison (soil prevalence 1.5%, other prevalence 1.9%, OR = 0.79, q = 0.47). [src: pgp_pangenome_ecology]

The acdS enrichment remained strong after phylum-level fixed effects in logistic regression (OR = 6.98, p = 4.8e-61) and in a strict rhizosphere-only sensitivity analysis using genomes with “rhizosphere” or “root nodule” in their isolation source (OR = 10.6, q = 7.6e-38). Bacillota_A was an exception for nifH, showing enrichment in soil (OR = ∞, q = 2.5e-4). [src: pgp_pangenome_ecology]

### Core, accessory, and singleton status

The hypothesis that PGP genes are predominantly horizontally transferred accessory genes was rejected. All 13 PGP genes had significantly higher core fractions than the genome-wide baseline of 46.8% core, with BH-FDR q < 0.05 for all genes. pqqC was 81.5% core, 7.8% auxiliary, and 10.7% singleton (q = 0.0); pqqB was 78.1% core, 8.9% auxiliary, and 13.0% singleton (q = 3.0e-247); hcnA was 78.5% core, 10.8% auxiliary, and 10.8% singleton (q = 9.2e-37); ipdC was 76.5% core, 9.7% auxiliary, and 13.7% singleton (q = 3.4e-19); acdS was 70.4% core, 13.4% auxiliary, and 16.2% singleton (q = 7.9e-25); nifH was 63.8% core, 15.1% auxiliary, and 21.0% singleton (q = 4.3e-71); and pqqD was 55.5% core, 17.0% auxiliary, and 27.5% singleton (q = 2.2e-86). [src: pgp_pangenome_ecology]

The mean accessory fraction across all PGP genes was 29.7%, compared with 53.2% genome-wide. Pangenome openness, measured by singleton fraction, correlated negatively with PGP gene richness (Spearman ρ = −0.195, p = 2.0e-97, n = 11,272 species with ≥2 genomes), consistent with PGP-rich species having more closed pangenomes. [src: pgp_pangenome_ecology]

pqqD was an outlier, with the lowest reported core fraction among the highlighted genes (55.5%) and the highest singleton fraction (27.5%), suggesting that it can sometimes spread as a standalone gene; the functional pqqB–pqqC unit was predominantly core in this analysis. [src: pgp_pangenome_ecology]

### Tryptophan completeness and ipdC

Completeness of the tryptophan biosynthesis pathway, assessed with GapMind, predicted ipdC presence: ipdC occurred in 2.5% of species with a complete pathway (GapMind score ≥ 0.9) versus 0.9% of species with an incomplete pathway (Fisher OR = 2.81, p = 6.3e-10). A logistic model using tryptophan completeness alone gave OR = 2.81, 95% CI 1.97–4.01, p = 1.4e-08, n = 11,272; adding soil status gave OR = 2.87, p = 7.0e-09. [src: pgp_pangenome_ecology]

The tyrosine pathway also predicted ipdC presence at a similar effect size (OR = 3.62, p = 2.3e-11), so the result does not support a tryptophan-specific mechanism. The report interprets this as consistent with TyrR regulation of ipdC in Enterobacter cloacae, because TyrR responds to tryptophan, tyrosine, and phenylalanine. [src: pgp_pangenome_ecology]

The tryptophan–ipdC association reversed within soil/rhizosphere species (n = 1,039), where the OR was 0.30 (p = 0.02), while remaining positive in non-soil species (n = 10,233; OR = 3.56, p = 7.7e-13). The report treats the soil reversal as hypothesis-generating and suggests that soil PGPB may obtain aromatic amino acids from plant exudates while retaining ipdC for indole-3-acetic-acid production from plant-supplied substrate. [src: pgp_pangenome_ecology]

A phylum-plus-soil logistic model failed because of quasi-complete separation caused by the rarity of ipdC, which occurred in 214 species (1.9%). [src: pgp_pangenome_ecology]

### Overall interpretation

Together, the co-occurrence and environmental analyses support a non-diazotrophic pqqC + acdS module as a stable, specialized rhizosphere niche marker: pqqC and acdS were tightly co-selected (OR = 7.24), acdS was strongly soil-enriched (OR = 7.02), and PGP genes were predominantly core rather than accessory. nifH represented a separate ecological guild with different co-occurrence partners and environmental distribution. [src: pgp_pangenome_ecology]

The report identifies pqqD as a partial exception to the vertical-inheritance pattern and notes that the nifH count was 2,756 rather than the approximately 1,913 estimated in the research plan, reflecting incremental growth in the GTDB r214 pangenome; the discrepancy did not affect the analyses. [src: pgp_pangenome_ecology]

## Caveats

Environment classification was conservative and noisy: only 1,637 species (5.9% of species with an environment label) were classified as soil/rhizosphere dominant, while 291,279 genomes had isolation-source metadata and 93.5% were classifiable. The report states that NCBI is biased toward clinical and host-associated sampling and that the acdS and pqqC enrichment effects may therefore underestimate true rhizosphere enrichment. [src: pgp_pangenome_ecology]

PGP detection relied on Bakta gene annotations matching exact gene names such as nifH, acdS, and pqqC. Product-only annotations and variant gene names could be missed, particularly for less-characterized PGP genes. [src: pgp_pangenome_ecology]

Gene-cluster annotations were not functionally validated: truncations, frameshifts, and pseudogenization were not filtered, so a cluster annotated as pqqC was not necessarily functional. [src: pgp_pangenome_ecology]

ipdC was rare, occurring in only 214 of 11,272 species (1.9%), which limited statistical power for the stratified H4 analysis; the soil reversal (OR = 0.30, p = 0.02) should therefore be treated as hypothesis-generating rather than conclusive. [src: pgp_pangenome_ecology]

GapMind tryptophan and tyrosine completeness scores may proxy for overall metabolic pathway completeness. The report states that genome size, COG coverage, or total pathway count should be controlled to separate aromatic-pathway-specific effects from general metabolic capacity. [src: pgp_pangenome_ecology]

The report also notes that co-occurrence does not establish physical linkage: whether pqqC and acdS occupy the same genomic island, operon, or separate loci remains unresolved. It proposes operonic-context analysis, deeper nifH ecological stratification, a controlled ipdC model, focused hcnA–hcnC phylogeny, and comparison with commercial inoculant strains as next steps. [src: pgp_pangenome_ecology]

## Slots Into

- [[concepts/pangenome-integration]] — PGP genes were predominantly core, and PGP gene richness correlated negatively with pangenome openness, providing evidence about genome organization and inheritance. [src: pgp_pangenome_ecology]
- [[concepts/ecotype-environment-gene-content]] — Soil/rhizosphere environments enriched acdS, pqqC, and hcnC while depleting nifH, linking environment to gene content and ecological guild structure. [src: pgp_pangenome_ecology]
- [[concepts/gene-function-acquisition-depth]] — Core/accessory distributions and the openness correlation constrain whether PGP traits are vertically inherited or laterally acquired. [src: pgp_pangenome_ecology]
- [[concepts/environmental-resistome]] — The report extends environment-stratified gene-distribution analysis to plant-growth-promoting traits, especially the soil enrichment of acdS, pqqC, and hcnC. [src: pgp_pangenome_ecology]
