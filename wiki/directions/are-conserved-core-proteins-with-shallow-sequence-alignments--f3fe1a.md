---
type: "Research direction"
description: "Hundreds of thousands of core gene clusters have very shallow multiple-sequence-alignment depth (few related sequences found when AlphaFold's alignments were built), and most are hypothetical. Does shallowness mean recent, lineage-restricted origin, or ancient families that diverged beyond recognition?"
hypothesis: "Most shallow-alignment core clusters are restricted to a single genus or family, which points to recent origin. Shallow clusters with relatives spread across many phyla are a minority."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Cluster, annotation, taxonomy and alignment-depth tables are in the catalog but are very large; the cross-clade family counts and the balanced sampling have to be computed."
databases: ["kbase.ke_pangenome", "kescience.alphafold", "kescience.fitnessbrowser"]
tables: ["kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.genome", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kescience.alphafold.alphafold_msa_depths"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "alphafold_msa_annotation--0b782ee2"]
conflicts: []
papers: ["41273079", "34791371", "37821698", "32124724"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/alphafold_msa_annotation--0b782ee2"]
projects: ["alphafold_msa_annotation"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Are conserved core proteins with shallow sequence alignments young lineage inventions or ancient divergent families?

Hundreds of thousands of core gene clusters have very shallow multiple-sequence-alignment depth (few related sequences found when AlphaFold's alignments were built), and most are hypothetical. Does shallowness mean recent, lineage-restricted origin, or ancient families that diverged beyond recognition?

## Hypothesis

Most shallow-alignment core clusters are restricted to a single genus or family, which points to recent origin. Shallow clusters with relatives spread across many phyla are a minority.

## Why it matters

The two readings predict different work. Lineage-restricted proteins call for ecology and de novo gene-origin studies. Divergent ancient families call for structure-based function recovery.

## How to test it

Take core clusters whose representative sequence has a very shallow alignment depth. For each, use protein-family identifiers from the annotation tables to count how many species clades and phyla hold a related cluster. Compare against core clusters with deep alignments and against accessory clusters, matched for protein length. The genome collection is not phylogenetically balanced (Pseudomonas and E. coli are over-represented), so repeat the comparison on a sample balanced across genera and phyla, and judge lineage restriction only on counts that survive it. Alignment depth was looked up for the representative sequence only, so also check a few members per cluster. Finally, ask whether clusters confined to one lineage are the ones with essential or condition-specific phenotypes in the transposon-fitness compendium.

## What would support or refute it

Support: the large majority of shallow core clusters are confined to one genus or family, far more than the matched deep clusters, and this persists in the balanced sample. Refute: most have relatives across many phyla, which favors divergence over recent origin, or the confinement disappears once sampling is balanced.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Cluster, annotation, taxonomy and alignment-depth tables are in the catalog but are very large; the cross-clade family counts and the balanced sampling have to be computed.

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--0b782ee2|EC and KEGG annotation almost absent among low-depth core proteins]] (Insufficient literature evidence)

## Closest published work

- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 34791371](https://pubmed.ncbi.nlm.nih.gov/34791371/) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- [PMID 37821698](https://pubmed.ncbi.nlm.nih.gov/37821698/) Unraveling the functional dark matter through global metagenomics.
- [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/) An assessment of genome annotation coverage across the bacterial tree of life.

PMID 41273079 and PMID 34791371 describe structure-database coverage, and PMID 37821698 surveys functional dark matter in metagenomes. None asks whether conserved low-depth proteins are lineage-restricted or ancient.
