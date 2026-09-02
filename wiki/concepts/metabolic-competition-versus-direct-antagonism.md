---
type: "Concept"
description: "Metabolic overlap predicts some antagonism, while direct mechanisms explain the remainder"
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Metabolic Overlap Explains Part but Not All of Microbial Antagonism

Microbial antagonism can arise when a commensal consumes the same resources as a target pathogen, but shared resource use does not fully explain inhibition. The [[summaries/cf_formulation_design__REPORT]] evaluates this distinction using carbon-utilization profiles, planktonic inhibition assays, growth kinetics, patient transcriptomics, and pangenome analysis. [src: cf_formulation_design]

## Evidence for Metabolic Competition

In synthetic cystic-fibrosis sputum conditions, *Pseudomonas aeruginosa* PA14 preferentially used amino acids: endpoint OD values were 0.60 for proline, 0.56 for histidine, 0.46 for ornithine, 0.40 for glutamate, 0.36 for aspartate, 0.36 for isoleucine, and 0.35 for arginine. [src: cf_formulation_design] Glucose supported OD 0.22, whereas threonine, methionine, cysteine, serine, and glycine each supported essentially no growth at <0.07. [src: cf_formulation_design]

Across 142 isolates with both inhibition and carbon-utilization measurements, metabolic overlap with PA14 significantly predicted planktonic inhibition, with r = 0.384 and p = 2.3×10⁻⁶. [src: cf_formulation_design] This result supports [[concepts/condition-specific-fitness]] because competition depended on resource-use behavior under a defined assay condition rather than on a universal antagonism score. [src: cf_formulation_design]

A multivariate metabolic model explained R² = 0.274 of inhibition variance, and adding genus-level taxonomy increased the fit to R² = 0.360. [src: cf_formulation_design] Five-fold cross-validation, in which the model is repeatedly evaluated on held-out data, yielded CV R² = 0.145 ± 0.142, showing that out-of-sample predictive power was lower than the training fit. [src: cf_formulation_design]

## Evidence for Direct or Taxon-Linked Antagonism

Metabolism alone left approximately 73% of inhibition variance unexplained, while genus contributed an additional 8.6% of explained variance. [src: cf_formulation_design] The genus contribution is consistent with species-specific direct-antagonism mechanisms, although the analysis does not by itself identify the molecules or interactions responsible. [src: cf_formulation_design]

Residual analysis identified inhibitors whose observed inhibition exceeded the metabolic model's expectation: *Streptococcus salivarius* ASMA-737 had a positive residual of +74.1%, *Gemella sanguinis* ASMA-3044 had +62.2%, and *Neisseria mucosa* ASMA-3643 had +57.2%. [src: cf_formulation_design] These residuals support the hypothesis that some commensals combine resource competition with direct antagonism, rather than demonstrating a specific direct mechanism. [src: cf_formulation_design]

Growth kinetics refined but did not replace the metabolic explanation. [src: cf_formulation_design] PA14 was the fastest grower on preferred substrates in most comparisons, while commensals exceeded its maximum growth rate in only 13.8% of substrate comparisons and began growing earlier in 43.1% of comparisons. [src: cf_formulation_design] Growth kinetic parameters were moderately correlated with endpoint OD at r ≈ 0.40, and adding kinetics increased the model fit to R² = 0.311 for the 29 isolates with all three assay types. [src: cf_formulation_design]

## Formulation Implications

The formulation analysis operationalized antagonism as a combination of metabolic coverage and measured inhibition. [src: cf_formulation_design] *Micrococcus luteus* grew on 9 of PA14's 11 preferred substrates, making it central to the minimum three-species formulation that achieved complete PA14 niche coverage despite its measured best inhibition of 38% and engraftability of 0.000. [src: cf_formulation_design] This contrast illustrates why niche overlap and direct inhibitory strength should be treated as distinct formulation criteria. [src: cf_formulation_design]

The strict-safe two-species candidate, *Rothia dentocariosa* plus *N. mucosa*, provided 84% mean inhibition and combined engraftability of 0.820, whereas the three-species candidate containing *M. luteus*, *N. mucosa*, and *S. salivarius* provided 75% inhibition and engraftability of 0.140. [src: cf_formulation_design] The report therefore recommended the two-species formulation as the primary clinical candidate and treated the three-species formulation as an aspirational second-line candidate contingent on demonstrating *M. luteus* engraftment in vivo. [src: cf_formulation_design]

Pairwise interaction measurements further support a mixed-mechanism interpretation but remain provisional. [src: cf_formulation_design] Mean synergy scores were +5.3% for *N. mucosa* + ASMA-2260, +1.4% for ASMA-3913 + ASMA-2260, −2.2% for *N. mucosa* + ASMA-2464, −14.2% for ASMA-3913 + ASMA-2464, and −19.8% for ASMA-1478 + ASMA-1197. [src: cf_formulation_design] Overall mean synergy was −5.8%, but the analysis included only 8 comparisons across 5 unique pairs. [src: cf_formulation_design] These results connect to [[concepts/cofitness-network-architecture]] by showing that combining individually inhibitory organisms does not guarantee additive or synergistic community inhibition. [src: cf_formulation_design]

## Boundary Conditions and Tensions

The evidence is limited to planktonic assays using PA14, whereas *P. aeruginosa* in cystic-fibrosis lungs primarily occupies structured biofilms. [src: cf_formulation_design] The carbon panel contained 22 substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. [src: cf_formulation_design] Consequently, the measured metabolic-overlap relationship may not capture resource competition or direct antagonism in airway biofilms. [src: cf_formulation_design]

The metabolic model covered 142 isolates representing 62 of 211 species (29%), and growth kinetics were available for only 32 isolates. [src: cf_formulation_design] The core cohort was enriched for deeply characterized taxa, including *Rothia*, *Streptococcus*, *Neisseria*, and *Gemella*. [src: cf_formulation_design] Pairwise interaction data covered only 3 A × 3 B isolate combinations, and the complete 10-pair interaction matrix for the five-species core had not been measured. [src: cf_formulation_design]

The pairwise database contained identical `fact_pairwise_interaction` and `fact_carbon_utilization` values, with correlation = 1.0 and mean difference = 0.0, so endpoint OD data could not assess per-substrate co-culture effects. [src: cf_formulation_design] Current interaction conclusions therefore relied on the RFU-based competition assay rather than on endpoint-OD co-culture measurements. [src: cf_formulation_design]

## Open Directions

- Measure the complete 10-pair interaction matrix for the five-species core with RFU-based competition assays and substrate-resolved co-cultures to determine whether pairwise effects are additive, synergistic, or antagonistic. [src: cf_formulation_design]
- Repeat inhibition and carbon-utilization assays in biofilm models containing mucins, lipids, iron, polyamines, and the genomically nominated sugar alcohols to test whether the planktonic metabolic-overlap relationship transfers to airway-like conditions. [src: cf_formulation_design]
- Test PAO1 and 3–5 mucoid clinical PA isolates alongside PA14 to determine whether metabolic predictors and residual inhibitor rankings generalize across pathogen backgrounds. [src: cf_formulation_design]
- Expand the matched isolate cohort and use held-out validation to determine whether genus-level residuals predict direct antagonism after controlling for metabolic overlap, growth kinetics, and phylogenetic relatedness. [src: cf_formulation_design]
- Combine metabolite profiling, transcriptomics, and targeted inhibition assays for *S. salivarius* ASMA-737, *G. sanguinis* ASMA-3044, and *N. mucosa* ASMA-3643 to identify mechanisms underlying their +74.1%, +62.2%, and +57.2% positive residuals. [src: cf_formulation_design]
