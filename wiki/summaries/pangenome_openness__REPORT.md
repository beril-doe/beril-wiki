---
type: "Summary"
description: "Summary of the project Pangenome Openness Analysis."
doc_type: "short"
full_text: "sources/pangenome_openness__REPORT.md"
---
# Pangenome Openness Analysis

This page summarises the Pangenome Openness Analysis. It asked whether pangenome openness predicts whether environment or phylogeny dominates a species' gene content. Openness was not significantly correlated with either effect. [src: pangenome_openness] The evidence is a null correlation on a limited set of species. [src: pangenome_openness] See also [[concepts/pangenome-openness-and-its-correlates]] and [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Key Findings

### Openness does not track environment or phylogeny effects

Neither correlation was significant, so the report concludes that an open or closed pangenome does not predict whether environment or phylogeny dominates gene content. [src: pangenome_openness]
- Openness vs Environment effect: Spearman rho -0.05, p-value 0.54. [src: pangenome_openness]
- Openness vs Phylogeny effect: Spearman rho 0.03, p-value 0.73. [src: pangenome_openness]

### Interpretations the report proposes

These are the report's explanations, not measured results.
- The open/closed distinction describes gene content variability but does not predict its ecological versus phylogenetic drivers. [src: pangenome_openness]
- Pangenome structure may be independent of eco-phylo dynamics, so open pangenomes do not necessarily imply environment-driven adaptation. [src: pangenome_openness]
- The lack of correlation is consistent with horizontal gene transfer (HGT) being opportunistic rather than ecologically directed. [src: pangenome_openness]
- HGT may not track environmental similarity, and gene acquisition might be opportunistic rather than niche-specific. [src: pangenome_openness]
- Core/accessory classification may not capture functional adaptation, because the genes that vary may not be the ones responding to environment. [src: pangenome_openness]

### Background framing

The report cites Tettelin et al. (2005) as introducing the open/closed pangenome framework for bacterial genomes. [src: pangenome_openness] It cites McInerney et al. (2017) as arguing that pangenome structure reflects a balance of selection, drift, and HGT. [src: pangenome_openness] It used the GTDB taxonomy and pangenome framework of Parks et al. (2022) for consistent cross-species comparisons. [src: pangenome_openness]

## Data and Methods

Pre-computed openness metrics per species came from the KBase pangenome statistics, read from the `pangenome` table via Spark. [src: pangenome_openness] Environment and phylogeny effect sizes came from the `ecotype_analysis` project. [src: pangenome_openness]

## Caveats and Open Work

- Sample size is limited to species with both pangenome statistics and ecotype analysis results. [src: pangenome_openness]
- Openness is a single summary metric that may not capture the full complexity of pangenome structure. [src: pangenome_openness]
- Environment and phylogeny effects come from partial correlations that may not fully disentangle confounded variables. [src: pangenome_openness]
- The upstream ecotype analysis may have limited statistical power for species with few genomes. [src: pangenome_openness]

Proposed next analyses:
- Stratify by gene function, asking whether open pangenomes show environment effects specifically in L (mobile) or V (defense) categories. [src: pangenome_openness]
- Test alternative openness metrics: auxiliary fraction, Heap's law alpha, or pangenome fluidity. [src: pangenome_openness]
- Test an openness x lifestyle interaction, such as open pathogens versus open environmental species. [src: pangenome_openness]

## Slots Into

- [[concepts/pangenome-openness-and-its-correlates]]: openness was uncorrelated with the environment effect (rho -0.05, p 0.54) and the phylogeny effect (rho 0.03, p 0.73). [src: pangenome_openness]
- [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]: openness does not predict whether environment or phylogeny dominates gene content. [src: pangenome_openness]
