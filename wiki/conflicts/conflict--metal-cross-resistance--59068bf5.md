<!-- tension-hash: 59068bf500948962 -->
# Metal-specific cross-resistance or a general-stress response: what the universal positivity measures

Gene-level metal cross-resistance — the tendency for a gene's fitness response to one metal to predict its response to another — is reported as uniformly positive across the tested metal pairs, but the corpus disagrees about what that uniformity measures. One report records the positivity while noting that no non-metal stress controls were included, leaving it unable to separate metal-specific cross-resistance from a general-stress response [src: metal_cross_resistance]. A separate specificity analysis supplies a non-metal comparison and supports a substantial metal-specific component, yet its 38.0% general-sick and 7.2% metal+stress records leave the causal ambiguity in place [src: metal_specificity]. The distinction matters because it determines whether cross-resistance matrices can predict metal-specific vulnerabilities, or whether they mostly re-describe which genes are fragile under any insult.

## Evidence Sides

**Universal positivity, without non-metal controls.** All tested metal pairs were positive, but no non-metal stress controls were included in the design [src: metal_cross_resistance]. The report itself flags this as a tension between the strength of the universal positivity and uncertainty about its cause [src: metal_cross_resistance]. The counter_ion_effects project is identified as partially addressing the issue, but the study cannot independently separate metal-specific cross-resistance from a general-stress response [src: metal_cross_resistance]. This side is therefore explicitly a null on the controls, not a claim that the general-stress explanation was tested and rejected.

**A substantial metal-specific component, with residual ambiguity.** A specificity analysis — classifying each metal-important gene record by whether it is also sick outside metal conditions — **supports** the existence of a substantial metal-specific component [src: metal_specificity]. It nonetheless found 38.0% general-sick records (genes sick broadly, not only under metals) and 7.2% metal+stress records (genes sick under metals and under other stresses), so it does not eliminate the causal ambiguity [src: metal_specificity]. This side refines rather than overturns the first: it supplies the missing non-metal comparison, but the residual fractions keep the causal question open.

## Possible Reconciliations

- *Hypothesis:* the two results are compatible if cross-resistance is a mixture — a metal-specific core plus a general-stress background — in which case the universal positivity would aggregate both components rather than evidence either alone.
- *Hypothesis:* the general-sick and metal+stress fractions may be concentrated in a subset of organisms or metals, so that per-pair correlations differ in how much general-stress signal they carry.
- *Hypothesis:* part of the shared positive signal may arise from the effects that the counter_ion_effects project is identified as partially addressing, rather than from a shared metal mechanism [src: metal_cross_resistance].

## Resolving Work

- Re-compute the pairwise cross-resistance correlations after excluding the 38.0% general-sick records, and ask whether universal positivity survives the exclusion [src: metal_specificity].
- Add non-metal stress conditions as explicit controls in the cross-resistance design, and test whether metal–non-metal correlations match metal–metal correlations [src: metal_cross_resistance].
- Repeat the specificity classification at alternative sick-rate thresholds and ask how sensitive the metal-specific/general-sick split is to threshold choice [src: metal_specificity].
- Stratify the 7.2% metal+stress records by organism and metal pair, and ask whether the ambiguity is uniform or localised [src: metal_specificity].

Source concept: [[concepts/metal-cross-resistance]]
