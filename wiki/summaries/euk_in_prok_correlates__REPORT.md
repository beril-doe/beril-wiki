---
type: "Summary"
description: "Tests eukaryotic contamination correlates in NMDC metagenomes under batch control"
doc_type: "short"
full_text: "sources/euk_in_prok_correlates__REPORT.md"
---
# Metadata Correlates of Eukaryotic Contamination in NMDC Prokaryote-Targeted Metagenomes

## Overview

This project quantified eukaryotic read fractions across 2,759 NMDC ReadbasedAnalysis runs from 9 studies using native `nmdc.results` GOTTCHA2 classifications, then tested whether sample environment, geography, and sequencing metadata explain variation in eukaryotic signal. The central contribution is a methodological warning: strong cross-study environment associations are largely confounded with study/batch, whereas environmental effects become predictive within a batch-controlled study. [src: euk_in_prok_correlates]

## Key Findings

### Eukaryotic reads are common and mainly photosynthetic

GOTTCHA2 detected eukaryotic reads in 77% of the 2,759 runs. Among all runs, the median eukaryotic fraction was 2.7%, the mean was 13.3%, and 20% of runs exceeded 20% eukaryotic reads. Among runs with detectable eukaryotic signal, plastid sequences represented a median 100% of that signal, indicating that contamination in this environmental collection was dominated by plant or algal chloroplast DNA rather than animal-host DNA. [src: euk_in_prok_correlates]

The response variable was GOTTCHA2 relative eukaryotic abundance, defined as Eukaryota plus plastid abundance at superkingdom rank for each ReadbasedAnalysis run. It was strongly zero-inflated: 23% of runs had no detectable eukaryotic reads, with a long upper tail in which one in five runs exceeded 20% eukaryotic reads. [src: euk_in_prok_correlates]

Kraken2 and Centrifuge produced approximately 0 domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; Kraken's only eukaryotic kingdom was Metazoa/human. Consequently, GOTTCHA2 was the only usable estimator of eukaryotic fraction in this analysis, and the near-absence of a metazoan or host signal was informative for this largely environmental collection. [src: euk_in_prok_correlates]

### Eukaryotic source tracks sample matrix

Eukaryotic composition varied coherently by matrix. Aquatic freshwater samples had 99.5% eukaryotic detection and a plastid share of 1.00, with algal plastids as the dominant source. Terrestrial soil samples had 55.7% detection and a plastid share of 0.43, indicating mixed plant plastid, soil fungal, and protist signal. Plant-root samples had 100% detection and a plastid share of 0.03, with root-associated fungi and protists as the dominant non-plastid source. [src: euk_in_prok_correlates]

The eukaryotic fraction differed strongly by matrix in a Kruskal–Wallis test, with H=77.8 and p=1.3×10⁻¹⁷; all pairwise matrix contrasts were significant after BH-FDR, where FDR means false discovery rate. After excluding the `Unknown` or missing-metadata bucket, `ecosystem_type` reduced to the same three biomes—Soil, Freshwater, and Roots—and produced the same test as matrix rather than an independent confirmation. An earlier p≈10⁻⁵⁰ result that retained `Unknown` was a missingness artifact and was removed. [src: euk_in_prok_correlates]

### Cross-study environment effects are batch-confounded

In NMDC, each biome was approximately 80–100% nested within a single study, preventing the strong univariate environment association from being cleanly separated from study or batch. A gradient-boosted model of eukaryotic fraction gave R²=0.24 for `study_id` alone under random cross-validation, R²=0.35 for environment under random cross-validation, R²=−0.30 for environment under GroupKFold out-of-study validation, and R²=−0.39 for environment plus sequencing under GroupKFold. GroupKFold is cross-validation in which complete studies are held out as groups. [src: euk_in_prok_correlates]

Environment explained no more variance than `study_id` alone, and the out-of-study environment model performed worse than predicting the mean; its out-of-study detection AUC was 0.56, approximately chance. Adding sequencing platform and depth did not improve prediction. Thus, a naive cross-collection regression of eukaryotic fraction on environmental metadata would report a strong but largely batch-driven association. [src: euk_in_prok_correlates]

Across the collection, measured sequencing depth was negatively associated with eukaryotic fraction, with Spearman ρ=−0.29, p=5.2×10⁻⁷, and n=292 runs with measured depth. This association was not batch-controlled: measured-depth runs came from a handful of non-soil studies, while the dominant NEON soil study recorded no depth, so the result is suggestive rather than a controlled sequencing-depth effect. [src: euk_in_prok_correlates]

### Within one study, vegetation and geography are predictive

