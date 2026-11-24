---
type: "Method"
description: "Non-linear dimensionality reduction (Uniform Manifold Approximation and Projection) of embeddings or profile distances to 2D, including its pairing with DBSCAN to define AMR ecotypes."
sources: ["summaries/amr_strain_variation__REPORT.md", "summaries/env_embedding_explorer__REPORT.md"]
aliases: ["UMAP + DBSCAN", "UMAP and DBSCAN clustering of AMR profiles", "Uniform Manifold Approximation and Projection"]
---
# UMAP

This page covers UMAP, the non-linear dimensionality reduction of embeddings or profile distances to 2D, including its pairing with DBSCAN to define AMR ecotypes. UMAP is uniform manifold approximation and projection, and AMR is antimicrobial resistance. It was used on AMR profiles and on AlphaEarth embeddings. [src: amr_strain_variation, env_embedding_explorer]

## Key facts

- Alias: UMAP + DBSCAN, UMAP and DBSCAN clustering of AMR profiles.
- The notebook 05_amr_ecotypes.ipynb applies UMAP + DBSCAN clustering to AMR profiles and examines environment-ecotype association. [src: amr_strain_variation]
- The env_embedding_explorer project stored 79,449 rows of pre-computed UMAP 2D coordinates in data/umap_coords.csv. [src: env_embedding_explorer]

## Use on AMR profiles

Of 974 species with at least 15 genomes eligible for clustering, 190 (19.5%) form at least 2 distinct AMR ecotypes. This used UMAP + DBSCAN clustering of AMR Jaccard distances. [src: amr_strain_variation] The median silhouette score was 0.620, which the report interprets as good cluster quality. [src: amr_strain_variation] See [[concepts/amr-ecotypes-and-environmental-association]] and [[summaries/amr_strain_variation__REPORT]].

## Use on AlphaEarth embeddings

UMAP reduction of the 64-dimensional embeddings to 2D reveals substantial structure. [src: env_embedding_explorer] DBSCAN clustering identified 320 clusters. [src: env_embedding_explorer] See [[entities/alphaearth-environmental-embeddings]], [[concepts/independent-continuous-environment-embeddings-versus-categorical-isolation-source]] and [[summaries/env_embedding_explorer__REPORT]].

## Caveats

- UMAP is a non-linear projection. Its cluster structure depends on parameters (n_neighbors, min_dist) and may not reflect true high-dimensional topology. [src: env_embedding_explorer]
- DBSCAN with eps=0.5 produced 320 clusters. The report considers this likely too fine-grained and suggests that coarser clustering may better match environment categories. [src: env_embedding_explorer]
