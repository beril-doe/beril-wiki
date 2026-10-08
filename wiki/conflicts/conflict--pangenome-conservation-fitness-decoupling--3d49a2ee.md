<!-- tension-hash: 3d49a2ee7d685cf2 -->
# Do the metal fitness atlas and the counter-ion analysis report the same per-metal core-enrichment deltas?

Two projects report per-metal "deltas" for metal-tolerance genes: the difference between the fraction of fitness-important genes classified as core in the pangenome (the full gene set across a species' sequenced genomes) and a baseline core fraction. The deltas reported in the metal fitness atlas do not match the pre-correction deltas reported in the counter-ion effects analysis for the same metals. Neither report, as cited here, explains whether different gene sets or baselines account for the gap [src: metal_fitness_atlas, counter_ion_effects]. This matters for [[concepts/pangenome-conservation-fitness-decoupling]], because the size and sign of these deltas are the evidence for how strongly metal fitness genes concentrate in the core genome.

## Evidence Sides

**Metal fitness atlas values**

The atlas reports cadmium at -0.010 and molybdenum at +0.148 [src: metal_fitness_atlas, counter_ion_effects].

**Counter-ion effects pre-correction values**

Before the counter-ion analysis applies its correction, it reports cadmium at -0.008 and molybdenum at +0.132 [src: metal_fitness_atlas, counter_ion_effects].

**What is and is not established**

The values differ in magnitude for both metals. In the examples cited, they agree in sign: cadmium is negative in both and molybdenum is positive in both [src: metal_fitness_atlas, counter_ion_effects]. Neither report, as cited here, says whether different gene sets or baselines explain the difference. The wiki therefore records both values and does not prefer either one [src: metal_fitness_atlas, counter_ion_effects].

## Possible Reconciliations

- **Hypothesis: different gene sets.** The counter-ion analysis may have rebuilt the set of fitness-important genes with a different threshold, organism set or filtering step. That would change which genes enter each metal's core fraction.
- **Hypothesis: different baselines.** The two projects may compute the baseline core fraction differently, for example per metal versus pooled across organisms. That would shift every delta even if the gene sets were identical.
- **Hypothesis: different data snapshots.** The projects may have drawn on different versions of the fitness or pangenome tables in the KBase Data Lakehouse. Small changes in gene-to-cluster mapping would then move the deltas.

Neither report, as cited here, establishes any of these. Each is a candidate explanation only.

## Resolving Work

- **Gene-level comparison:** Join the per-metal gene lists from both projects on gene identifier and compute the set differences. This tests whether the two projects scored the same genes for cadmium and molybdenum.
- **Baseline audit:** Recompute each metal's baseline core fraction under both projects' definitions on one shared organism set. This tests whether the delta gap is entirely due to the baseline.
- **Snapshot check:** Record the table versions each project queried, rerun the atlas pipeline on the counter-ion project's snapshot, and compare the outputs. This tests whether data drift accounts for the gap.
- **Full-table reconciliation:** Line up every metal's delta from both reports and check whether the gap is systematic (same direction and similar size) or specific to individual metals. This tests whether a single method difference can explain the discrepancy.
