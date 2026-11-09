---
type: "Finding"
description: "Although quinate produces fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), Complex I is more essential on quinate, and the report proposes that \u03b2-ketoadipate ring cleavage creates a concentrated TCA-cycle NADH burst exceeding NDH-2's reoxidation capacity."
finding_id: "respiratory_chain_wiring--e16ee45a"
result: "inference"
source: "respiratory_chain_wiring"
quantities: [{"value": "0.57", "what": "NADH per carbon atom on quinate", "unit": "NADH/carbon", "denominator": "", "scope": "theoretical stoichiometry"}, {"value": "1.50", "what": "NADH per carbon atom on glucose (and on acetate)", "unit": "NADH/carbon", "denominator": "", "scope": "theoretical stoichiometry"}]
caveat: "The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions."
first_added: "2026-11-09"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# Quinate Complex I dependence proposed to reflect NADH burst rate, not yield

Although quinate produces fewer NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), Complex I is more essential on quinate, and the report proposes that β-ketoadipate ring cleavage creates a concentrated TCA-cycle NADH burst exceeding NDH-2's reoxidation capacity. [src: respiratory_chain_wiring]

## Key figures

- **0.57 NADH/carbon**: NADH per carbon atom on quinate (scope theoretical stoichiometry) [src: respiratory_chain_wiring]
- **1.50 NADH/carbon**: NADH per carbon atom on glucose (and on acetate) (scope theoretical stoichiometry) [src: respiratory_chain_wiring]

## Evidence

> Quinate produces FEWER NADH per carbon atom (0.57) than glucose (1.50) or acetate (1.50), yet Complex I is MORE essential on quinate. The resolution: aromatic ring cleavage via the β-ketoadipate pathway produces succinyl-CoA + acetyl-CoA simultaneously, creating a concentrated NADH burst in the TCA cycle that exceeds NDH-2's reoxidation capacity. Glucose distributes NADH production across Entner-Doudoroff pathway steps plus TCA, staying within NDH-2's capacity. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions. [src: respiratory_chain_wiring]

> - The stoichiometry analysis uses theoretical pathway biochemistry, not measured flux distributions [src: respiratory_chain_wiring]

## Other caveats in this report

- The flux-balance analysis (FBA) model predicts zero flux through NDH-2 and ACIAD3522 on standard media. The report attributes its failure to predict condition-specific requirements to missing capacity constraints. [src: respiratory_chain_wiring]
- The central prediction that NDH-2 compensates on glucose cannot be directly tested because NDH-2 lacks growth data. [src: respiratory_chain_wiring]
- The cross-species comparison includes only 4 organisms without NDH-2 and is underpowered. [src: respiratory_chain_wiring]
- Variable annotation may cause the NDH-2 search to miss orthologs in Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522's classification as a respiratory NADH dehydrogenase is uncertain; it may have another metabolic function. [src: respiratory_chain_wiring]
