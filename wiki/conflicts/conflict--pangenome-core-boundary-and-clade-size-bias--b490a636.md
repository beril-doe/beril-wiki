<!-- tension-hash: b490a6368362e3e2 -->
# Is Essential-Core Enrichment Robust Across Clade-Size Strata, or Strongest in Larger Clades?

The integrated analysis and the central digest describe the same result differently. The result is that genes essential for fitness are enriched in the core genome. The integrated analysis says this enrichment was robust across clade-size and lifestyle strata [src: conservation_vs_fitness]. The central digest says the enrichment was strongest in organisms with larger clades [src: discoveries]. The disagreement bears on [[concepts/pangenome-core-boundary-and-clade-size-bias]]: if enrichment strength tracks clade size, part of the essential-core signal might reflect how the core boundary is drawn. This is a hypothesis, not a finding.

Some terms used here:
- **Core genome**: the gene clusters classified as core in a species pangenome. The supplied sources do not state the membership threshold.
- **Auxiliary genes**: the gene clusters not classified as core.
- **Clade size**: the number of genomes sampled for a species clade.
- **Stratum**: a subgroup of organisms defined by clade size or lifestyle.

## Evidence Sides

**Side A: the enrichment is robust across strata.** The integrated analysis reports that essential-core enrichment was robust across clade-size and lifestyle strata [src: conservation_vs_fitness]. The supplied text does not say whether "robust" refers to direction, magnitude or both, and it gives no stratum-level magnitudes.

**Side B: the enrichment is strongest in larger clades.** The central digest reports that the same enrichment was strongest in organisms with larger clades [src: discoveries]. This is a claim about relative strength, so it implies that the size of the effect varies with clade size. The supplied digest text gives no stratum-specific effect sizes or tests either.

## Possible Reconciliations

- **Hypothesis 1: both statements hold, at different levels.** The enrichment could persist in every stratum (direction robust) while its magnitude varies, being largest in larger clades. The sources supplied here do not report the stratum-specific effect sizes that would show this [src: conservation_vs_fitness; discoveries].
- **Hypothesis 2: clade size affects the core boundary itself.** Larger clades may define the core boundary more sharply, which would make it more discriminative and inflate the apparent enrichment. This follows the concept page's framing that sampling depth shapes core classification [src: conservation_vs_fitness]. It is untested here.
- **Hypothesis 3: the two summaries use different comparisons.** "Robust" and "strongest" may come from different analyses, thresholds or organism subsets. If so, the two statements would not be directly comparable. The supplied text does not specify either analysis well enough to check this.

## Resolving Work

- **Stratum-level effect sizes.** Use the Fitness Browser–pangenome link table to report, for each clade-size stratum, the essential-core odds ratio (the odds that an essential gene is core divided by the odds that a non-essential gene is core) with confidence intervals (ranges expressing the statistical uncertainty of each estimate). This would test whether direction is stable while magnitude varies.
- **Clade size as a continuous variable.** Fit a per-organism model of enrichment against genomes per clade, controlling for lifestyle. This would test whether "strongest in larger clades" survives that adjustment.
- **Subsampling large clades.** Subsample large clades down to small-clade genome counts and recompute core/auxiliary calls and enrichment. This would test whether the apparent clade-size effect comes from how the core boundary is drawn.
- **Provenance audit.** Trace the digest entry to the notebook and statistic it summarizes. This would establish whether both statements describe the same comparison.
