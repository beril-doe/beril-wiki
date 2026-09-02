---
type: "Concept"
description: "Why costly, non-conserved genes may be lost from bacterial genomes"
sources: ["summaries/costly_dispensable_genes__REPORT.md"]
---
# Evolutionary loss of costly, non-conserved genes

Costly, non-conserved genes are a distinct pangenomic class whose laboratory burden and limited distribution suggest ongoing evolutionary instability rather than persistent core metabolism. [src: costly_dispensable_genes] The analysis examines 5,526 genes in this class among 142,190 genes from 43 bacteria. [src: costly_dispensable_genes] The underlying evidence and methods are summarized in [[summaries/costly_dispensable_genes__REPORT]]. [src: costly_dispensable_genes]

## Central claim

The report supports the interpretation that many costly+dispensable genes are horizontally acquired genomic material—including insertion sequences, prophage remnants, transposases, and defense systems—that imposes a fitness burden and is subsequently vulnerable to gene loss. [src: costly_dispensable_genes] This interpretation **refines** [[concepts/gene-essentiality]] by separating laboratory-measured burden from long-term pangenome conservation: a gene can reduce laboratory fitness without being evolutionarily retained across strains. [src: costly_dispensable_genes]

The evidence is strongest for mobile and recently acquired DNA, but the report does not establish that every costly+dispensable gene is nonfunctional or destined for deletion. [src: costly_dispensable_genes] Instead, the findings suggest the hypothesis that selection removes costly accessory genes unless environmental or community conditions periodically reward their functions. [src: costly_dispensable_genes]

## Evidence for mobile-element-associated burden

Costly+dispensable genes are 7.45 times more likely than costly+conserved genes to contain mobile-element keywords such as transposase, integrase, phage, IS element, recombinase, or prophage (OR=7.45, p=4.6e-71). [src: costly_dispensable_genes] The SEED category “Phages, Prophages, Transposable elements, Plasmids” is enriched 11.7-fold in the costly+dispensable group (FDR=1.3e-17), where FDR means false discovery rate. [src: costly_dispensable_genes] “Virulence” is enriched 26.7-fold (FDR=5.6e-14), although that result is based on small counts of 21 versus 4 genes. [src: costly_dispensable_genes]

These enrichments **support** [[concepts/mobile-element-associated-fitness-burden]] and **refine** [[concepts/horizontal-gene-transfer-driven-innovation]] by indicating that horizontal acquisition can produce genes that are both potentially useful in particular settings and burdensome in laboratory conditions. [src: costly_dispensable_genes]

## Evidence for recent acquisition and weak retention

Only 50.8% of costly+dispensable genes have SEED annotations, compared with 74.9% of costly+conserved genes. [src: costly_dispensable_genes] KEGG annotation rates are 20.0% and 42.7%, respectively. [src: costly_dispensable_genes] The costly+dispensable group contains 44.5% orphan genes with no ortholog group, compared with 13.1% among costly+conserved genes. [src: costly_dispensable_genes]

The median ortholog breadth is 15 organisms for costly+dispensable genes and 31 organisms for costly+conserved genes (Mann–Whitney p=4.0e-99, rank-biserial r=0.233). [src: costly_dispensable_genes] Costly+dispensable genes also have a 24.2% singleton fraction, whereas no costly+conserved genes are singletons; this comparison is partly structural because core genes cannot be singletons by definition. [src: costly_dispensable_genes] Within the dispensable category, costly genes are only slightly more likely than neutral genes to be singletons (OR=1.09, p=0.02). [src: costly_dispensable_genes]

The costly+dispensable genes have a median length of 615 bp, compared with 765 bp for costly+conserved genes (p=4.2e-75, rank-biserial r=0.170). [src: costly_dispensable_genes] Their shorter length is consistent with the presence of IS elements and gene fragments, but does not by itself prove that individual genes are degraded remnants. [src: costly_dispensable_genes] Together, poor annotation, orphan status, narrow ortholog breadth, singleton frequency, and short length **support** [[concepts/gene-function-acquisition-depth]] and [[concepts/functional-dark-matter]] as relevant frameworks for distinguishing recent acquisition from deeply conserved cellular function. [src: costly_dispensable_genes]

## Depletion from core metabolism

