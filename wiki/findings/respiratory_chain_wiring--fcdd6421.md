---
type: "Finding"
description: "After filtering likely misannotations, 5 of 14 organisms have validated NDH-2, and those with NDH-2 show larger Complex I aromatic deficits (mean = -0.297) than those without (mean = -0.156), opposite to the compensation prediction and not significant (p = 0.52)."
finding_id: "respiratory_chain_wiring--fcdd6421"
result: "null result"
source: "respiratory_chain_wiring"
quantities: [{"value": "5 of 14", "what": "organisms with validated NDH-2", "unit": "organisms", "denominator": "14 organisms", "scope": "after filtering to 1-2 NDH-2 hits"}, {"value": "-0.297", "what": "mean Complex I aromatic deficit with NDH-2", "unit": "", "denominator": "", "scope": ""}, {"value": "-0.156", "what": "mean Complex I aromatic deficit without NDH-2", "unit": "", "denominator": "", "scope": ""}, {"value": "0.52", "what": "p-value of comparison", "unit": "", "denominator": "", "scope": "not significant"}]
caveat: "The cross-species comparison has only 4 organisms without NDH-2, insufficient for statistical significance."
first_added: "2026-11-09"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# Alternative dehydrogenase presence does not predict Complex I dispensability across species

After filtering likely misannotations, 5 of 14 organisms have validated NDH-2, and those with NDH-2 show larger Complex I aromatic deficits (mean = -0.297) than those without (mean = -0.156), opposite to the compensation prediction and not significant (p = 0.52). [src: respiratory_chain_wiring]

## Key figures

- **5 of 14 organisms**: organisms with validated NDH-2 (denominator 14 organisms; scope after filtering to 1-2 NDH-2 hits) [src: respiratory_chain_wiring]
- **-0.297**: mean Complex I aromatic deficit with NDH-2 [src: respiratory_chain_wiring]
- **-0.156**: mean Complex I aromatic deficit without NDH-2 [src: respiratory_chain_wiring]
- **0.52**: p-value of comparison (scope not significant) [src: respiratory_chain_wiring]

## Evidence

> After correcting for likely false positives in NDH-2 identification (filtering to organisms with 1-2 NDH-2 hits, excluding those with >2 hits that likely represent misannotated Complex I subunits), 5 of 14 organisms have validated NDH-2. Organisms WITH NDH-2 show LARGER Complex I aromatic deficits (mean = -0.297) than those WITHOUT (mean = -0.156), the opposite of the compensation prediction (p = 0.52, not significant). The NDH-2 compensation hypothesis is not supported by cross-species fitness data — NDH-2 presence does not predict whether Complex I is dispensable on aromatics. The ADP1 respiratory wiring pattern may be species-specific rather than a general rule. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

The cross-species comparison has only 4 organisms without NDH-2, insufficient for statistical significance. [src: respiratory_chain_wiring]

> - Cross-species comparison has only 4 organisms without NDH-2, insufficient for statistical significance [src: respiratory_chain_wiring]

## Other caveats in this report

- The flux-balance analysis (FBA) model predicts zero flux through NDH-2 and ACIAD3522 on standard media. The report attributes its failure to predict condition-specific requirements to missing capacity constraints. [src: respiratory_chain_wiring]
- The central prediction that NDH-2 compensates on glucose cannot be directly tested because NDH-2 lacks growth data. [src: respiratory_chain_wiring]
- The NADH stoichiometry and flux-rate explanation rely on theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- Variable annotation may cause the NDH-2 search to miss orthologs in Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522's classification as a respiratory NADH dehydrogenase is uncertain; it may have another metabolic function. [src: respiratory_chain_wiring]
