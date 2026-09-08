---
type: Method
description: Binary association statistic used to compare gene co-occurrence.
sources:
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
title: Phi coefficient
---
# Phi coefficient

## What it is

**Canonical name:** Phi coefficient. [^cofitness_coinheritance]

**Known aliases:** No aliases were reported in the source document. [^cofitness_coinheritance]

**Stable external identifier:** No stable external identifier was reported in the source document. [^cofitness_coinheritance]

Phi coefficient is a binary association statistic used here to measure co-occurrence between gene clusters across genome-by-cluster presence vectors. [^cofitness_coinheritance]

## Use in co-fitness and co-inheritance analysis

The study mapped laboratory-measured co-fitness pairs to pangenome cluster pairs and evaluated each pair with phi coefficients calculated from binary genome-by-cluster presence vectors. [^cofitness_coinheritance]

Across 9 organisms, cofit gene pairs had a mean delta phi of +0.011 relative to prevalence-matched random pairs, with 7 of 9 organisms showing positive effects. [^cofitness_coinheritance]

The aggregate pairwise effect was delta=+0.003, with Mann-Whitney p=1.66e-29, while the Wilcoxon signed-rank test across organisms was not significant (W=9, p=0.13), indicating high inter-organism variance. [^cofitness_coinheritance]

Organism-level delta phi values ranged from +0.093 for Ddia6719 to -0.042 for Korea, with Putida showing -0.000. [^cofitness_coinheritance]

Ddia6719 had mean phi=0.182 for cofit pairs and 0.089 for random pairs, whereas Korea had mean phi=0.447 for cofit pairs and 0.489 for random pairs. [^cofitness_coinheritance]

The Korea negative delta was interpreted as statistical noise because 95.2% of its cofit pairs had NaN phi values, only approximately 8,000 of 166,601 pairs were computable, and both genes were present in 100% of 72 genomes for the affected pairs. [^cofitness_coinheritance]

Only 0.7% of cofit pairs were genomically adjacent within 5 genes, and excluding adjacent pairs did not change the result pattern. [^cofitness_coinheritance]

## Module-level results

Across 195 independent component analysis (ICA) modules in 6 organisms, within-module co-occurrence had mean phi=0.229 versus a prevalence-matched null mean of 0.177 from 1000 permutations, for delta=+0.053. [^cofitness_coinheritance]

A total of 51/195 modules (26%) were significant at p<0.05, and 21/195 modules (11%) remained significant at q<0.05 after Benjamini-Hochberg false discovery rate correction. [^cofitness_coinheritance]

Accessory modules had mean delta phi +0.108, with 8/11 (73%) significant at p<0.05 and 4/11 (36%) significant at q<0.05. [^cofitness_coinheritance]

Core modules had mean delta +0.059, with 29/120 (24%) significant at p<0.05 and 13/120 (11%) significant at q<0.05. [^cofitness_coinheritance]

Mixed modules had mean delta +0.031, with 14/64 (22%) significant at p<0.05 and 4/64 (6%) significant at q<0.05. [^cofitness_coinheritance]

The accessory-versus-core difference in delta phi trended toward significance with Mann-Whitney p=0.051. [^cofitness_coinheritance]

## Interpretation and limitations

Co-fitness strength was weakly anti-correlated with co-occurrence across 1.04M pairs, with Spearman rho=-0.109 and p<1e-300. [^cofitness_coinheritance]

The report attributed this pattern to a prevalence ceiling in which strong co-fitness pairs are often core genes with near-universal prevalence, leaving little variance for co-occurrence detection. [^cofitness_coinheritance]

Phi was higher among near genomes than medium-distance genomes, with mean phi=0.102 versus 0.067, consistent with shared ancestry. [^cofitness_coinheritance]

Most species lacked genomes in the far phylogenetic stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [^cofitness_coinheritance]

The report identifies auxiliary-only comparisons in which both clusters are below 95% prevalence as a next analysis for reducing the prevalence-ceiling limitation. [^cofitness_coinheritance]

## Related pages

This method is used in [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md) to connect [kescience-fitnessbrowser](kescience-fitnessbrowser.md) co-fitness measurements with pangenome gene presence and absence. [^cofitness_coinheritance]

The findings support [cofitness-network-architecture](../concepts/cofitness-network-architecture.md) by showing that pairwise co-fitness produces a weak co-occurrence signal, whereas coordinated ICA modules produce stronger co-inheritance. [^cofitness_coinheritance]

The analysis also contributes to [pangenome-integration](../concepts/pangenome-integration.md) and [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md) through linked pangenome, phylogenetic, module, and annotation data. [^cofitness_coinheritance]

[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
