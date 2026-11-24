---
type: "Organism"
description: "Pseudomonad species whose BacDive strains provide the species-level utilization baseline."
sources: ["summaries/fw300_metabolic_consistency__REPORT.md", "summaries/pseudomonas_carbon_ecology__REPORT.md"]
aliases: ["Pseudomonas_E fluorescens_E"]
---
# Pseudomonas fluorescens

This page covers Pseudomonas fluorescens, also known as Pseudomonas_E fluorescens_E. Its BacDive strains provide the species-level utilization baseline. [src: fw300_metabolic_consistency]

## Key facts

- BacDive aggregates P. fluorescens strains across a broad clade, which GTDB reclassification designates Pseudomonas_E fluorescens_E. [src: fw300_metabolic_consistency]
- The P. fluorescens group is described in the literature (Silby et al. 2011; Loper et al. 2012, as cited in the pseudomonas_carbon_ecology report) as metabolically diverse, with ~54% of the pangenome encoding variable metabolic capabilities. [src: pseudomonas_carbon_ecology]

## BacDive utilization baseline

The overall BacDive baseline for P. fluorescens is 22/80 = 27.5% utilization. FW300-N2E3 produces metabolites that BacDive strains use at 3/7 = 43%. A binomial test found no significant difference (p = 0.40), so the strain's metabolites are used at a rate consistent with the species norm. [src: fw300_metabolic_consistency]

Tryptophan is a clear case. 0 of 50 P. fluorescens strains in BacDive use it as a carbon source, which the report classes as high confidence (per-strain consensus). [src: fw300_metabolic_consistency] The report notes this fits published work on cross-feeding. It cites Sibanyoni et al. (2025) for amino acid cross-feeding between Priestia megaterium and P. fluorescens in the rhizosphere. [src: fw300_metabolic_consistency]

[[entities/trehalose]] use varies between strains: 1 of 6 were positive. [src: fw300_metabolic_consistency]

## Caveats

Strain variation limits the species consensus. The report deduplicates per strain by majority vote before computing rates. Even so, a species consensus may not reflect what FW300-N2E3 itself can do, as the trehalose result (1/6 positive) shows. [src: fw300_metabolic_consistency] See [[concepts/reliability-of-species-level-bacdive-consensus-phenotypes]], [[concepts/metabolite-production-versus-utilization-discordance]] and [[summaries/fw300_metabolic_consistency__REPORT]].
