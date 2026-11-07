---
type: "Research direction"
description: "Plant-growth genes are mostly core and read as vertically inherited, yet other work finds them among the genes most strongly co-occurring with transposases. Do the two views describe different copies of the same genes?"
hypothesis: "Within a species, transposase-adjacent copies of ACC deaminase and nitrogen-fixation genes are the accessory minority, and core copies lack transposase neighbours."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Core status and gene positions exist, but contig-level neighbourhoods must be extracted."
collections: ["kbase-ke-pangenome"]
findings: ["pgp_pangenome_ecology--45e0cc45"]
conflicts: ["conflict--horizontal-gene-transfer-driven-innovation--9137941d", "conflict--two-speed-bacterial-genome--c03a2981"]
papers: ["24905353", "41724873", "31639358"]
builds_on: ["findings/pgp_pangenome_ecology--45e0cc45", "conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d", "conflicts/conflict--two-speed-bacterial-genome--c03a2981"]
projects: ["pgp_pangenome_ecology", "plant_microbiome_ecotypes"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do plant-growth gene copies near transposases form a separate mobile subpopulation?

Plant-growth genes are mostly core and read as vertically inherited, yet other work finds them among the genes most strongly co-occurring with transposases. Do the two views describe different copies of the same genes?

## Hypothesis

Within a species, transposase-adjacent copies of ACC deaminase and nitrogen-fixation genes are the accessory minority, and core copies lack transposase neighbours.

## Why it matters

It would show that plant-growth traits are both stable lineage features and occasionally mobile, which changes how inoculant traits are expected to spread.

## How to test it

For the plant-growth marker genes named in the two projects, use Pangenome Collection genome contigs to classify each cluster as core or accessory and record transposase neighbours within a fixed gene window. Compare the share of transposase-adjacent copies in each class, and compare singleton copies with others. Report nitrogen fixation under one gene definition, since the projects report very different core fractions for it.

## What would support or refute it

Support: transposase adjacency is rare among core copies and enriched among accessory or singleton copies. Refute: adjacency is equal across classes, or absent in accessory copies.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Core status and gene positions exist, but contig-level neighbourhoods must be extracted.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/pgp_pangenome_ecology--45e0cc45|Plant-growth genes are mostly core, rejecting the accessory/HGT hypothesis]] (Extends retrieved work)
- Conflict: [[conflicts/conflict--horizontal-gene-transfer-driven-innovation--9137941d|Plant-Growth-Promoting Traits: Vertically Inherited Core Genes or Transposase-Linked Mobile Cargo?]]
- Conflict: [[conflicts/conflict--two-speed-bacterial-genome--c03a2981|How Core Is Nitrogen Fixation? Conflicting Core-Genome Fractions Across Projects]]

## Closest published work

- [PMID 24905353](https://pubmed.ncbi.nlm.nih.gov/24905353/) New insights into 1-aminocyclopropane-1-carboxylate (ACC) deaminase phylogeny, evolution and ecological significance.
- [PMID 41724873](https://pubmed.ncbi.nlm.nih.gov/41724873/) Comparative genomic analyses reveal key traits for biocontrol and the promotion of plant growth in Paenibacillus strains.
- [PMID 31639358](https://pubmed.ncbi.nlm.nih.gov/31639358/) The Ecology and Evolution of Pangenomes.

PMID 24905353 reports mostly vertical inheritance of ACC deaminase with some transfer, and PMID 41724873 suggests transfer in mobile regions. Neither separates core copies from transposase-adjacent copies.
