---
type: Method
description: Density-based clustering method for identifying embedding and ecotype
  clusters
sources:
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: env_embedding_explorer
  resource: ../summaries/env_embedding_explorer__REPORT.md
  title: env embedding explorer
title: DBSCAN
---
# DBSCAN

## What this entity is

**Canonical name:** DBSCAN. [^amr_strain_variation]

**Known aliases:** None reported in these documents. [^amr_strain_variation][^env_embedding_explorer]

**Stable external identifier:** None reported in these documents. [^amr_strain_variation][^env_embedding_explorer]

DBSCAN is a density-based clustering method used after [umap](umap.md) (uniform manifold approximation and projection) to identify distinct antimicrobial-resistance (AMR) ecotypes. [^amr_strain_variation] The [env_embedding_explorer__REPORT](../summaries/env_embedding_explorer__REPORT.md) shows that the same method was also applied to UMAP projections of 64-dimensional AlphaEarth embeddings, where eps=0.5 produced 320 embedding clusters. [^env_embedding_explorer]

## Key facts across projects

In the AMR ecotype analysis, DBSCAN included 974 species with at least 15 genomes. [^amr_strain_variation] Of these, 190 (19.5%) formed at least 2 distinct AMR ecotypes. [^amr_strain_variation] The median silhouette score for the ecotype clusters was 0.620. [^amr_strain_variation] The analysis generated 176,177 ecotype assignments and 974 ecotype summaries. [^amr_strain_variation]

Environment–ecotype association testing was limited because 52.7% of genomes had no classifiable isolation source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [^amr_strain_variation] Case-study UMAP plots for [klebsiella-pneumoniae](klebsiella-pneumoniae.md), [staphylococcus-aureus](staphylococcus-aureus.md), and [salmonella-enterica](salmonella-enterica.md) showed visible environmental structuring, but the underpowered statistical tests did not establish a general environment–ecotype association. [^amr_strain_variation]

The AlphaEarth application **supports** DBSCAN as a reusable clustering step for embedding analysis: many of its 320 clusters were dominated by a single harmonized environment category, while Human gut and Human clinical genomes were distributed across many clusters. [^env_embedding_explorer] This **refines** the AMR use case by showing that apparent clusters can reflect environmental and geographic structure, not only AMR ecotypes. [^env_embedding_explorer] The report cautions that DBSCAN cluster structure depends on UMAP parameters and that eps=0.5 may produce overly fine-grained clusters; coarser clustering may better match environment categories. [^env_embedding_explorer]

DBSCAN therefore contributes to the [environmental-resistome](../concepts/environmental-resistome.md) analysis by providing the clustering step for testing whether within-species AMR repertoires form ecologically structured groups. [^amr_strain_variation]

## Related pages

- [umap](umap.md) — dimensionality-reduction method used before DBSCAN in both the AMR ecotype and AlphaEarth embedding analyses. [^amr_strain_variation][^env_embedding_explorer]
- [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md) — source report describing the AMR ecotype analysis. [^amr_strain_variation]
- [env_embedding_explorer__REPORT](../summaries/env_embedding_explorer__REPORT.md) — source report describing DBSCAN clustering of AlphaEarth embeddings. [^env_embedding_explorer]
- [environmental-resistome](../concepts/environmental-resistome.md) — cross-project concept covering environmental structure in AMR repertoires. [^amr_strain_variation]
- [environment-embedding-geography](../concepts/environment-embedding-geography.md) — concept covering geographic and environmental structure in AlphaEarth embeddings. [^env_embedding_explorer]

[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^env_embedding_explorer]: [env embedding explorer](../summaries/env_embedding_explorer__REPORT.md)
