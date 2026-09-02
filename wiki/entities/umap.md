---
type: "Method"
description: "UMAP is a nonlinear method for visualizing structure in genome embeddings."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/env_embedding_explorer__REPORT.md"]
---
# UMAP

## What it is

UMAP (Uniform Manifold Approximation and Projection) is a nonlinear dimensional-reduction method used in this study to identify distinct antimicrobial-resistance (AMR) ecotypes. [src: amr_strain_variation]

- **Canonical name:** UMAP. [src: amr_strain_variation]
- **Known aliases:** Uniform Manifold Approximation and Projection. [src: amr_strain_variation]
- **Stable external identifier:** None was reported in the source documents. [src: amr_strain_variation; env_embedding_explorer]
- **Related method:** [[entities/dbscan]] was applied after UMAP for density-based clustering. [src: amr_strain_variation]

## Applications and findings

In the AMR ecotype analysis, UMAP included 974 species with at least 15 genomes suitable for clustering. [src: amr_strain_variation] Of those 974 species, 190 (19.5%) formed at least two distinct AMR ecotypes. [src: amr_strain_variation] The median silhouette score for the ecotype clusters was 0.620. [src: amr_strain_variation]

Case-study UMAP plots for [[entities/klebsiella-pneumoniae]], [[entities/staphylococcus-aureus]], and [[entities/salmonella-enterica]] showed visible environmental structuring, although the available statistical tests were underpowered to establish a general environment–ecotype association. [src: amr_strain_variation] Environment–ecotype testing was limited because 52.7% of genomes had no classifiable isolation_source, and only 2 species had sufficient within-species environmental diversity for chi-squared testing after strict expected-frequency criteria. [src: amr_strain_variation] Escherichia coli was not included in the case studies because it exceeded the 500-genome computational cap. [src: amr_strain_variation] UMAP outputs included 176,177 ecotype assignments and 974 ecotype summaries. [src: amr_strain_variation]

The genome-embedding explorer **refines** this AMR-focused use: UMAP projected 64-dimensional AlphaEarth satellite-derived embeddings for 83,287 genomes into two dimensions, and [[entities/dbscan]] identified 320 clusters. [src: env_embedding_explorer] Many clusters were dominated by a single harmonized environment category, while phylum coloring also showed taxonomic structure partly confounded with environment. [src: env_embedding_explorer] This **supports** using UMAP to inspect environmental and taxonomic structure, but its nonlinear projections depend on parameters including n_neighbors and min_dist and may not represent the true high-dimensional topology. [src: env_embedding_explorer]

The method and its results contribute to [[summaries/amr_strain_variation__REPORT]] and [[summaries/env_embedding_explorer__REPORT]], informing the [[concepts/environmental-resistome]] synthesis and the [[concepts/environment-embedding-geography]] synthesis. [src: amr_strain_variation; env_embedding_explorer]
