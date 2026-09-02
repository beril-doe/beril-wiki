---
type: "Concept"
description: "Pooled runs complicate statistical units and can add metadata label noise."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Pooled sequencing runs complicate the statistical unit and metadata assignment

A pooled sequencing run combines material from multiple biosamples, making the sequencing run—not each constituent biosample—the defensible statistical unit when the measured taxonomic result exists only once per run. In this report, 1,067 of 2,759 runs were pooled from multiple biosamples, so treating each biosample as an independent observation would create pseudo-replication, meaning artificial inflation of the apparent sample size by duplicating one run-level measurement. [src: euk_in_prok_correlates]

## Evidence from the NMDC analysis

The analysis therefore operated at the `workflow_run_id` level rather than the biosample level because 1,067 of 2,759 runs were pooled from multiple biosamples. [src: euk_in_prok_correlates] This choice preserved the unit at which the GOTTCHA2 eukaryotic abundance measurement was observed and avoided counting one pooled result multiple times. [src: euk_in_prok_correlates]

Pooled runs still required an environmental and study label for downstream association tests. Each pooled run inherited environment and collection metadata from a single representative biosample selected by `MIN(biosample_id)`, the minimum biosample identifier in the joined set. [src: euk_in_prok_correlates] If the pooled biosamples differed in local metadata, this assignment introduced predictor label noise rather than additional independent environmental observations. [src: euk_in_prok_correlates] The report characterizes this as a conservative bias that can weaken associations rather than manufacture them. [src: euk_in_prok_correlates]

The metadata bridge linked runs to biosamples and studies through `nmdc.metadata.biosample_to_workflow_run`, joined on `workflow_run_id`, and then through `biosample_set_associated_studies`, whose child tables are keyed by `parent_id`. [src: euk_in_prok_correlates] This procedure linked 99%+ of classified runs while retaining run-level aggregation. [src: euk_in_prok_correlates] Large read-based taxonomy tables, including the approximately 29M-row `kraken2_classification_report`, were aggregated to one row per `workflow_run_id` before metadata joins. [src: euk_in_prok_correlates]

## Statistical implications

The pooled-run structure separates two problems: pseudoreplication changes the effective number of observations, whereas representative-biosample assignment can mislabel predictors even when the run remains the correct response unit. [src: euk_in_prok_correlates] Consequently, a run-level analysis can avoid false precision without eliminating uncertainty about which biosample-level environment generated the pooled signal. [src: euk_in_prok_correlates]

This issue is directly relevant to [[concepts/cross-tenant-data-bridging]], because the validity of ecological inference depends on joining workflow results to the correct metadata grain. [src: euk_in_prok_correlates] It also refines [[concepts/schema-to-value-space-join-validation]]: successful key-based joins do not by themselves demonstrate that a pooled run has a uniquely correct environmental label. [src: euk_in_prok_correlates] The problem contributes to [[concepts/metadata-resolution-and-within-species-heterogeneity]], since metadata recorded at one biosample or representative-biosample level may not describe all material contributing to a pooled run. [src: euk_in_prok_correlates]

## Practical interpretation

The accompanying analysis used run-level observations for hypothesis testing and treated the inherited metadata as potentially noisy, rather than expanding pooled runs into independent biosample records. [src: euk_in_prok_correlates] This design is preferable to biosample-level pseudo-replication, but it does not replace explicit information about pooling composition, relative biosample contributions, or biosample-specific environmental metadata. [src: euk_in_prok_correlates]

## Open Directions

- Recover the complete set of biosamples and their contribution weights for the 1,067 pooled runs, then fit weighted or hierarchical models to test whether representative-biosample assignment changes effect estimates. [src: euk_in_prok_correlates]
- Compare `MIN(biosample_id)` labels with alternative pooled labels, such as majority environment or contribution-weighted environment, and quantify how much metadata-label noise changes association strength. [src: euk_in_prok_correlates]
- Reanalyze the eukaryotic-fraction models at the run level with cluster-robust or hierarchical uncertainty, using pooling structure as a grouping variable, to determine whether conclusions remain stable without biosample pseudo-replication. [src: euk_in_prok_correlates]
- Validate the run-to-biosample-to-study joins against explicit parent-child key audits and unresolved-record counts, asking whether the reported 99%+ linkage rate hides systematic failures among pooled or unusually structured records. [src: euk_in_prok_correlates]
