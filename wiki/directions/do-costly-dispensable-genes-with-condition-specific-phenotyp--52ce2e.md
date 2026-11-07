---
type: "Research direction"
description: "Some genes cost growth in the lab yet are not conserved, and a minority of them still have condition-specific phenotypes. Are those with phenotypes retained in more genomes of their species than those without?"
hypothesis: "Among costly, non-conserved genes, those with a condition-specific phenotype are carried by a larger share of their species' genomes, and are less often singletons, than those without one, because conditional benefit slows their loss."
approach: "lakehouse analysis"
readiness: "data in the lakehouse"
readiness_basis: "Fitness classes and per-gene pangenome links already exist for the organisms in the costly-dispensable findings."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["costly_dispensable_genes--7f8211ca", "costly_dispensable_genes--f4e2ff44"]
conflicts: []
papers: ["22448042", "29769716", "22761588"]
builds_on: ["findings/costly_dispensable_genes--7f8211ca", "findings/costly_dispensable_genes--f4e2ff44"]
projects: ["costly_dispensable_genes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do costly dispensable genes with condition-specific phenotypes persist longer in their species?

Some genes cost growth in the lab yet are not conserved, and a minority of them still have condition-specific phenotypes. Are those with phenotypes retained in more genomes of their species than those without?

## Hypothesis

Among costly, non-conserved genes, those with a condition-specific phenotype are carried by a larger share of their species' genomes, and are less often singletons, than those without one, because conditional benefit slows their loss.

## Why it matters

It would give a measurable link between occasional conditional usefulness and gene retention, testing whether costly accessory genes are simply on their way out or are held by selection.

## How to test it

For Fitness Browser organisms, take costly, non-conserved genes and split them by presence of a condition-specific phenotype. Using the Pangenome Collection, compare the share of species genomes carrying each gene and the singleton fraction between the two groups, matching on gene length and organism. Repeat within mobile-element-annotated genes only, since those dominate this class.

## What would support or refute it

Support: genes with a phenotype are carried by more genomes and are fewer singletons than matched genes without one. Refute: prevalence and singleton fraction are equal, or genes with phenotypes are rarer, meaning conditional benefit does not slow loss.

## Data

Approach: lakehouse analysis. Readiness: data in the lakehouse. Fitness classes and per-gene pangenome links already exist for the organisms in the costly-dispensable findings.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/costly_dispensable_genes--7f8211ca|Costly dispensable genes are not inert: some have condition-specific phenotypes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--f4e2ff44|Singleton fraction contrast with costly conserved genes is partly structural]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.

PMID 22448042 predicts that costly, dispensable functions are lost, and PMID 29769716 reports condition-specific phenotypes. Neither tests whether having such a phenotype predicts how widely a costly dispensable gene is retained.
