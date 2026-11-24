---
type: "Research direction"
description: "Do adaptive functional categories still differentiate gene-content ecotypes more than housekeeping categories once population structure from the core genome is accounted for?"
hypothesis: "After conditioning on core-genome phylogenetic distance, adaptive COG categories (defense, unknown function, mobile elements) still differ between ecotypes by more than housekeeping categories do, though the gap shrinks."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Tree distances and annotations are in the catalog, but the earlier sample was limited by Spark cluster load."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.phylogenetic_tree_distance_pairs", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.eggnog_mapper_annotations", "kbase.ke_pangenome.ncbi_env"]
findings: ["ecotype_functional_differentiation--3b6894d0", "ecotype_functional_differentiation--4eb80979", "ecotype_functional_differentiation--7b08ff2a"]
conflicts: []
papers: ["31611653", "31615877", "33423895", "24451205"]
builds_on: ["findings/ecotype_functional_differentiation--3b6894d0", "findings/ecotype_functional_differentiation--4eb80979", "findings/ecotype_functional_differentiation--7b08ff2a"]
projects: ["ecotype_functional_differentiation"]
topics: ["distributed-computation-and-analysis-execution"]
---
# Does gene-content ecotype differentiation survive control for within-species phylogeny in adaptive categories?

Do adaptive functional categories still differentiate gene-content ecotypes more than housekeeping categories once population structure from the core genome is accounted for?

## Hypothesis

After conditioning on core-genome phylogenetic distance, adaptive COG categories (defense, unknown function, mobile elements) still differ between ecotypes by more than housekeeping categories do, though the gap shrinks.

## Why it matters

It would separate ecological adaptation from demographic substructure and show whether annotation gaps hide niche genes.

## How to test it

For the 12 analysed species, use pairwise tree distances between genomes. Permute ecotype labels within phylogenetic clusters and recompute the size of each category's difference between ecotypes. Compare adaptive versus housekeeping categories with and without control. Add habitat metadata from the environment tables where present.

## What would support or refute it

Support: adaptive categories keep a larger difference after control. Refute: the difference falls to the housekeeping level, which would point to demographic structure.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Tree distances and annotations are in the catalog, but the earlier sample was limited by Spark cluster load.

## Builds on

- Finding: [[findings/ecotype_functional_differentiation--3b6894d0|Adaptive COG categories differentiate ecotypes with larger effect sizes than housekeeping categories]] (Candidate novel)
- Finding: [[findings/ecotype_functional_differentiation--4eb80979|Every analysed species shows non-random functional differentiation between gene-content ecotypes]] (Extends retrieved work)
- Finding: [[findings/ecotype_functional_differentiation--7b08ff2a|Defense category V differentiates ecotypes in most species]] (Insufficient literature evidence)

## Closest published work

- [PMID 31611653](https://pubmed.ncbi.nlm.nih.gov/31611653/) Global ecotypes in the ubiquitous marine clade SAR86.
- [PMID 31615877](https://pubmed.ncbi.nlm.nih.gov/31615877/) Genomic Variations Underlying Speciation and Niche Specialization of Shewanella baltica.
- [PMID 33423895](https://pubmed.ncbi.nlm.nih.gov/33423895/) Mechanisms That Shape Microbial Pangenomes.
- [PMID 24451205](https://pubmed.ncbi.nlm.nih.gov/24451205/) Single-cell enabled comparative genomics of a deep ocean SAR11 bathytype.

Single-taxon ecotype studies (31611653, 31615877) show non-random gene content; this tests a multi-species adaptive-versus-housekeeping contrast with phylogenetic control.
