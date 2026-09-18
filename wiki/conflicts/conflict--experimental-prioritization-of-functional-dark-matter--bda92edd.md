<!-- tension-hash: bda92edd5ccca676 -->
# Are stress conditions where dark-gene phenotypes concentrate, or where truly dark genes are depleted relative to annotation-lag genes?

Two projects in this corpus describe the condition profile of strong fitness phenotypes among unannotated ("dark") bacterial genes in ways that do not line up. One reports stress as the condition class where strong dark-gene phenotypes concentrate most; the other reports strong-phenotype truly dark genes as *depleted* in stress relative to annotation-lag genes. The disagreement matters for experimental prioritization: it determines whether a laboratory screening a dark-gene candidate list should weight stress conditions heavily, and whether that weighting should be the same for the residual genes that resist modern reannotation as for the dark set as a whole. Because the two analyses use different gene sets and different comparisons — one a within-set concentration, the other a between-class contrast — collapsing them into a single recommendation would misdirect assay design. The tension is recorded on [[concepts/experimental-prioritization-of-functional-dark-matter]].

## Evidence Sides

**Stress is the largest concentration of strong dark-gene phenotypes.** The overall dark-gene analysis — covering unknown genes generally, without partitioning by whether modern reannotation resolves them — reports stress conditions as producing the largest concentration of strong dark-gene phenotypes. [src: functional_dark_matter] This is a statement about where strong phenotypes fall within the dark set as a whole, not a contrast against another gene class.

**Stress is depleted among truly dark genes relative to annotation-lag genes.** The truly dark analysis splits unknown genes into annotation-lag genes (hypothetical in the original annotation but resolvable by modern reannotation) and truly dark genes (residual genes that resist reannotation). Among strong-phenotype genes it reports stress proportions of 28.7% versus 43.2% for annotation-lag genes, with OR = 0.53 — an odds ratio below 1, meaning reduced odds of a stress condition — and p < 0.001. [src: truly_dark_genes] A separate comparison in the same project reports stress at 43.3% versus 54.7%. [src: truly_dark_genes] Both comparisons point the same direction: stress is less characteristic of truly dark genes than of annotation-lag genes.

## Possible Reconciliations

- *Hypothesis: the two claims have different denominators.* One measures the share of strong dark-gene phenotypes falling in stress within a single pooled dark set; the other measures a between-class contrast of two disjoint subsets. Stress could be the modal condition overall while still being relatively rarer in the residual subset.
- *Hypothesis: annotation-lag genes drive the overall signal.* If annotation-lag genes are numerically dominant in the pooled dark set and carry the higher stress proportion, the pooled result would inherit their profile without the residual subset sharing it.
- *Hypothesis: the two truly-dark comparisons themselves use different strong-phenotype filters or condition groupings*, so the 28.7%/43.2% and 43.3%/54.7% figures index different slices and neither supersedes the other.

## Resolving Work

- Re-run the overall dark-gene condition tabulation with annotation-lag and truly dark genes reported separately under one shared strong-phenotype threshold: does the pooled stress ranking survive stratification?
- Publish the exact denominators (gene counts per class, condition-group definitions) behind the 28.7%/43.2% and 43.3%/54.7% comparisons: are these two thresholds on one dataset or two datasets?
- Recompute the overall analysis's condition ranking as a between-class odds ratio rather than a within-set concentration, so both sides use the same statistic and directions become directly comparable.
- Test whether annotation-lag genes numerically dominate the pooled dark set; if so, quantify how much of the pooled stress signal they contribute.
- Run matched stress and nutrient/iron/mixed-community assays on a held-out truly dark candidate set: does assay success follow the depletion direction?
