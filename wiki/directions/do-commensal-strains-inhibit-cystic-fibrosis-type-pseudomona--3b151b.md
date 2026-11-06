---
type: "Research direction"
description: "All inhibition assays used PA14, which carries the ExoU toxin and makes only the Pel matrix, whereas among 291 cystic fibrosis isolates 94% carry ExoS and 5% carry ExoU, a very different mix from environmental isolates. Does a commensal's shared nutrient use with PA14 predict how strongly it inhibits typical ExoS-carrying cystic fibrosis isolates?"
hypothesis: "Metabolic overlap with PA14 predicts inhibition of PA14 only modestly and predicts inhibition of ExoS-carrying cystic fibrosis isolates still less. Interference mechanisms, not nutrient overlap, will explain a larger share against those isolates."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Genome-based classification of toxin type exists for 6,760 genomes, but all inhibition measurements were made with PA14 only and have not been validated against ExoS-positive or PAO1-type strains."
collections: ["kbase-ke-pangenome", "protect-genomedepot"]
findings: ["cf_formulation_design--1799127b", "cf_formulation_design--951bde52", "cf_formulation_design--8bf20af1"]
conflicts: []
papers: ["19936230", "27881418", "17873029", "25036925", "42151817"]
builds_on: ["findings/cf_formulation_design--1799127b", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--8bf20af1"]
projects: ["cf_formulation_design"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Do commensal strains inhibit cystic fibrosis-type Pseudomonas as well as the PA14 test strain?

All inhibition assays used PA14, which carries the ExoU toxin and makes only the Pel matrix, whereas among 291 cystic fibrosis isolates 94% carry ExoS and 5% carry ExoU, a very different mix from environmental isolates. Does a commensal's shared nutrient use with PA14 predict how strongly it inhibits typical ExoS-carrying cystic fibrosis isolates?

## Hypothesis

Metabolic overlap with PA14 predicts inhibition of PA14 only modestly and predicts inhibition of ExoS-carrying cystic fibrosis isolates still less. Interference mechanisms, not nutrient overlap, will explain a larger share against those isolates.

## Why it matters

A formulation designed on PA14 could fail on the strains patients actually carry. This would show whether nutrient competition is a transferable design rule.

## How to test it

Grow the 142-isolate commensal set against PA14, PAO1 and cystic fibrosis isolates that are ExoS-positive and ExoU-negative. Compare inhibition rankings. For each target strain, compute metabolic overlap using that strain's own substrate preferences, and test whether it predicts inhibition better than PA14 overlap. Use spent-medium and contact-free assays to separate nutrient depletion from secreted inhibitors.

## What would support or refute it

Support: rankings differ between PA14 and ExoS-positive isolates, and strain-specific overlap does not predict inhibition. Refutation: rankings match and strain-specific overlap predicts inhibition about as well as for PA14.

## Data

Approach: experiment. Readiness: needs new measurements. Genome-based classification of toxin type exists for 6,760 genomes, but all inhibition measurements were made with PA14 only and have not been validated against ExoS-positive or PAO1-type strains.

- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]
- Collection: [[data/protect-genomedepot|PROTECT Pathogen Browser]]

## Builds on

- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)

## Closest published work

- [PMID 19936230](https://pubmed.ncbi.nlm.nih.gov/19936230/) Pseudomonas aeruginosa population structure revisited.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 25036925](https://pubmed.ncbi.nlm.nih.gov/25036925/) Predominant pathogen competition and core microbiota divergence in chronic airway infection.
- [PMID 42151817](https://pubmed.ncbi.nlm.nih.gov/42151817/) Characterization of two exoU+/exoS+ carbapenem-non-susceptible Pseudomonas aeruginosa co-colonizing the lung of a bacterial pneumonia patient.

PMID 27881418 shows environmental pseudomonads inhibit patient-derived Pseudomonas aeruginosa, and PMID 17873029 describes carbon preferences in sputum. Neither asks whether a nutrient-overlap rule built on one toxin-type strain transfers to the ExoS-dominant clinical population.
