<!-- tension-hash: 2b613a7bddf3aa31 -->
# Environment–Gene-Content Correlation Magnitude: Ecotype Reanalysis Versus the Original Ecotype Analysis

Two related projects agree on the direction of a null result but disagree on the absolute size of the effect they measure. That effect is a partial correlation, meaning a correlation measured after removing the influence of another variable. The reanalysis found no stronger correlations for environmental species (p=0.83, where the p-value is the probability of a result at least this extreme if no true difference exists). It also reported a 27x higher overall median partial correlation than the original analysis. The comparator it used for the original does not match the median the original analysis itself reports [src: ecotype_env_reanalysis, ecotype_analysis]. This matters because, without a demonstrated cause, the absolute correlation difference must not be read as a biological contradiction [src: ecotype_env_reanalysis, ecotype_analysis]. It also bears on a broader question raised in [[concepts/classifier-database-compatibility-in-taxonomic-quantification]]: whether quantities produced by different pipelines can be compared directly.

## Evidence Sides

**Side 1: Ecotype reanalysis (genome-level environmental comparison)**
- Its genome-level environmental comparison found no stronger correlations for environmental species (p=0.83). This is a null result, not evidence of an opposite effect [src: ecotype_env_reanalysis, ecotype_analysis].
- It reported a 27x higher overall median partial correlation than the original analysis [src: ecotype_env_reanalysis, ecotype_analysis].
- It used 0.003 as its comparator value for the original analysis [src: ecotype_env_reanalysis, ecotype_analysis].
- It lists full-genome extraction without downsampling (reducing data to a smaller subsample before analysis) as one of several methodological differences. It does not demonstrate that this difference is the cause [src: ecotype_env_reanalysis, ecotype_analysis].

**Side 2: Original ecotype analysis**
- It reports a median of 0.0025, which differs from the 0.003 comparator the reanalysis used [src: ecotype_env_reanalysis, ecotype_analysis].
- Its magnitude has not been reconciled with the reanalysis. The discrepancy remains open [src: ecotype_env_reanalysis, ecotype_analysis].

## Possible Reconciliations

- **Hypothesis A: pipeline-driven magnitude.** The magnitude gap may come from methodological differences, such as full-genome extraction without downsampling, rather than from biology. The reanalysis lists this difference but does not demonstrate it as the cause [src: ecotype_env_reanalysis, ecotype_analysis].
- **Hypothesis B: comparator mismatch.** Part of the stated fold difference may depend on which original median is used as the baseline, 0.003 or 0.0025 [src: ecotype_env_reanalysis, ecotype_analysis]. This page does not compute an alternative fold difference.

## Resolving Work

- **Downsampling ablation.** Rerun the reanalysis pipeline on the same genomes with and without the original downsampling step, and compare median partial correlations. Does full-genome extraction alone shift the magnitude?
- **Baseline audit.** Trace the 0.003 comparator in the reanalysis back to the original analysis outputs. Was it taken from a different table, species subset or rounding than the reported 0.0025 median [src: ecotype_env_reanalysis, ecotype_analysis]?
- **Matched-species comparison.** Restrict both analyses to an identical species list and identical environment classifications, then recompute medians. Does the magnitude gap persist under matched inputs?
- **One-factor-at-a-time methods comparison.** Switch each listed methodological difference individually, holding the others fixed. Which single change, if any, accounts for the reported 27x difference [src: ecotype_env_reanalysis, ecotype_analysis]?
- **Null-result robustness.** Repeat the reanalysis's environmental-species comparison, with its original comparison group unchanged, under each pipeline variant. Does the null finding (p=0.83 in the reanalysis) hold regardless of magnitude changes [src: ecotype_env_reanalysis, ecotype_analysis]?
