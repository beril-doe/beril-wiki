---
type: "Finding"
description: "ACIAD3522, a one-subunit non-proton-pumping NADH-FMN oxidoreductase, has growth ratios of 1.39 on quinate, 1.39 on glucose, and 0.013 on acetate (lethal)."
finding_id: "respiratory_chain_wiring--d117b49e"
result: "observation"
source: "respiratory_chain_wiring"
quantities: [{"value": "0.013", "what": "ACIAD3522 growth ratio on acetate", "unit": "", "denominator": "", "scope": "lethal"}, {"value": "1.39", "what": "ACIAD3522 growth ratio on quinate and glucose", "unit": "", "denominator": "", "scope": "dispensable"}]
caveat: "ACIAD3522 may not be a true respiratory NADH dehydrogenase, since NADH-FMN oxidoreductase could serve other metabolic functions."
first_added: "2026-11-09"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# ACIAD3522 is lethal on acetate but dispensable on quinate and glucose

ACIAD3522, a one-subunit non-proton-pumping NADH-FMN oxidoreductase, has growth ratios of 1.39 on quinate, 1.39 on glucose, and 0.013 on acetate (lethal). [src: respiratory_chain_wiring]

## Key figures

- **0.013**: ACIAD3522 growth ratio on acetate (scope lethal) [src: respiratory_chain_wiring]
- **1.39**: ACIAD3522 growth ratio on quinate and glucose (scope dispensable) [src: respiratory_chain_wiring]

## Evidence

> | ACIAD3522 (NADH-FMN OR) | 1 | No | 1.39 (dispensable) | 1.39 (dispensable) | 0.013 (lethal) | [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

ACIAD3522 may not be a true respiratory NADH dehydrogenase, since NADH-FMN oxidoreductase could serve other metabolic functions. [src: respiratory_chain_wiring]

> - ACIAD3522 may not be a true NADH dehydrogenase in the respiratory sense — "NADH-FMN oxidoreductase" could serve other metabolic functions [src: respiratory_chain_wiring]

## Other caveats in this report

- The flux-balance analysis (FBA) model predicts zero flux through NDH-2 and ACIAD3522 on standard media. The report attributes its failure to predict condition-specific requirements to missing capacity constraints. [src: respiratory_chain_wiring]
- The central prediction that NDH-2 compensates on glucose cannot be directly tested because NDH-2 lacks growth data. [src: respiratory_chain_wiring]
- The NADH stoichiometry and flux-rate explanation rely on theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison includes only 4 organisms without NDH-2 and is underpowered. [src: respiratory_chain_wiring]
- Variable annotation may cause the NDH-2 search to miss orthologs in Fitness Browser organisms. [src: respiratory_chain_wiring]
