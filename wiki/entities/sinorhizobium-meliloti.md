---
type: Organism
description: Rhizobial model organism used in fitness, pathway, and pangenome analyses.
sources:
- id: cofitness_coinheritance
  resource: ../summaries/cofitness_coinheritance__REPORT.md
  title: cofitness coinheritance
- id: essential_metabolome
  resource: ../summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: functional_dark_matter
  resource: ../summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
- id: pathway_capability_dependency
  resource: ../summaries/pathway_capability_dependency__REPORT.md
  title: pathway capability dependency
title: Sinorhizobium meliloti
---
# Sinorhizobium meliloti

## Identity

**Canonical name:** Sinorhizobium meliloti. [^cofitness_coinheritance]

**Known alias:** Smeli. [^cofitness_coinheritance]

**Stable external identifier:** Not reported in this document. [^cofitness_coinheritance]

Sinorhizobium meliloti was analyzed to test whether laboratory-measured gene co-fitness predicts gene co-occurrence across bacterial pangenomes. [^cofitness_coinheritance]

## Key Facts from cofitness_coinheritance

The analysis included 241 genomes, 6,004 pangenome clusters, and 528,699 co-fitness pairs for Sinorhizobium meliloti. [^cofitness_coinheritance]

Its pairwise co-fitness comparison had a delta phi of +0.002, with 230,516 co-fitness pairs; the mean phi was 0.029 for co-fitness pairs and 0.026 for prevalence-matched random pairs, with p<1e-17. [^cofitness_coinheritance]

Sinorhizobium meliloti contributed co-fitness data to the cross-organism analysis, in which 7 of 9 organisms had positive pairwise co-occurrence effects, although inter-organism variance limited the aggregate interpretation. [^cofitness_coinheritance]

All organisms in the primary analysis were evaluated by mapping co-fitness pairs to pangenome cluster pairs and calculating phi coefficients from binary genome-by-cluster presence vectors; ten prevalence-matched random pairs were generated per co-fitness pair. [^cofitness_coinheritance]

A phylogenetic tree was available for Sinorhizobium meliloti in the targeted organism set. [^cofitness_coinheritance]

## Metabolic capability and fitness

In a separate seven-organism pilot, Smeli had complete GapMind predictions for all 18 amino-acid biosynthesis pathways (18/18; 100%). [^essential_metabolome] This **refines** the co-fitness analysis by adding computational pathway-completeness evidence for the same organism, but does not establish that those pathways are essential for viability because the comparison used computational calls and rich-media RB-TnSeq essential-gene data. [^essential_metabolome]

The Smeli result contributes to the pilot’s observation that 17 of 18 amino-acid pathways were present in all 7 analyzed organisms; the study’s limited sample means this supports near-universal, not bacteria-wide universal, completeness. [^essential_metabolome] GapMind coverage and pathway calls may miss non-canonical or divergent routes, so the finding remains computational. [^essential_metabolome]

The metabolic-capability/dependency analysis included Sinorhizobium meliloti among its seven Tier 1 organisms, extending the earlier completeness result by placing pathway predictions alongside RB-TnSeq fitness evidence rather than treating capability as dependency. [^pathway_capability_dependency] The broader study classified 161 organism–pathway pairs into Active Dependency, Latent Capability, Incomplete but Important, and Missing categories, but did not report a Smeli-specific category in the available summary. [^pathway_capability_dependency]

## Functional dark-matter prioritization

The functional-dark-matter study included Sinorhizobium meliloti in its proposed 10 organism–condition experiment set, with one carbon-source and one stress experiment. [^functional_dark_matter] This **extends** the earlier co-fitness and essential-metabolome evidence by translating organism-level pathway and fitness integration into targeted experiments, rather than adding a new organism-specific phenotype for Smeli. [^functional_dark_matter]

Across that 10-experiment set, the experiments were projected to address 242 of the top 500 dark genes (45.3%); the Smeli experiments were part of this coverage estimate, which is a prioritization result rather than a direct measurement in this organism. [^functional_dark_matter]

These findings contribute to [cofitness-network-architecture](../concepts/cofitness-network-architecture.md), which evaluates whether co-fitness relationships predict pangenome co-occurrence, and to [pangenome-integration](../concepts/pangenome-integration.md), which addresses integration of fitness and pangenome presence/absence data. [^cofitness_coinheritance]

The underlying integration used the [kescience-fitnessbrowser](kescience-fitnessbrowser.md) dataset together with KBase pangenome and phylogenetic data. [^cofitness_coinheritance]

For the complete study context, see [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md), [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md), [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md), and [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md). [^cofitness_coinheritance] [^essential_metabolome] [^functional_dark_matter] [^pathway_capability_dependency]

[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
