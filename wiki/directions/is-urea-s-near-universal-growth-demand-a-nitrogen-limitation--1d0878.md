---
type: "Research direction"
description: "Why do 97.9% of genes in the filtered 2,034-gene matrix show severe defects on urea at ratio < 0.5, while urea fitness is nearly uncorrelated with quinate (r = 0.11) and weakly with other conditions (r = 0.12-0.28)?"
hypothesis: "Urea is a slow nitrogen-limited substrate, so broad defects come from general physiological sensitivity. Beyond the urease genes, urea-specific effects are few once urea is supplied as nitrogen with a permissive carbon source."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "ADP1 data are in the explorer database, which is not among the listed collections, and ADP1 is absent from the Fitness Browser; the new conditions need new assays."
collections: []
findings: ["acinetobacter_adp1_explorer--df385e36", "acinetobacter_adp1_explorer--886c47ff", "adp1_deletion_phenotypes--f675f8be", "adp1_deletion_phenotypes--e7f5d7d3"]
conflicts: []
papers: ["18319726", "25374488", "18840283"]
builds_on: ["findings/acinetobacter_adp1_explorer--df385e36", "findings/acinetobacter_adp1_explorer--886c47ff", "findings/adp1_deletion_phenotypes--f675f8be", "findings/adp1_deletion_phenotypes--e7f5d7d3"]
projects: ["acinetobacter_adp1_explorer", "adp1_deletion_phenotypes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Is urea's near-universal growth demand a nitrogen-limitation effect rather than urea-specific gene use?

Why do 97.9% of genes in the filtered 2,034-gene matrix show severe defects on urea at ratio < 0.5, while urea fitness is nearly uncorrelated with quinate (r = 0.11) and weakly with other conditions (r = 0.12-0.28)?

## Hypothesis

Urea is a slow nitrogen-limited substrate, so broad defects come from general physiological sensitivity. Beyond the urease genes, urea-specific effects are few once urea is supplied as nitrogen with a permissive carbon source.

## Why it matters

It would show whether continuous phenotype landscapes of about 5 independent dimensions reflect specific gene sets or growth-rate sensitivity, guiding how to design condition panels.

## How to test it

In the ADP1 deletion collection, grow the mutants with urea as sole carbon source versus urea as nitrogen source with a permissive carbon source, and replicate timepoints because the original growth ratios are single-timepoint. Compare the fraction of genes with defects (ratio < 0.5) and the pairwise correlations between conditions. The matrix excludes 499 essential and 316 incomplete-data genes, so interpret results for dispensable genes only.

## What would support or refute it

Support: defect fractions fall sharply when urea is only the nitrogen source and the correlation with other carbon sources rises. Refute: the urea fraction and low correlations persist in the nitrogen-source design, which would indicate genuinely urea-specific genes.

## Data

Approach: experiment. Readiness: needs new measurements. ADP1 data are in the explorer database, which is not among the listed collections, and ADP1 is absent from the Fitness Browser; the new conditions need new assays.

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--df385e36|Urea fitness nearly independent of other carbon-source fitness]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--f675f8be|Carbon sources split into demanding, moderate and robust growth-defect tiers]] (Extends retrieved work)
- Finding: [[findings/adp1_deletion_phenotypes--e7f5d7d3|Eight conditions provide about five independent phenotypic dimensions]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.
- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.

PMID 18319726 phenotyped the ADP1 deletion collection and PMID 25374488 used a multiomics approach. Neither separates a nitrogen-source effect from a carbon-source effect for urea.
