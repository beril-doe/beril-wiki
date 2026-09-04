---
type: "Concept"
description: "How conserved core genes can remain costly under laboratory conditions"
sources: ["summaries/conservation_fitness_synthesis__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md", "summaries/conservation_vs_fitness__REPORT.md"]
---
# The Core-Genome Burden Paradox

The core-genome burden paradox is the observation that genes retained broadly across bacterial genomes can nevertheless impose a measurable fitness burden when deleted under laboratory conditions. The paradox arises because conservation suggests long-term value, whereas a higher growth rate after deletion suggests that maintaining the gene is costly in the tested environment. [src: conservation_fitness_synthesis]

The evidence is summarized in [[summaries/conservation_fitness_synthesis__REPORT]], [[summaries/core_gene_tradeoffs__REPORT]], and the independent analyses [[summaries/fitness_effects_conservation__REPORT]] and [[summaries/conservation_vs_fitness__REPORT]]. It connects [[concepts/gene-essentiality]], [[concepts/condition-specific-fitness]], and [[concepts/pangenome-integration]]. [src: conservation_fitness_synthesis, core_gene_tradeoffs]

## Key Evidence

Across 194,216 protein-coding genes from 43 diverse bacteria, essential genes were 82% core, whereas genes that were always neutral in the tested experiments were 66% core. [src: conservation_fitness_synthesis] This establishes a modest conservation gradient, but also shows that broad conservation is not equivalent to universal laboratory essentiality. [src: conservation_fitness_synthesis] The independent analysis **supports** this gradient: essential genes were 82% core, compared with 66% for always-neutral genes, while genes affecting 20+ experiments were 79% core and genes affecting 1–5 experiments were 71% core. [src: fitness_effects_conservation] The breadth association was statistically strong but weak in magnitude (Spearman rho=0.086, p=8.1e-230), refining the interpretation that fitness importance is informative but only a weak predictor of conservation. [src: fitness_effects_conservation]

The new 33-organism Fitness Browser–pangenome linkage **supports** the direction of this conservation gradient while **refining** its scope: essential genes were 86.1% core versus 81.2% for non-essential genes, with a median odds ratio of 1.56, and 18 of 33 organisms showed significant enrichment after Benjamini-Hochberg false discovery rate correction (BH-FDR, a multiple-testing correction; q < 0.05). [src: conservation_vs_fitness]

This estimate comes from a different cohort and essentiality definition, so it should not be treated as a replacement or numerical reconciliation of the 82% versus 66% comparison. [src: conservation_vs_fitness, conservation_fitness_synthesis, fitness_effects_conservation]

Core genes were more likely than accessory genes to be burdensome in laboratory conditions: 24.4% of core genes showed positive fitness when deleted, compared with 19.9% of accessory genes. [src: conservation_fitness_synthesis] Here, positive deletion fitness means that the mutant grew better than the reference strain under the assay conditions. [src: conservation_fitness_synthesis] The function-resolved analysis **supports** this aggregate result but **refines** it: core genes were more burdensome in Protein Metabolism, Motility, and RNA Metabolism, with core-minus-non-core burden differences of +6.2, +7.8, and +12.9 percentage points, respectively, whereas Cell Wall genes showed the reverse pattern, with a difference of -14.1 percentage points. [src: core_gene_tradeoffs] The independent analysis likewise **supports** a broader two-sided effect structure: core genes had heavier fitness-effect tails in both the negative and positive directions, rather than being uniformly beneficial or costly to retain. [src: fitness_effects_conservation]

Core genes were 1.78x more likely than accessory genes to have strong condition-specific phenotypes and 1.29x more likely to be trade-offs that were important in some conditions but burdensome in others. [src: conservation_fitness_synthesis] The trade-off analysis **supports** this enrichment: it identified 25,271 true trade-off genes, 17.8% of the genes examined, with an odds ratio of 1.29 and p=1.2e-44 for core-versus-non-core enrichment. [src: core_gene_tradeoffs] These results support [[concepts/condition-specific-fitness]] because the phenotype of a conserved gene depends on the environment in which fitness is measured. [src: conservation_fitness_synthesis] The independent analysis further **supports** this interpretation: genes with strong condition-specific annotations were 77.3% core versus 70.3% for genes without such annotations, with OR=1.78 and p=1.8e-97. [src: fitness_effects_conservation]

