<!-- tension-hash: 59068bf500948962 -->
# Universal Positive Metal Cross-Resistance: Metal-Specific Mechanism or General-Stress Response?

All tested metal pairs were positive, but it is unresolved whether that positivity reflects metal-specific cross-resistance or a general-stress response, because no non-metal stress controls were included. [src: metal_cross_resistance] This matters for [[concepts/metal-cross-resistance]]. Cross-resistance means fitness responses to one metal predict responses to another. If the signal is mostly general stress, the term would overstate how much metals share specific resistance genes. The specificity analysis finds a substantial metal-specific component, but it also finds 38.0% general-sick and 7.2% metal+stress records, so the cause of the positivity remains open. [src: metal_specificity]

## Evidence Sides

**Side A: universal positivity without a non-metal control**

All tested metal pairs were positive. [src: metal_cross_resistance] However, the study included no non-metal stress controls, so it cannot on its own separate metal-specific cross-resistance from a general-stress response. [src: metal_cross_resistance] The report notes that the counter_ion_effects project partially addresses this gap. [src: metal_cross_resistance] On this side, the universal positivity is an established pattern whose cause the study cannot independently resolve.

**Side B: a substantial metal-specific component, with residual ambiguity**

The specificity analysis classifies metal-important gene records by whether they also cause fitness defects in non-metal experiments. [src: metal_specificity] It **supports** the existence of a substantial metal-specific component. [src: metal_specificity] It also finds two other classes. General-sick records are genes whose loss impairs growth broadly across conditions, and they make up 38.0% of records. Metal+stress records are genes important under metals and also under other stresses, and they make up 7.2%. [src: metal_specificity] Because of these classes, the analysis does not eliminate the causal ambiguity. [src: metal_specificity]

## Possible Reconciliations

- *Hypothesis:* The universal positivity is a mixture. Metal-specific genes drive part of the correlation, and general-sick genes add a shared baseline that would push correlations positive under any pair of stressful conditions.
- *Hypothesis:* Metal+stress genes are the bridge. Positivity driven by them would be neither strictly metal-specific nor fully general.
- *Hypothesis:* The strength of correlation for a given metal pair depends on the share of metal-specific genes it involves. On this view, the two projects measure different slices of the same gene set rather than conflicting.

## Resolving Work

- Recompute the metal-pair fitness correlations from the metal cross-resistance analysis using only records classified as metal-specific. This tests whether the correlations stay positive without general-sick and metal+stress records.
- Correlate fitness under each metal against non-metal stress experiments in the same organisms. This tests whether metal–non-metal pairs are as uniformly positive as metal–metal pairs, which would be the missing stress control.
- Integrate counter_ion_effects results with the specificity classes. A counter-ion is the accompanying ion in a metal salt. This tests how much of the positivity follows from that counter-ion or salt component of metal treatments rather than the metal itself.
- Stratify metal pairs by their share of metal+stress records. This tests whether pairs dominated by shared stress genes show stronger cross-resistance than pairs dominated by metal-specific genes.
