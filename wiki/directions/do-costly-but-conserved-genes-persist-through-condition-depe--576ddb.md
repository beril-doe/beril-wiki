---
type: "Research direction"
description: "Are genes that are burdensome in the lab yet conserved in pangenomes retained by condition-dependent benefits, and do costly dispensable genes instead show signatures of ongoing loss?"
hypothesis: "Costly-conserved genes, concentrated in motility, RNA metabolism and protein metabolism, are essential or beneficial under some natural-like conditions and are rarely lost across related strains. Costly dispensable genes, which are mobile-element enriched, are patchily distributed and lost more often."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "The computational comparison uses existing tables, but the decisive field-like competition assays need new measurements."
collections: ["kescience-fitnessbrowser", "kbase-ke-pangenome"]
findings: ["conservation_fitness_synthesis--b05bd909", "conservation_fitness_synthesis--d115e8ed", "conservation_fitness_synthesis--415598f3", "core_gene_tradeoffs--a0b96f0f", "core_gene_tradeoffs--c29ab7fa", "costly_dispensable_genes--31cecf6a", "costly_dispensable_genes--7f8211ca"]
conflicts: []
papers: ["22448042", "22761588", "29769716", "38948139"]
builds_on: ["findings/conservation_fitness_synthesis--b05bd909", "findings/conservation_fitness_synthesis--d115e8ed", "findings/conservation_fitness_synthesis--415598f3", "findings/core_gene_tradeoffs--a0b96f0f", "findings/core_gene_tradeoffs--c29ab7fa", "findings/costly_dispensable_genes--31cecf6a", "findings/costly_dispensable_genes--7f8211ca"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs", "costly_dispensable_genes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do costly-but-conserved genes persist through condition-dependent benefit, unlike costly dispensable genes?

Are genes that are burdensome in the lab yet conserved in pangenomes retained by condition-dependent benefits, and do costly dispensable genes instead show signatures of ongoing loss?

## Hypothesis

Costly-conserved genes, concentrated in motility, RNA metabolism and protein metabolism, are essential or beneficial under some natural-like conditions and are rarely lost across related strains. Costly dispensable genes, which are mobile-element enriched, are patchily distributed and lost more often.

## Why it matters

It would show whether the burden paradox is a trade-off structure maintained by selection in nature or a laboratory artifact. It would also separate retention from loss as distinct regimes.

## How to test it

In Fitness Browser organisms with several sequenced relatives, compare three classes: costly-conserved, costly-dispensable and neutral-conserved genes. Measure conditions of importance (fit < -1) and burden (fit > 1), and gene loss on the species tree as patchy presence in close relatives. Then compete wild-type and mutant strains for selected flagellar and RNA-metabolism genes under soil, biofilm or host-like conditions.

## What would support or refute it

Support: costly-conserved genes show more importance conditions and lower loss rates than costly-dispensable genes, and a field-like assay shows a benefit for the mutant-versus-wild-type comparison. Refute: costly-conserved genes resemble neutral-conserved genes in importance conditions and loss, or field-like assays show no benefit.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. The computational comparison uses existing tables, but the decisive field-like competition assays need new measurements.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/conservation_fitness_synthesis--b05bd909|Lab-costly but conserved genes suggest purifying selection in nature]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--d115e8ed|The core-burden excess is driven by specific functional categories]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--415598f3|Core genes are more often burdens than accessory genes]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--a0b96f0f|Many genes are important in some conditions and burdensome in others]] (Insufficient literature evidence)
- Finding: [[findings/core_gene_tradeoffs--c29ab7fa|Trade-off genes are enriched among core genes]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--31cecf6a|Costly dispensable genes are strongly enriched for mobile-element keywords]] (Insufficient literature evidence)
- Finding: [[findings/costly_dispensable_genes--7f8211ca|Costly dispensable genes are not inert: some have condition-specific phenotypes]] (Insufficient literature evidence)

## Closest published work

- [PMID 22448042](https://pubmed.ncbi.nlm.nih.gov/22448042/) The Black Queen Hypothesis: evolution of dependencies through adaptive gene loss.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.

PMID 22448042 predicts loss of costly dispensable functions and PMID 22761588 addresses selection-driven gene loss. Neither compares conserved and dispensable costly genes by condition-dependent importance and observed loss.
