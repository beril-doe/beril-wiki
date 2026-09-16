<!-- tension-hash: 16573a145d4550d5 -->
# Plant Compartment Effects on Functional Gene Content: Small Real Signal or Sampling-Driven Magnitude?

The plant compartment analysis bears directly on [[concepts/ecotype-environment-gene-content]] because its two analysis stages give different headline magnitudes and different readings. If the stages are conflated, the earlier figure can be misread as describing the refined result, or a large compartment effect can be claimed against the corpus's broad environmental null. This page keeps the two stages apart and records what each supports.

## Evidence Sides

**Refined 17-marker analysis: a small but real compartment effect**

In the refined 17-marker analysis, compartment profiles differed at a PERMANOVA (permutational multivariate analysis of variance, which tests whether groups differ in a distance space; its R² can reflect both centroid location and within-group dispersion) R² (fraction of variance explained) of 0.071. [src: plant_microbiome_ecotypes] The db-RDA (distance-based redundancy analysis, a constrained ordination that isolates location effects) location-only R² was 0.060, p (permutation p-value, the probability of a result at least this strong under randomly shuffled group labels) = 0.001. [src: plant_microbiome_ecotypes] Of the PERMANOVA R², 84% was centroid shift and 16% was dispersion. [src: plant_microbiome_ecotypes] The project reads this as a small but real compartment effect. [src: plant_microbiome_ecotypes]

**Earlier 25-marker analysis: a large R² attributed mainly to taxonomic sampling**

In the earlier 25-marker analysis, R² = 0.527 fell to a residual R² = 0.072 once the three genome-rich species per compartment were excluded. [src: plant_microbiome_ecotypes; ecotype_env_reanalysis] That project attributed the drop mainly to taxonomic sampling. The 0.072 figure belongs to this earlier stage and does not describe the refined analysis. [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]

**Broad environmental null context**

Neither stage amounts to a large community-wide environment effect alongside the broad environmental null. [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]

## Possible Reconciliations

- *Hypothesis:* Both stages detect the same modest compartment signal. The earlier stage's headline was inflated by a few genome-rich species, and its residual value is similar to the refined PERMANOVA R² only by coincidence, because the marker panels differ.
- *Hypothesis:* Part of the refined effect is still taxonomic. Lineage composition could produce centroid shift without compartment-specific selection on gene content. If so, the "small but real" effect would be smaller once phylogeny is controlled.
- *Hypothesis:* A compartment effect and a broad environmental null can both hold. Compartment may be a sharper contrast than the environment categories used in the broader null, so a small, real effect in one setting would not contradict weak effects elsewhere.

## Resolving Work

- Rerun PERMANOVA and db-RDA on the refined 17-marker panel, excluding the three genome-rich species per compartment. This tests whether the refined effect survives the same sensitivity check that collapsed the earlier headline.
- Repeat the compartment test with phylogenetic control, using a phylogeny-aware distance (one that discounts gene-content differences explained by evolutionary relatedness) or a genus-level block permutation (shuffling compartment labels only within each genus, so lineage composition stays fixed). This tests whether the centroid-shift share reflects compartment or lineage.
- Run the 25-marker and 17-marker panels side by side on an identical species set. This would separate the effect of the panel change from the effect of species exclusion on R².
- Apply the partial-correlation framework (correlation between two variables after controlling for others) from the ecotype environment reanalysis to the plant-compartment species. This tests whether compartment behaves differently from the broad environment categories behind the null.
