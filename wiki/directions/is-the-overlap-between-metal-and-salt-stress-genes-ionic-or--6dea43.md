---
type: "Research direction"
description: "Of the metal-important gene records, 39.8 percent are also important under NaCl stress, and zinc sulfate, which adds no chloride, shows 44.6 percent overlap. Does the overlap come from osmotic load, from sodium or other ion effects, or from shared envelope damage?"
hypothesis: "Shared metal and salt genes reflect osmotic and membrane stress, so they also matter under an equal osmotic load without ions, such as sorbitol, and less so under KCl or choline chloride."
approach: "experiment"
readiness: "needs new measurements"
readiness_basis: "Existing data lack the matched osmotic and potassium controls."
collections: ["kescience-fitnessbrowser"]
findings: ["counter_ion_effects--5a2d3c21", "counter_ion_effects--482d2003", "counter_ion_effects--5c39821b", "counter_ion_effects--619981e8"]
conflicts: ["conflict--gene-essentiality--1ce33d4d"]
papers: ["27474723", "34432491", "12829273", "40302248"]
builds_on: ["findings/counter_ion_effects--5a2d3c21", "findings/counter_ion_effects--482d2003", "findings/counter_ion_effects--5c39821b", "findings/counter_ion_effects--619981e8", "conflicts/conflict--gene-essentiality--1ce33d4d"]
projects: ["counter_ion_effects", "metal_specificity"]
topics: ["gene-essentiality-and-perturbation-assay-validity"]
---
# Is the overlap between metal and salt stress genes ionic or osmotic?

Of the metal-important gene records, 39.8 percent are also important under NaCl stress, and zinc sulfate, which adds no chloride, shows 44.6 percent overlap. Does the overlap come from osmotic load, from sodium or other ion effects, or from shared envelope damage?

## Hypothesis

Shared metal and salt genes reflect osmotic and membrane stress, so they also matter under an equal osmotic load without ions, such as sorbitol, and less so under KCl or choline chloride.

## Why it matters

It would tell which metal-fitness genes are specific metal defences and which are general stress genes, and what a clean metal-specific list needs excluded.

## How to test it

In Desulfovibrio vulgaris Hildenborough and Pseudomonas stutzeri RCH2, run transposon-library fitness assays under zinc, cobalt and iron alongside NaCl, KCl, sorbitol and choline chloride at matched osmolarity. For the genes shared between metal and NaCl, ask which of the control conditions they also respond to.

## What would support or refute it

Osmotic cause supported: shared genes respond to sorbitol. Ionic cause supported: they respond to KCl or choline chloride but not sorbitol. Sodium-specific cause supported: they respond to NaCl only. Refutation of general stress: shared genes are absent from every control condition.

## Data

Approach: experiment. Readiness: needs new measurements. Existing data lack the matched osmotic and potassium controls.

- Collection: [[data/kescience-fitnessbrowser|Fitness Browser]]

## Builds on

- Finding: [[findings/counter_ion_effects--5a2d3c21|Large share of metal-important genes also matter under NaCl stress]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--482d2003|NaCl overlap does not track chloride delivered by the metal salt]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--5c39821b|DvH metal–NaCl fitness correlations vary widely; report attributes this to toxicity mechanism]] (Insufficient literature evidence)
- Finding: [[findings/counter_ion_effects--619981e8|Dose-dependent chloride effect on NaCl overlap rejected]] (Insufficient literature evidence)
- Conflict: [[conflicts/conflict--gene-essentiality--1ce33d4d|How Large Is the Overlap Between Metal-Fitness and Osmotic-Stress Genes?]]

## Closest published work

- [PMID 27474723](https://pubmed.ncbi.nlm.nih.gov/27474723/) Novel Metal Cation Resistance Systems from Mutant Fitness Analysis of Denitrifying Pseudomonas stutzeri.
- [PMID 34432491](https://pubmed.ncbi.nlm.nih.gov/34432491/) Deciphering Microbial Metal Toxicity Responses via Random Bar Code Transposon Site Sequencing and Activity-Based Metabolomics.
- [PMID 12829273](https://pubmed.ncbi.nlm.nih.gov/12829273/) Efflux-mediated heavy metal resistance in prokaryotes.
- [PMID 40302248](https://pubmed.ncbi.nlm.nih.gov/40302248/) High-Throughput Tn-Seq Screens Identify Both Known and Novel Pseudomonas putida KT2440 Genes Involved in Metal Tolerance.

PMID 27474723 and PMID 34432491 profile metal toxicity by transposon fitness. They do not separate osmotic from ionic causes using matched controls.
