---
type: "Concept"
description: "Jointly optimize inhibition, resource coverage, safety, and engraftability when designing protective microbial consortia."
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Designing Protective Microbial Consortia Requires Joint Optimization of Inhibition, Coverage, Safety, and Engraftability

Protective microbial consortia should be designed as multi-objective formulations rather than selected solely for maximal pathogen inhibition. Inhibition, coverage of the pathogen's resource niche, safety constraints, and the probability of engraftment can favor different species or community sizes. The [[summaries/cf_formulation_design__REPORT]] provides a cystic-fibrosis airway case study centered on suppressing [[entities/pseudomonas-aeruginosa]] through metabolic competition and direct antagonism. [src: cf_formulation_design]

The study supports metabolic competition as a real but incomplete planktonic mechanism, while establishing an evidence boundary: planktonic inhibition does not directly establish protection against the structured *Pseudomonas aeruginosa* biofilms that primarily occupy cystic-fibrosis airways. [src: cf_formulation_design]

## Metabolic competition explains part of antagonism

In synthetic cystic-fibrosis sputum conditions, PA14 preferentially used amino acids: endpoint OD values were 0.60 for proline, 0.56 for histidine, 0.46 for ornithine, 0.40 for glutamate, 0.36 for aspartate, 0.36 for isoleucine, and 0.35 for arginine. Glucose supported OD 0.22, whereas threonine, methionine, cysteine, serine, and glycine each supported essentially no growth at <0.07. [src: cf_formulation_design]

Across 142 isolates with both inhibition and carbon-utilization measurements, metabolic overlap with PA14 significantly predicted planktonic inhibition, with r = 0.384 and p = 2.3×10⁻⁶. A multivariate metabolic model explained R² = 0.274 of inhibition variance; adding genus-level taxonomy increased the fit to R² = 0.360. Five-fold cross-validation, in which the model is repeatedly evaluated on held-out data, yielded CV R² = 0.145 ± 0.142, showing that out-of-sample predictive power was lower than the training fit. [src: cf_formulation_design]

This **supports** [[concepts/condition-specific-fitness]]: resource-use similarity contributed to competitive fitness under a defined assay condition rather than providing a universal antagonism score. It also **refines** a metabolism-only interpretation: approximately 73% of inhibition variance remained unexplained, while genus contributed an additional 8.6% of explained variance. The genus contribution is consistent with species-specific direct-antagonism mechanisms, although the analysis did not identify the responsible molecules or interactions. [src: cf_formulation_design]

Residual analysis identified inhibitors whose observed inhibition exceeded the metabolic model's expectation: *Streptococcus salivarius* ASMA-737 had a positive residual of +74.1%, *Gemella sanguinis* ASMA-3044 had +62.2%, and *Neisseria mucosa* ASMA-3643 had +57.2%. These residuals **support the hypothesis** that some commensals combine resource competition with direct antagonism, rather than demonstrating a specific direct mechanism. [src: cf_formulation_design]

Growth kinetics further separated possible mechanisms. PA14 was the fastest grower on preferred substrates in most comparisons; commensals exceeded its maximum growth rate in only 13.8% of substrate comparisons but began growing earlier in 43.1% of comparisons. Growth kinetic parameters were moderately correlated with endpoint OD at r ≈ 0.40, and adding kinetics increased the model fit to R² = 0.311 among the 29 isolates with all three assay types. [src: cf_formulation_design]

These results **refine** a single-score view of inhibition: endpoint growth, lag-time advantage, and direct antagonism can contribute distinct evidence, and a formulation should not be judged from any one assay alone. The condition-specific measurements do not demonstrate that the same advantages persist in a spatially structured airway biofilm. [src: cf_formulation_design]

## Coverage and engraftability can oppose one another

The formulation analysis operationalized antagonism as a combination of metabolic coverage and measured inhibition. Strict safety-filter optimization identified a five-species core of [[entities/neisseria-mucosa]], [[entities/streptococcus-salivarius]], [[entities/micrococcus-luteus]], [[entities/rothia-dentocariosa]], and [[entities/gemella-sanguinis]]. [src: cf_formulation_design]

The best strict-safe formulations varied across objectives: the k=1 formulation containing *N. mucosa* had 18% niche coverage, 88% inhibition, and engraftability 1.595; the k=2 formulation containing *R. dentocariosa* + *N. mucosa* had 18% coverage, 84% inhibition, and engraftability 0.820; the k=3 formulation containing *M. luteus* + *N. mucosa* + *S. salivarius* had 100% coverage, 75% inhibition, and engraftability 0.140; the k=4 formulation had 100% coverage, 76% inhibition, and engraftability 0.185; and the k=5 core had 100% coverage, 78% inhibition, and engraftability 0.188. [src: cf_formulation_design]

