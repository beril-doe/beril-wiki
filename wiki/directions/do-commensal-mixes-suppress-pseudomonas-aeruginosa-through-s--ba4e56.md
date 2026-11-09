---
type: "Research direction"
description: "If no single substrate favours commensals over the PA14 reference strain, does a three-member commensal formulation that covers PA14's preferred substrates inhibit it more than its members' individual effects would predict?"
hypothesis: "The combination of Micrococcus luteus, Neisseria mucosa and Streptococcus salivarius inhibits PA14 more than the average of its members, because together they deplete PA14's preferred substrates, and the extra suppression disappears if those substrates are added back."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Only a few pairwise combinations have been measured, and all assays used PA14, so combination and non-PA14 results require new growth experiments."
collections: []
findings: ["cf_formulation_design--94972e2b", "cf_formulation_design--8bf20af1", "cf_formulation_design--951bde52", "cf_formulation_design--c513d6f7", "cf_formulation_design--1799127b"]
conflicts: []
papers: ["17873029", "35174108", "27881418", "25036925", "40818976", "19936230"]
builds_on: ["findings/cf_formulation_design--94972e2b", "findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--c513d6f7", "findings/cf_formulation_design--1799127b"]
projects: ["cf_formulation_design"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do commensal mixes suppress Pseudomonas aeruginosa through shared resource depletion beyond members alone?

If no single substrate favours commensals over the PA14 reference strain, does a three-member commensal formulation that covers PA14's preferred substrates inhibit it more than its members' individual effects would predict?

## Hypothesis

The combination of Micrococcus luteus, Neisseria mucosa and Streptococcus salivarius inhibits PA14 more than the average of its members, because together they deplete PA14's preferred substrates, and the extra suppression disappears if those substrates are added back.

## Why it matters

Prebiotic selection failed on every tested substrate, and the formulation score assumes members act additively with only a few pairs measured. A real synergy, or its absence, decides whether formulations can be designed from substrate overlap or must be built by direct testing.

## How to test it

Grow PA14, and separately an ExoS-positive strain of the PAO1 type, with each member alone, all pairs, and the three-member mix in a defined medium with the preferred substrates present. Repeat with the preferred substrates supplemented in excess. Compare observed inhibition with the average of the members' individual effects.

## What would support or refute it

Support: the mix beats the member average on both strains and the advantage shrinks when substrates are supplemented. Refute: the mix equals the average, or the advantage persists with excess substrate, pointing to direct antagonism rather than resource depletion.

## Data

Approach: experiment. Readiness: needs new measurements. Only a few pairwise combinations have been measured, and all assays used PA14, so combination and non-PA14 results require new growth experiments.

## Builds on

- Finding: [[findings/cf_formulation_design--94972e2b|Adding Micrococcus luteus lifts modeled niche coverage to full]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--c513d6f7|Larger formulation sizes are statistically indistinguishable on composite score]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 25036925](https://pubmed.ncbi.nlm.nih.gov/25036925/) Predominant pathogen competition and core microbiota divergence in chronic airway infection.
- [PMID 40818976](https://pubmed.ncbi.nlm.nih.gov/40818976/) Synergistic effects of commensals and phage predation in suppressing colonization by pathogenic Vibrio parahaemolyticus.
- [PMID 19936230](https://pubmed.ncbi.nlm.nih.gov/19936230/) Pseudomonas aeruginosa population structure revisited.

PMIDs 17873029 and 35174108 describe sputum carbon preferences and commensals in the cystic fibrosis airway, and PMID 40818976 shows commensals and phage working together against another pathogen. None tests whether a substrate-coverage-designed commensal mix acts beyond its members' average.
