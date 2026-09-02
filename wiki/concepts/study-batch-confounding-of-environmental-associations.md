---
type: "Concept"
description: "How study and batch structure can reverse environmental generalization"
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Study and batch confounding can reverse environmental generalization

Environmental associations estimated across heterogeneous studies can reflect study or batch structure rather than portable environmental effects. The [[summaries/euk_in_prok_correlates__REPORT]] provides a direct example: eukaryotic read fractions appeared environmentally predictable under random cross-validation but failed to generalize when entire studies were held out. [src: euk_in_prok_correlates]

## Core claim

When environmental categories are strongly nested within studies, an environmental predictor can act as a proxy for study-specific protocols, populations, sequencing workflows, or unmeasured sample-processing factors. [src: euk_in_prok_correlates] In this setting, random train/test splits allow closely related samples from the same study to appear in both partitions, whereas study-held-out validation tests whether the environmental association transfers to a new batch or study. [src: euk_in_prok_correlates] This makes [[concepts/study-batch-confounding-of-environmental-associations]] a direct extension of [[concepts/sampling-composition-confounding-of-environmental-signal]] and [[concepts/callability-limited-comparative-inference]].

## Evidence from eukaryotic read fractions

The analysis quantified GOTTCHA2 relative eukaryotic abundance across 2,759 NMDC ReadbasedAnalysis runs from 9 studies. [src: euk_in_prok_correlates] Each biome was approximately 80–100% nested within a single study, preventing a clean separation of environment from study or batch in cross-study univariate comparisons. [src: euk_in_prok_correlates]

A gradient-boosted model using study_id alone achieved R²=0.24 under random cross-validation, while an environment model achieved R²=0.35 under the same validation scheme. [src: euk_in_prok_correlates] Under GroupKFold, meaning cross-validation in which complete studies are held out as groups, the environment model achieved R²=−0.30 out of study, and the model combining environment with sequencing achieved R²=−0.39. [src: euk_in_prok_correlates] The out-of-study environment model therefore performed worse than predicting the mean, while its out-of-study detection AUC was 0.56, approximately chance. [src: euk_in_prok_correlates]

This **contradicts** the interpretation that the stronger random-validation environment score demonstrates broadly transferable environmental prediction. [src: euk_in_prok_correlates] Instead, the contrast between random-validation and study-held-out performance supports the hypothesis that cross-study environmental signal was substantially batch-driven. [src: euk_in_prok_correlates]

Adding sequencing platform and depth did not improve the study-held-out prediction. [src: euk_in_prok_correlates] Measured sequencing depth was negatively associated with eukaryotic fraction across the collection, with Spearman ρ=−0.29, p=5.2×10⁻⁷, and n=292 runs with measured depth, but this association was not batch-controlled. [src: euk_in_prok_correlates] The depth result is therefore suggestive rather than evidence of a controlled sequencing-depth effect because measured-depth runs came from a handful of non-soil studies, while the dominant NEON soil study recorded no depth. [src: euk_in_prok_correlates]

## Why within-study analysis changes the conclusion

A batch-controlled analysis of 1,186 runs from the dominant NEON soil metagenome study used one sampling program with a constant protocol and batch. [src: euk_in_prok_correlates] Within that study, local vegetation was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹ across 11 `env_local_scale` levels. [src: euk_in_prok_correlates] Geography was also associated with eukaryotic fraction across 47 sites at H=310.4 and p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates]

A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06, contrasting with the cross-study out-of-study R²=−0.30. [src: euk_in_prok_correlates] This **supports** a genuine fine-scale environmental signal when batch is held approximately constant, while the result remains potentially confounded by sub-batches such as sampling campaigns because the design was not randomized. [src: euk_in_prok_correlates] The finding therefore refines [[concepts/environment-embedding-geography]]: environmental metadata can be predictive, but its apparent portability depends on the validation and sampling structure. [src: euk_in_prok_correlates]

## Implications for study design and interpretation

Random cross-validation should not be treated as evidence of environmental generalization when samples from the same study or batch can occur in both training and test partitions. [src: euk_in_prok_correlates] Study-held-out GroupKFold or within-study contrasts are more appropriate tests of whether an environmental association survives batch changes. [src: euk_in_prok_correlates]

The analysis also used the `workflow_run_id` level rather than the biosample level because 1,067 of 2,759 runs were pooled from multiple biosamples, avoiding pseudo-replication from biosample-level joins. [src: euk_in_prok_correlates] Metadata linkage connected workflow runs to biosamples and studies through NMDC tables and linked 99%+ of classified runs. [src: euk_in_prok_correlates] For pooled runs, assigning environment and collection metadata from a representative biosample selected by `MIN(biosample_id)` could introduce predictor label noise when pooled biosamples differ, which the report characterizes as a conservative bias that can weaken associations rather than manufacture them. [src: euk_in_prok_correlates]

Interpretation is further limited when study metadata omit influential processing variables. [src: euk_in_prok_correlates] NMDC did not populate DNA-extraction kit, size fractionation or filtration, host-depletion method, or library-preparation fields, and `has_filtration` was all false in the processing metadata. [src: euk_in_prok_correlates] These unmeasured factors can remain residual explanations for apparent environmental differences even after measured sequencing variables are included. [src: euk_in_prok_correlates]

## Tensions

The cross-study analysis shows strong environmental differences, including environment-model R²=0.35 under random cross-validation, while study-held-out validation gives R²=−0.30 and detection AUC=0.56. [src: euk_in_prok_correlates] The within-NEON analysis nevertheless gives positive predictive performance, with R²=+0.17 ± 0.06. [src: euk_in_prok_correlates] These results are not mutually exclusive: they indicate that an environmental signal may be real within a controlled study while failing to generalize across studies because study and environment are confounded. [src: euk_in_prok_correlates]

The within-study result also has a residual tension: constant protocol and batch reduce confounding, but local environment and geography may still track sub-batches such as sampling campaigns. [src: euk_in_prok_correlates] The evidence therefore supports batch-aware environmental prediction without establishing that the observed within-study associations are causal or portable to aquatic or host-associated collections. [src: euk_in_prok_correlates]

## Open Directions

- Use additional NMDC studies with overlapping biome categories, apply study-held-out GroupKFold, and test whether environmental prediction remains above the R²=−0.30 observed in the original cross-study analysis. [src: euk_in_prok_correlates]
- Obtain extraction, filtration, size-fractionation, host-depletion, and library-preparation metadata, then fit hierarchical or batch-adjusted models to test whether these measured workflow factors explain the residual study effect. [src: euk_in_prok_correlates]
- Reanalyze the 1,186-run NEON soil subset with sampling campaign or field-collection batch as held-out groups, testing whether the within-study R²=+0.17 ± 0.06 survives sub-batch validation. [src: euk_in_prok_correlates]
- Separate pooled and unpooled workflow runs and compare representative-biosample metadata with biosample-resolved metadata, testing how the 1,067 pooled runs affect environmental effect estimates. [src: euk_in_prok_correlates]
- Repeat eukaryotic-fraction estimation with classifiers whose reference databases include comparable eukaryotic and plastid coverage, testing whether the observed environment-by-study pattern is robust to the GOTTCHA2-specific measurement scale. [src: euk_in_prok_correlates]
