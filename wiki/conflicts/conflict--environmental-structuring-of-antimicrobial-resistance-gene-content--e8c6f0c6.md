<!-- tension-hash: e8c6f0c62f74ebd2 -->
# Clinical Versus Environmental AMR Content: Two Reports, Two Scales of Difference

Two projects ask whether a species' isolation environment predicts how many antimicrobial-resistance (AMR) gene clusters it carries. Both find that clinical species carry more than soil, aquatic or other classes, but they report different absolute levels and slightly different ratios. The first gives medians of 5 (clinical) versus 2 (soil, aquatic and host-associated), with a ratio of 2.5×. [src: amr_environmental_resistome] The second gives 10.6 clusters per species for Human/Clinical versus 3.0–4.6 for the other classes, with a ratio of 2.7×. [src: amr_pangenome_atlas] The statistics differ in kind (a median versus per-species figures), so they must not be merged. The question matters because the size of the environmental effect shapes how strongly niche can be used to predict resistance. The concept page is [[concepts/environmental-structuring-of-antimicrobial-resistance-gene-content]].

## Evidence Sides

**Side A: amr_environmental_resistome (medians)**
- The medians are 5 for clinical species versus 2 for soil, aquatic and host-associated species. [src: amr_environmental_resistome]
- The reported ratio is 2.5×. [src: amr_environmental_resistome]
- Direction: clinical is higher. The figure is a median, not a per-species figure.

**Side B: amr_pangenome_atlas (per-species figures)**
- Human/Clinical species carry 10.6 clusters per species, versus 3.0–4.6 for the other classes. [src: amr_pangenome_atlas]
- The reported ratio is 2.7×. [src: amr_pangenome_atlas]
- Direction: clinical is higher. The figures are per-species, not medians.

Both sides agree on direction. They differ in absolute level and in ratio: 2.5× [src: amr_environmental_resistome] and 2.7× [src: amr_pangenome_atlas]. Neither ratio is averaged with the other, and neither is preferred.

## Possible Reconciliations

- **Hypothesis: the summary statistic explains the gap.** A median of 5 and a per-species figure of 10.6 may differ because the two statistics respond differently to a skewed distribution. This is untested.
- **Hypothesis: the environment classes are defined differently.** The comparison groups are "soil, aquatic and host-associated" in one report and "the other classes" in the other. Different groupings could move both the levels and the ratios. This is untested.
- **Hypothesis: the two ratios are compatible once the denominators match.** The 2.5× and 2.7× figures may come from different baselines. This cannot be confirmed from the tension text alone.

## Resolving Work

- **Data:** the per-species AMR cluster counts behind both reports. **Method:** compute the median and the per-species figure for each environment class on one shared table. **Question:** do both statistics give the same ordering and similar ratios?
- **Data:** the environment labels used by each project. **Method:** cross-tabulate the labels species by species. **Question:** do the "soil, aquatic and host-associated" and "other classes" groupings contain the same species?
- **Data:** the clinical and non-clinical comparison sets. **Method:** recompute the ratio with identical numerator and denominator definitions, using a bootstrap (resampling) interval. **Question:** is the gap between the two ratios larger than sampling noise?
- **Data:** the species sets analysed by each project. **Method:** restrict both analyses to the species they share. **Question:** does the difference in absolute level persist on identical species?
- **Data:** the AMR cluster definitions used by each project. **Method:** compare the detection and clustering criteria. **Question:** does the unit "cluster" mean the same thing in both reports?
