---
type: "Research direction"
description: "No tested substrate favours commensals over PA14 (ratios 0.77-0.96 for the most selective), yet the k=3 formulation is modelled to cover PA14's niche fully. Does exclusion arise from combined substrate depletion, and not direct antagonism?"
hypothesis: "Inhibition of PA14 by the M. luteus + N. mucosa + S. salivarius formulation is relieved by adding back PA14's preferred substrates, and spent-medium depletion of those substrates scales with inhibition. This would indicate resource competition rather than direct antagonism."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Only 8 pairwise comparisons across 5 unique pairs exist; combination, depletion and add-back assays have not been run."
collections: []
findings: ["cf_formulation_design--8bf20af1", "cf_formulation_design--94972e2b", "cf_formulation_design--951bde52", "cf_formulation_design--c513d6f7"]
conflicts: []
papers: ["17873029", "35174108", "27881418"]
builds_on: ["findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--94972e2b", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--c513d6f7"]
projects: ["cf_formulation_design"]
topics: ["metabolic-models-and-pathway-level-evidence"]
---
# Does cooperative depletion of PA14's preferred substrates drive exclusion by multi-strain formulations?

No tested substrate favours commensals over PA14 (ratios 0.77-0.96 for the most selective), yet the k=3 formulation is modelled to cover PA14's niche fully. Does exclusion arise from combined substrate depletion, and not direct antagonism?

## Hypothesis

Inhibition of PA14 by the M. luteus + N. mucosa + S. salivarius formulation is relieved by adding back PA14's preferred substrates, and spent-medium depletion of those substrates scales with inhibition. This would indicate resource competition rather than direct antagonism.

## Why it matters

If depletion is the mechanism, formulations can be designed from substrate overlap. If inhibition is antagonistic or ignores coverage, additive scoring is the wrong model.

## How to test it

In co-culture with PA14, measure growth of M. luteus alone, pairs and the k=3 formulation in defined medium with PA14's preferred substrates. Quantify substrate depletion in spent medium, run substrate add-back rescue, and test cell-free supernatant for direct inhibition. Compare observed inhibition with the additive mean of single members (75% in the model) and with modelled niche coverage (18% to 100%). Run the xylitol, myoinositol, xylose, arabinose, fucose and rhamnose sole-carbon assay on the core species and PA14.

## What would support or refute it

Support: inhibition falls when preferred substrates are added back, tracks measured depletion, and is absent in cell-free supernatant. Refute: inhibition persists with add-back or supernatant, or does not scale with coverage. Departure from additivity alone cannot separate depletion from antagonism.

## Data

Approach: experiment. Readiness: needs new measurements. Only 8 pairwise comparisons across 5 unique pairs exist; combination, depletion and add-back assays have not been run.

## Builds on

- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--94972e2b|Adding Micrococcus luteus lifts modeled niche coverage to full]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--c513d6f7|Larger formulation sizes are statistically indistinguishable on composite score]] (Insufficient literature evidence)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.

PMID 17873029, 35174108 and 27881418 characterize CF sputum nutrients, commensal effects and environmental pseudomonad inhibition, but none tests whether substrate-coverage-designed formulations act through resource depletion.
