---
type: "Research direction"
description: "In ADP1 deletion mutants, fitness on urea tracked fitness on other carbon sources very little. Which genes are specific to urea, and do they belong to a nitrogen-handling program conserved across the genus rather than to central carbon metabolism?"
hypothesis: "Urea-specific fitness genes form a nitrogen-assimilation and regulation set that is much more conserved across Acinetobacter genomes than the genes shared by the carbon-source conditions."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "The ADP1 growth matrix exists but sits in a species-specific database, not the Fitness Browser, so linking its genes to the pangenome has not been shown."
collections: ["kbase-ke-pangenome"]
findings: ["acinetobacter_adp1_explorer--df385e36", "acinetobacter_adp1_explorer--886c47ff"]
conflicts: []
papers: ["18319726"]
builds_on: ["findings/acinetobacter_adp1_explorer--df385e36", "findings/acinetobacter_adp1_explorer--886c47ff"]
projects: ["acinetobacter_adp1_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does Acinetobacter ADP1 handle urea through its own gene set, separate from carbon metabolism?

In ADP1 deletion mutants, fitness on urea tracked fitness on other carbon sources very little. Which genes are specific to urea, and do they belong to a nitrogen-handling program conserved across the genus rather than to central carbon metabolism?

## Hypothesis

Urea-specific fitness genes form a nitrogen-assimilation and regulation set that is much more conserved across Acinetobacter genomes than the genes shared by the carbon-source conditions.

## Why it matters

Urea was largely independent of the other tested conditions, which suggests growth substrates differ in how many genes they recruit. A distinct, conserved urea gene set would show a separate nitrogen layer in a model organism and expose unannotated members of it.

## How to test it

From the ADP1 deletion growth data on 8 carbon sources, extract genes whose fitness is distinctive for urea. Check their conservation in the Pangenome Collection across Acinetobacter genomes and their annotation status. Then delete a sample of the urea-specific genes and test growth on urea as carbon versus nitrogen source in defined medium.

## What would support or refute it

Support: the urea-specific genes are enriched in nitrogen and regulatory functions and are more conserved than genes shared across carbon sources. Refute: they are a random or poorly conserved sample, or their loss affects growth equally with other nitrogen sources.

## Data

Approach: analysis then experiment. Readiness: unknown. The ADP1 growth matrix exists but sits in a species-specific database, not the Fitness Browser, so linking its genes to the pangenome has not been shown.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/acinetobacter_adp1_explorer--df385e36|Urea fitness nearly independent of other carbon-source fitness]] (Insufficient literature evidence)
- Finding: [[findings/acinetobacter_adp1_explorer--886c47ff|ADP1 is absent from the Fitness Browser]] (Insufficient literature evidence)

## Closest published work

- [PMID 18319726](https://pubmed.ncbi.nlm.nih.gov/18319726/) A complete collection of single-gene deletion mutants of Acinetobacter baylyi ADP1.

PMID 18319726 built the ADP1 single-gene deletion collection, but it does not ask whether urea growth uses a separate gene set.
