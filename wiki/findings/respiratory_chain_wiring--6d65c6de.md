---
type: "Finding"
description: "ADP1's branched respiratory chain (62 genes across 8 subsystems) is described as wired in a condition-dependent manner: quinate requires only Complex I, acetate requires Complex I, cytochrome bo3, ACIAD3522, and more, and glucose requires no specific respiratory component, which the report calls qualitatively different configurations per substrate rather than a quantitative gradient."
finding_id: "respiratory_chain_wiring--6d65c6de"
result: "observation"
source: "respiratory_chain_wiring"
quantities: [{"value": "62", "what": "respiratory chain genes in ADP1", "unit": "genes", "denominator": "", "scope": "across 8 subsystems"}, {"value": "8", "what": "respiratory subsystems", "unit": "subsystems", "denominator": "", "scope": "ADP1 respiratory chain"}]
caveat: "NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested with this dataset."
first_added: "2026-11-09"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# Respiratory requirements in ADP1 differ qualitatively by carbon source

ADP1's branched respiratory chain (62 genes across 8 subsystems) is described as wired in a condition-dependent manner: quinate requires only Complex I, acetate requires Complex I, cytochrome bo3, ACIAD3522, and more, and glucose requires no specific respiratory component, which the report calls qualitatively different configurations per substrate rather than a quantitative gradient. [src: respiratory_chain_wiring]

## Key figures

- **62 genes**: respiratory chain genes in ADP1 (scope across 8 subsystems) [src: respiratory_chain_wiring]
- **8 subsystems**: respiratory subsystems (scope ADP1 respiratory chain) [src: respiratory_chain_wiring]

## Evidence

> ADP1's branched respiratory chain (62 genes across 8 subsystems) is wired in a condition-dependent manner. Quinate requires only Complex I; acetate requires Complex I, cytochrome bo3, ACIAD3522, and more; glucose requires no specific respiratory component. This is not a quantitative gradient — it's qualitatively different respiratory configurations per substrate. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested with this dataset. [src: respiratory_chain_wiring]

> - NDH-2 has no growth data — the central prediction (NDH-2 compensates on glucose) cannot be directly tested with this dataset [src: respiratory_chain_wiring]

## Other caveats in this report

- The flux-balance analysis (FBA) model predicts zero flux through NDH-2 and ACIAD3522 on standard media. The report attributes its failure to predict condition-specific requirements to missing capacity constraints. [src: respiratory_chain_wiring]
- The NADH stoichiometry and flux-rate explanation rely on theoretical pathway biochemistry rather than measured flux distributions. [src: respiratory_chain_wiring]
- The cross-species comparison includes only 4 organisms without NDH-2 and is underpowered. [src: respiratory_chain_wiring]
- Variable annotation may cause the NDH-2 search to miss orthologs in Fitness Browser organisms. [src: respiratory_chain_wiring]
- ACIAD3522's classification as a respiratory NADH dehydrogenase is uncertain; it may have another metabolic function. [src: respiratory_chain_wiring]
