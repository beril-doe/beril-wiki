---
type: "Finding"
description: "Per-pathway Kruskal-Wallis tests (BH-FDR corrected) showed 17 of 18 amino acid pathways have significantly different community completeness across ecosystem types (q < 0.05), most extremely glycine (H = 92.98, q = 1.2\u00d710\u207b\u00b9\u2079), asparagine (H = 66.19, q = 3.8\u00d710\u207b\u00b9\u2074) and cysteine (H = 62.66, q = 1.5\u00d710\u207b\u00b9\u00b3); only tyrosine was not significant (q = 0.71)."
finding_id: "nmdc_community_metabolic_ecology--4a766ba0"
result: "observation"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "17 of 18", "what": "amino acid pathways with significantly different completeness across ecosystem types", "unit": "pathways", "denominator": "18 amino acid pathways", "scope": "q < 0.05, BH-FDR"}, {"value": "H = 92.98, q = 1.2\u00d710\u207b\u00b9\u2079", "what": "glycine biosynthesis Kruskal-Wallis result", "unit": "", "denominator": "", "scope": ""}, {"value": "q = 0.71", "what": "tyrosine, the non-significant pathway", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 220-sample cohort comprised 126 Soil, 33 Freshwater and 61 samples with unrecorded ecosystem type, so the three-group contrasts rest on an unequal cohort with a large unresolved category."
first_added: "2026-10-27"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Nearly all amino-acid pathways differ in community completeness across ecosystem types

Per-pathway Kruskal-Wallis tests (BH-FDR corrected) showed 17 of 18 amino acid pathways have significantly different community completeness across ecosystem types (q < 0.05), most extremely glycine (H = 92.98, q = 1.2×10⁻¹⁹), asparagine (H = 66.19, q = 3.8×10⁻¹⁴) and cysteine (H = 62.66, q = 1.5×10⁻¹³); only tyrosine was not significant (q = 0.71). [src: nmdc_community_metabolic_ecology]

## Key figures

- **17 of 18 pathways**: amino acid pathways with significantly different completeness across ecosystem types (denominator 18 amino acid pathways; scope q < 0.05, BH-FDR) [src: nmdc_community_metabolic_ecology]
- **H = 92.98, q = 1.2×10⁻¹⁹**: glycine biosynthesis Kruskal-Wallis result [src: nmdc_community_metabolic_ecology]
- **q = 0.71**: tyrosine, the non-significant pathway [src: nmdc_community_metabolic_ecology]

## Evidence

> Per-pathway Kruskal-Wallis tests (BH-FDR corrected) showed that 17 of 18 amino acid pathways have significantly different community completeness levels across ecosystem types (q < 0.05). The most extreme differences were in glycine (H = 92.98, q = 1.2×10⁻¹⁹), asparagine (H = 66.19, q = 3.8×10⁻¹⁴), and cysteine (H = 62.66, q = 1.5×10⁻¹³) biosynthesis. Only tyrosine was not significantly differentiated (q = 0.71). [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

The 220-sample cohort comprised 126 Soil, 33 Freshwater and 61 samples with unrecorded ecosystem type, so the three-group contrasts rest on an unequal cohort with a large unresolved category. [src: nmdc_community_metabolic_ecology]

> Ecosystem distribution in the full 220-sample cohort: 126 Soil, 33 Freshwater, 61 with unrecorded ecosystem type. All 33 Freshwater samples lacked paired metabolomics data in NMDC and were therefore excluded from H1 testing; they were retained for H2 (PCA) using pathway completeness alone. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- H1 was overwhelmingly single-study: 125/131 samples (95%) came from nmdc:sty-11-r2h77870. All leucine samples came from that study, and the arginine association persisted after excluding the six samples from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology]
- The listed positive, soil-directed PC1 loadings are glucuronate, fumarate, succinate, lysine, and cellobiose. The source calls all five carbon-utilization pathways, although lysine is also identified elsewhere in the report as an amino-acid pathway. [src: nmdc_community_metabolic_ecology]
- The report interprets the leucine and arginine associations in light of stated synthesis costs of 37 and 26 ATP equivalents, respectively. This is a mechanistic interpretation, not direct evidence of gene loss; the predicted benefit of more methionine data remains untested. [src: nmdc_community_metabolic_ecology]
- Correcting three misassigned isoleucine compounds changed the leucine result from r −0.326 to −0.390 and q 0.045 to 0.022. [src: nmdc_community_metabolic_ecology]
- Phenylalanine hydroxylation is proposed as a possible reason tyrosine availability may not track the measured tyrosine-biosynthesis completeness score. [src: nmdc_community_metabolic_ecology]
