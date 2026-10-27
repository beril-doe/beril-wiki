---
type: "Research direction"
description: "Core gene clusters with very shallow AlphaFold MSA (multiple sequence alignment) depth, mostly hypothetical, are present in most genomes of a species clade. Do they carry measurable fitness or essentiality effects?"
hypothesis: "Among clusters bridged to Fitness Browser genes, core clusters with MSA depth < 10 are enriched for essential or strongly condition-dependent genes relative to higher-depth core clusters, and this persists after controlling for gene length and taxon."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "MSA depth, pangenome and fitness data are in the lakehouse, but the join was not run and member-level depth needs new computation."
collections: ["kbase-ke-pangenome", "kescience-fitnessbrowser", "kbase-uniref"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "alphafold_msa_annotation--0b782ee2", "alphafold_msa_annotation--3386d12a", "truly_dark_genes--92c362cf"]
conflicts: []
papers: ["41273079", "34791371", "32124724", "29769716"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/alphafold_msa_annotation--0b782ee2", "findings/alphafold_msa_annotation--3386d12a", "findings/truly_dark_genes--92c362cf"]
projects: ["alphafold_msa_annotation", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do conserved proteins with very shallow sequence families have measurable fitness phenotypes?

Core gene clusters with very shallow AlphaFold MSA (multiple sequence alignment) depth, mostly hypothetical, are present in most genomes of a species clade. Do they carry measurable fitness or essentiality effects?

## Hypothesis

Among clusters bridged to Fitness Browser genes, core clusters with MSA depth < 10 are enriched for essential or strongly condition-dependent genes relative to higher-depth core clusters, and this persists after controlling for gene length and taxon.

## Why it matters

The census holds 415,603 such clusters, of which 286,439 are hypothetical. Measurable phenotypes would mean a large conserved fraction is functionally active yet sparsely represented in sequence families, prioritizing it for structural and functional work.

## How to test it

Join the low-depth core clusters to Fitness Browser essentiality and |fitness| calls through pangenome links, and compare them with core clusters in higher MSA-depth bins (e.g. depth ≥ 10,000). Stratify by gene length, taxon and phylogenetically balanced samples, and use member-level rather than representative-only depth for a subset. Add ESMFold-based novelty as an axis not using MSA depth.

## What would support or refute it

Support: low-depth core clusters show higher essential or strong-fitness rates in stratified models. Refute: rates match higher-depth clusters after length and taxon control. The census excludes clusters lacking a non-UPI UniProt accession, so the conclusions cannot represent the unbridged population. Fitness effects would not by themselves show purifying selection or structural novelty.

## Data

Approach: lakehouse analysis. Readiness: needs compute. MSA depth, pangenome and fitness data are in the lakehouse, but the join was not run and member-level depth needs new computation.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--0b782ee2|EC and KEGG annotation almost absent among low-depth core proteins]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--3386d12a|Domain annotation richness rises steadily with MSA depth in core clusters]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--92c362cf|Reannotation resolves most dark genes, leaving small truly dark core]] (Insufficient literature evidence)

## Closest published work

- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 34791371](https://pubmed.ncbi.nlm.nih.gov/34791371/) AlphaFold Protein Structure Database: massively expanding the structural coverage of protein-sequence space with high-accuracy models.
- [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/) An assessment of genome annotation coverage across the bacterial tree of life.
- [PMID 29769716](https://pubmed.ncbi.nlm.nih.gov/29769716/) Mutant phenotypes for thousands of bacterial genes of unknown function.

PMID 41273079 and PMID 34791371 describe AlphaFold structural coverage and PMID 32124724 assesses annotation coverage, but none asks whether conserved proteins at shallow MSA depth have measurable fitness phenotypes.
