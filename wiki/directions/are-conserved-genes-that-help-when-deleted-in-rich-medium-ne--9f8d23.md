---
type: "Research direction"
description: "Core genes in motility, RNA metabolism and protein metabolism are more often beneficial to delete than accessory genes are. Do those benefits vanish or reverse in structured, competitive environments?"
hypothesis: "The deletion benefit is an artefact of shaken rich medium. In sand or soil-like structured culture, or in mixed community culture, the same core genes become important, which would explain why selection keeps them."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Existing browser data are all from laboratory media, so structured and competitive conditions require new library experiments."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["conservation_fitness_synthesis--415598f3", "conservation_fitness_synthesis--d115e8ed", "conservation_fitness_synthesis--b05bd909", "core_gene_tradeoffs--fef60979"]
conflicts: []
papers: ["22448042", "22761588", "29769716"]
builds_on: ["findings/conservation_fitness_synthesis--415598f3", "findings/conservation_fitness_synthesis--d115e8ed", "findings/conservation_fitness_synthesis--b05bd909", "findings/core_gene_tradeoffs--fef60979"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Are conserved genes that help when deleted in rich medium needed in structured habitats?

Core genes in motility, RNA metabolism and protein metabolism are more often beneficial to delete than accessory genes are. Do those benefits vanish or reverse in structured, competitive environments?

## Hypothesis

The deletion benefit is an artefact of shaken rich medium. In sand or soil-like structured culture, or in mixed community culture, the same core genes become important, which would explain why selection keeps them.

## Why it matters

It would test directly whether conservation reflects selection in nature that laboratory fitness assays miss. If the benefit persists in structured habitats, these genes may be genuinely costly and kept by other forces.

## How to test it

In the Fitness Browser, list core genes in motility and chemotaxis, RNA metabolism and protein metabolism whose deletion helps in some conditions. Then run barcoded transposon libraries of two or three organisms from the browser in shaken rich medium, in sand- or soil-matrix culture, and in competition with a second species. Compare each gene's fitness across the three settings against accessory genes with similar lab cost.

## What would support or refute it

Support: flagellar and other core-burden genes lose their deletion benefit or become important in structured or competitive culture, more than matched accessory genes. Refutation: the benefit persists unchanged, so the cost is real and conservation has another explanation.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Existing browser data are all from laboratory media, so structured and competitive conditions require new library experiments.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/conservation_fitness_synthesis--415598f3|Core genes are more often burdens than accessory genes]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--d115e8ed|The core-burden excess is driven by specific functional categories]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--b05bd909|Lab-costly but conserved genes suggest purifying selection in nature]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--fef60979|Core genes are disproportionately burdensome in protein, motility and RNA metabolism]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 22448042 predicts loss of costly dispensable functions and 22761588 treats selection-driven gene loss, while 29769716 reports mutant phenotypes in laboratory conditions. None tests conserved but laboratory-costly genes in structured or competitive settings.
