---
type: "Research direction"
description: "Is commensal suppression of P. aeruginosa PA14 driven by community-level depletion of its preferred substrates, given that no single substrate favored commensals?"
hypothesis: "Suppression needs live commensal cells consuming PA14's preferred substrates. Cell-free spent medium will not suppress, and adding back the depleted substrates will restore PA14 growth."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Needs new culture experiments; lakehouse data only predict substrate overlap."
collections: []
findings: ["cf_formulation_design--8bf20af1", "cf_formulation_design--94972e2b", "cf_formulation_design--951bde52", "cf_formulation_design--c513d6f7"]
conflicts: []
papers: ["17873029", "27881418", "35174108", "25036925", "40818976"]
builds_on: ["findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--94972e2b", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--c513d6f7"]
projects: ["cf_formulation_design"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do cystic fibrosis commensals suppress Pseudomonas by depleting shared nutrients?

Is commensal suppression of P. aeruginosa PA14 driven by community-level depletion of its preferred substrates, given that no single substrate favored commensals?

## Hypothesis

Suppression needs live commensal cells consuming PA14's preferred substrates. Cell-free spent medium will not suppress, and adding back the depleted substrates will restore PA14 growth.

## Why it matters

It would define a design rule for probiotic formulations, which would be built around combined substrate coverage rather than a selective prebiotic.

## How to test it

Co-culture PA14 with Micrococcus luteus, Neisseria mucosa and Streptococcus salivarius, singly and combined, in a sputum-like medium. Compare with cell-free spent medium, and with co-culture supplemented with PA14's preferred substrates. Measure PA14 growth and the pair-wise combined effects that the additive assumption leaves untested.

## What would support or refute it

Supported if inhibition needs cells and is reversed by substrate add-back. Refuted if spent medium inhibits or add-back changes nothing, pointing to secreted inhibitors.

## Data

Approach: experiment. Readiness: needs new measurements. Needs new culture experiments; lakehouse data only predict substrate overlap.

## Builds on

- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--94972e2b|Adding Micrococcus luteus lifts modeled niche coverage to full]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--c513d6f7|Larger formulation sizes are statistically indistinguishable on composite score]] (Insufficient literature evidence)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.
- [PMID 25036925](https://pubmed.ncbi.nlm.nih.gov/25036925/) Predominant pathogen competition and core microbiota divergence in chronic airway infection.
- [PMID 40818976](https://pubmed.ncbi.nlm.nih.gov/40818976/) Synergistic effects of commensals and phage predation in suppressing colonization by pathogenic Vibrio parahaemolyticus.

PMID 17873029 described P. aeruginosa carbon preferences in sputum, and PMIDs 27881418 and 35174108 showed commensal inhibition. None tests depletion as the mechanism.
