<!-- tension-hash: 9415d508f6f4764c -->
# Do metal-tolerance scores track metal-associated isolation ecology?

Projects in this corpus disagree on whether genome-derived metal-tolerance scores line up with where bacteria are actually isolated. An isolate-level comparison against BacDive (a curated database of strain isolation and phenotype metadata) reports higher scores among contamination-associated isolates, while a species-scale cross-resistance analysis finds no correlation. [src: bacdive_metal_validation, metal_cross_resistance] Global metagenome and amplicon analyses offer related but non-equivalent biogeographic signals. [src: metal_resistance_global_biogeography, microbeatlas_metal_ecology] The outcome matters for [[concepts/environmental-resistome]], because it bears on how far these scores can be treated as validated against real isolation ecology.

## Evidence Sides

**Side A: contamination-associated isolates score higher**

BacDive reports higher metal-tolerance scores among contamination-associated isolates. This includes a Cohen's d (standardized mean difference between groups) of +1.00 for heavy-metal contamination, based on n = 10 isolates. [src: bacdive_metal_validation, metal_cross_resistance] This side reports a positive direction at the isolate level, but the heavy-metal group is small.

**Side B: no species-scale correlation**

The cross-resistance analysis found no species-scale correlation between multi-metal tolerance and metal-associated isolation. Spearman rho, a rank correlation coefficient, was approximately −0.02, with a p-value (the probability of a result at least this extreme if no association existed) of p > 0.8. After matching, only 20 independent species remained. [src: bacdive_metal_validation, metal_cross_resistance] This null result rests on a small species sample, so it does not establish that no association exists.

**Context: related but non-equivalent global signals**

A global analysis of MAGs (metagenome-assembled genomes) found that soil had 5.8% prevalence of metal resistance with an OR (odds ratio) of 5.05. Marine samples had 1.2% prevalence with an OR of 0.20. [src: metal_resistance_global_biogeography, microbeatlas_metal_ecology] MicrobeAtlas, a global amplicon-survey collection, found that metal-type diversity was associated with groundwater prevalence (ρ = +0.112, p = 0.0019) but not with groundwater-specific fold enrichment (ρ = +0.042, p = 0.242). [src: metal_resistance_global_biogeography, microbeatlas_metal_ecology] These results concern biome prevalence and genus-level metal-type diversity rather than isolate tolerance scores, so they are related to, but do not directly test, either side.

## Possible Reconciliations

- **Hypothesis 1: unit of analysis.** Side A compares contamination-associated isolates, while Side B collapses data to independent species. [src: bacdive_metal_validation, metal_cross_resistance] A signal carried by particular contaminated isolates may vanish once strains are pooled to species.
- **Hypothesis 2: sample size.** Both sides rest on small groups, so either result could reflect limited power rather than true presence or absence of an association.
- **Hypothesis 3: score definition.** Side B used a multi-metal tolerance score; if it differs from the score Side A tested, the analyses may measure different traits.
- **Hypothesis 4: prevalence versus enrichment.** The MicrobeAtlas contrast between prevalence and fold enrichment suggests that habitat breadth, rather than specialization, might drive any apparent metal–environment link.

## Resolving Work

- **Same score, different units.** Use BacDive isolation records and pangenome (all genes across a species' genomes) metal-tolerance scores, applying one score at isolate and species level. Does the positive effect persist after strains are collapsed to species?
- **Mixed-effects modelling.** Fit BacDive contamination categories in a mixed-effects model (regression with fixed and random terms), with species as a random effect (a per-species offset). Is the isolate-level association explained by species identity?
- **Stricter taxonomic matching.** Re-match the cross-resistance validation set with stricter taxonomic bridging and add species. Does a species-scale correlation emerge with a larger sample?
- **Biome stratification of isolates.** Combine MAG biome labels with isolate scores. Do high-scoring species concentrate in soil and avoid marine samples?
- **Breadth controls.** Use MicrobeAtlas groundwater samples in a regression that explicitly includes habitat breadth and sampling intensity as covariates. Does metal-type diversity predict groundwater fold enrichment once breadth is controlled?
