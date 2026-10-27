---
type: "Finding"
description: "After phylum and genome-size control, 48 of 50 orthologous groups (96%) retain a positive plant-association coefficient that is large (|coef| > 0.2) and statistically significant at BH-FDR q < 0.05."
finding_id: "plant_microbiome_ecotypes--8106ac12"
result: "observation"
source: "plant_microbiome_ecotypes"
quantities: [{"value": "48 of 50", "what": "OGs retaining a positive, significant plant-association coefficient", "unit": "OGs", "denominator": "50 OGs", "scope": "phylum and genome-size control, BH-FDR q < 0.05"}, {"value": "96%", "what": "share of OGs retaining a positive, significant plant-association coefficient", "unit": "%", "denominator": "50 OGs", "scope": ""}]
caveat: "The model fit converged for 48/50 OGs; for COG2351 and COG5343 the design matrix was singular, likely perfect separation by a phylum dummy."
first_added: "2026-10-27"
source_hash: "ab4bafa20bb607a1edf87a293d67885cd96017817bfabdbff2c19bac9dc95272"
---
# Nearly all top plant-enriched gene families persist after phylum and genome-size control

After phylum and genome-size control, 48 of 50 orthologous groups (96%) retain a positive plant-association coefficient that is large (|coef| > 0.2) and statistically significant at BH-FDR q < 0.05. [src: plant_microbiome_ecotypes]

## Key figures

- **48 of 50 OGs**: OGs retaining a positive, significant plant-association coefficient (denominator 50 OGs; scope phylum and genome-size control, BH-FDR q < 0.05) [src: plant_microbiome_ecotypes]
- **96%**: share of OGs retaining a positive, significant plant-association coefficient (denominator 50 OGs) [src: plant_microbiome_ecotypes]

## Evidence

> **48 of 50 OGs (96%) retain a positive plant-association coefficient that is large (|coef| > 0.2) and statistically significant at BH-FDR q < 0.05** after phylum + log₁₀(genome_size) control. [src: plant_microbiome_ecotypes]

From the report [[summaries/plant_microbiome_ecotypes__REPORT]].

## Caveat

The model fit converged for 48/50 OGs; for COG2351 and COG5343 the design matrix was singular, likely perfect separation by a phylum dummy. [src: plant_microbiome_ecotypes]

> The model fit converged for 48/50 OGs; for the remaining two (COG2351 and COG5343) the design matrix was singular — likely perfect separation by a phylum dummy given their very strong raw prevalence gaps (62% vs 23% and 64% vs 21% respectively). [src: plant_microbiome_ecotypes]

## Other caveats in this report

- The original compartment PERMANOVA R² = 0.527 was largely a taxonomic-sampling artifact: excluding three dominant species reduced it to 0.072, although the reported per-marker enrichments persisted. The stated compartment counts do not sum to 1,136 and should not be silently reconciled. [src: plant_microbiome_ecotypes]
- The proposed purifying-selection explanation is an interpretation of mixed proxy evidence, not a direct demonstration of selection. [src: plant_microbiome_ecotypes]
- Co-occurring plant-associated genera show a small redundancy signal. The earlier extreme Cohen’s d = −7.54 largely resulted from using the SD of permutation means instead of the raw pair-level SD; corrected analyses yield about −0.4. [src: plant_microbiome_ecotypes]
- The reduction in COG3569 odds ratio from 8.92 to 6.01 indicates partial phylogenetic confounding. [src: plant_microbiome_ecotypes]
- NB02 classified 15,474/25,660 species (60.3%) as dual-nature by binary marker presence; NB07's weighted composite scheme classified 25.2% as dual-nature. The passage establishes different classification definitions but does not give an NB07 denominator. [src: plant_microbiome_ecotypes]
