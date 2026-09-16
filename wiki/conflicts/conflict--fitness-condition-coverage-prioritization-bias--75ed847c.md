<!-- tension-hash: 75ed847cdb0efff1 -->
# Does Deep Condition Profiling Inflate Specific Phenotypes, Pleiotropic Phenotypes, or Neither?

Projects in this corpus disagree about which way deep condition profiling biases fitness-based gene prioritization. Deep profiling here means testing an organism across many experimental conditions. One project reads deep coverage as a source of more condition-specific top candidates [src: functional_dark_matter]. Another reads it as a source of more pleiotropic calls, where pleiotropic means a gene affects fitness across many unrelated conditions [src: metal_specificity]. A third result shows that a large block of off-target experiments did not erase specificity [src: discoveries]. This matters for [[concepts/fitness-condition-coverage-prioritization-bias]], because the direction of that bias remains unresolved.

## Evidence Sides

**Side A: deep coverage inflates condition-specific candidates.** One report attributes MR-1's 25/100 top candidates to its 121 conditions [src: functional_dark_matter]. On this reading, more conditions give a gene more chances to show a specific phenotype, and that raises its priority.

**Side B: deep coverage inflates pleiotropic calls.** Another report attributes the lower metal-specific fraction among novel families (45.6% versus 58.2%) to deep profiling raising pleiotropic calls [src: metal_specificity]. On this reading, a high experiment count pushes genes away from a "metal-specific" label and toward a general-fitness-defect label.

**Side C: deep coverage did not abolish specificity.** The corrected DvH result shows that 608 non-metal experiments did not drive essential-metal specificity to zero [src: discoveries]. This result is not evidence for inflation in either direction. It shows only that large non-target coverage did not eliminate specific calls.

The tension text concludes that whether deep coverage inflates specific phenotypes, pleiotropic phenotypes, or neither depends on the scoring rule, and that no analysis here tests the three cases under a common threshold [src: functional_dark_matter, metal_specificity, discoveries].

## Possible Reconciliations

- *Hypothesis:* the sides use different scoring rules. A rule that rewards the strongest single-condition phenotype would favor deep coverage, which fits Side A. A rule that classifies a gene by the breadth of its phenotypes would penalize deep coverage, which fits Side B.
- *Hypothesis:* the effect depends on which conditions are added. Conditions unrelated to the target class may add specific hits in some organisms and pleiotropic hits in others. Side C would then be one organism where added non-target conditions did not eliminate specific calls, without indicating which effect, if any, dominated.
- *Hypothesis:* the attributions in Sides A and B are interpretations of composition, not tested causal effects. Coverage depth may be confounded with organism identity in both projects.

## Resolving Work

- **Common-threshold re-scoring.** Re-score MR-1, DvH and the other deeply profiled organisms in the Fitness Browser under one shared specificity threshold. Question: does depth move genes toward specific or pleiotropic calls once the rule is held fixed?
- **Condition subsampling.** Rarefy each deeply profiled organism's experiments to the depth of shallow organisms and recompute top-candidate membership and metal-specific fractions. Question: do MR-1's top-candidate count and the novel-family metal-specific fraction change with depth alone?
- **Matched comparison of novel and annotated families.** Compare novel and annotated families within the same organisms. Question: does the gap between 45.6% and 58.2% persist once organism depth is matched, or is it a composition effect?
- **Category-resolved depth effect.** Using the DvH experiments, separate metal and non-metal conditions and add them incrementally. Question: which condition categories, if any, shift essential-metal specificity, and in which direction?
