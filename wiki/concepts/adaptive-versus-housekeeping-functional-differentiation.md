---
type: "Concept"
description: "Adaptive functions show larger ecotype shifts, but phylogeny dominates genome-wide gene content"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md", "summaries/cog_analysis__REPORT.md", "summaries/ecotype_analysis__REPORT.md"]
---
# Adaptive Functions Differentiate More Strongly Than Housekeeping Functions Among Gene-Content Ecotypes

Within-species gene-content ecotypes are groups of genomes clustered by differences in their accessory gene content, and this report tested whether those groups differ in COG (Clusters of Orthologous Groups) functional profiles. [src: ecotype_functional_differentiation]

The analysis found partial support for stronger differentiation of adaptive functions than housekeeping functions: adaptive COG categories showed a higher significance rate and substantially larger mean effect sizes, although housekeeping categories also differentiated frequently. [src: ecotype_functional_differentiation]

## Key Evidence

The adaptive set comprised categories V (defense), P (inorganic ion transport and metabolism), G (carbohydrate transport and metabolism), E (amino acid transport and metabolism), Q (secondary metabolites biosynthesis, transport, and catabolism), M (cell wall, membrane, and envelope biogenesis), and K (transcription), whereas the housekeeping set comprised J (translation), F (nucleotide transport and metabolism), H (coenzyme transport and metabolism), and C (energy production and conversion). [src: ecotype_functional_differentiation]

Across 257 chi-square or Fisher’s exact tests covering 12 species and 23 COG categories, 170 tests (66.1%) were significant after Benjamini–Hochberg false-discovery-rate correction at q < 0.05. [src: ecotype_functional_differentiation]

Adaptive categories were significant in 67 of 84 tests (79.8%), compared with 33 of 48 tests (68.8%) for housekeeping categories, giving a 1.16x significance-rate ratio. [src: ecotype_functional_differentiation]

The mean effect size was 0.0136 for adaptive categories and 0.0064 for housekeeping categories, giving a 2.13x ratio; a one-sided Mann–Whitney U test gave p = 2.53 x 10^-6. [src: ecotype_functional_differentiation]

These results support the interpretation that ecotypes differ in both adaptive and housekeeping functions, but that their proportional functional shifts are larger for adaptive categories. [src: ecotype_functional_differentiation]

## Functional Pattern

The most frequently differentiated categories included E, significant in 11/12 species (91.7%); V, significant in 11/12 species (91.7%); and G, significant in 10/12 species (83.3%). [src: ecotype_functional_differentiation]

Among the adaptive categories, the reported mean effect sizes were 0.0078 for V, 0.0176 for G, 0.0155 for M, 0.0170 for P, 0.0112 for Q, 0.0141 for K, and 0.0120 for E. [src: ecotype_functional_differentiation]

Housekeeping categories also showed repeated differentiation: J, F, and H were each significant in 8/12 species, while C was significant in 9/12 species. [src: ecotype_functional_differentiation]

The reported mean effect sizes were 0.0051 for J, 0.0041 for F, 0.0069 for H, and 0.0095 for C. [src: ecotype_functional_differentiation]

The contrast therefore concerns effect magnitude more strongly than an absolute separation between adaptive and housekeeping functions, because housekeeping categories differentiated in many species and had a significance rate of 68.8%. [src: ecotype_functional_differentiation]

The broader 32-species COG comparison **supports** this functional partitioning: novel or singleton genes were enriched in defense category V by +2.83%, while core genes were depleted relative to novel or singleton genes in translation J by -4.65%, nucleotide metabolism F by -2.09%, coenzyme metabolism H by -2.06%, amino acid metabolism E by -1.81%, and energy production C by -1.75%. These patterns were observed across 9 phyla and 357,623 genes, but they describe core-versus-novel gene classes rather than within-species ecotype contrasts. [src: cog_analysis]

## Interpretation and Boundaries

The findings are consistent with a model in which ecotype-defining gene-content differences preferentially alter defense, transport, secondary metabolism, carbohydrate use, amino-acid metabolism, and envelope functions, while also affecting core cellular processes. [src: ecotype_functional_differentiation]

