---
type: "Research direction"
description: "Genes with condition-specific phenotypes are more often core than accessory, contrary to the idea that condition-specific means niche-specific. Is that because the conditions that would reveal accessory genes' functions are missing from laboratory panels?"
hypothesis: "Accessory genes whose annotation names a specific substrate or stress show phenotypes as often as core genes when that condition was tested. Their apparent neutrality comes from conditions never offered."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Experiment, annotation, specific-phenotype and cluster tables are in the catalog. The core-status link and the substrate mapping must be built, and the follow-up screens need new measurements."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.experiment", "kescience.fitnessbrowser.seedannotation", "kescience.fitnessbrowser.specog", "kescience.fitnessbrowser.gene", "kbase.ke_pangenome.gene_cluster"]
findings: ["fitness_effects_conservation--ae67b7f2", "fitness_effects_conservation--e931cad7", "conservation_fitness_synthesis--0c074210"]
conflicts: []
papers: ["29769716", "38948139", "21592774"]
builds_on: ["findings/fitness_effects_conservation--ae67b7f2", "findings/fitness_effects_conservation--e931cad7", "findings/conservation_fitness_synthesis--0c074210"]
projects: ["conservation_fitness_synthesis", "fitness_effects_conservation"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Do accessory genes look condition-neutral because labs never offer their substrate?

Genes with condition-specific phenotypes are more often core than accessory, contrary to the idea that condition-specific means niche-specific. Is that because the conditions that would reveal accessory genes' functions are missing from laboratory panels?

## Hypothesis

Accessory genes whose annotation names a specific substrate or stress show phenotypes as often as core genes when that condition was tested. Their apparent neutrality comes from conditions never offered.

## Why it matters

If true, the core enrichment is a sampling artifact of the laboratory panel, and accessory genes are as condition-dependent as core genes. It would also give a way to choose conditions that expose unmeasured accessory function.

## How to test it

Annotate genes in the transposon-mutant fitness collection with the substrate or stress implied by their SEED role or domain. For each organism, check from the experiment table whether that condition was tested. Link genes to core or accessory status through the pangenome gene clusters. Compare phenotype rates for core and accessory genes separately for tested and untested cognate conditions, using the specific-phenotype table. For organisms with many untested cases, run new fitness screens adding the missing substrates and ask whether previously neutral accessory genes gain phenotypes.

## What would support or refute it

Support: accessory genes with a tested cognate condition show phenotypes at core-like rates, and new screens reveal phenotypes for many untested ones. Refute: accessory genes stay neutral even under their predicted substrate, so they are inert in the laboratory.

## Data

Approach: analysis then experiment. Readiness: needs compute. Experiment, annotation, specific-phenotype and cluster tables are in the catalog. The core-status link and the substrate mapping must be built, and the follow-up screens need new measurements.

## Builds on

- Finding: [[findings/fitness_effects_conservation--ae67b7f2|Condition-specific phenotype genes are enriched in the core genome]] (Candidate novel)
- Finding: [[findings/fitness_effects_conservation--e931cad7|Neutral-overall, condition-critical genes are commoner among core genes]] (Insufficient literature evidence)
- Finding: [[findings/conservation_fitness_synthesis--0c074210|Condition-specific fitness effects do not imply accessory status]] (Insufficient literature evidence)

## Closest published work

- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 21592774](https://pubmed.ncbi.nlm.nih.gov/21592774/) Gene dispensability.

PMID 29769716 reports condition-specific phenotypes for poorly annotated genes, and PMID 38948139 finds fitness genes enriched in core genes. Neither tests whether missing matching conditions explain accessory genes' apparent neutrality.
