---
type: Method
description: Permutational multivariate analysis of variance for multivariate composition
  tests
sources:
- id: enigma_sso_asv_ecology
  resource: ../summaries/enigma_sso_asv_ecology__REPORT.md
  title: enigma sso asv ecology
- id: harvard_forest_warming
  resource: ../summaries/harvard_forest_warming__REPORT.md
  title: harvard forest warming
- id: lignin_community_enrichment
  resource: ../summaries/lignin_community_enrichment__REPORT.md
  title: lignin community enrichment
- id: prophage_ecology
  resource: ../summaries/prophage_ecology__REPORT.md
  title: prophage ecology
- id: pseudomonas_carbon_ecology
  resource: ../summaries/pseudomonas_carbon_ecology__REPORT.md
  title: pseudomonas carbon ecology
title: PERMANOVA
---
# PERMANOVA

## What this entity is

**Canonical name:** PERMANOVA (permutational multivariate analysis of variance). [^enigma_sso_asv_ecology]

**Known aliases:** permutational multivariate analysis of variance. [^enigma_sso_asv_ecology]

**Stable external identifier:** Not reported in the source document. [^enigma_sso_asv_ecology]

PERMANOVA is a method used in this corpus to test whether environmental, spatial, phylogenetic, and other sample-group variables explain multivariate community or gene-module composition. [^enigma_sso_asv_ecology]

## Use in SSO subsurface community ecology

PERMANOVA applied to 37 sediment core segments found that hydrogeological zone explained 27.5% of community variance, with F = 4.05 and p = 0.0001. [^enigma_sso_asv_ecology]

In the same analysis, well identity explained 19.2% of community variance but was not significant, with F = 0.80 and p = 0.979. [^enigma_sso_asv_ecology]

The report interprets these results as evidence that depth and saturated-zone plume intersection have stronger effects on sediment community composition than horizontal well identity, although the plume explanation remains a hypothesis because direct SSO geochemistry was unavailable. [^enigma_sso_asv_ecology]

A separate PERMANOVA of groundwater communities found that well identity explained 49.9% of variance with p = 0.001, filter size explained 10.1% with p = 0.001, depth within the saturated zone explained 2.5% with p = 0.430, and sampling date explained 0.8% with p = 0.998. [^enigma_sso_asv_ecology]

These groundwater results support persistent well-level spatial structure over the 9-day sampling interval, but they do not establish long-term or seasonal stability. [^enigma_sso_asv_ecology]

## Use in long-term soil warming

In the Harvard Forest warming study, PERMANOVA on Bray–Curtis genus distances refined the SSO findings by showing that treatment explained 7.6% of variance (p = 0.069), whereas soil horizon explained 30.6% (p = 0.0002) and the treatment × horizon four-cell factor explained 41% (p = 0.0002). [^harvard_forest_warming] This supports the broader conclusion that environmental context can structure community composition, while indicating that the warming response was strongly horizon-specific rather than a uniform treatment effect. [^harvard_forest_warming]

The detailed analysis is documented in [harvard_forest_warming__REPORT](../summaries/harvard_forest_warming__REPORT.md). [^harvard_forest_warming]

## Use in lignin-enrichment community ecology

In a 21-sample lignin-enrichment experiment, Bray–Curtis PERMANOVA supported and substantially strengthened the evidence that treatment restructures bacterial communities: across seven groups, treatment explained 97.9% of variance (F = 111.35, p = 0.001), while the Base-versus-Round-1 model explained 0.992 of variance (F = 394.42, p = 0.008). [^lignin_community_enrichment] The Round-2 factorial model refined this result by separating prior history from current conditions: Round-1 history explained 58.9% (F = 14.31, p = 0.002), whereas current carbon source explained 32.7% (F = 4.85, p = 0.018). [^lignin_community_enrichment]

The same analysis cautions that PERMANOVA signal is not exclusively a difference in group centroids: PERMDISP, a test of multivariate dispersion, was significant for 16S (p = 0.0004) and ITS (p = 0.0001), indicating that heterogeneous within-group dispersion also contributed. [^lignin_community_enrichment] This qualifies, rather than contradicts, the strong treatment and history effects, particularly because fungal history was not statistically detectable (R² = 0.142, p = 0.090). [^lignin_community_enrichment]

