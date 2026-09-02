---
type: "Method"
description: "Permutational multivariate analysis of variance for multivariate composition tests"
sources: ["summaries/enigma_sso_asv_ecology__REPORT.md", "summaries/harvard_forest_warming__REPORT.md", "summaries/lignin_community_enrichment__REPORT.md", "summaries/prophage_ecology__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
# PERMANOVA

## What this entity is

**Canonical name:** PERMANOVA (permutational multivariate analysis of variance). [src: enigma_sso_asv_ecology]

**Known aliases:** permutational multivariate analysis of variance. [src: enigma_sso_asv_ecology]

**Stable external identifier:** Not reported in the source document. [src: enigma_sso_asv_ecology]

PERMANOVA is a method used in this corpus to test whether environmental, spatial, phylogenetic, and other sample-group variables explain multivariate community or gene-module composition. [src: enigma_sso_asv_ecology]

## Use in SSO subsurface community ecology

PERMANOVA applied to 37 sediment core segments found that hydrogeological zone explained 27.5% of community variance, with F = 4.05 and p = 0.0001. [src: enigma_sso_asv_ecology]

In the same analysis, well identity explained 19.2% of community variance but was not significant, with F = 0.80 and p = 0.979. [src: enigma_sso_asv_ecology]

The report interprets these results as evidence that depth and saturated-zone plume intersection have stronger effects on sediment community composition than horizontal well identity, although the plume explanation remains a hypothesis because direct SSO geochemistry was unavailable. [src: enigma_sso_asv_ecology]

A separate PERMANOVA of groundwater communities found that well identity explained 49.9% of variance with p = 0.001, filter size explained 10.1% with p = 0.001, depth within the saturated zone explained 2.5% with p = 0.430, and sampling date explained 0.8% with p = 0.998. [src: enigma_sso_asv_ecology]

These groundwater results support persistent well-level spatial structure over the 9-day sampling interval, but they do not establish long-term or seasonal stability. [src: enigma_sso_asv_ecology]

## Use in long-term soil warming

In the Harvard Forest warming study, PERMANOVA on Bray–Curtis genus distances refined the SSO findings by showing that treatment explained 7.6% of variance (p = 0.069), whereas soil horizon explained 30.6% (p = 0.0002) and the treatment × horizon four-cell factor explained 41% (p = 0.0002). [src: harvard_forest_warming] This supports the broader conclusion that environmental context can structure community composition, while indicating that the warming response was strongly horizon-specific rather than a uniform treatment effect. [src: harvard_forest_warming]

The detailed analysis is documented in [[summaries/harvard_forest_warming__REPORT]]. [src: harvard_forest_warming]

## Use in lignin-enrichment community ecology

In a 21-sample lignin-enrichment experiment, Bray–Curtis PERMANOVA supported and substantially strengthened the evidence that treatment restructures bacterial communities: across seven groups, treatment explained 97.9% of variance (F = 111.35, p = 0.001), while the Base-versus-Round-1 model explained 0.992 of variance (F = 394.42, p = 0.008). [src: lignin_community_enrichment] The Round-2 factorial model refined this result by separating prior history from current conditions: Round-1 history explained 58.9% (F = 14.31, p = 0.002), whereas current carbon source explained 32.7% (F = 4.85, p = 0.018). [src: lignin_community_enrichment]

The same analysis cautions that PERMANOVA signal is not exclusively a difference in group centroids: PERMDISP, a test of multivariate dispersion, was significant for 16S (p = 0.0004) and ITS (p = 0.0001), indicating that heterogeneous within-group dispersion also contributed. [src: lignin_community_enrichment] This qualifies, rather than contradicts, the strong treatment and history effects, particularly because fungal history was not statistically detectable (R² = 0.142, p = 0.090). [src: lignin_community_enrichment]

The detailed analysis is documented in [[summaries/lignin_community_enrichment__REPORT]]. [src: lignin_community_enrichment]

## Use in prophage-module ecology

In the prophage analysis, PERMANOVA on Bray-Curtis module composition across a 1,773-species subsample found significant effects for genome-size quartile, environment, and family-level phylogeny, each with p = 0.01; genome size was dominant (F = 212.99), followed by environment (F = 30.04) and phylogeny (F = 6.17). [src: prophage_ecology] This **supports** the existing environmental-context findings while **refining** them by showing that environment explained prophage-module composition beyond host phylogeny, although genome size remained the strongest reported predictor. [src: prophage_ecology]

The detailed analysis is documented in [[summaries/prophage_ecology__REPORT]]. [src: prophage_ecology]

## Use in Pseudomonas carbon-pathway ecology

A PERMANOVA-like permutation test of 62-pathway carbon profiles across 54 free-living and plant-associated Pseudomonas species found a significant association with isolation environment after 999 permutations (p = 0.006); between-group mean distance was 2.054 versus within-group mean distance of 1.890. [src: pseudomonas_carbon_ecology] This **supports** the existing evidence that environmental context structures multivariate composition, while **refining** it by showing that the ecological signal was modest: a four-class Random Forest achieved balanced accuracy of 0.408 +/- 0.169 against a 0.250 chance baseline. [src: pseudomonas_carbon_ecology]

Unlike the stronger treatment, horizon, and prophage-module effects above, the Pseudomonas result indicates that carbon profiles alone are insufficient for fine-grained environment discrimination; the dominant axis instead separated Pseudomonas s.s. from Pseudomonas_E. [src: pseudomonas_carbon_ecology] The detailed analysis is documented in [[summaries/pseudomonas_carbon_ecology__REPORT]]. [src: pseudomonas_carbon_ecology]

## Related pages

The method is documented in the source summary [[summaries/enigma_sso_asv_ecology__REPORT]]. [src: enigma_sso_asv_ecology]

The lignin results support [[concepts/condition-specific-fitness]], where community composition is interpreted in relation to carbon regime, and [[concepts/ecological-memory]], where Round-1 history is distinguished from current conditions. [src: lignin_community_enrichment]

The results contribute to [[concepts/ecotype-environment-gene-content]], which addresses environment-linked microbial community structure. [src: enigma_sso_asv_ecology]

The results also inform [[concepts/multi-omics-integration]], because geochemistry and metagenomics were identified as needed to validate the 16S-based interpretations. [src: enigma_sso_asv_ecology]

The prophage application also informs [[concepts/phage-defense-syndromes-and-arms-race]], because PERMANOVA identified environment-linked prophage-module composition beyond phylogeny. [src: prophage_ecology]

The Pseudomonas application informs [[concepts/environment-embedding-geography]] by testing environmental separation in pathway-profile space and [[concepts/metabolic-model-gapfilling]] by evaluating GapMind-derived carbon capabilities. [src: pseudomonas_carbon_ecology]
