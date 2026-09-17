<!-- tension-hash: cd13abd8a4e20f5d -->
# Does the Pangenome-Openness Null Speak to the Sampling-Depth Explanation, or Only Past It?

This page records a disagreement over what a null result is allowed to close. One line of work reports no relationship between pangenome openness — a summary of whether a species keeps acquiring new genes as more genomes are added — and the relative strength of environment versus phylogeny effects on gene content. A second line, feeding [[concepts/sampling-depth-and-downsampling-effects]], holds that differences in the *scale* of correlation estimates across projects may be methodological in origin (how genomes are sampled, processed and covered) rather than biological. The dispute matters because reading the openness null as a general statement about eco-phylogenetic dynamics would retire a question that the sampling-depth line argues has not yet been asked in a controlled way.

## Evidence Sides

**The openness null is orthogonal, not contradictory.** The pangenome-openness null correlations do not contradict the sampling-depth result: they test whether an openness summary predicts effect sizes rather than whether changing genome sampling changes correlation estimates. [src: pangenome_openness] On this reading the two results are measurements of different quantities and cannot adjudicate each other.

**The openness null is itself under-determined.** The null results leave unresolved whether openness fails because pangenome structure is genuinely decoupled from eco-phylogenetic dynamics, because the metric is too coarse, or because the matched species sample and upstream effect estimates limit power. [src: pangenome_openness] A null that admits three incompatible readings — real decoupling, measurement coarseness, or insufficient power — cannot be treated as settled in any direction.

**The correlation-scale difference is unattributed.** Resolving whether the correlation-scale difference is driven mainly by downsampling, genome-set composition, extraction behavior, embedding coverage, condition coverage, missingness, or another methodological factor requires a controlled reanalysis. [src: ecotype_env_reanalysis, ecotype_analysis, core_gene_tradeoffs] These candidate factors are named on this side as a list of possibilities, without definitions and without any ranking among them, so which one carries the scale difference stays open until that controlled reanalysis is run. [src: ecotype_env_reanalysis, ecotype_analysis, core_gene_tradeoffs]

## Possible Reconciliations

- **Orthogonality hypothesis:** the two results answer different questions and both stand as stated, with the openness null constraining only openness-as-predictor claims.
- **Coarse-metric hypothesis:** openness, as a single per-species summary, discards the structure that would couple gene-content variation to environment; a finer descriptor might behave differently.
- **Shared-power hypothesis:** the matched species sample and upstream effect estimates limit power for both analyses, so the openness null and the correlation-scale spread are two symptoms of one sampling limitation.
- **Composite-methodology hypothesis:** several of the listed factors contribute jointly, so no single-factor explanation will reproduce the observed scale difference.

## Resolving Work

- Species-level genome sets from the ecotype analyses, re-run through the same correlation estimator across a downsampling ladder with composition held fixed: does estimate scale move with sampling depth alone?
- The matched species sample, re-scored with alternative openness descriptors (accumulation-curve based and accessory-fraction based) against the same effect estimates: does any finer metric predict effect sizes where the coarse summary did not?
- Simulated gene-content data with an injected openness–effect coupling of known magnitude, analysed at the matched sample size: what coupling would have been detectable?
- Per-species records of embedding coverage, condition coverage and missingness, regressed against correlation estimates: which methodological factor carries the scale difference? [src: ecotype_env_reanalysis, ecotype_analysis, core_gene_tradeoffs]
- A single controlled reanalysis pipeline shared across the three projects, so that extraction behavior and genome-set composition stop varying between them.
