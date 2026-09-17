<!-- tension-hash: 2d1b0ad4ef2f5576 -->
# Conflict: Is Universal Metal Cross-Resistance Specific Biology or a General Stress Response?

Two projects in this corpus report overlapping fitness signals across stresses and disagree about what the overlap means. The metal cross-resistance work reports that all tested metal pairs were positive, but that no negative controls were included — no stressor expected *not* to share genes with metals — so universal cross-resistance cannot be distinguished from a general-stress response that any harsh condition would produce. [src: metal_cross_resistance] The counter-ion study measures a different overlap: it supports shared cellular stress biology and reports 4,304/10,821 shared NaCl–metal records (genes important under a metal that are also important under sodium chloride osmotic/ionic stress), including 44.6% overlap for zinc sulfate despite 0 mM chloride. [src: counter_ion_effects] Whether that second result bears on the first project's missing control is itself part of the dispute. The stakes are interpretive: it determines whether the cofitness structure — the correlation of gene fitness profiles across conditions — described in [[concepts/cofitness-network-architecture]] is metal-specific wiring or a general-vulnerability backbone visible through any lens.

## Evidence Sides

**Side A — the cross-resistance signal is real and universal, but uncontrolled.** All tested metal pairs were positive; no pair reversed sign. The project itself flags the gap: because no negative controls were included, universal cross-resistance cannot be distinguished from a general-stress response. [src: metal_cross_resistance] This side's claim is not that the general-stress explanation is wrong — it is that the design cannot exclude it, so the positive result stands undiscriminated rather than refuted.

**Side B — much of the shared signal is shared stress biology, not counter-ion artifact.** The counter-ion study supports shared cellular stress biology and reports 4,304/10,821 shared NaCl–metal records. Its discriminating observation is a null on the counter-ion hypothesis: zinc sulfate had 44.6% overlap despite 0 mM chloride, so chloride delivered by the metal salt does not explain the overlap. [src: counter_ion_effects] Note this null rules out the *counter-ion* explanation, not the metal-specific one.

## Possible Reconciliations

- *Hypothesis 1 (two-layer signal):* both are right at different layers — a general-stress layer shared with NaCl plus a metal-specific layer on top — and the uncontrolled design of Side A sums the two into one positive correlation.
- *Hypothesis 2 (control asymmetry):* NaCl is itself an ionic stress and so is an unusually permissive "negative control"; a chemically unrelated stressor might show much less overlap, leaving cross-resistance more specific than Side B implies.
- *Hypothesis 3 (denominator mismatch):* the two projects count different objects — pairwise gene-level correlations versus gene-record overlaps — so their conclusions may not be commensurable rather than contradictory.

## Resolving Work

- Re-run the metal-pair correlation analysis with explicitly non-metal, non-ionic stressors (e.g. antibiotic, temperature, carbon-source shift) as declared negative controls, asking whether metal–metal correlations exceed metal–control correlations.
- Partition metal fitness profiles into NaCl-shared and NaCl-non-shared gene sets, recompute metal-pair correlations on each partition, and ask whether positivity survives removal of the shared-stress layer.
- Repeat the sulfate-versus-chloride contrast for additional sulfate salts to test whether the 0 mM chloride result at 44.6% generalizes beyond zinc. [src: counter_ion_effects]
- Reconcile denominators by recomputing both projects' statistics on the intersection of their organisms and metals, asking whether the disagreement is biological or definitional.
