<!-- tension-hash: 9415d508f6f4764c -->
# Metal-contamination isolation history and metal tolerance: a positive isolate-level effect against a species-scale null

Whether a bacterium's isolation source — a metal-contaminated site versus an environmental baseline — predicts its metal tolerance is unsettled in this corpus. One project reports a large positive effect from curated isolate metadata; another, testing the same hypothesis after collapsing to species, finds essentially no correlation. Because the metal-tolerance scoring underlying [[concepts/environmental-resistome]] is genome-based, whether isolation ecology validates it decides how far those scores can be trusted as ecological predictions rather than as annotation artifacts.

## Evidence Sides

**Positive effect at the isolate/strain scale.** Using BacDive (a curated bacterial strain metadata database), contamination-associated isolates score higher on metal tolerance, with Cohen's *d* (a standardized mean difference in units of the baseline standard deviation) of +1.00 for heavy-metal contamination on n = 10 isolates [src: bacdive_metal_validation]. This is a directional, positive result on a small denominator.

**No association at the species scale.** The cross-resistance analysis found no species-scale correlation between multi-metal tolerance and metal-associated isolation, with a Spearman rho (rank correlation) of approximately −0.02 at p > 0.8, on a set left with only 20 independent species after collapsing strains to species [src: metal_cross_resistance]. This is a null result on a small denominator, not evidence of an opposite effect.

**Habitat-scale genomic evidence — related but non-equivalent.** Across metagenome-assembled genomes (MAGs; genomes reconstructed from metagenomic reads rather than isolates), soil showed 5.8% prevalence of metal resistance with an odds ratio (OR) of 5.05 while marine samples showed 1.2% and OR = 0.20 [src: metal_resistance_global_biogeography]. In MicrobeAtlas, metal-type diversity was associated with groundwater prevalence (ρ = +0.112, p = 0.0019) but not with groundwater-specific fold enrichment (ρ = +0.042, p = 0.242) [src: microbeatlas_metal_ecology]. These test habitat occupancy, not isolation-source labels, so they neither confirm nor refute either side directly.

## Possible Reconciliations

- *Hypothesis: scale of the unit of analysis.* Collapsing strains to species may average away a strain-level tolerance signal, so the positive isolate-level *d* and the species-scale rho ≈ −0.02 could both be correct at their own units of analysis.
- *Hypothesis: denominator limits on both sides.* With n = 10 on one side and 20 independent species on the other, neither design may be able to distinguish a moderate true effect from no effect, so the disagreement could be sampling variation rather than biology.
- *Hypothesis: different constructs.* One side scores tolerance to metals generally; the other scores multi-metal tolerance. If cross-metal breadth and single-metal tolerance are decoupled, agreement would not be expected.
- *Hypothesis: label quality.* Isolation-source annotation may carry contamination signal that species-level matching dilutes, making the discrepancy a metadata-linkage effect.

## Resolving Work

- Re-run the isolate-level comparison and the species-collapsed test on one shared matched cohort, reporting both *d* and rho, to ask whether unit of analysis alone flips the sign.
- Conduct a pre-registered power analysis for both designs to state the smallest effect each denominator (n = 10; 20 independent species) can detect.
- Test single-metal versus multi-metal tolerance scores separately against the same isolation labels to ask whether the constructs diverge.
- Audit the strain-to-species matching step and quantify how many contamination labels are lost or blurred, asking whether linkage attrition explains the null.
- Join MAG habitat prevalence to isolation-source labels for shared taxa to ask whether habitat-scale enrichment and isolation-source effects agree within the same lineages.
