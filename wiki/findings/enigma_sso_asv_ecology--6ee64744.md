---
type: "Finding"
description: "In groundwater, median Bray-Curtis dissimilarity was 0.351 by date, 0.750 by filter and 0.917 spatially, and the date-1 and date-2 distance matrices correlate at Mantel rho = 0.867 (p = 0.001), indicating spatial patterns are temporally stable at the 9-day scale."
finding_id: "enigma_sso_asv_ecology--6ee64744"
result: "observation"
source: "enigma_sso_asv_ecology"
quantities: [{"value": "0.867", "what": "Mantel correlation between date-1 and date-2 distance matrices", "unit": "rho", "denominator": "", "scope": "9-day scale"}, {"value": "0.351", "what": "median Bray-Curtis by date", "unit": "", "denominator": "", "scope": ""}, {"value": "0.917", "what": "median Bray-Curtis spatial", "unit": "", "denominator": "", "scope": ""}]
caveat: "Groundwater ASV data cover only 5 of 9 wells (L7, L9, M4, M6, U2), missing M5 and U3."
first_added: "2026-10-27"
source_hash: "1153f1f3f4d12bf8f52c79351cc2441f7f7114eaae9b86f58aae67797d6cb55a"
---
# Groundwater spatial patterns are stable over nine days

In groundwater, median Bray-Curtis dissimilarity was 0.351 by date, 0.750 by filter and 0.917 spatially, and the date-1 and date-2 distance matrices correlate at Mantel rho = 0.867 (p = 0.001), indicating spatial patterns are temporally stable at the 9-day scale. [src: enigma_sso_asv_ecology]

## Key figures

- **0.867 rho**: Mantel correlation between date-1 and date-2 distance matrices (scope 9-day scale) [src: enigma_sso_asv_ecology]
- **0.351**: median Bray-Curtis by date [src: enigma_sso_asv_ecology]
- **0.917**: median Bray-Curtis spatial [src: enigma_sso_asv_ecology]

## Evidence

> The variation hierarchy — temporal (median BC = 0.351) < filter (0.750) < spatial (0.917) — confirms that spatial patterns are temporally stable at the 9-day scale. The Mantel correlation between date-1 and date-2 distance matrices is ρ = 0.867 (p = 0.001): which wells are most similar to each other is nearly identical across the two sampling dates. [src: enigma_sso_asv_ecology]

From the report [[summaries/enigma_sso_asv_ecology__REPORT]].

## Caveat

Groundwater ASV data cover only 5 of 9 wells (L7, L9, M4, M6, U2), missing M5 and U3. [src: enigma_sso_asv_ecology]

> - **Groundwater coverage**: Only 5 of 9 wells have groundwater ASV data (L7, L9, M4, M6, U2), missing the critical wells M5 (denitrification hotspot) and U3 (plume entry). [src: enigma_sso_asv_ecology]

## Other caveats in this report

- NMDS stress is 0.067, but Procrustes correspondence with the physical grid is marginal (m² = 0.379, p = 0.080). [src: enigma_sso_asv_ecology]
- Biogeochemical processes are inferred from taxonomy rather than directly measured; class-level annotation covers 22 classes and 78%, while genus-level annotation covers 65 genera and 21%. [src: enigma_sso_asv_ecology]
- Guild analysis assigns 65 annotated genera to 11 guilds and tests co-occurrence across nine wells; these correlations do not demonstrate interactions. [src: enigma_sso_asv_ecology]
- Sediment cores were sampled once per well in Feb–Mar 2023 with no within-well temporal replication; the 18-month offset to groundwater sampling in 2024 confounds material and time. [src: enigma_sso_asv_ecology]
- A northeast-to-southwest saturated-zone plume is the report's explanatory model, not an independently verified flow-path measurement. [src: enigma_sso_asv_ecology]
