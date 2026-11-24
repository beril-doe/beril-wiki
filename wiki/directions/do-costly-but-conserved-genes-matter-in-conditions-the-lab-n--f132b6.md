---
type: "Research direction"
description: "Thousands of core genes burden growth in lab conditions yet stay conserved. Do they carry fitness benefits under other conditions, or is the burden a measurement artifact?"
hypothesis: "Costly conserved genes are more likely than other core genes to show a strong fitness defect in at least one other tested condition, which fits selection maintaining them for conditions outside the burden-scoring experiments."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Fitness and pangenome tables are in the catalog, but per-gene fitness values and the cluster join were not shown, so compute is needed."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.experiment", "kbase.ke_pangenome.gene_cluster"]
findings: ["core_gene_tradeoffs--35113c1c", "core_gene_tradeoffs--fef60979", "core_gene_tradeoffs--fbfb5326"]
conflicts: []
papers: ["29769716", "22761588", "36097170", "25968644"]
builds_on: ["findings/core_gene_tradeoffs--35113c1c", "findings/core_gene_tradeoffs--fef60979", "findings/core_gene_tradeoffs--fbfb5326"]
projects: ["core_gene_tradeoffs"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do costly but conserved genes matter in conditions the lab never tested?

Thousands of core genes burden growth in lab conditions yet stay conserved. Do they carry fitness benefits under other conditions, or is the burden a measurement artifact?

## Hypothesis

Costly conserved genes are more likely than other core genes to show a strong fitness defect in at least one other tested condition, which fits selection maintaining them for conditions outside the burden-scoring experiments.

## Why it matters

It would separate true conditional essentiality from noise in burden calls and show how much of the conserved genome the standard lab conditions miss.

## How to test it

In Fitness Browser data, define costly conserved genes (burden in some experiment, core in the pangenome). Compare them with matched core genes, matched on functional category such as RNA metabolism, on whether they have strong defects in other experiments and on how many condition classes show defects. Require a burden in at least two independent experiments, to guard against single-experiment noise. Include the cell wall category, where non-core genes were more burdensome.

## What would support or refute it

Support: costly conserved genes have more conditional defects than matched core genes. Refute: they look like matched core genes or defects are absent, which would point to noise or trade-offs without a benefit.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Fitness and pangenome tables are in the catalog, but per-gene fitness values and the cluster join were not shown, so compute is needed.

## Builds on

- Finding: [[findings/core_gene_tradeoffs--35113c1c|Costly yet conserved genes suggest purifying selection despite metabolic cost]] (Candidate novel)
- Finding: [[findings/core_gene_tradeoffs--fef60979|Core RNA Metabolism genes are disproportionately burdensome in the lab]] (Candidate novel)
- Finding: [[findings/core_gene_tradeoffs--fbfb5326|Cell Wall reverses the core-gene burden pattern]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 36097170](https://pubmed.ncbi.nlm.nih.gov/36097170/) A bacterial pan-genome makes gene essentiality strain-dependent and evolvable.
- [PMID 25968644](https://pubmed.ncbi.nlm.nih.gov/25968644/) Rapid quantification of mutant fitness in diverse bacteria by sequencing randomly bar-coded transposons.

29769716 and 22761588 give the fitness data and gene-cost concept. They do not test whether costly conserved genes carry benefits in other conditions.
