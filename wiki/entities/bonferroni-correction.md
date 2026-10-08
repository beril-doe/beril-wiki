---
type: "Method"
description: "Bonferroni correction is a family-wise multiple-testing correction that divides the significance level by the number of tests in a family; in this corpus it sets confirmatory thresholds in the gene-function agora, MicrobeAtlas metal-ecology and SNIPE defense-system projects."
sources: ["summaries/gene_function_ecological_agora__REPORT.md", "summaries/microbeatlas_metal_ecology__REPORT.md", "summaries/snipe_defense_system__REPORT.md"]
---
# Bonferroni correction

Bonferroni correction is a family-wise multiple-testing correction. It divides the nominal significance level by the number of tests in a pre-defined family, and each test must pass that stricter threshold. In this corpus it sets confirmatory thresholds in three projects: a horizontal-gene-transfer atlas, a phylogenetically controlled metal-ecology analysis and a phage-defense niche analysis. One audit applies it alongside Benjamini-Hochberg false-discovery-rate (FDR, the expected share of false positives among called results) control [src: gene_function_ecological_agora, microbeatlas_metal_ecology, snipe_defense_system].

## Use in the gene-function ecological agora

The project tests only 4 pre-registered hypotheses (Bacteroidota PUL; Mycobacteriota mycolic; Cyanobacteria PSII; Alm 2006 r ≈ 0.74), which gives a Bonferroni threshold of α = 0.05 / 4 = 0.0125. The report says all the significant findings it cites survive this threshold "trivially": NB12 mycolic-acid p<10⁻⁶, NB16 PSII class p<10⁻⁵ and P4-D1 enrichments all p<10⁻¹¹ [src: gene_function_ecological_agora].

Correction was applied separately within each test family (NB11 4 tests at α/4, NB12 4 tests at α/4, NB16 4 tests at α/4). Atlas-wide multiple testing across 13.7M scores was not corrected this way. The report describes it as exploratory by design, so atlas-wide scores should not be read as Bonferroni-confirmed [src: gene_function_ecological_agora].

At the [[entities/cyanobacteriia]] class rank, both pre-registered [[entities/photosystem-ii]] (PSII) criteria pass at α/4 = 0.0125. For the producer criterion, PSII scores sit above the atlas non-housekeeping median, with a very large effect (d=1.50). For the consumer criterion, they also sit above that median, with a moderate-large effect (d=0.70). In other words, PSII KOs are less phylogenetically clumped than typical non-housekeeping KOs at class rank. The report treats the hypothesis as supported but donor-undistinguished, so passing the correction does not identify transfer donors [src: gene_function_ecological_agora].

Caveat: the report calls the Cyanobacteria–PSII n=21 sample size and its rank-dependent contradictions a real concern. It still calls the class-rank result statistically defensible (α=2×10⁻⁵ for producer, 2×10⁻⁴ for consumer, both below Bonferroni α/4=0.0125), arguing that the very large effect d=1.50 balances the small n. The correction does not remove the rank dependence itself [src: gene_function_ecological_agora].

A review had suggested correcting for multiple testing. In response, notebook NB30 listed all formally tested significance claims, grouped them into test families, and applied both family-wise Bonferroni and [[entities/benjamini-hochberg-fdr]] corrections, reporting survival under each [src: gene_function_ecological_agora].

Result: 14 of 16 formal hypothesis tests survive family-wise Bonferroni. The 2 tests that do not survive are null results the project had already reported as such [src: gene_function_ecological_agora].

- Family 1, pre-registered hypotheses: 4 tests, 4 surviving (100%) [src: gene_function_ecological_agora]
- Family 2, P4-D1 biome enrichment: 6 tests, 5 surviving (83%) [src: gene_function_ecological_agora]
- Family 3, P4-D5 residualization replication: 6 tests, 5 surviving (83%) [src: gene_function_ecological_agora]
- Total formal tests: 16 tests, 14 surviving (88%) [src: gene_function_ecological_agora]

Surviving Bonferroni is not the same as supporting a hypothesis. In the NB30 Family 1 table, the Alm 2006 r ≈ 0.74 reproduction test survives the correction (raw p 1×10⁻⁴³) but its verdict is NOT REPRODUCED. The p-value is significant because of the large n, while the observed r=0.10–0.29 is too small to reproduce the original correlation. The "4 of 4 survive" count therefore covers corrected significance, not four confirmed hypotheses [src: gene_function_ecological_agora].

The report's own PSII p-values do not agree with one another, and it does not reconcile them. The earlier summary gives PSII class p<10⁻⁵, and the review response gives 2×10⁻⁵ for the producer test and 2×10⁻⁴ for the consumer test. The NB30 audit instead reports p 2.1×10⁻⁵ for the H3 Cyanobacteria PSII class hypothesis, which is not below 10⁻⁵. NB30 also gives 2.3×10⁻⁵ for the residualized consumer test at class rank. Every version still passes α/4 = 0.0125, but the exact p-values should be cited per analysis rather than as one settled number [src: gene_function_ecological_agora].

## Use in MicrobeAtlas metal ecology

This analysis controls for phylogenetic structure with [[entities/phylogenetic-generalized-least-squares]] (PGLS, regression with phylogenetically correlated residuals) in n = 606 genera with AMR data. After that control, the number of distinct metal types a genus resists is the only metal AMR predictor that survives Bonferroni correction (β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴; threshold p < 0.0083 for 6 models) [src: microbeatlas_metal_ecology].

The report's correction scheme covers ~47 tests in total [src: microbeatlas_metal_ecology]:

- 6 simple confirmatory PGLS models, corrected by Bonferroni (α/6 = 0.0083) [src: microbeatlas_metal_ecology].
- 6 Pagel's λ tests, also labelled confirmatory, assessed by likelihood-ratio test with no additional correction [src: microbeatlas_metal_ecology].
- A multi-predictor PGLS (3 predictors in 1 model), not corrected beyond the model [src: microbeatlas_metal_ecology].
- Exploratory only: robustness R1–R2 and R4–R6 (9 coefficients), archaeal PGLS R3 (3 coefficients), sensitivity S1–S5 (24 coefficients) and an OTU abundance filter S5 (1 test) [src: microbeatlas_metal_ecology].

Because the confirmatory λ tests are uncorrected, the family-wise control does not cover every confirmatory test [src: microbeatlas_metal_ecology].

The primary result (p = 1.5×10⁻⁴) also falls below a Bonferroni threshold for the full 47-test family (0.05/47 ≈ 0.0011). The report notes this was not its stated correction method and presents it as an upper-bound robustness check [src: microbeatlas_metal_ecology].

Across rarefaction iterations, 57.5% reached Bonferroni significance (p < 0.0083). The primary result therefore did not clear the threshold in every resampled iteration, which is a robustness caveat on the headline association [src: microbeatlas_metal_ecology].

## Use in the SNIPE defense-system analysis

Species carrying the [[entities/snipe-defense-system]] occupy statistically distinct environmental niches: they differ in 22/64 [[entities/alph-aearth]] embedding dimensions at p < 0.05 after Bonferroni correction. The supplied evidence does not say how large the corrected test family was beyond these dimensions [src: snipe_defense_system].

## Related

- [[entities/benjamini-hochberg-fdr]]
- [[entities/phylogenetic-generalized-least-squares]]
- cohens d
- [[summaries/gene_function_ecological_agora__REPORT]]
- [[summaries/microbeatlas_metal_ecology__REPORT]]
- [[summaries/snipe_defense_system__REPORT]]
