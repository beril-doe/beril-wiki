---
type: "Concept"
description: "Why statistical significance must be interpreted alongside functional effect size"
sources: ["summaries/ecotype_functional_differentiation__REPORT.md"]
---
# Statistical Significance Versus Effect Size

Large comparative datasets can produce statistically significant results even when the associated functional differences are small, so significance and effect magnitude answer different questions. [src: ecotype_functional_differentiation]

## Core Idea

A statistical test evaluates whether the observed difference is unlikely under a specified null hypothesis, whereas an effect size describes how large or biologically consequential that difference is. [src: ecotype_functional_differentiation]

In the [[summaries/ecotype_functional_differentiation__REPORT]], within-species gene-content ecotypes were compared across 23 COG categories using 257 chi-square or Fisher’s exact tests, with BH-FDR (Benjamini–Hochberg false-discovery-rate) correction. [src: ecotype_functional_differentiation]

The analysis found 170 significant tests, corresponding to 66.1%, at q < 0.05, and all 12 species with valid clusters had at least one significantly differentiated COG category. [src: ecotype_functional_differentiation]

These results support the conclusion that ecotype gene-content variation was not functionally random, but statistical significance alone does not establish that the differences were large. [src: ecotype_functional_differentiation]

## Evidence for Small but Detectable Differences

The largest reported mean effect sizes were 0.0392 for COG category S, which represents unknown function, and 0.0337 for category L, which represents replication, recombination, and repair. [src: ecotype_functional_differentiation]

The report states that these effect sizes were small and that significance may partly reflect large sample sizes. [src: ecotype_functional_differentiation]

The underlying comparison assigned 1,820 genomes across 12 species, providing a comparatively large set of genome-level observations for detecting category-proportion differences. [src: ecotype_functional_differentiation]

This pattern strengthens [[concepts/ecotype-environment-gene-content]] by showing that widespread ecotype differentiation can be statistically reproducible while its per-category magnitude remains modest. [src: ecotype_functional_differentiation]

## Adaptive Versus Housekeeping Categories

The comparison between [[concepts/adaptive-versus-housekeeping-functional-differentiation]] categories illustrates why significance rates and effect sizes should be reported together. [src: ecotype_functional_differentiation]

Adaptive categories V, P, G, E, Q, M, and K were significant in 67 of 84 tests, or 79.8%, whereas housekeeping categories J, F, H, and C were significant in 33 of 48 tests, or 68.8%. [src: ecotype_functional_differentiation]

The significance-rate ratio was 1.16x, while the mean effect size was 0.0136 for adaptive categories and 0.0064 for housekeeping categories, a 2.13x ratio. [src: ecotype_functional_differentiation]

A one-sided Mann–Whitney U test comparing the effect-size distributions gave p = 2.53 x 10^-6, supporting a difference in effect-size distributions between the category groups. [src: ecotype_functional_differentiation]

The unequal ratios show that adaptive categories differed not only in how often they reached statistical significance, but also in the magnitude of their proportional shifts. [src: ecotype_functional_differentiation]

## Interpretation and Limits

The report’s findings should be interpreted with [[concepts/statistical-significance-versus-effect-size]] rather than as evidence that every significant category has a large functional consequence. [src: ecotype_functional_differentiation]

Approximately 38% of gene clusters had COG annotations, leaving 62% unannotated, so the measured effect sizes describe annotated COG space rather than all ecotype-specific genes. [src: ecotype_functional_differentiation]

The analysis used 12 species from a 15-species sample drawn from 456 eligible species, so the observed significance and effect-size distributions may not represent the full eligible dataset. [src: ecotype_functional_differentiation]

Without within-species phylogenetic controls such as core-genome trees, the analysis cannot distinguish ecological adaptation from phylogenetic or demographic substructure. [src: ecotype_functional_differentiation]

This limitation connects the interpretation to [[concepts/phenotype-database-coverage-bias]] and means that a small but significant category shift should not automatically be treated as an independently evolved ecological adaptation. [src: ecotype_functional_differentiation]

## Practical Reporting Principle

Comparative analyses should report the number of tests, correction procedure, exact significance threshold, proportion of significant results, effect-size distribution, and sample size together. [src: ecotype_functional_differentiation]

For this dataset, the combination of 170 significant results out of 257 tests, mean effect sizes of 0.0136 and 0.0064 for the two category groups, and the reported limitations gives a more informative interpretation than the significance count alone. [src: ecotype_functional_differentiation]

## Open Directions

- Use the existing 1,820 genome-to-ecotype assignments and 257 COG differentiation-test results with confidence intervals or bootstrap resampling to determine how stable the small effect sizes are across genomes and species. [src: ecotype_functional_differentiation]
- Extend the analysis from the 15-species sample to all 456 eligible species and model effect size against genome count to test how comparative dataset size influences detection of significant functional differences. [src: ecotype_functional_differentiation]
- Overlay within-species core-genome phylogenies on ecotype assignments and repeat the category tests with phylogenetic controls to test whether significant small effects persist after accounting for phylogenetic or demographic structure. [src: ecotype_functional_differentiation]
- Integrate the 62% of gene clusters lacking COG annotations with AlphaFold or domain analysis to test whether unannotated genes contain additional ecotype-specific effects that are absent from the current effect-size estimates. [src: ecotype_functional_differentiation]
