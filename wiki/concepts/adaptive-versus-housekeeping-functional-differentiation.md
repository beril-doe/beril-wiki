---
type: Concept
description: Ecotype functions differ mainly in adaptive effect magnitude, not significance
  alone.
sources:
- id: ecotype_functional_differentiation
  resource: ../summaries/ecotype_functional_differentiation__REPORT.md
  title: ecotype functional differentiation
- id: cog_analysis
  resource: ../summaries/cog_analysis__REPORT.md
  title: cog analysis
- id: ecotype_analysis
  resource: ../summaries/ecotype_analysis__REPORT.md
  title: ecotype analysis
- id: core_gene_tradeoffs
  resource: ../summaries/core_gene_tradeoffs__REPORT.md
  title: core gene tradeoffs
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
title: Adaptive Functions Differentiate More Strongly Than Housekeeping Functions
  Among Gene-Content Ecotypes
---
# Adaptive Functions Differentiate More Strongly Than Housekeeping Functions Among Gene-Content Ecotypes

Within-species gene-content ecotypes are groups of genomes clustered by accessory gene-content differences. Comparing their COG (Clusters of Orthologous Groups) profiles shows that ecotypes differ in both adaptive and housekeeping functions, with larger proportional shifts in adaptive categories. [^ecotype_functional_differentiation]

This result also illustrates why statistical significance and effect size answer different questions: a statistical test evaluates whether an observation is unlikely under a specified null hypothesis, whereas an effect size describes the magnitude or biological consequence of the difference. [^ecotype_functional_differentiation] The evidence therefore supports non-random functional differentiation, but does not imply that every significant category has a large functional consequence. [^ecotype_functional_differentiation]

## Key Evidence

The adaptive set comprised COG categories V (defense), P (inorganic ion transport and metabolism), G (carbohydrate transport and metabolism), E (amino acid transport and metabolism), Q (secondary metabolites biosynthesis, transport, and catabolism), M (cell wall, membrane, and envelope biogenesis), and K (transcription). The housekeeping set comprised J (translation), F (nucleotide transport and metabolism), H (coenzyme transport and metabolism), and C (energy production and conversion). [^ecotype_functional_differentiation]

Across 257 chi-square or Fisher’s exact tests covering 12 species and 23 COG categories, 170 tests (66.1%) were significant after Benjamini–Hochberg false-discovery-rate (BH-FDR) correction at q < 0.05; all 12 species with valid clusters had at least one significantly differentiated category. [^ecotype_functional_differentiation] Adaptive categories were significant in 67 of 84 tests (79.8%), compared with 33 of 48 tests (68.8%) for housekeeping categories, a 1.16x significance-rate ratio. [^ecotype_functional_differentiation]

The effect-size contrast was stronger: mean effect size was 0.0136 for adaptive categories and 0.0064 for housekeeping categories, a 2.13x ratio. A one-sided Mann–Whitney U test comparing the distributions gave p = 2.53 x 10^-6. [^ecotype_functional_differentiation] Thus, the results support stronger adaptive differentiation in magnitude while refining any claim of absolute adaptive-versus-housekeeping separation: housekeeping categories differentiated frequently and had a 68.8% significance rate. [^ecotype_functional_differentiation]

The most frequently differentiated categories were E, significant in 11/12 species (91.7%); V, significant in 11/12 species (91.7%); and G, significant in 10/12 species (83.3%). [^ecotype_functional_differentiation] Adaptive-category mean effect sizes were 0.0078 for V, 0.0176 for G, 0.0155 for M, 0.0170 for P, 0.0112 for Q, 0.0141 for K, and 0.0120 for E. [^ecotype_functional_differentiation] Housekeeping categories J, F, and H were each significant in 8/12 species, while C was significant in 9/12 species; their mean effect sizes were 0.0051 for J, 0.0041 for F, 0.0069 for H, and 0.0095 for C. [^ecotype_functional_differentiation]

