---
type: "Concept"
description: "Using satellite-derived AlphaEarth embeddings as an independent environment definition and how it agrees with text-based isolation categories; stops at GC-specific mechanisms."
sources: ["summaries/env_embedding_explorer__REPORT.md", "summaries/gc_ecotype_ecology__REPORT.md"]
---
# Independent continuous environment embeddings versus categorical isolation source

This page covers independent continuous environment embeddings versus categorical isolation source. AlphaEarth satellite-derived embeddings give an environment definition that does not use isolation-source text. [src: gc_ecotype_ecology] In the GC ecotype study the two definitions agree on 10 of 17 jointly testable species, but the AlphaEarth signal is mostly orthogonal to isolation category at the level of individual principal components. [src: gc_ecotype_ecology] The evidence comes from two reports and is mostly single-study. See [[entities/alphaearth-environmental-embeddings]] and [[concepts/genome-gc-content-as-an-ecological-signal]].

## Independent, continuous definition of environment

AlphaEarth provided a definition of environment that uses no isolation_source text and is continuous. [src: gc_ecotype_ecology] The report describes AlphaEarth Foundations as a 64-d learned representation of remotely sensed local environment. It captures continuous climate, vegetation and land-cover gradients that only partly overlap with curator-supplied labels such as soil, clinical or marine. [src: gc_ecotype_ecology]

The test covered species with ≥ 30 genomes carrying embeddings: 197 species, 131 of them with ≥ 2 ANI (average nucleotide identity) clusters. [src: gc_ecotype_ecology] For each species, GC residualized by ANI-cluster mean was correlated with the top 5 principal components of the within-cluster residual embeddings. [src: gc_ecotype_ecology]

## Agreement with isolation categories

The AlphaEarth test found 53 significant species of 131 at FDR (false discovery rate) < 0.05, a 40% rate. [src: gc_ecotype_ecology] Of the 17 species testable under both definitions, 10 (59%) were significant in both. [src: gc_ecotype_ecology] The report calls this strong corroboration, and it concludes that two independent definitions converge on similar species sets. [src: gc_ecotype_ecology] Only 17 species were jointly testable, so the 59% rests on a small set.

AlphaEarth-only hits include *Streptococcus pneumoniae* (r = -0.34 over 527 genomes) [src: gc_ecotype_ecology], *Bacteroides xylanisolvens* [src: gc_ecotype_ecology] and the archaeon *Methanosarcina mazei* (r = -0.59). [src: gc_ecotype_ecology] The report suggests the within-species GC × ecology signal is not specific to a bacterial subset. [src: gc_ecotype_ecology] See [[entities/streptococcus-pneumoniae]] and [[entities/bacteroides-xylanisolvens]].

## Where the two definitions diverge

For the 20 top AlphaEarth-significant species, the GC-correlated principal component was decomposed into raw AlphaEarth dimensions and tested by ANOVA against isolation category. [src: gc_ecotype_ecology] The most recurrent top-loading dimensions were A06, A02, A48, A53, A50, A09, A15 and A40, each top in 4–6 of 20 species. [src: gc_ecotype_ecology] Only 5 of 20 (25%) of these principal components also discriminated isolation category. [src: gc_ecotype_ecology] For the other 75%, the report calls the AlphaEarth signal largely orthogonal to categorical isolation source. [src: gc_ecotype_ecology]

## Structure of the embedding space

In the separate embedding-explorer report, many AlphaEarth clusters were dominated by a single environment category. [src: env_embedding_explorer] Rare types (Air, Extreme, Plant) concentrated in a few clusters, while Human gut and Human clinical spread across many. The report suggests this reflects geographic sub-structure. [src: env_embedding_explorer] DBSCAN with eps=0.5 gave 320 clusters, likely too fine-grained, and coarser clustering might match categories better. [src: env_embedding_explorer] Coloring the [[entities/umap]] (uniform manifold approximation and projection) by phylum showed some taxonomic clustering. [src: env_embedding_explorer] This is partly confounded with environment, for example Campylobacterota are predominantly gut-associated. [src: env_embedding_explorer] See [[summaries/env_embedding_explorer__REPORT]] and [[summaries/gc_ecotype_ecology__REPORT]].

## Tensions

- Species-level agreement is 10 of 17 (59%) jointly testable species [src: gc_ecotype_ecology], yet only 5 of 20 (25%) GC-correlated AlphaEarth principal components also discriminate isolation category. [src: gc_ecotype_ecology] These are different units and populations, so they are not directly comparable.
- The AlphaEarth analysis used PCA (principal component analysis) plus Pearson correlation. That captures only linear monotone signals and would miss nonlinear environmental relationships. [src: gc_ecotype_ecology]

## Open Directions

- Repeat the GC test with a nonlinear association measure on the AlphaEarth embeddings, to see whether species missed by PCA plus Pearson appear.
- Enlarge the jointly testable set beyond 17 species, for example by relaxing the genome-count threshold, to test whether 59% agreement holds.
- Re-cluster the embeddings with a coarser DBSCAN setting and compare the clusters to isolation categories, to address the 320-cluster fragmentation.
- Test whether the 75% of principal components that do not discriminate isolation category align with geographic or climate variables.
