---
type: "Concept"
description: "Whether environment-metadata associations with a measured sample property survive when study/batch is held out; covers univariate versus out-of-study models and the recommended controls, not wet-lab mechanisms."
sources: ["summaries/euk_in_prok_correlates__REPORT.md", "summaries/nmdc_community_metabolic_ecology__REPORT.md"]
---
# Study and batch confounding of cross-collection metadata correlates

Environment associations with a measured sample property can be largely a study or batch effect. In the National Microbiome Data Collaborative (NMDC) data, the eukaryotic fraction of metagenomic reads shows a strong univariate association with sample matrix. That association does not survive when whole studies are held out. [src: euk_in_prok_correlates] The main evidence is one project, euk_in_prok_correlates, on one collection. A second project, nmdc_community_metabolic_ecology, adds a related study-dominance caveat. See [[summaries/euk_in_prok_correlates__REPORT]] and [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Univariate signal

The eukaryotic fraction differs across sample matrices (Kruskal–Wallis H=77.8, p=1.3×10⁻¹⁷). [src: euk_in_prok_correlates] All pairwise matrix contrasts are significant after BH-FDR (Benjamini-Hochberg false discovery rate) correction. [src: euk_in_prok_correlates] The report calls this association strong but confounded. [src: euk_in_prok_correlates]

Ecosystem type does not add independent support. After the Unknown or missing-metadata bucket is excluded, ecosystem_type reduces to Soil, Freshwater and Roots, so its test is identical to the matrix test. [src: euk_in_prok_correlates] An earlier version kept the Unknown bucket, which has the highest median eukaryotic fraction. It reported an inflated p≈10⁻⁵⁰, which the report removed as a missingness artifact. [src: euk_in_prok_correlates]

## Why the signal is confounded

Each NMDC biome is ~80–100% nested within a single study. The strong univariate environment signal therefore cannot be separated from study or batch. [src: euk_in_prok_correlates] The inference uses non-parametric tests (Kruskal–Wallis, Mann–Whitney with BH-FDR) or cross-validated gradient boosting with GroupKFold by study, because of this batch structure. [src: euk_in_prok_correlates]

## Out-of-study prediction

Prediction of NMDC euk_logit shows the confounding directly. Values are R² unless stated.

| Model | R² |
|---|---|
| study_id only, random CV (cross-validation), the batch ceiling | 0.24 [src: euk_in_prok_correlates] |
| environment, random CV | 0.35 [src: euk_in_prok_correlates] |
| environment, GroupKFold (out-of-study) | −0.30 [src: euk_in_prok_correlates] |
| environment + sequencing metadata, GroupKFold | −0.39 [src: euk_in_prok_correlates] |

Environment explains no more variance than study_id alone. With whole studies held out, it performs worse than predicting the mean. [src: euk_in_prok_correlates] Out-of-study detection AUC (area under curve) is 0.56, about chance. [src: euk_in_prok_correlates] Adding platform and depth metadata does not help. [src: euk_in_prok_correlates] The environment model does not generalize across studies. [src: euk_in_prok_correlates]

## Consequences and recommended controls

A naive cross-collection regression of eukaryotic fraction on environmental metadata would report a strong but largely spurious, batch-driven association. [src: euk_in_prok_correlates] The report describes this as a cautionary headline: cross-study metadata-correlate analysis is confounded and over-claims. [src: euk_in_prok_correlates] It says this qualifies the cross-collection biome correlate of Eisenhofer et al., because within NMDC a biome correlate is inseparable from study or batch. [src: euk_in_prok_correlates] A metadata-resolved correlate analysis is feasible only under batch control. [src: euk_in_prok_correlates]

The report recommends GroupKFold by study or within-study contrasts. [src: euk_in_prok_correlates] A within-study approach is developed in [[concepts/within-study-environmental-drivers-of-eukaryotic-dna-in-soil-metagenomes]]. It also recommends analysing at the workflow_run_id level. NMDC pools biosamples in 1,067 of 2,759 ReadbasedAnalysis runs, so biosample-level joins inflate n through pseudoreplication. [src: euk_in_prok_correlates] Pooled runs inherit metadata from a single representative biosample, MIN(biosample_id). [src: euk_in_prok_correlates] The report states that differing local metadata among pooled biosamples adds label noise. It calls this a conservative bias that can only weaken associations, not manufacture them. [src: euk_in_prok_correlates]

## Limits of the evidence

- NMDC read-based taxonomy spans only ~9 studies, and one soil study contributes ≈43% of runs. The cross-study generalization test is under-powered. The within-study result is shown for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]
- Even within one study, env_local_scale and geography may track sampling-campaign sub-batches. Within-study control is therefore the best available control, not a randomized one. [src: euk_in_prok_correlates]
- A separate NMDC project shows the same dominance. In its H1 dataset, 95% of samples (125/131) come from nmdc:sty-11-r2h77870, and the other 6 come from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology] There, cross-study LC-MS (liquid chromatography-mass spectrometry) protocol heterogeneity is largely absent as a confounder for leucine and arginine, although the 175 metabolomics samples span multiple studies. [src: nmdc_community_metabolic_ecology] See [[concepts/confounding-and-robustness-in-environmental-metabolomics-genomics-association]].

## Proposed remedies

The euk_in_prok_correlates report proposes importing a many-study raw-read resource, or computing eukaryotic fraction across a broader collection. This would break the batch confound and allow a properly powered cross-study correlate analysis. [src: euk_in_prok_correlates] The nmdc_community_metabolic_ecology report suggests that future analyses with broader multi-study coverage could model study-level random effects to improve power. [src: nmdc_community_metabolic_ecology]

## Open Directions

- Import a many-study raw-read resource, or compute eukaryotic fraction across a broader collection. This would give a properly powered cross-study analysis and close the gap of about 9 studies.
- Fit study-level random effects once multi-study coverage exists. This would test whether power improves over GroupKFold alone.
- Repeat the GroupKFold-by-study comparison for aquatic and host-associated studies. This would test whether the soil-only within-study result extends.
- Rerun the models at workflow_run_id level, excluding pooled runs. This would check how pseudoreplication and label noise affect the estimates.
