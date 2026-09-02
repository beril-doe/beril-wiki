---
type: "Concept"
description: "Why conserved bacterial genes can still impose laboratory fitness burdens"
sources: ["summaries/conservation_fitness_synthesis__REPORT.md"]
---
# The Core-Genome Burden Paradox

The core-genome burden paradox is the observation that genes retained broadly across bacterial genomes can nevertheless impose a measurable fitness burden when deleted under laboratory conditions. The paradox arises because conservation suggests long-term value, whereas a higher growth rate after deletion suggests that maintaining the gene is costly in the tested environment. [src: conservation_fitness_synthesis]

The evidence is summarized in [[summaries/conservation_fitness_synthesis__REPORT]] and connects [[concepts/gene-essentiality]], [[concepts/condition-specific-fitness]], and [[concepts/pangenome-integration]]. [src: conservation_fitness_synthesis]

## Key Evidence

Across 194,216 protein-coding genes from 43 diverse bacteria, essential genes were 82% core, whereas genes that were always neutral in the tested experiments were 66% core. [src: conservation_fitness_synthesis] This establishes a modest conservation gradient, but also shows that broad conservation is not equivalent to universal laboratory essentiality. [src: conservation_fitness_synthesis]

Core genes were more likely than accessory genes to be burdensome in laboratory conditions: 24.4% of core genes showed positive fitness when deleted, compared with 19.9% of accessory genes. [src: conservation_fitness_synthesis] Here, positive deletion fitness means that the mutant grew better than the reference strain under the assay conditions. [src: conservation_fitness_synthesis]

Core genes were 1.78x more likely than accessory genes to have strong condition-specific phenotypes and 1.29x more likely to be trade-offs that were important in some conditions but burdensome in others. [src: conservation_fitness_synthesis] These results support [[concepts/condition-specific-fitness]] because the phenotype of a conserved gene depends on the environment in which fitness is measured. [src: conservation_fitness_synthesis]

## Interpreting Conservation and Laboratory Cost Together

Laboratory conditions are an impoverished proxy for environments such as soil, biofilms, and host tissue, so a gene that improves growth when deleted in rich medium may still provide fitness value in nature. [src: conservation_fitness_synthesis] This interpretation suggests the hypothesis that some conserved genes are maintained because their benefits appear in environments not represented by the laboratory assays. [src: conservation_fitness_synthesis]

The joint conservation–fitness matrix classified 28,017 genes as both costly in the laboratory and conserved in the pangenome. [src: conservation_fitness_synthesis] This category is evidence for, rather than a direct measurement of, purifying selection in natural environments because laboratory fitness and pangenome conservation measure different aspects of gene value. [src: conservation_fitness_synthesis]

The same analysis identified 5,526 genes that were costly in the laboratory but dispensable in the pangenome. [src: conservation_fitness_synthesis] These genes are candidates for mobile elements, recently acquired genes, or genes undergoing loss, but their evolutionary status requires further testing. [src: conservation_fitness_synthesis]

This joint interpretation refines [[concepts/pangenome-integration]] by treating conservation and laboratory cost as complementary evidence rather than interpreting either measurement alone. [src: conservation_fitness_synthesis]

## Function-Specific Structure of the Paradox

The burden pattern was not uniform across functional categories. [src: conservation_fitness_synthesis] Motility and chemotaxis genes showed a +7.8pp core-burden excess, RNA metabolism showed a +12.9pp excess, and protein metabolism showed a +6.2pp excess. [src: conservation_fitness_synthesis]

Cell-wall genes showed the opposite pattern: non-core cell-wall genes were more burdensome than core cell-wall genes. [src: conservation_fitness_synthesis] The report interprets the motility and chemotaxis result as consistent with flagella being energetically expensive but useful for chemotaxis in natural environments, and interprets the protein-metabolism result as consistent with ribosomal components being costly but required for rapid growth responses. [src: conservation_fitness_synthesis] These functional differences indicate that the paradox reflects distinct ecological and physiological trade-offs rather than a single genome-wide mechanism. [src: conservation_fitness_synthesis]

## Coordinated Core-Genome Architecture

Independent component analysis (ICA), a method for identifying coordinated fitness modules, identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis] These modules contained 86% core genes compared with an 81.5% baseline, with an odds ratio of 1.46 and p=1.6e-87. [src: conservation_fitness_synthesis] A total of 59% of the modules were more than 90% core genes. [src: conservation_fitness_synthesis]

This organization supports [[concepts/cofitness-network-architecture]] by showing that conservation and burden can be structured in coordinated functional units rather than only in individual essential genes. [src: conservation_fitness_synthesis]

## Limits and Non-Findings

Accessory genes were not systematically more burdensome than core genes; instead, they were less costly in the tested laboratory conditions, contrary to a genome-streamlining hypothesis. [src: conservation_fitness_synthesis]

Strong condition-specific fitness effects were more common among core genes, but condition-specific fitness did not establish niche-specific fitness because the experiments did not directly measure fitness across natural niches. [src: conservation_fitness_synthesis]

Module-family breadth did not predict conservation: families spanning more organisms did not have higher core fractions, with rho=-0.01 and p=0.91. [src: conservation_fitness_synthesis] The report attributes the absence of a gradient in part to an already high baseline that left little room for one. [src: conservation_fitness_synthesis]

## Tensions

The central tension is between laboratory burden and evolutionary retention: deletion can improve growth under tested conditions while the gene remains broadly conserved across genomes. [src: conservation_fitness_synthesis] The available evidence does not resolve this tension by directly measuring natural-environment fitness; it supports the hypothesis that unmeasured environments, ecological interactions, or long-term selection maintain at least some costly core genes. [src: conservation_fitness_synthesis]

## Open Directions

- Use the 5,526 costly-and-dispensable genes, mobile-element annotations, and comparative-genomic analyses to test whether these genes are enriched for mobile elements, recent acquisitions, or signatures of gene loss. [src: conservation_fitness_synthesis]
- Combine core-versus-accessory status, laboratory fitness measurements, and AlphaEarth environmental data with statistical tests to ask whether organisms from more variable environments contain more trade-off genes in their core genomes. [src: conservation_fitness_synthesis]
- Analyze the 43-organism conservation and fitness dataset with cross-species comparative methods to identify gene families that are universally essential across all 43 organisms. [src: conservation_fitness_synthesis]
- Reanalyze the 48 accessory modules containing exclusively flexible-genome co-regulated functions with module-level fitness and conservation data to determine whether they represent coherent adaptive programs. [src: conservation_fitness_synthesis]
- Pair RB-TnSeq measurements with fitness assays in soil, biofilm, and host-associated conditions to test whether laboratory-burdensome conserved genes become beneficial in natural-environment proxies. [src: conservation_fitness_synthesis]
