<!-- tension-hash: 744fe541f5a71c61 -->
# Broad Environmental Null versus Subsystem-Specific Environmental Signals in Gene Content

Projects in [[concepts/ecotype-environment-gene-content]] disagree on where environmental signals in microbial gene content appear. A broad reanalysis of gene-content similarity found that environmental species did not show stronger environment–gene-content correlations than human-associated species, while prophage-module analyses reported environment effects within a specific functional subsystem [src: ecotype_env_reanalysis; prophage_ecology]. A soil-metal analysis reported metal-linked variation in COG profiles [src: soil_metal_functional_genomics]. This matters because the answer decides whether these subsystem signals are real exceptions or come from structured confounding. The sides also use different feature spaces and response variables, so they may not measure the same thing.

## Evidence Sides

**Side A: broad environmental null.** The ecotype reanalysis measured how strongly environment tracks gene content using a partial correlation (a correlation computed after removing the effect of a control variable). Environmental species had a median partial correlation of 0.051, compared with 0.084 for human-associated species. A Mann-Whitney U test (a rank-based test comparing two groups without assuming normality) gave U=1536, p=0.83, where p is the probability of a result at least this extreme if there were no true difference. [src: ecotype_env_reanalysis; prophage_ecology] So environmental species did not show a stronger environment–gene-content link. This side's result is a null.

**Side B: subsystem-specific environmental signals.** Prophage modules (annotation-defined groups of phage-derived genes) showed environment effects after controlling for genome size and host family. The F statistic, a ratio of between-group to within-group variance, was F=30.04 for environment and F=6.17 for phylogeny, and the within-quartile tests were significant. [src: ecotype_env_reanalysis; prophage_ecology]

The soil-metal analysis found 2,355 significant associations between COGs (Clusters of Orthologous Groups, families of orthologous genes) and metals. It also reported a conditional R² = 0.799 from db-RDA (distance-based redundancy analysis); R² is the share of variance a model explains, and a conditional R² is computed after a conditioning variable is removed, so it may describe residual rather than total variance. [src: soil_metal_functional_genomics] These tests cover metal-linked COG variation in soil only and remain vulnerable to co-contamination among metals, conditional-R² interpretation, non-independent tests, effect-size uncertainty, and spatial mismatch. [src: soil_metal_functional_genomics]

## Possible Reconciliations

- **Hypothesis 1: different feature spaces.** Whole-genome gene-content similarity may dilute environment effects concentrated in a few subsystems. Under this hypothesis, the broad null and the subsystem signals can both be correct.
- **Hypothesis 2: structured confounding.** The subsystem signals may reflect confounders rather than environmental selection. Candidates include genome size, metal co-contamination, a conditional R² that describes residual rather than total variance, or spatial mismatch between samples and genomes. This hypothesis would weaken the subsystem signals but would not by itself establish the broad null as general.
- **Hypothesis 3: different response variables.** Species-level partial correlations, module composition, and community COG profiles answer different questions. Under this hypothesis, the results are not directly comparable, and neither side refutes the other.

## Resolving Work

- Apply one dedicated functional annotation (prophage and metal-resistance modules) to the matched species set from the ecotype reanalysis. Recompute partial correlations per subsystem to test whether subsystem-level signals appear where whole-genome similarity is null.
- Harmonize environmental metadata across all three projects, then rerun the prophage analysis on matched species. This tests whether the environment F statistic persists on a common species and metadata base.
- Report the unconditional R² next to the conditional db-RDA R² = 0.799 for soil metals [src: soil_metal_functional_genomics]. This shows how much of that figure depends on what was conditioned out.
- Fit partial-correlation models across co-varying metals and report effect sizes. This tests whether the COG–metal associations survive co-contamination and non-independent testing.
- Restrict soil samples to those with spatially matched genomes. This tests whether metal–COG signals hold when spatial mismatch is removed.
