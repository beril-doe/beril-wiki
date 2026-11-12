---
type: "Research direction"
description: "Do gut communities form a continuous gradient, so that the Crohn's candidate species replicate while discrete state labels shift between cohorts?"
hypothesis: "A one-dimensional gradient fitted to many cohorts predicts Crohn's candidate abundance as well as the four labelled states do, and its placement of samples agrees across studies far better than the labels do."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "The catalog shows cohort sample metadata and an E. coli abundance table but not the species abundance matrix the models need."
databases: ["arkinlab.cmd_reference"]
tables: ["arkinlab.cmd_reference.sample_metadata", "arkinlab.cmd_reference.ecoli_relab_by_cohort"]
findings: ["ibd_phage_targeting--56e3bb7d", "ibd_phage_targeting--d7f80dce"]
conflicts: []
papers: ["39244168", "41726920"]
builds_on: ["findings/ibd_phage_targeting--56e3bb7d", "findings/ibd_phage_targeting--d7f80dce"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Do gut communities form a continuous gradient that explains why candidate species replicate?

Do gut communities form a continuous gradient, so that the Crohn's candidate species replicate while discrete state labels shift between cohorts?

## Hypothesis

A one-dimensional gradient fitted to many cohorts predicts Crohn's candidate abundance as well as the four labelled states do, and its placement of samples agrees across studies far better than the labels do.

## Why it matters

The state labels agreed poorly across studies even though the candidate list replicated in held-out samples. If a gradient explains this, patient stratification should use position on a gradient and not state labels.

## How to test it

Using multi-cohort gut metagenomic profiles with sample metadata, fit a discrete mixture model and a continuous latent gradient model to the same samples. Compare how well each predicts held-out candidate abundance and Crohn's status within each cohort, and how stable sample positions are across studies. Use the E1 candidate list that replicated in the held-out HMP2 samples as the target.

## What would support or refute it

Support: the gradient predicts candidates and disease as well as the states, with steadier positions across studies. Refutation: the discrete states predict candidates better, or positions are no steadier, so the replication reflects real discrete structure.

## Data

Approach: lakehouse analysis. Readiness: unknown. The catalog shows cohort sample metadata and an E. coli abundance table but not the species abundance matrix the models need.

## Builds on

- Finding: [[findings/ibd_phage_targeting--56e3bb7d|Ecotype-specific targeting survives, but the earlier Jaccard statistic was replaced]] (Insufficient literature evidence)
- Finding: [[findings/ibd_phage_targeting--d7f80dce|E1 Crohn's candidate species replicate in held-out HMP2 cohort]] (Insufficient literature evidence)

## Closest published work

- [PMID 39244168](https://pubmed.ncbi.nlm.nih.gov/39244168/) Population-specific differences in the human microbiome: Factors defining the diversity.
- [PMID 41726920](https://pubmed.ncbi.nlm.nih.gov/41726920/) Enhanced multi-omic viral profiling from microbial community sequencing with BAQLaVa.

PMID 39244168 shows microbiome differences between populations and PMID 41726920 profiles viruses in the same HMP2 cohort; neither asks whether discrete community states or a continuous gradient explains candidate replication.
