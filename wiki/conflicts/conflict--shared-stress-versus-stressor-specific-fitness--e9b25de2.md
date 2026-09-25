<!-- tension-hash: e9b25de212b4084e -->
# Manganese, Zinc and Iron Conservation Estimates Disagree Between the Counter-Ion Analysis and the Primary Metal Fitness Atlas

Two projects in this corpus report per-metal conservation estimates — the enrichment of metal fitness genes in the core genome, expressed as a delta above a baseline core fraction — for the same three metals, and the numbers do not match. The disagreement matters because these deltas are the quantitative basis for the claim that metal fitness genes are conserved, and because the two analyses sit on opposite sides of the shared-stress correction question developed in [[concepts/shared-stress-versus-stressor-specific-fitness]]: whether a fitness signal reflects a general cellular stress response or a metal-specific requirement. If the gap is methodological, the conservation claim survives with a wider error bar; if it is biological, the per-metal ranking that downstream interpretation rests on is unstable.

## Evidence Sides

**Counter-ion analysis (shared-stress-corrected estimates).** After shared-stress treatment, the counter-ion analysis reports manganese at +0.182, zinc at +0.115, and iron at +0.182. [src: counter_ion_effects] Under these values, manganese and iron are tied at the top of the three, and zinc sits distinctly below both.

**Primary metal fitness atlas.** For the same three metals the primary atlas reports manganese at +0.198, zinc at +0.151, and iron at +0.116. [src: metal_fitness_atlas] Here the ordering is manganese, then zinc, then iron — iron falls to the bottom of the three rather than tying for the top, and both manganese and zinc are estimated higher than in the counter-ion analysis.

The two sets therefore disagree in magnitude for all three metals and in direction of the iron-versus-zinc comparison. These values should not be reconciled by averaging, because the analyses differ in record sets, organism coverage, and correction procedure. [src: counter_ion_effects, metal_fitness_atlas]

## Possible Reconciliations

- *Hypothesis: the gap is a record-set artifact.* The two analyses may draw on different sets of fitness records, so the deltas are estimated over non-identical gene pools and are not directly comparable. [src: counter_ion_effects, metal_fitness_atlas]
- *Hypothesis: the gap is an organism-coverage artifact.* Differing organism coverage per metal could shift a per-metal delta without any underlying biological difference, particularly for metals carried by few organisms. [src: counter_ion_effects, metal_fitness_atlas]
- *Hypothesis: the gap is produced by the correction procedure itself.* Removing shared-stress genes could move a metal's delta up or down depending on how much of that metal's signal is shared-stress, which would make the discrepancy an intended consequence of correction rather than an error. [src: counter_ion_effects]

None of these is established; the sources state only that matched-data reanalysis is required to determine whether the discrepancy is methodological or biological. [src: counter_ion_effects, metal_fitness_atlas]

## Resolving Work

- Take the intersection of the two projects' fitness record sets and recompute manganese, zinc and iron deltas on that matched set under each project's procedure: does the gap close when the records are identical?
- Recompute each metal's delta restricted to organisms present in both analyses, reporting per-metal organism counts alongside the delta: is the disagreement driven by coverage rather than by correction?
- Run the counter-ion shared-stress correction on the atlas's own record set and report the before/after delta for each of the three metals: does correction alone reproduce the observed shifts?
- Report a confidence interval or resampling spread for each per-metal delta on both sides: do the two estimates for iron actually exclude each other, or is the apparent reversal within noise?
- For iron specifically, where the two sides disagree most in rank, audit which genes enter each analysis and which are removed as shared-stress: is the reversal attributable to an identifiable gene set?
