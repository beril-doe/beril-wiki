<!-- tension-hash: bc62c0e9aeb9992e -->
# Marker Definitions and Statistical Context Change Functional Conclusions

The disagreement concerns when an apparent ecological signal should be treated as a biological difference, a marker-definition artifact, a conditional statistical effect, or merely a prioritization hypothesis. Across [[concepts/functional-marker-validation]], [[concepts/soil-metal-functional-genomics]], and [[concepts/functional-dark-matter]], the central issue is whether changed detectors, conditioning choices, terminology, and annotation depth alter the claim itself or only refine its interpretation.

## Evidence Sides

**Original versus corrected iron-reduction signal**

The original analysis supported a shallow-enrichment narrative for iron reduction, whereas the corrected detector found no significant deep-versus-shallow, deep-versus-baseline, or shallow-versus-baseline difference. [src: bacillota_b_subsurface_accessory] The disagreement is attributable to marker definition: K07811, K17324, and K17323 were replaced by PFAM and motif-based signals, and the resulting cohort counts and tests changed. [src: bacillota_b_subsurface_accessory] The correction is considered robust for the multi-heme cytochrome signal but remains a Phase 1 correction that does not fully determine whether the original clay-project comparison with the Bagnoud porewater pattern should be retained. [src: bacillota_b_subsurface_accessory]

**Terminology and retained sulfate-related signal**

The existing source describes the retained signal as “sulfite reduction,” whereas the new clay report describes it as dissimilatory “sulfate reduction”; both report 5/9 positives and the same null scale, but the terminology is not identical. [src: bacillota_b_subsurface_accessory] [src: clay_confined_subsurface] Verification against the underlying marker definitions and source tables is required rather than treating the labels as interchangeable. [src: bacillota_b_subsurface_accessory]

**Conditional versus unconditional environmental effect**

The soil-metal report presents a conditional db-RDA result of R² = 0.799 and p = 0.005 with 999 permutations after conditioning on batch and project effects. [src: soil_metal_functional_genomics] The unconditional R² for metals alone was not reported and may be substantially lower. [src: soil_metal_functional_genomics] This refines what the conditional result can support: it describes residual variance after project accession was removed rather than necessarily total community COG variance. [src: soil_metal_functional_genomics]

**Annotation breadth versus functional certainty**

The analysis reports that 33,105 of 39,532 pangenome-linked dark genes received non-hypothetical Bakta descriptions, but treats pathway, domain, module, and environmental links as hypotheses requiring validation. [src: functional_dark_matter] Broader annotation improves candidate identification, but a database product description is not equivalent to a biologically specific ecological marker. [src: functional_dark_matter]

## Possible Reconciliations

- **Marker-definition hypothesis:** The shallow-enrichment result and the null corrected result could both be accurate for different marker sets, because replacing K07811, K17324, and K17323 changed cohort membership and tests.
- **Scope hypothesis:** The multi-heme cytochrome correction may be robust while the clay-project comparison with the Bagnoud porewater pattern remains unresolved.
- **Terminology hypothesis:** “Sulfite reduction” and dissimilatory “sulfate reduction” may refer to overlapping but non-identical marker definitions; matching source tables could determine whether the 5/9 positives are directly comparable.
- **Statistical-conditioning hypothesis:** R² = 0.799 may describe a strong residual metal effect without implying an equally large unconditional environmental effect.
- **Evidence-level hypothesis:** Non-hypothetical annotation may prioritize candidates without establishing ecological function.

## Resolving Work

- Re-run the iron-reduction comparisons using both the original K07811, K17324, and K17323 markers and the PFAM/motif-based detector, with identical cohorts and tests, to determine which result follows from marker choice.
- Compare the underlying marker definitions and source tables for the “sulfite reduction” and dissimilatory “sulfate reduction” signals, including whether the same 5/9 samples are positive.
- Report unconditional and conditional db-RDA models with the same permutations, batch/project terms, and variance partitions to quantify how much of the metal-associated effect remains after conditioning.
- Reanalyze the 2,355 discoveries among 3,915 implied tests under dependence-aware FDR procedures and assess whether co-contamination changes the discovery rate.
- Experimentally validate prioritized dark-gene candidates with domain, pathway, and environmental evidence to test whether annotation predictions correspond to biologically specific markers.
