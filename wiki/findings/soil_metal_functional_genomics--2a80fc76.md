---
type: "Finding"
description: "In the copper-specific analysis (116 COGs, FDR < 0.05; 7,566 samples with nearby KBase genomes at 10 km), top positives include cell division and nucleotide transport (BQ, FQ, FK, CF) and top negatives include energy production (DI, CE), suggesting energetic trade-offs under copper stress."
finding_id: "soil_metal_functional_genomics--2a80fc76"
result: "inference"
source: "soil_metal_functional_genomics"
quantities: [{"value": "116", "what": "copper-associated COGs", "unit": "COGs", "denominator": "", "scope": "FDR < 0.05"}, {"value": "7,566", "what": "samples with nearby KBase genomes", "unit": "samples", "denominator": "", "scope": "within 10 km"}]
caveat: "At the 10 km proximity criterion many nearby genomes may not be co-located with the copper measurements, so sensitivity analysis at 5 km and 20 km is needed before attributing COG-copper associations to the measured sites."
first_added: "2026-10-27"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Copper-associated COGs suggest an energetic trade-off under copper stress

In the copper-specific analysis (116 COGs, FDR < 0.05; 7,566 samples with nearby KBase genomes at 10 km), top positives include cell division and nucleotide transport (BQ, FQ, FK, CF) and top negatives include energy production (DI, CE), suggesting energetic trade-offs under copper stress. [src: soil_metal_functional_genomics]

## Key figures

- **116 COGs**: copper-associated COGs (scope FDR < 0.05) [src: soil_metal_functional_genomics]
- **7,566 samples**: samples with nearby KBase genomes (scope within 10 km) [src: soil_metal_functional_genomics]

## Evidence

> - **Copper-specific analysis** (116 COGs, FDR < 0.05; 7,566 samples with nearby KBase genomes at 10 km): top positives include cell division and nucleotide transport (BQ, FQ, FK, CF); top negatives include energy production (DI, CE), suggesting energetic trade-offs under copper stress. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

At the 10 km proximity criterion many nearby genomes may not be co-located with the copper measurements, so sensitivity analysis at 5 km and 20 km is needed before attributing COG-copper associations to the measured sites. [src: soil_metal_functional_genomics]

> **Copper-specific analysis uses a 10 km proximity criterion** to match soil samples to KBase genomes. At 10 km, many "nearby" genomes may not be co-located with the copper measurements. Sensitivity analysis at 5 km and 20 km thresholds is needed before COG-copper associations can be attributed to the measured sites. [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA and PGLS analyses were complete, while effect-size and spatial validation remained pending. [src: soil_metal_functional_genomics]
- All reported associations are observational. Covariation of Cr, Cu, Pb and Zn in industrial soils confounds metal-specific interpretation; whether the COG associations represent metal-specific or general multi-metal stress responses remains unresolved. [src: soil_metal_functional_genomics]
- Because db-RDA conditioned on project accession, R² = 0.799 concerns residual rather than necessarily total COG variance. The unconditional metals-only R² was not reported and could be substantially lower; the report calls for both values alongside the conditional figure. [src: soil_metal_functional_genomics]
- The report flags a high 60% discovery rate from 2,355 significant associations among 3,915 tests (9 metals × 435 COGs) in 51,748 samples. It argues that metal co-contamination and dependent tests may make its reported Benjamini–Hochberg FDR anti-conservative, and calls for a partial-correlation model. This is the report's methodological assessment, not a validated recalculation of FDR. [src: soil_metal_functional_genomics]
- A pending effect-size audit would examine the ρ distribution across 2,355 associations and flag ρ < 0.05. [src: soil_metal_functional_genomics]
