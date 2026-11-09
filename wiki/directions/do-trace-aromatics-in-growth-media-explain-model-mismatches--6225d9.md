---
type: "Research direction"
description: "In ADP1, flux balance predictions and transposon essentiality disagree for about a quarter of shared genes, and aromatic degradation genes are strongly enriched among them. Is the mismatch a missing model input or a real substrate requirement?"
hypothesis: "The mismatch arises because trace aromatic compounds in nominally aromatic-free media make these genes necessary. Under rigorously scrubbed media the aromatic degradation genes will become dispensable, as the model predicts."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The ADP1 deletion collection, existing growth data and model exist, but the decisive growth assays in purified media do not."
collections: ["kbase-msd-biochemistry", "kbase-phenotype"]
findings: ["acinetobacter_adp1_explorer--1cfedc83", "adp1_deletion_phenotypes--ec39f324"]
conflicts: ["conflict--condition-space-dimensionality--aeb98adb"]
papers: ["18840283", "18319726", "8002591", "15691962"]
builds_on: ["findings/acinetobacter_adp1_explorer--1cfedc83", "findings/adp1_deletion_phenotypes--ec39f324", "conflicts/conflict--condition-space-dimensionality--aeb98adb"]
projects: ["acinetobacter_adp1_explorer", "adp1_deletion_phenotypes", "adp1_triple_essentiality"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do trace aromatics in growth media explain model mismatches for aromatic degradation genes?

In ADP1, flux balance predictions and transposon essentiality disagree for about a quarter of shared genes, and aromatic degradation genes are strongly enriched among them. Is the mismatch a missing model input or a real substrate requirement?

## Hypothesis

The mismatch arises because trace aromatic compounds in nominally aromatic-free media make these genes necessary. Under rigorously scrubbed media the aromatic degradation genes will become dispensable, as the model predicts.

## Why it matters

If trace inputs cause the mismatch, discordant genes can be partly resolved by correcting media rather than rewriting metabolism, and the sole discrete phenotypic module would reflect environmental contamination. If not, the model lacks real biology.

## How to test it

Regrow ADP1 deletion mutants of the 24 quinate-specific aromatic degradation genes in carefully purified defined media, with and without a defined trace of aromatic substrates. Compare growth with the existing ADP1 deletion growth data and with flux balance predictions made with the same media composition in the ModelSEED Biochemistry framework.

## What would support or refute it

Support: defects shrink in scrubbed media and reappear with added trace aromatics, matching the revised model. Refute: defects stay unchanged without any aromatic source, pointing to a real requirement or a regulatory effect the model omits.

## Data

Approach: experiment. Readiness: needs new measurements. The ADP1 deletion collection, existing growth data and model exist, but the decisive growth assays in purified media do not.

- Collection: [[data/kbase-msd-biochemistry|ModelSEED Biochemistry]]
- Collection: [[data/kbase-phenotype|Phenotype Collection]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--1cfedc83|FBA and TnSeq essentiality agree for about three-quarters of shared genes]] (Extends retrieved work)
- Finding: [[findings/adp1_deletion_phenotypes--ec39f324|Aromatic degradation genes form the only discrete phenotypic module]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--condition-space-dimensionality--aeb98adb|Aromatic degradation in *Acinetobacter baylyi* ADP1: substrate-specific requirement or model-input gap?]]

## Closest published work

- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 8002591](https://pubmed.ncbi.nlm.nih.gov/8002591/) The pca-pob supraoperonic cluster of Acinetobacter calcoaceticus contains quiA, the structural gene for quinate-shikimate dehydrogenase.
- [PMID 15691962](https://pubmed.ncbi.nlm.nih.gov/15691962/) Transcriptional organization of genes for protocatechuate and quinate degradation from Acinetobacter sp. strain ADP1.

PMID 18840283 used ADP1 knockout data to refine a metabolic model, and PMID 18319726 phenotyped the deletion collection. Neither tests whether trace media components cause the aromatic-pathway discrepancies.
