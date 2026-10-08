---
type: "Method"
description: "Procrustes analysis is an ordination-alignment method used in BERIL projects to test whether community or functional configurations correspond to physical layouts or to each other."
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/harvard_forest_warming__REPORT.md"]
---
In this corpus, Procrustes analysis (also called Procrustes superimposition or Procrustes alignment) is used to test whether one multivariate configuration, such as a community ordination, lines up with another, such as a physical sampling grid or a paired data layer. [src: enigma_sso_asv_ecology, harvard_forest_warming]

## Uses in the corpus

### SSO sediment communities versus the physical well grid

Across the 9 [[entities/sso]] wells (3×3 grid, ~6 m span), sediment-associated communities show significant distance-decay of similarity by [[entities/mantel-test]] (Spearman ρ = 0.323, p = 0.029, 9,999 permutations). The [[entities/nmds]] ordination fits well (stress 0.067), but Procrustes analysis finds only marginal correspondence between the community ordination and the physical grid (m² = 0.379, p = 0.080). This Procrustes result does not reach the conventional p < 0.05 threshold, so the grid-shaped arrangement of the community ordination is weaker evidence than the Mantel distance-decay signal from the same nine wells. See [[summaries/enigma_sso_asv_ecology__REPORT]]. [src: enigma_sso_asv_ecology]

The project's figure `procrustes_overlay.png` is a Procrustes superimposition of the community ordination onto the well grid. It shows directly how the ordination positions line up with grid geometry. [src: enigma_sso_asv_ecology]

### Harvard Forest DNA versus RNA functional pools

At [[entities/harvard-forest]], the notebook `04_dna_vs_rna_divergence.ipynb` ran a paired n=25 [[entities/permanova]] on DNA and RNA KO (KEGG Orthology gene-family) pools, together with a Procrustes alignment test. The test asks whether the metagenomic and metatranscriptomic functional configurations correspond. The supplied evidence records only that the test was run and its sample size; it does not give the Procrustes statistic or its significance. See [[summaries/harvard_forest_warming__REPORT]]. [src: harvard_forest_warming]

## Evidence strength

The only Procrustes outcome reported in the assigned evidence is the marginal SSO grid correspondence. It comes from a single small grid of wells and should not be read as an established spatial structuring of community composition. [src: enigma_sso_asv_ecology]

The Harvard Forest use documents that the method was applied, not what it found. [src: harvard_forest_warming]
