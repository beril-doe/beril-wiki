<!-- tension-hash: 2d1b0ad4ef2f5576 -->
# Metal Cross-Resistance: Metal-Specific Shared Mechanisms or General Stress Response?

This tension comes from [[concepts/cofitness-network-architecture]]. All tested metal pairs were positive in gene-level fitness comparisons, where fitness is the growth effect of disrupting a gene under a condition [src: metal_cross_resistance]. The open question is whether that uniformly positive signal reflects cross-resistance mechanisms shared among metals or a general-stress response that any harsh condition would trigger. It matters because metal-pair relationships are read as network architecture: if shared vulnerability inflates them, inferences about metal-specific support networks are confounded. The metal study included no negative controls [src: metal_cross_resistance]. A counter-ion study, which tests whether the anion delivered with a metal salt (its counter-ion, such as chloride) explains overlap with NaCl (sodium chloride, an osmotic/ionic stressor), reports 4,304/10,821 shared NaCl–metal records, with zinc sulfate at 44.6% overlap despite 0 mM chloride [src: counter_ion_effects].

## Evidence Sides

**Side 1: Universal positive cross-resistance among metals**

All tested metal pairs were positive [src: metal_cross_resistance]. The same source notes that no negative controls were included, so universal cross-resistance cannot be distinguished from a general-stress response [src: metal_cross_resistance]. The positive direction is therefore an observation whose attribution to metal-specific mechanisms is untested rather than refuted [src: metal_cross_resistance].

**Side 2: Shared cellular stress biology beyond metals**

The counter-ion study supports shared cellular stress biology [src: counter_ion_effects]. It reports 4,304/10,821 shared NaCl–metal records, meaning gene records important under both a metal and NaCl [src: counter_ion_effects]. Zinc sulfate had 44.6% overlap despite 0 mM chloride [src: counter_ion_effects]. This argues against chloride counter-ion carry-over as the explanation for the overlap and points instead to stress biology shared between metal and NaCl conditions [src: counter_ion_effects].

## Possible Reconciliations

- *Hypothesis:* The positive metal-pair signal is a mixture of two components. One is a shared-stress component also visible under NaCl. The other is a metal-specific component. Both sides would then be partly right, and the metal-specific share is unknown.
- *Hypothesis:* The universal positivity is largely a general-stress artifact. It would then shrink or vanish once genes shared with NaCl are removed.
- *Hypothesis:* Metal-specific cross-resistance is real and survives stress controls. The shared NaCl–metal records would then reflect a separate, parallel vulnerability layer rather than the cross-resistance signal itself.

None of these is established. The evidence above supports only the observations as stated.

## Resolving Work

- **Non-metal negative controls:** Use fitness profiles for non-metal stressors (osmotic, oxidative, antibiotic) in the same organisms. Compute metal–non-metal correlations with the same pipeline. Question: are metal–metal correlations stronger than metal–non-metal ones?
- **Stress-gene exclusion:** Take the shared NaCl–metal gene records from the counter-ion study. Recompute metal-pair correlations after excluding those genes. Question: does the universal positive direction persist on the metal-specific residual?
- **Partial correlation on a stress axis:** Build a general-stress fitness score from NaCl and other stress experiments. Fit partial correlations between metal pairs conditioned on that score. Question: how much of each metal-pair relationship is independent of general stress?
- **Counter-ion-matched contrasts:** Pair metals delivered as chloride versus non-chloride salts, such as zinc sulfate. Compare their overlap with NaCl-important genes and their pairwise metal correlations. Question: does counter-ion chemistry modulate cross-resistance beyond the shared-stress layer?
