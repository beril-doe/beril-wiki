---
type: "Finding"
description: "Among 54 free-living and plant-associated species (>=5 genomes, >=60% majority environment agreement), carbon pathway profiles were significantly associated with isolation environment in a PERMANOVA-like permutation test (999 permutations, p = 0.006), with between-group mean distance 2.054 exceeding within-group mean distance 1.890."
finding_id: "pseudomonas_carbon_ecology--eb1d58ae"
result: "observation"
source: "pseudomonas_carbon_ecology"
quantities: [{"value": "p = 0.006", "what": "Permutation test of pathway profiles vs isolation environment", "unit": "", "denominator": "", "scope": "999 permutations, 54 species"}, {"value": "2.054", "what": "Between-group mean distance", "unit": "", "denominator": "", "scope": ""}, {"value": "1.890", "what": "Within-group mean distance", "unit": "", "denominator": "", "scope": ""}, {"value": "74.9%", "what": "Variance captured by first 5 PCA components", "unit": "%", "denominator": "total variance", "scope": "62-pathway profiles"}]
caveat: "The primary axis of variation separates Pseudomonas s.s. from Pseudomonas_E, and within Pseudomonas_E lifestyle categories overlap substantially, so lifestyle-associated variation is subtler than the deep phylogenetic divide."
first_added: "2026-10-27"
source_hash: "9a0d1678e23b48d6e7732b56ad5ca0452fed1ff9fcf5c9c5e8e9b23315c58260"
---
# Carbon pathway profiles associate with isolation environment across free-living and plant-associated species

Among 54 free-living and plant-associated species (>=5 genomes, >=60% majority environment agreement), carbon pathway profiles were significantly associated with isolation environment in a PERMANOVA-like permutation test (999 permutations, p = 0.006), with between-group mean distance 2.054 exceeding within-group mean distance 1.890. [src: pseudomonas_carbon_ecology]

## Key figures

- **p = 0.006**: Permutation test of pathway profiles vs isolation environment (scope 999 permutations, 54 species) [src: pseudomonas_carbon_ecology]
- **2.054**: Between-group mean distance [src: pseudomonas_carbon_ecology]
- **1.890**: Within-group mean distance [src: pseudomonas_carbon_ecology]
- **74.9%**: Variance captured by first 5 PCA components (denominator total variance; scope 62-pathway profiles) [src: pseudomonas_carbon_ecology]

## Evidence

> Among 54 free-living and plant-associated species (>=5 genomes, >=60% majority environment agreement), carbon pathway profiles are significantly associated with isolation environment. A PERMANOVA-like permutation test (999 permutations) yielded **p = 0.006**, with between-group mean distance (2.054) exceeding within-group mean distance (1.890). PCA of the 62-pathway profiles captured 74.9% of variance in the first 5 components, with PC1 alone explaining 31.2%. [src: pseudomonas_carbon_ecology]

From the report [[summaries/pseudomonas_carbon_ecology__REPORT]].

## Caveat

The primary axis of variation separates Pseudomonas s.s. from Pseudomonas_E, and within Pseudomonas_E lifestyle categories overlap substantially, so lifestyle-associated variation is subtler than the deep phylogenetic divide. [src: pseudomonas_carbon_ecology]

> PCA of all species' pathway profiles reveals that the primary axis of variation separates *Pseudomonas* s.s. from *Pseudomonas_E*, driven by the dramatic sugar pathway loss described in Finding 1. Within *Pseudomonas_E*, lifestyle categories (free-living, host-associated, plant-associated) show substantial overlap, indicating that the lifestyle-associated variation within this subgenus is more subtle than the deep phylogenetic divide. [src: pseudomonas_carbon_ecology]

## Other caveats in this report

- Only 64.2% of genomes (8,171/12,732) had classifiable isolation sources; categories were assigned by keywords. [src: pseudomonas_carbon_ecology]
- Small classes, overlapping environments and coarse pathway resolution may explain the classifier's moderate accuracy. [src: pseudomonas_carbon_ecology]
- The report contrasts within-infection metabolic loss with a hypothesis of ancestral lineage-level streamlining; the timing remains an interpretation. [src: pseudomonas_carbon_ecology]
- The report notes strain-level hydrocarbon-gene variation and hypothesizes that 62 GapMind pathways may be too coarse for fine-grained environment prediction. [src: pseudomonas_carbon_ecology]
- Release from selection for plant-associated metabolism during an animal-host transition is an interpretation of the pathway-loss pattern, not a directly tested transition. [src: pseudomonas_carbon_ecology]
