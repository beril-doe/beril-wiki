---
type: "Finding"
description: "Leucine biosynthesis community completeness versus ambient metabolite intensity in NMDC had Spearman r = \u22120.390, p = 0.002, q (BH) = 0.022, n = 62, significant after FDR correction."
finding_id: "nmdc_community_metabolic_ecology--33da3819"
result: "observation"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "\u22120.390", "what": "Spearman r", "unit": "", "denominator": "", "scope": ""}, {"value": "0.022", "what": "BH q-value", "unit": "", "denominator": "", "scope": ""}, {"value": "62", "what": "samples", "unit": "", "denominator": "", "scope": ""}]
caveat: "The current H1 dataset is effectively single-study, so generalisation of the leucine and arginine signals is untested."
first_added: "2026-11-24"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Leucine completeness negatively tracks ambient leucine after FDR correction

Leucine biosynthesis community completeness versus ambient metabolite intensity in NMDC had Spearman r = −0.390, p = 0.002, q (BH) = 0.022, n = 62, significant after FDR correction. [src: nmdc_community_metabolic_ecology]

## Key figures

- **−0.390**: Spearman r [src: nmdc_community_metabolic_ecology]
- **0.022**: BH q-value [src: nmdc_community_metabolic_ecology]
- **62**: samples [src: nmdc_community_metabolic_ecology]

## Evidence

> | leu | 62 | −0.390 | 0.002 | 0.022 | **Yes** | [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

The current H1 dataset is effectively single-study, so generalisation of the leucine and arginine signals is untested. [src: nmdc_community_metabolic_ecology]

> The current H1 dataset is effectively single-study; replicating this analysis across additional NMDC studies with paired taxonomy + metabolomics would test whether the leu/arg signals generalise beyond the current cohort. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- Methionine biosynthesis had the largest reported correlation effect (r = −0.496), but sample size limited significance (n = 18, q = 0.117). [src: nmdc_community_metabolic_ecology]
- All 33 Freshwater samples lacked paired NMDC metabolomics and were excluded from H1 testing but retained for H2 PCA using pathway completeness alone. [src: nmdc_community_metabolic_ecology]
- Glutamine was skipped in the NMDC H1 pathway correlation analysis with n = 4. [src: nmdc_community_metabolic_ecology]
- Proline was skipped in the NMDC H1 pathway correlation analysis with n = 9. [src: nmdc_community_metabolic_ecology]
- In the NMDC H1 dataset, 95% of samples (125/131) originated from study nmdc:sty-11-r2h77870, with the remaining 6 from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology]
