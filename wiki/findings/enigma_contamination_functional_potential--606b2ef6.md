---
type: "Finding"
description: "All index variants in both confirmatory mapping modes remained non-significant after FDR (q = 0.546 across the 8 confirmatory-variant tests), including uranium-only."
finding_id: "enigma_contamination_functional_potential--606b2ef6"
result: "null result"
source: "enigma_contamination_functional_potential"
quantities: [{"value": "0.546", "what": "FDR q across the confirmatory-variant tests", "unit": "", "denominator": "8 confirmatory-variant tests", "scope": "both confirmatory mapping modes, all index variants"}]
caveat: "The null applies to genus-aggregated broad-COG functional proxies; functional redundancy or species-, strain-, or pathway-scale responses remain possible interpretations, not established results."
first_added: "2026-10-27"
source_hash: "4dcb3d9608b4e864e109a4e0ca80952e30f26797b2d3de85a58962f773ba79f1"
---
# Confirmatory defense null holds across alternative contamination index definitions

All index variants in both confirmatory mapping modes remained non-significant after FDR (q = 0.546 across the 8 confirmatory-variant tests), including uranium-only. [src: enigma_contamination_functional_potential]

## Key figures

- **0.546**: FDR q across the confirmatory-variant tests (denominator 8 confirmatory-variant tests; scope both confirmatory mapping modes, all index variants) [src: enigma_contamination_functional_potential]

## Evidence

> Across both confirmatory mapping modes, all index variants remained non-significant after FDR (`q = 0.546` across the 8 confirmatory-variant tests), including uranium-only. [src: enigma_contamination_functional_potential]

From the report [[summaries/enigma_contamination_functional_potential__REPORT]].

## Caveat

The null applies to genus-aggregated broad-COG functional proxies; functional redundancy or species-, strain-, or pathway-scale responses remain possible interpretations, not established results. [src: enigma_contamination_functional_potential]

> Within this ENIGMA subset, contamination gradients did not translate into a robust community-level shift in inferred stress-related functional potential when features are aggregated at genus resolution from broad COG categories. This is compatible with contamination-driven taxonomic turnover that is functionally redundant or too fine-scale (species/strain/pathway level) for the present mapping. [src: enigma_contamination_functional_potential]

## Other caveats in this report

- The species-proxy high-coverage analysis is underpowered at n=1; fraction-level analyses use more rows. [src: enigma_contamination_functional_potential]
- The report designates Spearman tests as confirmatory and adjusted models as exploratory sensitivity analyses. [src: enigma_contamination_functional_potential]
- Fraction-aware analyses address potential confounding from collapsing community fractions. [src: enigma_contamination_functional_potential]
- Because available ENIGMA taxonomy stops at genus, the species-proxy mode approximates higher resolution using only genera mapping to exactly one GTDB species clade. [src: enigma_contamination_functional_potential]
- A species-proxy high-coverage test was infeasible at mapped-abundance fraction >= 0.25 because too little coverage remained. [src: enigma_contamination_functional_potential]
