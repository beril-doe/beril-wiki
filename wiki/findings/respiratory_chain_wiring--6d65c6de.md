---
type: "Finding"
description: "ADP1's branched respiratory chain (62 genes across 8 subsystems) is wired in a condition-dependent manner: quinate requires only Complex I, acetate requires Complex I, cytochrome bo3, ACIAD3522 and more, and glucose requires no specific respiratory component, which the report calls qualitatively different configurations rather than a quantitative gradient."
finding_id: "respiratory_chain_wiring--6d65c6de"
result: "observation"
source: "respiratory_chain_wiring"
quantities: [{"value": "62", "what": "genes in the ADP1 branched respiratory chain", "unit": "genes", "denominator": "", "scope": "ADP1, across 8 subsystems"}]
caveat: "The ADP1 respiratory wiring pattern may be species-specific rather than a general rule."
first_added: "2026-11-24"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# ADP1 uses qualitatively different respiratory configurations on different carbon sources

ADP1's branched respiratory chain (62 genes across 8 subsystems) is wired in a condition-dependent manner: quinate requires only Complex I, acetate requires Complex I, cytochrome bo3, ACIAD3522 and more, and glucose requires no specific respiratory component, which the report calls qualitatively different configurations rather than a quantitative gradient. [src: respiratory_chain_wiring]

## Key figures

- **62 genes**: genes in the ADP1 branched respiratory chain (scope ADP1, across 8 subsystems) [src: respiratory_chain_wiring]

## Evidence

> ADP1's branched respiratory chain (62 genes across 8 subsystems) is wired in a condition-dependent manner. Quinate requires only Complex I; acetate requires Complex I, cytochrome bo3, ACIAD3522, and more; glucose requires no specific respiratory component. This is not a quantitative gradient — it's qualitatively different respiratory configurations per substrate. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

The ADP1 respiratory wiring pattern may be species-specific rather than a general rule. [src: respiratory_chain_wiring]

> The ADP1 respiratory wiring pattern may be species-specific rather than a general rule. [src: respiratory_chain_wiring]

## Other caveats in this report

- ADP1 NDH-2 is missing from the deletion collection and has no growth data. [src: respiratory_chain_wiring]
- The cross-species NDH-2 analysis excludes organisms with >2 NDH-2 hits as likely misannotated Complex I subunits and retains organisms with 1-2 hits. [src: respiratory_chain_wiring]
- Of ADP1 respiratory-chain genes, 36 have growth data and 26 do not, with missing data including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]
- The report states that FBA fails to predict condition-specific respiratory requirements because optimal-pathway assumptions miss capacity constraints that force alternative suboptimal pathways at high flux. [src: respiratory_chain_wiring]
- The ADP1 dataset has no NDH-2 growth data, so the central prediction that NDH-2 compensates on glucose cannot be tested directly. [src: respiratory_chain_wiring]
