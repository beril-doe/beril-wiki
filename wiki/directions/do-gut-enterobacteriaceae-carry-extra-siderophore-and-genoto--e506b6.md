---
type: "Research direction"
description: "Do gut-associated Enterobacteriaceae carry more iron-siderophore and genotoxin clusters than their non-gut relatives, or does the enrichment among the Crohn's targets come from lineage alone?"
hypothesis: "Within Enterobacteriaceae, genomes from inflamed or gut sources do not carry more siderophore or genotoxin clusters than genomes from other sources. The large enrichment seen against the full cluster catalog is a lineage effect."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "The pangenome and metagenome tables are in the catalog, but mapping cluster themes onto annotations and matching genomes needs new computation."
databases: ["kbase.ke_pangenome", "kescience.mgnify"]
tables: ["kbase.ke_pangenome.bakta_annotations", "kbase.ke_pangenome.gtdb_metadata", "kbase.ke_pangenome.ncbi_env", "kescience.mgnify.gene_bgc"]
findings: ["ibd_phage_targeting--446eca8c"]
conflicts: []
papers: ["41606218", "42458242"]
builds_on: ["findings/ibd_phage_targeting--446eca8c"]
projects: ["ibd_phage_targeting"]
topics: ["translational-microbiome-and-phage-therapeutics"]
---
# Do gut Enterobacteriaceae carry extra siderophore and genotoxin clusters beyond lineage expectation?

Do gut-associated Enterobacteriaceae carry more iron-siderophore and genotoxin clusters than their non-gut relatives, or does the enrichment among the Crohn's targets come from lineage alone?

## Hypothesis

Within Enterobacteriaceae, genomes from inflamed or gut sources do not carry more siderophore or genotoxin clusters than genomes from other sources. The large enrichment seen against the full cluster catalog is a lineage effect.

## Why it matters

The enrichment was measured against a rare-cluster background, so it may reflect lineage and not disease selection. This test says whether iron and genotoxin traits justify a Crohn's-specific mechanism axis for target choice.

## How to test it

Take Enterobacteriaceae genomes from the pangenome collection with their isolation source and predicted cluster content. Compare siderophore and genotoxin cluster counts between gut-associated and non-gut genomes within each genus, and against matched Enterobacteriaceae drawn at random. Repeat with the environmental metagenome cluster tables as an outside check.

## What would support or refute it

Support for lineage-only: within-genus gut and non-gut genomes carry the same clusters. Refutation: gut genomes within genera carry more clusters, pointing to habitat selection beyond lineage.

## Data

Approach: lakehouse analysis. Readiness: needs compute. The pangenome and metagenome tables are in the catalog, but mapping cluster themes onto annotations and matching genomes needs new computation.

## Builds on

- Finding: [[findings/ibd_phage_targeting--446eca8c|Tier-A core gene clusters are enriched for iron-siderophore and genotoxin themes]] (Insufficient literature evidence)

## Closest published work

- [PMID 41606218](https://pubmed.ncbi.nlm.nih.gov/41606218/) From niche to niche: investigating microbial communities and their specialised metabolite gene clusters in human microbiomes.
- [PMID 42458242](https://pubmed.ncbi.nlm.nih.gov/42458242/) Genomic insights into specialized and primary metabolism gene clusters in methicillin-resistant Staphylococcus aureus from Egyptian community settings.

PMID 41606218 surveys specialised metabolite clusters across human microbiomes and PMID 42458242 does so for Staphylococcus aureus; neither separates lineage from habitat selection for iron and genotoxin clusters among gut Enterobacteriaceae.
