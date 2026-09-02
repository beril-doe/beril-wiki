---
type: "Organism"
description: "Pseudomonas putida evidence spans co-fitness, metabolism, and ecological carbon use"
sources: ["summaries/cofitness_coinheritance__REPORT.md", "summaries/essential_metabolome__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pathway_capability_dependency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# Pseudomonas putida

## Identity

**Canonical name:** Pseudomonas putida. [src: cofitness_coinheritance]

**Known alias:** Putida, the label used for this organism in the report. [src: cofitness_coinheritance]

**Stable external identifier:** No stable external identifier was reported in the source document. [src: cofitness_coinheritance]

## Evidence from co-fitness and co-inheritance analysis

Pseudomonas putida was one of the 9 organisms included in the primary analysis of laboratory-measured gene co-fitness and pangenome gene co-occurrence. [src: cofitness_coinheritance]

The dataset contained 128 genomes, 5,409 pangenome clusters, and 458,688 cofit pairs for Pseudomonas putida. [src: cofitness_coinheritance]

At the pairwise level, Pseudomonas putida had a delta phi of -0.000, with 205,323 cofit pairs, a mean phi of 0.171 for cofit pairs, a mean phi of 0.171 for prevalence-matched random pairs, and a Mann–Whitney p-value of 0.41. [src: cofitness_coinheritance] This result does not provide evidence that pairwise co-fitness predicted gene co-occurrence in Pseudomonas putida under the reported analysis. [src: cofitness_coinheritance]

Pseudomonas putida contributed 38 independent component analysis (ICA) modules, where ICA identifies coordinated multi-gene variation patterns, and 6 modules (16%) were significant. [src: cofitness_coinheritance] Within its modules, the mean phi was 0.266 compared with a prevalence-matched null mean of 0.202. [src: cofitness_coinheritance] This module-level result supports the broader finding that coordinated multi-gene modules may show stronger co-inheritance than individual pairwise co-fitness relationships, although the signal was significant for only 6 of 38 modules. [src: cofitness_coinheritance]

## Evidence from pathway completeness, fitness, and carbon ecology

In the [[entities/gapmind]] pilot, Pseudomonas putida had complete predictions for 18 of 18 amino-acid biosynthesis pathways (100%), including serine biosynthesis, and 1,041 total GapMind predictions. [src: essential_metabolome] This computational result refines the co-fitness profile with evidence of broad pathway completeness, but does not establish that those pathways or their genes are essential for viability. [src: essential_metabolome]

The Pseudomonas putida KT2440 strain was one of 7 Tier 1 organisms with matching GapMind and Fitness Browser data in the capability-versus-dependency analysis. [src: pathway_capability_dependency] This supports the existing GapMind evidence while refining it with a direct comparison between predicted pathway capability and experimentally measured fitness dependence; the report does not assign a separate four-way classification to this organism in the entity-level results. [src: pathway_capability_dependency]

The new carbon-ecology analysis further supports broad metabolic capability at the relevant [[entities/pseudomonas-e]] group level: the Pseudomonas fluorescens/putida group retained substantially more plant-derived sugar and sugar-alcohol pathway completeness than the Pseudomonas aeruginosa group, while core organic-acid and amino-acid pathways remained near-universal in both groups. [src: pseudomonas_carbon_ecology] This refines the organism-level GapMind evidence by indicating that ecological differentiation is concentrated in accessory carbon capabilities rather than universally conserved core pathways. [src: pseudomonas_carbon_ecology] Carbon profiles also carried a statistically significant but modest environment signal among free-living and plant-associated species, so the result supports ecological relevance of pathway content without establishing that carbon profiles alone identify Pseudomonas putida’s habitat. [src: pseudomonas_carbon_ecology]

## Evidence from functional dark-matter prioritization

The new dark-gene analysis refines the organism-level picture by prioritizing Pseudomonas putida N2C3 candidate AO356_11255: it had an absolute fitness effect of 3.4 under nitrogen conditions, a D-alanyl-D-alanine carboxypeptidase prediction, an EamA domain, and a lab–field odds ratio of 44. [src: functional_dark_matter] Its enrichment in soil, freshwater, and wastewater matched the reported nitrogen-utilization fitness phenotype, although the environmental association is a prioritization signal rather than direct functional validation. [src: functional_dark_matter]

Pseudomonas putida N2C3 also contributed 18 of the top 100 phenotype-bearing dark-gene candidates, and the proposed experimental campaign included N2C3 stress and carbon-source experiments. [src: functional_dark_matter] This supports the existing module-level interpretation that condition-specific, coordinated phenotypes can guide experiments, while extending it from co-inheritance statistics to experimentally actionable dark-gene hypotheses. [src: functional_dark_matter]

## Related pages

This organism is documented in [[summaries/cofitness_coinheritance__REPORT]], [[summaries/essential_metabolome__REPORT]], [[summaries/functional_dark_matter__REPORT]], [[summaries/pathway_capability_dependency__REPORT]], and [[summaries/pseudomonas_carbon_ecology__REPORT]], and contributes evidence to [[concepts/cofitness-network-architecture]], [[concepts/pangenome-integration]], [[concepts/cross-tenant-data-bridging]], [[concepts/metabolic-model-gapfilling]], [[concepts/gene-essentiality]], [[concepts/condition-specific-fitness]], [[concepts/ecotype-environment-gene-content]], and [[concepts/environment-embedding-geography]]. [src: cofitness_coinheritance] [src: essential_metabolome] [src: functional_dark_matter] [src: pathway_capability_dependency] [src: pseudomonas_carbon_ecology]
