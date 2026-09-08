---
title: Occurrence and Capability Do Not Establish Environmental Catabolism
type: Conflict
sources:
- id: enigma_carbon_census_1
  resource: ../../wiki/summaries/enigma_carbon_census_1__REPORT.md
  title: enigma carbon census 1
- id: pseudomonas_carbon_ecology
  resource: ../../wiki/summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
- id: metabolic_capability_dependency
  resource: ../../wiki/summaries/metabolic_capability_dependency__REPORT.md
  title: metabolic capability dependency
- id: essential_metabolome
  resource: ../../wiki/summaries/essential_metabolome__REPORT.md
  title: essential metabolome
- id: nmdc_community_metabolic_ecology
  resource: ../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md
  title: nmdc community metabolic ecology
---
<!-- tension-hash: a268834c4180a420 -->
# Occurrence and Capability Do Not Establish Environmental Catabolism

The tension in [occurrence-versus-catabolic-activity](../../wiki/concepts/occurrence-versus-catabolic-activity.md) is whether detecting a taxon or predicting its metabolic capability is sufficient to claim that it catabolizes a compound in situ. Environmental prevalence and genome-derived pathway profiles can justify site selection or provide intermediate ecological evidence, but the cited results distinguish these signals from direct measurements of degradation, uptake, expression, or carbon flux.

## Evidence Sides

**Occurrence and capability provide meaningful ecological evidence.** The census found 3-hydroxybenzoic-acid utilizers at 0.90 field prevalence at genus resolution, supporting the practical hypothesis that the taxon is accessible for enrichment. [^enigma_carbon_census_1] The *Pseudomonas* report likewise shows that environment-associated carbon profiles derived from genomes may provide an intermediate ecological signal. [^pseudomonas_carbon_ecology] The metabolic-capability study found that all 10 target species formed metabolic clusters, and environment-cluster associations were significant for *Salmonella enterica* and *Phenylobacterium* sp. [^metabolic_capability_dependency]

**Occurrence and computational capability are insufficient to establish in situ catabolism.** The environmental atlas was explicitly classified as an abundance or occurrence proxy rather than evidence of compound degradation or activity. [^enigma_carbon_census_1] The *Pseudomonas* profiles were pathway predictions from genomes, not environmental activity measurements; modest classifier performance and strong subgenus separation limit compound-specific catabolism claims. [^pseudomonas_carbon_ecology] Near-complete amino-acid pathway predictions across 7 organisms did not establish biosynthetic activity, and the apparent *D. vulgaris* serine auxotrophy remains unresolved without growth testing. [^essential_metabolome] Negative associations between community pathway completeness and ambient amino-acid intensity did not directly demonstrate catabolic uptake, pathway expression, or carbon flux. [^nmdc_community_metabolic_ecology] The metabolic-capability study’s latent-capability result came from laboratory fitness conditions, while its ecotype associations were observational and had no explicit phylogenetic correction. [^metabolic_capability_dependency]

## Possible Reconciliations

- **Hypothesis — measurement difference:** Prevalence, genome-derived capability, and laboratory fitness measure accessibility or potential, whereas compound-resolved experiments and activity measurements measure environmental catabolism.
- **Hypothesis — scope difference:** A taxon can be ecologically associated with a compound or environment without performing that compound’s degradation in situ.
- **Hypothesis — evidentiary layering:** Occurrence and capability may be valid site-selection and prioritization signals, while uptake, expression, or carbon flux requires independent validation.
- **Hypothesis — resolution difference:** Genus-level prevalence and subgenus-separated classifiers may capture ecological structure without resolving the specific strain, pathway, or condition responsible for activity.

## Resolving Work

- Pair occurrence surveys with compound-resolved enrichment experiments to test whether 3-hydroxybenzoic-acid utilizers recover and demonstrably degrade the compound.
- Measure pathway expression and compound uptake in environmental samples using transcript, protein, or isotope-tracing methods to distinguish genomic potential from active carbon flux.
- Test the apparent *D. vulgaris* serine auxotrophy through controlled growth experiments, including serine supplementation and omission conditions.
- Reanalyze ecotype associations with explicit phylogenetic correction and independent environmental activity measurements to test whether capability predicts catabolism beyond lineage structure.
- Expand the 7-organism essential-metabolome pilot and address missing *E. coli* GapMind coverage to determine whether computational pathway completeness generalizes experimentally.

[^enigma_carbon_census_1]: [enigma carbon census 1](../../wiki/summaries/enigma_carbon_census_1__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../../wiki/summaries/pseudomonas_carbon_ecology__REPORT.md)
[^metabolic_capability_dependency]: [metabolic capability dependency](../../wiki/summaries/metabolic_capability_dependency__REPORT.md)
[^essential_metabolome]: [essential metabolome](../../wiki/summaries/essential_metabolome__REPORT.md)
[^nmdc_community_metabolic_ecology]: [nmdc community metabolic ecology](../../wiki/summaries/nmdc_community_metabolic_ecology__REPORT.md)
