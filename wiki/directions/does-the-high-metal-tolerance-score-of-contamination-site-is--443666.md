---
type: "Research direction"
description: "Do isolates from heavy-metal-contaminated sites truly carry higher genome-predicted metal tolerance once taxonomy is accounted for, given that taxonomy already explains much of the score?"
hypothesis: "The contamination-site shift is mostly a taxonomic composition effect; within the same orders, contaminated-site isolates do not differ from environmental isolates beyond noise."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "The catalog showed only the BacDive isolation table; BacDive phenotype tables and the metal-score table were not shown, so feasibility depends on locating them."
databases: ["kescience.bacdive"]
tables: ["kescience.bacdive.isolation"]
findings: ["bacdive_metal_validation--09db2bda", "bacdive_phenotype_metal_tolerance--1dfee01c", "bacdive_phenotype_metal_tolerance--31230ece"]
conflicts: []
papers: ["37290750", "25594414", "29769716"]
builds_on: ["findings/bacdive_metal_validation--09db2bda", "findings/bacdive_phenotype_metal_tolerance--1dfee01c", "findings/bacdive_phenotype_metal_tolerance--31230ece"]
projects: ["bacdive_metal_validation", "bacdive_phenotype_metal_tolerance"]
topics: ["sampling-coverage-and-statistical-confounding"]
---
# Does the high metal-tolerance score of contamination-site isolates survive adequate sample size and taxonomic matching?

Do isolates from heavy-metal-contaminated sites truly carry higher genome-predicted metal tolerance once taxonomy is accounted for, given that taxonomy already explains much of the score?

## Hypothesis

The contamination-site shift is mostly a taxonomic composition effect; within the same orders, contaminated-site isolates do not differ from environmental isolates beyond noise.

## Why it matters

Genome-based tolerance scores are used to prioritise strains for bioremediation. If taxonomy absorbs the signal, isolation site adds no information and scores should be treated as lineage traits.

## How to test it

Using BacDive isolation categories, build contamination and baseline groups across the full database rather than the 10 matched isolates, and compare scores within order or class strata with a mixed model. Phenotype and metal-score tables were not shown in the catalog, so locate them first. Add a sample-size calculation per stratum before testing.

## What would support or refute it

Support: the within-order difference is near zero while the pooled difference stays near one standard deviation. Refute: a clear within-order shift remains with adequate group sizes.

## Data

Approach: lakehouse analysis. Readiness: unknown. The catalog showed only the BacDive isolation table; BacDive phenotype tables and the metal-score table were not shown, so feasibility depends on locating them.

## Builds on

- Finding: [[findings/bacdive_metal_validation--09db2bda|Heavy metal contamination isolates score higher on predicted metal tolerance]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--1dfee01c|Taxonomy explains metal tolerance variance; phenotypes add nothing beyond it]] (Candidate novel)
- Finding: [[findings/bacdive_phenotype_metal_tolerance--31230ece|Reversed urease effect is driven by Actinomycetes]] (Candidate novel)

## Closest published work

- [PMID 37290750](https://pubmed.ncbi.nlm.nih.gov/37290750/) Genotypic and Phenotypic Characterization of Antimicrobial and Heavy Metal Tolerance in Salmonella enterica and Escherichia coli Isolates from Swine Feed Mills.
- [PMID 25594414](https://pubmed.ncbi.nlm.nih.gov/25594414/) Copper tolerance mechanisms of Mesorhizobium amorphae and its role in aiding phytostabilization by Robinia pseudoacacia in copper contaminated soil.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

37290750 compares genotype with measured tolerance in two species; this direction asks how much isolation site adds beyond lineage across BacDive.
