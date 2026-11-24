---
type: "Concept"
description: "Whether gene-fitness-derived traits such as metal tolerance measured in single-organism lab assays predict taxon abundance along field geochemical gradients; stops at this one site and genus-level matching."
sources: ["summaries/bacdive_metal_validation__REPORT.md", "summaries/lab_field_ecology__REPORT.md"]
---
# Laboratory fitness as a predictor of field abundance

Single-organism lab fitness in the Fitness Browser (FB) does not yet reliably predict taxon abundance along the Oak Ridge geochemical gradient. The one direct test gave a suggestive, nonsignificant correlation, and the evidence stops at one site and genus-level matching. [src: lab_field_ecology]

## The Oak Ridge test

The lab_field_ecology project defined a lab metal tolerance score as negative mean fitness under stress, so higher scores mean more tolerance. [src: lab_field_ecology] It correlated this score with the high-uranium/low-uranium field abundance ratio and found Spearman rho=0.503, p=0.095, n=12 genera. [src: lab_field_ecology] The trend ran in the predicted direction: genera with higher lab tolerance tended to be more abundant at contaminated sites. Power was limited by the small number of genera. [src: lab_field_ecology] The bacdive_metal_validation report cites the same result as rho=0.50, p=0.095, n=11 genera. [src: bacdive_metal_validation] That report gives n=11 where lab_field_ecology gives n=12, and neither report explains the difference. The report claims this is the first study to link FB lab fitness directly to ENIGMA CORAL field community composition across a geochemical gradient. [src: lab_field_ecology]

## Relation to the BacDive analysis

The bacdive_metal_validation report calls its BacDive analysis stronger evidence for the same hypothesis at much larger scale (n=10 for heavy metal, n=176 for all contamination, d=+0.43-1.00). [src: bacdive_metal_validation] It attributes the difference in significance to the power gained from BacDive's larger sample. [src: bacdive_metal_validation] This is that report's own reading. The two analyses use different data, so the comparison is not a direct replication. See [[concepts/validating-metal-tolerance-predictions-against-culture-collection-metadata]].

## Why lab fitness may not transfer

The report proposes three explanations. These are hypotheses and were not tested.

- Field sites vary in pH, redox potential, carbon sources, sulfate, nitrate and other parameters. A metal-tolerant organism may lack the metabolism a given site needs. [src: lab_field_ecology]
- Field competition, cross-feeding and syntrophy are absent from single-organism fitness. [src: lab_field_ecology] The report cites LaSarre et al. (2020), who showed that coculture interactions are "not necessarily predictable a priori" from single-organism fitness. The report treats this as parallel to its own result. [src: lab_field_ecology]
- 16S amplicons resolve only to genus, but FB organisms are specific strains. A genus such as *Pseudomonas* contains thousands of species with different ecologies. [src: lab_field_ecology] See [[concepts/genus-level-amplicon-resolution-and-rare-taxon-limits-in-matching-reference-organisms-to-field-data]].

## Further limits

- The tolerance score is a crude aggregate. [src: lab_field_ecology]
- The analysis did not control for pH, dissolved oxygen or carbon sources. [src: lab_field_ecology]
- *Rhodanobacter* is not in the FB, although it dominates contaminated Oak Ridge wells. [src: lab_field_ecology] See [[entities/rhodanobacter]].
- The report cites Peng et al. (2022), who found that Oak Ridge *Rhodanobacter* strains acquired metal resistance by horizontal gene transfer. [src: lab_field_ecology] It also notes that its costly_dispensable_genes project found metal resistance genes enriched in the accessory genome. [src: lab_field_ecology]

## Proposed next steps in the report

The report proposes using metagenomic data, if available in the ENIGMA CORAL genome and assembly tables, instead of 16S amplicons to match FB organisms at species or strain level. [src: lab_field_ecology] It also proposes computing per-metal fitness scores, such as uranium-specific and chromium-specific, and correlating them with the matching metal concentrations at each Oak Ridge site. [src: lab_field_ecology]

## Open Directions

- Match FB organisms to metagenome-assembled data at species or strain level, which would address the genus-level mismatch.
- Replace the aggregate score with per-metal fitness scores correlated with each site's metal concentration.
- Add pH, dissolved oxygen and carbon sources as covariates, to test whether confounding hides or creates the trend.
- Add *Rhodanobacter* to the FB so the dominant contaminated-site genus can be tested.
- Extend the test to more genera or sites, to raise power beyond n=12.
