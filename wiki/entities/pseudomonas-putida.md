---
type: Organism
description: Pseudomonas putida evidence spans co-fitness, metabolism, and ecological
  carbon use
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
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: Pseudomonas putida
---
# Pseudomonas putida

## Identity

**Canonical name:** Pseudomonas putida. [^cofitness_coinheritance]

**Known alias:** Putida, the label used for this organism in the report. [^cofitness_coinheritance]

**Stable external identifier:** No stable external identifier was reported in the source document. [^cofitness_coinheritance]

## Evidence from co-fitness and co-inheritance analysis

Pseudomonas putida was one of the 9 organisms included in the primary analysis of laboratory-measured gene co-fitness and pangenome gene co-occurrence. [^cofitness_coinheritance]

The dataset contained 128 genomes, 5,409 pangenome clusters, and 458,688 cofit pairs for Pseudomonas putida. [^cofitness_coinheritance]

At the pairwise level, Pseudomonas putida had a delta phi of -0.000, with 205,323 cofit pairs, a mean phi of 0.171 for cofit pairs, a mean phi of 0.171 for prevalence-matched random pairs, and a Mann–Whitney p-value of 0.41. [^cofitness_coinheritance] This result does not provide evidence that pairwise co-fitness predicted gene co-occurrence in Pseudomonas putida under the reported analysis. [^cofitness_coinheritance]

Pseudomonas putida contributed 38 independent component analysis (ICA) modules, where ICA identifies coordinated multi-gene variation patterns, and 6 modules (16%) were significant. [^cofitness_coinheritance] Within its modules, the mean phi was 0.266 compared with a prevalence-matched null mean of 0.202. [^cofitness_coinheritance] This module-level result supports the broader finding that coordinated multi-gene modules may show stronger co-inheritance than individual pairwise co-fitness relationships, although the signal was significant for only 6 of 38 modules. [^cofitness_coinheritance]

## Evidence from pathway completeness, fitness, and carbon ecology

In the [gapmind](gapmind.md) pilot, Pseudomonas putida had complete predictions for 18 of 18 amino-acid biosynthesis pathways (100%), including serine biosynthesis, and 1,041 total GapMind predictions. [^essential_metabolome] This computational result refines the co-fitness profile with evidence of broad pathway completeness, but does not establish that those pathways or their genes are essential for viability. [^essential_metabolome]

The Pseudomonas putida KT2440 strain was one of 7 Tier 1 organisms with matching GapMind and Fitness Browser data in the capability-versus-dependency analysis. [^pathway_capability_dependency] This supports the existing GapMind evidence while refining it with a direct comparison between predicted pathway capability and experimentally measured fitness dependence; the report does not assign a separate four-way classification to this organism in the entity-level results. [^pathway_capability_dependency]

The new carbon-ecology analysis further supports broad metabolic capability at the relevant [pseudomonas-e](pseudomonas-e.md) group level: the Pseudomonas fluorescens/putida group retained substantially more plant-derived sugar and sugar-alcohol pathway completeness than the Pseudomonas aeruginosa group, while core organic-acid and amino-acid pathways remained near-universal in both groups. [^pseudomonas_carbon_ecology] This refines the organism-level GapMind evidence by indicating that ecological differentiation is concentrated in accessory carbon capabilities rather than universally conserved core pathways. [^pseudomonas_carbon_ecology] Carbon profiles also carried a statistically significant but modest environment signal among free-living and plant-associated species, so the result supports ecological relevance of pathway content without establishing that carbon profiles alone identify Pseudomonas putida’s habitat. [^pseudomonas_carbon_ecology]

## Evidence from functional dark-matter prioritization

The new dark-gene analysis refines the organism-level picture by prioritizing Pseudomonas putida N2C3 candidate AO356_11255: it had an absolute fitness effect of 3.4 under nitrogen conditions, a D-alanyl-D-alanine carboxypeptidase prediction, an EamA domain, and a lab–field odds ratio of 44. [^functional_dark_matter] Its enrichment in soil, freshwater, and wastewater matched the reported nitrogen-utilization fitness phenotype, although the environmental association is a prioritization signal rather than direct functional validation. [^functional_dark_matter]

Pseudomonas putida N2C3 also contributed 18 of the top 100 phenotype-bearing dark-gene candidates, and the proposed experimental campaign included N2C3 stress and carbon-source experiments. [^functional_dark_matter] This supports the existing module-level interpretation that condition-specific, coordinated phenotypes can guide experiments, while extending it from co-inheritance statistics to experimentally actionable dark-gene hypotheses. [^functional_dark_matter]

## Related pages

This organism is documented in [cofitness_coinheritance__REPORT](../summaries/cofitness_coinheritance__REPORT.md), [essential_metabolome__REPORT](../summaries/essential_metabolome__REPORT.md), [functional_dark_matter__REPORT](../summaries/functional_dark_matter__REPORT.md), [pathway_capability_dependency__REPORT](../summaries/pathway_capability_dependency__REPORT.md), and [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md), and contributes evidence to [cofitness-network-architecture](../concepts/cofitness-network-architecture.md), [pangenome-integration](../concepts/pangenome-integration.md), [cross-tenant-data-bridging](../concepts/cross-tenant-data-bridging.md), [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md), [gene-essentiality](../concepts/gene-essentiality.md), [condition-specific-fitness](../concepts/condition-specific-fitness.md), [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md), and [environment-embedding-geography](../concepts/environment-embedding-geography.md). [^cofitness_coinheritance] [^essential_metabolome] [^functional_dark_matter] [^pathway_capability_dependency] [^pseudomonas_carbon_ecology]

[^cofitness_coinheritance]: [cofitness coinheritance](../summaries/cofitness_coinheritance__REPORT.md)
[^essential_metabolome]: [essential metabolome](../summaries/essential_metabolome__REPORT.md)
[^pathway_capability_dependency]: [pathway capability dependency](../summaries/pathway_capability_dependency__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../summaries/functional_dark_matter__REPORT.md)
