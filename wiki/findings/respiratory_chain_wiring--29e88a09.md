---
type: "Finding"
description: "The report interprets ADP1 condition-specific respiratory wiring as operating at the metabolic level, with all three dehydrogenases present simultaneously and the limiting one depending on carbon-source NADH flux, a passive flux-based system rather than an active transcriptional switch."
finding_id: "respiratory_chain_wiring--29e88a09"
result: "inference"
source: "respiratory_chain_wiring"
quantities: []
caveat: "NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested with this dataset."
first_added: "2026-11-24"
source_hash: "e44ee5fea95d2bf94013d27d0b2afd372d6612ac3bf997f73e2813afe5bb42b3"
---
# Respiratory wiring appears passive and flux-based, not a transcriptional switch

The report interprets ADP1 condition-specific respiratory wiring as operating at the metabolic level, with all three dehydrogenases present simultaneously and the limiting one depending on carbon-source NADH flux, a passive flux-based system rather than an active transcriptional switch. [src: respiratory_chain_wiring]

## Evidence

> This means the condition-specific respiratory wiring operates at the metabolic level: all three dehydrogenases are present simultaneously, and which one becomes limiting depends on the NADH flux rate from the carbon source being catabolized. The cell uses a passive, flux-based wiring system rather than an active transcriptional switch. [src: respiratory_chain_wiring]

From the report [[summaries/respiratory_chain_wiring__REPORT]].

## Caveat

NDH-2 has no growth data, so the central prediction that NDH-2 compensates on glucose cannot be directly tested with this dataset. [src: respiratory_chain_wiring]

> NDH-2 has no growth data — the central prediction (NDH-2 compensates on glucose) cannot be directly tested with this dataset [src: respiratory_chain_wiring]

## Other caveats in this report

- ADP1 NDH-2 is missing from the deletion collection and has no growth data. [src: respiratory_chain_wiring]
- The cross-species NDH-2 analysis excludes organisms with >2 NDH-2 hits as likely misannotated Complex I subunits and retains organisms with 1-2 hits. [src: respiratory_chain_wiring]
- The report cautions that ADP1 respiratory wiring may be species-specific rather than general. [src: respiratory_chain_wiring]
- Of ADP1 respiratory-chain genes, 36 have growth data and 26 do not, with missing data including NDH-2 and several ATP synthase subunits. [src: respiratory_chain_wiring]
- The report states that FBA fails to predict condition-specific respiratory requirements because optimal-pathway assumptions miss capacity constraints that force alternative suboptimal pathways at high flux. [src: respiratory_chain_wiring]
