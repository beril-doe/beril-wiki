---
type: "Compound"
description: "Rhamnose, a plant-derived sugar that appears in this corpus both as a genomic pathway marker for Pseudomonas environment classification and as a candidate selective prebiotic, with the caveat that its selectivity is predicted from pathway completeness rather than measured growth."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/functional_dark_matter__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
---
Rhamnose is a sugar described as a plant cell wall component, and it appears in this corpus both as a genomic pathway marker and as a candidate prebiotic substrate [src: pseudomonas_carbon_ecology, cf_formulation_design]. Source tables refer to it as "Rhamnose" and, in gap listings, as "Rhamnose utilization" [src: functional_dark_matter].

## Candidate selective prebiotic in consortium design

In the cystic fibrosis formulation-design project, the rhamnose row reports 1% pathway completeness for *Pseudomonas aeruginosa* (PA) against 100% completeness in [[entities/neisseria-mucosa]] (*N. mucosa*) and [[entities/gemella-sanguinis]] (*G. sanguinis*), with a reported selectivity of 0.99 [src: cf_formulation_design].

That selectivity is a genomic prediction, not an observed growth result. The project's rationale frames the candidates as "100% commensal pathway completeness vs 0% PA" and states explicitly that the prediction "must be validated experimentally"; the same report's Section 2.11 is narrower, giving PA fucose and rhamnose completeness as 1% and tying other candidates to single carriers (xylitol completeness 98% in *Streptococcus salivarius*) [src: cf_formulation_design].

The wider claim — that genomic pathway comparison yields sugar alcohol prebiotics as a strategy "qualitatively different from amino acid supplementation" — is therefore a hypothesis rather than a demonstrated result: growth selectivity remains untested, each candidate pathway occurs in only 1–2 core species, xylitol completeness is 98% in *Streptococcus salivarius*, and PA fucose and rhamnose completeness is 1% [src: cf_formulation_design]. See [[concepts/computational-pathway-prediction-validation]] and [[concepts/competitive-exclusion-consortium-design]].

## Pathway completeness across Pseudomonas

In the *Pseudomonas* carbon-ecology project, within a subgenus-level comparison (*Pseudomonas* sensu stricto versus *Pseudomonas_E* species), "rhamnose and fucose are more complete in *P. aeruginosa* (66.8%) than *P. fluorescens* group (41.3% and 45.1% respectively), though this difference was not statistically significant after FDR correction" — FDR (false discovery rate) correction being the multiple-testing adjustment applied across the pathway comparisons [src: pseudomonas_carbon_ecology]. The contrast is thus a null result at the resolution available, not a demonstrated clade difference, and the figure is reported inside a group-level analysis rather than as a standalone species-level completeness value [src: pseudomonas_carbon_ecology].

Rhamnose nevertheless carried weight as a predictive feature: among the top environment-classifier pathways it ranked third with importance 0.086, behind D-serine (0.132, associated with rhizosphere niches) and arabinose (0.094), and ahead of fucose (0.085) and xylose (0.070) [src: pseudomonas_carbon_ecology].

## Utilization gaps in fitness-data organisms

Rhamnose utilization is listed as a carbon-source gap in 31 organisms, with Marinobacter, *P. putida* and Phaeo given as examples [src: functional_dark_matter]. Such gaps are candidates for the prioritization logic discussed in [[concepts/experimental-prioritization-of-functional-dark-matter]].

## Tensions

Within cf_formulation_design, the rationale's blanket "100% commensal pathway completeness vs 0% PA" does not match the project's own per-pathway numbers, which give PA rhamnose completeness as 1% and 100% completeness only for *N. mucosa* and *G. sanguinis* [src: cf_formulation_design]. The report does not explain the inconsistency between the 0% framing and the 1% table value, so it is recorded here as an unresolved internal discrepancy and is not averaged or reconciled.

Across projects, the two reports characterise PA differently: cf_formulation_design treats near-absent rhamnose capability in PA (1%) as the basis for selectivity, while pseudomonas_carbon_ecology reports rhamnose completeness in *P. aeruginosa* at 66.8% inside a subgenus-level comparison whose difference from the *P. fluorescens* group did not survive FDR correction [src: cf_formulation_design, pseudomonas_carbon_ecology]. Neither source addresses the other, and neither states why the values differ; differences in genome panel, aggregation level or completeness definition are only hypotheses, untested in this corpus. The discrepancy is left open: settling which value applies to a clinical formulation would require a recomputation of rhamnose pathway completeness on a single declared genome set.

## Related pages

- [[concepts/computational-pathway-prediction-validation]] — rhamnose selectivity is a genomic prediction that "must be validated experimentally" [src: cf_formulation_design]
- [[concepts/null-results-under-limited-statistical-resolution]] — the *P. aeruginosa* versus *P. fluorescens* group rhamnose/fucose contrast was not significant after FDR correction [src: pseudomonas_carbon_ecology]
- [[concepts/metabolic-capacity-specialization]] — rhamnose ranked third (importance 0.086) among environment-classifier pathways [src: pseudomonas_carbon_ecology]
- [[entities/fucose]], [[entities/xylitol]], [[entities/xylose]], [[entities/arabinose]] — sugars tabulated alongside rhamnose in these projects [src: cf_formulation_design, pseudomonas_carbon_ecology]
