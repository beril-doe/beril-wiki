<!-- tension-hash: a9245bd114de0b57 -->
# Metal-Tolerance Scores and Metal-Contaminated Isolation: A Positive Pangenome-Scale Effect Beside a Null Species-Scale Test

Two projects ask whether a genome-derived metal-tolerance score predicts that an organism was isolated from a metal-contaminated environment, and they report opposite answers. The isolation-environment analysis reports a strong heavy-metal association for the composite score (Cohen's *d*, the difference in means expressed in standard-deviation units, = +1.00), whereas the metal cross-resistance analysis reports no species-scale correlation with metal-associated isolation (Spearman rho, a rank-correlation statistic, approximately -0.02, p > 0.8). [src: bacdive_metal_validation] [src: metal_cross_resistance] The disagreement matters because the positive result is the main external validation offered for composite metal-tolerance scores, and the null result is the test that would license using those scores at species resolution. This conflict is inherited from [[concepts/composite-resistance-score-limitations]] and [[concepts/within-species-conservation-between-species-functional-divergence]].

## Evidence Sides

**Positive association at isolate and pangenome scale.** BacDive — a curated bacterial phenotype and isolation-metadata database — yielded Cohen's *d* = +1.00 for heavy-metal contamination in n=10 isolates, and a pangenome-scale Metal Fitness Atlas result of Cohen's *d* = +1.0 across 42K strains. [src: bacdive_metal_validation] This side's outcome is a group-contrast effect size between contamination-associated organisms and an environmental baseline, not a correlation.

**Null correlation at Fitness Browser species scale.** The cross-resistance study found no correlation between multi-metal tolerance scores and BacDive metal-environment isolation at Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8). [src: metal_cross_resistance] After matching and collapsing strains, it retained 20 independent species and judged the test underpowered. [src: metal_cross_resistance] The result stays a null with an explicit power caveat; it is not evidence of absence of association. These results do not establish whether the discrepancy reflects scale, matching, phenotype definition, or sampling. [src: metal_cross_resistance]

## Possible Reconciliations

- *Scale hypothesis*: the two analyses may measure the same underlying effect at incompatible resolutions, with the species-scale test having too few independent units to detect it. [src: metal_cross_resistance]
- *Matching hypothesis*: differences in how genomes were bridged to BacDive records may admit or exclude different organisms, so the two tests may not share a comparable denominator. [src: metal_cross_resistance]
- *Outcome-definition hypothesis*: a binary contamination-versus-baseline contrast and a continuous rank correlation against a multi-metal score may not be estimating the same quantity, so both could be correct as stated. [src: metal_cross_resistance]
- *Sampling hypothesis*: the organisms retained by each pipeline may differ in phylogenetic and environmental composition. [src: metal_cross_resistance]

The tension cannot be resolved from the available summaries because the analyses differ in matching, aggregation, and outcome definition. [src: metal_cross_resistance]

## Resolving Work

- Build a common strain-level bridge between genome-derived scores and BacDive isolation records, then re-run both the group contrast and the rank correlation on the identical matched set — do the two statistics still disagree on one denominator? [src: metal_cross_resistance]
- Preregister metal-specific outcome definitions before re-analysis, so effect direction and threshold are fixed in advance — does any single metal carry the composite association? [src: metal_cross_resistance]
- Report a power analysis for the species-scale test at its retained 20 independent species, asking what effect size it could have detected. [src: metal_cross_resistance]
- Repeat the heavy-metal contrast with more than the n=10 matched isolates to test whether Cohen's *d* = +1.00 is stable. [src: bacdive_metal_validation]
- Audit the 42K-strain pangenome-scale result for phylogenetic non-independence, asking how much of *d* = +1.0 survives clade-aware aggregation. [src: bacdive_metal_validation]
