<!-- tension-hash: 1ce33d4df91ec246 -->
# How Much of the Metal-Fitness Signal Is Shared Stress? Two Overlap Estimates, 39.8% Versus 14.7%

Two projects in this corpus measured the same thing — the fraction of genes important for metal fitness that are also important under ionic/osmotic stress — and got answers a factor of 2.7 apart [src: metal_specificity]. The counter-ion analysis reports 39.8% overlap between metal-important and NaCl-stress genes [src: counter_ion_effects]; a separate metal-specificity analysis reports 14.7% of metal-important genes sick under osmotic stress [src: metal_specificity]. The disagreement matters because the overlap fraction sets how much of the "metal fitness" atlas is metal biology rather than generic cellular vulnerability, and therefore how much of the downstream essentiality reasoning in [[concepts/gene-essentiality]] rests on condition-specific signal. Both sides agree the overlap is substantial and in the same direction; they disagree on its magnitude, and the two magnitudes license different interpretive claims.

## Evidence Sides

**Large overlap, atlas conclusions intact — the counter-ion analysis.** This side found 39.8% overlap between metal-important and NaCl-stress genes [src: counter_ion_effects]. It then tested whether that overlap undermines the metal atlas by removing shared-stress genes, and found that core enrichment was preserved for 12 of 14 metals, retaining the original 87.4% core fraction and the OR=2.08 conclusion (OR = odds ratio, the ratio of odds of being core-genome-encoded in metal-important versus comparison genes) [src: counter_ion_effects]. On this side the overlap is large but not corrosive: a big shared-stress component coexists with robust metal-specific core enrichment.

**Smaller overlap under stricter criteria — the metal-specificity analysis.** This side found 14.7% of metal-important genes sick under osmotic stress [src: metal_specificity]. It also identified the source of the gap rather than disputing the other estimate: the 2.7× discrepancy reflects stricter thresholds and different organism sets [src: metal_specificity]. Note this is a stricter-threshold estimate, not a null result — neither side reports an absence of overlap.

## Possible Reconciliations

- **Threshold hypothesis.** A stricter sickness threshold admits fewer genes to the "also stressed" set, so the two percentages may be two points on one monotonic threshold curve rather than two incompatible facts [src: metal_specificity].
- **Denominator/organism-set hypothesis.** Because the organism sets differ partially, the two percentages may share a numerator definition but not a denominator, making them non-comparable as stated [src: metal_specificity].
- **Compatibility hypothesis.** Both estimates may be correct and jointly consistent with the atlas surviving correction, since removing shared-stress genes preserved core enrichment for 12 of 14 metals and the 87.4% core, OR=2.08 conclusion [src: counter_ion_effects].

## Resolving Work

- Re-run the metal-specificity overlap calculation using the counter-ion analysis's exact threshold on its exact organism set: does the estimate converge on 39.8%, and if not, what residual explains the gap?
- Sweep the sickness threshold across its range on a single fixed organism set and plot overlap versus stringency: is the 39.8%/14.7% pair reproducible as two points on one curve?
- Intersect the two organism sets and report overlap on the intersection only: how much of the 2.7× discrepancy is organism composition rather than threshold?
- Repeat the shared-stress-removal test under the stricter threshold: do core enrichment and the OR=2.08 conclusion still hold for 12 of 14 metals?
- Report per-metal overlap under both methodologies side by side: are the 2 of 14 metals that lose enrichment the same under each threshold?
