---
type: "Finding"
description: "Effect sizes (Spearman \u03c1) have not yet been systematically reported across all 2,355 associations; many may be statistically significant but biologically small."
finding_id: "soil_metal_functional_genomics--e27860e8"
result: "null result"
source: "soil_metal_functional_genomics"
quantities: [{"value": "2,355", "what": "association set requiring systematic effect-size assessment", "unit": "associations", "denominator": "", "scope": "significant COG-metal associations"}]
caveat: "The effect size audit of the \u03c1 distribution across 2,355 associations, flagging \u03c1 < 0.05, remains pending."
first_added: "2026-10-27"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Effect sizes not yet systematically reported for significant associations

Effect sizes (Spearman ρ) have not yet been systematically reported across all 2,355 associations; many may be statistically significant but biologically small. [src: soil_metal_functional_genomics]

## Key figures

- **2,355 associations**: association set requiring systematic effect-size assessment (scope significant COG-metal associations) [src: soil_metal_functional_genomics]

## Evidence

> Effect sizes (Spearman ρ) have not yet been systematically reported across all 2,355 associations; many may be statistically significant but biologically small. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

The effect size audit of the ρ distribution across 2,355 associations, flagging ρ < 0.05, remains pending. [src: soil_metal_functional_genomics]

> 1. Effect size audit: ρ distribution across 2,355 associations; flag ρ < 0.05 [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA and PGLS analyses were complete, while effect-size and spatial validation remained pending. [src: soil_metal_functional_genomics]
- All reported associations are observational. Covariation of Cr, Cu, Pb and Zn in industrial soils confounds metal-specific interpretation; whether the COG associations represent metal-specific or general multi-metal stress responses remains unresolved. [src: soil_metal_functional_genomics]
- Because db-RDA conditioned on project accession, R² = 0.799 concerns residual rather than necessarily total COG variance. The unconditional metals-only R² was not reported and could be substantially lower; the report calls for both values alongside the conditional figure. [src: soil_metal_functional_genomics]
- The report flags a high 60% discovery rate from 2,355 significant associations among 3,915 tests (9 metals × 435 COGs) in 51,748 samples. It argues that metal co-contamination and dependent tests may make its reported Benjamini–Hochberg FDR anti-conservative, and calls for a partial-correlation model. This is the report's methodological assessment, not a validated recalculation of FDR. [src: soil_metal_functional_genomics]
- A 10 km sample-to-genome matching threshold may not establish site co-location; the report requires sensitivity analyses at 5 km and 20 km before attributing COG–copper associations to measured sites. [src: soil_metal_functional_genomics]
