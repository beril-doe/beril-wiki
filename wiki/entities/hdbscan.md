---
type: Method
description: Density-based clustering method considered for ecotype analysis
sources:
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
title: HDBSCAN
---
# HDBSCAN

## What this entity is

**Canonical name:** HDBSCAN (Hierarchical Density-Based Spatial Clustering of Applications with Noise), a density-based clustering method. [^ecotype_functional_differentiation]

**Known aliases:** HDBSCAN; the report does not provide additional aliases. [^ecotype_functional_differentiation]

**Stable external identifier:** Not reported in the source document. [^ecotype_functional_differentiation]

## Key facts

HDBSCAN was unavailable on the cluster used for the ecotype analysis, so the report used KMeans instead. [^ecotype_functional_differentiation]

The report states that KMeans assumes spherical clusters and requires a selected number of clusters, whereas HDBSCAN could better handle variable-density subpopulations. [^ecotype_functional_differentiation]

The analysis applied PCA followed by KMeans, searched k = 2–6, and selected the best silhouette score; comparing these results with HDBSCAN is proposed as a future direction. [^ecotype_functional_differentiation]

HDBSCAN is therefore relevant to [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) as an alternative clustering approach for testing whether within-species gene-content ecotypes are robust to clustering assumptions. [^ecotype_functional_differentiation]

## Related pages

- [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md) — source summary describing the unavailable-cluster limitation and proposed HDBSCAN comparison. [^ecotype_functional_differentiation]
- [kmeans-clustering](kmeans-clustering.md) — clustering method used in the analysis instead of HDBSCAN. [^ecotype_functional_differentiation]
- [dbscan](dbscan.md) — related density-based clustering method. [^ecotype_functional_differentiation]

[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
