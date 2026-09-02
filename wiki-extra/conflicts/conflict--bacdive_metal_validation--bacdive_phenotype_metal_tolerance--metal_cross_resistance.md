<!-- tension-hash: 081d42e873f51cb3 -->
# BacDive coverage and metal-resistance estimates are not interchangeable

The [[concepts/composite-resistance-score-limitations]] page records several disagreements among analyses that appear to address related questions but use different matching, aggregation, outcome, gene-set, and threshold definitions. These tensions matter because the reported coverage, metal association, stress overlap, and core-enrichment estimates cannot be compared or averaged without first determining whether they measure the same populations and constructs.

## Evidence Sides

**Species-level bridge coverage.** The phenotype analysis reports 37,368 matched strains across 5,647 GTDB species, whereas the isolation-environment analysis reports 42,227 matched strains across 6,426 GTDB species. [src: bacdive_phenotype_metal_tolerance] [src: bacdive_metal_validation] The difference may reflect different matching or filtering pipelines, so the coverage estimates should not yet be treated as interchangeable.

**Composite-score association with metal-associated isolation.** The isolation-environment analysis reports a strong heavy-metal association for the composite score (Cohen’s d = +1.00). [src: bacdive_metal_validation]

**Species-scale correlation with metal-associated isolation.** The metal cross-resistance analysis reports no species-scale correlation with metal-associated isolation (Spearman rho approximately -0.02, p > 0.8). [src: metal_cross_resistance] The summaries cannot resolve this tension because the analyses differ in matching, aggregation, and outcome definition. [src: metal_cross_resistance]

**Metal–osmotic-stress overlap.** Metal-important genes overlapped with NaCl-stress genes at 39.8% in the counter-ion analysis, whereas 14.7% were sick under osmotic stress in the metal-specificity analysis. [src: metal_specificity] The difference was attributed to stricter fitness and statistical thresholds and partially different organism sets; the directional agreement supports overlap between metal and osmotic stress while showing that composite or thresholded scores are sensitive to operational definitions. [src: metal_specificity]

**Genome-wide core-enrichment estimates.** The atlas reports an 87.4% core fraction for broad metal-important genes. [src: metal_fitness_atlas] This is not directly interchangeable with the 84.8% pooled core fraction for metal-specific genes or the 92.0%/91.0%/89.8% tiers in the cross-resistance analysis because the sources use different gene sets and definitions. [src: metal_specificity] [src: metal_cross_resistance]

## Possible Reconciliations

- **Hypothesis — pipeline scope:** The two BacDive totals could differ because matching, strain inclusion, species assignment, or filtering was performed differently.
- **Hypothesis — estimand mismatch:** Cohen’s d and species-level Spearman rho may describe different aggregation levels or outcome definitions, allowing a strong group contrast and a near-zero species-scale correlation to coexist.
- **Hypothesis — threshold and cohort effects:** The 39.8% and 14.7% overlap estimates may differ because of stricter fitness and statistical thresholds and partially different organism sets.
- **Hypothesis — gene-set definitions:** The 87.4%, 84.8%, and 92.0%/91.0%/89.8% core fractions may converge after applying the same locus set, conservation definition, specificity threshold, and non-metal controls.

## Resolving Work

- Re-run both BacDive analyses from the same strain-level bridge table; apply identical matching, GTDB assignment, and filtering; test whether the totals converge.
- Analyze the same bridged strains with preregistered metal-specific outcomes; compare Cohen’s d and Spearman rho under matched aggregation to determine whether the association is scale-dependent.
- Recalculate metal–NaCl overlap on one organism set using both published fitness/statistical thresholds; quantify how much each threshold changes the estimate.
- Apply one locus set, conservation rule, metal-specificity threshold, and non-metal control set to all three core-enrichment analyses; test whether the reported fractions remain different.
