---
type: "Research direction"
description: "For genes where model-predicted essentiality and transposon essentiality disagree in Acinetobacter baylyi ADP1, is the disagreement explained by redundant paralogs that the model leaves out?"
hypothesis: "Genes the model predicts essential but transposons call dispensable are enriched for paralogs that can cover the same reaction. Deleting both paralogs together will be lethal or severely growth-limiting."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The ADP1 database itself was not shown in the catalog, and the decisive step needs new double mutants."
databases: []
tables: []
findings: ["acinetobacter_adp1_explorer--1cfedc83", "acinetobacter_adp1_explorer--c925d9c6"]
conflicts: []
papers: ["18840283", "18319726"]
builds_on: ["findings/acinetobacter_adp1_explorer--1cfedc83", "findings/acinetobacter_adp1_explorer--c925d9c6"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Are FBA-versus-TnSeq disagreements in ADP1 mostly caused by redundant paralogs?

For genes where model-predicted essentiality and transposon essentiality disagree in Acinetobacter baylyi ADP1, is the disagreement explained by redundant paralogs that the model leaves out?

## Hypothesis

Genes the model predicts essential but transposons call dispensable are enriched for paralogs that can cover the same reaction. Deleting both paralogs together will be lethal or severely growth-limiting.

## Why it matters

It would show whether model errors reflect missing redundancy, which model edits can fix, or regulatory effects the model cannot capture, which would limit what flux models can predict.

## How to test it

Among the genes with both calls, list those the model predicts essential but transposons call dispensable. Identify paralogs for the same reaction by annotation, then construct double deletions for a panel of such pairs in ADP1 and measure growth on minimal medium. Include matched control pairs from concordant genes.

## What would support or refute it

Support: double deletions are lethal or strongly impaired while single deletions are tolerated, more often than in controls. Refute: double deletions grow normally, pointing to regulation or model error.

## Data

Approach: experiment. Readiness: needs new measurements. The ADP1 database itself was not shown in the catalog, and the decisive step needs new double mutants.

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--1cfedc83|FBA and TnSeq essentiality agree for about three-quarters of shared genes]] (Extends retrieved work)
- Finding: [[findings/acinetobacter_adp1_explorer--c925d9c6|A fifth of genes change FBA flux class between media]] (Extends retrieved work)

## Closest published work

- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 18840283 used discrepancies to refine the ADP1 model and PMID 18319726 built the deletion collection; neither tested whether discordant genes sit in redundant paralog pairs.
