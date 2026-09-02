---
type: "Concept"
description: "Why laboratory fitness measurements only partially reflect natural selection"
sources: ["summaries/conservation_fitness_synthesis__REPORT.md"]
---
# Laboratory Fitness as an Imperfect Proxy for Natural Selection

Laboratory fitness measurements quantify how mutations affect growth under tested experimental conditions, whereas natural selection acts across environments such as soil, biofilms, host tissue, and other settings that are not represented by a single laboratory regime. [src: conservation_fitness_synthesis] This distinction is central to interpreting [[summaries/conservation_fitness_synthesis__REPORT]] and connects [[concepts/condition-specific-fitness]], [[concepts/gene-essentiality]], and [[concepts/pangenome-integration]].

## The Proxy Problem

Random barcode transposon sequencing (RB-TnSeq), a method that estimates mutant fitness from barcode abundance after pooled growth, measures the cost or benefit of gene disruption under particular laboratory conditions. [src: conservation_fitness_synthesis] Pangenome conservation instead records whether genes are retained across genomes and therefore reflects evolutionary pressures accumulated across environments and histories rather than a direct measurement of natural-environment fitness. [src: conservation_fitness_synthesis] The two measurements are consequently complementary but not interchangeable. [src: conservation_fitness_synthesis]

The synthesis integrated RB-TnSeq fitness measurements with pangenome conservation data for 194,216 protein-coding genes from 43 diverse bacteria. [src: conservation_fitness_synthesis] Essential genes were 82% core, while genes that were always neutral in the available experiments were still 66% core, establishing a modest quantitative conservation gradient rather than a sharp division between conserved important genes and unconserved neutral genes. [src: conservation_fitness_synthesis] This **supports** [[concepts/gene-essentiality]] while showing that laboratory neutrality does not imply evolutionary dispensability. [src: conservation_fitness_synthesis]

## The Core-Genome Burden Paradox

Core genes were more likely than accessory genes to be burdensome under laboratory conditions: 24.4% of core genes showed positive fitness when deleted, compared with 19.9% of accessory genes. [src: conservation_fitness_synthesis] A positive deletion-fitness value means that the mutant grew better under the tested laboratory conditions, so the intact gene imposed a measurable burden in that context. [src: conservation_fitness_synthesis] Core genes were also 1.78x more likely to have strong condition-specific phenotypes and 1.29x more likely to be trade-offs that were important in some conditions but burdensome in others. [src: conservation_fitness_synthesis]

These findings **refine** [[concepts/condition-specific-fitness]]: conservation is not evidence that a gene is inert or universally beneficial in the laboratory, and laboratory burden is not evidence that the gene lacks value in nature. [src: conservation_fitness_synthesis] The apparent paradox is therefore expected if genes retained by natural selection can carry costs in nutrient-rich or otherwise simplified laboratory environments while providing benefits in environments that were not assayed. [src: conservation_fitness_synthesis]

## Joint Interpretation of Fitness and Conservation

The 28,017 genes that were both costly in the laboratory and conserved in the pangenome provide the strongest evidence in this synthesis for purifying selection in natural environments, but they do not directly measure fitness in those environments. [src: conservation_fitness_synthesis] The 5,526 genes that were costly and dispensable are candidates for ongoing gene loss, although the report identifies them as candidates rather than establishing that loss is occurring. [src: conservation_fitness_synthesis] This joint classification **supports** [[concepts/pangenome-integration]] by using conservation and laboratory cost together instead of treating either measurement as sufficient on its own. [src: conservation_fitness_synthesis]

The evidence is strongest as an inference when laboratory cost and broad conservation coincide, because the two data types point in different directions under the laboratory proxy: deletion improves measured growth, yet the gene remains widely retained. [src: conservation_fitness_synthesis] The inference remains indirect because the dataset does not directly measure selection in soil, biofilms, host tissue, or other natural environments. [src: conservation_fitness_synthesis]

## Functional and Network-Level Structure

