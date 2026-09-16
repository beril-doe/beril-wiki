---
type: "Summary"
description: "Summary of a synthesis that combines RB-TnSeq fitness and pangenome conservation across 43 organisms, covering a modest conservation gradient, a core-genome burden paradox, selection signatures, and core-enriched fitness modules."
doc_type: "short"
full_text: "sources/conservation_fitness_synthesis__REPORT.md"
---
# Gene Conservation, Fitness, and the Architecture of Bacterial Genomes

## Overview

This synthesis integrates RB-TnSeq fitness measurements, a method that assays mutant fitness using random barcode transposon sequencing, with pangenome conservation data across 194,216 protein-coding genes from 43 diverse organisms (the report calls them bacteria, although its examples include archaea), spanning archaea such as Methanococcus, plant pathogens such as Ralstonia, and gut commensals such as Bacteroides. It finds a modest but quantitative conservation gradient: essential genes are 82% core, whereas always-neutral genes are 66% core. [src: conservation_fitness_synthesis]

## Key Findings

### Conservation and fitness gradient

More important genes are more conserved, but the effect is modest: even genes with no detectable fitness effect in any experiment are 66% core. The gradient covers 194,216 protein-coding genes across 43 organisms and is illustrated in the report's `figures/fitness_conservation_gradient.png`. [src: conservation_fitness_synthesis]

### The core-genome burden paradox

Core genes are more likely to be burdensome in laboratory conditions: 24.4% show positive fitness when deleted, meaning the mutant grows better, compared with 19.9% of accessory genes. Genes with strong condition-specific phenotypes are also 1.78x more likely to be core, and trade-off genes, which are important or burdensome depending on conditions, are 1.29x more likely to be core. These results support [[concepts/gene-essentiality]] and [[concepts/condition-specific-fitness]] by indicating that conservation does not identify an inert housekeeping genome. [src: conservation_fitness_synthesis]

### Natural selection and the selection-signature matrix

The report resolves the paradox by treating laboratory conditions as an impoverished proxy for nature: a gene that improves fitness when deleted in rich medium may still be essential in soil, biofilms, host tissue, or other natural environments. The report proposes this explanation; it did not measure it in the field. The 28,017 genes that are both costly in the laboratory and conserved in the pangenome are presented as the strongest evidence for purifying selection in natural environments, whereas the 5,526 genes that are costly and dispensable are candidates for ongoing gene loss. The selection-signature matrix is illustrated in `figures/selection_signature.png`. This refines [[concepts/pangenome-integration]] by using conservation and laboratory cost jointly rather than interpreting either measurement alone. [src: conservation_fitness_synthesis]

### Coordinated core-genome architecture

Independent component analysis (ICA), a decomposition method for identifying coordinated fitness modules, identified 1,116 co-regulated fitness modules across 32 organisms. These modules were enriched in core genes, with 86% core genes versus an 81.5% baseline, an odds ratio of 1.46, and p=1.6e-87; 59% of modules were more than 90% core genes. The ICA fitness-module dataset used here comprises these 1,116 co-regulated modules across 32 organisms. The core-genome architecture is illustrated in `figures/core_genome_active.png`. This supports [[concepts/cofitness-network-architecture]] by showing that conservation is organized into coordinated functional units rather than only individual essential genes. [src: conservation_fitness_synthesis]

### Function-specific burden patterns

The burden paradox is function-specific. Motility and chemotaxis genes show a +7.8pp core-burden excess, RNA metabolism shows a +12.9pp excess, and protein metabolism shows a +6.2pp excess. Cell-wall genes reverse the pattern: non-core cell-wall genes are more burdensome. The report interprets the pattern as consistent with flagella being energetically expensive but useful for chemotaxis in natural environments, and ribosomal components being costly but required for rapid growth responses. The synthesis offers these explanations as interpretations and does not measure them directly. [src: conservation_fitness_synthesis]

## Caveats and Stated Non-Findings

Module-family breadth did not predict conservation: families spanning more organisms did not have higher core fractions, with rho=-0.01 and p=0.91. The report attributes the absence of a gradient in part to an already high baseline that leaves little room for one. [src: conservation_fitness_synthesis]

