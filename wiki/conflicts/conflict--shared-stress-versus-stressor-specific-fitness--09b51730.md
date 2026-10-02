<!-- tension-hash: 09b5173096c2ab0c -->
# Does Universal Positive Metal Cross-Resistance Imply a Uniform Shared-Stress Response?

Two projects measure overlap between fitness profiles — genome-wide measurements of how gene knockouts change in abundance under a stress — but reach different pictures of how uniform that overlap is. The metal cross-resistance study finds that all tested metal-pair correlations were positive and reads this as a universal directional layer of shared stress response [src: metal_cross_resistance], while the counter-ion analysis finds that metal–NaCl correlations vary substantially across metals, spanning iron r=0.086 to zinc r=0.715, where r is the Pearson correlation coefficient between two conditions' gene-level fitness values [src: counter_ion_effects]. The disagreement matters because it decides whether a positive correlation between two metal conditions can be attributed to one general stress program, or whether the shared component must be decomposed per stressor before any mechanistic claim is made — the core requirement of [[concepts/shared-stress-versus-stressor-specific-fitness]].

## Evidence Sides

**Universal directional layer.** The metal cross-resistance study reports that all tested metal-pair correlations were positive and interprets this as a universal directional layer, i.e. a shared component that never reverses sign between metals [src: metal_cross_resistance].

**Stressor-dependent overlap.** The counter-ion analysis shows that metal–NaCl correlations vary substantially across metals, including iron r=0.086 and zinc r=0.715 [src: counter_ion_effects]. Positivity across metal pairs therefore does not establish a uniform response to NaCl, nor identify which shared stressor generates the signal [src: metal_cross_resistance, counter_ion_effects].

This is not a direct contradiction, because the analyses compare different condition pairs: metal–metal pairs on one side, metal–NaCl pairs on the other [src: metal_cross_resistance, counter_ion_effects]. The counter-ion result **refines** rather than overturns the cross-resistance interpretation [src: metal_cross_resistance, counter_ion_effects].

## Possible Reconciliations

- *Hypothesis: sign versus magnitude.* The two results may be compatible if the universal layer constrains only the sign of correlations, while magnitude is set stressor-by-stressor — a picture in which iron r=0.086 remains positive yet near-uninformative [src: counter_ion_effects].
- *Hypothesis: different denominators.* The universal claim is stated over tested metal pairs [src: metal_cross_resistance] and the variable claim over metal–NaCl pairs [src: counter_ion_effects]; the tension may dissolve entirely once each claim is read against its own denominator [src: metal_cross_resistance, counter_ion_effects].
- *Hypothesis: multiple shared components.* There may be more than one shared-stress axis, so that metals co-vary strongly with each other while loading unevenly onto the NaCl axis [src: metal_cross_resistance, counter_ion_effects]. This remains a hypothesis; no side tests it directly.

## Resolving Work

- Recompute metal–metal and metal–NaCl correlations in the same organisms and the same gene set, then ask whether the variation seen for NaCl also appears within metal pairs [src: metal_cross_resistance, counter_ion_effects].
- Decompose each metal fitness profile into a shared component and a residual, then test whether all-positive metal-pair correlations survive removal of the shared component [src: metal_cross_resistance].
- Ask what distinguishes iron at r=0.086 from zinc at r=0.715, using per-gene contributions rather than whole-profile summaries [src: counter_ion_effects].
- Test whether the universal positivity claim holds when NaCl is included as one more condition in the pair set, which would place both claims on a single denominator [src: metal_cross_resistance, counter_ion_effects].