The proxy limitation is not restricted to isolated genes. Independent component analysis (ICA), a decomposition method for identifying coordinated fitness modules, identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis] These modules contained 86% core genes versus an 81.5% baseline, with an odds ratio of 1.46 and p=1.6e-87, and 59% of modules were more than 90% core genes. [src: conservation_fitness_synthesis] This **supports** [[concepts/cofitness-network-architecture]] by indicating that conserved architecture is organized into coordinated functional units whose laboratory phenotypes may depend on conditions and interactions among genes. [src: conservation_fitness_synthesis]

The burden pattern was function-specific: motility and chemotaxis genes showed a +7.8pp core-burden excess, RNA metabolism showed a +12.9pp excess, and protein metabolism showed a +6.2pp excess. [src: conservation_fitness_synthesis] Cell-wall genes showed the reverse pattern, with non-core cell-wall genes more burdensome under the tested conditions. [src: conservation_fitness_synthesis] The report interprets these patterns as consistent with flagella being energetically expensive but useful for chemotaxis in natural environments, and with ribosomal components being costly but required for rapid growth responses. [src: conservation_fitness_synthesis] These interpretations are hypotheses about environmental value rather than direct measurements of natural selection. [src: conservation_fitness_synthesis]

## Limits on Generalization

Condition-specific fitness did not establish niche-specific fitness: genes with strong condition-specific effects were more likely to be core rather than accessory, which the report interpreted as evidence that core genes simply had more detectable effects under the tested conditions. [src: conservation_fitness_synthesis] Module-family breadth also did not predict conservation, with rho=-0.01 and p=0.91. [src: conservation_fitness_synthesis] The report attributed that null result partly to an already high baseline of conservation that left little room for a gradient. [src: conservation_fitness_synthesis]

Accessory genes were not systematically burdensome, contrary to the streamlining hypothesis. [src: conservation_fitness_synthesis] This result **contradicts** a simple expectation that flexible genes are generally costly to maintain, while leaving open the possibility that costs depend on environment, genetic background, or the particular accessory functions represented in the dataset. [src: conservation_fitness_synthesis]

## Tensions

The central tension is between laboratory burden and evolutionary retention: 24.4% of core genes were burdensome when deleted in the laboratory, yet core genes were more conserved than always-neutral genes, which were 66% core. [src: conservation_fitness_synthesis] The synthesis resolves this tension as an environmental mismatch rather than as evidence that either measurement is invalid: laboratory conditions measure a restricted component of fitness, while pangenome conservation integrates selection across broader evolutionary contexts. [src: conservation_fitness_synthesis]

A second tension concerns condition specificity: core genes were 1.78x more likely to show strong condition-specific phenotypes, but the report did not find that condition-specific fitness was equivalent to niche-specific fitness. [src: conservation_fitness_synthesis] Resolving that distinction requires environmental experiments or validated environmental proxies rather than further interpretation of laboratory measurements alone. [src: conservation_fitness_synthesis]

## Open Directions

- Combine the 5,526 costly-and-dispensable genes with mobile-element annotations and genome-loss histories, then test whether they show signatures of recent acquisition or ongoing loss. [src: conservation_fitness_synthesis]
- Link core trade-off genes to AlphaEarth environmental data and use comparative analysis to ask whether organisms from more variable environments have more trade-off genes in their core. [src: conservation_fitness_synthesis]
- Compare RB-TnSeq results across the 43 organisms and identify gene families that are essential in every organism, then test whether their conservation persists across additional environmental conditions. [src: conservation_fitness_synthesis]
- Characterize the 48 accessory modules containing co-regulated functions exclusively in the flexible genome, then test their fitness across environmental conditions and genetic backgrounds. [src: conservation_fitness_synthesis]
- Pair direct fitness assays in soil, biofilms, or host-associated conditions with pangenome conservation to determine which laboratory-burdened core genes provide context-dependent natural-environment benefits. [src: conservation_fitness_synthesis]