Accessory genes were not systematically burdensome. Contrary to the streamlining hypothesis, they were less costly than core genes. [src: conservation_fitness_synthesis]

Condition-specific fitness did not mean niche-specific fitness. Genes with strong condition-specific effects were more likely to be core rather than accessory, indicating that core genes simply had more detectable effects under the tested conditions. [src: conservation_fitness_synthesis]

The findings do not directly establish fitness in natural environments: the laboratory measurements capture the cost of maintaining genes, while the pangenome captures evolutionary pressure to retain them. The costly-and-conserved category is therefore evidence for, rather than a direct measurement of, purifying selection in nature. [src: conservation_fitness_synthesis]

## Open Questions

The report poses several open questions for follow-up: characterize the 5,526 costly-and-dispensable genes as possible mobile elements, recently acquired genes, or genes undergoing loss; test whether organisms from more variable environments have more trade-off genes in their core using AlphaEarth environmental data; identify universally essential gene families across all 43 organisms; and characterize the 48 accessory modules that contain co-regulated functions exclusively in the flexible genome. [src: conservation_fitness_synthesis]

## Data and Provenance

The synthesis uses Fitness Browser RB-TnSeq mutant-fitness data for approximately 194K genes across 43 organisms (described in the report as bacteria), KBase pangenome gene-cluster conservation data across 27,690 species, upstream per-gene fitness summary statistics, and ICA fitness modules across 32 organisms. It generates no new data files; the figures were produced from cached upstream data. [src: conservation_fitness_synthesis]

## Slots Into

- [[concepts/gene-essentiality]] — the conservation gradient, core-genome burden paradox, and costly-versus-dispensable selection signature connect fitness effects with gene essentiality. [src: conservation_fitness_synthesis]
- [[concepts/condition-specific-fitness]] — genes with strong condition-specific effects being 1.78x more likely to be core, together with the function-specific burden patterns, extend interpretation of context-dependent fitness. [src: conservation_fitness_synthesis]
- [[concepts/cofitness-network-architecture]] — 1,116 ICA-derived co-regulated modules, their 86% core composition, and the 59% exceeding 90% core genes provide cross-organism architectural evidence. [src: conservation_fitness_synthesis]
- [[concepts/pangenome-integration]] — the 28,017 costly-and-conserved and 5,526 costly-and-dispensable genes demonstrate how pangenome conservation can be integrated with laboratory fitness. [src: conservation_fitness_synthesis]
- [[concepts/pangenome-conservation-fitness-decoupling]] — the modest gradient from essential genes (82% core) to always-neutral genes (66% core) shows that conservation only weakly tracks how important a gene is to laboratory fitness. [src: conservation_fitness_synthesis]
- [[concepts/laboratory-fitness-versus-natural-selection]] — the report's caveat that laboratory conditions are an impoverished proxy for nature frames its selection-signature interpretation. [src: conservation_fitness_synthesis]
- [[concepts/core-genome-burden-paradox]] — deleting core genes improves fitness more often than deleting accessory genes (24.4% versus 19.9%), with function-specific excesses and a cell-wall reversal. [src: conservation_fitness_synthesis]
- [[concepts/condition-dependent-gene-tradeoffs]] — genes with strong condition-specific phenotypes are 1.78x more likely to be core, and trade-off genes are 1.29x more likely to be core. [src: conservation_fitness_synthesis]
- [[concepts/costly-dispensable-gene-loss]] — the 5,526 costly-and-dispensable genes are posed as candidates for ongoing gene loss; their identities remain unresolved. [src: conservation_fitness_synthesis]
- [[concepts/module-level-coinheritance]] — 1,116 ICA modules are core-enriched (OR=1.46, p=1.6e-87). Module-family breadth did not predict core fraction (rho=-0.01, p=0.91), and 48 accessory modules remain uncharacterized. [src: conservation_fitness_synthesis]
- [[concepts/pangenome-core-boundary-and-clade-size-bias]] — the report attributes the null breadth-conservation result to an already high baseline core fraction. [src: conservation_fitness_synthesis]
- [[concepts/lab-field-fitness-concordance]] — the report proposes linking laboratory fitness to AlphaEarth environmental data to test whether organisms from variable environments carry more trade-off genes in their core. [src: conservation_fitness_synthesis]