The detailed analysis is documented in [lignin_community_enrichment__REPORT](../summaries/lignin_community_enrichment__REPORT.md). [^lignin_community_enrichment]

## Use in prophage-module ecology

In the prophage analysis, PERMANOVA on Bray-Curtis module composition across a 1,773-species subsample found significant effects for genome-size quartile, environment, and family-level phylogeny, each with p = 0.01; genome size was dominant (F = 212.99), followed by environment (F = 30.04) and phylogeny (F = 6.17). [^prophage_ecology] This **supports** the existing environmental-context findings while **refining** them by showing that environment explained prophage-module composition beyond host phylogeny, although genome size remained the strongest reported predictor. [^prophage_ecology]

The detailed analysis is documented in [prophage_ecology__REPORT](../summaries/prophage_ecology__REPORT.md). [^prophage_ecology]

## Use in Pseudomonas carbon-pathway ecology

A PERMANOVA-like permutation test of 62-pathway carbon profiles across 54 free-living and plant-associated Pseudomonas species found a significant association with isolation environment after 999 permutations (p = 0.006); between-group mean distance was 2.054 versus within-group mean distance of 1.890. [^pseudomonas_carbon_ecology] This **supports** the existing evidence that environmental context structures multivariate composition, while **refining** it by showing that the ecological signal was modest: a four-class Random Forest achieved balanced accuracy of 0.408 +/- 0.169 against a 0.250 chance baseline. [^pseudomonas_carbon_ecology]

Unlike the stronger treatment, horizon, and prophage-module effects above, the Pseudomonas result indicates that carbon profiles alone are insufficient for fine-grained environment discrimination; the dominant axis instead separated Pseudomonas s.s. from Pseudomonas_E. [^pseudomonas_carbon_ecology] The detailed analysis is documented in [pseudomonas_carbon_ecology__REPORT](../summaries/pseudomonas_carbon_ecology__REPORT.md). [^pseudomonas_carbon_ecology]

## Related pages

The method is documented in the source summary [enigma_sso_asv_ecology__REPORT](../summaries/enigma_sso_asv_ecology__REPORT.md). [^enigma_sso_asv_ecology]

The lignin results support [condition-specific-fitness](../concepts/condition-specific-fitness.md), where community composition is interpreted in relation to carbon regime, and [ecological-memory](../concepts/ecological-memory.md), where Round-1 history is distinguished from current conditions. [^lignin_community_enrichment]

The results contribute to [ecotype-environment-gene-content](../concepts/ecotype-environment-gene-content.md), which addresses environment-linked microbial community structure. [^enigma_sso_asv_ecology]

The results also inform [multi-omics-integration](../concepts/multi-omics-integration.md), because geochemistry and metagenomics were identified as needed to validate the 16S-based interpretations. [^enigma_sso_asv_ecology]

The prophage application also informs [phage-defense-syndromes-and-arms-race](../concepts/phage-defense-syndromes-and-arms-race.md), because PERMANOVA identified environment-linked prophage-module composition beyond phylogeny. [^prophage_ecology]

The Pseudomonas application informs [environment-embedding-geography](../concepts/environment-embedding-geography.md) by testing environmental separation in pathway-profile space and [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) by evaluating GapMind-derived carbon capabilities. [^pseudomonas_carbon_ecology]

[^enigma_sso_asv_ecology]: [enigma sso asv ecology](../summaries/enigma_sso_asv_ecology__REPORT.md)
[^harvard_forest_warming]: [harvard forest warming](../summaries/harvard_forest_warming__REPORT.md)
[^lignin_community_enrichment]: [lignin community enrichment](../summaries/lignin_community_enrichment__REPORT.md)
[^prophage_ecology]: [prophage ecology](../summaries/prophage_ecology__REPORT.md)
[^pseudomonas_carbon_ecology]: [pseudomonas carbon ecology](../summaries/pseudomonas_carbon_ecology__REPORT.md)
