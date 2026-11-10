---
type: "Finding"
description: "In exploratory OLS adjusted for depth, latitude, longitude, and mapped-abundance fraction, the defense coefficient was positive under relaxed mapping (beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462), while strict mapping gave beta = 0.000640, p = 0.00354, FDR q = 0.130."
finding_id: "enigma_contamination_functional_potential--a97faeef"
result: "observation"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "0.000751", "what": "OLS contamination coefficient for defense score", "unit": "", "denominator": "", "scope": "relaxed_all_clades, adjusted for depth, latitude, longitude, mapped-abundance fraction"}, {"value": "0.0462", "what": "FDR q-value", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}, {"value": "0.130", "what": "FDR q-value", "unit": "", "denominator": "", "scope": "strict_single_clade"}]
caveat: "Exploratory significance is concentrated in defense and depends on coverage and covariate specification; a broader effect across outcomes is not yet established."
first_added: "2026-10-27"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# Covariate-adjusted models give a positive defense-contamination signal in relaxed mapping

In exploratory OLS adjusted for depth, latitude, longitude, and mapped-abundance fraction, the defense coefficient was positive under relaxed mapping (beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462), while strict mapping gave beta = 0.000640, p = 0.00354, FDR q = 0.130. [src: enigma_contamination_functional_potential]

## Key figures

- **0.000751**: OLS contamination coefficient for defense score (scope relaxed_all_clades, adjusted for depth, latitude, longitude, mapped-abundance fraction) [src: enigma_contamination_functional_potential]
- **0.0462**: FDR q-value (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]
- **0.130**: FDR q-value (scope strict_single_clade) [src: enigma_contamination_functional_potential]

## Evidence

> - Coverage-adjusted OLS (`contamination + depth + latitude + longitude + mapped_abundance_fraction`): - `relaxed_all_clades`: beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462 - `strict_single_clade`: beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, FDR q = 0.130 [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

Exploratory significance is concentrated in defense and depends on coverage and covariate specification; a broader effect across outcomes is not yet established. [src: enigma_contamination_functional_potential]

> - Exploratory sensitivity-model significance is concentrated in defense and depends on coverage/covariate specification; broader effect across outcomes is not yet established. [src: enigma_contamination_functional_potential]

## Other caveats in this report

- The species-proxy high-coverage analysis is underpowered at n=1; fraction-level analyses use more rows. [src: enigma_contamination_functional_potential]
- The report designates Spearman tests as confirmatory and adjusted models as exploratory sensitivity analyses. [src: enigma_contamination_functional_potential]
- Fraction-aware analyses address potential confounding from collapsing community fractions. [src: enigma_contamination_functional_potential]
- Because available ENIGMA taxonomy stops at genus, the species-proxy mode approximates higher resolution using only genera mapping to exactly one GTDB species clade. [src: enigma_contamination_functional_potential]
- A species-proxy high-coverage test was infeasible at mapped-abundance fraction >= 0.25 because too little coverage remained. [src: enigma_contamination_functional_potential]
