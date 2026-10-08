<!-- tension-hash: 3657d68293e1612c -->
# Global Metal-Resistance Prevalence Versus Local Co-Enrichment with T4SS-Linked Neighbourhoods

Two projects reach apparently opposite readings of how metal resistance relates to horizontal-gene-transfer machinery in environmental metagenome-assembled genomes (MAGs, genomes reconstructed from metagenomic reads). One reads a global contrast between marginal prevalences (each feature's frequency measured separately, not their co-occurrence) as evidence that metal resistance and type IV secretion system (T4SS, a conjugative transfer apparatus) machinery are not uniformly co-distributed. The other reports conditional enrichment of metal-resistance types in MAGs whose glycosyltransferase family 2 (GT2) genes sit in T4SS-adjacent neighbourhoods. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt] The question matters for [[concepts/scale-dependent-mobile-element-associations]] because global decoupling and local coupling would imply different roles for conjugative machinery in spreading metal-resistance functions. A shared MAG denominator for the global contrast has not been established, so the two readings may not be in direct conflict. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]

## Evidence Sides

**Global contrast reads as non-uniform co-distribution**

The metal-resistance biogeography report gives a 2.8% metal-resistance prevalence in 22,356 geolocated MAGs. It sets this against a 21.8% T4SS prevalence and reads the difference as non-uniform co-distribution. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt] The evidence does not establish that the two prevalences share a MAG denominator, and different marginal prevalences do not establish a relationship in the joint distribution (how often the two features occur together in the same MAG), so this side does not demonstrate decoupling. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]

**Local conditional enrichment in GT2-neighbourhood MAGs**

The T4SS–CAZy analysis, named for carbohydrate-active enzyme (CAZy) families, found a mean of 0.045 metal-resistance types in GT2-neighbourhood MAGs (n=376), against 0.004 in non-GT2 MAGs. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt] This enrichment awaits the T4SS–CAZy threshold check and the housekeeping-gene check (housekeeping genes are conserved genes for routine cellular functions, used as a control baseline). Neither this result nor the global contrast has been tested against a shared null baseline. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]

## Possible Reconciliations

- **Hypothesis: scale dependence.** Metal resistance could be rare across the environmental MAG pool yet concentrated in a small subset of genomes, so the local enrichment could coexist with low global prevalence; this would not show that the global contrast demonstrates decoupling. Neither side has been tested against a shared null baseline. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]
- **Hypothesis: denominator mismatch.** If the two prevalences were computed over different MAG sets, the global contrast would carry no co-occurrence information, leaving the local result as the only joint-distribution evidence. A shared denominator has not been established. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]
- **Hypothesis: artefactual enrichment.** The local enrichment could weaken or disappear once the still-pending threshold and housekeeping-gene checks are applied, leaving neither side with demonstrated coupling. [src: metal_resistance_global_biogeography, t4ss_cazy_environmental_hgt]

## Resolving Work

- **Shared denominator:** Recompute metal-resistance and T4SS carriage on the same geolocated MAG set and cross-tabulate them. Test association with a contingency test such as Fisher's exact test. *Question:* within one denominator, does T4SS carriage predict metal-resistance carriage?
- **Shared null baseline:** Permute gene labels across MAGs, stratified by genome size and taxonomy, to build one null for a joint-occurrence association statistic (such as an odds ratio) applied to both the global MAG set and the GT2-neighbourhood comparison. *Question:* does either co-occurrence signal exceed chance expectation?
- **Threshold sensitivity:** Rerun the GT2-neighbourhood definition across a range of T4SS–CAZy distance thresholds. *Question:* does the metal-resistance enrichment persist across thresholds or depend on one cut-off?
- **Housekeeping-gene control:** Compare GT2-neighbourhood and non-GT2 MAGs for housekeeping-gene counts and completeness. *Question:* is the enrichment explained by differences in assembly quality or genome size rather than by mobilization?
