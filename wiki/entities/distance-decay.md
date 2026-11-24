---
type: "Other"
description: "Biogeographic pattern in which similarity decreases with geographic distance."
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/env_embedding_explorer__REPORT.md"]
aliases: ["distance decay of similarity"]
---
# Distance-decay

Distance-decay (also called distance decay of similarity) is a biogeographic pattern in which similarity between communities decreases with geographic distance. [src: env_embedding_explorer] Two projects here measure it: a meter-scale sediment community study with a significant Mantel test, and an embedding-based analysis of genome pairs worldwide.

## Key facts

- Definition: community similarity decreases with geographic distance, a fundamental pattern in biogeography. [src: env_embedding_explorer]
- Sediment communities across 9 wells show it at meter scale. [src: enigma_sso_asv_ecology] See [[concepts/meter-scale-spatial-structure-and-distance-decay-of-subsurface-communities]].
- The env_embedding_explorer report treats genome embedding distance versus geographic distance as a form of it. [src: env_embedding_explorer] See [[concepts/distance-decay-of-environmental-embeddings-with-geographic-distance]].

## Sediment communities at meter scale

Sediment-associated microbial communities across the 9 SSO wells (3×3 grid, ~6 m span) show significant distance-decay of similarity (Mantel test: Spearman ρ = 0.323, p = 0.029, 9,999 permutations). [src: enigma_sso_asv_ecology] The same analysis reported mean Bray-Curtis = 0.747. [src: enigma_sso_asv_ecology] See [[entities/mantel-test]] and [[summaries/enigma_sso_asv_ecology__REPORT]].

## Embedding distance across genomes

Across 50,000 sampled genome pairs with good-quality coordinates, the [[entities/alphaearth-environmental-embeddings]] cosine distance has a clear monotonic relationship with geographic distance. [src: env_embedding_explorer]

The gradient differs by source:

| Genome source | Nearby | Far | Ratio |
|---|---|---|---|
| Environmental (Soil, Marine, Freshwater, Extreme, Plant) | 0.27 (<100 km) | 0.90 (>10,000 km) | 3.4x [src: env_embedding_explorer] |
| Human-associated (gut, clinical, other) | 0.37 | 0.75 | 2.0x [src: env_embedding_explorer] |

The report quantifies the geographic signal as 3.4x for environmental and 2.0x for human-associated samples. [src: env_embedding_explorer]

The relationship is strongest below 2,000 km and plateaus above 5,000 km. [src: env_embedding_explorer] The report suggests the embeddings capture spatially autocorrelated local conditions (climate, vegetation, land use). [src: env_embedding_explorer] It also suggests they capture environmental features more than raw distance. [src: env_embedding_explorer]

## Interpretation (the report's, not tested here)

The report finds the stronger decay in environmental samples consistent with environmental selection. [src: env_embedding_explorer] It reads the weaker decay in human-associated samples as echoing the idea that dispersal limitation generates stronger geographic patterns than deterministic selection alone. [src: env_embedding_explorer] See also [[summaries/env_embedding_explorer__REPORT]].
