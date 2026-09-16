<!-- tension-hash: 081d42e873f51cb3 -->
# Composite metal-tolerance scores: four incompatible accountings

This page records four distinct disagreements that the concept page [[concepts/composite-resistance-score-limitations]] documents among projects that build genome-derived metal-tolerance scores and metal-important gene sets, and all four are covered here: (1) how many BacDive strains and GTDB species the pangenome bridge links; (2) whether the composite score is strongly associated with metal-contaminated isolation or shows no detectable association; (3) how much metal-important gene fitness overlaps counter-ion/osmotic stress; and (4) what fraction of metal-relevant genes is core. The disagreements are, on their face, about bridges, thresholds, and outcome definitions — the operational choices that turn genomes and fitness matrices into a single number — rather than about biology directly. The stakes are practical: if the coverage counts and effect sizes are not interchangeable, then no downstream page may pool them, and the composite score cannot yet be treated as a calibrated instrument. Definitions used below: a **pangenome** is the union of gene families observed across the genomes assigned to a species, partitioned into a **core** portion (families present in essentially all member genomes, under whatever presence threshold the analysis adopts) and an accessory portion; a **core fraction** is the share of a given gene set that falls in that core portion.

## Evidence Sides

### 1. How large is the BacDive → GTDB pangenome bridge?

**Side A — the phenotype analysis.** The phenotype analysis reports 37,368 matched strains across 5,647 GTDB species (GTDB = the Genome Taxonomy Database, the reference taxonomy in which the pangenome species are defined). [src: bacdive_phenotype_metal_tolerance]

**Side B — the isolation-environment analysis.** The isolation-environment analysis reports 42,227 matched strains across 6,426 GTDB species. [src: bacdive_metal_validation]

The two reported species-level bridge totals are not the same. The concept page records that this may reflect different matching or filtering pipelines and should be resolved before treating the coverage estimates as interchangeable; the matching procedure behind each total is precisely what is unresolved, so neither side may be described here as using a particular matching rule. [src: bacdive_phenotype_metal_tolerance] [src: bacdive_metal_validation]

### 2. Does the composite score track metal-associated isolation?

**Side A — strong association reported.** The isolation-environment analysis reports a strong heavy-metal association for the composite score, Cohen's d = +1.00 (Cohen's d = a standardized difference between group means expressed in pooled standard-deviation units; +1.00 is a full standard deviation). [src: bacdive_metal_validation]

**Side B — no detectable correlation reported.** The metal cross-resistance analysis reports no species-scale correlation with metal-associated isolation, Spearman rho approximately -0.02, p > 0.8 (Spearman rho = a rank-based correlation coefficient; a value near zero with a large p-value means no monotonic relationship was detectable in that analysis). This is a non-detection as reported, not an established null. [src: metal_cross_resistance]

This tension cannot be resolved from the available summaries because the analyses differ in matching, aggregation, and outcome definition; a common strain-level bridge and preregistered metal-specific outcomes are needed. [src: metal_cross_resistance]

### 3. How much do metal-important genes overlap counter-ion/osmotic stress?

**Side A — higher overlap.** In the counter-ion analysis, metal-important genes overlapped with NaCl-stress genes at 39.8%. [src: metal_specificity]

**Side B — lower overlap.** In the metal-specificity analysis, 14.7% of metal-important genes were sick under osmotic stress. [src: metal_specificity]

Both figures reach this page under a single citation tag, and the input labels the sides only as "the counter-ion analysis" and "the metal-specificity analysis"; no claim is made here about which project computed which figure. The difference was attributed to stricter fitness and statistical thresholds and partially different organism sets; the directional agreement supports overlap between metal and osmotic stress while showing that composite or thresholded scores are sensitive to operational definitions — a methodological tension rather than a biological resolution. [src: metal_specificity]

### 4. What fraction of metal-relevant genes is core?

**Side A — genome-wide metal-important genes.** The atlas reports an 87.4% core fraction for broad metal-important genes. [src: metal_fitness_atlas]

**Side B — metal-specific genes.** The specificity analysis reports an 84.8% pooled core fraction for metal-specific genes. [src: metal_specificity]

**Side C — cross-resistance tiers.** The cross-resistance analysis reports tiered core fractions of 92.0% / 91.0% / 89.8%. [src: metal_cross_resistance]

The atlas's genome-wide core-enrichment result is directionally consistent with the existing two-tier interpretation, but its figure is not directly interchangeable with the other two because the sources use different gene sets and definitions. The concept page states this should be resolved by applying a common locus set, conservation definition, metal-specificity threshold, and non-metal control set rather than by averaging the estimates. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

## Possible Reconciliations

These are hypotheses, not findings; none is established by the evidence above.

