---
type: "Concept"
description: "Sparse pairwise assays limit reliable prediction of multispecies community effects"
sources: ["summaries/cf_formulation_design__REPORT.md"]
---
# Sparse Pairwise Interaction Data Limit Prediction of Multi-Species Community Effects

Pairwise interaction measurements are insufficient for confidently predicting the effects of a multi-species formulation when the tested isolate combinations are few, the interaction matrix is incomplete, and the assay does not resolve the relevant ecological mechanism. In [[summaries/cf_formulation_design__REPORT]], pairwise evidence was used to inform a proposed competitive-exclusion consortium, but the resulting additive formulation scores remain provisional. [src: cf_formulation_design]

## Evidence from the formulation study

The study analyzed only 8 pairwise comparisons across 5 unique pairs, including 3 A × 3 B isolate combinations, rather than the complete interaction structure of the proposed five-species core. [src: cf_formulation_design] The complete 10-pair interaction matrix for the five-species core had not been measured. [src: cf_formulation_design]

Observed mean synergy scores varied substantially among tested pairs: +5.3% for *Neisseria mucosa* + ASMA-2260, +1.4% for ASMA-3913 + ASMA-2260, −2.2% for *N. mucosa* + ASMA-2464, −14.2% for ASMA-3913 + ASMA-2464, and −19.8% for ASMA-1478 + ASMA-1197. [src: cf_formulation_design] The overall mean synergy was −5.8%, but this estimate was based on only 8 comparisons across 5 unique pairs. [src: cf_formulation_design]

This sparse design limits extrapolation from pairwise effects to the proposed multispecies communities: a positive or near-additive result for one pair does not establish that the same species will remain compatible in a larger consortium, while a negative pairwise interaction may reflect isolate-specific or condition-specific behavior rather than a universal species-level incompatibility. The report therefore treated additive formulation scoring as provisional. [src: cf_formulation_design]

## Measurement and representation limitations

The interaction data could not be interpreted as a complete per-substrate co-culture experiment because `fact_pairwise_interaction` was identical to `fact_carbon_utilization`, with correlation = 1.0 and mean difference = 0.0. [src: cf_formulation_design] Consequently, the interaction conclusions relied on the RFU-based competition assay rather than endpoint optical-density data assessing per-substrate co-culture effects. [src: cf_formulation_design]

The proposed five-species core comprised *N. mucosa*, *Streptococcus salivarius*, *Micrococcus luteus*, *Rothia dentocariosa*, and *Gemella sanguinis*, but the report had not measured its complete 10-pair interaction matrix. [src: cf_formulation_design] This gap is especially consequential because the formulation optimizer selected a k=3 combination, *M. luteus* + *N. mucosa* + *S. salivarius*, as the global optimum among 127,598 valid unique-species formulations, while the available pairwise measurements did not provide full interaction coverage for that community. [src: cf_formulation_design]

The limitation connects directly to [[concepts/competitive-exclusion-consortium-design]]: niche coverage and inhibition scores can identify plausible members, but they do not by themselves establish that the members will coexist or jointly suppress the target. [src: cf_formulation_design] It also refines [[concepts/cofitness-network-architecture]], because sparse pairwise edges cannot determine the architecture of a larger interaction network when unmeasured edges may alter community behavior. [src: cf_formulation_design]

## Relationship to assay context

The inhibition assays were planktonic, whereas *Pseudomonas aeruginosa* in cystic-fibrosis lungs primarily occupies structured biofilms. [src: cf_formulation_design] Thus, even a more complete planktonic pairwise matrix would not by itself establish multispecies performance in the biofilm context relevant to the intended application. [src: cf_formulation_design] This limitation links the concept to [[concepts/planktonic-to-biofilm-translation]] and [[concepts/condition-specific-fitness]]. [src: cf_formulation_design]

The formulation report combined pairwise interactions with carbon utilization, growth kinetics, patient metagenomics, metatranscriptomics, and pangenome analysis, but the pairwise component remained the least complete evidence for assigning additive or synergistic community effects. [src: cf_formulation_design] This is a case for [[concepts/multi-omics-integration]] in which complementary data improve candidate selection but do not replace direct measurement of higher-order interactions. [src: cf_formulation_design]

## Interpretation

The available data support the hypothesis that pairwise competition can contribute to multispecies formulation design, but they do not establish that pairwise synergy or antagonism is transferable to the full consortium. [src: cf_formulation_design] The strongest defensible conclusion is therefore candidate prioritization, not validated prediction of community-level suppression. [src: cf_formulation_design]

## Open Directions

- Measure all 10 pairwise interactions among the five proposed core species using the same RFU-based competition assay, then test whether the observed edges predict the k=3 and k=5 formulation outcomes. [src: cf_formulation_design]
- Repeat the complete pairwise matrix and the candidate formulations in structured biofilm models, asking whether planktonic synergy scores predict biofilm inhibition of *P. aeruginosa*. [src: cf_formulation_design]
- Separate per-substrate co-culture effects from endpoint carbon-utilization measurements by generating substrate-resolved co-culture data, asking whether competition is additive, synergistic, or antagonistic on the 22 tested substrates. [src: cf_formulation_design]
- Expand the isolate-by-isolate interaction design beyond the 3 A × 3 B combinations and use a hierarchical model to test whether interaction effects are species-level, isolate-specific, or condition-specific. [src: cf_formulation_design]
- Test the candidate formulations against PAO1 and 3–5 mucoid clinical *P. aeruginosa* isolates, asking whether pairwise and community effects transfer beyond PA14. [src: cf_formulation_design]
