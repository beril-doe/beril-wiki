<!-- tension-hash: 1f2162673aeeba2f -->
# Environment partial-correlation medians that differ between the original ecotype analysis and its reanalysis

Both projects summarize how strongly environment tracks microbial genomic variation as a median partial correlation — a partial correlation being the association between two variables once the influence of other variables has been removed. The two reported medians are not the same number, and the reanalysis attributes the difference to methodological choices rather than to an error in either result [src: ecotype_env_reanalysis]. The disagreement matters because [[concepts/environment-embedding-geography]] leans on effect sizes to judge whether satellite-derived embeddings and environmental metadata resolve ecology at genome-relevant scale; if a median moves with pipeline choices, cross-project effect-size comparison in this concept is not currently licensed.

## Evidence Sides

**Original ecotype analysis — median 0.0025 for its environment measure.** The original analysis reports a median partial correlation of 0.0025 for the environment measure it used [src: ecotype_analysis].

**Reanalysis — median 0.081 across all 183 species.** The reanalysis reports a median partial correlation of 0.081 across all 183 species [src: ecotype_env_reanalysis]. Taken side by side, 0.0025 for the original environment measure versus 0.081 in the reanalysis **contradicts** any direct comparison of their absolute effect sizes [src: ecotype_analysis; ecotype_env_reanalysis].

**Reanalysis's own account of the gap.** The reanalysis does not claim the original median is wrong; it attributes the discrepancy to different genome sets, full-genome extraction, and downsampling procedures [src: ecotype_env_reanalysis].

## Possible Reconciliations

- *Hypothesis:* the two medians are computed over different genome sets, so the species denominators are not the same population and the medians are not estimates of a single quantity [src: ecotype_env_reanalysis].
- *Hypothesis:* full-genome extraction captures more environment-associated genomic variation than the original narrower environment measure, so the higher median reflects a broader signal rather than a stronger one [src: ecotype_env_reanalysis].
- *Hypothesis:* downsampling procedures differ in how many observations enter each per-species correlation, shifting the distribution whose median is reported [src: ecotype_env_reanalysis].
- *Hypothesis (null-preserving):* both medians are correct for their own pipelines, and the tension is about comparability, not about either result being refuted — neither number should be averaged into the other.

## Resolving Work

- Re-run the reanalysis pipeline restricted to the exact genome set of the original analysis, and report the median partial correlation on that fixed set: does the gap survive when the genome set is held constant?
- Hold the genome set fixed and toggle only full-genome extraction versus the original environment measure, reporting per-species partial correlations: how much of the shift is attributable to extraction scope alone?
- Vary the downsampling procedure across a grid of retained-sample sizes on one pipeline and plot the resulting median: is the median sensitive to downsampling depth, and in which direction?
- Publish per-species paired partial correlations for species present in both analyses, and test their rank agreement: do the two pipelines order species the same way even when absolute magnitudes diverge?
- Specify, for each pipeline, the denominator of species entering the median, so that any future cross-project effect-size claim states which population it describes.
