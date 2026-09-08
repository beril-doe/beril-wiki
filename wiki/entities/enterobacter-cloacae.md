---
type: Organism
description: Bacterium analyzed for gene-content ecotype differentiation
sources:
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
title: Enterobacter cloacae
---
# Enterobacter cloacae

## Identity

Enterobacter cloacae is the canonical name of the bacterial organism analyzed in this report. [^ecotype_functional_differentiation]

- **Canonical name:** Enterobacter cloacae. [^ecotype_functional_differentiation]
- **Known aliases:** No aliases are specified in the source document. [^ecotype_functional_differentiation]
- **Stable external identifier:** No stable external identifier is reported in the source document. [^ecotype_functional_differentiation]

## Findings in ecotype functional differentiation

The report identified valid gene-content ecotypes for Enterobacter cloacae using principal-component analysis (PCA), followed by KMeans clustering. [^ecotype_functional_differentiation]

Enterobacter cloacae was represented by **216 genomes**, assigned to **5 ecotypes**, with **210 genomes assigned** to an ecotype. [^ecotype_functional_differentiation]

This result contributed to the report-wide finding that valid gene-content ecotypes were detected in **12 of 15 sampled species (80%)**, assigning **1,820 genomes across 12 species**. [^ecotype_functional_differentiation]

The report selected ecotype counts by searching **k = 2–6** and choosing the clustering with the best silhouette score; valid clusters required at least **2 ecotypes**, at least **10 genomes per ecotype**, and at least **20 assigned genomes in total**. [^ecotype_functional_differentiation]

The Enterobacter cloacae result supports [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md), which synthesizes evidence that within-species gene-content variation can form functionally differentiated ecotypes. [^ecotype_functional_differentiation]

It also contributes to [pangenome-integration](../concepts/pangenome-integration.md) by linking pangenome-derived gene-content clustering with COG functional profiles. [^ecotype_functional_differentiation]

The report’s broader functional comparison used COG (Clusters of Orthologous Groups) categories and found significant ecotype differentiation in **170 of 257 tests (66.1%)** after Benjamini–Hochberg false-discovery-rate correction at **q < 0.05**; the source does not provide a separate COG significance result specifically for Enterobacter cloacae. [^ecotype_functional_differentiation]

## Limitations relevant to interpretation

The Enterobacter cloacae ecotype assignments may reflect phylogenetic or demographic substructure as well as ecological adaptation because the analysis did not apply within-species phylogenetic controls such as core-genome trees. [^ecotype_functional_differentiation]

The report also notes that approximately **38%** of gene clusters had COG annotations, leaving **62%** unannotated, so ecotype-specific genes in Enterobacter cloacae may be underrepresented in the functional comparison. [^ecotype_functional_differentiation]

## Related pages

- [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md) — source report summarized on this page.
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — within-species gene-content ecotypes and their environmental and functional interpretation.
- [pangenome-integration](../concepts/pangenome-integration.md) — integration of pangenome gene-content data with functional profiles.
- [kmeans-clustering](kmeans-clustering.md) — clustering method used in the analysis.
- [cog-functional-categories](cog-functional-categories.md) — functional classification system used for COG profiles.

[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
