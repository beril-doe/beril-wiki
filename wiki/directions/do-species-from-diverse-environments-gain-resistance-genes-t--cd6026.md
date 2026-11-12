---
type: "Research direction"
description: "Species from more varied environments carry more resistance genes, and a smaller share of them are core. Is this because such species acquire resistance by horizontal transfer, or just because they have been sampled more heavily?"
hypothesis: "In species from diverse environments, accessory resistance genes sit next to mobile-element genes more often than in narrow-niche species with matched genome counts. Heavy sampling alone would not produce this difference."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Resistance calls, annotations and embeddings are in the catalog; neighbour assignment must be derived and may be incomplete in fragmented assemblies, and embeddings cover only part of the genomes."
databases: ["kbase.ke_pangenome"]
tables: ["kbase.ke_pangenome.bakta_amr", "kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gene_cluster", "kbase.ke_pangenome.alphaearth_embeddings_all_years"]
findings: ["amr_pangenome_atlas--b878500b", "amr_pangenome_atlas--1e435872"]
conflicts: []
papers: ["36882798", "38039820", "38457973", "35873140"]
builds_on: ["findings/amr_pangenome_atlas--b878500b", "findings/amr_pangenome_atlas--1e435872"]
projects: ["amr_pangenome_atlas"]
topics: ["laboratory-fitness-versus-natural-selection-and-gene-conservation"]
---
# Do species from diverse environments gain resistance genes through mobile elements?

Species from more varied environments carry more resistance genes, and a smaller share of them are core. Is this because such species acquire resistance by horizontal transfer, or just because they have been sampled more heavily?

## Hypothesis

In species from diverse environments, accessory resistance genes sit next to mobile-element genes more often than in narrow-niche species with matched genome counts. Heavy sampling alone would not produce this difference.

## Why it matters

It would point to horizontal transfer as the route by which environmental breadth accumulates resistance, which affects where surveillance should focus. If not, the correlation is a sampling artefact.

## How to test it

Take species with at least 3 genomes and environmental embeddings. Only 28% of genomes have these embeddings, and they are biased toward genomes with geographic metadata, so first compare the embedded subset with the rest on taxonomy and genome count, and repeat the main comparison within phyla to limit that bias. Use the contig-and-index structure of resistance gene cluster identifiers to find neighbouring genes, and score neighbours for transposase, integrase and phage annotations. Compare the share of mobile-flanked accessory resistance genes between high- and low-diversity species, stratified by genome count and phylum, and test the same in matched non-resistance accessory genes as a control.

## What would support or refute it

Support: mobile flanking of accessory resistance genes rises with environmental diversity after stratifying, and exceeds the control genes. Refute: flanking is similar across diversity levels, or rises equally for control genes. A result seen only in the metadata-rich subset would be treated as inconclusive for the wider collection.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Resistance calls, annotations and embeddings are in the catalog; neighbour assignment must be derived and may be incomplete in fragmented assemblies, and embeddings cover only part of the genomes.

## Builds on

- Finding: [[findings/amr_pangenome_atlas--b878500b|Species from more diverse environments carry more, less-core AMR genes]] (Insufficient literature evidence)
- Finding: [[findings/amr_pangenome_atlas--1e435872|AMR clusters are depleted from core and enriched in auxiliary genomes]] (Extends retrieved work)

## Closest published work

- [PMID 36882798](https://pubmed.ncbi.nlm.nih.gov/36882798/) Latent antibiotic resistance genes are abundant, diverse, and mobile in human, animal, and environmental microbiomes.
- [PMID 38039820](https://pubmed.ncbi.nlm.nih.gov/38039820/) Rare resistome rather than core resistome exhibited higher diversity and risk along the Yangtze River.
- [PMID 38457973](https://pubmed.ncbi.nlm.nih.gov/38457973/) Environmental drivers impact the accumulation and diversity of antibiotic resistance in green stormwater infrastructure.
- [PMID 35873140](https://pubmed.ncbi.nlm.nih.gov/35873140/) Comparative Genomic Analysis of the Human Pathogen Wohlfahrtiimonas Chitiniclastica Provides Insight Into the Identification of Antimicrobial Resistance Genotypes and Potential Virulence Traits.

PMID 36882798 shows latent resistance genes are mobile across microbiomes, and PMID 38457973 links environmental drivers to resistance accumulation; neither tests mobile context across species in relation to environmental diversity.
