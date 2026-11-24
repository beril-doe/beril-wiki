---
type: "Research direction"
description: "Are co-regulated multi-gene modules inherited together across strains more strongly than co-fit gene pairs, and is the effect concentrated in accessory modules?"
hypothesis: "Modules from independent component analysis (ICA) that are mostly accessory genes show stronger co-inheritance than matched random gene sets and than co-fit pairs, even after accounting for how common each gene is across genomes."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Source tables are in the catalog, but per-organism presence-matrix extraction on Spark was slow and limited the earlier sample."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.cofit", "kescience.fitnessbrowser.gene", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome"]
findings: ["cofitness_coinheritance--92f9f732", "cofitness_coinheritance--9ed1fa6e", "cofitness_coinheritance--12d090b9"]
conflicts: []
papers: ["34499026", "32100706", "40304385", "29769716"]
builds_on: ["findings/cofitness_coinheritance--92f9f732", "findings/cofitness_coinheritance--9ed1fa6e", "findings/cofitness_coinheritance--12d090b9"]
projects: ["cofitness_coinheritance"]
topics: ["distributed-computation-and-analysis-execution"]
---
# Do multi-gene regulatory modules, rather than co-fit pairs, mark the units that selection keeps together across genomes?

Are co-regulated multi-gene modules inherited together across strains more strongly than co-fit gene pairs, and is the effect concentrated in accessory modules?

## Hypothesis

Modules from independent component analysis (ICA) that are mostly accessory genes show stronger co-inheritance than matched random gene sets and than co-fit pairs, even after accounting for how common each gene is across genomes.

## Why it matters

If true, the selective units behind gene-content evolution are modules, not pairs, and lab fitness data could be used to predict which genes travel together in pangenomes.

## How to test it

For the Fitness Browser organisms with module and co-fitness data (for example Btheta and Korea), map genes to pangenome clusters. Compute co-inheritance for modules, co-fit pairs and prevalence-matched random sets. Stratify by core fraction, and restrict to accessory modules and species with enough accessory variation.

## What would support or refute it

Support: accessory modules beat prevalence-matched random sets and beat pairs in most organisms. Refute: the advantage disappears once prevalence is matched, which would mean the signal is a prevalence artefact.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Source tables are in the catalog, but per-organism presence-matrix extraction on Spark was slow and limited the earlier sample.

## Builds on

- Finding: [[findings/cofitness_coinheritance--92f9f732|Multi-gene ICA modules show stronger co-inheritance than pairwise co-fitness]] (Candidate novel)
- Finding: [[findings/cofitness_coinheritance--9ed1fa6e|Accessory ICA modules show the strongest co-inheritance]] (Insufficient literature evidence)
- Finding: [[findings/cofitness_coinheritance--12d090b9|Across-organism test of co-fitness effect is not significant]] (Insufficient literature evidence)

## Closest published work

- [PMID 34499026](https://pubmed.ncbi.nlm.nih.gov/34499026/) Gene-gene relationships in an Escherichia coli accessory genome are linked to function and mobility.
- [PMID 32100706](https://pubmed.ncbi.nlm.nih.gov/32100706/) Coinfinder: detecting significant associations and dissociations in pangenomes.
- [PMID 40304385](https://pubmed.ncbi.nlm.nih.gov/40304385/) Heterogeneity in recombination rates and accessory gene co-occurrence distinguish Pseudomonas aeruginosa phylogroups.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

Earlier pangenome co-occurrence work (34499026, 32100706, 40304385) tests gene pairs; this tests whether co-regulated modules with a prevalence control are the unit of co-inheritance.
