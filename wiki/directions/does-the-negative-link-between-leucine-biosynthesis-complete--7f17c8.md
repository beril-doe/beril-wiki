---
type: "Research direction"
description: "Is communities' leucine-pathway completeness lower where ambient leucine is higher in general, as a Black Queen-style cross-feeding signal, or only in one study?"
hypothesis: "The negative association holds in at least several independent studies with similar direction once study is a random effect; if it reflects one cohort, it vanishes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Catalog shows metabolomics, taxonomy, file-to-sample mapping and study tables; the number of studies with paired data was not shown."
databases: ["kbase.nmdc_arkin", "nmdc.metadata"]
tables: ["kbase.nmdc_arkin.metabolomics_gold", "kbase.nmdc_arkin.centrifuge_gold", "kbase.nmdc_arkin.omics_files_table", "nmdc.metadata.study_set"]
findings: ["nmdc_community_metabolic_ecology--33da3819"]
conflicts: []
papers: ["31316056", "35085485", "33311510"]
builds_on: ["findings/nmdc_community_metabolic_ecology--33da3819"]
projects: ["nmdc_community_metabolic_ecology"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does the negative link between leucine biosynthesis completeness and ambient leucine hold across independent NMDC studies?

Is communities' leucine-pathway completeness lower where ambient leucine is higher in general, as a Black Queen-style cross-feeding signal, or only in one study?

## Hypothesis

The negative association holds in at least several independent studies with similar direction once study is a random effect; if it reflects one cohort, it vanishes.

## Why it matters

A reproducible link would show that environmental metabolite pools shape which community members keep biosynthesis genes, a prediction about gene loss under cross-feeding.

## How to test it

Match NMDC metabolomics features with taxonomy profiles by sample across all studies having both, compute pathway completeness per community, and fit leucine intensity against completeness with study as a random effect and leave-one-study-out checks. Compare leucine with arginine and with pathways showing no expected relation.

## What would support or refute it

Support: same-sign effect in most studies and in the pooled mixed model. Refute: the effect appears only in the original study or reverses elsewhere.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Catalog shows metabolomics, taxonomy, file-to-sample mapping and study tables; the number of studies with paired data was not shown.

## Builds on

- Finding: [[findings/nmdc_community_metabolic_ecology--33da3819|Leucine completeness negatively tracks ambient leucine after FDR correction]] (Candidate novel)

## Closest published work

- [PMID 31316056](https://pubmed.ncbi.nlm.nih.gov/31316056/) Predictive metabolomic profiling of microbial communities using amplicon or metagenomic sequences.
- [PMID 35085485](https://pubmed.ncbi.nlm.nih.gov/35085485/) Genomic structure predicts metabolite dynamics in microbial communities.
- [PMID 33311510](https://pubmed.ncbi.nlm.nih.gov/33311510/) Using metacommunity ecology to understand environmental metabolomes.

31316056, 35085485 and 33311510 link communities to metabolites by prediction or modelling; none tests this leucine association across studies.
