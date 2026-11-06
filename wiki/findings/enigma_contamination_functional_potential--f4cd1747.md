---
type: "Finding"
description: "In the predeclared confirmatory Spearman test under relaxed_all_clades mapping, the association was rho = 0.0587, 95% bootstrap CI [-0.128, 0.250], Spearman p = 0.546, FDR q = 0.862."
finding_id: "enigma_contamination_functional_potential--f4cd1747"
result: "null result"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "0.0587", "what": "Spearman rho, site defense score vs contamination", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}, {"value": "[-0.128, 0.250]", "what": "95% bootstrap CI for rho", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}, {"value": "0.862", "what": "FDR q-value", "unit": "", "denominator": "", "scope": "relaxed_all_clades"}]
caveat: "The current pangenome bridge did not map 862 of 1,392 observed genera, so the null covers only the mapped genera."
first_added: "2026-10-27"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# No significant defense–contamination association in relaxed mapping

In the predeclared confirmatory Spearman test under relaxed_all_clades mapping, the association was rho = 0.0587, 95% bootstrap CI [-0.128, 0.250], Spearman p = 0.546, FDR q = 0.862. [src: enigma_contamination_functional_potential]

## Key figures

- **0.0587**: Spearman rho, site defense score vs contamination (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]
- **[-0.128, 0.250]**: 95% bootstrap CI for rho (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]
- **0.862**: FDR q-value (scope relaxed_all_clades) [src: enigma_contamination_functional_potential]

## Evidence

> - `relaxed_all_clades`: rho = 0.0587, 95% bootstrap CI [-0.128, 0.250], Spearman p = 0.546, FDR q = 0.862 [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

The current pangenome bridge did not map 862 of 1,392 observed genera, so the null covers only the mapped genera. [src: enigma_contamination_functional_potential]

> - 862/1,392 observed genera were unmapped to current pangenome bridge. [src: enigma_contamination_functional_potential]

## Other caveats in this report

- The species-proxy high-coverage analysis is underpowered at n=1; fraction-level analyses use more rows. [src: enigma_contamination_functional_potential]
- The report designates Spearman tests as confirmatory and adjusted models as exploratory sensitivity analyses. [src: enigma_contamination_functional_potential]
- Fraction-aware analyses address potential confounding from collapsing community fractions. [src: enigma_contamination_functional_potential]
- Because available ENIGMA taxonomy stops at genus, the species-proxy mode approximates higher resolution using only genera mapping to exactly one GTDB species clade. [src: enigma_contamination_functional_potential]
- A species-proxy high-coverage test was infeasible at mapped-abundance fraction >= 0.25 because too little coverage remained. [src: enigma_contamination_functional_potential]
