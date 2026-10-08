---
type: "Summary"
description: "Summary of the pangenome_openness project, which found no significant correlation between species pangenome openness and environment or phylogeny effects on gene content."
doc_type: "short"
full_text: "sources/pangenome_openness__REPORT.md"
---
# Pangenome Openness Analysis

## Overview

This analysis tested whether bacterial pangenome openness predicts the relative influence of environment or phylogeny on gene content, using species with both pangenome statistics and ecotype-analysis results. [src: pangenome_openness]

## Key Findings

No significant relationship was detected between pangenome openness and either environment or phylogeny effects. Openness versus environment effect had Spearman rho = **-0.05** and p-value = **0.54**; openness versus phylogeny effect had Spearman rho = **0.03** and p-value = **0.73**. [src: pangenome_openness]

The results indicate that whether a species has an open or closed pangenome does not predict whether environment or phylogeny dominates its gene-content variation. [src: pangenome_openness]

The report interprets this null result as suggesting that pangenome structure may be independent of eco-phylogenetic dynamics, that horizontal gene transfer (HGT) may be opportunistic rather than tied to environmental similarity, and that core/accessory classification may not capture the genes most relevant to functional adaptation. The report describes the finding that openness is uncorrelated with environment effects as consistent with HGT being opportunistic rather than ecologically directed. The null correlation does not establish that mechanism. These interpretations are hypotheses rather than direct demonstrations from the reported correlations. [src: pangenome_openness]

The analysis places the result in the context of the open/closed pangenome framework introduced by Tettelin et al. (2005), the balance of selection, drift, and HGT discussed by McInerney et al. (2017), and the GTDB taxonomy and pangenome framework provided by Parks et al. (2022). [src: pangenome_openness]

## Data and Figures

Species-level openness metrics were pre-computed KBase pangenome statistics, read from the `pangenome` table via Spark. Environment and phylogeny effect sizes came from the upstream `ecotype_analysis` project. [src: pangenome_openness]

The report includes the figure `figures/pangenome_vs_effects.png`, which shows scatter plots of pangenome openness against environment and phylogeny effect sizes. [src: pangenome_openness]

## Caveats

The sample is limited to species with both pangenome statistics and ecotype-analysis results. The report does not give a sample count. [src: pangenome_openness]

Pangenome openness is a single summary metric and may not represent the full complexity of pangenome structure. [src: pangenome_openness]

Environment and phylogeny effects were derived from partial correlations, which may not fully disentangle confounded variables. [src: pangenome_openness]

The upstream ecotype analysis may have limited statistical power for some species with few genomes. [src: pangenome_openness]

## Future Directions

The report proposes stratifying by gene function to test whether open pangenomes show environment effects specifically in L (mobile) or V (defense) categories, testing auxiliary fraction, Heap's law alpha, or pangenome fluidity as alternative openness metrics, and testing openness-by-lifestyle interactions such as open pathogen versus open environmental species comparisons. [src: pangenome_openness]

## Slots Into

- [[concepts/pangenome-integration]] — The null correlations test whether pangenome openness predicts ecological or phylogenetic drivers of gene-content variation. [src: pangenome_openness]
- [[concepts/ecotype-environment-gene-content]] — The analysis connects pangenome openness to environment and phylogeny effect sizes from ecotype analysis. [src: pangenome_openness]
- [[concepts/pangenome-openness-determinants]] — This is a null result: openness did not track environment or phylogeny dominance, and the report offers untested interpretations of why. [src: pangenome_openness]
- [[concepts/horizontal-gene-transfer-driven-innovation]] — The report reads the null correlation as consistent with opportunistic, not niche-specific, HGT, but this remains a hypothesis. [src: pangenome_openness]
- [[concepts/phylogenetic-confounding-of-pangenome-associations]] — The environment and phylogeny effects come from partial correlations that may not fully disentangle confounded variables. [src: pangenome_openness]
- [[concepts/sampling-depth-and-downsampling-effects]] — The sample was restricted to species with both input datasets, and the upstream ecotype analysis may have limited statistical power for some species with few genomes. [src: pangenome_openness]