The k=3 formulation was the minimum size achieving complete PA14 niche coverage because *M. luteus* grew on 9 of PA14's 11 preferred substrates. Its measured best inhibition was 38% and its engraftability was 0.000. [src: cf_formulation_design] Thus niche overlap and direct inhibitory strength are distinct formulation criteria: *M. luteus* was central to complete coverage but was not a strong inhibitor or demonstrated engraftable species. This **supports** a coverage-versus-establishment interpretation of [[concepts/competitive-exclusion-consortium-design]]. [src: cf_formulation_design]

Exhaustive enumeration of C(97,3) = 147,440 possible triples produced 127,598 valid unique-species formulations, and the k=3 combination was the global optimum with composite score 0.562. However, bootstrap resampling over 1,000 replicates produced 95% composite-score confidence intervals of [0.753, 0.753] for k=1, [0.514, 0.588] for k=2, [0.551, 0.562] for k=3, [0.534, 0.578] for k=4, and [0.520, 0.587] for k=5; the k=2 through k=5 intervals overlapped. [src: cf_formulation_design]

The overlapping intervals **weaken** any claim that larger formulations are statistically preferable on the composite score, even though larger formulations can improve niche coverage. [src: cf_formulation_design]

Among 134 species detected in patient metagenomes, engraftability, defined as prevalence × log(activity ratio), was highest for *N. mucosa* at 1.595; *R. dentocariosa* scored 0.422 and *S. salivarius* scored 0.172. [src: cf_formulation_design] The report recommends k=2, *R. dentocariosa* + *N. mucosa*, as the primary clinical candidate because both species are lung-adapted, provide 84% mean inhibition, and have combined engraftability 0.820, nearly 6× higher than the k=3 formulation's 0.140. [src: cf_formulation_design]

The k=3 formulation is instead an aspirational second-line candidate contingent on demonstrating *M. luteus* engraftment in vivo: *M. luteus* had zero lung genomes and zero detected patient engraftability. This **qualifies** engraftability as an inferred objective: prevalence and transcriptional activity provide a prioritization signal, but do not establish post-administration persistence. [src: cf_formulation_design]

## Direct interactions and formulation robustness

Pairwise interaction measurements further **support** a mixed-mechanism interpretation but remain provisional. Mean synergy scores were +5.3% for *N. mucosa* + ASMA-2260, +1.4% for ASMA-3913 + ASMA-2260, −2.2% for *N. mucosa* + ASMA-2464, −14.2% for ASMA-3913 + ASMA-2464, and −19.8% for ASMA-1478 + ASMA-1197. Overall mean synergy was −5.8% across only 8 comparisons and 5 unique pairs. [src: cf_formulation_design] These results connect to [[concepts/cofitness-network-architecture]]: combining individually inhibitory organisms does not guarantee additive or synergistic community inhibition. [src: cf_formulation_design]

The strict-safe two-species candidate, *R. dentocariosa* plus *N. mucosa*, provided 84% mean inhibition and combined engraftability of 0.820. The candidate isolates included strong planktonic performers, including 88% best inhibition for *N. mucosa* and 79% for *R. dentocariosa*. These measurements support the primary-candidate recommendation but do not establish protection against established airway biofilms. [src: cf_formulation_design]

The strict-safe optimization filtered candidate species before ranking formulations, so the reported optima represent tradeoffs within a safety-constrained candidate set rather than unconstrained maximization of inhibition. Species-level pathway conservation across 499 genomes supported robustness checks: *M. luteus* showed 18/18 amino-acid pathways and 39/39 carbon pathways conserved at >95%; *S. salivarius* showed 18/18 and 32/35; *R. dentocariosa* showed 14/18 and 39/41; *N. mucosa* showed 16/16 and 27/27; and *G. sanguinis* showed 7/18 and 37/39, respectively. [src: cf_formulation_design]

These observations **support** [[concepts/pangenome-integration]] because conservation across genomes can test whether a proposed metabolic role is reproducible within a species, while not replacing direct safety or engraftment testing. [src: cf_formulation_design]

## Tensions and boundary conditions