A batch-controlled analysis of the dominant NEON soil metagenome study included 1,186 runs from one sampling program with a constant protocol and batch. Within this study, local vegetation (`env_local_scale`, 11 levels) was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹. Median eukaryotic fractions were 23% in sedge/forb herbaceous soil, 14% in emergent wetland, 13% in dwarf scrub, and 2% in evergreen forest, while deciduous forest, cropland, and pasture were approximately 0. [src: euk_in_prok_correlates]

Geography also differed strongly across 47 sites, with H=310.4 and p=2.4×10⁻⁴⁶. The highest median fractions occurred at Arctic tundra sites—Utqiaġvik 30%, Caribou-Poker Creeks 22%, and Toolik 17%—compared with 2–8% in temperate forests. [src: euk_in_prok_correlates]

A model using local environment and geography achieved within-study five-fold R²=+0.17 ± 0.06, contrasting with the cross-study out-of-study R²=−0.30. This supports a genuine fine-scale environmental signal when batch is held approximately constant, while remaining subject to possible sub-batch confounding within the study. [src: euk_in_prok_correlates]

### Analysis design and data handling

The analysis used Kruskal–Wallis and Mann–Whitney tests with BH-FDR, plus cross-validated gradient boosting with GroupKFold by study. It analyzed data at the `workflow_run_id` level rather than the biosample level because 1,067 of 2,759 runs were pooled from multiple biosamples; biosample-level joins would inflate the sample size through pseudo-replication. [src: euk_in_prok_correlates]

The native `nmdc.results` tables were keyed by `data_object_id` or `workflow_run_id`. Runs were linked to biosamples and studies through `nmdc.metadata.biosample_to_workflow_run`, joined on `workflow_run_id`, and then through `biosample_set_associated_studies`, whose child tables are keyed by `parent_id`; this linked 99%+ of classified runs. Large read-based taxonomy tables, including the approximately 29M-row `kraken2_classification_report`, were aggregated to one row per `workflow_run_id` before joining metadata. [src: euk_in_prok_correlates]

## Caveats

The cross-study analysis included only approximately 9 studies, with one soil study accounting for approximately 43% of runs. The cross-study generalization test was therefore under-powered, and the within-study result was demonstrated for one soil study only; it may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

NMDC did not populate DNA-extraction kit, size fractionation or filtration, host-depletion method, or library-preparation fields. Processing booleans in `biosample_to_workflow_run` were near-constant, with `has_filtration` all false. The strongest literature-linked wet-lab factors therefore remain unmeasured residuals. [src: euk_in_prok_correlates]

Absolute eukaryotic fractions are classifier- and database-dependent. Because only GOTTCHA2 yielded a usable eukaryotic fraction, its values should be interpreted as relative or ordinal rather than calibrated absolute contamination. [src: euk_in_prok_correlates]

Even within the NEON soil study, `env_local_scale` and geography may track sub-batches such as sampling campaigns. The within-study analysis is the best available control, not a randomized design. [src: euk_in_prok_correlates]

Of the 2,759 runs, 1,067 were pooled from multiple biosamples. Each pooled run inherited environment and collection metadata from a single representative biosample selected by `MIN(biosample_id)`. If pooled biosamples differed in local metadata, this introduced predictor label noise; the report characterizes this as a conservative bias that can weaken associations rather than manufacture them. [src: euk_in_prok_correlates]

Sampling depth was not measured in the NEON soil study because it had zero non-null `depth` values. The depth association was therefore a cross-study statistic and was not part of the batch-controlled within-study result. [src: euk_in_prok_correlates]

The classifier databases were not interchangeable for eukaryote quantification: Kraken2 and Centrifuge were prokaryote-restricted in this NMDC deployment, whereas GOTTCHA2 was plastid- and eukaryote-aware. Cross-collection contamination-QC correlates should therefore control for study or batch using GroupKFold by study or within-study contrasts. [src: euk_in_prok_correlates]

## Slots Into

- [[concepts/environment-embedding-geography]] — the within-study vegetation and geography results show that environmental metadata can predict eukaryotic signal when batch is controlled. [src: euk_in_prok_correlates]
- [[concepts/cross-tenant-data-bridging]] — the report documents the NMDC results-to-metadata bridging required to connect workflow runs with biosamples and studies while avoiding pooled-run pseudo-replication. [src: euk_in_prok_correlates]
- [[concepts/multi-omics-integration]] — the analysis integrates read-based taxonomic results with environmental, study, and sequencing metadata and exposes classifier/database compatibility limits. [src: euk_in_prok_correlates]
