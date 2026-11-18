---
type: "Research direction"
description: "Conserved genes for motility, RNA metabolism and protein metabolism are more often beneficial to delete in the lab than accessory genes. For the specific motility genes whose loss helps growth in ordinary liquid culture, is there a setting where the same genes become important?"
hypothesis: "Motility and chemotaxis genes whose deletion improves growth in liquid culture are the same genes whose deletion is strongly harmful in surface-motility or soft-agar assays and in a soil or root setting. Lab burden of these conserved genes therefore reflects a benefit that appears only in structured habitats."
approach: "analysis then experiment"
readiness: "unknown"
readiness_basis: "The experiment table lists motility-assay descriptions and the gene and SEED-role tables exist, but the catalog did not show the per-gene fitness values, and the soil or root step needs new measurements."
databases: ["kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedroles", "kescience.fitnessbrowser.organism"]
findings: ["conservation_fitness_synthesis--d115e8ed", "conservation_fitness_synthesis--415598f3", "conservation_fitness_synthesis--b05bd909", "core_gene_tradeoffs--fef60979"]
conflicts: []
papers: ["22448042", "22761588", "29769716", "24739623"]
builds_on: ["findings/conservation_fitness_synthesis--d115e8ed", "findings/conservation_fitness_synthesis--415598f3", "findings/conservation_fitness_synthesis--b05bd909", "findings/core_gene_tradeoffs--fef60979"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do conserved motility genes that cost growth in liquid pay back in structured habitats?

Conserved genes for motility, RNA metabolism and protein metabolism are more often beneficial to delete in the lab than accessory genes. For the specific motility genes whose loss helps growth in ordinary liquid culture, is there a setting where the same genes become important?

## Hypothesis

Motility and chemotaxis genes whose deletion improves growth in liquid culture are the same genes whose deletion is strongly harmful in surface-motility or soft-agar assays and in a soil or root setting. Lab burden of these conserved genes therefore reflects a benefit that appears only in structured habitats.

## Why it matters

If it holds, lab cost for conserved genes can be read as a pointer to the natural setting that keeps them under selection, which turns a puzzle in the conservation-versus-fitness literature into a prediction. If the costly genes are not needed in any structured setting, the cost is simply tolerated or the genes are retained for other reasons.

## How to test it

Step 1, analysis: in the barcoded-fitness collection, list experiments that are motility or soft-agar assays, using the experiment descriptions, in organisms such as Keio, Putida and psRCH2. Using the gene and SEED-role tables, select motility and chemotaxis genes. For each gene, compare its effect in ordinary liquid experiments with its effect in the motility assays. Step 2, experiment: pool a barcoded Putida transposon library in liquid medium, in soft agar, and in soil or on plant roots, then ask whether genes that were costly in liquid are required in the structured settings. The catalog did not show the per-gene fitness values, so step 1 first needs those per-organism fitness tables.

## What would support or refute it

Support: genes that help growth when deleted in liquid are clearly harmful to lose in soft agar and in soil or on roots, more so than other costly gene groups. Refute: costly motility genes are unimportant in every structured setting tested, or the harmful effect falls on a different set of motility genes than the costly ones, which fits tolerated cost.

## Data

Approach: analysis then experiment. Readiness: unknown. The experiment table lists motility-assay descriptions and the gene and SEED-role tables exist, but the catalog did not show the per-gene fitness values, and the soil or root step needs new measurements.

## Builds on

- Finding: [[findings/conservation_fitness_synthesis--d115e8ed|The core-burden excess is driven by specific functional categories]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--415598f3|Core genes are more often burdens than accessory genes]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--b05bd909|Lab-costly but conserved genes suggest purifying selection in nature]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--fef60979|Core genes are disproportionately burdensome in protein, motility and RNA metabolism]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 24739623](https://pubmed.ncbi.nlm.nih.gov/24739623/) Implications of streamlining theory for microbial ecology.

PMID 22448042 and PMID 22761588 predict that costly dispensable functions are lost, and PMID 29769716 reports condition-specific phenotypes; none tests whether the specific costly motility genes of conserved gene sets pay back in structured habitats.
