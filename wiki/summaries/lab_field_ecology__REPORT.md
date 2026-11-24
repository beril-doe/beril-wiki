---
type: "Summary"
description: "Summary of the project Lab Fitness Predicts Field Ecology at Oak Ridge."
doc_type: "short"
full_text: "sources/lab_field_ecology__REPORT.md"
---
# Lab Fitness Predicts Field Ecology at Oak Ridge

This report asks whether Fitness Browser (FB) lab fitness predicts field ecology at Oak Ridge. Five of 11 tested FB genera correlate with uranium after false discovery rate (FDR) correction, which the report finds consistent with geochemistry shaping community structure. [src: lab_field_ecology] The lab-derived metal tolerance score is only suggestively, not significantly, correlated with field abundance ratio (rho=0.503, p=0.095, n=12 genera). [src: lab_field_ecology] The evidence is limited by genus-level resolution and few genera. [src: lab_field_ecology]

Power is limited by the small number of genera. [src: lab_field_ecology] The analysis used 108 overlapping samples, which may not capture the full range of Oak Ridge geochemistry. [src: lab_field_ecology]

## Key Findings

### Which Fitness Browser genera occur in the field

Of 26 unique genera represented in the Fitness Browser, 14 are detected in Oak Ridge groundwater communities via 16S amplicon sequencing. [src: lab_field_ecology]

The most prevalent are Sphingomonas (93% of 108 sites), Pseudomonas (91%), and Caulobacter (82%). [src: lab_field_ecology]

Desulfovibrio, the primary ENIGMA model organism, is detected at only 34% of sites at very low abundance (max 0.09% relative abundance). [src: lab_field_ecology]

Of 14 FB genera detected at Oak Ridge, 11 had sufficient prevalence (>=10 sites) for correlation analysis. [src: lab_field_ecology]

Three genera (Shewanella, Dechlorosoma, Marinobacter) were excluded due to low prevalence (<10 sites). [src: lab_field_ecology]

The report states that Rhodanobacter dominates contaminated Oak Ridge wells (Carlson et al. 2019). [src: lab_field_ecology] It is not in the Fitness Browser, and the report calls adding it a high-impact target. [src: lab_field_ecology]

### Genus abundance versus uranium (H2)

After BH-FDR (Benjamini-Hochberg false discovery rate) correction, 5 genera show significant correlations with uranium, in both directions. [src: lab_field_ecology]

The report calls H2 partially supported: 5 of 11 tested FB genera correlate with uranium after FDR correction (q<0.05), which it finds consistent with geochemistry shaping community structure. [src: lab_field_ecology]

| Genus | Spearman rho | p | FDR q | Direction at high uranium |
|---|---|---|---|---|
| Herbaspirillum | +0.336 | 3.8e-4 | 0.001 | more abundant [src: lab_field_ecology] |
| Bacteroides | +0.264 | 0.006 | 0.013 | more abundant [src: lab_field_ecology] |
| Caulobacter | -0.411 | 1.0e-5 | 1.1e-4 | less abundant [src: lab_field_ecology] |
| Sphingomonas | -0.382 | 4.5e-5 | 2.5e-4 | less abundant [src: lab_field_ecology] |
| Pedobacter | -0.266 | 0.005 | 0.013 | less abundant [src: lab_field_ecology] |

Azospirillum (rho=+0.20, p=0.042) is marginal after FDR correction (q=0.077). [src: lab_field_ecology]

Desulfovibrio shows no correlation (rho=0.022, p=0.82). [src: lab_field_ecology]

Pseudomonas shows no correlation (rho=-0.059, p=0.55), and both are ENIGMA model organisms. [src: lab_field_ecology]

The report says Desulfovibrio is rare in the 16S data (max 0.09% relative abundance), making correlation analysis unreliable. [src: lab_field_ecology]

The report calls Caulobacter and Sphingomonas sensitive indicators of uranium contamination, while Herbaspirillum and Bacteroides may be tolerant colonizers. [src: lab_field_ecology]

### Lab tolerance versus field abundance (H1)

The lab-derived metal tolerance score is the negative mean fitness under stress, with higher meaning more tolerant. [src: lab_field_ecology]

Its correlation with the high-uranium/low-uranium field abundance ratio is suggestive but not significant (Spearman rho=0.503, p=0.095, n=12 genera). [src: lab_field_ecology]

The trend is in the predicted direction, but statistical power is limited by the small number of genera. [src: lab_field_ecology]

### Community composition (H3)

Sites split at the median uranium concentration show distinct community compositions. [src: lab_field_ecology]

The top genera at high-uranium sites differ from low-uranium sites, with rare-biosphere taxa and subsurface specialists becoming more prominent at contaminated sites. [src: lab_field_ecology]

The report calls H3 partially supported: the shift is not simply "more metal-tolerant organisms" but reflects broader ecological restructuring, including changes in rare taxa, redox conditions, and carbon/energy sources. [src: lab_field_ecology]

### Proposed explanations for the lab-field gap

These are the report's proposals, not measurements.

Field sites vary in pH, redox potential, carbon sources, sulfate, nitrate, and dozens of other parameters beyond uranium, so an organism may tolerate metals in the lab but lack the metabolic capabilities for a particular site. [src: lab_field_ecology]

Field communities involve competition, cross-feeding, and syntrophy, while lab fitness measures single-organism performance in isolation. [src: lab_field_ecology]

