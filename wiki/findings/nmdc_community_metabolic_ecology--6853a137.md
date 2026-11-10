---
type: "Finding"
description: "Tyrosine correlated in the opposite, nonsignificant direction (r = +0.419, ns), and isoleucine biosynthesis (r = \u22120.057, n = 18, q = 0.823) showed no BQH signal at this sample size."
finding_id: "nmdc_community_metabolic_ecology--6853a137"
result: "null result"
source: "nmdc_community_metabolic_ecology"
quantities: [{"value": "r = +0.419", "what": "tyrosine Spearman correlation, anti-BQH direction, nonsignificant", "unit": "", "denominator": "", "scope": ""}, {"value": "r = \u22120.057, n = 18, q = 0.823", "what": "isoleucine biosynthesis correlation", "unit": "", "denominator": "", "scope": ""}]
caveat: "Tyrosine can be produced from phenylalanine via non-biosynthetic hydroxylation, which the tyr completeness score does not capture, so the opposite sign may reflect decoupling of biosynthesis and pool."
first_added: "2026-10-27"
source_hash: "1959fd37259df598f708ecfea2c796883e3a8f2f62ea52e1443073544a8866d5"
---
# Tyrosine and isoleucine show no Black Queen signal

Tyrosine correlated in the opposite, nonsignificant direction (r = +0.419, ns), and isoleucine biosynthesis (r = −0.057, n = 18, q = 0.823) showed no BQH signal at this sample size. [src: nmdc_community_metabolic_ecology]

## Key figures

- **r = +0.419**: tyrosine Spearman correlation, anti-BQH direction, nonsignificant [src: nmdc_community_metabolic_ecology]
- **r = −0.057, n = 18, q = 0.823**: isoleucine biosynthesis correlation [src: nmdc_community_metabolic_ecology]

## Evidence

> One outlier was tyrosine (r = +0.419, ns), whose anti-BQH direction may reflect alternative tyrosine sources (e.g., phenylalanine hydroxylation) complicating the biosynthesis-vs-availability relationship. Isoleucine biosynthesis (r = −0.057, n = 18, q = 0.823) is testable as the 13th pathway but shows no BQH signal at this sample size. [src: nmdc_community_metabolic_ecology]

From the report [[summaries/nmdc_community_metabolic_ecology__REPORT]].

## Caveat

Tyrosine can be produced from phenylalanine via non-biosynthetic hydroxylation, which the tyr completeness score does not capture, so the opposite sign may reflect decoupling of biosynthesis and pool. [src: nmdc_community_metabolic_ecology]

> The tyrosine outlier (r = +0.42) merits caution: tyrosine can be produced from phenylalanine via non-biosynthetic hydroxylation, so communities with high *phenylalanine* biosynthesis completeness — not captured in our `tyr` completeness score — may still supply tyrosine, decoupling the biosynthesis-vs-pool relationship. [src: nmdc_community_metabolic_ecology]

## Other caveats in this report

- The 220-sample cohort comprised 126 soil, 33 freshwater, and 61 ecosystem-unrecorded samples. All 33 freshwater samples lacked paired metabolomics, excluding them from H1 but not H2. [src: nmdc_community_metabolic_ecology]
- H1 was overwhelmingly single-study: 125/131 samples (95%) came from nmdc:sty-11-r2h77870. All leucine samples came from that study, and the arginine association persisted after excluding the six samples from nmdc:sty-11-547rwq94. [src: nmdc_community_metabolic_ecology]
- The listed positive, soil-directed PC1 loadings are glucuronate, fumarate, succinate, lysine, and cellobiose. The source calls all five carbon-utilization pathways, although lysine is also identified elsewhere in the report as an amino-acid pathway. [src: nmdc_community_metabolic_ecology]
- The report interprets the leucine and arginine associations in light of stated synthesis costs of 37 and 26 ATP equivalents, respectively. This is a mechanistic interpretation, not direct evidence of gene loss; the predicted benefit of more methionine data remains untested. [src: nmdc_community_metabolic_ecology]
- Correcting three misassigned isoleucine compounds changed the leucine result from r −0.326 to −0.390 and q 0.045 to 0.022. [src: nmdc_community_metabolic_ecology]
