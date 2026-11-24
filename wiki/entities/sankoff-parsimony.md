---
type: "Method"
description: "A tree-based parsimony algorithm used to count gain events of a gene family on the GTDB species tree as a tractable HGT proxy."
sources: ["summaries/discoveries.md", "summaries/gene_function_ecological_agora__REPORT.md"]
aliases: ["Sankoff parsimony M16"]
---
# Sankoff parsimony

This page covers Sankoff parsimony, a tree-based parsimony algorithm used to count gain events of a gene family on the GTDB species tree as a tractable horizontal gene transfer (HGT) proxy. The gene_function_ecological_agora project, which calls the method M16, made it its primary Phase 2 atlas metric. [src: gene_function_ecological_agora] The evidence comes from one project, which scored a panel of 748 KEGG ortholog (KO) families. [src: gene_function_ecological_agora] See also [[summaries/gene_function_ecological_agora__REPORT]] and [[concepts/horizontal-gene-transfer-inference-metrics-and-control-class-calibration]].

## Key facts

- The project made Sankoff parsimony on the GTDB-r214 tree topology the primary atlas metric for Phase 2, and it demoted parent-rank dispersion to a diagnostic. [src: gene_function_ecological_agora]
- The report argues that the method is tractable at full GTDB scale, with 17M gain events on an 18,989-leaf tree. Exact duplication transfer loss (DTL) methods are not tractable at that scale. [src: gene_function_ecological_agora]
- The approach follows the precedent of Mirkin et al. 2003 and Csurös 2010. They used parsimony as an HGT proxy where full DTL reconciliation with AleRax, ALE or Notung is computationally infeasible. [src: gene_function_ecological_agora]

## What was measured

NB09b scored Sankoff parsimony for all 748 panel KOs on the GTDB-r214 species tree, pruned to 18,989 P1B leaves. The run took 11 seconds. [src: gene_function_ecological_agora] NB10 then identified 17,073,194 Sankoff parsimony gain events on the GTDB-r214 tree. [src: gene_function_ecological_agora]

## Acquisition-depth attribution

Sankoff parsimony paired with M22 recipient-rank gain attribution gives a tree-aware acquisition-depth signal at full GTDB scale. [src: gene_function_ecological_agora] The project used M22 to attribute 17M gain events to five acquisition-depth bins: recent, older_recent, mid, older and ancient. The central digest reports that this produces clean signatures by control class. [src: discoveries] The digest is summarised in [[summaries/discoveries]].
