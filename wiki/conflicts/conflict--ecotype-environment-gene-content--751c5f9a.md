<!-- tension-hash: 751c5f9aeeea664a -->
# Does Metal Type Diversity Shape Microbial Niche Breadth and Gene Content, or Do Individual Metals Drive Functional Shifts?

This page records a tension within [[concepts/ecotype-environment-gene-content]]. MicrobeAtlas found metal type diversity associated with niche breadth, meaning the range of environments a lineage occupies, whereas the broad environmental comparison was null and the strict prevalence analysis was non-significant. [src: microbeatlas_metal_ecology; ecotype_env_reanalysis] A soil-metal study found strong metal–function associations, but because several metals co-vary and partial-correlation analyses remain pending, it cannot separate metal type diversity from individual metal concentrations as drivers of functional shifts. [src: soil_metal_functional_genomics] Whether "metal exposure" means breadth of metal types or concentration of specific metals changes which mechanisms and which analyses the corpus should pursue.

## Evidence Sides

**Metal type diversity is associated with niche breadth.** MicrobeAtlas found metal type diversity associated with niche breadth. [src: microbeatlas_metal_ecology; ecotype_env_reanalysis]

**Null and non-significant results in other analyses.** The broad environmental comparison was null. The strict prevalence analysis was non-significant at p = 0.092, where p is the probability of a result at least this extreme if no true association exists. Strict prevalence refers to applying a stricter prevalence cutoff when counting a taxon toward niche breadth. [src: microbeatlas_metal_ecology; ecotype_env_reanalysis] A non-significant result is not evidence that the association is absent.

**Strong metal–function signal, but drivers unresolved.** The soil-metal study found strong associations between metals and COGs (Clusters of Orthologous Groups, gene families grouped by shared function). Chromium, copper, lead and zinc co-vary in these samples. Partial-correlation analyses, which estimate each metal's association while holding the others constant, remain pending. The study therefore does not resolve whether metal type diversity or individual metal concentrations drive functional shifts. [src: soil_metal_functional_genomics]

## Possible Reconciliations

- *Hypothesis:* The diversity–niche-breadth signal is real but weak. Under this hypothesis it would reach significance only with the less restrictive definition of niche breadth, and lose significance under strict prevalence filtering because fewer taxa are retained.
- *Hypothesis:* Metal type diversity stands in for co-occurring individual metals. If so, the MicrobeAtlas association and the soil-metal COG associations reflect the same underlying concentration effects of a few dominant metals.
- *Hypothesis:* Metal effects are specific to particular metals and environments. On this view they are diluted in broad environmental comparisons, which would explain the null result there, while still appearing in focused soil datasets.

## Resolving Work

- **Partial correlations in the soil data.** Run the pending partial-correlation analyses on the soil-metal COG dataset, controlling for co-varying chromium, copper, lead and zinc. This tests whether any single metal's association with COGs survives once the others are held constant.
- **Niche-breadth sensitivity analysis.** Recompute MicrobeAtlas niche breadth across a graded series of prevalence thresholds. This tests whether the association with metal type diversity weakens smoothly with sample size or disappears abruptly.
- **Leave-one-metal-out models.** Fit niche-breadth models that drop one metal at a time from the diversity count. This tests whether "diversity" is driven by one or two individual metals.
- **Shared samples across projects.** Find samples present in both the soil-metal and MicrobeAtlas data, and fit metal type count and individual metal concentrations as competing predictors of COG profiles. This tests which formulation explains more functional variation.
- **Stratified environmental comparison.** Repeat the broad environmental comparison within individual environment types. This tests whether the null result reflects heterogeneity across environments that masks metal-specific effects.
