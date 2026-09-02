<!-- tension-hash: 5fdeecf0f11662b2 -->
# Leakage or Real Structure? A Tension Between Instability and Biological Signal

The disagreement is whether unstable or cross-pipeline results should be interpreted primarily as evidence of outcome leakage or as evidence of genuine functional and environmental structure measured differently across analyses. [[concepts/selection-on-outcome-leakage]] cautions that the available evidence does not establish universal leakage criteria, while the ecotype analyses report differentiated gene functions and environmental associations that may reflect real biology. The distinction matters because methodological instability can be mistaken for leakage, while genuine structure can also be amplified or obscured by annotation, sampling, clustering, and validation choices.

## Evidence Sides

**Side 1 — Instability does not establish leakage**

The evidence does not establish a universal Jaccard cutoff for detecting leakage. [src: pitfalls] The values 0.5 and 0.3 were explicitly project-specific decision thresholds for the cited sensitivity procedure, so applying them unchanged to another dataset or clustering method would be an unsupported extrapolation. [src: pitfalls] The observed instability also does not by itself identify whether clustering, differential-abundance modeling, subgroup sample size, or study structure contributed most to the changes. [src: pitfalls]

The ecotype reanalysis further shows that absolute partial-correlation values can differ substantially when genome inclusion and downsampling change: its median across 183 species was 0.081 versus 0.003 in the original analysis, described as a 27x difference. [src: ecotype_env_reanalysis] This supports retaining the existing warning against interpreting instability or magnitude across incompatible methodologies as evidence of leakage alone, while the within-method environmental-versus-human-associated null comparison remains informative. [src: ecotype_env_reanalysis]

**Side 2 — The analyses retain evidence of biological structure**

The ecotype functional-differentiation result refines this tension rather than resolving it: all 12 analyzed species had at least one differentiated COG category, but approximately 38% of gene clusters had COG annotations, and the report notes that effect significance may partly reflect large sample sizes. [src: ecotype_functional_differentiation] Thus, widespread COG differences are compatible with real functional structure, annotation and sampling effects, or reuse of related gene-content information; they do not alone quantify leakage. [src: ecotype_functional_differentiation]

The original ecotype analysis reports a weak environmental signal overall, whereas the reanalysis reports a median partial correlation of 0.081 under a different pipeline. [src: ecotype_analysis, ecotype_env_reanalysis] This supports treating cross-pipeline magnitude comparisons as a tension in measurement and sampling rather than as evidence that leakage caused either result. [src: ecotype_analysis, ecotype_env_reanalysis]

## Possible Reconciliations

- **Measurement hypothesis:** The 0.081 versus 0.003 medians may reflect genome inclusion, downsampling, or other pipeline differences rather than a change in the underlying biological signal. [src: ecotype_env_reanalysis]
- **Scope hypothesis:** The 0.5 and 0.3 thresholds may be valid for the cited sensitivity procedure but not transferable across datasets or clustering methods. [src: pitfalls]
- **Definitional hypothesis:** “Instability,” “functional differentiation,” and “leakage” may describe different properties; differentiated COG categories do not alone quantify leakage. [src: ecotype_functional_differentiation]
- **Sampling hypothesis:** Large sample sizes, subgroup size, and study structure may influence apparent significance or instability without determining whether the biological structure is genuine. [src: ecotype_functional_differentiation, pitfalls]

## Resolving Work

- Re-run the analyses across feature partitions and clustering methods while preserving the underlying samples and labels; test whether instability tracks partitioning or clustering.
- Repeat validation with controlled subgroup sample sizes and study-structure splits; determine whether the observed changes persist after balancing sampling conditions.
- Compare leakage diagnostics using the project-specific 0.5 and 0.3 thresholds only within their original procedure, then evaluate calibration on independent datasets.
- Reanalyze COG differentiation after restricting to annotated clusters and applying sample-size-aware effect estimates; test whether the 12-species pattern remains.
- Hold genome inclusion, downsampling, and environmental covariates constant across pipelines; determine whether the 0.081 versus 0.003 difference is methodological or biological.
