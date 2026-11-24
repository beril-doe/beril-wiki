---
type: "Method"
description: "Distance-matrix correlation test used to relate environmental embedding distance to AMR composition distance."
sources: ["summaries/amr_environmental_resistome__REPORT.md", "summaries/amr_strain_variation__REPORT.md", "summaries/discoveries.md", "summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/metal_cross_resistance__REPORT.md"]
aliases: ["Mantel tests"]
---
# Mantel test

This page covers the Mantel test, a distance-matrix correlation test used to relate environmental embedding distance to AMR (antimicrobial resistance) composition distance. The corpus also uses it to compare ANI (average nucleotide identity) distance matrices with AMR Jaccard distance matrices, to test spatial turnover, and to test cross-resistance structure. [src: amr_environmental_resistome, amr_strain_variation, enigma_sso_asv_ecology, metal_cross_resistance]

## Key facts

- Used in four projects: amr_environmental_resistome, amr_strain_variation, enigma_sso_asv_ecology and metal_cross_resistance. [src: amr_environmental_resistome, amr_strain_variation, enigma_sso_asv_ecology, metal_cross_resistance]

## Environment and AMR composition

A Mantel test finds that cosine distance of AlphaEarth embeddings predicts Bray-Curtis distance of AMR mechanism fractions (r = 0.098, p = 0.001). [src: amr_environmental_resistome] See [[entities/alphaearth-environmental-embeddings]] and [[concepts/environmental-and-clinical-distribution-of-antimicrobial-resistance]].

## Phylogenetic signal of AMR genes

Mantel tests compared ANI distance matrices with AMR Jaccard distance matrices across 1,261 species. [src: amr_strain_variation] Of these, 55.6% (701 species) show significant phylogenetic signal (FDR, false discovery rate, < 0.05). [src: amr_strain_variation] The median Mantel r is 0.247. [src: amr_strain_variation] 87.8% of species show a positive correlation. [src: amr_strain_variation]

Non-core (putatively acquired) AMR genes show stronger signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117). The paired t-test gave t = -8.35, p = 7.0e-16, n = 489. [src: amr_strain_variation, discoveries] The report calls this counter-intuitive. It also notes that core genes are nearly universal (>=95% prevalence by definition). Their Jaccard distances are near zero with little variance, which suppresses distance-based metrics such as Mantel r. This artifact partially explains the lower signal independently of biology. [src: amr_strain_variation] See [[concepts/intrinsic-versus-acquired-resistance-gene-conservation]] and [[concepts/phylogenetic-signal-of-gene-content-and-traits]].

## Spatial structure in subsurface communities

Sediment communities across the 9 SSO wells (3×3 grid, ~6 m span) show significant distance-decay of similarity (Mantel Spearman ρ = 0.323, p = 0.029, 9,999 permutations). [src: enigma_sso_asv_ecology] Turnover is not aligned with the hillslope (uphill-downhill ρ = −0.049, p = 0.580). [src: enigma_sso_asv_ecology] Turnover is larger along the east-west axis (ρ = 0.227) than uphill-downhill (ρ = −0.049). [src: enigma_sso_asv_ecology] The east-west column Mantel ρ = 0.227 has p = 0.092. The report reads this as pointing to a lateral structuring force rather than topography-driven hydrology. [src: enigma_sso_asv_ecology] See [[entities/distance-decay]] and [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]].

For groundwater, distance matrices from two sampling dates correlated at ρ = 0.867 (p = 0.001). Between-well similarity patterns were nearly identical across dates. [src: enigma_sso_asv_ecology] See [[concepts/temporal-stability-of-groundwater-communities]].

## Metal cross-resistance

Mantel tests across 351 organism pairs gave mean r = 0.23 with 62% positive. The report describes this as moderate but consistent conservation of cross-resistance architecture. [src: metal_cross_resistance] The pairwise results are in data/mantel_test_results.csv (351 rows). [src: metal_cross_resistance] See universal positivity and chemistry specific magnitude of metal cross resistance.

## Sources

[[summaries/amr_environmental_resistome__REPORT]], [[summaries/amr_strain_variation__REPORT]], [[summaries/discoveries]], [[summaries/enigma_sso_asv_ecology__REPORT]], [[summaries/metal_cross_resistance__REPORT]].
