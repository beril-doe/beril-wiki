---
type: "Research direction"
description: "Is the lack of relationship between module family breadth and core fraction a ceiling effect of a high core baseline, or does it show that conservation belongs to individual genes?"
hypothesis: "Within the subset of modules that have many accessory genes, family breadth still does not predict core fraction, so conservation is a gene property; modules with accessory members will instead show stronger co-inheritance than core modules."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Module assignments and pangenome flags exist per the findings, but the catalog did not show module tables, so they may need to be regenerated."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.ortholog", "kescience.fitnessbrowser.cofit", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.pangenome"]
findings: ["module_conservation--3c784bf6", "module_conservation--ef29c9c3", "module_conservation--ba3f89b5", "cofitness_coinheritance--92f9f732"]
conflicts: ["conflict--conservation-of-cofitness-modules-across-genomes-and-organisms--daff4d3a"]
papers: ["29545622", "25483351", "34499026", "32100706", "29769716"]
builds_on: ["findings/module_conservation--3c784bf6", "findings/module_conservation--ef29c9c3", "findings/module_conservation--ba3f89b5", "findings/cofitness_coinheritance--92f9f732", "conflicts/conflict--conservation-of-cofitness-modules-across-genomes-and-organisms--daff4d3a"]
projects: ["cofitness_coinheritance", "conservation_fitness_synthesis", "fitness_modules", "module_conservation"]
topics: ["gene-fitness-landscapes-and-cofitness-modules"]
---
# Why do cofitness modules show no link between cross-organism breadth and conservation?

Is the lack of relationship between module family breadth and core fraction a ceiling effect of a high core baseline, or does it show that conservation belongs to individual genes?

## Hypothesis

Within the subset of modules that have many accessory genes, family breadth still does not predict core fraction, so conservation is a gene property; modules with accessory members will instead show stronger co-inheritance than core modules.

## Why it matters

If true, shared regulation across organisms does not constrain gene retention, and module conservation cannot be used to infer which gene sets are selected together. If a gradient appears, module scope matters.

## How to test it

Using Fitness Browser ICA module families and ortholog tables, restrict to modules with a substantial accessory share. Test breadth against core fraction using pangenome core flags, and compare against a null that preserves each organism's core baseline. Then relate module co-inheritance across genomes to accessory fraction.

## What would support or refute it

Support: no breadth-core gradient in the restricted set, and co-inheritance tracks accessory fraction. Refute: a clear positive gradient emerges once the ceiling is removed.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Module assignments and pangenome flags exist per the findings, but the catalog did not show module tables, so they may need to be regenerated.

## Builds on

- Finding: [[findings/module_conservation--3c784bf6|Conservation appears to be a gene property, not module scope]] (Candidate novel)
- Finding: [[findings/module_conservation--ef29c9c3|Family breadth does not predict core fraction]] (Candidate novel)
- Finding: [[findings/module_conservation--ba3f89b5|Fitness modules are enriched in core genes]] (Candidate novel)
- Finding: [[findings/cofitness_coinheritance--92f9f732|Multi-gene ICA modules show stronger co-inheritance than pairwise co-fitness]] (Candidate novel)
- Conflict: [[conflicts/conflict--conservation-of-cofitness-modules-across-genomes-and-organisms--daff4d3a|Core-Enriched Cofitness Modules Versus Accessory-Module Co-inheritance: A Tension]]

## Closest published work

- [PMID 29545622](https://pubmed.ncbi.nlm.nih.gov/29545622/) A comprehensive evaluation of module detection methods for gene expression data.
- [PMID 25483351](https://pubmed.ncbi.nlm.nih.gov/25483351/) Ten years of pan-genome analyses.
- [PMID 34499026](https://pubmed.ncbi.nlm.nih.gov/34499026/) Gene-gene relationships in an Escherichia coli accessory genome are linked to function and mobility.
- [PMID 32100706](https://pubmed.ncbi.nlm.nih.gov/32100706/) Coinfinder: detecting significant associations and dissociations in pangenomes.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

Pangenome co-occurrence papers (34499026, 32100706) and module detection work (29545622) do not test breadth against core fraction; this direction removes the ceiling effect.
