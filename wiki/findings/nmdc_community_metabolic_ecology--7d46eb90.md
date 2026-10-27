---
type: "Finding"
description: "In a soil-only re-run on 125 Soil-ecosystem samples, leucine remained FDR-significant (r = \u22120.390, q = 0.022, n = 62, identical because all leucine samples are Soil), while arginine lost FDR significance (r = \u22120.264, q = 0.117, n = 78) but remained directionally consistent, and the 11/13-negative sign test was unchanged (p = 0.011)."
finding_id: "nmdc_community_metabolic_ecology--7d46eb90"
result: "observation"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "r = \u22120.390, q = 0.022, n = 62", "what": "leucine correlation in soil-only analysis", "unit": "", "denominator": "", "scope": "Soil samples"}, {"value": "r = \u22120.264, q = 0.117, n = 78", "what": "arginine correlation in soil-only analysis", "unit": "", "denominator": "", "scope": "Soil samples"}, {"value": "p = 0.011", "what": "binomial sign test for 11/13 negative correlations", "unit": "", "denominator": "", "scope": "soil-only re-run"}]
caveat: "Abiotic features (pH, temperature, total organic carbon, etc.) were all NaN for the 174-sample analysis matrix, preventing partial correlation tests and leaving possible environmental confounding of H1 and H2."
first_added: "2026-10-27"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Leucine signal survives soil-only stratification; arginine loses FDR significance

In a soil-only re-run on 125 Soil-ecosystem samples, leucine remained FDR-significant (r = −0.390, q = 0.022, n = 62, identical because all leucine samples are Soil), while arginine lost FDR significance (r = −0.264, q = 0.117, n = 78) but remained directionally consistent, and the 11/13-negative sign test was unchanged (p = 0.011). [src: nmdc_community_metabolic_ecology]

## Key figures

- **r = −0.390, q = 0.022, n = 62**: leucine correlation in soil-only analysis (scope Soil samples) [src: nmdc_community_metabolic_ecology]
- **r = −0.264, q = 0.117, n = 78**: arginine correlation in soil-only analysis (scope Soil samples) [src: nmdc_community_metabolic_ecology]
- **p = 0.011**: binomial sign test for 11/13 negative correlations (scope soil-only re-run) [src: nmdc_community_metabolic_ecology]

## Evidence

> To control for the strong ecosystem-type effect (Finding 2), H1 was re-run on the 125 Soil-ecosystem samples only (excluding the 6 Unknown-ecosystem samples in the H1 dataset). Results: **leu remains FDR-significant** (r = −0.390, q = 0.022, n = 62 — identical to the full-cohort result, since the leu samples are all Soil); arg loses FDR significance (r = −0.264, q = 0.117, n = 78) but remains directionally consistent. The binomial sign test (11/13 negative, p = 0.011) is unchanged, confirming the majority-negative direction is robust to ecosystem stratification. [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

Abiotic features (pH, temperature, total organic carbon, etc.) were all NaN for the 174-sample analysis matrix, preventing partial correlation tests and leaving possible environmental confounding of H1 and H2. [src: nmdc_community_metabolic_ecology]

> - **Abiotic feature coverage**: Abiotic features (pH, temperature, total organic carbon, etc.) were absent (all NaN) for the 174-sample analysis matrix, preventing partial correlation tests controlling for environmental gradients. These variables could confound both H1 and H2 results. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- The 220-sample cohort comprised 126 soil, 33 freshwater, and 61 ecosystem-unrecorded samples. All 33 freshwater samples lacked paired metabolomics, excluding them from H1 but not H2. [src: nmdc_community_metabolic_ecology]
- H1 was overwhelmingly single-study: 125/131 samples (95%) came from nmdc:sty-11-r2h77870. All leucine samples came from that study, and the arginine association persisted after excluding the six samples from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology]
- The listed positive, soil-directed PC1 loadings are glucuronate, fumarate, succinate, lysine, and cellobiose. The source calls all five carbon-utilization pathways, although lysine is also identified elsewhere in the report as an amino-acid pathway. [src: nmdc_community_metabolic_ecology]
- The report interprets the leucine and arginine associations in light of stated synthesis costs of 37 and 26 ATP equivalents, respectively. This is a mechanistic interpretation, not direct evidence of gene loss; the predicted benefit of more methionine data remains untested. [src: nmdc_community_metabolic_ecology]
- Correcting three misassigned isoleucine compounds changed the leucine result from r −0.326 to −0.390 and q 0.045 to 0.022. [src: nmdc_community_metabolic_ecology]
