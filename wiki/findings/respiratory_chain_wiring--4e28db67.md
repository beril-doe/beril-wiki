---
type: "Finding"
description: "ADP1 quinate catabolism produces fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), yet Complex I is more essential on quinate."
finding_id: "respiratory_chain_wiring--4e28db67"
result: "observation"
source: "respiratory_chain_wiring"
quantities: [{"value": "0.57", "what": "NADH per carbon atom on quinate", "unit": "", "denominator": "", "scope": ""}, {"value": "1.50", "what": "NADH per carbon atom on glucose and on acetate", "unit": "", "denominator": "", "scope": ""}]
caveat: "The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions."
first_added: "2026-11-24"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# Complex I is most needed on the lowest-NADH-yield substrate

ADP1 quinate catabolism produces fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), yet Complex I is more essential on quinate. [src: respiratory_chain_wiring]

## Key figures

- **0.57**: NADH per carbon atom on quinate [src: respiratory_chain_wiring]
- **1.50**: NADH per carbon atom on glucose and on acetate [src: respiratory_chain_wiring]

## Evidence

> Quinate produces FEWER NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), yet Complex I is MORE essential on quinate. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions. [src: respiratory_chain_wiring]

> The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions [src: respiratory_chain_wiring]

## Other caveats in this report

- ADP1 NDH-2 is missing from the deletion collection and has no growth data. [src: respiratory_chain_wiring]
- The cross-species NDH-2 analysis excludes organisms with >2 NDH-2 hits as likely misannotated Complex I subunits and retains organisms with 1-2 hits. [src: respiratory_chain_wiring]
- The report cautions that ADP1 respiratory wiring may be species-specific rather than general. [src: respiratory_chain_wiring]
- Of ADP1 respiratory-chain genes, 36 have growth data and 26 do not, with missing data including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]
- The report states that FBA fails to predict condition-specific respiratory requirements because optimal-pathway assumptions miss capacity constraints that force alternative suboptimal pathways at high flux. [src: respiratory_chain_wiring]
