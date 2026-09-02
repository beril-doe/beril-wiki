---
type: "Method"
description: "Statistical method for rank-based comparisons of cofitness and pathway completeness"
sources: ["summaries/fitness_modules__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Mann-Whitney U Test

## What this entity is

The canonical name is Mann-Whitney U test, a statistical method used in the report to test whether within-module cofitness was elevated relative to background cofitness. [src: fitness_modules]

Known alias: Wilcoxon rank-sum test. [src: fitness_modules]

No stable external identifier is specified in the source document. [src: fitness_modules]

## Key facts from fitness_modules

The report identified 1,116 stable independent-component-analysis modules across 32 organisms, with each organism represented by at least 100 experiments. [src: fitness_modules]

The Mann-Whitney U test found significantly elevated within-module cofitness in 94.2% of the modules at p < 0.05. [src: fitness_modules]

Across the modules, within-module mean absolute correlation was 0.34 versus 0.12 in the background, corresponding to a 2.8x correlation enrichment. [src: fitness_modules]

These results support the interpretation that the ICA modules capture biologically coherent co-regulated groups, while the test evaluates enrichment of cofitness rather than assigning precise gene-level molecular functions. [src: fitness_modules]

## Application in pseudomonas_carbon_ecology

The new report **refines** the method’s documented use by applying it to pathway-completeness distributions: 43 of 62 carbon pathways differed between the *Pseudomonas* s.s. and *Pseudomonas_E* groups after Benjamini-Hochberg false-discovery-rate correction at q < 0.05. [src: pseudomonas_carbon_ecology] This extends the test from cofitness enrichment to nonparametric comparison of predicted metabolic capabilities, rather than contradicting its earlier use. [src: pseudomonas_carbon_ecology]

The cofitness-module findings extend [[concepts/cofitness-network-architecture]], and the source summary is [[summaries/fitness_modules__REPORT]]. [src: fitness_modules] The carbon-pathway application is summarized in [[summaries/pseudomonas_carbon_ecology__REPORT]]. [src: pseudomonas_carbon_ecology]

## Related pages

- [[concepts/cofitness-network-architecture]] — cross-project synthesis of cofitness network structure.
- [[concepts/gene-essentiality]] — distinguishes process-level module context from gene-level function prediction.
- [[summaries/fitness_modules__REPORT]] — summary of the source report.
- [[summaries/pseudomonas_carbon_ecology__REPORT]] — application to carbon-pathway comparisons.
