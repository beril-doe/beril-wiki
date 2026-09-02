---
type: "Concept"
description: "Limits of interpreting UMAP and density clusters as ecological structure"
sources: ["summaries/env_embedding_explorer__REPORT.md"]
---
# Dimensionality Reduction and Density Clustering Can Overstate Ecological Structure

[[summaries/env_embedding_explorer__REPORT]] shows that nonlinear dimensionality reduction and density-based clustering can make ecological structure appear more discrete, stable, or interpretable than the underlying high-dimensional evidence supports. [src: env_embedding_explorer]

## Evidence

The project applied UMAP, a nonlinear dimensionality-reduction method, to 64-dimensional AlphaEarth embeddings from 83,287 genomes and used DBSCAN, a density-based clustering method, to identify 320 clusters. [src: env_embedding_explorer] Many UMAP clusters were dominated by a single harmonized environment category, while rare categories such as Air, Extreme, and Plant concentrated in a few clusters. [src: env_embedding_explorer] Human gut and Human clinical genomes were distributed across many clusters, potentially reflecting geographic substructure rather than discrete ecological types. [src: env_embedding_explorer]

Coloring the UMAP projection by phylum also revealed taxonomic structure, but that pattern was partly confounded with environment. [src: env_embedding_explorer] Campylobacterota, for example, were predominantly gut-associated, so their apparent separation in the projection cannot be interpreted as purely taxonomic or purely environmental without additional controls. [src: env_embedding_explorer]

## Why the Structure Is Interpretation-Limited

UMAP’s apparent cluster structure depends on parameters including `n_neighbors` and `min_dist`, and the resulting two-dimensional projection may not represent the true topology of the original high-dimensional embedding space. [src: env_embedding_explorer] Consequently, visual separation in UMAP is evidence of a representation-dependent pattern, not by itself evidence for discrete ecological communities or environment-defined genomic lineages. [src: env_embedding_explorer]

DBSCAN produced 320 clusters with `eps=0.5`, but the report notes that this may be too fine-grained and that coarser clustering could better match environment categories. [src: env_embedding_explorer] The number and composition of inferred clusters therefore depend on clustering choices, making ecological interpretation sensitive to the selected density threshold and scale. [src: env_embedding_explorer]

The environmental labels used to interpret clusters were themselves incomplete and heterogeneous: isolation_source was available for 76,295 genomes (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%), and env_medium for 31,483 (37.8%) among the AlphaEarth genomes. [src: env_embedding_explorer] A keyword workflow mapped 5,774 unique isolation_source values to 12 broad categories, captured 71% of genomes with a label, left 17% in Other, and classified 12.5% as Unknown because isolation_source was missing or null. [src: env_embedding_explorer] These coverage and harmonization limits mean that apparent cluster–environment correspondence can reflect labeling decisions as well as embedding structure. [src: env_embedding_explorer]

The dataset also has a strong human-associated composition: Human clinical included 16,390 genomes (20%), Human gut included 13,466 (16%), and Human other included 1,669 (2%), while Soil included 6,073 (7%), Marine 5,850 (7%), and Freshwater 5,840 (7%). [src: env_embedding_explorer] The 38% human-associated fraction may distribute clinical and gut samples across relatively interchangeable urban or host-associated contexts, potentially diluting or reshaping ecological patterns inferred from the full projection. [src: env_embedding_explorer]

## Interpretation Rule

UMAP separation and DBSCAN membership should be treated as exploratory structure that requires validation in the original 64-dimensional space and against independently harmonized environmental variables. [src: env_embedding_explorer] A cluster should not be treated as an ecological unit unless its membership is stable across dimensionality-reduction and clustering settings, remains associated with environmental variables after accounting for taxonomy and geography, and corresponds to reproducible genomic or functional differences. [src: env_embedding_explorer]

This limitation refines [[concepts/environmental-embedding-ecological-validity]] and [[concepts/embedding-cluster-interpretation-limits]] by distinguishing projection-level patterns from validated ecological structure. [src: env_embedding_explorer] It also bears on [[concepts/ecotype-clustering-validity]] and [[concepts/ecotype-environment-gene-content]], because cluster labels can affect which genomes are compared as ecological groups and whether environment appears predictive of gene content. [src: env_embedding_explorer]

## Open Directions

- Recompute UMAP over the 79,449 genomes with valid values across all 64 dimensions while varying `n_neighbors` and `min_dist`; test whether the same environmental and taxonomic separations persist. [src: env_embedding_explorer]
- Re-run DBSCAN across a grid of `eps` values, compare the resulting cluster assignments with coarser alternatives, and ask which resolution best reproduces independently harmonized environment categories. [src: env_embedding_explorer]
- Compare UMAP and DBSCAN assignments with distances in the original 64-dimensional space; test whether cluster separation remains after removing projection effects. [src: env_embedding_explorer]
- Use the 50,109 genomes classified as Good coordinates and stratify by environmental versus human-associated categories; test whether cluster structure remains after controlling for geographic distance and sampling composition. [src: env_embedding_explorer]
- Compare keyword-based environment labels with `env_broad_scale` for the 42% of genomes covered by the structured field; test whether cluster–environment associations are robust to harmonization schema. [src: env_embedding_explorer]
- Reassess [[concepts/ecotype-environment-gene-content]] on stable, environmentally validated clusters and environmental-only samples; test whether genomic differences remain after controlling for phylogeny. [src: env_embedding_explorer]
