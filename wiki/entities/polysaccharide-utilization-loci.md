---
type: Gene_Or_Pathway
description: Polysaccharide-utilization loci and their qualified HGT signal
sources:
- id: gene_function_ecological_agora
  resource: ../summaries/gene_function_ecological_agora__REPORT.md
  title: gene function ecological agora
title: Polysaccharide-utilization loci
---
# Polysaccharide-utilization loci

## Identity

**Canonical name:** polysaccharide-utilization loci.  
**Known alias:** PUL; PUL CAZymes. [^gene_function_ecological_agora]

No stable external identifier for this entity is reported in the source document. [^gene_function_ecological_agora]

Polysaccharide-utilization loci are represented in this project through carbohydrate-active enzyme functions associated with the Bacteroidota × PUL hypothesis. [^gene_function_ecological_agora]

## Evidence from the Gene Function Ecological Agora

The original absolute-zero Innovator-Exchange criterion for Bacteroidota × PUL CAZymes was falsified at UniRef50 resolution. [^gene_function_ecological_agora]

Sankoff-parsimony diagnostics nevertheless recovered a small relative horizontal gene transfer signal with Cohen’s d = 0.15, so the synthesis classified the result as a qualified pass or reframed finding rather than evidence for the original strong criterion. [^gene_function_ecological_agora]

The Bacteroidota × PUL hypothesis had a leaf_consistency value of 0.41, where leaf_consistency is the fraction of species in a recipient clade carrying a KO, compared with an atlas reference of 0.20. [^gene_function_ecological_agora]

The project found that Bacteroidota had 1.40× gut/rumen enrichment with p < 10⁻³⁵, providing ecological consistency for interpreting PUL-associated functions in this clade. [^gene_function_ecological_agora]

Among 577 Bacteroidota species, phenotype profiles were saccharolytic and glycoside-hydrolase-rich, with anaerobic phenotypes at 33.2% versus 22.0% atlas-wide. [^gene_function_ecological_agora]

## Gene-neighborhood and mobile-element context

A complete large-scale PUL gene-neighborhood scan was deferred because Spark and pandas joins exceeded memory limits. [^gene_function_ecological_agora]

The PUL hypothesis set had an MGE-machinery rate of 0.00%, compared with an atlas-wide baseline of 1.37% of KO-bearing gene clusters. [^gene_function_ecological_agora]

Because the PUL neighborhood scan was not completed, the non-phage-borne interpretation for PUL systems relies on per-cluster MGE-machinery rates and literature context rather than complete cargo-neighborhood scans. [^gene_function_ecological_agora]

## Interpretation and limits

The PUL result **refines** the proposed link between Bacteroidota and Innovator-Exchange behavior: the strict absolute-zero criterion was not supported, while the small relative Sankoff signal remains compatible with limited acquisition or exchange. [^gene_function_ecological_agora]

The result should not be treated as proof that PUL functions are broadly exchanged across Bacteroidota, because the observed effect was small at Cohen’s d = 0.15 and the neighborhood analysis was scale-bounded. [^gene_function_ecological_agora]

Further analysis could combine the PUL KO set with memory-efficient contig-neighborhood methods and composition-based mobile-element confirmation to test whether PUL-associated genes occur in transferable genomic contexts. [^gene_function_ecological_agora]

## Related pages

- [gene_function_ecological_agora__REPORT](../summaries/gene_function_ecological_agora__REPORT.md) — source-project summary.
- [gene-function-acquisition-depth](../concepts/gene-function-acquisition-depth.md) — Sankoff-derived acquisition-depth framework used to evaluate the PUL hypothesis.
- [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md) — ecological and phenotype consistency for Bacteroidota-associated gene functions.
- [pangenome-integration](../concepts/pangenome-integration.md) — integration of KO presence, phylogeny, pangenome data, and mobile-element measurements.

[^gene_function_ecological_agora]: [gene function ecological agora](../summaries/gene_function_ecological_agora__REPORT.md)
