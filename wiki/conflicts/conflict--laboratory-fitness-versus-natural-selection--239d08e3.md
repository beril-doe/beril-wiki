<!-- tension-hash: 239d08e358ff3c3b -->
# Tension: Does the Essentiality–Conservation Gradient Survive Rescoping and Covariate Adjustment?

Two projects report different headline values for how often essential genes fall in the core genome — 82% versus 86.1% — and a single-organism model suggests that much of the apparent fitness–conservation signal may be carried by gene length rather than by fitness itself. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness] [src: field_vs_lab_fitness] The disagreement matters because the same gradient is used to argue that laboratory fitness is a partial proxy for natural selection (see [[concepts/laboratory-fitness-versus-natural-selection]]); if the estimate moves with cohort definition or collapses under covariate adjustment, the strength of that proxy claim changes with it.

## Evidence Sides

**Broad synthesis: 82% essential-core.** The broad synthesis reports an essential-core estimate of 82%, framed as one end of a quantitative gradient across its cohort. [src: conservation_fitness_synthesis] "Core" here means presence across a species' pangenome — the union of genes seen in a species — rather than presence in any single genome.

**33-organism linkage: 86.1% essential-core.** The linkage analysis, run over 33 organisms, reports 86.1% essential-core. [src: conservation_vs_fitness] The tension is described as an unresolved *scope* tension: the two cohorts and the two essentiality definitions differ, so the numbers are not competing estimates of a single quantity.

**DvH, length-adjusted: CV-AUC rises to 0.645.** In *Desulfovibrio vulgaris* Hildenborough (DvH), adding gene length raised CV-AUC — cross-validated area under the receiver-operating-characteristic curve, a measure of how well a model ranks positives above negatives — to 0.645, whereas fitness alone reached only 0.517–0.548. [src: field_vs_lab_fitness] This is a single-organism result.

**Broad analyses, unadjusted: a real but weak gradient.** Broader analyses report a real but weak gradient without any length adjustment. [src: fitness_effects_conservation, conservation_fitness_synthesis] They therefore neither confirm nor refute the DvH length effect; they simply did not test for it.

## Possible Reconciliations

- *Hypothesis: cohort composition explains the 82% versus 86.1% offset.* If the two cohorts differ in organism membership and in how essentiality is called, both values could be correct for their own scope and never need reconciling into one number. [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]
- *Hypothesis: gene length is a shared confounder of both fitness and conservation.* Longer genes may be both easier to call as essential (more transposon insertion opportunities) and more likely to be core, in which case part of the broad gradient is length, not selection. [src: field_vs_lab_fitness]
- *Hypothesis: the DvH result is organism-specific.* The length effect may reflect DvH's insertion callability rather than a general property, leaving the broad weak gradient intact. [src: field_vs_lab_fitness] [src: fitness_effects_conservation, conservation_fitness_synthesis]

## Resolving Work

- Recompute the broad gradient with gene length as an explicit covariate and report how much of the effect remains — does the weak gradient survive length adjustment outside DvH? [src: conservation_fitness_synthesis]
- Harmonise essentiality definitions and organism membership across the two cohorts, then re-derive both core percentages under each definition — is the 82%/86.1% gap definitional or biological? [src: conservation_fitness_synthesis] [src: conservation_vs_fitness]
- Model insertion callability (per-gene insertion opportunity) alongside fitness in the broad cohort — is "essential" partly an artefact of low callability? [src: field_vs_lab_fitness]
- Add phylogenetic correction so related organisms are not counted as independent observations — does the gradient hold after shared-ancestry adjustment? [src: conservation_vs_fitness]
- Vary pangenome coverage (number and breadth of genomes per species) and test whether core fraction estimates, and the gradient between categories, are stable. [src: fitness_effects_conservation, conservation_fitness_synthesis]