The largest mean effect sizes overall were 0.0392 for S (unknown function) and 0.0337 for L (replication, recombination, and repair), showing that the strongest differences were not confined to the predefined adaptive set. [^ecotype_functional_differentiation] The report characterizes these effect sizes as small and notes that significance may partly reflect the large sample size: 1,820 genomes were assigned across 12 species. [^ecotype_functional_differentiation]

## Interpretation and Boundaries

The findings are consistent with a model in which ecotype-defining gene-content differences preferentially alter defense, transport, secondary metabolism, carbohydrate use, amino-acid metabolism, and envelope functions while also affecting core cellular processes. [^ecotype_functional_differentiation] Widespread significance is therefore not evidence that all differences are large, and the significance-versus-effect-size comparison **supports** reporting both quantities together. [^ecotype_functional_differentiation]

Evidence from laboratory fitness and gene conservation **refines** this contrast: core genes were more burdensome than non-core genes in Protein Metabolism, Motility, and RNA Metabolism, whereas non-core genes were more burdensome in the Cell Wall category. [^core_gene_tradeoffs] The same analysis identified 25,271 condition-dependent trade-off genes and 28,017 genes that were both costly and conserved, suggesting that conservation may preserve functions whose laboratory costs are offset by benefits in other environments. [^core_gene_tradeoffs] Across approximately 194,000 genes from 43 bacteria, essential genes were 82% core whereas always-neutral genes were 66% core, although the association was weak overall. [^fitness_effects_conservation] Strong condition-specific effects were enriched among core genes (77.3% core versus 70.3% without specific phenotypes), and core genes had heavier fitness-effect tails in both negative and positive directions. [^fitness_effects_conservation] These findings support condition-dependent interpretation rather than an assumption that housekeeping-associated or conserved functions are uniformly low-cost or constitutive. [^core_gene_tradeoffs][^fitness_effects_conservation]

The broader 32-species COG comparison **supports** the functional partitioning but **refines** its scope: novel or singleton genes were enriched in defense category V by +2.83%, while core genes were depleted relative to novel or singleton genes in translation J by -4.65%, nucleotide metabolism F by -2.09%, coenzyme metabolism H by -2.06%, amino acid metabolism E by -1.81%, and energy production C by -1.75%. Novel or singleton genes were also enriched in mobile-element category L by +10.88%, with 100% consistency across species, and in V by +2.83%, with 100% consistency. These patterns spanned 9 phyla and 357,623 genes, but describe core-versus-novel classes rather than within-species ecotype contrasts. [^cog_analysis]

The comparison assigned 1,820 genomes across 12 species spanning 6 phyla, with valid gene-content ecotypes in 12 of 15 sampled species (80%); the sample came from 456 eligible species and may not represent broader phylogenetic or ecological diversity. [^ecotype_functional_differentiation] Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated, so the measured effects describe annotated COG space and may miss ecotype-specific adaptive genes. [^ecotype_functional_differentiation] The broader comparison reported approximately 70% gene annotation coverage; this **refines** rather than replaces the caveat, since the differing figures may reflect different datasets or annotation denominators. [^cog_analysis] Singleton neutrality may additionally reflect poor transposon coverage rather than true absence of function. [^fitness_effects_conservation]

The observed association is between gene-content clusters and functional-category proportions, not direct evidence that adaptive categories cause ecological differentiation. [^ecotype_functional_differentiation] Across 172 species, the median partial correlation between environmental similarity and gene-content similarity was 0.0025, compared with 0.0143 for phylogeny; phylogeny dominated in 60.5% of species, and environmental effects were non-significant in 156 species (90.7%). [^ecotype_analysis] This does not negate the larger adaptive-category effect sizes but suggests the hypothesis that ecological differentiation is concentrated in specific gene subsets rather than governing whole-genome gene-content similarity. [^ecotype_analysis] Environmental and host-associated bacteria did not differ significantly in environmental effects (p=0.66), and AlphaEarth embeddings covered only 28.4% of genomes. [^ecotype_analysis]

