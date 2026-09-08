---
type: Method
description: UMAP is a nonlinear method for visualizing structure in genome embeddings.
sources:
- id: amr_strain_variation
  resource: ../summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
- id: env_embedding_explorer
  resource: ../summaries/env_embedding_explorer__REPORT.md
  title: env embedding explorer
title: UMAP
---
# UMAP

## What it is

UMAP (Uniform Manifold Approximation and Projection) is a nonlinear dimensional-reduction method used in this study to identify distinct antimicrobial-resistance (AMR) ecotypes. [^amr_strain_variation]

- **Canonical name:** UMAP. [^amr_strain_variation]
- **Known aliases:** Uniform Manifold Approximation and Projection. [^amr_strain_variation]
- **Stable external identifier:** None was reported in the source documents. [^amr_strain_variation][^env_embedding_explorer]
- **Related method:** [dbscan](dbscan.md) was applied after UMAP for density-based clustering. [^amr_strain_variation]

## Applications and findings

In the AMR ecotype analysis, UMAP included 974 species with at least 15 genomes suitable for clustering. [^amr_strain_variation] Of those 974 species, 190 (19.5%) formed at least two distinct AMR ecotypes. [^amr_strain_variation] The median silhouette score for the ecotype clusters was 0.620. [^amr_strain_variation]

Case-study UMAP plots for [klebsiella-pneumoniae](klebsiella-pneumoniae.md), [staphylococcus-aureus](staphylococcus-aureus.md), and [salmonella-enterica](salmonella-enterica.md) showed visible environmental structuring, although the available statistical tests were underpowered to establish a general environment–ecotype association. [^amr_strain_variation] Environment–ecotype testing was limited because 52.7% of genomes had no classifiable isolation_source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [^amr_strain_variation] Escherichia coli was not included in the case studies because it exceeded the 500-genome computational cap. [^amr_strain_variation] UMAP outputs included 176,177 ecotype assignments and 974 ecotype summaries. [^amr_strain_variation]

The genome-embedding explorer **refines** this AMR-focused use: UMAP projected 64-dimensional AlphaEarth satellite-derived embeddings for 83,287 genomes into two dimensions, and [dbscan](dbscan.md) identified 320 clusters. [^env_embedding_explorer] Many clusters were dominated by a single harmonized environment category, while phylum coloring also showed taxonomic structure partly confounded with environment. [^env_embedding_explorer] This **supports** using UMAP to inspect environmental and taxonomic structure, but its nonlinear projections depend on parameters including n_neighbors and min_dist and may not represent the true high-dimensional topology. [^env_embedding_explorer]

The method and its results contribute to [amr_strain_variation__REPORT](../summaries/amr_strain_variation__REPORT.md) and [env_embedding_explorer__REPORT](../summaries/env_embedding_explorer__REPORT.md), informing the [environmental-resistome](../concepts/environmental-resistome.md) synthesis and the [environment-embedding-geography](../concepts/environment-embedding-geography.md) synthesis. [^amr_strain_variation][^env_embedding_explorer]

[^amr_strain_variation]: [amr strain variation](../summaries/amr_strain_variation__REPORT.md)
[^env_embedding_explorer]: [env embedding explorer](../summaries/env_embedding_explorer__REPORT.md)
