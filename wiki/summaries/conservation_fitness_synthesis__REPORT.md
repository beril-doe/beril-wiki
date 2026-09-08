---
type: Summary
description: Synthesis of gene conservation, fitness effects, and bacterial genome
  architecture
doc_type: short
full_text: ../sources/conservation_fitness_synthesis__REPORT.md
title: Gene Conservation, Fitness, and the Architecture of Bacterial Genomes
sources:
- id: conservation_fitness_synthesis
  resource: ../sources/conservation_fitness_synthesis__REPORT.md
  title: conservation fitness synthesis
---
# Gene Conservation, Fitness, and the Architecture of Bacterial Genomes

## Overview

This synthesis integrates RB-TnSeq fitness measurements, a method that assays mutant fitness using random barcode transposon sequencing, with pangenome conservation data across 194,216 protein-coding genes from 43 diverse bacteria, spanning archaea such as Methanococcus, plant pathogens such as Ralstonia, and gut commensals such as Bacteroides. It finds a modest but quantitative conservation gradient: essential genes are 82% core, whereas always-neutral genes are 66% core. [^conservation_fitness_synthesis]

## Key Findings

### Conservation and fitness gradient

More important genes are more conserved, but the effect is modest: even genes with no detectable fitness effect in any experiment are 66% core. The gradient covers 194,216 protein-coding genes across 43 bacteria. [^conservation_fitness_synthesis]

### The core-genome burden paradox

Core genes are more likely to be burdensome in laboratory conditions: 24.4% show positive fitness when deleted, meaning the mutant grows better, compared with 19.9% of accessory genes. Core genes are also 1.78x more likely to have strong condition-specific phenotypes and 1.29x more likely to be trade-offs that are both important and burdensome depending on conditions. These results support [gene-essentiality](../concepts/gene-essentiality.md) and [condition-specific-fitness](../concepts/condition-specific-fitness.md) by indicating that conservation does not identify an inert housekeeping genome. [^conservation_fitness_synthesis]

### Natural selection and the selection-signature matrix

The report resolves the paradox by treating laboratory conditions as an impoverished proxy for nature: a gene that improves fitness when deleted in rich medium may still be essential in soil, biofilms, host tissue, or other natural environments. The 28,017 genes that are both costly in the laboratory and conserved in the pangenome are presented as the strongest evidence for purifying selection in natural environments, whereas the 5,526 genes that are costly and dispensable are candidates for ongoing gene loss. This refines [pangenome-integration](../concepts/pangenome-integration.md) by using conservation and laboratory cost jointly rather than interpreting either measurement alone. [^conservation_fitness_synthesis]

### Coordinated core-genome architecture

Independent component analysis (ICA), a decomposition method for identifying coordinated fitness modules, identified 1,116 co-regulated fitness modules across 32 organisms. These modules were enriched in core genes, with 86% core genes versus an 81.5% baseline, an odds ratio of 1.46, and p=1.6e-87; 59% of modules were more than 90% core genes. This supports [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) by showing that conservation is organized into coordinated functional units rather than only individual essential genes. [^conservation_fitness_synthesis]

### Function-specific burden patterns

The burden paradox is function-specific. Motility and chemotaxis genes show a +7.8pp core-burden excess, RNA metabolism shows a +12.9pp excess, and protein metabolism shows a +6.2pp excess. Cell-wall genes reverse the pattern: non-core cell-wall genes are more burdensome. The report interprets the pattern as consistent with flagella being energetically expensive but useful for chemotaxis in natural environments, and ribosomal components being costly but required for rapid growth responses. [^conservation_fitness_synthesis]

## Caveats and Stated Non-Findings

Module-family breadth did not predict conservation: families spanning more organisms did not have higher core fractions, with rho=-0.01 and p=0.91. The report attributes the absence of a gradient in part to an already high baseline that leaves little room for one. [^conservation_fitness_synthesis]

Accessory genes were not systematically burdensome. Contrary to the streamlining hypothesis, they were less costly than core genes. [^conservation_fitness_synthesis]

Condition-specific fitness did not mean niche-specific fitness. Genes with strong condition-specific effects were more likely to be core rather than accessory, indicating that core genes simply had more detectable effects under the tested conditions. [^conservation_fitness_synthesis]

The findings do not directly establish fitness in natural environments: the laboratory measurements capture the cost of maintaining genes, while the pangenome captures evolutionary pressure to retain them. The costly-and-conserved category is therefore evidence for, rather than a direct measurement of, purifying selection in nature. [^conservation_fitness_synthesis]

## Open Questions

The report identifies five areas for follow-up: characterize the 5,526 costly-and-dispensable genes as possible mobile elements, recently acquired genes, or genes undergoing loss; test whether organisms from more variable environments have more trade-off genes in their core using AlphaEarth environmental data; identify universally essential gene families across all 43 organisms; and characterize the 48 accessory modules that contain co-regulated functions exclusively in the flexible genome. [^conservation_fitness_synthesis]

## Data and Provenance

The synthesis uses Fitness Browser RB-TnSeq mutant-fitness data for approximately 194K genes across 43 bacteria, KBase pangenome gene-cluster conservation data across 27,690 species, upstream per-gene fitness summary statistics, and ICA fitness modules across 32 organisms. It generates no new data files; the figures were produced from cached upstream data. [^conservation_fitness_synthesis]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — the conservation gradient, core-genome burden paradox, and costly-versus-dispensable selection signature connect fitness effects with gene essentiality. [^conservation_fitness_synthesis]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — the 1.78x enrichment of strong condition-specific effects among core genes and the function-specific burden patterns extend interpretation of context-dependent fitness. [^conservation_fitness_synthesis]
- [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) — 1,116 ICA-derived co-regulated modules, their 86% core composition, and the 59% exceeding 90% core genes provide cross-organism architectural evidence. [^conservation_fitness_synthesis]
- [pangenome-integration](../concepts/pangenome-integration.md) — the 28,017 costly-and-conserved and 5,526 costly-and-dispensable genes demonstrate how pangenome conservation can be integrated with laboratory fitness. [^conservation_fitness_synthesis]

[^conservation_fitness_synthesis]: [conservation fitness synthesis](../sources/conservation_fitness_synthesis__REPORT.md)
