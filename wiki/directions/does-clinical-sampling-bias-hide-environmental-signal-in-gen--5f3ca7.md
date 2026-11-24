---
type: "Research direction"
description: "Does excluding clinical and human-associated genomes strengthen the relationship between environmental embeddings and gene content?"
hypothesis: "Removing clinical and human-associated genomes raises the environment effect on gene content above the very small median seen across species."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Embedding, environment and tree tables are in the catalog; coverage of genomes is partial."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.alphaearth_embeddings_all_years", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.phylogenetic_tree_distance_pairs"]
findings: ["env_embedding_explorer--2b7f8fd1", "env_embedding_explorer--43490c25", "ecotype_analysis--3c51caf0", "ecotype_analysis--9366534f"]
conflicts: []
papers: ["37804485", "37189129", "33175127"]
builds_on: ["findings/env_embedding_explorer--2b7f8fd1", "findings/env_embedding_explorer--43490c25", "findings/ecotype_analysis--3c51caf0", "findings/ecotype_analysis--9366534f"]
projects: ["ecotype_analysis", "env_embedding_explorer"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Does clinical sampling bias hide environmental signal in gene content?

Does excluding clinical and human-associated genomes strengthen the relationship between environmental embeddings and gene content?

## Hypothesis

Removing clinical and human-associated genomes raises the environment effect on gene content above the very small median seen across species.

## Why it matters

If true, weak environment effects reflect a biased genome sample, and environment-based inference should be restricted to environmental isolates.

## How to test it

In species with satellite embeddings, compare environment versus phylogeny effects on gene content for all genomes and for non-clinical genomes, using habitat classes from NCBI environment attributes and tree distances.

## What would support or refute it

Support: the environment effect and share of species with detectable effects rise after exclusion. Refute: results stay near zero.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Embedding, environment and tree tables are in the catalog; coverage of genomes is partial.

## Builds on

- Finding: [[findings/env_embedding_explorer--2b7f8fd1|Clinical bias may explain weak environment–gene content signal]] (Insufficient literature evidence)
- Finding: [[findings/env_embedding_explorer--43490c25|Human-associated genomes show a flatter embedding distance gradient]] (Candidate novel)
- Finding: [[findings/ecotype_analysis--3c51caf0|Median environment partial correlation is very small across species]] (Insufficient literature evidence)
- Finding: [[findings/ecotype_analysis--9366534f|Most species show no significant environment effect on gene content]] (Insufficient literature evidence)

## Closest published work

- [PMID 37804485](https://pubmed.ncbi.nlm.nih.gov/37804485/) Macroalgal microbiome biogeography is shaped by environmental drivers rather than geographical distance.
- [PMID 37189129](https://pubmed.ncbi.nlm.nih.gov/37189129/) Geography, not lifestyle, explains the population structure of free-living and host-associated deep-sea hydrothermal vent snail symbionts.
- [PMID 33175127](https://pubmed.ncbi.nlm.nih.gov/33175127/) Divergence in environmental adaptation between terrestrial clades of the Bacillus cereus group.

37189129 finds geography rather than lifestyle structures symbiont populations, but not with embedding-based environment effects.