The inhibition assays used planktonic cultures and PA14, whereas PA in cystic-fibrosis lungs primarily occupies structured biofilms. Strong planktonic candidate performance and metabolic prediction **contradict** neither the biofilm concern nor each other: the former is a direct assay result, while the latter identifies an unmeasured translation gap. [src: cf_formulation_design] The carbon panel contained 22 substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. Consequently, measured metabolic overlap may not capture resource competition or direct antagonism in airway biofilms. [src: cf_formulation_design]

The metabolic model covered 142 isolates representing 62 of 211 species (29%), and growth kinetics were available for only 32 isolates. The core cohort was enriched for deeply characterized taxa, including *Rothia*, *Streptococcus*, *Neisseria*, and *Gemella*. Pairwise interaction data covered only 3 A × 3 B isolate combinations and 8 comparisons across 5 unique pairs; the complete 10-pair interaction matrix for the five-species core had not been measured. [src: cf_formulation_design]

The pairwise database contained identical `fact_pairwise_interaction` and `fact_carbon_utilization` values, with correlation = 1.0 and mean difference = 0.0, so endpoint OD data could not assess per-substrate co-culture effects. Current interaction conclusions therefore relied on the RFU-based competition assay rather than endpoint-OD co-culture measurements. [src: cf_formulation_design]

The report recommends testing PAO1 and 3–5 mucoid clinical PA isolates because PA14-based inhibition measurements have not been validated against PAO1 or ExoS+ clinical strains, even though pangenome analysis found no amino-acid pathway differences between ExoU+ and ExoS+ PA. [src: cf_formulation_design] Genomic pathway conservation and patient transcriptional activity can refine candidate selection but do not demonstrate spatial colonization, biofilm competition, or protection from PA in vivo. [src: cf_formulation_design]

## Design principle

A defensible consortium-ranking framework should retain separate objectives for pathogen inhibition, resource-niche coverage, safety eligibility, and engraftability, then report the tradeoff surface rather than treating one composite score as definitive. This **extends** [[concepts/multi-omics-integration]] because the objectives draw on inhibition assays, carbon utilization, growth kinetics, patient metagenomics, metatranscriptomics, and pangenome pathway comparisons. [src: cf_formulation_design]

For this case, the evidence favors *R. dentocariosa* + *N. mucosa* as the primary candidate because it combines 84% mean inhibition with combined engraftability 0.820, while the *M. luteus*-containing k=3 formulation remains valuable as a coverage-maximizing hypothesis rather than a clinically established solution. [src: cf_formulation_design]

## Open Directions

- Measure the complete 10-pair interaction matrix for the five-species core with RFU-based competition assays and substrate-resolved co-cultures, including spatially structured co-cultures, to determine whether effects are additive, synergistic, or antagonistic. [src: cf_formulation_design]
- Repeat inhibition and carbon-utilization assays with PAO1 and 3–5 mucoid clinical PA isolates, then test the k=2 and k=3 formulations in mixed-species biofilm models to determine whether planktonic inhibition predicts biofilm biomass reduction or PA exclusion. [src: cf_formulation_design]
- Test biofilm models using mucins, lipids, iron, polyamines, xylitol, myoinositol, xylose, arabinose, and other genomically nominated sugar alcohols and pentoses; compare planktonic and biofilm phenotypes to quantify which condition-specific fitness measurements transfer. [src: cf_formulation_design]
- Track formulation species by strain-resolved metagenomics and metatranscriptomics during biofilm growth or an airway-relevant model, and administer the k=2 and k=3 formulations in an in vivo engraftment model, to test whether inferred engraftability predicts actual establishment and activity. [src: cf_formulation_design]
- Expand the matched isolate cohort and use held-out validation to determine whether genus-level residuals predict direct antagonism after controlling for metabolic overlap, growth kinetics, and phylogenetic relatedness. [src: cf_formulation_design]
- Combine metabolite profiling, transcriptomics, and targeted inhibition assays for *S. salivarius* ASMA-737, *G. sanguinis* ASMA-3044, and *N. mucosa* ASMA-3643 to identify mechanisms underlying their +74.1%, +62.2%, and +57.2% positive residuals. [src: cf_formulation_design]
- Experimentally test xylitol, myoinositol, xylose, and arabinose supplementation with the candidate commensals and PA, asking whether predicted pathway gaps create selective commensal growth without increasing PA growth. [src: cf_formulation_design]
- Recompute the multi-objective ranking with uncertainty intervals for inhibition, coverage, safety, and measured engraftment, asking whether the recommended formulation remains optimal when inferred objectives are replaced by direct measurements. [src: cf_formulation_design]
