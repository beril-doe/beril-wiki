---
type: "Concept"
description: "Jointly balances inhibition, niche coverage, safety, and engraftability."
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Designing Protective Microbial Consortia Requires Joint Optimization of Inhibition, Coverage, Safety, and Engraftability

Protective microbial consortia should be designed as multi-objective formulations rather than selected solely for maximal pathogen inhibition, because inhibition, coverage of the pathogen's resource niche, safety constraints, and the probability of engraftment can favor different species or community sizes. The [[summaries/cf_formulation_design__REPORT]] provides a cystic-fibrosis airway case study centered on suppressing [[entities/pseudomonas-aeruginosa]] through metabolic competition and direct antagonism. [src: cf_formulation_design]

## Evidence for a multi-objective design problem

Metabolic overlap with PA14 significantly predicted planktonic inhibition across 142 isolates with both measurements (r = 0.384, p = 2.3×10⁻⁶), but the metabolic model explained only R² = 0.274 of inhibition variance and explained R² = 0.360 after genus-level taxonomy was added. [src: cf_formulation_design]

This **supports** [[concepts/condition-specific-fitness]] by showing that resource-use similarity can contribute to competitive fitness, while also demonstrating that metabolism alone is insufficient: approximately 73% of inhibition variance remained unexplained, and genus contributed an additional 8.6% of explained variance, plausibly capturing species-specific direct antagonism. [src: cf_formulation_design]

Growth kinetics further separated possible mechanisms of protection. Commensals exceeded PA14's maximum growth rate in only 13.8% of substrate comparisons but began growing earlier in 43.1% of comparisons; adding kinetics to the metabolic model increased the fit to R² = 0.311 among the 29 isolates with all three assay types. [src: cf_formulation_design]

The results therefore **refine** a single-score view of inhibition: endpoint growth, lag-time advantage, and direct antagonism can contribute distinct evidence, and a formulation should not be judged from any one assay alone. [src: cf_formulation_design]

## Coverage and engraftability can oppose one another

Strict safety-filter optimization identified a five-species core of [[entities/neisseria-mucosa]], [[entities/streptococcus-salivarius]], [[entities/micrococcus-luteus]], [[entities/rothia-dentocariosa]], and [[entities/gemella-sanguinis]]. [src: cf_formulation_design]

The best strict-safe formulations varied across objectives: the k=1 formulation containing *N. mucosa* had 18% niche coverage, 88% inhibition, and engraftability 1.595; the k=2 formulation containing *R. dentocariosa* + *N. mucosa* had 18% coverage, 84% inhibition, and engraftability 0.820; the k=3 formulation containing *M. luteus* + *N. mucosa* + *S. salivarius* had 100% coverage, 75% inhibition, and engraftability 0.140; the k=4 formulation had 100% coverage, 76% inhibition, and engraftability 0.185; and the k=5 core had 100% coverage, 78% inhibition, and engraftability 0.188. [src: cf_formulation_design]

The k=3 formulation was the minimum size achieving complete PA14 niche coverage because *M. luteus* grew on 9 of PA14's 11 preferred substrates. [src: cf_formulation_design]

These results **support** [[concepts/competitive-exclusion-consortium-design]] as a coverage-versus-establishment problem: the formulation with complete niche coverage was not the formulation with the highest inferred engraftability. [src: cf_formulation_design]

Exhaustive enumeration of C(97,3) = 147,440 possible triples produced 127,598 valid unique-species formulations, and the k=3 combination was the global optimum with composite score 0.562. [src: cf_formulation_design]

However, bootstrap resampling over 1,000 replicates produced 95% composite-score confidence intervals of [0.753, 0.753] for k=1, [0.514, 0.588] for k=2, [0.551, 0.562] for k=3, [0.534, 0.578] for k=4, and [0.520, 0.587] for k=5; the k=2 through k=5 intervals overlapped. [src: cf_formulation_design]

The overlapping intervals **weaken** any claim that larger formulations are statistically preferable on the composite score, even though larger formulations can improve niche coverage. [src: cf_formulation_design]

## Engraftability is an inferred objective, not a demonstrated outcome

Among 134 species detected in patient metagenomes, the engraftability score, defined as prevalence × log(activity ratio), was highest for *N. mucosa* at 1.595; *R. dentocariosa* scored 0.422 and *S. salivarius* scored 0.172. [src: cf_formulation_design]

