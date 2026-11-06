---
type: "Research direction"
description: "Does the near-independence of urea fitness from other carbon sources in ADP1 reflect different NADH and respiratory demand, and not just a distinct gene set?"
hypothesis: "Urea growth differs from the other carbon sources in its dependence on Complex I, so Complex I deletion, alone or combined with deletion of any NDH-2 gene, produces carbon-source-specific defects that match the fitness correlation structure (urea r = 0.11 with quinate)."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The urea correlation exists, but mutant construction, NADH/NAD+ assays and co-purification are new experiments."
collections: ["kbase-ke-pangenome"]
findings: ["acinetobacter_adp1_explorer--df385e36", "acinetobacter_adp1_explorer--4460d103", "acinetobacter_adp1_explorer--1cfedc83"]
conflicts: []
papers: ["18840283", "18319726", "17437026"]
builds_on: ["findings/acinetobacter_adp1_explorer--df385e36", "findings/acinetobacter_adp1_explorer--4460d103", "findings/acinetobacter_adp1_explorer--1cfedc83"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Is urea fitness independent of other carbons because of respiratory wiring or separate genes?

Does the near-independence of urea fitness from other carbon sources in ADP1 reflect different NADH and respiratory demand, and not just a distinct gene set?

## Hypothesis

Urea growth differs from the other carbon sources in its dependence on Complex I, so Complex I deletion, alone or combined with deletion of any NDH-2 gene, produces carbon-source-specific defects that match the fitness correlation structure (urea r = 0.11 with quinate).

## Why it matters

It would explain condition-specific essentiality through redox flux and show whether unannotated essential genes are respiratory accessory factors. The competing reading, that urea needs the respiratory chain like the other carbons, would make the independence a gene-set property.

## How to test it

First search the ADP1 genome for NDH-2 genes. Then delete a Complex I subunit, and the NDH-2 gene if present, singly and in combination. Grow on quinate, glucose, acetate, lactate and urea, and measure NADH/NAD+. Test the co-fitness partners ACIAD3137 and ACIAD2176 by co-purification with Complex I. In the lakehouse, test K03885 against K00330-K00343 co-occurrence across pangenome species.

## What would support or refute it

Support: Complex I deletion gives defects on quinate and glucose-type substrates that differ from urea, and NDH-2 loss shifts dependence on Complex I. Refute: urea shows the same Complex I dependence as the other carbons, or no genotype changes the condition pattern.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The urea correlation exists, but mutant construction, NADH/NAD+ assays and co-purification are new experiments.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--df385e36|Urea fitness nearly independent of other carbon-source fitness]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--4460d103|Unannotated essential genes are leads for novel essential functions]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--1cfedc83|FBA and TnSeq essentiality agree for about three-quarters of shared genes]] (Extends retrieved work)

## Closest published work

- [PMID 18840283](https://pubmed.ncbi.nlm.nih.gov/18840283/) Iterative reconstruction of a global metabolic model of Acinetobacter baylyi ADP1 using high-throughput growth phenotype and gene essentiality data.
- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.
- [PMID 17437026](https://pubmed.ncbi.nlm.nih.gov/17437026/) A genome-scale computational study of the interplay between transcriptional regulation and metabolism.

PMID 18840283 and PMID 18319726 describe the ADP1 deletion collection and FBA essentiality consistency; neither tests respiratory compensation or condition-specific redox flux.