*Bridge totals (1).* **Hypothesis: the two totals are different stages of one pipeline, not two answers to one question.** The smaller total may be a post-filter set — restricted to strains carrying the fields that analysis required — while the larger may be an earlier match set. **Hypothesis: different matching or filtering rules.** A pipeline that accepts looser name matches would link more strains than one requiring stricter agreement, which would raise strain and species totals together in the direction observed; the concept page itself flags matching or filtering differences as the candidate cause. Under either hypothesis both totals are correct for their own pipeline and neither is a coverage estimate for the other's analysis. [src: bacdive_phenotype_metal_tolerance] [src: bacdive_metal_validation]

*Effect size vs non-detection (2).* **Hypothesis: aggregation level, not signal strength, drives the discrepancy.** A contrast between a contaminated-isolation group and a baseline is a different estimand from a species-scale rank correlation across all species, and averaging scores to species can dilute a group contrast toward zero. **Hypothesis: outcome definition.** A categorical "isolated from heavy-metal contamination" label and a broader species-level "metal-associated isolation" variable need not measure the same thing. **Hypothesis: sample composition and power.** A large group contrast and a corpus-wide correlation near zero can coexist if the association is confined to a small subset, or if the correlation was estimated on too few independent units to detect anything. The projects themselves note that matching, aggregation, and outcome definition all differ. [src: metal_cross_resistance]

*Overlap percentages (3).* The reported reconciliation is the leading hypothesis: **stricter fitness and statistical thresholds plus partially different organism sets** shrink 39.8% to 14.7% without either estimate being wrong. [src: metal_specificity] A second hypothesis: **the denominators differ** — "overlapped with NaCl-stress genes" and "sick under osmotic stress" may index different comparator experiment sets, so the two percentages may not be the same ratio computed twice.

*Core fractions (4).* **Hypothesis: differently drawn gene sets with different baselines.** Broad metal-important genes, metal-specific genes, and cross-resistance tiers are different selections from the same fitness data, and core enrichment can vary with how narrowly the gene set is drawn. **Hypothesis: conservation definition.** "Core" depends on the pangenome and the presence threshold used; two definitions applied to one locus set can move a core fraction by several points. **Hypothesis: pooled vs organism-mean aggregation.** A pooled fraction (total core / total genes) and a mean of per-organism fractions weight organisms with large gene sets differently. Under all three, the estimates would not be in conflict but simply not comparable — which is why the concept page directs that they not be averaged. [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]

## Resolving Work

**Bridge totals (1)**
- Recompute both bridges from the same BacDive snapshot and GTDB release with a single logged matching function, emitting strict-match and fallback-match counts separately; question: does either published total reappear, and is the gap a matching-rule difference?
- Publish per-stage strain counts for each analysis (raw records → name-matched → score-linked → metadata-complete); question: is 37,368 a filtered subset of 42,227, or an independently matched set?
- Diff the two matched-species lists and classify every species present in one list and absent from the other by cause (name handling, synonym resolution, missing pangenome score); question: which rule accounts for most of the difference?
- Re-run each analysis's headline result on the intersection bridge; question: do the effect sizes survive a common denominator?

**Effect size vs non-detection (2)**
- Build a single strain-level bridge and preregister metal-specific outcomes before analysis; question: at strain level with one outcome definition, is the association d = +1.00, rho ≈ -0.02, or neither?
- Recompute the species-scale Spearman correlation restricted to the contaminated-isolation categories used in the d = +1.00 contrast; question: is the non-detection a dilution artifact of corpus-wide aggregation?
- Report the group sizes, number of independent species, and score distributions behind both statistics side by side; question: does either statistic have the power to distinguish the two reported results?
- Apply a phylogenetically aware model to both estimands on the shared bridge; question: does either association survive control for lineage structure?

**Overlap percentages (3)**
- Recompute both overlap statistics on one organism set across a grid of fitness and significance thresholds; question: at which thresholds does 39.8% become 14.7%?
- State the denominator and comparator experiment set explicitly for each ("NaCl-stress genes" vs "sick under osmotic stress"); question: are these the same ratio at all?
- Add a non-metal, non-osmotic control-stress overlap as a floor; question: how much of either overlap exceeds a generic stress-gene baseline?

**Core fractions (4)**
- Apply a common locus set, a single conservation definition, one metal-specificity threshold, and a non-metal control set, then recompute all estimates; question: do 87.4%, 84.8%, and 92.0%/91.0%/89.8% converge, or do the gaps persist under identical definitions? [src: metal_fitness_atlas] [src: metal_specificity] [src: metal_cross_resistance]
- Report every core fraction as both pooled and organism-mean, each with its baseline alongside; question: how much of the spread is an aggregation choice?
- Trace each gene set's containment relationship to the others; question: do the differences track how narrowly the set is drawn?
- Compute the forbidden shortcut explicitly and test it: show a pooled average of the published figures against the recomputed common-definition estimate; question: how far would averaging have misled?
