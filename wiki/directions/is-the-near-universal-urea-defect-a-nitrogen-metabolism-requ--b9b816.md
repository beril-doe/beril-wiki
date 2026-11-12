---
type: "Research direction"
description: "In the ADP1 deletion collection, nearly all genes show severe defects on urea but few on quinate, and urea behaves largely independently of the carbon sources. Does urea reveal a distinct nitrogen-metabolism gene set, or does slow growth on it magnify every defect?"
hypothesis: "The urea defects are mostly nitrogen-specific: when growth rate is matched with a slow, non-urea nitrogen condition, a compact set of nitrogen-handling genes stays defective on urea while the broad defect fraction falls."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "The existing data is a single set of 8 conditions, with no nitrogen-source or growth-rate-matched comparison."
collections: []
findings: ["adp1_deletion_phenotypes--f675f8be", "adp1_deletion_phenotypes--69241676", "adp1_deletion_phenotypes--e7f5d7d3"]
conflicts: []
papers: ["18319726", "25374488"]
builds_on: ["findings/adp1_deletion_phenotypes--f675f8be", "findings/adp1_deletion_phenotypes--69241676", "findings/adp1_deletion_phenotypes--e7f5d7d3"]
projects: ["adp1_deletion_phenotypes"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Is the near-universal urea defect a nitrogen-metabolism requirement or a slow-growth effect?

In the ADP1 deletion collection, nearly all genes show severe defects on urea but few on quinate, and urea behaves largely independently of the carbon sources. Does urea reveal a distinct nitrogen-metabolism gene set, or does slow growth on it magnify every defect?

## Hypothesis

The urea defects are mostly nitrogen-specific: when growth rate is matched with a slow, non-urea nitrogen condition, a compact set of nitrogen-handling genes stays defective on urea while the broad defect fraction falls.

## Why it matters

It would tell whether the demanding tier reports real nitrogen-source requirements or a growth-rate threshold, which determines how condition-specific gene sets from deletion collections should be read.

## How to test it

Grow the ADP1 deletion collection on urea as nitrogen source and on a non-urea nitrogen source at the same carbon source, plus a slow-growth control condition chosen to match the urea growth rate. Compare the defect fractions and identify genes defective on urea but not in the growth-matched control; compare them with the genes specific to urea in the existing data.

## What would support or refute it

Support: the broad defect fraction drops in the growth-matched control and the retained urea-only genes form a compact nitrogen-related set. Refute: the broad defect fraction persists in the slow control, showing a growth-rate effect rather than a urea-specific requirement.

## Data

Approach: experiment. Readiness: needs new measurements. The existing data is a single set of 8 conditions, with no nitrogen-source or growth-rate-matched comparison.

## Builds on

- Finding: [[findings/adp1_deletion_phenotypes--f675f8be|Carbon sources split into demanding, moderate and robust growth-defect tiers]] (Extends retrieved work)
- Finding: [[findings/adp1_deletion_phenotypes--69241676|A third of genes concentrate growth importance on one carbon source]] (Insufficient literature evidence)
- Finding: [[findings/adp1_deletion_phenotypes--e7f5d7d3|Eight conditions provide about five independent phenotypic dimensions]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 25374488](https://pubmed.ncbi.nlm.nih.gov/25374488/) Novel metabolic features in Acinetobacter baylyi ADP1 revealed by a multiomics approach.

PMID 18319726 phenotyped the ADP1 deletion collection on several carbon sources and PMID 25374488 studied quinate-specific expression changes. Neither tests whether growth rate drives the demand tiers.
