---
type: "Method"
description: "Nonparametric multi-group test across environments or categories, reported with eta-squared effect sizes; does not cover two-group tests or multiple-testing corrections."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/cazyme_pangenome_ecology__REPORT.md", "summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
aliases: ["BH-FDR", "KW", "Kruskal-Wallis", "Mann–Whitney"]
---
# Kruskal-Wallis test with eta-squared effect size

This page covers the Kruskal-Wallis (KW) test with eta-squared effect size. Four projects use KW to compare measures across environments, biomes or ecosystem types. [src: amr_environmental_resistome, cazyme_pangenome_ecology, euk_in_prok_correlates, nmdc_community_metabolic_ecology] Very small p-values appear throughout. In the AMR project, where η² is reported, the effect sizes are modest. [src: amr_environmental_resistome]

## Key facts

- The AMR report reads its η² values of 0.02–0.13 as environment explaining 2-13% of variance in antimicrobial resistance (AMR) composition. [src: amr_environmental_resistome]
- Benjamini-Hochberg false discovery rate (BH-FDR) correction is applied alongside KW in the CAZyme, eukaryote and metabolic-ecology projects. [src: cazyme_pangenome_ecology, euk_in_prok_correlates, nmdc_community_metabolic_ecology]
- The NMDC eukaryote analysis uses KW and Mann–Whitney tests with BH-FDR, or cross-validated gradient boosting with GroupKFold by study. It does this because of zero inflation and batch structure. [src: euk_in_prok_correlates]

## AMR gene content by environment

Across bacterial species, each AMR measure tested differed by environment. [src: amr_environmental_resistome] The report describes the effect sizes as modest, despite the very small p-values. [src: amr_environmental_resistome] See [[concepts/environmental-structuring-of-antimicrobial-resistance-gene-content]] and [[summaries/amr_environmental_resistome__REPORT]].

| Outcome | KW H | p | η² |
|---|---|---|---|
| AMR count | 781.9 | 9.4×10⁻¹⁶⁷ | 0.056 [src: amr_environmental_resistome] |
| Core AMR % | 506.0 | 4×10⁻¹⁰⁷ | 0.036 [src: amr_environmental_resistome] |
| Metal resistance | 1498.4 | ~0 | 0.107 [src: amr_environmental_resistome] |
| Target modification | 1394.9 | 1.7×10⁻²⁹⁹ | 0.100 [src: amr_environmental_resistome] |
| Efflux | 768.0 | 9.8×10⁻¹⁶⁴ | 0.055 [src: amr_environmental_resistome] |
| Enzymatic inactivation | 266.0 | 2.0×10⁻⁵⁵ | 0.019 [src: amr_environmental_resistome] |

Clinical species have a median of 5 AMR gene clusters, against 2 for soil, aquatic and host-associated species. [src: amr_environmental_resistome] Clinical species have 68% accessory (acquired) AMR, against 43% in soil species. [src: amr_environmental_resistome]

The report cautions that phylogeny likely explains much more variance than environment does. [src: amr_environmental_resistome] See [[concepts/phylogenetic-confounding-of-environment-amr-associations]].

## CAZyme classes across biomes

All 6 non-zero CAZy classes differed across 18 biomes, with all p < 10^-150 after BH-FDR correction. [src: cazyme_pangenome_ecology] The CL class was all zeros and was excluded. [src: cazyme_pangenome_ecology] The effect survived genome-size correction, which used KW on per-Mbp residuals. It was also significant within all 5 top phyla: Pseudomonadota, Firmicutes_A, Bacteroidota, Bacillota_A and Actinomycetota. [src: cazyme_pangenome_ecology] The results are stored in a 7-row table. [src: cazyme_pangenome_ecology] See [[concepts/biome-level-carbohydrate-active-enzyme-repertoire-differentiation]] and [[summaries/cazyme_pangenome_ecology__REPORT]].

| CAZy class | H | BH-adjusted p |
|---|---|---|
| GT | 12,524 | ≈ 0 [src: cazyme_pangenome_ecology] |
| GH | 7,793 | ≈ 0 [src: cazyme_pangenome_ecology] |
| CB | 7,527 | ≈ 0 [src: cazyme_pangenome_ecology] |
| CE | 2,584 | ≈ 0 [src: cazyme_pangenome_ecology] |
| PL | 893 | 1.1 × 10^-180 [src: cazyme_pangenome_ecology] |
| AA | 767 | 8.3 × 10^-154 [src: cazyme_pangenome_ecology] |

## Eukaryotic fraction in NMDC metagenomes

The NMDC eukaryotic fraction differs across sample matrices (H=77.8, p=1.3×10⁻¹⁷). [src: euk_in_prok_correlates] All pairwise matrix contrasts are significant after BH-FDR. [src: euk_in_prok_correlates] The report calls this association strong but confounded. [src: euk_in_prok_correlates] See [[concepts/study-and-batch-confounding-of-cross-collection-metadata-correlates]].

Within the NEON soil study, the eukaryotic fraction varies with local vegetation across 11 env_local_scale levels (H=119.1, p=7.6×10⁻²¹). [src: euk_in_prok_correlates] It also varies across 47 sites (H=310.4, p=2.4×10⁻⁴⁶). [src: euk_in_prok_correlates] See [[concepts/within-study-environmental-drivers-of-eukaryotic-dna-in-soil-metagenomes]].

## Community metabolic completeness by ecosystem

BH-FDR-corrected KW tests found ecosystem differences in community completeness for 17 of 18 amino acid pathways (q < 0.05). [src: nmdc_community_metabolic_ecology] The largest differences were in glycine (H = 92.98, q = 1.2×10⁻¹⁹) [src: nmdc_community_metabolic_ecology], asparagine (H = 66.19, q = 3.8×10⁻¹⁴) [src: nmdc_community_metabolic_ecology] and cysteine (H = 62.66, q = 1.5×10⁻¹³). [src: nmdc_community_metabolic_ecology] Tyrosine was the only pathway without significant differentiation (q = 0.71). [src: nmdc_community_metabolic_ecology]

In the ecosystem principal component analysis (PCA), PC1 explained 49.4% of variance and differed across ecosystem types (H = 52.98, p < 0.0001). [src: nmdc_community_metabolic_ecology] PC2 explained 16.6% and also differed (H = 123.74, p < 0.0001). [src: nmdc_community_metabolic_ecology] See [[concepts/ecosystem-differentiation-of-community-metabolic-potential]].