Fourteen SEED top-level categories are significantly depleted in costly+dispensable genes at FDR < 0.05, including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response, and RNA Metabolism. [src: costly_dispensable_genes] By contrast, the 28,017 costly+conserved genes are maintained in categories that include core cellular functions such as Protein Metabolism, Respiration, and Motility. [src: costly_dispensable_genes]

This contrast **supports** [[concepts/core-genome-burden-paradox]]: laboratory cost does not imply evolutionary loss when natural selection can offset that cost in environments not represented by the laboratory assay. [src: costly_dispensable_genes] It also **supports** [[concepts/pangenome-integration]] by showing that laboratory fitness measurements and pangenome conservation provide complementary evidence about gene persistence. [src: costly_dispensable_genes]

## Conditional persistence

The costly+dispensable class is not phenotypically inert: 14.1% of its genes have condition-specific phenotypes, compared with 16.7% of costly+conserved genes and 2.7% of neutral+dispensable genes. [src: costly_dispensable_genes] This result **supports** [[concepts/condition-specific-fitness]] and suggests the hypothesis that episodic benefits can delay the loss of genes that are costly under tested laboratory conditions. [src: costly_dispensable_genes]

The condition-specific result does not demonstrate that these genes are maintained by selection in nature because the phenotype data are biased toward conditions that can be tested in the laboratory. [src: costly_dispensable_genes] A gene may therefore appear costly and dispensable in the available data while retaining value in unmeasured environments, hosts, or microbial communities. [src: costly_dispensable_genes]

## Organism-level heterogeneity

*Pseudomonas stutzeri* RCH2 contributes 21.5% of its genes as costly+dispensable, compared with 14.0% for the next organism, *Bacteroides thetaiotaomicron*. [src: costly_dispensable_genes] The report identifies a recent mobile-element invasion or strain-specific genomic expansion as possible explanations, but leaves the cause unresolved. [src: costly_dispensable_genes] This outlier **qualifies** the cross-organism interpretation and links the concept to [[concepts/genome-expansion-versus-streamlining]]. [src: costly_dispensable_genes]

## Interpretation and limits

The report interprets the costly+dispensable class as genomic debris or unstable accessory material produced by horizontal gene transfer, but the evidence is partly dependent on annotation, orthology, and laboratory-fitness definitions. [src: costly_dispensable_genes] “Costly” is defined as max_fit > 1 in any experiment, so classification can be driven by a single experiment and is sensitive to fitness-data noise. [src: costly_dispensable_genes] The pangenome classification is binary, so it does not capture the fraction of genomes carrying each gene. [src: costly_dispensable_genes]

SEED and KEGG annotations cover only 56-79% of genes, and the unannotated fraction may have different functional profiles. [src: costly_dispensable_genes] The 90% identity DIAMOND threshold used to link Fitness Browser measurements with pangenome genes may miss recently acquired genes with low sequence similarity. [src: costly_dispensable_genes] Ortholog groups were assigned using bidirectional best hits across 48 organisms, so genes with orthologs outside that set may be misclassified as orphans. [src: costly_dispensable_genes]

The 21.5% value for *Pseudomonas stutzeri* RCH2 may reflect strain-specific genomic features rather than a general pattern. [src: costly_dispensable_genes] These limitations **support** treating evolutionary loss as a testable interpretation rather than an established fate for all costly, non-conserved genes. [src: costly_dispensable_genes]

## Open Directions

- Reanalyze gene presence as a continuous fraction of pangenome genomes, rather than a binary core/accessory label, and test whether increasing laboratory burden predicts decreasing prevalence after controlling for organism and gene length. [src: costly_dispensable_genes]
- Re-link Fitness Browser genes to pangenomes with sequence-similarity-sensitive homology methods and manual synteny checks to determine how many apparent costly+dispensable genes were missed or misclassified by the 90% identity DIAMOND threshold. [src: costly_dispensable_genes]
- Compare longitudinal genomes or closely related strain phylogenies for mobile-element-rich costly genes to test whether their loss, retention, or pseudogenization follows the predicted burden-associated pattern. [src: costly_dispensable_genes]
- Test *Pseudomonas stutzeri* RCH2 against related strains using mobile-element annotation, genome architecture, and phylogenetic reconstruction to distinguish recent invasion from strain-specific genomic expansion. [src: costly_dispensable_genes]
- Measure the 14.1% condition-specific subset across community, host-associated, and environmental conditions using targeted competition assays to ask whether context-specific benefits explain persistence of costly+dispensable genes. [src: costly_dispensable_genes]
