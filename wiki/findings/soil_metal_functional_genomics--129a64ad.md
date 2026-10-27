---
type: "Finding"
description: "The analysis reports 2,355 significant COG-metal associations (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples, with chromium and lead driving the strongest signals and transporters (ABC, RND) and biosynthesis genes dominating top hits."
finding_id: "soil_metal_functional_genomics--129a64ad"
result: "observation"
source: "soil_metal_functional_genomics"
quantities: [{"value": "2,355", "what": "significant COG-metal associations", "unit": "associations", "denominator": "", "scope": "FDR < 0.05, 9 metals"}, {"value": "51,748", "what": "soil samples analysed", "unit": "samples", "denominator": "", "scope": ""}, {"value": "9", "what": "metals tested", "unit": "metals", "denominator": "", "scope": "Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg"}]
caveat: "The report assesses that a 60% discovery rate (2,355 significant of 3,915 tests, 9 metals \u00d7 435 COGs) is high and argues that metal co-contamination and non-independent tests may make its Benjamini-Hochberg FDR anti-conservative; this is the report's methodological assessment, not a validated FDR recalculation."
first_added: "2026-10-27"
source_hash: "afe5423a06222e7ee2957401c00f4af52fea13df31be748b4ab108fb1dfe6144"
---
# Many COG–metal associations in soils, strongest for chromium and lead

The analysis reports 2,355 significant COG-metal associations (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples, with chromium and lead driving the strongest signals and transporters (ABC, RND) and biosynthesis genes dominating top hits. [src: soil_metal_functional_genomics]

## Key figures

- **2,355 associations**: significant COG-metal associations (scope FDR < 0.05, 9 metals) [src: soil_metal_functional_genomics]
- **51,748 samples**: soil samples analysed [src: soil_metal_functional_genomics]
- **9 metals**: metals tested (scope Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) [src: soil_metal_functional_genomics]

## Evidence

> - **2,355 significant COG-metal associations** (FDR < 0.05) across 9 metals (Cu, Co, Cr, Ni, Zn, Pb, As, Cd, Hg) in 51,748 soil samples. Chromium and Lead drive the strongest signals; transporters (ABC, RND) and biosynthesis genes dominate top hits. [src: soil_metal_functional_genomics]

From the report [[summaries/soil_metal_functional_genomics__REPORT]].

## Caveat

The report assesses that a 60% discovery rate (2,355 significant of 3,915 tests, 9 metals × 435 COGs) is high and argues that metal co-contamination and non-independent tests may make its Benjamini-Hochberg FDR anti-conservative; this is the report's methodological assessment, not a validated FDR recalculation. [src: soil_metal_functional_genomics]

> **2,355 significant associations at FDR < 0.05 in 51,748 samples:** With 9 metals × 435 COGs = 3,915 tests, a 60% discovery rate is high. Metals co-contaminate (Cr, Pb, Zn, Cu co-vary in industrial soils), so tests are not independent — Benjamini-Hochberg FDR correction assumes independent tests and will be anti-conservative under positive correlation. True FDR is likely higher than reported. The partial correlation model (NB05 item 3) is the correct remedy. [src: soil_metal_functional_genomics]

## Other caveats in this report

- The report is preliminary: Spearman correlation, db-RDA and PGLS analyses were complete, while effect-size and spatial validation remained pending. [src: soil_metal_functional_genomics]
- All reported associations are observational. Covariation of Cr, Cu, Pb and Zn in industrial soils confounds metal-specific interpretation; whether the COG associations represent metal-specific or general multi-metal stress responses remains unresolved. [src: soil_metal_functional_genomics]
- Because db-RDA conditioned on project accession, R² = 0.799 concerns residual rather than necessarily total COG variance. The unconditional metals-only R² was not reported and could be substantially lower; the report calls for both values alongside the conditional figure. [src: soil_metal_functional_genomics]
- A 10 km sample-to-genome matching threshold may not establish site co-location; the report requires sensitivity analyses at 5 km and 20 km before attributing COG–copper associations to measured sites. [src: soil_metal_functional_genomics]
- A pending effect-size audit would examine the ρ distribution across 2,355 associations and flag ρ < 0.05. [src: soil_metal_functional_genomics]
