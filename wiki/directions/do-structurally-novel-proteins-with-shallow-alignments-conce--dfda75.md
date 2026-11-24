---
type: "Research direction"
description: "Where do conserved core genes with very shallow alignment depth and mostly hypothetical annotation concentrate taxonomically, and does structure prediction give them function clues?"
hypothesis: "Core genes with shallow alignment depth are concentrated in a few under-sampled lineages, and their predicted structures match known folds more often than their sequence annotation does."
approach: "analysis then experiment"
readiness: "needs compute"
readiness_basis: "Tables are in the catalog, but Foldseek runs and the cluster-to-UniProt mapping require compute."
databases: ["kbase.ke_pangenome", "kescience.alphafold"]
tables: ["kescience.alphafold.alphafold_msa_depths", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gtdb_taxonomy_r214v1", "kbase.ke_pangenome.interproscan_domains"]
findings: ["alphafold_msa_annotation--0d54bd05", "alphafold_msa_annotation--164a1689", "alphafold_msa_annotation--6288b8d2"]
conflicts: []
papers: ["34599769", "34791371", "41273079", "41911251"]
builds_on: ["findings/alphafold_msa_annotation--0d54bd05", "findings/alphafold_msa_annotation--164a1689", "findings/alphafold_msa_annotation--6288b8d2"]
projects: ["alphafold_msa_annotation"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do structurally novel proteins with shallow alignments concentrate in specific lineages?

Where do conserved core genes with very shallow alignment depth and mostly hypothetical annotation concentrate taxonomically, and does structure prediction give them function clues?

## Hypothesis

Core genes with shallow alignment depth are concentrated in a few under-sampled lineages, and their predicted structures match known folds more often than their sequence annotation does.

## Why it matters

It would separate a sequence-database gap in particular lineages from truly new protein folds, and show where annotation effort pays off.

## How to test it

Join the AlphaFold alignment-depth table to pangenome gene clusters via UniProt links, select core clusters with shallow alignment depth and hypothetical Bakta calls, and map them onto GTDB taxonomy to test lineage enrichment against all core clusters. For a sample, run Foldseek against structure databases and check domain hits in InterProScan.

## What would support or refute it

Support: enrichment in a few lineages and frequent fold matches. Refute: even spread across lineages and no fold matches, implying novel folds or poor predictions.

## Data

Approach: analysis then experiment. Readiness: needs compute. Tables are in the catalog, but Foldseek runs and the cluster-to-UniProt mapping require compute.

## Builds on

- Finding: [[findings/alphafold_msa_annotation--0d54bd05|Core genes' lower hypothetical rate coexists with a structurally novel subset]] (Candidate novel)
- Finding: [[findings/alphafold_msa_annotation--164a1689|Core genes have much deeper MSAs than accessory genes]] (Candidate novel)
- Finding: [[findings/alphafold_msa_annotation--6288b8d2|MSA depth tracks domain annotation richness across bacterial clusters]] (Candidate novel)

## Closest published work

- [PMID 34599769](https://pubmed.ncbi.nlm.nih.gov/34599769/) Applying and improving AlphaFold at CASP14.
- [PMID 34791371](https://pubmed.ncbi.nlm.nih.gov/34791371/) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 41911251](https://pubmed.ncbi.nlm.nih.gov/41911251/) ECOD: Classification of domains in AFDB Swiss-Prot structure predictions.

The AlphaFold papers 34599769, 34791371 and 41273079 describe prediction and databases, not alignment depth by pangenome class or lineage.
