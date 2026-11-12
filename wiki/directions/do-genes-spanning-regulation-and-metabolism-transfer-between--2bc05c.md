---
type: "Research direction"
description: "The complexity hypothesis predicts that genes with many interaction partners are hard to transfer. Yet gene families annotated to both regulatory and metabolic pathways show roughly twice the cross-clade exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) families. Do transferred copies of these genes arrive with a regulator next to them?"
hypothesis: "Transferred copies of mixed-category genes sit within a few genes of a regulator more often than vertically inherited copies of the same families, and this gap is absent for pure regulatory and pure metabolic families."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Gain events and annotations exist in the lakehouse, but neighbourhood adjacency per event must be computed."
collections: ["kbase-ke-pangenome", "kbase-uniref", "kbase-ontology-source"]
findings: ["gene_function_ecological_agora--e172b656", "gene_function_ecological_agora--c0bd8a1a", "gene_function_ecological_agora--4ca87c61"]
conflicts: []
papers: ["37232518", "10097118", "16077904", "37485539"]
builds_on: ["findings/gene_function_ecological_agora--e172b656", "findings/gene_function_ecological_agora--c0bd8a1a", "findings/gene_function_ecological_agora--4ca87c61"]
projects: ["gene_function_ecological_agora"]
topics: ["pangenome-structure-and-genome-evolution"]
---
# Do genes spanning regulation and metabolism transfer between clades with a regulator beside them?

The complexity hypothesis predicts that genes with many interaction partners are hard to transfer. Yet gene families annotated to both regulatory and metabolic pathways show roughly twice the cross-clade exchange rate (0.57%) of pure regulatory (0.27%) or pure metabolic (0.28%) families. Do transferred copies of these genes arrive with a regulator next to them?

## Hypothesis

Transferred copies of mixed-category genes sit within a few genes of a regulator more often than vertically inherited copies of the same families, and this gap is absent for pure regulatory and pure metabolic families.

## Why it matters

It would refine the complexity hypothesis by showing that self-contained regulated units can overcome integration limits. If transferred copies show no regulator adjacency, the mixed-category excess more likely reflects annotation breadth, since the group differences are small.

## How to test it

Using the gene-gain events from the gene-function atlas in the Pangenome Collection and UniRef Clusters, with regulator and pathway labels from Ontologies, count a regulator as present if a transcription factor or response regulator lies within five genes on the same contig. Compare regulator adjacency for transferred copies and vertical copies, for mixed, pure regulatory and pure metabolic families, with random genes from the same genomes as a null. To rule out annotation breadth, also compare mixed families against pure families matched on the number of pathway memberships. Photosystem II serves as a reference case.

## What would support or refute it

Support: transferred mixed-category copies are more often regulator-adjacent than vertical copies, pure families show no such gap, and the result holds after matching on pathway membership number. Refutation: adjacency is similar for transferred and vertical copies, or the mixed-category excess vanishes when families are matched on annotation breadth.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Gain events and annotations exist in the lakehouse, but neighbourhood adjacency per event must be computed.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/kbase-uniref|UniRef Clusters]]
- Collection: [[data/kbase-ontology-source|Ontologies]]

## Builds on

- Finding: [[findings/gene_function_ecological_agora--e172b656|Mixed regulatory-and-metabolic KOs show the highest Innovator-Exchange rate]] (Candidate novel)
- Finding: [[findings/gene_function_ecological_agora--c0bd8a1a|Function classes have distinct gene-acquisition depth profiles, CRISPR-Cas most recent-skewed]] (Insufficient literature evidence)
- Finding: [[findings/gene_function_ecological_agora--4ca87c61|Photosystem II innovation is exchange-type, but only at Cyanobacteriia class rank]] (Candidate novel)

## Closest published work

- [PMID 37232518](https://pubmed.ncbi.nlm.nih.gov/37232518/) Empirical Evidence That Complexity Limits Horizontal Gene Transfer.
- [PMID 10097118](https://pubmed.ncbi.nlm.nih.gov/10097118/) Horizontal gene transfer among genomes: the complexity hypothesis.
- [PMID 16077904](https://pubmed.ncbi.nlm.nih.gov/16077904/) Identification and categorization of horizontally transferred genes in prokaryotic genomes.
- [PMID 37485539](https://pubmed.ncbi.nlm.nih.gov/37485539/) Dissecting the HGT network of carbon metabolic genes in soil-borne microbiota.

PMID 37232518 and PMID 10097118 show complexity limits transfer, and PMID 16077904 and PMID 37485539 find regulatory and metabolic genes enriched among transferred genes. None examines genes annotated to both categories or tests whether a neighbouring regulator explains their transfer.
