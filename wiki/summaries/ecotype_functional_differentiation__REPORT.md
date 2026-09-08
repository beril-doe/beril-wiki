---
type: Summary
description: Multi-species evidence that bacterial ecotypes differ systematically
  in gene functions
doc_type: short
full_text: ../sources/ecotype_functional_differentiation__REPORT.md
title: Ecotype Functional Differentiation
sources:
- id: ecotype_functional_differentiation
  resource: ../sources/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
---
# Ecotype Functional Differentiation

## Overview

This report tests whether within-species gene-content ecotypes differ functionally by clustering bacterial genomes from the BERDL pangenome database and comparing their COG (Clusters of Orthologous Groups) profiles. PCA followed by KMeans identified valid gene-content ecotypes in 12 of 15 sampled species (80%), assigning 1,820 genomes across 12 species spanning 6 phyla; species averaged 3.7 ecotypes, with a range of 2–6 and a mean silhouette score of 0.215 (median: 0.174). The results indicate that ecotype gene-content variation is systematically differentiated in function, especially in adaptive categories, although ecotype boundaries are overlapping and the analysis is limited by sampling, annotation coverage, clustering assumptions, and possible phylogenetic confounding. [^ecotype_functional_differentiation]

## Key Findings

### Gene-content ecotypes are widespread

Valid gene-content ecotypes were detected in 12 of 15 sampled species (80%). The clearest separation occurred in *Erwinia amylovora* (silhouette = 0.468, 2 ecotypes) and *Bacteroides xylanisolvens* (silhouette = 0.366, 6 ecotypes), while the weakest signals occurred in *Staphylococcus simulans* (0.118) and *Streptococcus pseudopneumoniae* (0.131). Valid clusters required at least 2 ecotypes with at least 10 genomes each and at least 20 assigned genomes in total. [^ecotype_functional_differentiation]

The 12 successful species were *Staphylococcus simulans* (78 genomes, 3 ecotypes, 63 assigned), *Enterococcus D gallinarum* (95, 3, 86), *Pectobacterium carotovorum* (57, 2, 57), *Streptococcus pseudopneumoniae* (127, 4, 118), *Bacillus safensis* (120, 3, 117), *Limosilactobacillus fermentum* (118, 4, 107), *Enterobacter cloacae M* (136, 4, 123), *Enterobacter kobei* (252, 2, 252), *Enterobacter cloacae* (216, 5, 210), *Erwinia amylovora* (231, 2, 231), *Bacteroides xylanisolvens* (207, 6, 207), and *Mycobacterium avium* (249, 6, 249). [^ecotype_functional_differentiation]

### Ecotypes show pervasive COG functional differentiation

Across 257 chi-square or Fisher’s exact tests covering 12 species and 23 COG categories, 170 tests (66.1%) were significant after BH-FDR (Benjamini–Hochberg false-discovery-rate) correction at q < 0.05. All 12 species had at least one significantly differentiated COG category, rejecting the null hypothesis that ecotype gene-content variation is functionally random. [^ecotype_functional_differentiation]

The most frequently differentiated categories were E (amino acid metabolism), significant in 11/12 species (91.7%); S (unknown function), 11/12 (91.7%); V (defense), 11/12 (91.7%); and G (carbohydrate metabolism), 10/12 (83.3%). The least frequently differentiated categories were A (RNA processing), 1/9; B (chromatin), 1/8; and Z (cytoskeleton), 2/6. [^ecotype_functional_differentiation]

### Adaptive categories have larger effect sizes than housekeeping categories

The hypothesis that adaptive categories V, P, G, E, Q, M, and K would differentiate more than housekeeping categories J, F, H, and C received partial support. Adaptive categories had a significance rate of 79.8% (67/84), compared with 68.8% (33/48) for housekeeping categories, a 1.16x ratio. Their mean effect size was 0.0136 versus 0.0064 for housekeeping categories, a 2.13x ratio, and the one-sided Mann–Whitney U test gave p = 2.53 x 10^-6. [^ecotype_functional_differentiation]

Housekeeping categories also differentiated in many species, but adaptive categories showed substantially larger proportional shifts between ecotypes. The report interprets this as evidence that ecotypes differ in both adaptive and housekeeping functions, with stronger differentiation in defense, transport, secondary metabolism, and cell-wall functions than in translation, nucleotide metabolism, coenzyme metabolism, and energy production. [^ecotype_functional_differentiation]

