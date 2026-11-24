---
type: "Method"
description: "Hierarchical clustering of binary pathway profiles with Jaccard distance, cut at 50% of maximum distance, to define within-species metabolic ecotypes."
sources: ["summaries/discoveries.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Metabolic ecotype clustering

Metabolic ecotype clustering is a method that groups genomes within a species by their pathway profiles. It uses hierarchical clustering of binary pathway profiles with Jaccard distance, cut at 50% of maximum distance. [src: pathway_capability_dependency] It gives a median of 4 ecotypes per species. [src: pathway_capability_dependency] The report says this median should be interpreted as an order-of-magnitude estimate. [src: pathway_capability_dependency]

## Key facts

- **Input:** Binary pathway profiles (complete or incomplete) across 80 pathways. [src: pathway_capability_dependency]
- **Species included:** 225 species with 50 or more genomes and at least 3 variable pathways. [src: pathway_capability_dependency]
- **Algorithm:** Hierarchical clustering with Jaccard distance. [src: pathway_capability_dependency]
- **Ecotype count:** Each species' dendrogram is cut at 50% of maximum distance, and the number of clusters is the number of ecotypes. [src: pathway_capability_dependency]
- **Pathway source:** The central discoveries digest describes the profiles as GapMind pathway profiles. [src: discoveries]

## Result

Across the 225 species, the method gives a median of 4 metabolic ecotypes per species and a maximum of 8. [src: discoveries, pathway_capability_dependency] See [[concepts/within-species-metabolic-ecotypes-from-pathway-variation]] for the wider interpretation, and [[summaries/pathway_capability_dependency__REPORT]] and [[summaries/discoveries]] for the source summaries.

## Caveats

A fixed 50% distance threshold is a simplification, and different thresholds would give different ecotype counts. [src: pathway_capability_dependency] Separately, the report states that the median of 4 ecotypes per species should be interpreted as an order-of-magnitude estimate. [src: pathway_capability_dependency]
