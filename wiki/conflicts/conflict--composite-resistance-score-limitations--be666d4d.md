<!-- tension-hash: be666d4d32f74d67 -->
# Heavy-Metal Isolation and Composite Metal-Tolerance Scores: A Positive Contamination Contrast Versus a Null Species-Scale Test

Two projects disagree on whether genome-derived composite metal-tolerance scores track isolation from metal-contaminated environments. The isolation-environment analysis reports a strong heavy-metal association (Cohen's d = +1.00, a standardized mean difference). [src: bacdive_metal_validation] The metal cross-resistance analysis reports no species-scale correlation with metal-associated isolation (Spearman rho, a rank correlation coefficient, approximately -0.02; p, the probability of a result this extreme under no association, > 0.8). [src: metal_cross_resistance] This matters because the tension cannot be resolved from the available summaries: the analyses differ in matching, aggregation, and outcome definition. [src: metal_cross_resistance] The question bears on [[concepts/composite-resistance-score-limitations]] and on [[concepts/within-species-conservation-between-species-functional-divergence]].

## Evidence Sides

**Positive association: isolation-environment analysis**

BacDive (a bacterial strain phenotype and isolation-source database) found Cohen's d = +1.00 for heavy-metal contamination. The comparison was n=10 isolates against approximately 5,000 environmental-baseline strains. [src: bacdive_metal_validation] The effect therefore rests on a single comparison with 10 heavy-metal isolates. [src: bacdive_metal_validation]

The cross-resistance report describes this prior project as a pangenome-scale analysis (a pangenome being the combined gene content across strains of a species) (42K strains, Cohen's d = +1.0). [src: metal_cross_resistance] The 42K figure reflects the scale of the matched-strain bridge, not the denominator of the effect size. It is therefore not a separate validation result. [src: bacdive_metal_validation, metal_cross_resistance]

**Null result: metal cross-resistance analysis**

The cross-resistance study tested multi-metal tolerance scores against BacDive metal-environment isolation at Fitness Browser species scale. The Fitness Browser is a collection of genome-wide mutant fitness data. The study found no correlation (Spearman rho approximately -0.02, p > 0.8). [src: metal_cross_resistance] After matching and collapsing strains, it retained 20 independent species and judged the test underpowered. [src: metal_cross_resistance] It is thus a null result from a test its authors judged underpowered, not evidence of absence. [src: metal_cross_resistance]

## Possible Reconciliations

- **Hypothesis (aggregation scale):** an association among individual isolates may not survive collapsing to species. The two analyses differ in aggregation. [src: metal_cross_resistance]
- **Hypothesis (matching):** the two studies use different matching procedures. They may therefore be comparing different organism sets. [src: metal_cross_resistance]
- **Hypothesis (outcome definition):** the analyses differ in outcome definition, so contrasting heavy-metal-contamination isolates with a baseline and correlating multi-metal tolerance scores with metal-environment isolation may not test the same phenotype. [src: metal_cross_resistance]
- **Hypothesis (sampling/power):** the null result may reflect the 20-species sample rather than a true absence of association. [src: metal_cross_resistance]

The source states that the available results do not establish which of scale, matching, phenotype definition, or sampling explains the discrepancy. [src: metal_cross_resistance]

## Resolving Work

- **Common strain-level bridge:** match BacDive isolates to scored genomes with one shared strain-level procedure. Then re-run both the contamination contrast and the rank correlation on the same matched set. The question is whether the two results converge once matching is held constant.
- **Preregistered metal-specific outcomes:** use BacDive isolation records together with Fitness Browser metal fitness data. Define outcomes for each metal before testing, then compare against the composite score. The question is whether the association is driven by particular metals or by general stress tolerance.
- **Aggregation sensitivity:** on the matched data, compute the effect at strain level and again after species collapsing. The question is whether collapsing alone removes the signal.
- **Power analysis for the species-scale test:** for the Fitness Browser species set, estimate the number of independent species needed to detect a correlation of plausible size. The question is whether the 20-species null can rule anything out.
