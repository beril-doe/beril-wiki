<!-- tension-hash: c66707fcf54d98d8 -->
# Conflict: A weak overall environmental signal versus a median partial correlation of 0.081 across ecotype pipelines

Two projects in this corpus characterise the same question — how strongly environment, as opposed to other structure, tracks species-level variation — and report magnitudes that do not read the same way. The original ecotype analysis reports a weak environmental signal overall, whereas the reanalysis reports a median partial correlation of 0.081 under a different pipeline. [src: ecotype_analysis, ecotype_env_reanalysis] A *partial correlation* here is the association between environment and the response after statistically removing the other modelled predictors; a *median* is the middle value across the species analysed, not a per-species effect. The disagreement matters because this pair sits under [[concepts/selection-on-outcome-leakage]], where the tempting explanation for any inflated-looking association is that grouping and testing used the same features. Recording the disagreement as a measurement-and-sampling tension keeps that leakage explanation from being applied by default to a discrepancy that has not been shown to require it.

## Evidence Sides

**The original ecotype analysis: a weak environmental signal overall.** The original ecotype analysis reports a weak environmental signal overall. [src: ecotype_analysis, ecotype_env_reanalysis]

**The reanalysis: a median partial correlation of 0.081.** Under a different pipeline, the reanalysis reports a median partial correlation of 0.081. [src: ecotype_analysis, ecotype_env_reanalysis] Neither side is offered as evidence that selection-on-outcome leakage produced the other's result; the cross-pipeline magnitude comparison is treated as a tension in measurement and sampling. [src: ecotype_analysis, ecotype_env_reanalysis]

## Possible Reconciliations

- *Hypothesis (species sampling):* the two pipelines may summarise different sets of species, so the medians describe different denominators rather than different biology.
- *Hypothesis (covariate specification):* if the two pipelines partial out different covariates, the residual environmental association each reports is defined differently, and the magnitudes are not directly comparable.
- *Hypothesis (summary statistic):* a qualitative "weak overall" verdict and a median partial correlation may be compatible descriptions of one distribution, with disagreement arising only at the point of verbal summary.

These are hypotheses; none is established by the evidence recorded here.

## Resolving Work

- Re-run both pipelines on the identical species list and report the median partial correlation from each, asking whether the magnitude gap survives a common denominator.
- Publish the covariate set and partialling step for each pipeline side by side, asking which term's inclusion or exclusion moves the median.
- Report the full distribution of per-species partial correlations from both pipelines, not the median alone, asking whether the distributions differ in shape or only in central tendency.
- Apply each pipeline's summarisation rule to the other pipeline's per-species estimates, asking how much of the disagreement is summary convention rather than estimation.
- Specify in advance any grouping used before testing in each pipeline, asking whether selection-on-outcome leakage is even available as an explanation for either result.
