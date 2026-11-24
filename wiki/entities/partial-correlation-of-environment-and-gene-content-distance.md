---
type: "Method"
description: "Partial correlation between pairwise gene-content distance and environmental distance while controlling for phylogenetic distance (ANI), used to separate environmental and phylogenetic effects; stops at plain Mantel tests."
sources: ["summaries/ecotype_analysis__REPORT.md", "summaries/ecotype_env_reanalysis__REPORT.md"]
aliases: ["Partial correlation of distance matrices", "partial Mantel-style correlation", "partial correlation"]
---
# Partial correlation of environment and gene content distance

In the original ecotype analysis of 172 species, the median partial correlation for environment was 0.0025, and phylogeny dominated in 60.5% of species. [src: ecotype_analysis] The reanalysis gave a much higher median of 0.081 across 183 species. It found no stronger environmental signal in environmental than in human-associated species. [src: ecotype_env_reanalysis] The report says the absolute values of the two analyses are not comparable. [src: ecotype_env_reanalysis]

## Key facts

- In the original ecotype analysis ([[summaries/ecotype_analysis__REPORT]]), the median partial correlation for environment was 0.0025 across 172 species. [src: ecotype_analysis]
- The same analysis reported a median partial correlation for phylogeny of 0.0143. [src: ecotype_analysis]
- Phylogeny dominated in 60.5% of species, and environment dominated in 39.5%. [src: ecotype_analysis]

## Reanalysis and group comparison

In the reanalysis ([[summaries/ecotype_env_reanalysis__REPORT]]), the median partial correlation across all 183 species was 0.081, compared with 0.003 in the original analysis. [src: ecotype_env_reanalysis] Environmental species (n=37, median 0.051) did not show stronger environment–gene content correlations than human-associated species (n=93, median 0.084). The one-sided Mann-Whitney U test gave U=1536, p=0.83. [src: ecotype_env_reanalysis]

## Caveats

- Partial correlations assume linear relationships between distance matrices, so they may miss nonlinear ecological effects. [src: ecotype_analysis]
- The reanalysis omitted genome downsampling. The report says this changes the distance distributions, and that larger genome sample sizes detect weaker correlations. [src: ecotype_env_reanalysis]
- Omitting downsampling gave 27x higher overall partial correlations than the original analysis. The report says the absolute values are not comparable. It says the group comparison remains valid because both groups use the same methodology. [src: ecotype_env_reanalysis]