The new analysis **refines** the essentiality side of this pattern by separating essential-core, essential-auxiliary, and essential-unmapped genes: essential-core genes were the most enzyme-rich and best annotated, whereas essential-auxiliary genes were 38.2% hypothetical and essential-unmapped genes were 44.7% hypothetical. [src: conservation_vs_fitness] Thus, conservation-linked essentiality does not imply that every essential function belongs to a well-characterized core gene; poorly annotated essential genes remain part of the burden–conservation problem. [src: conservation_vs_fitness]

## Interpreting Conservation and Laboratory Cost Together

Laboratory conditions are an impoverished proxy for environments such as soil, biofilms, and host tissue, so a gene that improves growth when deleted in rich medium may still provide fitness value in nature. [src: conservation_fitness_synthesis] This interpretation suggests the hypothesis that some conserved genes are maintained because their benefits appear in environments not represented by the laboratory assays. [src: conservation_fitness_synthesis]

The joint conservation–fitness matrix classified 28,017 genes as both costly in the laboratory and conserved in the pangenome. [src: conservation_fitness_synthesis] The new analysis **supports** treating this Costly + Conserved group as the strongest evidence for genes maintained despite laboratory-measured cost, while retaining the existing qualification that this is evidence for, rather than a direct measurement of, purifying selection in natural environments because laboratory fitness and pangenome conservation measure different aspects of gene value. [src: core_gene_tradeoffs, conservation_fitness_synthesis]

The same analysis identified 5,526 genes that were costly in the laboratory but dispensable in the pangenome. [src: conservation_fitness_synthesis] These genes are candidates for mobile elements, recently acquired genes, or genes undergoing loss, but their evolutionary status requires further testing. [src: conservation_fitness_synthesis] This joint interpretation refines [[concepts/pangenome-integration]] by treating conservation and laboratory cost as complementary evidence rather than interpreting either measurement alone. [src: conservation_fitness_synthesis]

The independent analysis identifies 4,450 genes (2.7%) that were neutral overall but critical in one condition. These ephemeral-niche genes were more common among core genes (3.0%) than auxiliary genes (1.7%) or singleton genes (1.6%), which **supports** the conclusion that conserved genes can carry conditionally important functions rather than being uniformly active or uniformly essential. [src: fitness_effects_conservation]

## Function-Specific Structure of the Paradox

The burden pattern was not uniform across functional categories. [src: conservation_fitness_synthesis] Motility and chemotaxis genes showed a +7.8pp core-burden excess, RNA metabolism showed a +12.9pp excess, and protein metabolism showed a +6.2pp excess. [src: conservation_fitness_synthesis] The new category-level results **support** these values and **refine** the interpretation by identifying Cell Wall genes as an explicit reversal: non-core cell-wall genes were more burdensome than core cell-wall genes, with a -14.1 percentage-point difference. [src: core_gene_tradeoffs]

The report interprets the motility and chemotaxis result as consistent with flagella being energetically expensive but useful for chemotaxis in natural environments, and interprets the protein-metabolism result as consistent with ribosomal components being costly but required for rapid growth responses. [src: conservation_fitness_synthesis] These functional differences indicate that the paradox reflects distinct ecological and physiological trade-offs rather than a single genome-wide mechanism. [src: conservation_fitness_synthesis] They also **support** the interpretation that the conserved genome is functionally active rather than uniformly inert, because genes with strong condition-specific effects were more likely to be core. [src: core_gene_tradeoffs]

## Coordinated Core-Genome Architecture

Independent component analysis (ICA), a method for identifying coordinated fitness modules, identified 1,116 co-regulated fitness modules across 32 organisms. [src: conservation_fitness_synthesis] These modules contained 86% core genes compared with an 81.5% baseline, with an odds ratio of 1.46 and p=1.6e-87. [src: conservation_fitness_synthesis] A total of 59% of the modules were more than 90% core genes. [src: conservation_fitness_synthesis]

This organization supports [[concepts/cofitness-network-architecture]] by showing that conservation and burden can be structured in coordinated functional units rather than only in individual essential genes. [src: conservation_fitness_synthesis]

## Limits and Non-Findings

Accessory genes were not systematically more burdensome than core genes; instead, they were less costly in the tested laboratory conditions, contrary to a genome-streamlining hypothesis. [src: conservation_fitness_synthesis]

