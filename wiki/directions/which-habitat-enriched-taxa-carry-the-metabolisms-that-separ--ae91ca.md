---
type: "Research direction"
description: "Do genera enriched in groundwater (Rhodanobacter, Gallionella, Sideroxydans) and in sediment (Anaeromyxobacter, Arcobacter, Ca. Methanoperedens) differ in denitrification, iron oxidation, iron reduction and methanotrophy gene content, as the taxonomy-based inference implies?"
hypothesis: "Groundwater-enriched genera carry denitrification and iron-oxidation genes while sediment-enriched genera carry iron-reduction and methane-oxidation genes, and the partition persists when both materials are sampled on the same date."
approach: "experiment"
readiness: "unknown"
readiness_basis: "The existing contrast is confounded with time by about 18 months, and the supplied evidence does not establish whether contemporaneous paired metagenomes exist."
collections: ["enigma-coral", "kbase-ke-pangenome"]
findings: ["enigma_sso_asv_ecology--51556105"]
conflicts: []
papers: ["22179233", "20305024", "22140175", "38391193"]
builds_on: ["findings/enigma_sso_asv_ecology--51556105"]
projects: ["enigma_sso_asv_ecology"]
topics: ["subsurface-and-soil-community-ecology"]
---
# Which habitat-enriched taxa carry the metabolisms that separate groundwater from sediment communities?

Do genera enriched in groundwater (Rhodanobacter, Gallionella, Sideroxydans) and in sediment (Anaeromyxobacter, Arcobacter, Ca. Methanoperedens) differ in denitrification, iron oxidation, iron reduction and methanotrophy gene content, as the taxonomy-based inference implies?

## Hypothesis

Groundwater-enriched genera carry denitrification and iron-oxidation genes while sediment-enriched genera carry iron-reduction and methane-oxidation genes, and the partition persists when both materials are sampled on the same date.

## Why it matters

It would turn a taxonomic contrast into a functional one and show whether the material contrast reflects genuine niche partitioning rather than the roughly 18-month sampling offset.

## How to test it

Run same-resolution shotgun metagenomics on groundwater and sediment from the same wells on the same date, if such paired data are not already available. Quantify denitrification, iron oxidation and reduction, sulfur oxidation and methanotrophy genes, and compare with 16S-derived assignments, including reads lacking genus-level classification. Also analyse the M6-C2 isolate genomes for fermentation and sulfate reduction.

## What would support or refute it

Support: gene-level abundances follow the taxonomic prediction and persist with contemporaneous sampling. Refutation: gene content does not differ between materials, or the contrast disappears when sampled at the same time.

## Data

Approach: experiment. Readiness: unknown. The existing contrast is confounded with time by about 18 months, and the supplied evidence does not establish whether contemporaneous paired metagenomes exist.

- Collection: [[data/enigma-coral|ENIGMA CORAL]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/enigma_sso_asv_ecology--51556105|Groundwater and sediment host distinct taxa within the same wells]] (Extends retrieved work)

## Closest published work

- [PMID 22179233](https://pubmed.ncbi.nlm.nih.gov/22179233/) Denitrifying bacteria from the genus Rhodanobacter dominate bacterial communities in the highly contaminated subsurface of a nuclear legacy waste site.
- [PMID 20305024](https://pubmed.ncbi.nlm.nih.gov/20305024/) Denitrifying bacteria isolated from terrestrial subsurface sediments exposed to mixed-waste contamination.
- [PMID 22140175](https://pubmed.ncbi.nlm.nih.gov/22140175/) Rhodanobacter denitrificans sp. nov., isolated from nitrate-rich zones of a contaminated aquifer.
- [PMID 38391193](https://pubmed.ncbi.nlm.nih.gov/38391193/) Metal-oxide precipitation influences microbiome structure in hyporheic zones receiving acid rock drainage.

PMID 22179233 shows Rhodanobacter dominating Oak Ridge groundwater and sediment, and PMID 38391193 links metal-oxide precipitation to community structure, but neither provides paired, same-date functional profiling of the two materials.
