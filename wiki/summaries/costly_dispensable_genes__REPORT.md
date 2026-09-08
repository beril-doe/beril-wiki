---
type: Summary
description: Characterizes costly, dispensable bacterial genes as mobile-element-rich
  genomic debris.
doc_type: short
full_text: ../sources/costly_dispensable_genes__REPORT.md
title: The 5,526 Costly + Dispensable Genes
sources:
- id: costly_dispensable_genes
  resource: ../sources/costly_dispensable_genes__REPORT.md
  title: costly dispensable genes
---
# The 5,526 Costly + Dispensable Genes

## Overview

This analysis characterizes 5,526 bacterial genes that are both costly in laboratory fitness measurements and dispensable in the pangenome. Across 142,190 genes from 43 bacteria, the costly+dispensable quadrant is dominated by mobile genetic elements and recently acquired, poorly annotated, taxonomically restricted DNA rather than core metabolic functions. [^costly_dispensable_genes]

## Key Findings

### Mobile genetic elements dominate

Costly+dispensable genes are 7.45x more likely to contain mobile-element keywords such as transposase, integrase, phage, IS element, recombinase, or prophage than costly+conserved genes (OR=7.45, p=4.6e-71). The SEED category “Phages, Prophages, Transposable elements, Plasmids” is 11.7x enriched (FDR=1.3e-17), while “Virulence” is 26.7x enriched (FDR=5.6e-14), although the latter is based on small counts of 21 versus 4 genes. [^costly_dispensable_genes]

### Costly+dispensable genes show signatures of recent acquisition

Only 50.8% of costly+dispensable genes have SEED annotations, compared with 74.9% of costly+conserved genes; KEGG annotation rates are 20.0% and 42.7%, respectively. [^costly_dispensable_genes]

The costly+dispensable group contains 44.5% orphan genes with no ortholog group, compared with 13.1% among costly+conserved genes. Its median ortholog breadth is 15 organisms, compared with 31 for costly+conserved genes (Mann–Whitney p=4.0e-99, rank-biserial r=0.233). [^costly_dispensable_genes]

The costly+dispensable group has a 24.2% singleton fraction, whereas no costly+conserved genes are singletons; this comparison is partly structural because core genes cannot be singletons by definition. Within the dispensable category, costly genes are only slightly more likely than neutral genes to be singletons (OR=1.09, p=0.02). [^costly_dispensable_genes]

Costly+dispensable genes are shorter, with a median length of 615 bp versus 765 bp for costly+conserved genes (p=4.2e-75, rank-biserial r=0.170), consistent with IS elements and gene fragments. [^costly_dispensable_genes]

### Core metabolism is depleted

Fourteen SEED top-level categories are significantly depleted in costly+dispensable genes at FDR < 0.05, including Protein Metabolism, Respiration, Carbohydrates, Amino Acids, Cofactors/Vitamins, Motility, Stress Response, and RNA Metabolism. These core cellular functions are maintained in the 28,017 costly+conserved genes, whose energetic burden is interpreted as being offset by natural selection in environments not captured by laboratory experiments. [^costly_dispensable_genes]

### *Pseudomonas stutzeri* RCH2 is an outlier

psRCH2 contributes 21.5% of its genes as costly+dispensable, compared with 14.0% for the next organism, *Bacteroides thetaiotaomicron*. The report interprets this as potentially reflecting a recent mobile-element invasion or strain-specific genomic expansion, but identifies the cause as unresolved. [^costly_dispensable_genes]

### Some costly+dispensable genes have condition-specific effects

Despite being burdensome and non-conserved, 14.1% of costly+dispensable genes have condition-specific phenotypes, compared with 16.7% of costly+conserved genes and 2.7% of neutral+dispensable genes. This pattern suggests that costly+dispensable genes are not inert and that condition-specific effects may slow their loss from genomes. [^costly_dispensable_genes]

### Interpretation and biological significance

The report interprets costly+dispensable genes as genomic debris from horizontal gene transfer, including insertion sequences, prophage remnants, transposases, and defense systems that impose host costs and are not conserved across the species pangenome. Their mobile-element enrichment, narrow taxonomic distribution, short length, poor annotation, and depletion from core metabolism support this interpretation. [^costly_dispensable_genes]

These genes are candidates for ongoing gene loss: they may have been acquired by horizontal gene transfer but impose sufficient cost to be purged over evolutionary time unless they provide a selective advantage in particular environments. The 14.1% with condition-specific phenotypes may persist when the relevant conditions occur frequently enough. [^costly_dispensable_genes]

The contrast with the 28,017 costly+conserved genes indicates that costly+conserved genes are enriched in core metabolism, including Protein Metabolism, Respiration, and Motility, whereas the pangenome identifies costly+dispensable genes as evolutionarily unstable. The report frames this as a distinction between laboratory-measured cost and environmental maintenance by selection. [^costly_dispensable_genes]

The report connects these findings to the Black Queen Hypothesis, which proposes that costly genes can be lost when community members provide their functions as public goods; to mutant-fitness work showing that laboratory fitness data can assign phenotypes to genes of unknown function; to evidence that accessory genomes modulate strain-dependent essentiality; and to genome degradation associated with relaxed selection in symbiotic cyanobacteria. [^costly_dispensable_genes]

The analysis is presented as a cross-organism characterization of genes that are simultaneously burdensome and not conserved in the pangenome. It reports that the mobile-element profile narrows the interpretation of costly non-conserved genes toward horizontal-gene-transfer-mediated genome expansion rather than degrading metabolic pathways. [^costly_dispensable_genes]

## Caveats

- “Burden” is defined as max_fit > 1 in any experiment, so a single experiment can classify a gene as burdensome and the result is sensitive to noise in the fitness data. [^costly_dispensable_genes]
- SEED and KEGG annotations cover only 56-79% of genes, and the unannotated fraction may have different functional profiles. [^costly_dispensable_genes]
- The pangenome core/accessory classification is binary; using the fraction of genomes carrying each gene would provide more resolution. [^costly_dispensable_genes]
- The 90% identity DIAMOND threshold used for Fitness Browser–pangenome linking may miss recently acquired genes with low sequence similarity. [^costly_dispensable_genes]
- The extreme 21.5% costly+dispensable proportion in psRCH2 may reflect strain-specific genomic features rather than a general pattern. [^costly_dispensable_genes]
- Ortholog groups are assigned using bidirectional best hits across 48 organisms, so genes with orthologs outside this set may be misclassified as orphans. [^costly_dispensable_genes]
- Condition-specific phenotype data is biased toward conditions that can be tested in the laboratory. [^costly_dispensable_genes]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — Adds a cross-organism selection-quadrant analysis showing that costly, non-conserved genes are enriched for mobile elements rather than core cellular functions. [^costly_dispensable_genes]
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — Shows that 14.1% of costly+dispensable genes nevertheless have condition-specific phenotypes, linking genomic dispensability to context-dependent fitness effects. [^costly_dispensable_genes]
- [pangenome-integration](../concepts/pangenome-integration.md) — Connects laboratory fitness burden with pangenome conservation, ortholog breadth, orphan status, singleton frequency, and gene length. [^costly_dispensable_genes]

[^costly_dispensable_genes]: [costly dispensable genes](../sources/costly_dispensable_genes__REPORT.md)
