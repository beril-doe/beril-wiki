---
type: "Research direction"
description: "Does lung-associated streamlining of sugar catabolism in P. aeruginosa leave amino acid use intact, so that commensals exclude it through community-level resource depletion and not through a selective substrate?"
hypothesis: "Lung PA genomes lose sugar pathways but keep amino acid catabolism, and a multi-commensal formulation suppresses ExoS+ PA strains through joint depletion, with a combined effect that departs from the mean of its members."
approach: "analysis then experiment"
readiness: "needs new measurements"
readiness_basis: "Genome-side comparison is in the lakehouse, but all inhibition data are PA14 and non-PA14 co-cultures are new."
collections: ["protect-genomedepot", "kbase-ke-pangenome"]
findings: ["cf_formulation_design--460ed03a", "cf_formulation_design--8bf20af1", "cf_formulation_design--94972e2b", "cf_formulation_design--951bde52", "cf_formulation_design--1799127b"]
conflicts: []
papers: ["17873029", "25409940", "31214142", "35174108", "27881418", "25036925"]
builds_on: ["findings/cf_formulation_design--460ed03a", "findings/cf_formulation_design--8bf20af1", "findings/cf_formulation_design--94972e2b", "findings/cf_formulation_design--951bde52", "findings/cf_formulation_design--1799127b"]
projects: ["cf_formulation_design"]
topics: ["data-infrastructure-provenance-and-research-practice"]
---
# Lung adaptation shortens Pseudomonas carbon repertoires, leaving commensals no selective substrate

Does lung-associated streamlining of sugar catabolism in P. aeruginosa leave amino acid use intact, so that commensals exclude it through community-level resource depletion and not through a selective substrate?

## Hypothesis

Lung PA genomes lose sugar pathways but keep amino acid catabolism, and a multi-commensal formulation suppresses ExoS+ PA strains through joint depletion, with a combined effect that departs from the mean of its members.

## Why it matters

It would shift probiotic design for CF infection from picking a prebiotic to assembling guilds that jointly deplete PA's preferred resources.

## How to test it

Compare GapMind pathway scores in lung versus non-lung PA genomes with phylogeny controlled. Then co-culture ExoS+ (PAO1-type) and ExoU+ PA strains, not only PA14, with the k=3 formulation (M. luteus, N. mucosa, S. salivarius) versus its members, measuring the combined inhibition and substrate depletion directly instead of assuming additivity.

## What would support or refute it

Support: lung strains show lower sugar scores (e.g. sorbitol -0.165) with amino acid pathways retained, and formulation inhibition departs from additivity. Refute: lung PA keep sugar pathways under phylogenetic control, or one substrate gives a clear commensal advantage.

## Data

Approach: analysis then experiment. Readiness: needs new measurements. Genome-side comparison is in the lakehouse, but all inhibition data are PA14 and non-PA14 co-cultures are new.

- Collection: [[data/protect-genomedepot|PROTECT Pathogen Browser]]
- Collection: [[data/kbase-ke-pangenome|Pangenome Collection]]

## Builds on

- Finding: [[findings/cf_formulation_design--460ed03a|Lung P. aeruginosa genomes score lower on sugar pathways than non-lung genomes]] (Extends retrieved work)
- Finding: [[findings/cf_formulation_design--8bf20af1|No tested substrate gives commensals a clear advantage over PA14]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--94972e2b|Adding Micrococcus luteus lifts modeled niche coverage to full]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--951bde52|Metabolic overlap with PA14 predicts inhibition, but only modestly]] (Insufficient literature evidence)
- Finding: [[findings/cf_formulation_design--1799127b|Cystic fibrosis P. aeruginosa is mostly ExoS+, unlike the PA14 assay strain]] (Extends retrieved work)

## Closest published work

- [PMID 17873029](https://pubmed.ncbi.nlm.nih.gov/17873029/) Nutritional cues control Pseudomonas aeruginosa multicellular behavior in cystic fibrosis sputum.
- [PMID 25409940](https://pubmed.ncbi.nlm.nih.gov/25409940/) Impact of glycerol-3-phosphate dehydrogenase on virulence factor production by Pseudomonas aeruginosa.
- [PMID 31214142](https://pubmed.ncbi.nlm.nih.gov/31214142/) Catabolism of Nucleic Acids by a Cystic Fibrosis Pseudomonas aeruginosa Isolate: An Adaptive Pathway to Cystic Fibrosis Sputum Environment.
- [PMID 35174108](https://pubmed.ncbi.nlm.nih.gov/35174108/) Commensal Bacteria in the Cystic Fibrosis Airway Microbiome Reduce P. aeruginosa Induced Inflammation.
- [PMID 27881418](https://pubmed.ncbi.nlm.nih.gov/27881418/) Environmental Pseudomonads Inhibit Cystic Fibrosis Patient-Derived Pseudomonas aeruginosa.
- [PMID 25036925](https://pubmed.ncbi.nlm.nih.gov/25036925/) Predominant pathogen competition and core microbiota divergence in chronic airway infection.

PMID 25409940 and PMID 31214142 describe carbon use by single CF isolates and PMID 17873029 gives sputum carbon preferences; none tests genome-wide streamlining or non-additive multi-strain exclusion.
