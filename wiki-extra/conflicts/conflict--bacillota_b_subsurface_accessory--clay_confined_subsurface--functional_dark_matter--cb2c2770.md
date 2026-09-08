---
title: Functional Markers, Statistical Conditioning, and Ecological Certainty
type: Conflict
sources:
- id: bacillota_b_subsurface_accessory
  resource: ../../wiki/summaries/bacillota_b_subsurface_accessory__REPORT.md
  title: bacillota b subsurface accessory
- id: clay_confined_subsurface
  resource: ../../wiki/summaries/clay_confined_subsurface__REPORT.md
  title: clay confined subsurface
- id: soil_metal_functional_genomics
  resource: ../../wiki/summaries/soil_metal_functional_genomics__REPORT.md
  title: soil metal functional genomics
- id: functional_dark_matter
  resource: ../../wiki/summaries/functional_dark_matter__REPORT.md
  title: functional dark matter
---
<!-- tension-hash: 0de05df7526c08a8 -->
# Functional Markers, Statistical Conditioning, and Ecological Certainty

The disagreement concerns how strongly functional-genomic signals support ecological interpretations. Differences in marker definitions changed the iron-reduction result, terminology may conceal non-identical sulfate-related signals, conditioning changed the interpretation of environmental variance, and broad annotation expanded candidate discovery without establishing functional certainty. These issues matter because apparently conflicting conclusions may reflect different operational definitions, statistical targets, or evidentiary standards rather than a single biological disagreement across [functional-marker-validation](../../wiki/concepts/functional-marker-validation.md).

## Evidence Sides

**Original and retained functional-signal interpretations.** The original analysis supported a shallow-enrichment narrative for iron reduction, whereas the corrected detector found no significant deep-versus-shallow, deep-versus-baseline, or shallow-versus-baseline difference. [^bacillota_b_subsurface_accessory] The existing source describes the retained signal as “sulfite reduction,” whereas the new clay report describes it as dissimilatory “sulfate reduction”; both report 5/9 positives and the same null scale, but the terminology is not identical. [^bacillota_b_subsurface_accessory] [^clay_confined_subsurface] The soil-metal report also presents a strong conditional association: conditioning on batch and project effects produced R² = 0.799 and p = 0.005 with 999 permutations. [^soil_metal_functional_genomics]

**Corrected, conditioned, and validation-focused interpretation.** The disagreement is attributable to marker definition rather than to silently reconciling numerical results: K07811, K17324, and K17323 were replaced by PFAM and motif-based signals, and the resulting cohort counts and tests changed. [^bacillota_b_subsurface_accessory] The correction is considered robust for the multi-heme cytochrome signal but remains a Phase 1 correction that does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained. [^bacillota_b_subsurface_accessory] The unconditional R² for metals alone was not reported and may be substantially lower. [^soil_metal_functional_genomics] Likewise, the 2,355 discoveries among 3,915 implied tests represent a 60% discovery rate, but co-contamination may make tests non-independent and the true FDR may be higher than reported. [^soil_metal_functional_genomics] Finally, 33,105 of 39,532 pangenome-linked dark genes received non-hypothetical Bakta descriptions, but pathway, domain, module, and environmental links remain hypotheses requiring validation. [^functional_dark_matter]

## Possible Reconciliations

- **Marker-definition hypothesis:** The original shallow-enrichment result and the corrected null results could differ because K07811, K17324, and K17323 measured a different biological proxy from the PFAM and motif-based signals.
- **Terminology hypothesis:** “Sulfite reduction” and dissimilatory “sulfate reduction” may refer to overlapping but non-identical marker sets; the shared 5/9 positives and same null scale do not establish equivalence.
- **Conditioning hypothesis:** R² = 0.799 may describe residual variance after batch and project effects were removed, while the unreported unconditional effect could be lower.
- **Annotation-certainty hypothesis:** Non-hypothetical Bakta descriptions may improve prioritization without demonstrating a biologically specific ecological marker.

## Resolving Work

- Recompute every cohort count and deep-versus-shallow, deep-versus-baseline, and shallow-versus-baseline test using both marker definitions; ask whether the conclusion changes solely because of marker membership.
- Compare the underlying source tables and marker definitions for “sulfite reduction” and dissimilatory “sulfate reduction”; ask whether the 5/9 positives are the same samples and genes.
- Report conditional and unconditional db-RDA models with permutation procedures and variance partitioning; ask how much metal-associated variation remains after batch and project effects are removed.
- Reanalyze the 3,915 implied tests with dependence-aware FDR or grouped permutations; ask whether the 2,355 discoveries remain credible under co-contamination.
- Experimentally validate prioritized dark genes with domain, pathway, expression, or biochemical assays; ask whether Bakta descriptions predict actual ecological function.

[^bacillota_b_subsurface_accessory]: [bacillota b subsurface accessory](../../wiki/summaries/bacillota_b_subsurface_accessory__REPORT.md)
[^clay_confined_subsurface]: [clay confined subsurface](../../wiki/summaries/clay_confined_subsurface__REPORT.md)
[^soil_metal_functional_genomics]: [soil metal functional genomics](../../wiki/summaries/soil_metal_functional_genomics__REPORT.md)
[^functional_dark_matter]: [functional dark matter](../../wiki/summaries/functional_dark_matter__REPORT.md)