16S amplicon data resolves to genus, but FB organisms are specific strains, and a genus like Pseudomonas contains thousands of species with vastly different ecologies. [src: lab_field_ecology]

Geochemistry measurements are snapshots, but community composition reflects historical conditions and colonization history. [src: lab_field_ecology]

### Links to prior literature

Carlson et al. (2019) showed that low pH with elevated uranium and metals selectively inhibits non-Rhodanobacter taxa at Oak Ridge; the report finds its Caulobacter and Sphingomonas depletion consistent with this. [src: lab_field_ecology]

Peng et al. (2022) found that Rhodanobacter strains at Oak Ridge acquired heavy metal resistance via horizontal gene transfer. [src: lab_field_ecology]

The report says this parallels its costly_dispensable_genes finding that metal resistance genes are enriched in the accessory genome. [src: lab_field_ecology]

Michael et al. (2024) demonstrated reproducible microbial succession at Oak Ridge following carbon amendments, and the report says its uranium-abundance correlations support this deterministic relationship. [src: lab_field_ecology]

LaSarre et al. (2020) showed that microbial interactions in coculture are "not necessarily predictable a priori" from single-organism fitness data, which the report says parallels its finding that lab metal tolerance does not predict field abundance. [src: lab_field_ecology]

Price et al. (2018) generated the Fitness Browser data used here. [src: lab_field_ecology]

The report states that it provides the first test of whether FB lab fitness measurements predict field ecology at the sites where many FB organisms were originally isolated. [src: lab_field_ecology]

It also states this is the first study to directly link FB lab fitness data with ENIGMA CORAL field community composition across a geochemical gradient. [src: lab_field_ecology]

It says the ENIGMA CORAL database, previously undocumented, contains rich community composition and geochemistry data suitable for ecological analysis. [src: lab_field_ecology]

## Data and Methods

Geochemistry came from `enigma_coral.ddt_brick0000010` (metal concentrations per sample, 108 sites) via Spark. [src: lab_field_ecology]

Community data came from `enigma_coral.ddt_brick0000459` (ASV counts per community, 868K rows; ASV = amplicon sequence variant). [src: lab_field_ecology]

Taxonomy came from `enigma_coral.ddt_brick0000454` (ASV-to-genus mapping, 627K rows). [src: lab_field_ecology]

FB per-gene fitness covered 43 organisms. [src: lab_field_ecology]

## Caveats and Open Work

16S amplicon data resolves to genus level only, so species/strain-level matching to FB organisms is not possible. [src: lab_field_ecology]

The 108 overlapping samples may not capture the full range of Oak Ridge geochemistry. [src: lab_field_ecology]

The metal tolerance score is a crude aggregate; condition-specific fitness scores (e.g., uranium-only) would be more informative. [src: lab_field_ecology]

Community data include multiple communities per sample (different filter sizes, replicates), which were aggregated. [src: lab_field_ecology]

Only 12 FB genera have enough data for the metal tolerance correlation, limiting statistical power. [src: lab_field_ecology]

Confounding variables (pH, dissolved oxygen, carbon sources) are not controlled for. [src: lab_field_ecology]

### Next analyses proposed by the report

- Species-level resolution: use metagenomic data, if available in ENIGMA CORAL genome/assembly tables, instead of 16S amplicons to match FB organisms at species or strain level. [src: lab_field_ecology]
- Multivariate analysis: use CCA (canonical correlation analysis) or RDA to model community composition from multiple geochemical variables at once, controlling for pH, redox, and carbon sources. [src: lab_field_ecology]
- Condition-specific fitness: compute per-metal fitness scores (e.g., uranium-specific, chromium-specific) instead of an aggregate stress tolerance, and correlate them with the corresponding metal concentrations at each site. [src: lab_field_ecology]
- Temporal analysis: the ENIGMA samples span multiple dates, so test whether community changes over time track geochemical changes. [src: lab_field_ecology]
- Rhodanobacter: add it to the Fitness Browser, since it dominates contaminated wells but is absent from the FB. [src: lab_field_ecology]

## Slots Into

- [[concepts/laboratory-fitness-as-a-predictor-of-field-abundance]]: the aggregate tolerance score was not significantly correlated with the high-uranium/low-uranium abundance ratio (rho=0.503, p=0.095, n=12 genera). [src: lab_field_ecology]
- [[concepts/geochemical-and-contamination-plume-control-of-subsurface-community-structure]]: 5 of 11 tested genera correlate with uranium, and sites split at median uranium show distinct communities. [src: lab_field_ecology]
- [[concepts/genus-level-amplicon-resolution-and-rare-taxon-limits-in-matching-reference-organisms-to-field-data]]: genus-only resolution prevents strain-level matching to FB organisms [src: lab_field_ecology], and Desulfovibrio's rarity (max 0.09% relative abundance) makes correlation analysis unreliable. [src: lab_field_ecology] The report proposes metagenomic data as a route to species-level matching. [src: lab_field_ecology]
- [[concepts/accessory-conservation-of-metal-and-antibiotic-resistance-genes]]: the report says metal resistance genes are enriched in the accessory genome. [src: lab_field_ecology]
- [[concepts/horizontal-transfer-signatures-of-metal-resistance-genes]]: Peng et al. (2022) found horizontal transfer of heavy metal resistance in Oak Ridge Rhodanobacter. [src: lab_field_ecology]