The ecotype correlation analysis **refines** this model’s ecological interpretation: across 172 species, the median partial correlation between environmental similarity and gene-content similarity was 0.0025, compared with 0.0143 for phylogeny; phylogeny dominated in 60.5% of species, and environmental effects were non-significant in 156 species (90.7%). [src: ecotype_analysis] This does not negate the larger adaptive-category effect sizes; it suggests the hypothesis that ecological differentiation is concentrated in specific gene subsets rather than governing whole-genome gene-content similarity. [src: ecotype_analysis]

The cross-species result **refines** this model by associating genomic novelty broadly with mobile elements and defense: novel or singleton genes were enriched in COG L (mobile elements) by +10.88%, with 100% consistency across species, and in COG V by +2.83%, with 100% consistency. This is evidence for a conserved core-versus-novel functional architecture, not direct evidence that mobile or defense functions cause ecological differentiation. [src: cog_analysis]

This interpretation remains an association between gene-content clusters and functional-category proportions rather than a direct demonstration that the adaptive categories cause ecological differentiation. [src: ecotype_functional_differentiation]

The analysis identified valid gene-content ecotypes in 12 of 15 sampled species (80%), assigning 1,820 genomes across 12 species spanning 6 phyla, but the sample was drawn from 456 eligible species and may not represent broader phylogenetic or ecological diversity. [src: ecotype_functional_differentiation]

Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated, so unannotated ecotype-specific adaptive genes may have been missed or the observed pattern may be biased toward better-characterized functions. [src: ecotype_functional_differentiation] The new comparison **refines** this caveat rather than replacing it: its COG annotations covered approximately 70% of genes, and unassigned genes may skew its distributions; the differing coverage figures may reflect different datasets or annotation denominators. [src: cog_analysis]

The largest mean effect sizes were 0.0392 for S (unknown function) and 0.0337 for L (replication, recombination, and repair), indicating that the strongest functional differences were not confined to the predefined adaptive set. [src: ecotype_functional_differentiation]

Without within-species phylogenetic controls such as core-genome trees, the analysis cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [src: ecotype_functional_differentiation] The environmental-correlation analysis **supports** retaining this boundary: environmental and host-associated bacteria did not show a significant difference in environmental effects (p=0.66), and AlphaEarth embeddings covered only 28.4% of genomes. [src: ecotype_analysis]

The report’s interpretation should therefore be integrated with [[concepts/ecotype-environment-gene-content]], [[concepts/phylogenetic-confounding-of-pangenome-associations]], [[concepts/ontology-and-category-schema-sensitivity]], and [[concepts/functional-dark-matter]].

The underlying project summaries are [[summaries/ecotype_functional_differentiation__REPORT]], [[summaries/cog_analysis__REPORT]], and [[summaries/ecotype_analysis__REPORT]].

## Open Directions

- Use the 1,820 genome-to-ecotype assignments and core-genome phylogenetic trees with phylogenetically controlled models to test whether the 2.13x adaptive-versus-housekeeping mean-effect-size ratio persists after accounting for shared ancestry. [src: ecotype_functional_differentiation]
- Extend the analysis from the 15-species stratified sample to all 456 eligible species and test whether the 79.8% versus 68.8% significance-rate contrast is consistent across genome-count bins and phylogenetic groups. [src: ecotype_functional_differentiation]
- Combine the ecotype assignments with habitat metadata and multivariate association methods to test whether the larger adaptive-category shifts predict environmental differences rather than only lineage structure. [src: ecotype_functional_differentiation]
- Analyze the 62% of gene clusters lacking COG annotations with AlphaFold or domain analysis to determine whether unannotated ecotype-differentiating genes are enriched for adaptive functions and whether the adaptive-versus-housekeeping contrast changes after their inclusion. [src: ecotype_functional_differentiation]
- Recluster the same genome-by-gene-content data with HDBSCAN and compare category-level significance and effect sizes with the KMeans results to test whether the conclusion depends on spherical-cluster assumptions and the selected value of k. [src: ecotype_functional_differentiation]
- Repeat the ecotype analysis with the broader COG comparison’s mobile-element and defense categories separated from housekeeping categories, testing whether the +10.88% COG L and +2.83% COG V novelty enrichments predict within-species ecotype differentiation. [src: cog_analysis]
- Test the adaptive-category contrast against alternative environmental distances and direct metadata in the 172-species dataset, asking whether the weak whole-genome environmental signal is stronger for specific COG subsets. [src: ecotype_analysis]
