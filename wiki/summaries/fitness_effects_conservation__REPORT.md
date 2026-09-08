---
type: Summary
description: Quantifies how bacterial gene fitness effects relate to pangenome conservation.
doc_type: short
full_text: ../sources/fitness_effects_conservation__REPORT.md
title: Fitness Effects vs Conservation — Quantitative Analysis
sources:
- id: fitness_effects_conservation
  resource: ../sources/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
---
# Fitness Effects vs Conservation — Quantitative Analysis

## Overview

This analysis compares genome-wide mutant fitness measurements from the Fitness Browser with pangenome conservation across approximately 194,000 genes from 43 diverse bacteria. RB-TnSeq (random barcode transposon sequencing) mutant fitness data, essentiality classifications, condition-specific phenotype annotations, and KBase pangenome gene-cluster mappings were integrated to test whether fitness importance predicts whether genes are core, auxiliary, or singleton. [^fitness_effects_conservation]

## Key Findings

### Conservation increases with fitness importance

A clear conservation gradient spans fitness categories: essential genes with no viable mutants were 82% core (n=27,693); genes often sick in more than 10% of experiments were 78% core (n=15,989); mixed genes were 70% core (n=20,739); sometimes-sick genes were 72% core (n=25,201); always-neutral genes were 66% core (n=94,889); and sometimes-beneficial genes were 70% core (n=9,705). [^fitness_effects_conservation]

The same gradient held when genes were binned by their strongest fitness effect: essential genes were 82.2% core, genes with min_fit < -3 were 77.7% core, and genes with min_fit from -1 to 0 were 66.4% core. [^fitness_effects_conservation]

### Breadth of fitness effects predicts conservation

Fitness breadth was positively associated with core status, although the association was weak in magnitude: Spearman rho=0.086, p=8.1e-230. Essential genes were 82% core, genes affecting 20+ experiments were 79% core, genes affecting 6-20 experiments were 73% core, genes affecting 1-5 experiments were 71% core, and genes with 0 experiments were 66% core. [^fitness_effects_conservation]

### Core genes show both stronger costs and stronger benefits

Core genes were more likely than auxiliary genes to show a positive fitness effect when deleted: 24.4% were ever beneficial versus 19.9% of auxiliary genes, with OR=0.77 for auxiliary versus core. This contradicts the expectation that accessory genes are generally costly to carry and suggests that core genes participate more often in trade-off situations, helping under some conditions while imposing costs under others. [^fitness_effects_conservation]

Core and auxiliary genes had distinct fitness-effect distributions, with core genes showing heavier tails in both the negative direction, indicating importance, and the positive direction, indicating burdens when retained or deleted under particular conditions. [^fitness_effects_conservation]

### Condition-specific effects are enriched among core genes

Genes tagged with strong condition-specific effects in the `specificphenotype` annotation were 77.3% core, compared with 70.3% for genes without specific phenotypes; the association had OR=1.78 and p=1.8e-97. This contradicts the expectation that condition-specific genes are predominantly accessory and instead suggests that core genes can have measurable condition-specific effects because they participate in well-characterized pathways. [^fitness_effects_conservation]

### Ephemeral niche genes

A total of 4,450 genes (2.7%) fit the ephemeral-niche pattern of being neutral overall but critical in one condition. These genes were more common among core genes (3.0%) than auxiliary genes (1.7%) or singleton genes (1.6%), suggesting that core genes may have more detectable conditional effects because they participate in more pathways. [^fitness_effects_conservation]

### Novel genes are largely neutral under tested laboratory conditions

Novel singleton genes showed near-zero mean fitness, suggesting that they were largely invisible to the tested laboratory fitness assays rather than systematically beneficial or detrimental. The report notes that this apparent neutrality may also reflect poor transposon coverage. [^fitness_effects_conservation]

### Overall interpretation

Across the full spectrum, gene fitness importance and pangenome conservation were positively correlated: essential genes were 82% core, whereas always-neutral genes were 66% core, a 16-percentage-point gradient spanning approximately 194,000 genes across 43 diverse bacteria. The gradient was statistically robust but conservation was only weakly predicted by fitness importance. [^fitness_effects_conservation]

The combined results indicate that core genes are more functionally active under the tested conditions, showing larger fitness effects in both directions because they are embedded in critical pathways, whereas accessory genes tend to be functionally quieter in laboratory assays. This interpretation is consistent with stronger purifying selection on core genes and with pangenome models in which selection contributes to gene-frequency distributions, but the analysis itself does not establish that selection is the sole driver. [^fitness_effects_conservation]

## Caveats

The fitness measurements are biased toward rich media and standard stresses, so many ecological niches are unrepresented. [^fitness_effects_conservation]

The 16-percentage-point conservation gradient, although statistically robust, means that fitness importance is only a weak predictor of conservation. [^fitness_effects_conservation]

Fitness measurements were based on single-gene knockouts and therefore did not capture epistatic interactions. [^fitness_effects_conservation]

The Fitness Browser covered 43 bacteria, primarily Proteobacteria, limiting generalizability to other bacterial lineages. [^fitness_effects_conservation]

Singleton and novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [^fitness_effects_conservation]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — links essentiality, fitness-effect magnitude, and fitness breadth to pangenome conservation.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — adds evidence that condition-specific and ephemeral-niche fitness effects are enriched among core genes rather than restricted to accessory genes.
- [pangenome-integration](../concepts/pangenome-integration.md) — connects Fitness Browser mutant phenotypes with core, auxiliary, and singleton gene conservation across bacterial pangenomes.
- conservation fitness synthesis — compares fitness importance and conservation across the full gene spectrum, including the core-gene cost-benefit pattern.

[^fitness_effects_conservation]: [fitness effects conservation](../sources/fitness_effects_conservation__REPORT.md)
