---
type: "Concept"
description: "Missing protocol fields leave environmental metagenomic associations confounded."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Missing laboratory-protocol metadata leaves residual confounding in environmental metagenomics

Environmental metagenomic associations can remain confounded when laboratory variables such as extraction, filtration, host depletion, and library preparation are absent from the metadata needed to separate ecological effects from processing effects. [src: euk_in_prok_correlates]

The [[summaries/euk_in_prok_correlates__REPORT]] provides a direct example: eukaryotic read fractions were quantified across 2,759 NMDC ReadbasedAnalysis runs from 9 studies, but the database did not populate DNA-extraction kit, size fractionation or filtration, host-depletion method, or library-preparation fields. [src: euk_in_prok_correlates]

## Evidence from eukaryotic-read fractions

GOTTCHA2 detected eukaryotic reads in 77% of the 2,759 runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20% eukaryotic reads. [src: euk_in_prok_correlates] These fractions were classifier- and database-dependent because Kraken2 and Centrifuge produced approximately 0 domain-level Eukaryota signal in this deployment, whereas GOTTCHA2 was plastid- and eukaryote-aware. [src: euk_in_prok_correlates] The resulting GOTTCHA2 values should therefore be interpreted as relative or ordinal contamination measures rather than calibrated absolute fractions. [src: euk_in_prok_correlates]

The apparent environmental structure was substantial: aquatic freshwater samples had 99.5% eukaryotic detection and a plastid share of 1.00, terrestrial soil had 55.7% detection and a plastid share of 0.43, and plant-root samples had 100% detection and a plastid share of 0.03. [src: euk_in_prok_correlates] Matrix differences were significant in a Kruskal–Wallis test with H=77.8 and p=1.3×10⁻¹⁷, and all pairwise matrix contrasts were significant after BH-FDR, where FDR means false discovery rate. [src: euk_in_prok_correlates]

These results establish strong observed environmental differences, but they do not identify which differences arise from sample ecology and which arise from unrecorded laboratory processing. [src: euk_in_prok_correlates]

## Study and batch confounding

Each biome was approximately 80–100% nested within a single study, making environmental effects difficult to separate from study or batch effects. [src: euk_in_prok_correlates] A gradient-boosted model using study_id alone achieved R²=0.24 under random cross-validation, while an environment-only model achieved R²=0.35 under random cross-validation but R²=−0.30 under GroupKFold out-of-study validation; GroupKFold holds complete studies out as validation groups. [src: euk_in_prok_correlates] Adding environment and sequencing variables produced R²=−0.39 under GroupKFold, and the out-of-study detection AUC was 0.56, approximately chance. [src: euk_in_prok_correlates]

The failure of cross-study generalization supports [[concepts/study-batch-confounding-of-environmental-associations]]: a strong pooled environmental association can primarily encode study composition and processing history rather than a portable environmental effect. [src: euk_in_prok_correlates] Missing protocol fields prevent direct adjustment for the wet-lab variables that may differ systematically among studies. [src: euk_in_prok_correlates]

The measured sequencing-depth association illustrates the same limitation: sequencing depth had Spearman ρ=−0.29, p=5.2×10⁻⁷, and n=292 runs with measured depth, but measured-depth runs came from a handful of non-soil studies while the dominant NEON soil study recorded no depth. [src: euk_in_prok_correlates] This association is therefore suggestive rather than a controlled sequencing-depth effect. [src: euk_in_prok_correlates]

## Within-study signal does not eliminate protocol uncertainty

Within the dominant NEON soil metagenome study, 1,186 runs came from one sampling program with a constant protocol and batch. [src: euk_in_prok_correlates] Local vegetation was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹, and geography differed across 47 sites with H=310.4 and p=2.4×10⁻⁴⁶. [src: euk_in_prok_correlates] A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06, compared with cross-study out-of-study R²=−0.30. [src: euk_in_prok_correlates]

This within-study result supports [[concepts/environment-embedding-geography]] by showing that environmental metadata can retain predictive signal when study-level protocol variation is approximately held constant. [src: euk_in_prok_correlates] It does not establish that the result is free of protocol confounding because local environment and geography may still track sub-batches such as sampling campaigns. [src: euk_in_prok_correlates]

## Metadata and join limitations

The NMDC analysis linked workflow runs to biosamples and studies through workflow_run_id and biosample-to-workflow associations, linking 99%+ of classified runs. [src: euk_in_prok_correlates] It analyzed data at the workflow_run_id level because 1,067 of 2,759 runs were pooled from multiple biosamples, avoiding pseudo-replication from biosample-level joins. [src: euk_in_prok_correlates]

However, each pooled run inherited environmental and collection metadata from a representative biosample selected by MIN(biosample_id), so heterogeneous pooled biosamples could introduce predictor label noise. [src: euk_in_prok_correlates] This label noise was characterized as a conservative bias that can weaken associations rather than manufacture them. [src: euk_in_prok_correlates] The limitation connects this concept to [[concepts/pooled-run-pseudoreplication-and-metadata-label-noise]] and [[concepts/environmental-metadata-harmonization-bias]]. [src: euk_in_prok_correlates]

## Implication for environmental inference

Environmental metagenomic studies should treat absent extraction, filtration, size-fractionation, host-depletion, and library-preparation metadata as unresolved confounders rather than as evidence that protocol effects are absent. [src: euk_in_prok_correlates] Cross-study models should use study- or batch-controlled validation, such as GroupKFold by study or within-study contrasts, when protocol metadata cannot be recovered. [src: euk_in_prok_correlates] Classifier and reference-database compatibility must also be audited before comparing contamination or taxonomic fractions across studies. [src: euk_in_prok_correlates]

## Tensions

The dataset contains both a strong cross-collection environmental association and a failure of out-of-study environmental prediction, while the batch-controlled NEON analysis retains a positive within-study signal. [src: euk_in_prok_correlates] These findings are not mutually exclusive: they indicate that fine-scale environmental structure may be real while the pooled cross-study association is not portable because study, batch, and unmeasured protocol variables are entangled. [src: euk_in_prok_correlates]

## Open Directions

- Recover DNA-extraction kit, filtration, size-fractionation, host-depletion, and library-preparation records from laboratory information systems, then fit hierarchical models or batch-stratified models to test which protocol variables explain residual eukaryotic-fraction variation. [src: euk_in_prok_correlates]
- Reanalyze the 2,759 runs with classifier-compatible reference databases and a common taxonomic estimator, then test whether environmental associations persist after database effects are controlled. [src: euk_in_prok_correlates]
- Use the 1,186-run NEON subset with sampling-campaign identifiers and restricted permutations or mixed-effects models to test whether the vegetation and geography signal survives sub-batch control. [src: euk_in_prok_correlates]
- Resolve pooled-run heterogeneity by retaining all biosample-level protocol and environmental labels, then compare run-level models with measurement-error or partial-pooling models to quantify label-noise attenuation. [src: euk_in_prok_correlates]
- Expand the analysis to additional studies with recorded sequencing depth and laboratory metadata, then use GroupKFold by study to ask whether protocol-aware models generalize beyond the dominant NEON soil study. [src: euk_in_prok_correlates]
