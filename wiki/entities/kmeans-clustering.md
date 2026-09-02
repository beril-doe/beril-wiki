---
type: "Method"
description: "Partitioning method used to identify gene-content and metabolic ecotypes"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md", "summaries/metabolic_capability_dependency__REPORT.md"]
---
# KMeans clustering

## What this entity is

**Canonical name:** KMeans clustering. [src: ecotype_functional_differentiation]

**Known aliases:** K-means clustering; KMeans. [src: ecotype_functional_differentiation]

**Stable external identifier:** None was reported in the source documents. [src: ecotype_functional_differentiation, metabolic_capability_dependency]

KMeans clustering is a partitioning method used after principal component analysis (PCA) to identify within-species gene-content ecotypes from bacterial pangenome data. [src: ecotype_functional_differentiation]

## Use in ecotype and metabolic differentiation

The gene-content analysis used PCA with up to 50 components followed by KMeans, searched cluster counts from k = 2–6, and selected the k with the best silhouette score. [src: ecotype_functional_differentiation]

KMeans identified valid gene-content ecotypes in 12 of 15 sampled species, assigning 1,820 genomes across 12 species spanning 6 phyla. [src: ecotype_functional_differentiation]

The species averaged 3.7 ecotypes, with a range of 2–6 ecotypes per species, and the mean silhouette score was 0.215 with a median of 0.174. [src: ecotype_functional_differentiation]

The clearest clustering occurred in *Erwinia amylovora*, with a silhouette score of 0.468 and 2 ecotypes, and in *Bacteroides xylanisolvens*, with a silhouette score of 0.366 and 6 ecotypes. [src: ecotype_functional_differentiation]

The weakest clustering signals occurred in *Staphylococcus simulans*, with a silhouette score of 0.118, and *Streptococcus pseudopneumoniae*, with a silhouette score of 0.131. [src: ecotype_functional_differentiation]

Valid clusters required at least 2 ecotypes, at least 10 genomes per ecotype, and at least 20 assigned genomes in total. [src: ecotype_functional_differentiation]

A separate metabolic-capability analysis **supports** the use of clustering for within-species metabolic ecotypes: all 10 target species formed clusters with silhouette scores greater than 0.2, ranging from 0.35 for *PALSA-747* sp. to 0.89 for *Salmonella enterica*. [src: metabolic_capability_dependency]

This result **refines** the earlier gene-content analysis rather than replacing it: the two studies used different species sets and feature definitions, with the metabolic analysis finding significant cluster–isolation-environment associations in *Salmonella enterica* (χ²=1570.2, df=25, p<0.0001) and *Phenylobacterium* sp. (χ²=12.2, df=1, p=0.0005), but not in four sampled marine organisms. [src: metabolic_capability_dependency]

The resulting gene-content ecotype assignments were compared using 257 chi-square or Fisher’s exact tests across 12 species and 23 COG categories, with 170 tests, or 66.1%, significant after Benjamini–Hochberg false-discovery-rate correction at q < 0.05. [src: ecotype_functional_differentiation]

## Interpretation and limitations

KMeans-based ecotype assignments provide multi-species evidence that within-species gene-content variation is functionally differentiated, while the overlapping cluster boundaries and small effect sizes limit the strength of ecological interpretation. [src: ecotype_functional_differentiation]

The largest reported mean COG-category effect sizes were 0.0392 for category S, representing unknown function, and 0.0337 for category L, representing replication, recombination, and repair. [src: ecotype_functional_differentiation]

KMeans was used because [[entities/hdbscan]] was unavailable on the cluster, and the report notes that KMeans assumes spherical clusters and requires a selected k, whereas HDBSCAN could better handle variable-density subpopulations. [src: ecotype_functional_differentiation]

Without within-species phylogenetic controls such as core-genome trees, the KMeans-derived ecotypes cannot be distinguished from phylogenetic or demographic substructure. [src: ecotype_functional_differentiation]

The metabolic-capability analysis **reinforces** this limitation: its environment–cluster associations were observational, lacked explicit phylogenetic correction, and could also reflect coarse isolation-source metadata or pathway annotations that miss ecologically relevant gene-content and expression differences. [src: metabolic_capability_dependency]

Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated, so KMeans-associated functional differences may be biased toward better-characterized functions. [src: ecotype_functional_differentiation]

The report proposes comparing KMeans results with HDBSCAN, overlaying core-genome phylogenetic trees on ecotype assignments, scaling the analysis to all 456 eligible species, and integrating habitat metadata. [src: ecotype_functional_differentiation]

## Related pages

This method is documented in [[summaries/ecotype_functional_differentiation__REPORT]] and [[summaries/metabolic_capability_dependency__REPORT]]. [src: ecotype_functional_differentiation, metabolic_capability_dependency]

It contributes to [[concepts/ecotype-environment-gene-content]], which addresses relationships among ecotypes, environments, and gene content, and to [[concepts/pangenome-integration]] through clustering of pangenome gene-content profiles. [src: ecotype_functional_differentiation]

The analysis also contributes to [[concepts/multi-omics-integration]] through proposed integration of functional annotation and protein-structure evidence. [src: ecotype_functional_differentiation]

KMeans was preceded by [[entities/principal-component-analysis]], and its functional comparisons used [[entities/cog-functional-categories]]. [src: ecotype_functional_differentiation]
