---
type: "Organism"
description: "Rhizobial model organism used in fitness, pathway, and pangenome analyses."
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md"]
---
# Sinorhizobium meliloti

## Identity

**Canonical name:** Sinorhizobium meliloti. [src: cofitness_coinheritance]

**Known alias:** Smeli. [src: cofitness_coinheritance]

**Stable external identifier:** Not reported in this document. [src: cofitness_coinheritance]

Sinorhizobium meliloti was analyzed to test whether laboratory-measured gene co-fitness predicts gene co-occurrence across bacterial pangenomes. [src: cofitness_coinheritance]

## Key Facts from cofitness_coinheritance

The analysis included 241 genomes, 6,004 pangenome clusters, and 528,699 co-fitness pairs for Sinorhizobium meliloti. [src: cofitness_coinheritance]

Its pairwise co-fitness comparison had a delta phi of +0.002, with 230,516 co-fitness pairs; the mean phi was 0.029 for co-fitness pairs and 0.026 for prevalence-matched random pairs, with p<1e-17. [src: cofitness_coinheritance]

Sinorhizobium meliloti contributed co-fitness data to the cross-organism analysis, in which 7 of 9 organisms had positive pairwise co-occurrence effects, although inter-organism variance limited the aggregate interpretation. [src: cofitness_coinheritance]

All organisms in the primary analysis were evaluated by mapping co-fitness pairs to pangenome cluster pairs and calculating phi coefficients from binary genome-by-cluster presence vectors; ten prevalence-matched random pairs were generated per co-fitness pair. [src: cofitness_coinheritance]

A phylogenetic tree was available for Sinorhizobium meliloti in the targeted organism set. [src: cofitness_coinheritance]

## Metabolic capability and fitness

In a separate seven-organism pilot, Smeli had complete GapMind predictions for all 18 amino-acid biosynthesis pathways (18/18; 100%). [src: essential_metabolome] This **refines** the co-fitness analysis by adding computational pathway-completeness evidence for the same organism, but does not establish that those pathways are essential for viability because the comparison used computational calls and rich-media RB-TnSeq essential-gene data. [src: essential_metabolome]

The Smeli result contributes to the pilot’s observation that 17 of 18 amino-acid pathways were present in all 7 analyzed organisms; the study’s limited sample means this supports near-universal, not bacteria-wide universal, completeness. [src: essential_metabolome] GapMind coverage and pathway calls may miss non-canonical or divergent routes, so the finding remains computational. [src: essential_metabolome]

The metabolic-capability/dependency analysis included Sinorhizobium meliloti among its seven Tier 1 organisms, extending the earlier completeness result by placing pathway predictions alongside RB-TnSeq fitness evidence rather than treating capability as dependency. [src: pathway_capability_dependency] The broader study classified 161 organism–pathway pairs into Active Dependency, Latent Capability, Incomplete but Important, and Missing categories, but did not report a Smeli-specific category in the available summary. [src: pathway_capability_dependency]

## Functional dark-matter prioritization

The functional-dark-matter study included Sinorhizobium meliloti in its proposed 10 organism–condition experiment set, with one carbon-source and one stress experiment. [src: functional_dark_matter] This **extends** the earlier co-fitness and essential-metabolome evidence by translating organism-level pathway and fitness integration into targeted experiments, rather than adding a new organism-specific phenotype for Smeli. [src: functional_dark_matter]

Across that 10-experiment set, the experiments were projected to address 242 of the top 500 dark genes (45.3%); the Smeli experiments were part of this coverage estimate, which is a prioritization result rather than a direct measurement in this organism. [src: functional_dark_matter]

These findings contribute to [[concepts/cofitness-network-architecture]], which evaluates whether co-fitness relationships predict pangenome co-occurrence, and to [[concepts/pangenome-integration]], which addresses integration of fitness and pangenome presence/absence data. [src: cofitness_coinheritance]

The underlying integration used the [[entities/kescience-fitnessbrowser]] dataset together with KBase pangenome and phylogenetic data. [src: cofitness_coinheritance]

For the complete study context, see [[summaries/cofitness_coinheritance__REPORT]], [[summaries/essential_metabolome__REPORT]], [[summaries/functional_dark_matter__REPORT]], and [[summaries/pathway_capability_dependency__REPORT]]. [src: cofitness_coinheritance] [src: essential_metabolome] [src: functional_dark_matter] [src: pathway_capability_dependency]
