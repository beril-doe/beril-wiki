<!-- tension-hash: 1ce33d4df91ec246 -->
# How Large Is the Overlap Between Metal-Fitness and Osmotic-Stress Genes?

Two analyses in the corpus measure how many metal-important genes are also important under salt or osmotic stress, and they report different overlap fractions [src: counter_ion_effects] [src: metal_specificity]. The difference matters because shared-stress genes could inflate the apparent core-genome enrichment of metal fitness genes, a claim tied to [[concepts/gene-essentiality]].

## Evidence Sides

**Side A: counter-ion analysis (larger overlap)**

The counter-ion analysis found 39.8% overlap between metal-important and NaCl-stress genes [src: counter_ion_effects]. NaCl is sodium chloride, used here as a general salt/ionic stress. Despite this large overlap, removing the shared-stress genes preserved core enrichment for 12 of 14 metals [src: counter_ion_effects]. It also preserved the original conclusion: 87.4% of metal-important genes are core, with OR=2.08 [src: counter_ion_effects]. OR is an odds ratio, the odds of being core among metal-important genes relative to the odds among the comparison set.

**Side B: separate metal-specificity analysis (smaller overlap)**

A separate analysis found 14.7% of metal-important genes sick under osmotic stress [src: metal_specificity]. "Sick" means a gene's mutants show reduced fitness under that condition. The tension text attributes the 2.7× discrepancy between the two estimates to stricter thresholds and different organism sets [src: counter_ion_effects] [src: metal_specificity].

The two figures rest on different thresholds and different organism sets [src: counter_ion_effects] [src: metal_specificity]. Neither figure should be treated as the corrected value of the other.

## Possible Reconciliations

- **Hypothesis 1: threshold stringency.** The stricter threshold in the separate analysis may exclude weaker fitness defects that the counter-ion analysis's threshold would count as shared stress. On this hypothesis, both figures are valid estimates of differently defined quantities.
- **Hypothesis 2: organism composition.** The two analyses cover different organism sets [src: counter_ion_effects] [src: metal_specificity]. Organisms with unusually high or low shared-stress fractions could shift either pooled estimate.
- **Hypothesis 3: condition definition.** "NaCl stress" and "osmotic stress" may not denote the same set of experiments in both projects. If they differ, the overlap is being measured against different stress panels.

## Resolving Work

- Re-run the separate analysis's overlap calculation using exactly the counter-ion analysis's threshold, on the same fitness data. This asks whether threshold stringency alone accounts for the 2.7× gap.
- Restrict both analyses to their shared organism set and recompute both overlap fractions. This asks whether organism composition, rather than method, drives the difference.
- Compute per-organism overlap under each threshold and test for outlier organisms with a leave-one-organism-out analysis. This asks whether any single organism dominates either pooled estimate.
- Tabulate the stress experiments counted as "NaCl" versus "osmotic" in each project and recompute overlap on a harmonized condition list. This asks whether condition definitions differ.
- Repeat the core-enrichment test, including the odds ratio, after removing shared-stress genes defined under each threshold. This asks whether the core conclusion is robust across both overlap definitions.
