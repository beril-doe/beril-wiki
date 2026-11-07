---
type: "Research direction"
description: "Deleting a conserved gene helps growth more often than deleting an accessory gene. The excess is concentrated in protein metabolism, RNA metabolism and motility. Does the benefit of deletion occur only in conditions that do not call on the gene's function?"
hypothesis: "Conserved genes that help growth when deleted do so mainly in experiments where their function is unneeded, for example flagellar genes in shaken liquid culture. The same genes matter in experiments that do use the function."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Fitness values and core status are linked for the burden findings, but whether experiment metadata can classify function use for each category has not been shown."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["core_gene_tradeoffs--fef60979", "core_gene_tradeoffs--a0b96f0f", "core_gene_tradeoffs--c29ab7fa", "conservation_fitness_synthesis--d115e8ed", "conservation_fitness_synthesis--b05bd909"]
conflicts: []
papers: ["29769716", "22761588", "25968644", "25112473"]
builds_on: ["findings/core_gene_tradeoffs--fef60979", "findings/core_gene_tradeoffs--a0b96f0f", "findings/core_gene_tradeoffs--c29ab7fa", "findings/conservation_fitness_synthesis--d115e8ed", "findings/conservation_fitness_synthesis--b05bd909"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Are conserved genes costly only under conditions where their function sits idle?

Deleting a conserved gene helps growth more often than deleting an accessory gene. The excess is concentrated in protein metabolism, RNA metabolism and motility. Does the benefit of deletion occur only in conditions that do not call on the gene's function?

## Hypothesis

Conserved genes that help growth when deleted do so mainly in experiments where their function is unneeded, for example flagellar genes in shaken liquid culture. The same genes matter in experiments that do use the function.

## Why it matters

It would show whether the puzzle of genes that are conserved yet costly in the lab is an artifact of lab conditions or a real trade-off. That decides how far lab fitness can be used to judge selection in nature.

## How to test it

Take gene-by-experiment fitness for the Fitness Browser organisms and link each gene to its core status in the Pangenome Collection. For costly core genes in the three named categories, label experiments as using or not using the function from the experiment's recorded growth mode and medium (for example shaken versus static or semisolid for flagellar genes). Where the records do not support a label, leave that experiment unlabeled. Compare how often burden and importance fall in the same genes, and in which experiment class each occurs.

## What would support or refute it

Support: genes that are costly when idle are the ones that are important when used, with burden concentrated in function-idle experiments. Refute: burden is spread evenly across experiment classes, or costly core genes are important nowhere, which would point to a real cost.

## Data

Approach: lakehouse analysis. Readiness: unknown. Fitness values and core status are linked for the burden findings, but whether experiment metadata can classify function use for each category has not been shown.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/core_gene_tradeoffs--fef60979|Core genes are disproportionately burdensome in protein, motility and RNA metabolism]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--a0b96f0f|Many genes are important in some conditions and burdensome in others]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--c29ab7fa|Trade-off genes are enriched among core genes]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--d115e8ed|The core-burden excess is driven by specific functional categories]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--b05bd909|Lab-costly but conserved genes suggest purifying selection in nature]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.
- [PMID 25112473](https://pubmed.ncbi.nlm.nih.gov/25112473/) Towards an informative mutant phenotype for every bacterial gene.

PMID 29769716 maps condition-specific mutant phenotypes for poorly annotated genes, and PMID 22761588 discusses selection-driven gene loss. Neither asks whether the burden of conserved genes tracks whether their function is in use.
