---
type: "Finding"
description: "Across 13 testable amino acid biosynthesis pathways, 11 of 13 (85%) showed negative Spearman correlations between community pathway completeness and ambient amino acid metabolite intensity, the direction predicted by the Black Queen Hypothesis; leucine (r = \u22120.390, q = 0.022, n = 62) and arginine (r = \u22120.297, q = 0.049, n = 80) passed BH-FDR correction, and a binomial sign test gave p = 0.011, indicating a weak but consistent community-scale signal."
finding_id: "nmdc_community_metabolic_ecology--dcef6254"
result: "observation"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "11 of 13 (85%)", "what": "pathways with negative Spearman correlation between community pathway completeness and ambient amino acid metabolite intensity", "unit": "pathways", "denominator": "13 testable amino acid biosynthesis pathways", "scope": "NMDC samples with GapMind completeness and metabolomics"}, {"value": "r = \u22120.390, q = 0.022, n = 62", "what": "leucine biosynthesis correlation after BH-FDR", "unit": "", "denominator": "", "scope": ""}, {"value": "r = \u22120.297, q = 0.049, n = 80", "what": "arginine biosynthesis correlation after BH-FDR", "unit": "", "denominator": "", "scope": ""}, {"value": "p = 0.011", "what": "binomial sign test of the majority-negative direction", "unit": "", "denominator": "", "scope": ""}]
caveat: "95% of H1 samples (125/131) came from a single NMDC study (nmdc:sty-11-r2h77870), and all leucine samples (n = 62) came from that study, so generalization beyond it is untested."
first_added: "2026-10-27"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Most amino-acid pathways show negative completeness–metabolite correlations, as Black Queen predicts

Across 13 testable amino acid biosynthesis pathways, 11 of 13 (85%) showed negative Spearman correlations between community pathway completeness and ambient amino acid metabolite intensity, the direction predicted by the Black Queen Hypothesis; leucine (r = −0.390, q = 0.022, n = 62) and arginine (r = −0.297, q = 0.049, n = 80) passed BH-FDR correction, and a binomial sign test gave p = 0.011, indicating a weak but consistent community-scale signal. [src: nmdc_community_metabolic_ecology]

## Key figures

- **11 of 13 (85%) pathways**: pathways with negative Spearman correlation between community pathway completeness and ambient amino acid metabolite intensity (denominator 13 testable amino acid biosynthesis pathways; scope NMDC samples with GapMind completeness and metabolomics) [src: nmdc_community_metabolic_ecology]
- **r = −0.390, q = 0.022, n = 62**: leucine biosynthesis correlation after BH-FDR [src: nmdc_community_metabolic_ecology]
- **r = −0.297, q = 0.049, n = 80**: arginine biosynthesis correlation after BH-FDR [src: nmdc_community_metabolic_ecology]
- **p = 0.011**: binomial sign test of the majority-negative direction [src: nmdc_community_metabolic_ecology]

## Evidence

> Across 13 testable amino acid biosynthesis pathways, **11 of 13 (85%) showed negative Spearman correlations** between community pathway completeness and ambient amino acid metabolite intensity — the direction predicted by the Black Queen Hypothesis (BQH). Two pathways reached significance after Benjamini-Hochberg FDR correction (q < 0.05): **leucine biosynthesis** (r = −0.390, q = 0.022, n = 62) and **arginine biosynthesis** (r = −0.297, q = 0.049, n = 80). Methionine biosynthesis showed the largest effect (r = −0.496) but was limited by sample size (n = 18, q = 0.117). A binomial sign test confirmed that the majority-negative direction is significantly non-random (p = 0.011), indicating a weak but consistent community-scale BQH signal. [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

95% of H1 samples (125/131) came from a single NMDC study (nmdc:sty-11-r2h77870), and all leucine samples (n = 62) came from that study, so generalization beyond it is untested. [src: nmdc_community_metabolic_ecology]

> Study-level analysis of the H1 dataset reveals that **95% of samples (125/131) originate from a single NMDC study (nmdc:sty-11-r2h77870)**; the remaining 6 samples are from a second study (nmdc:sty-11-547rwq94). This means cross-study LC-MS protocol heterogeneity is effectively absent as a confounder for leu: all leu samples (n = 62) are from one study with consistent analytical methods. For arg, excluding the 6-sample second study gives r = −0.264, p = 0.019 (n = 78), confirming the arginine signal is not driven by the minor study. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- The 220-sample cohort comprised 126 soil, 33 freshwater, and 61 ecosystem-unrecorded samples. All 33 freshwater samples lacked paired metabolomics, excluding them from H1 but not H2. [src: nmdc_community_metabolic_ecology]
- The listed positive, soil-directed PC1 loadings are glucuronate, fumarate, succinate, lysine, and cellobiose. The source calls all five carbon-utilization pathways, although lysine is also identified elsewhere in the report as an amino-acid pathway. [src: nmdc_community_metabolic_ecology]
- The report interprets the leucine and arginine associations in light of stated synthesis costs of 37 and 26 ATP equivalents, respectively. This is a mechanistic interpretation, not direct evidence of gene loss; the predicted benefit of more methionine data remains untested. [src: nmdc_community_metabolic_ecology]
- Correcting three misassigned isoleucine compounds changed the leucine result from r −0.326 to −0.390 and q 0.045 to 0.022. [src: nmdc_community_metabolic_ecology]
- Phenylalanine hydroxylation is proposed as a possible reason tyrosine availability may not track the measured tyrosine-biosynthesis completeness score. [src: nmdc_community_metabolic_ecology]
