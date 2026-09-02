---
type: "Method"
description: "Density-based clustering method for identifying embedding and ecotype clusters"
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/env_embedding_explorer__REPORT.md"]
---
# DBSCAN

## What this entity is

**Canonical name:** DBSCAN. [src: amr_strain_variation]

**Known aliases:** None reported in these documents. [src: amr_strain_variation, env_embedding_explorer]

**Stable external identifier:** None reported in these documents. [src: amr_strain_variation, env_embedding_explorer]

DBSCAN is a density-based clustering method used after [[entities/umap]] (uniform manifold approximation and projection) to identify distinct antimicrobial-resistance (AMR) ecotypes. [src: amr_strain_variation] The [[summaries/env_embedding_explorer__REPORT]] shows that the same method was also applied to UMAP projections of 64-dimensional AlphaEarth embeddings, where eps=0.5 produced 320 embedding clusters. [src: env_embedding_explorer]

## Key facts across projects

In the AMR ecotype analysis, DBSCAN included 974 species with at least 15 genomes. [src: amr_strain_variation] Of these, 190 (19.5%) formed at least 2 distinct AMR ecotypes. [src: amr_strain_variation] The median silhouette score for the ecotype clusters was 0.620. [src: amr_strain_variation] The analysis generated 176,177 ecotype assignments and 974 ecotype summaries. [src: amr_strain_variation]

Environment–ecotype association testing was limited because 52.7% of genomes had no classifiable isolation source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [src: amr_strain_variation] Case-study UMAP plots for [[entities/klebsiella-pneumoniae]], [[entities/staphylococcus-aureus]], and [[entities/salmonella-enterica]] showed visible environmental structuring, but the underpowered statistical tests did not establish a general environment–ecotype association. [src: amr_strain_variation]

The AlphaEarth application **supports** DBSCAN as a reusable clustering step for embedding analysis: many of its 320 clusters were dominated by a single harmonized environment category, while Human gut and Human clinical genomes were distributed across many clusters. [src: env_embedding_explorer] This **refines** the AMR use case by showing that apparent clusters can reflect environmental and geographic structure, not only AMR ecotypes. [src: env_embedding_explorer] The report cautions that DBSCAN cluster structure depends on UMAP parameters and that eps=0.5 may produce overly fine-grained clusters; coarser clustering may better match environment categories. [src: env_embedding_explorer]

DBSCAN therefore contributes to the [[concepts/environmental-resistome]] analysis by providing the clustering step for testing whether within-species AMR repertoires form ecologically structured groups. [src: amr_strain_variation]

## Related pages

- [[entities/umap]] — dimensionality-reduction method used before DBSCAN in both the AMR ecotype and AlphaEarth embedding analyses. [src: amr_strain_variation, env_embedding_explorer]
- [[summaries/amr_strain_variation__REPORT]] — source report describing the AMR ecotype analysis. [src: amr_strain_variation]
- [[summaries/env_embedding_explorer__REPORT]] — source report describing DBSCAN clustering of AlphaEarth embeddings. [src: env_embedding_explorer]
- [[concepts/environmental-resistome]] — cross-project concept covering environmental structure in AMR repertoires. [src: amr_strain_variation]
- [[concepts/environment-embedding-geography]] — concept covering geographic and environmental structure in AlphaEarth embeddings. [src: env_embedding_explorer]
