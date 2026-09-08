---
type: Organism
description: Bacterial species represented by a three-ecotype pangenome analysis.
sources:
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
title: Bacillus safensis
---
# Bacillus safensis

## Identity

**Canonical name:** *Bacillus safensis*. [^ecotype_functional_differentiation]

**Known aliases:** No aliases are reported in this document. [^ecotype_functional_differentiation]

**Stable external identifier:** No stable external identifier is reported in this document. [^ecotype_functional_differentiation]

## Evidence from ecotype functional differentiation

*Bacillus safensis* was one of the 12 species in which valid gene-content ecotypes were detected in the report’s 15-species sample. [^ecotype_functional_differentiation] The analysis assigned 120 genomes of *Bacillus safensis* to 3 ecotypes, with 117 genomes assigned to an ecotype. [^ecotype_functional_differentiation]

The ecotypes were identified by principal-component analysis (PCA), a dimensionality-reduction method, followed by KMeans clustering; valid clustering required at least 2 ecotypes with at least 10 genomes each and at least 20 assigned genomes in total. [^ecotype_functional_differentiation] The report selected among k = 2–6 KMeans clusters using silhouette score, but it does not provide a species-specific silhouette score for *Bacillus safensis*. [^ecotype_functional_differentiation]

The functional comparison used COG profiles, where COG means Clusters of Orthologous Groups, to test whether gene-content ecotypes differed in functional composition. [^ecotype_functional_differentiation] The report does not provide *Bacillus safensis*-specific counts of significant COG categories or category-level effect sizes. [^ecotype_functional_differentiation]

## Interpretation and limitations

The inclusion of *Bacillus safensis* among the 12 species with valid ecotypes contributes to the report’s multi-species evidence that within-species gene-content ecotypes can be functionally differentiated; this evidence feeds [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md). [^ecotype_functional_differentiation] The result also contributes to [pangenome-integration](../concepts/pangenome-integration.md) because the ecotypes were derived from BERDL pangenome gene-content data and compared through COG profiles. [^ecotype_functional_differentiation]

Interpretation for *Bacillus safensis* remains limited because the sampled species set contained 15 species drawn from 456 eligible species, approximately 38% of gene clusters had COG annotations, and the analysis lacked within-species phylogenetic controls. [^ecotype_functional_differentiation] KMeans was used because HDBSCAN was unavailable on the cluster, so the inferred ecotype structure depends on KMeans assumptions about cluster shape and the selected number of clusters. [^ecotype_functional_differentiation]

## Related pages

The source report is summarized at [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md). [^ecotype_functional_differentiation] Related analytical resources include [kmeans-clustering](kmeans-clustering.md), [principal-component-analysis](principal-component-analysis.md), and [cog-functional-categories](cog-functional-categories.md). [^ecotype_functional_differentiation]

[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
