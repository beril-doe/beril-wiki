---
type: "Research direction"
description: "Species from more diverse environments carry more resistance genes with a smaller core share, and within most phyla open pangenomes carry more of them. Is this resistance-specific, or the general accessory-gene growth of generalists?"
hypothesis: "The rise of resistance-gene count with environmental diversity is steeper than that of matched-size sets of other accessory gene classes, such as defense or metabolic genes, within the same phyla."
approach: "lakehouse analysis"
readiness: "needs compute"
readiness_basis: "Resistance clusters, accessory status and environmental embeddings exist, but only 28% of genomes have embeddings and the null sets have not been built."
collections: ["kbase-ke-pangenome"]
findings: ["amr_pangenome_atlas--b878500b", "amr_pangenome_atlas--ee1ea51b", "amr_pangenome_atlas--1e435872"]
conflicts: []
papers: ["38457973", "36882798", "38039820", "34737424"]
builds_on: ["findings/amr_pangenome_atlas--b878500b", "findings/amr_pangenome_atlas--ee1ea51b", "findings/amr_pangenome_atlas--1e435872"]
projects: ["amr_pangenome_atlas"]
topics: ["functional-dark-matter-and-annotation-resolution"]
---
# Do species from varied environments gain resistance genes beyond other accessory genes?

Species from more diverse environments carry more resistance genes with a smaller core share, and within most phyla open pangenomes carry more of them. Is this resistance-specific, or the general accessory-gene growth of generalists?

## Hypothesis

The rise of resistance-gene count with environmental diversity is steeper than that of matched-size sets of other accessory gene classes, such as defense or metabolic genes, within the same phyla.

## Why it matters

If resistance is steeper, environmental exposure selects for resistance genes themselves. If it matches other accessory classes, resistance is a passenger of open pangenomes, which changes how reservoirs of resistance are predicted.

## How to test it

In the Pangenome Collection, for species with several genomes and environmental embeddings, compute environmental diversity. Regress resistance-gene count and the counts of matched-size random accessory-gene sets on it, within each phylum. Compare slopes. Repeat with pangenome openness in the model, since openness correlates positively with resistance count in most phyla.

## What would support or refute it

Support: resistance has a clearly steeper slope than random accessory sets in most phyla after openness is included. Refutation: its slope sits within the spread of random accessory sets, or disappears once openness is included.

## Data

Approach: lakehouse analysis. Readiness: needs compute. Resistance clusters, accessory status and environmental embeddings exist, but only 28% of genomes have embeddings and the null sets have not been built.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/amr_pangenome_atlas--b878500b|Species from more diverse environments carry more, less-core AMR genes]] (Insufficient literature evidence)
- Finding: [[findings/amr_pangenome_atlas--ee1ea51b|Overall openness–AMR correlation hides positive within-phylum associations]] (Insufficient literature evidence)
- Finding: [[findings/amr_pangenome_atlas--1e435872|AMR clusters are depleted from core and enriched in auxiliary genomes]] (Extends retrieved work)

## Closest published work

- [PMID 38457973](https://pubmed.ncbi.nlm.nih.gov/38457973/) Environmental drivers impact the accumulation and diversity of antibiotic resistance in green stormwater infrastructure.
- [PMID 36882798](https://pubmed.ncbi.nlm.nih.gov/36882798/) Latent antibiotic resistance genes are abundant, diverse, and mobile in human, animal, and environmental microbiomes.
- [PMID 38039820](https://pubmed.ncbi.nlm.nih.gov/38039820/) Rare resistome rather than core resistome exhibited higher diversity and risk along the Yangtze River.
- [PMID 34737424](https://pubmed.ncbi.nlm.nih.gov/34737424/) Antibiotic resistance in the environment.

PMID 38457973 and PMID 38039820 link environmental drivers to resistance diversity in specific habitats. Neither compares resistance against other accessory gene classes to ask whether the environmental scaling is specific.
