---
type: "Research direction"
description: "Does the depletion of strong-phenotype truly dark genes in stress conditions reflect real biology, such as niche-specific roles, or limited condition coverage and polar effects?"
hypothesis: "The depletion persists after excluding genes in operons with annotated neighbours (polar-effect candidates) and after matching for number of conditions tested per organism, and dark genes instead show strong phenotypes in carbon or nitrogen conditions."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Experiment and gene tables are in the catalog; fitness value tables and operon calls were not shown and may need computing."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.specog"]
findings: ["truly_dark_genes--48796df1", "functional_dark_matter--96020d65"]
conflicts: []
papers: ["29769716", "25968644", "22125499"]
builds_on: ["findings/truly_dark_genes--48796df1", "findings/functional_dark_matter--96020d65"]
projects: ["functional_dark_matter", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Why are truly dark genes with strong phenotypes depleted in stress conditions?

Does the depletion of strong-phenotype truly dark genes in stress conditions reflect real biology, such as niche-specific roles, or limited condition coverage and polar effects?

## Hypothesis

The depletion persists after excluding genes in operons with annotated neighbours (polar-effect candidates) and after matching for number of conditions tested per organism, and dark genes instead show strong phenotypes in carbon or nitrogen conditions.

## Why it matters

It would redirect screens for dark-gene function away from standard stress panels and toward nutrient and niche-specific conditions.

## How to test it

Using Fitness Browser experiments and fitness data, classify conditions by class, flag dark genes adjacent to annotated same-strand genes as possible polar cases, and compare strong-phenotype rates by condition class between truly dark and annotation-lag genes within each organism. Then pick dark genes with phenotypes in unusual conditions and test them with targeted mutants in a tractable organism.

## What would support or refute it

Support: depletion holds in polar-filtered, condition-matched data. Refute: it disappears once polar candidates or condition depth are controlled, meaning the earlier result was an artifact.

## Data

Approach: analysis then experiment. Readiness: needs compute. Experiment and gene tables are in the catalog; fitness value tables and operon calls were not shown and may need computing.

## Builds on

- Finding: [[findings/truly_dark_genes--48796df1|Truly dark genes are depleted, not enriched, in stress conditions]] (Candidate novel)
- Finding: [[findings/functional_dark_matter--96020d65|Stress dark genes are not more accessory than carbon/nitrogen genes]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 22125499](https://pubmed.ncbi.nlm.nih.gov/22125499/) Evidence-based annotation of gene function in Shewanella oneidensis MR-1 using genome-wide fitness profiling across 121 conditions.

29769716 and 22125499 report phenotypes for poorly annotated genes but do not compare dark and annotation-lag genes by condition class.
