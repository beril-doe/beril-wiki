---
type: "Research direction"
description: "Do genes that make mutants grow better in the lab yet stay conserved across a species' genomes carry benefits under field-like conditions that standard assays miss?"
hypothesis: "Costly-but-conserved genes show fitness defects under field-relevant or ecologically realistic conditions, or strong benefits in other conditions, at a higher rate than costly-and-dispensable genes."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Fitness and pangenome tables are in the catalog; the robust burden classification and the cross-link must be computed, and ecological-condition tests need new assays."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.genefitness", "kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.besthitkegg", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.gene_genecluster_junction"]
findings: ["core_gene_tradeoffs--35113c1c", "conservation_fitness_synthesis--d4f23c67", "fitness_effects_conservation--6e6a4a45", "field_vs_lab_fitness--6def5903"]
conflicts: []
papers: ["29769716", "22761588", "37065130", "42262111"]
builds_on: ["findings/core_gene_tradeoffs--35113c1c", "findings/conservation_fitness_synthesis--d4f23c67", "findings/fitness_effects_conservation--6e6a4a45", "findings/field_vs_lab_fitness--6def5903"]
projects: ["conservation_fitness_synthesis", "core_gene_tradeoffs", "field_vs_lab_fitness", "fitness_effects_conservation"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Are costly-but-conserved genes kept by selection in natural conditions absent from laboratory assays?

Do genes that make mutants grow better in the lab yet stay conserved across a species' genomes carry benefits under field-like conditions that standard assays miss?

## Hypothesis

Costly-but-conserved genes show fitness defects under field-relevant or ecologically realistic conditions, or strong benefits in other conditions, at a higher rate than costly-and-dispensable genes.

## Why it matters

If true, laboratory 'burden' labels overstate real gene cost and purifying selection can be inferred from conservation. If false, much conservation is inertia or trade-off without a benefit we can identify.

## How to test it

In the Fitness Browser, classify genes as costly using a replicate-robust criterion rather than one positive-fitness experiment. Join them to core versus accessory status from the pangenome gene clusters. Compare costly-conserved and costly-dispensable genes for strong negative fitness in any other condition, with focus on Desulfovibrio vulgaris Hildenborough field-stress and metal conditions. Then test a few candidates in soil or host-like media.

## What would support or refute it

Support: costly-conserved genes are clearly more often important in some other or ecologically realistic condition than costly-dispensable genes. Refute: the two groups look alike, or costly-conserved genes show no benefit anywhere, pointing to noise or drift.

## Data

Approach: analysis then experiment. Readiness: needs compute. Fitness and pangenome tables are in the catalog; the robust burden classification and the cross-link must be computed, and ecological-condition tests need new assays.

## Builds on

- Finding: [[findings/core_gene_tradeoffs--35113c1c|Costly yet conserved genes suggest purifying selection despite metabolic cost]] (Candidate novel)
- Finding: [[findings/conservation_fitness_synthesis--d4f23c67|Core genes are more often burdens when deleted]] (Candidate novel)
- Finding: [[findings/fitness_effects_conservation--6e6a4a45|Core genes are more often beneficial to delete than auxiliary genes]] (Candidate novel)
- Finding: [[findings/field_vs_lab_fitness--6def5903|Fitness magnitude predicted conservation more than condition type in DvH]] (Candidate novel)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 22761588](https://pubmed.ncbi.nlm.nih.gov/22761588/) Selection-driven gene loss in bacteria.
- [PMID 37065130](https://pubmed.ncbi.nlm.nih.gov/37065130/) Large-scale genetic characterization of the model sulfate-reducing bacterium, Desulfovibrio vulgaris Hildenborough.
- [PMID 42262111](https://pubmed.ncbi.nlm.nih.gov/42262111/) Systemic trade-offs between core and accessory genomes govern stress adaptation in Rhodococcus erythropolis.

29769716 supplies the fitness data and 22761588 shows costly superfluous genes can be lost, but neither tests whether costly conserved genes have hidden benefits.
