---
type: "Concept"
description: "Mobile genetic elements as measurable host fitness burdens"
sources: ["summaries/costly_dispensable_genes__REPORT.md", "summaries/core_gene_tradeoffs__REPORT.md", "summaries/fitness_effects_conservation__REPORT.md"]
---
# Mobile genetic elements as measurable host fitness burdens

Mobile genetic elements (MGEs)—including transposases, integrases, phage sequences, insertion sequences, recombinases, and prophage-associated DNA—are a major component of the bacterial genes that are both costly in laboratory fitness assays and dispensable in the pangenome. [src: costly_dispensable_genes]

## Core finding

The analysis examined 142,190 genes from 43 bacteria and identified 5,526 genes in the costly+dispensable quadrant. [src: costly_dispensable_genes] These genes were 7.45 times more likely than costly+conserved genes to contain MGE-associated keywords, with OR=7.45 and p=4.6e-71. [src: costly_dispensable_genes] The SEED category “Phages, Prophages, Transposable elements, Plasmids” was 11.7 times enriched among costly+dispensable genes, with FDR=1.3e-17. [src: costly_dispensable_genes]

This evidence supports the interpretation that a measurable fraction of laboratory fitness burden is associated with mobile or recently mobile DNA rather than with conserved metabolic machinery. [src: costly_dispensable_genes] The interpretation is strongest for the enrichment statistics and remains an inference about evolutionary origin, because the analysis used annotation keywords and functional categories rather than direct measurements of element mobility or transfer. [src: costly_dispensable_genes]

The broader fitness–conservation analysis **refines** this contrast: across approximately 194,000 genes from 43 diverse bacteria, essential genes were 82% core whereas always-neutral genes were 66% core, but fitness importance was only a weak predictor of conservation. [src: fitness_effects_conservation] Thus, MGE-associated burden is a strong signature within the costly+dispensable subset, not evidence that all dispensable genes are burdensome or that all conserved genes are uniformly fit. The detailed comparison is summarized in [[summaries/fitness_effects_conservation__REPORT]]. [src: fitness_effects_conservation]

## Signatures of mobile and recently acquired DNA

Costly+dispensable genes had lower annotation coverage than costly+conserved genes: SEED annotations were present for 50.8% versus 74.9%, and KEGG annotations were present for 20.0% versus 42.7%, respectively. [src: costly_dispensable_genes] The costly+dispensable group also contained 44.5% orphan genes with no ortholog group, compared with 13.1% among costly+conserved genes. [src: costly_dispensable_genes] Its median ortholog breadth was 15 organisms, compared with 31 for costly+conserved genes, with Mann–Whitney p=4.0e-99 and rank-biserial r=0.233. [src: costly_dispensable_genes]

The costly+dispensable group had a 24.2% singleton fraction, whereas no costly+conserved genes were singletons. [src: costly_dispensable_genes] Within the dispensable category, costly genes were only slightly more likely than neutral genes to be singletons, with OR=1.09 and p=0.02. [src: costly_dispensable_genes] Costly+dispensable genes were also shorter, with a median length of 615 bp versus 765 bp for costly+conserved genes, with p=4.2e-75 and rank-biserial r=0.170. [src: costly_dispensable_genes]

Together, the annotation deficit, narrow ortholog breadth, singleton enrichment, and shorter median length support the hypothesis that many costly+dispensable genes reflect recently acquired, fragmented, or poorly characterized DNA. [src: costly_dispensable_genes] The singleton comparison should not be treated as independent evidence of mobility because core genes cannot be singletons by definition. [src: costly_dispensable_genes]

## Fitness burden versus conserved cellular function

Fourteen SEED top-level categories were significantly depleted in costly+dispensable genes at FDR < 0.05, including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response, and RNA Metabolism. [src: costly_dispensable_genes] By contrast, the 28,017 costly+conserved genes were interpreted as containing core cellular functions whose laboratory-measured burden may be offset by natural selection in environments not represented by the assays. [src: costly_dispensable_genes]

The core-gene trade-off analysis **supports** this distinction but **refines** it: core genes were more burdensome than non-core genes in Protein Metabolism, Motility, and RNA Metabolism, with differences of +6.2, +7.8, and +12.9 percentage points, respectively, while Cell Wall genes showed the reverse pattern, with a difference of -14.1 percentage points. [src: core_gene_tradeoffs] Thus, accessory MGE-associated burden remains strongly supported by the costly+dispensable enrichment, but burden among conserved genes is function-specific rather than uniformly low. [src: core_gene_tradeoffs]

The same analysis identified 25,271 true trade-off genes, representing 17.8% of the genes examined; trade-off genes were 1.29 times more likely to be core than non-core genes, with odds ratio 1.29 and p=1.2e-44. [src: core_gene_tradeoffs] This **supports** the interpretation that conservation can coexist with condition-dependent laboratory cost, rather than indicating universal essentiality. [src: core_gene_tradeoffs]

The new conservation analysis further **supports** and **refines** this trade-off interpretation: core genes were more likely than auxiliary genes to show a positive fitness effect when deleted, with 24.4% ever beneficial versus 19.9% of auxiliary genes, and OR=0.77 for auxiliary versus core. [src: fitness_effects_conservation] Core genes also had heavier tails in both negative and positive fitness-effect directions. [src: fitness_effects_conservation] These results suggest that conserved genes can participate in condition-dependent trade-offs, while the costly+dispensable MGE signal identifies a distinct burden associated with less-conserved DNA. [src: fitness_effects_conservation]

This contrast refines [[concepts/gene-essentiality]] by separating laboratory cost from evolutionary conservation: a gene can reduce measured fitness without being retained broadly across a species pangenome. [src: costly_dispensable_genes] It also connects to [[concepts/pangenome-integration]], because the costly phenotype becomes biologically interpretable only when combined with conservation, ortholog breadth, annotation, and gene-length information. [src: costly_dispensable_genes]

