<!-- tension-hash: b75f9138f9cf3618 -->
# Do Metal Conservation Estimates Differ Because of Method or Because of Biology?

The counter-ion analysis and the primary metal fitness atlas report different per-metal conservation estimates for manganese, zinc and iron [src: counter_ion_effects, metal_fitness_atlas]. A counter ion is the partner ion supplied alongside a metal in its salt. The disagreement matters for the framework in [[concepts/shared-stress-versus-stressor-specific-fitness]], which separates a shared cellular-stress component from metal-specific requirements before mechanistic interpretation [src: counter_ion_effects]. The discrepancy is already present in the uncorrected values, before any shared-stress treatment, so the correction step alone cannot explain it [src: counter_ion_effects, metal_fitness_atlas].

## Evidence Sides

**Counter-ion analysis (corrected and uncorrected values)**

The counter-ion analysis applies a shared-stress correction, which removes genes that respond to stress in general so that metal-specific genes remain. After this correction it reports manganese at +0.182, zinc at +0.115 and iron at +0.182 [src: counter_ion_effects]. Its own uncorrected values were manganese +0.182, zinc +0.145 and iron -0.040 [src: counter_ion_effects]. Within this analysis, the correction left manganese unchanged, lowered zinc, and changed the sign of iron from negative to positive [src: counter_ion_effects].

**Primary metal fitness atlas (uncorrected values)**

The primary atlas reports original, uncorrected estimates of manganese +0.198, zinc +0.151 and iron +0.116 [src: metal_fitness_atlas]. These values were not subjected to the counter-ion analysis's shared-stress correction [src: metal_fitness_atlas].

**Where the sides diverge**

Comparing the uncorrected values from the two analyses, the discrepancy is present even before any shared-stress treatment [src: counter_ion_effects, metal_fitness_atlas]. The largest qualitative difference is iron. It is negative in the counter-ion analysis's uncorrected value (-0.040) and positive in the atlas's (+0.116) [src: counter_ion_effects, metal_fitness_atlas]. The values should not be reconciled by averaging. The analyses differ in record sets, organism coverage and procedure [src: counter_ion_effects, metal_fitness_atlas].

## Possible Reconciliations

- **Hypothesis A (records):** The analyses differ in record sets [src: counter_ion_effects, metal_fitness_atlas]. If so, the uncorrected discrepancy may reflect which records were included rather than biology. This is untested.
- **Hypothesis B (coverage):** The analyses differ in organism coverage [src: counter_ion_effects, metal_fitness_atlas]. Different contributing organisms could shift per-metal estimates. This is untested.
- **Hypothesis C (procedural):** The analyses differ in procedure [src: counter_ion_effects, metal_fitness_atlas]. How each defines gene sets or computes the estimate could produce the gap independently of the shared-stress correction. This is untested.
- **Hypothesis D (biological):** The discrepancy could reflect a real biological difference that one record set captures and the other does not [src: counter_ion_effects, metal_fitness_atlas]. This is untested.

None of these is established. Matched-data reanalysis is required to decide whether the discrepancy is methodological or biological [src: counter_ion_effects, metal_fitness_atlas].

## Resolving Work

- **Matched records:** Recompute uncorrected manganese, zinc and iron estimates using one identical gene–condition record set and the same procedure. Does the uncorrected discrepancy persist when the inputs are matched?
- **Organism coverage:** Restrict both pipelines to the organisms they share for each metal, then recompute the iron estimate. Does the sign difference between the uncorrected iron values disappear?
- **Procedure:** Run the atlas procedure and the counter-ion procedure in turn on each analysis's own records, swapping one at a time. Is the gap driven by the procedure or by the records?
- **Correction:** Apply the shared-stress correction to the atlas's records under the matched setup. Does iron show the same negative-to-positive shift that the counter-ion analysis reports?
