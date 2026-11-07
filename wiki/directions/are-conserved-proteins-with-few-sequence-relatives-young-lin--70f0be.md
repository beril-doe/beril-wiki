---
type: "Research direction"
description: "Hundreds of thousands of core proteins have very few detectable relatives and are mostly unannotated. Are they young genes that became universal inside one lineage, or ancient proteins whose relatives are simply missing from databases?"
hypothesis: "Most shallow-depth core clusters are confined to one genus or family and are enriched for mobile-element annotations. Ancient, widely shared proteins with no structural relatives are the minority."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The shallow-depth core clusters and cross-clade cluster membership exist in the lakehouse, but the breadth counts and the comparison have not been run."
collections: ["kbase-ke-pangenome", "kbase-uniref"]
findings: ["alphafold_msa_annotation--b7b252bd", "alphafold_msa_annotation--f4d7e00d", "truly_dark_genes--947aec4f", "cog_analysis--7a21065f"]
conflicts: []
papers: ["21298028", "38977308", "41273079", "32124724"]
builds_on: ["findings/alphafold_msa_annotation--b7b252bd", "findings/alphafold_msa_annotation--f4d7e00d", "findings/truly_dark_genes--947aec4f", "findings/cog_analysis--7a21065f"]
projects: ["alphafold_msa_annotation", "cog_analysis", "truly_dark_genes"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Are conserved proteins with few sequence relatives young lineage-restricted genes, not ancient ones?

Hundreds of thousands of core proteins have very few detectable relatives and are mostly unannotated. Are they young genes that became universal inside one lineage, or ancient proteins whose relatives are simply missing from databases?

## Hypothesis

Most shallow-depth core clusters are confined to one genus or family and are enriched for mobile-element annotations. Ancient, widely shared proteins with no structural relatives are the minority.

## Why it matters

If the proteins are young and lineage-restricted, the apparent conserved-yet-novel paradox is lineage-specific gene birth, and these proteins are not a hidden universal core. Structural-genomics groups should then target them for lineage-specific biology. If they are widespread and ancient, they are deep unexplored protein families.

## How to test it

For the 415,603 core clusters with shallow alignment depth, use the Pangenome Collection and UniRef Clusters to count how many genera, families and phyla carry a matching cluster. Compare with deep-family core clusters. Compare the share carrying mobile-element annotation. Run it again with oversampled Pseudomonas and E. coli clades removed, to check that breadth is not a sampling effect.

## What would support or refute it

Support: most shallow clusters occur in a single genus or family and are enriched for mobile-element annotation, in balanced clades too. Refutation: a large share spans many families or phyla, or breadth matches deep-family clusters once oversampled clades are removed.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The shallow-depth core clusters and cross-clade cluster membership exist in the lakehouse, but the breadth counts and the comparison have not been run.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]

## Builds on

- Finding: [[findings/alphafold_msa_annotation--b7b252bd|Low-depth core clusters are mostly hypothetical and rarely EC- or KEGG-annotated]] (Insufficient literature evidence)
- Finding: [[findings/alphafold_msa_annotation--f4d7e00d|Core clusters have much deeper MSAs than accessory clusters]] (Insufficient literature evidence)
- Finding: [[findings/truly_dark_genes--947aec4f|Truly dark genes are shorter, more accessory, with narrower ortholog breadth]] (Candidate novel)
- Finding: [[findings/cog_analysis--7a21065f|Mobile elements dominate enrichment among novel genes across sampled species]] (Extends retrieved work)

## Closest published work

- [PMID 21298028](https://pubmed.ncbi.nlm.nih.gov/21298028/) Horizontal transfer, not duplication, drives the expansion of protein families in prokaryotes.
- [PMID 38977308](https://pubmed.ncbi.nlm.nih.gov/38977308/) Large-scale investigation of species-specific orphan genes in the human gut microbiome elucidates their evolutionary origins.
- [PMID 41273079](https://pubmed.ncbi.nlm.nih.gov/41273079/) AlphaFold Protein Structure Database 2025: a redesigned interface and updated structural coverage.
- [PMID 32124724](https://pubmed.ncbi.nlm.nih.gov/32124724/) An assessment of genome annotation coverage across the bacterial tree of life.

PMID 21298028 shows horizontal transfer drives protein-family expansion, and PMID 38977308 traces the origins of species-specific orphan genes in the gut. Neither asks whether genes that are core within species yet have shallow alignment depth are young lineage-restricted genes, and PMID 41273079 reports structure coverage without breadth.