## Conditional persistence

The mobile-element-associated interpretation does not imply that costly+dispensable genes are inert under every condition. [src: costly_dispensable_genes] In total, 14.1% of costly+dispensable genes had condition-specific phenotypes, compared with 16.7% of costly+conserved genes and 2.7% of neutral+dispensable genes. [src: costly_dispensable_genes] This pattern suggests the hypothesis that condition-specific benefits can slow the loss of burdensome accessory genes when the relevant environments occur frequently enough. [src: costly_dispensable_genes]

The core-gene analysis **supports** this conditional interpretation but **contradicts** the expectation that condition-specific genes are predominantly accessory: genes tagged with strong condition-specific effects were 77.3% core, compared with 70.3% without such phenotypes, with OR=1.78 and p=1.8e-97. [src: fitness_effects_conservation] It also identified 4,450 genes (2.7%) that were neutral overall but critical in one condition; these ephemeral-niche genes were 3.0% of core genes, versus 1.7% of auxiliary and 1.6% of singleton genes. [src: fitness_effects_conservation] The result supports [[concepts/condition-specific-fitness]] by showing that pangenome dispensability and laboratory burden do not eliminate context-dependent effects, while indicating that detectable conditional effects are not restricted to accessory DNA. [src: costly_dispensable_genes, fitness_effects_conservation]

The condition-specific measurements are limited to conditions that can be tested in the laboratory, so their prevalence may not represent the full environmental phenotype space. [src: costly_dispensable_genes]

## Organism-level heterogeneity

*Pseudomonas stutzeri* RCH2 contributed 21.5% of its genes as costly+dispensable, compared with 14.0% for the next organism, *Bacteroides thetaiotaomicron*. [src: costly_dispensable_genes] The report identifies recent mobile-element invasion or strain-specific genomic expansion as possible explanations for this outlier but does not resolve the cause. [src: costly_dispensable_genes] This unresolved variation links the concept to [[concepts/subsurface-bacillota-specialization]] and [[concepts/horizontal-gene-transfer-driven-innovation]] without establishing that either process caused the RCH2 pattern. [src: costly_dispensable_genes]

## Interpretation and limits

The observed combination of MGE enrichment, narrow taxonomic distribution, short length, poor annotation, and depletion from core metabolism supports the hypothesis that many costly+dispensable genes are genomic debris or unstable accessory DNA associated with horizontal gene transfer. [src: costly_dispensable_genes] The analysis does not by itself distinguish active transposable elements from prophage remnants, inactive fragments, defense systems, or other recently acquired genes. [src: costly_dispensable_genes]

“Burden” was defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and measurement noise may affect classification. [src: costly_dispensable_genes] The binary core/accessory classification does not capture the fraction of genomes carrying each gene. [src: costly_dispensable_genes] The 90% identity DIAMOND threshold used to link Fitness Browser measurements to pangenome genes may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes] Ortholog groups were assigned using bidirectional best hits across 48 organisms, so genes with orthologs outside that set may be misclassified as orphans. [src: costly_dispensable_genes]

The core-gene results further caution that laboratory burden should not be interpreted as dispensability: their explanation of costly conserved genes relies on laboratory fitness and conservation patterns rather than direct measurement of selection in natural environments. [src: core_gene_tradeoffs] The Fitness Browser condition types are biased toward experimentally convenient conditions rather than ecologically relevant conditions. [src: core_gene_tradeoffs] The newer analysis likewise notes that fitness measurements are biased toward rich media and standard stresses, that single-gene knockouts omit epistatic interactions, and that the dataset is primarily Proteobacteria, limiting generalizability to other bacterial lineages. [src: fitness_effects_conservation] Singleton and novel genes may lack fitness data because of poor transposon coverage rather than true neutrality. [src: fitness_effects_conservation]

## Open Directions

- Reanalyze Fitness Browser measurements with replicate-level models and a continuous burden score rather than the max_fit > 1 rule to test whether MGE-associated genes retain a fitness deficit after reducing single-experiment noise. [src: costly_dispensable_genes]
- Replace binary dispensable/core labels with per-gene genome prevalence and test whether MGE keyword enrichment and fitness burden vary continuously with prevalence. [src: costly_dispensable_genes]
- Re-link genes using lower-identity and profile-based homology searches, then quantify how many current orphan and singleton assignments disappear when recently acquired sequence is recovered. [src: costly_dispensable_genes]
- Compare long-read assemblies, element-boundary calls, and gene-neighborhood information for *Pseudomonas stutzeri* RCH2 to test whether its 21.5% costly+dispensable proportion reflects mobile-element invasion or strain-specific genomic expansion. [src: costly_dispensable_genes]
- Measure costly+dispensable candidates across environmental conditions not represented in the laboratory dataset to test whether the 14.1% condition-specific fraction underestimates context-dependent benefits. [src: costly_dispensable_genes]
- Integrate MGE annotation, ortholog prevalence, and phylogeny across a larger organism set to test whether the observed burden is general or concentrated in particular lineages. [src: costly_dispensable_genes]
- Stratify MGE-associated and conserved genes by functional category and condition, using the existing Fitness Browser measurements, to test whether the core-gene burden differences of +6.2, +7.8, +12.9, and -14.1 percentage points persist after controlling for assay coverage and gene length. [src: core_gene_tradeoffs]
- Reanalyze MGE-associated genes jointly by fitness-effect breadth, conservation class, and condition-specific phenotype to test whether broad or ephemeral fitness effects explain the apparent persistence of burdensome accessory genes. [src: fitness_effects_conservation]