The report recommends k=2, *R. dentocariosa* + *N. mucosa*, as the primary clinical candidate because both species are lung-adapted, provide 84% mean inhibition, and have combined engraftability 0.820, nearly 6× higher than the k=3 formulation's 0.140. [src: cf_formulation_design]

The k=3 formulation is instead an aspirational second-line candidate contingent on demonstrating *M. luteus* engraftment in vivo, because *M. luteus* had zero lung genomes and zero detected patient engraftability despite its role in achieving 100% niche coverage. [src: cf_formulation_design]

This **qualifies** the use of engraftability in optimization: prevalence and transcriptional activity provide a prioritization signal, but they do not establish post-administration persistence. [src: cf_formulation_design]

## Safety and robustness constrain the feasible set

The strict-safe optimization explicitly filtered candidate species before ranking formulations, so the reported optima represent tradeoffs within a safety-constrained candidate set rather than unconstrained maximization of inhibition. [src: cf_formulation_design]

Species-level pathway conservation across 499 genomes supported robustness checks, with *M. luteus* showing 18/18 amino-acid pathways and 39/39 carbon pathways conserved at >95%; *S. salivarius* showing 18/18 and 32/35; *R. dentocariosa* showing 14/18 and 39/41; *N. mucosa* showing 16/16 and 27/27; and *G. sanguinis* showing 7/18 and 37/39, respectively. [src: cf_formulation_design]

These observations **support** [[concepts/pangenome-integration]] because conservation across genomes can test whether a proposed metabolic role is likely to be reproducible within a species, while not replacing direct safety or engraftment testing. [src: cf_formulation_design]

The formulation evidence remains provisional because inhibition was measured in planktonic assays against PA14, whereas cystic-fibrosis airway PA primarily occupies structured biofilms; the carbon panel contained 22 substrates and omitted mucins, lipids, iron, polyamines, and the sugar alcohols identified genomically. [src: cf_formulation_design]

Pairwise interaction evidence was also limited to 8 comparisons across 5 unique pairs, and the complete 10-pair interaction matrix for the five-species core had not been measured. [src: cf_formulation_design]

## Design principle

A defensible consortium-ranking framework should retain separate objectives for pathogen inhibition, resource-niche coverage, safety eligibility, and engraftability, then report the tradeoff surface rather than treating one composite score as a definitive answer. This **extends** [[concepts/multi-omics-integration]] because the relevant objectives draw on inhibition assays, carbon utilization, growth kinetics, patient metagenomics, metatranscriptomics, and pangenome pathway comparisons. [src: cf_formulation_design]

For this case, the evidence favors *R. dentocariosa* + *N. mucosa* as the primary candidate because it combines 84% mean inhibition with combined engraftability 0.820, while the *M. luteus*-containing k=3 formulation remains valuable as a coverage-maximizing hypothesis rather than a clinically established solution. [src: cf_formulation_design]

## Open Directions

- Measure the complete 10-pair interaction matrix for the five-species core with the RFU-based competition assay, then test whether pairwise effects are additive, synergistic, or antagonistic. [src: cf_formulation_design]
- Repeat inhibition and growth-kinetic assays with PAO1 and 3–5 mucoid clinical PA isolates, then ask whether the ranking of k=2 and k=3 formulations transfers beyond PA14. [src: cf_formulation_design]
- Test the candidate consortia in structured biofilm airway models using the omitted substrates and airway-relevant components, then determine whether planktonic inhibition predicts biofilm suppression. [src: cf_formulation_design]
- Administer the k=2 and k=3 formulations in an in vivo engraftment model and quantify persistence of each species, directly testing whether inferred engraftability predicts establishment. [src: cf_formulation_design]
- Experimentally test xylitol, myoinositol, xylose, and arabinose supplementation with the candidate commensals and PA, asking whether the predicted pathway gaps create selective commensal growth without increasing PA growth. [src: cf_formulation_design]
- Recompute the multi-objective ranking with uncertainty intervals for inhibition, coverage, safety, and measured engraftment, asking whether the recommended formulation remains optimal when inferred objectives are replaced by direct measurements. [src: cf_formulation_design]
