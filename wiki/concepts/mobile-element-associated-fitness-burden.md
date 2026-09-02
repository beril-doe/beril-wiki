---
type: "Concept"
description: "How mobile elements impose measurable fitness burdens on bacterial hosts"
sources: ["summaries/costly_dispensable_genes__REPORT.md"]
---
# Mobile genetic elements as measurable host fitness burdens

Mobile genetic elements (MGEs)—including transposases, integrases, phage sequences, insertion sequences, recombinases, and prophage-associated DNA—are a major component of the bacterial genes that are both costly in laboratory fitness assays and dispensable in the pangenome. [src: costly_dispensable_genes]

## Core finding

The analysis examined 142,190 genes from 43 bacteria and identified 5,526 genes in the costly+dispensable quadrant. [src: costly_dispensable_genes] These genes were 7.45 times more likely than costly+conserved genes to contain MGE-associated keywords, with OR=7.45 and p=4.6e-71. [src: costly_dispensable_genes] The SEED category “Phages, Prophages, Transposable elements, Plasmids” was 11.7 times enriched among costly+dispensable genes, with FDR=1.3e-17. [src: costly_dispensable_genes]

This evidence supports the interpretation that a measurable fraction of laboratory fitness burden is associated with mobile or recently mobile DNA rather than with conserved metabolic machinery. [src: costly_dispensable_genes] The interpretation is strongest for the enrichment statistics and remains an inference about evolutionary origin, because the analysis used annotation keywords and functional categories rather than direct measurements of element mobility or transfer. [src: costly_dispensable_genes]

## Signatures of mobile and recently acquired DNA

Costly+dispensable genes had lower annotation coverage than costly+conserved genes: SEED annotations were present for 50.8% versus 74.9%, and KEGG annotations were present for 20.0% versus 42.7%, respectively. [src: costly_dispensable_genes] The costly+dispensable group also contained 44.5% orphan genes with no ortholog group, compared with 13.1% among costly+conserved genes. [src: costly_dispensable_genes] Its median ortholog breadth was 15 organisms, compared with 31 for costly+conserved genes, with Mann–Whitney p=4.0e-99 and rank-biserial r=0.233. [src: costly_dispensable_genes]

The costly+dispensable group had a 24.2% singleton fraction, whereas no costly+conserved genes were singletons. [src: costly_dispensable_genes] Within the dispensable category, costly genes were only slightly more likely than neutral genes to be singletons, with OR=1.09 and p=0.02. [src: costly_dispensable_genes] Costly+dispensable genes were also shorter, with a median length of 615 bp versus 765 bp for costly+conserved genes, with p=4.2e-75 and rank-biserial r=0.170. [src: costly_dispensable_genes]

Together, the annotation deficit, narrow ortholog breadth, singleton enrichment, and shorter median length support the hypothesis that many costly+dispensable genes reflect recently acquired, fragmented, or poorly characterized DNA. [src: costly_dispensable_genes] The singleton comparison should not be treated as independent evidence of mobility because core genes cannot be singletons by definition. [src: costly_dispensable_genes]

## Fitness burden versus conserved cellular function

Fourteen SEED top-level categories were significantly depleted in costly+dispensable genes at FDR < 0.05, including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response, and RNA Metabolism. [src: costly_dispensable_genes] By contrast, the 28,017 costly+conserved genes were interpreted as containing core cellular functions whose laboratory-measured burden may be offset by natural selection in environments not represented by the assays. [src: costly_dispensable_genes]

This contrast refines [[concepts/gene-essentiality]] by separating laboratory cost from evolutionary conservation: a gene can reduce measured fitness without being retained broadly across a species pangenome. [src: costly_dispensable_genes] It also connects to [[concepts/pangenome-integration]], because the costly phenotype becomes biologically interpretable only when combined with conservation, ortholog breadth, annotation, and gene-length information. [src: costly_dispensable_genes]

## Conditional persistence

The mobile-element-associated interpretation does not imply that costly+dispensable genes are inert under every condition. [src: costly_dispensable_genes] In total, 14.1% of costly+dispensable genes had condition-specific phenotypes, compared with 16.7% of costly+conserved genes and 2.7% of neutral+dispensable genes. [src: costly_dispensable_genes] This pattern suggests the hypothesis that condition-specific benefits can slow the loss of burdensome accessory genes when the relevant environments occur frequently enough. [src: costly_dispensable_genes]

This finding supports [[concepts/condition-specific-fitness]] by showing that pangenome dispensability and laboratory burden do not eliminate context-dependent effects. [src: costly_dispensable_genes] The condition-specific measurements are limited to conditions that can be tested in the laboratory, so their prevalence may not represent the full environmental phenotype space. [src: costly_dispensable_genes]

## Organism-level heterogeneity

*Pseudomonas stutzeri* RCH2 contributed 21.5% of its genes as costly+dispensable, compared with 14.0% for the next organism, *Bacteroides thetaiotaomicron*. [src: costly_dispensable_genes] The report identifies recent mobile-element invasion or strain-specific genomic expansion as possible explanations for this outlier but does not resolve the cause. [src: costly_dispensable_genes] This unresolved variation links the concept to [[concepts/genome-expansion-versus-streamlining]] and [[concepts/horizontal-gene-transfer-driven-innovation]] without establishing that either process caused the RCH2 pattern. [src: costly_dispensable_genes]

## Interpretation and limits

The observed combination of MGE enrichment, narrow taxonomic distribution, short length, poor annotation, and depletion from core metabolism supports the hypothesis that many costly+dispensable genes are genomic debris or unstable accessory DNA associated with horizontal gene transfer. [src: costly_dispensable_genes] The analysis does not by itself distinguish active transposable elements from prophage remnants, inactive fragments, defense systems, or other recently acquired genes. [src: costly_dispensable_genes]

“Burden” was defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and measurement noise may affect classification. [src: costly_dispensable_genes] The binary core/accessory classification does not capture the fraction of genomes carrying each gene. [src: costly_dispensable_genes] The 90% identity DIAMOND threshold used to link Fitness Browser measurements to pangenome genes may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes] Ortholog groups were assigned using bidirectional best hits across 48 organisms, so genes with orthologs outside that set may be misclassified as orphans. [src: costly_dispensable_genes]

## Open Directions

- Reanalyze Fitness Browser measurements with replicate-level models and a continuous burden score rather than the max_fit > 1 rule to test whether MGE-associated genes retain a fitness deficit after reducing single-experiment noise. [src: costly_dispensable_genes]
- Replace binary dispensable/core labels with per-gene genome prevalence and test whether MGE keyword enrichment and fitness burden vary continuously with prevalence. [src: costly_dispensable_genes]
- Re-link genes using lower-identity and profile-based homology searches, then quantify how many current orphan and singleton assignments disappear when recently acquired sequence is recovered. [src: costly_dispensable_genes]
- Compare long-read assemblies, element-boundary calls, and gene-neighborhood information for *Pseudomonas stutzeri* RCH2 to test whether its 21.5% costly+dispensable proportion reflects mobile-element invasion or strain-specific genomic expansion. [src: costly_dispensable_genes]
- Measure costly+dispensable candidates across environmental conditions not represented in the laboratory dataset to test whether the 14.1% condition-specific fraction underestimates context-dependent benefits. [src: costly_dispensable_genes]
- Integrate MGE annotation, ortholog prevalence, and phylogeny across a larger organism set to test whether the observed burden is general or concentrated in particular lineages. [src: costly_dispensable_genes]
