---
type: "Summary"
description: "Summary of the project Gene Conservation, Fitness, and the Architecture of Bacterial Genomes."
doc_type: "short"
full_text: "sources/conservation_fitness_synthesis__REPORT.md"
---
# Gene Conservation, Fitness, and the Architecture of Bacterial Genomes

This page summarises the synthesis project "Gene Conservation, Fitness, and the Architecture of Bacterial Genomes". It asked how gene fitness importance in the laboratory relates to conservation in the pangenome. The answer is that more important genes are more conserved, but the effect is modest, and the conserved genome is also the most functionally active part of the genome. [src: conservation_fitness_synthesis] The synthesis reuses cached upstream data and generates no new data files. [src: conservation_fitness_synthesis]

## Key Findings

### Fitness gradient and conservation

Conservation rises with fitness importance, but even genes with no detectable effect are mostly core. [src: conservation_fitness_synthesis] The gradient spans 194,216 protein-coding genes across 43 diverse bacteria, including Methanococcus, Ralstonia and Bacteroides. [src: conservation_fitness_synthesis] Essential genes are 82% core. [src: conservation_fitness_synthesis] Genes with no detectable fitness effect in any experiment are 66% core. [src: conservation_fitness_synthesis] See [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]] and [[concepts/essential-genes-and-core-genome-conservation]].

### Burdens and trade-offs

Core genes are more likely than accessory genes to be burdens. [src: conservation_fitness_synthesis] 24.4% of core genes show positive fitness when deleted, against 19.9% of accessory genes. [src: conservation_fitness_synthesis] The report states that, contrary to the streamlining hypothesis, accessory genes are less costly than core genes, so they are not systematically burdensome. [src: conservation_fitness_synthesis]

Core genes also show more condition-specific effects and more trade-offs:
- Genes with strong specific phenotypes are 1.78x more likely to be core. [src: conservation_fitness_synthesis]
- Genes that are both important and burdensome depending on conditions are 1.29x more likely to be core. [src: conservation_fitness_synthesis]

The report cautions that condition-specific effects do not imply niche specificity. Core genes simply have more detectable effects. [src: conservation_fitness_synthesis] See [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]].

### Function-specific burden

The core-burden excess is function-specific. [src: conservation_fitness_synthesis] Motility and chemotaxis genes show +7.8pp, RNA (ribonucleic acid) metabolism +12.9pp, and protein metabolism +6.2pp. [src: conservation_fitness_synthesis] Cell wall genes reverse the pattern: non-core cell wall genes are more burdensome. [src: conservation_fitness_synthesis] The report explains that flagella are energetically expensive but essential for chemotaxis in natural environments. [src: conservation_fitness_synthesis] It adds that ribosomal components are costly but required for rapid growth responses. [src: conservation_fitness_synthesis] See [[concepts/function-specific-burden-of-core-genes]].

### Costly but conserved genes and gene loss

The report reads laboratory fitness as capturing the cost of maintaining genes. It reads pangenome conservation as capturing the evolutionary pressure to keep them. [src: conservation_fitness_synthesis] It identifies 28,017 genes that are costly in the laboratory and conserved in the pangenome. It calls these its strongest evidence for purifying selection in natural environments. [src: conservation_fitness_synthesis] The 5,526 genes that are costly and dispensable are candidates for ongoing gene loss. [src: conservation_fitness_synthesis] See [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]].

### Co-regulated modules

The core genome contains coordinated functional units, not just individual essential genes. [src: conservation_fitness_synthesis] ICA (independent component analysis) identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis] These modules are enriched in core genes: 86% core versus an 81.5% baseline, with OR (odds ratio) 1.46 and p=1.6e-87. [src: conservation_fitness_synthesis] 59% of modules are >90% core genes. [src: conservation_fitness_synthesis]

Module families spanning more organisms do not have higher core fractions (rho=-0.01, p=0.91). [src: conservation_fitness_synthesis] The report attributes this to the already high baseline: there is no room for a gradient. [src: conservation_fitness_synthesis] See [[concepts/conservation-of-cofitness-modules-in-the-core-genome]] and [[entities/independent-component-analysis-fitness-modules]].

## Data and Methods

The Fitness Browser supplies RB-TnSeq (random barcode transposon sequencing) mutant fitness for ~194K genes across 43 bacteria. [src: conservation_fitness_synthesis] The KBase pangenome supplies gene cluster conservation across 27,690 species. [src: conservation_fitness_synthesis] The report also uses per-gene fitness summary statistics from upstream projects. [src: conservation_fitness_synthesis] The ICA modules come from an upstream fitness-modules project. [src: conservation_fitness_synthesis] All figures are produced from cached upstream data. [src: conservation_fitness_synthesis]

## Caveats and Open Work

- The report states that laboratory conditions are an impoverished proxy for nature. [src: conservation_fitness_synthesis] A gene with positive fitness when deleted in rich media may be essential in soil, biofilm, host tissue or other natural conditions. [src: conservation_fitness_synthesis]
- The identities of the 5,526 costly and dispensable genes are open. They may be mobile elements or recently acquired genes on the way out. [src: conservation_fitness_synthesis]
- It is open whether organisms from more variable environments have more core trade-off genes. The report proposes connecting laboratory fitness to AlphaEarth environmental data. [src: conservation_fitness_synthesis]
- It is open whether universally essential gene families exist across all 43 organisms. [src: conservation_fitness_synthesis]
- The co-regulated functions of the 48 accessory modules are unknown. [src: conservation_fitness_synthesis]

## Slots Into

- [[concepts/gene-fitness-importance-as-a-predictor-of-pangenome-conservation]]: essential genes are 82% core and neutral genes 66% core, a modest gradient. [src: conservation_fitness_synthesis]
- [[concepts/costly-but-conserved-genes-laboratory-burden-versus-conservation]]: 28,017 genes are costly yet conserved. [src: conservation_fitness_synthesis]
- [[concepts/function-specific-burden-of-core-genes]]: the burden excess differs by function. [src: conservation_fitness_synthesis]
- [[concepts/condition-dependent-fitness-trade-offs-of-core-versus-accessory-genes]]: core genes are more likely to be trade-offs. [src: conservation_fitness_synthesis]
- [[concepts/conservation-of-cofitness-modules-in-the-core-genome]]: modules are enriched in core genes. [src: conservation_fitness_synthesis]
