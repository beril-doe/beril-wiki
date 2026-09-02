---
type: "Organism"
description: "Bacterium analyzed for gene-content ecotype differentiation"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md"]
---
# Enterobacter cloacae

## Identity

Enterobacter cloacae is the canonical name of the bacterial organism analyzed in this report. [src: ecotype_functional_differentiation]

- **Canonical name:** Enterobacter cloacae. [src: ecotype_functional_differentiation]
- **Known aliases:** No aliases are specified in the source document. [src: ecotype_functional_differentiation]
- **Stable external identifier:** No stable external identifier is reported in the source document. [src: ecotype_functional_differentiation]

## Findings in ecotype functional differentiation

The report identified valid gene-content ecotypes for Enterobacter cloacae using principal-component analysis (PCA), followed by KMeans clustering. [src: ecotype_functional_differentiation]

Enterobacter cloacae was represented by **216 genomes**, assigned to **5 ecotypes**, with **210 genomes assigned** to an ecotype. [src: ecotype_functional_differentiation]

This result contributed to the report-wide finding that valid gene-content ecotypes were detected in **12 of 15 sampled species (80%)**, assigning **1,820 genomes across 12 species**. [src: ecotype_functional_differentiation]

The report selected ecotype counts by searching **k = 2–6** and choosing the clustering with the best silhouette score; valid clusters required at least **2 ecotypes**, at least **10 genomes per ecotype**, and at least **20 assigned genomes in total**. [src: ecotype_functional_differentiation]

The Enterobacter cloacae result supports [[concepts/ecotype-environment-gene-content]], which synthesizes evidence that within-species gene-content variation can form functionally differentiated ecotypes. [src: ecotype_functional_differentiation]

It also contributes to [[concepts/pangenome-integration]] by linking pangenome-derived gene-content clustering with COG functional profiles. [src: ecotype_functional_differentiation]

The report’s broader functional comparison used COG (Clusters of Orthologous Groups) categories and found significant ecotype differentiation in **170 of 257 tests (66.1%)** after Benjamini–Hochberg false-discovery-rate correction at **q < 0.05**; the source does not provide a separate COG significance result specifically for Enterobacter cloacae. [src: ecotype_functional_differentiation]

## Limitations relevant to interpretation

The Enterobacter cloacae ecotype assignments may reflect phylogenetic or demographic substructure as well as ecological adaptation because the analysis did not apply within-species phylogenetic controls such as core-genome trees. [src: ecotype_functional_differentiation]

The report also notes that approximately **38%** of gene clusters had COG annotations, leaving **62%** unannotated, so ecotype-specific genes in Enterobacter cloacae may be underrepresented in the functional comparison. [src: ecotype_functional_differentiation]

## Related pages

- [[summaries/ecotype_functional_differentiation__REPORT]] — source report summarized on this page.
- [[concepts/ecotype-environment-gene-content]] — within-species gene-content ecotypes and their environmental and functional interpretation.
- [[concepts/pangenome-integration]] — integration of pangenome gene-content data with functional profiles.
- [[entities/kmeans-clustering]] — clustering method used in the analysis.
- [[entities/cog-functional-categories]] — functional classification system used for COG profiles.
