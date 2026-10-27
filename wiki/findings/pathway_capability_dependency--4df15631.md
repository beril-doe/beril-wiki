---
type: "Finding"
description: "Among 225 species with sufficient genome diversity (50+ genomes and 3+ variable pathways), hierarchical clustering of binary pathway profiles (Jaccard distance) identifies a median of 4 metabolic ecotypes per species, with a maximum of 8."
finding_id: "pathway_capability_dependency--4df15631"
result: "observation"
source: "pathway_capability_dependency"
quantities: [{"value": "4", "what": "median metabolic ecotypes per species", "unit": "ecotypes", "denominator": "", "scope": "225 species with 50+ genomes and 3+ variable pathways"}, {"value": "8", "what": "maximum metabolic ecotypes per species", "unit": "ecotypes", "denominator": "", "scope": "225 species"}, {"value": "225", "what": "species meeting the genome and variable-pathway criteria", "unit": "species", "denominator": "", "scope": ""}]
caveat: "The median of 4 ecotypes per species depends on a fixed 50% clustering-distance threshold, and different thresholds would yield different counts, so it should be treated as an order-of-magnitude estimate."
first_added: "2026-10-27"
source_hash: "b48f1bebed72779629baaf7e71b9cffda8ab0298f49aa9c3460cc6d13bb7cf75"
---
# Species with many genomes split into a handful of metabolic ecotypes

Among 225 species with sufficient genome diversity (50+ genomes and 3+ variable pathways), hierarchical clustering of binary pathway profiles (Jaccard distance) identifies a median of 4 metabolic ecotypes per species, with a maximum of 8. [src: pathway_capability_dependency]

## Key figures

- **4 ecotypes**: median metabolic ecotypes per species (scope 225 species with 50+ genomes and 3+ variable pathways) [src: pathway_capability_dependency]
- **8 ecotypes**: maximum metabolic ecotypes per species (scope 225 species) [src: pathway_capability_dependency]
- **225 species**: species meeting the genome and variable-pathway criteria [src: pathway_capability_dependency]

## Evidence

> Among 225 species with sufficient genome diversity (50+ genomes and 3+ variable pathways), hierarchical clustering of binary pathway profiles (Jaccard distance) identifies a median of 4 metabolic ecotypes per species, with a maximum of 8. [src: pathway_capability_dependency]

From the report [[summaries/pathway_capability_dependency__REPORT]].

## Caveat

The median of 4 ecotypes per species depends on a fixed 50% clustering-distance threshold, and different thresholds would yield different counts, so it should be treated as an order-of-magnitude estimate. [src: pathway_capability_dependency]

> The hierarchical clustering with a fixed 50% distance threshold is a simplification. Different distance thresholds would yield different ecotype counts. The median of 4 ecotypes per species should be interpreted as an order-of-magnitude estimate. [src: pathway_capability_dependency]

## Other caveats in this report

- The report cites a separate finding of 28,017 Fitness Browser genes costly in lab but conserved in nature, underscoring lab-versus-nature limitations. [src: pathway_capability_dependency]
- The report proposes the hypothesis that environmental-condition breadth, rather than mean fitness under one condition, may constrain pathway gene loss. [src: pathway_capability_dependency]
- The core-completeness comparison is compressed by 7 well-studied model organisms; this passage names all 7. [src: pathway_capability_dependency]
- The pathway-openness signal was positive in 13 of 18 genera and significant in 5 of 18; small genus-level samples limit power. [src: pathway_capability_dependency]
- Only 7 of 48 Fitness Browser organisms matched GapMind genome data, and 23 pathways had sufficient annotation, limiting classification to 161 pairs. [src: pathway_capability_dependency]