Strong condition-specific fitness effects were more common among core genes, but condition-specific fitness did not establish niche-specific fitness because the experiments did not directly measure fitness across natural niches. [src: conservation_fitness_synthesis] The new analysis likewise cautions that its interpretation relies on laboratory fitness measurements and conservation patterns rather than direct measurement of selection in natural environments. [src: core_gene_tradeoffs]

Module-family breadth did not predict conservation: families spanning more organisms did not have higher core fractions, with rho=-0.01 and p=0.91. [src: conservation_fitness_synthesis] The report attributes the absence of a gradient in part to an already high baseline that left little room for one. [src: conservation_fitness_synthesis]

Novel singleton genes showed near-zero mean fitness in the independent analysis, suggesting that they were largely invisible to the tested laboratory assays rather than systematically beneficial or detrimental; however, this apparent neutrality may also reflect poor transposon coverage. [src: fitness_effects_conservation] This **refines** the interpretation of accessory quietness by making assay visibility a specific alternative to true neutrality. [src: fitness_effects_conservation]

The new linkage analysis further limits generalization: it mapped 44 of 48 organisms, but only 33 entered downstream analysis; four organisms were unmatched because their species had too few genomes for pangenome construction, and ten were excluded for <90% DIAMOND coverage. [src: conservation_vs_fitness] Essentiality was inferred from RB-TnSeq (random-barcode transposon sequencing) under library-construction growth conditions, and essential genes were slightly shorter, consistent with insertion bias. [src: conservation_vs_fitness]

## Tensions

The central tension is between laboratory burden and evolutionary retention: deletion can improve growth under tested conditions while the gene remains broadly conserved across genomes. [src: conservation_fitness_synthesis] The available evidence does not resolve this tension by directly measuring natural-environment fitness; it supports the hypothesis that unmeasured environments, ecological interactions, or long-term selection maintain at least some costly core genes. [src: conservation_fitness_synthesis]

The aggregate core-burden excess also coexists with the Cell Wall reversal, in which non-core genes were more burdensome than core genes. [src: core_gene_tradeoffs] This is not a contradiction of the genome-wide result, but it means that the paradox cannot be treated as a universal functional rule and must be tested at category and condition resolution. [src: core_gene_tradeoffs]

The 86.1% versus 81.2% essentiality-associated core fractions in the 33-organism linkage analysis are not directly comparable to the 82% versus 66% fractions from the 43-organism synthesis and independent analysis because the cohorts and classifications differ. [src: conservation_vs_fitness, conservation_fitness_synthesis, fitness_effects_conservation] The new result **supports** a positive essentiality–conservation association, while the differing effect sizes leave the magnitude sensitive to dataset composition and operational definitions. [src: conservation_vs_fitness]

## Open Directions

- Use the 5,526 costly-and-dispensable genes, mobile-element annotations, and comparative-genomic analyses to test whether these genes are enriched for mobile elements, recent acquisitions, or signatures of gene loss. [src: conservation_fitness_synthesis]
- Combine core-versus-accessory status, laboratory fitness measurements, and AlphaEarth environmental data with statistical tests to ask whether organisms from more variable environments contain more trade-off genes in their core genomes. [src: conservation_fitness_synthesis]
- Analyze the 43-organism conservation and fitness dataset with cross-species comparative methods to identify gene families that are universally essential across all 43 organisms. [src: conservation_fitness_synthesis]
- Reanalyze the 48 accessory modules containing exclusively flexible-genome co-regulated functions with module-level fitness and conservation data to determine whether they represent coherent adaptive programs. [src: conservation_fitness_synthesis]
- Pair RB-TnSeq measurements with fitness assays in soil, biofilm, and host-associated conditions to test whether laboratory-burdensome conserved genes become beneficial in natural-environment proxies. [src: conservation_fitness_synthesis]
- Stratify the 25,271 trade-off genes and the functional-category burden differences by assay condition and organism to test whether the Cell Wall reversal and the larger RNA-metabolism excess persist after condition coverage and phylogenetic structure are controlled. [src: core_gene_tradeoffs]
- Test whether the 4,450 ephemeral-niche genes remain enriched in core genomes after controlling for the number and type of conditions assayed, and whether singleton neutrality tracks transposon callability. [src: fitness_effects_conservation]
- Reanalyze the 33-organism essentiality–pangenome linkage with harmonized organism inclusion, pangenome clade size, coverage thresholds, and essentiality definitions to determine how much the 86.1% versus 81.2% association depends on dataset composition. [src: conservation_vs_fitness]