Without within-species phylogenetic controls such as core-genome trees, the analysis cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [^ecotype_functional_differentiation] A small but significant category shift should therefore not automatically be treated as an independently evolved ecological adaptation; this **supports** linking the interpretation to [ecotype-environment-gene-content](ecotype-environment-gene-content.md), [phylogenetic-confounding-of-pangenome-associations](phylogenetic-confounding-of-pangenome-associations.md), [ontology-and-category-schema-sensitivity](ontology-and-category-schema-sensitivity.md), [functional-dark-matter](functional-dark-matter.md), and [phenotype-database-coverage-bias](phenotype-database-coverage-bias.md). [^ecotype_functional_differentiation]

## Practical Reporting Principle

Comparative analyses should report the number of tests, correction procedure, exact significance threshold, proportion of significant results, effect-size distribution, and sample size together. [^ecotype_functional_differentiation] Here, the combination of 170 significant results out of 257 tests, mean effect sizes of 0.0136 and 0.0064, the 1,820-genome sample, and the stated annotation and phylogenetic limitations is more informative than the significance count alone. [^ecotype_functional_differentiation]

The underlying project summaries are [ecotype_functional_differentiation__REPORT](../summaries/ecotype_functional_differentiation__REPORT.md), [cog_analysis__REPORT](../summaries/cog_analysis__REPORT.md), [ecotype_analysis__REPORT](../summaries/ecotype_analysis__REPORT.md), [core_gene_tradeoffs__REPORT](../summaries/core_gene_tradeoffs__REPORT.md), and [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md).

## Open Directions

- Use the 1,820 genome-to-ecotype assignments and core-genome phylogenies with phylogenetically controlled models, confidence intervals, or bootstrap resampling to test whether the 2.13x adaptive-versus-housekeeping mean-effect-size ratio and the small effects remain stable after accounting for shared ancestry. [^ecotype_functional_differentiation]
- Extend the analysis from the 15-species sample to all 456 eligible species, modeling effect size against genome count and testing whether the 79.8% versus 68.8% significance-rate contrast persists across genome-count bins and phylogenetic groups. [^ecotype_functional_differentiation]
- Combine ecotype assignments with habitat metadata, alternative environmental distances, and multivariate association methods to test whether specific COG shifts predict environmental differences rather than lineage structure. [^ecotype_functional_differentiation][^ecotype_analysis]
- Analyze the 62% of unannotated gene clusters with AlphaFold or domain analysis and test whether their inclusion changes the adaptive-versus-housekeeping effect-size contrast. [^ecotype_functional_differentiation]
- Recluster the same gene-content data with HDBSCAN and compare category-level significance and effect sizes with KMeans to test dependence on spherical-cluster assumptions and the selected value of k. [^ecotype_functional_differentiation]
- Separate mobile-element and defense categories in the broader COG comparison and test whether the +10.88% COG L and +2.83% COG V novelty enrichments predict within-species ecotype differentiation. [^cog_analysis]
- Overlay ecotype-specific COG shifts with condition-resolved fitness measurements, controlling for transposon coverage, to test whether larger adaptive-category effects contain more costly conserved or condition-dependent trade-off genes and whether adaptive and housekeeping categories differ in fitness-effect breadth. [^ecotype_functional_differentiation][^core_gene_tradeoffs][^fitness_effects_conservation]

[^ecotype_functional_differentiation]: [ecotype functional differentiation](../summaries/ecotype_functional_differentiation__REPORT.md)
[^core_gene_tradeoffs]: [core gene tradeoffs](../summaries/core_gene_tradeoffs__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^cog_analysis]: [cog analysis](../summaries/cog_analysis__REPORT.md)
[^ecotype_analysis]: [ecotype analysis](../summaries/ecotype_analysis__REPORT.md)
