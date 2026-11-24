---
type: "Research direction"
description: "If horizontal gene transfer were ecologically directed, accessory genes should be shared more among strains from the same environment. Is that so in species that differ in openness?"
hypothesis: "Accessory genes are shared among same-environment strains only about as much as chance predicts after accounting for phylogeny, in both open and closed pangenomes, consistent with opportunistic transfer."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Pangenome summary tables, gene clusters and tree distances are in the catalog, but the gene-by-genome matrices and the permutation tests would need to be built."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.pangenome", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.ncbi_env", "kbase.ke_pangenome.phylogenetic_tree_distance_pairs", "kbase.ke_pangenome.bakta_pfam_domains"]
findings: ["pangenome_openness--d3aacb68", "pangenome_openness--0e2125d9", "pangenome_openness--737ca282", "ecotype_analysis--9366534f"]
conflicts: ["conflict--environmental-versus-phylogenetic-drivers-of-gene-content--3f19e23b"]
papers: ["23332119", "38743630", "25311532", "33423895"]
builds_on: ["findings/pangenome_openness--d3aacb68", "findings/pangenome_openness--0e2125d9", "findings/pangenome_openness--737ca282", "findings/ecotype_analysis--9366534f", "conflicts/conflict--environmental-versus-phylogenetic-drivers-of-gene-content--3f19e23b"]
projects: ["ecotype_analysis", "ecotype_env_reanalysis", "env_embedding_explorer", "pangenome_openness"]
topics: ["ecotypes-and-environmental-gene-content-differentiation"]
---
# Is pangenome openness unrelated to environment because gene exchange is opportunistic rather than directed?

If horizontal gene transfer were ecologically directed, accessory genes should be shared more among strains from the same environment. Is that so in species that differ in openness?

## Hypothesis

Accessory genes are shared among same-environment strains only about as much as chance predicts after accounting for phylogeny, in both open and closed pangenomes, consistent with opportunistic transfer.

## Why it matters

Openness did not track either the environment effect or the phylogeny effect across species. That is compatible with opportunistic transfer, but the species-level summary may hide gene-level structure. A gene-level test would separate the two explanations.

## How to test it

Choose species with ecotype results spanning low to high openness. Within each, test whether pairwise accessory-gene-content similarity rises with shared isolation environment beyond what tree distance predicts. Use a permutation that shuffles environment labels within ANI clusters. Then ask whether the genes driving any signal are enriched in particular functional categories (COG, Pfam). Compare the size of the signal with openness.

## What would support or refute it

Support: same-environment sharing is near the permutation null in species at all openness levels. Refute: a subset of species, or of gene categories, shows clear same-environment sharing that is independent of phylogeny. Refuting would imply that the null cross-species result hid directed transfer in some genes.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Pangenome summary tables, gene clusters and tree distances are in the catalog, but the gene-by-genome matrices and the permutation tests would need to be built.

## Builds on

- Finding: [[findings/pangenome_openness--d3aacb68|Uncorrelated openness suggests opportunistic rather than ecologically directed gene transfer]] (Candidate novel)
- Finding: [[findings/pangenome_openness--0e2125d9|Pangenome openness does not correlate with environment effect]] (Candidate novel)
- Finding: [[findings/pangenome_openness--737ca282|Pangenome openness does not correlate with phylogeny effect]] (Candidate novel)
- Finding: [[findings/ecotype_analysis--9366534f|Most species show no significant environment effect on gene content]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--environmental-versus-phylogenetic-drivers-of-gene-content--3f19e23b|Weak Environment Signal Versus Strong Niche-Breadth Signal in Gene Content]]

## Closest published work

- [PMID 23332119](https://pubmed.ncbi.nlm.nih.gov/23332119/) Horizontal gene transfer and the evolution of bacterial and archaeal population structure.
- [PMID 38743630](https://pubmed.ncbi.nlm.nih.gov/38743630/) Bacterial lifestyle shapes pangenomes.
- [PMID 25311532](https://pubmed.ncbi.nlm.nih.gov/25311532/) Genomics of Streptococcus salivarius, a major human commensal.
- [PMID 33423895](https://pubmed.ncbi.nlm.nih.gov/33423895/) Mechanisms That Shape Microbial Pangenomes.

PMID 23332119 shows habitat structuring of gene transfer and PMID 25311532 found no niche-specific genomic features in one species; this direction tests directed versus opportunistic exchange across species of differing openness.