### Replication/repair and unknown-function categories drive large differences

S (unknown function) had the largest mean effect size, 0.0392, and was significant in 11/12 species. L (replication, recombination, and repair) had the second-largest mean effect size, 0.0337, and was significant in 9/12 species. Category L includes transposases, integrases, and mobile genetic element machinery, while the large S-category effect indicates that a substantial fraction of ecotype differentiation involves genes whose functions remain uncharacterized. [^ecotype_functional_differentiation]

The remaining reported per-category results were E: 11/12 significant, rate 0.917, mean effect 0.0120; V: 11/12, 0.917, 0.0078; G: 10/12, 0.833, 0.0176; M: 9/12, 0.750, 0.0155; C: 9/12, 0.750, 0.0095; P: 9/12, 0.750, 0.0170; Q: 9/12, 0.750, 0.0112; K: 8/12, 0.667, 0.0141; J: 8/12, 0.667, 0.0051; F: 8/12, 0.667, 0.0041; and H: 8/12, 0.667, 0.0069. [^ecotype_functional_differentiation]

### Sampling and analysis

From 27,702 species in the BERDL pangenome database, 457 had at least 50 genomes and 456 remained eligible after filtering for COG annotation coverage. A stratified random sample of 15 species was drawn, with 5 species per genome-count bin of 50–100, 100–200, and 200–300 genomes; two species experienced transient Spark S3 read errors, and *Limisoma* sp. had insufficient structure for valid clustering. [^ecotype_functional_differentiation]

Clustering used PCA with up to 50 components followed by KMeans, searching k = 2–6 and selecting the best silhouette score. Differential enrichment used 257 chi-square/Fisher’s exact tests with BH-FDR correction at alpha = 0.05. The generated datasets included 456 eligible species, 1,820 genome-to-ecotype assignments, 12 clustering-statistics records, 894 ecotype COG profiles, and 257 COG differentiation-test results. [^ecotype_functional_differentiation]

## Caveats and Limitations

- The analysis covered 12 species from a 15-species sample (80%), out of 456 eligible species; although the stratified sample represented pangenome-size bins, it may not capture broader phylogenetic or ecological diversity. [^ecotype_functional_differentiation]
- KMeans was used because HDBSCAN was unavailable on the cluster; KMeans assumes spherical clusters and requires a selected k, whereas HDBSCAN could better handle variable-density subpopulations. [^ecotype_functional_differentiation]
- Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated; unannotated ecotype-specific adaptive genes may therefore be missed or the results may be biased toward better-characterized functions. [^ecotype_functional_differentiation]
- Without within-species phylogenetic controls such as core-genome trees, the analysis cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [^ecotype_functional_differentiation]
- Effect sizes were small: the largest mean effects were 0.039 for S and 0.034 for L in the report’s rounded narrative, while the detailed table gives 0.0392 and 0.0337; these represent approximately 3–4 percentage-point differences in COG-category proportions, and statistical significance may partly reflect large sample sizes. [^ecotype_functional_differentiation]
- Variable Spark query times of 94s–1642s during heavy cluster usage caused two species to be lost to S3 read errors. [^ecotype_functional_differentiation]

## Future Directions

The report proposes scaling the analysis to all 456 eligible species, overlaying core-genome phylogenetic trees on ecotype assignments, characterizing S-category genes with AlphaFold or domain analysis, integrating habitat metadata to test environmental associations, and comparing the KMeans results with HDBSCAN. [^ecotype_functional_differentiation]

## Slots Into

- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — adds multi-species evidence that within-species gene-content ecotypes are widespread and functionally differentiated, while identifying phylogenetic control and environment metadata as unresolved tests. [^ecotype_functional_differentiation]
- [pangenome-integration](../concepts/pangenome-integration.md) — contributes a BERDL pangenome analysis linking auxiliary gene-content clustering to COG functional differentiation across 12 species. [^ecotype_functional_differentiation]
- [multi-omics-integration](../concepts/multi-omics-integration.md) — identifies unannotated ecotype-differentiating genes as a target for integrating functional annotation and protein-structure evidence. [^ecotype_functional_differentiation]

[^ecotype_functional_differentiation]: [ecotype functional differentiation](../sources/ecotype_functional_differentiation__REPORT.md)
