---
type: Summary
description: Pan-bacterial ICA modules reveal conserved process-level fitness programs.
doc_type: short
full_text: ../sources/fitness_modules__REPORT.md
title: Pan-bacterial Fitness Modules via Independent Component Analysis
sources:
- id: fitness_modules
  resource: ../sources/fitness_modules__REPORT.md
  title: fitness modules
---
# Pan-bacterial Fitness Modules via Independent Component Analysis

## Overview

This report evaluates independent component analysis (ICA), a statistical decomposition method, for discovering pan-bacterial fitness modules from RB-TnSeq fitness data across 32 organisms. The approach identifies co-regulated biological-process modules rather than assigning precise molecular functions to individual genes; ortholog transfer remains the stronger gene-level function-prediction method. [^fitness_modules]

## Key Findings

- A strict module-membership threshold of |weight| >= 0.3 with a maximum of 50 genes was critical. The initial D'Agostino K-squared approach produced 100-280 genes per module with weak cofitness signal, with 59% enrichment and 1-17x correlation; absolute weight thresholds produced biologically coherent modules with 94% enrichment and 2.8x correlation enrichment. [^fitness_modules]

- Adding PFam domains and lowering the enrichment-overlap threshold from 3 to 2 increased the module annotation rate from 8% to 80%, expanding annotated modules from 92 to 890 and unlocking 7.6x more function predictions. PFam provided the broadest annotation coverage, whereas KEGG KOs were too gene-specific for module-level enrichment. [^fitness_modules]

- ICA decomposition identified 1,116 stable modules across 32 organisms, each with at least 100 experiments. Module sizes had a median range of 7-50 genes; 94.2% of modules showed significantly elevated within-module cofitness by Mann-Whitney U test at p < 0.05; within-module mean |r| was 0.34 versus 0.12 in the background, a 2.8x enrichment; and module genes showed 22.7x genomic-adjacency enrichment, indicating frequent operon co-localization. [^fitness_modules]

- In held-out benchmarking in which 20% of KEGG-annotated genes were withheld, ortholog transfer achieved 95.8% strict precision, 91.2% coverage, and 0.934 F1; domain-based prediction achieved 29.1% precision, 66.6% coverage, and 0.401 F1; Module-ICA achieved <1% strict precision and 23.3% coverage; and cofitness voting achieved <1% strict precision and 73.0% coverage. [^fitness_modules]

- Module-ICA and cofitness had near-zero strict KEGG KO precision because KEGG KO groups are gene-level assignments, averaging approximately 1.2 genes per unique KO; a module with 20 annotated members typically contained 20 different KOs. The report therefore interprets these methods as identifying process-level co-regulation and biological-process context rather than exact molecular-function or KO assignments. [^fitness_modules]

- Cross-organism alignment produced 1.15M bidirectional-best-hit (BBH) pairs across 32 organisms and 13,402 ortholog groups. It identified 156 module families spanning 2+ organisms, including 28 spanning 5+, 7 spanning 10+, and 1 spanning 21 organisms; 145 families had consensus functional labels, representing 93% of the families. [^fitness_modules]

- The analysis generated 6,691 function predictions for hypothetical proteins across the 32 organisms. Of these, 2,455 were family-backed, representing 37% and carrying cross-organism conservation support, while 4,236 were module-only predictions. Predictions used enrichment from KEGG, SEED, TIGRFam, and PFam. [^fitness_modules]

- The cross-organism results provide evidence for conserved fitness regulons across diverse bacterial phyla, including a largest module family spanning 21 organisms. The report presents this as evidence for deeply conserved co-regulation programs, while retaining the distinction between process-level module context and gene-level function identity. [^fitness_modules]

- The approach is complementary to sequence-based methods: Module-ICA is effective for identifying co-regulated gene groups and biological-process modules, whereas ortholog transfer is substantially better for predicting specific molecular functions. [^fitness_modules]

## Caveats

- Module-ICA had near-zero precision for predicting specific KEGG KO assignments because it captures process-level rather than gene-level function. The 6,691 predictions for hypothetical proteins should therefore be read as indicating involvement in a biological process, not possession of a specific KO-defined function. [^fitness_modules]

- Organisms with fewer than approximately 100 experiments produced weaker modules; for example, Caulo with 198 experiments showed only 2.9x correlation enrichment. [^fitness_modules]

- A 40% component cap, meaning components could not exceed 40% of the number of experiments, was necessary to avoid FastICA convergence failures but may cause some modules to be missed in organisms with few experiments. [^fitness_modules]

- PFam-based annotations provided the best coverage but operate at the domain level and may overcount functional associations. [^fitness_modules]

- The strict threshold and annotation results depend on analysis choices: the initial D'Agostino K-squared membership approach produced weakly enriched, oversized modules, while the absolute weight threshold and lower enrichment-overlap threshold produced the reported improvements. [^fitness_modules]

- The report's cross-organism alignment used BBH ortholog pairs and ortholog groups, so the 156 module families and their consensus labels represent aligned conservation patterns rather than proof that every member has an identical molecular function. [^fitness_modules]

## Slots Into

- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — the 1,116 ICA modules, 94.2% cofitness enrichment, 2.8x within-module correlation enrichment, and 22.7x genomic-adjacency enrichment extend the corpus's account of cofitness network structure. [^fitness_modules]
- [gene-essentiality](../concepts/gene-essentiality.md) — the held-out benchmark clarifies that cofitness modules provide process-level context, while ortholog transfer provides stronger gene-level function prediction. [^fitness_modules]
- [pangenome-integration](../concepts/pangenome-integration.md) — the 1.15M BBH pairs, 13,402 ortholog groups, and 156 cross-organism module families connect fitness modules to conserved and hypothetical genes across organisms. [^fitness_modules]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the analysis extends condition-dependent fitness profiling from individual gene associations to independently regulated modules across fitness experiments. [^fitness_modules]

[^fitness_modules]: [fitness modules](../sources/fitness_modules__REPORT.md)
