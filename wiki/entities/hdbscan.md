---
type: "Method"
description: "Density-based clustering method considered for ecotype analysis"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md"]
---
# HDBSCAN

## What this entity is

**Canonical name:** HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise), a density-based clustering method. [src: ecotype_functional_differentiation]

**Known aliases:** HDBSCAN; the report does not provide additional aliases. [src: ecotype_functional_differentiation]

**Stable external identifier:** Not reported in the source document. [src: ecotype_functional_differentiation]

## Key facts

HDBSCAN was unavailable on the cluster used for the ecotype analysis, so the report used KMeans instead. [src: ecotype_functional_differentiation]

The report states that KMeans assumes spherical clusters and requires a selected number of clusters, whereas HDBSCAN could better handle variable-density subpopulations. [src: ecotype_functional_differentiation]

The analysis applied PCA followed by KMeans, searched k = 2–6, and selected the best silhouette score; comparing these results with HDBSCAN is proposed as a future direction. [src: ecotype_functional_differentiation]

HDBSCAN is therefore relevant to [[concepts/ecotype-environment-gene-content]] as an alternative clustering approach for testing whether within-species gene-content ecotypes are robust to clustering assumptions. [src: ecotype_functional_differentiation]

## Related pages

- [[summaries/ecotype_functional_differentiation__REPORT]] — source summary describing the unavailable-cluster limitation and proposed HDBSCAN comparison. [src: ecotype_functional_differentiation]
- [[entities/kmeans-clustering]] — clustering method used in the analysis instead of HDBSCAN. [src: ecotype_functional_differentiation]
- [[entities/dbscan]] — related density-based clustering method. [src: ecotype_functional_differentiation]
