---
type: "Finding"
description: "Arginine biosynthesis community completeness versus ambient metabolite intensity in NMDC had Spearman r = \u22120.297, p = 0.007, q (BH) = 0.049, n = 80, significant after FDR correction."
finding_id: "nmdc_community_metabolic_ecology--821653f8"
result: "observation"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "\u22120.297", "what": "Spearman r", "unit": "", "denominator": "", "scope": ""}, {"value": "0.049", "what": "BH q-value", "unit": "", "denominator": "", "scope": ""}, {"value": "80", "what": "samples", "unit": "", "denominator": "", "scope": ""}]
caveat: "95% of H1 samples (125/131) originate from nmdc:sty-11-r2h77870, so the signal is effectively from a single study."
first_added: "2026-11-24"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Arginine completeness negatively tracks ambient arginine after FDR correction

Arginine biosynthesis community completeness versus ambient metabolite intensity in NMDC had Spearman r = −0.297, p = 0.007, q (BH) = 0.049, n = 80, significant after FDR correction. [src: nmdc_community_metabolic_ecology]

## Key figures

- **−0.297**: Spearman r [src: nmdc_community_metabolic_ecology]
- **0.049**: BH q-value [src: nmdc_community_metabolic_ecology]
- **80**: samples [src: nmdc_community_metabolic_ecology]

## Evidence

> | arg | 80 | −0.297 | 0.007 | 0.049 | **Yes** | [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

95% of H1 samples (125/131) originate from nmdc:sty-11-r2h77870, so the signal is effectively from a single study. [src: nmdc_community_metabolic_ecology]

> The 175 metabolomics samples derive from multiple NMDC studies. However, study-level analysis of the H1 subset reveals that 95% of H1 samples (125/131) originate from a single NMDC study (nmdc:sty-11-r2h77870), so cross-study LC-MS protocol heterogeneity is largely absent as a confounder for leu and arg. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- Methionine biosynthesis had the largest reported correlation effect (r = −0.496), but sample size limited significance (n = 18, q = 0.117). [src: nmdc_community_metabolic_ecology]
- All 33 Freshwater samples lacked paired NMDC metabolomics and were excluded from H1 testing but retained for H2 PCA using pathway completeness alone. [src: nmdc_community_metabolic_ecology]
- Glutamine was skipped in the NMDC H1 pathway correlation analysis with n = 4. [src: nmdc_community_metabolic_ecology]
- Proline was skipped in the NMDC H1 pathway correlation analysis with n = 9. [src: nmdc_community_metabolic_ecology]
- In the NMDC H1 dataset, 95% of samples (125/131) originated from study nmdc:sty-11-r2h77870, with the remaining 6 from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology]
