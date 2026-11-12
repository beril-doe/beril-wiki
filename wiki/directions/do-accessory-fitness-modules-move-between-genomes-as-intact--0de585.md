---
type: "Research direction"
description: "Some co-regulated fitness modules are made mostly of accessory genes. Are these modules physically clustered operons that are gained and lost together, as horizontally transferred units would be, or are they niche-specific modules that simply sit in variable parts of the genome?"
hypothesis: "Members of accessory-dominated modules lie close together on the chromosome and are present or absent together across genomes of a species far more than members of core modules."
approach: "lakehouse analysis"
readiness: "unknown"
readiness_basis: "Gene coordinates, cluster and genome tables are listed; the module membership lists come from the project's own outputs and the gene-to-cluster membership table was not among the catalog-matched tables."
databases: ["kbase.ke_pangenome", "kescience.fitnessbrowser"]
tables: ["kescience.fitnessbrowser.gene", "kescience.fitnessbrowser.seedannotation", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome"]
findings: ["module_conservation--d13bfcb2", "module_conservation--b36fddee", "module_conservation--ef29c9c3"]
conflicts: []
papers: ["42262111", "38948139", "29545622"]
builds_on: ["findings/module_conservation--d13bfcb2", "findings/module_conservation--b36fddee", "findings/module_conservation--ef29c9c3"]
projects: ["module_conservation"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Do accessory fitness modules move between genomes as intact transferable units?

Some co-regulated fitness modules are made mostly of accessory genes. Are these modules physically clustered operons that are gained and lost together, as horizontally transferred units would be, or are they niche-specific modules that simply sit in variable parts of the genome?

## Hypothesis

Members of accessory-dominated modules lie close together on the chromosome and are present or absent together across genomes of a species far more than members of core modules.

## Why it matters

Support would show that horizontal transfer of whole functional units, not single genes, shapes the variable genome. Refutation would send attention to niche-specific regulation of scattered genes.

## How to test it

Take modules with under half core genes and core-dominated modules from the Fitness Browser organisms with pangenome links. For each module, measure the chromosomal span of its members from gene coordinates, and measure how often members co-occur across the species' genomes using the pangenome cluster and genome tables together with the table linking genes to clusters. Check whether members have mobile-element annotations. Compare accessory with core modules, controlling for module size.

## What would support or refute it

Support: accessory modules are more compact and show stronger joint presence and absence across genomes than core modules, often with mobile-element neighbours. Refute: they are as dispersed and as independently distributed as core modules.

## Data

Approach: lakehouse analysis. Readiness: unknown. Gene coordinates, cluster and genome tables are listed; the module membership lists come from the project's own outputs and the gene-to-cluster membership table was not among the catalog-matched tables.

## Builds on

- Finding: [[findings/module_conservation--d13bfcb2|Some module families are accessory-dominated, possibly mobile or niche-specific]] (Insufficient literature evidence)
- Finding: [[findings/module_conservation--b36fddee|Most fitness modules are composed almost entirely of core genes]] (Insufficient literature evidence)
- Finding: [[findings/module_conservation--ef29c9c3|Module family breadth does not predict core fraction]] (Insufficient literature evidence)

## Closest published work

- [PMID 42262111](https://pubmed.ncbi.nlm.nih.gov/42262111/) Systemic trade-offs between core and accessory genomes govern stress adaptation in Rhodococcus erythropolis.
- [PMID 38948139](https://pubmed.ncbi.nlm.nih.gov/38948139/) Cofitness network connectivity determines a fuzzy essential zone in open bacterial pangenome.
- [PMID 29545622](https://pubmed.ncbi.nlm.nih.gov/29545622/) A comprehensive evaluation of module detection methods for gene expression data.

PMIDs 38948139 and 42262111 report core enrichment of fitness genes and co-expression modules in single species. Neither asks whether accessory modules are physically and evolutionarily coherent units.
