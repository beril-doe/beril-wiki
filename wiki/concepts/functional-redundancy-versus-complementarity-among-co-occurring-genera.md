---
type: "Concept"
description: "Whether co-occurring plant-associated genera in soil and rhizosphere communities are metabolically complementary or redundant, including effect-size formula error, aggregation choices and pathway resolution."
sources: ["summaries/discoveries.md", "summaries/plant_microbiome_ecotypes__REPORT.md"]
---
# Functional redundancy versus complementarity among co-occurring genera

Co-occurring plant-associated genera in NMDC soil and rhizosphere communities look functionally redundant, not complementary. The direction was robust under both aggregation methods the plant_microbiome_ecotypes report compared [src: plant_microbiome_ecotypes], and the report says it is robust at pathway resolution after the formula correction. [src: plant_microbiome_ecotypes] The first reported effect (Cohen's d = −7.54) was mostly a formula error, and the corrected effect is small, |d| ≈ 0.4. [src: plant_microbiome_ecotypes] The data come from NMDC soil communities, analysed across 80 GapMind pathways. [src: plant_microbiome_ecotypes] See also [[summaries/plant_microbiome_ecotypes__REPORT]] and [[summaries/discoveries]].

## The headline result and its correction

The central digest reported that co-occurring plant-associated genera show redundancy rather than complementarity (permutation p=1.0, Cohen's d=-7.54). [src: discoveries] The project report originally read d = -7.54 as strong redundancy. [src: plant_microbiome_ecotypes] It later called that value implausibly large. [src: plant_microbiome_ecotypes]

The cause was the denominator. NB06 divided the mean difference by the SD (standard deviation) of permutation means, which shrinks toward zero by the central limit theorem. NB14 divides by the raw pair-level SD, which is much larger. [src: plant_microbiome_ecotypes] The report also described the inflation as coming from max-aggregated species-to-genus GapMind scores. [src: plant_microbiome_ecotypes] Its own decomposition puts most of the change on the formula, not the aggregation (below). [src: plant_microbiome_ecotypes]

The underlying data were 69 genera in 348 soil/rhizosphere samples, all with GapMind data across 80 pathways. [src: plant_microbiome_ecotypes] The 1,048 co-occurring pairs had mean complementarity of 10.72. The richness-preserving permutation null (1,000 iterations) gave 12.74±0.27. [src: plant_microbiome_ecotypes] [[entities/gapmind]] supplied the pathway calls.

## Formula versus aggregation

Recomputing NB06's max-aggregated complementarity with the consistent formula on the same data gave d ≈ −0.43. [src: plant_microbiome_ecotypes] Switching from species-max to species-prevalence aggregation (the fix made in NB14) lowered |d| to 0.39. [src: plant_microbiome_ecotypes] Max-aggregation is a binary present/absent call per genus. Prevalence-weighting uses the fraction of species with the pathway. That switch is a ≈10% effect. [src: plant_microbiome_ecotypes]

The report therefore attributes the apparent 20× reduction to about 90% formula change and about 10% aggregation change. [src: plant_microbiome_ecotypes] NB14 described the same pattern. Direction was unchanged, and most of the move from −7.54 to −0.39 came from the formula. [src: plant_microbiome_ecotypes] The NB14 re-test was called credible in magnitude and the same in direction. [src: plant_microbiome_ecotypes] The direction was robust under both methods. [src: plant_microbiome_ecotypes]

## Corrected interpretation

Co-occurring genera in NMDC soil communities were slightly less complementary than random pairs (Cohen's d ≈ −0.4, permutation p < 0.001). This supports redundancy at a small effect size. [src: plant_microbiome_ecotypes] The real effect is small but stable, and the dramatic −7.54 was an artifact. [src: plant_microbiome_ecotypes] Hypothesis H3 (that co-occurring genera are complementary) stays not supported, because the conclusion does not depend on the aggregation choice. [src: plant_microbiome_ecotypes]

The report places this in line with Louca et al. (2018), who argued that functional redundancy is an emergent property of microbial systems. It adds that the small effect now sits within the range typical of comparable analyses. [src: plant_microbiome_ecotypes] It also calls the result consistent with the empirical findings of Puente-Sanchez et al. (2024). [src: plant_microbiome_ecotypes] Puente-Sanchez et al. found that complementarity can drive genome streamlining in some contexts. [src: plant_microbiome_ecotypes]

The report proposes, as an ecological reading, that environmental filtering for the same functions dominates assembly over niche partitioning. [src: plant_microbiome_ecotypes, discoveries] This is an interpretation, not a direct test. The digest states it as a conclusion that plant compartments select a common functional toolkit. [src: discoveries]

## Limits on the redundancy conclusion

- **Pathway resolution.** The report warns that 80 GapMind pathways may be too coarse. [src: plant_microbiome_ecotypes] Complementarity may exist at finer metabolic resolution. [src: plant_microbiome_ecotypes] It proposes reaction-level or substrate-specific analysis to reveal patterns that pathway-level aggregation masks. [src: plant_microbiome_ecotypes]
- **Genus matching.** The NMDC taxonomy bridge matched 260 of 322 genera (80.7%) to GTDB and lost 62 (19.3%). [src: plant_microbiome_ecotypes] Sensitivity analysis of this loss was deferred. [src: plant_microbiome_ecotypes] The effect on H3 is unknown. If the unmatched genera include key complementary partners, the redundancy signal could be artifactual. [src: plant_microbiome_ecotypes] See [[concepts/genus-level-taxonomy-bridging-to-pangenome-clades-and-its-coverage-limits]].
- **GapMind scoring.** Core-level completeness was 0% across all compartments, which suggests the threshold is too stringent for broad taxonomic comparison. [src: plant_microbiome_ecotypes] That threshold remains a separate open question. [src: plant_microbiome_ecotypes] In support of the pathway scores themselves, BacDive metabolite utilization cross-validated GapMind predictions at 83.1% consistency. [src: plant_microbiome_ecotypes] See [[concepts/reliability-and-coverage-limits-of-gapmind-pathway-predictions]] and [[entities/bacdive]].
- **PGP–pathogen exclusion test.** The original NMDC co-occurrence data had 0 PGP-dominant and 2 pathogen-dominant genera, and the other 67 were dual-nature (PGP = plant growth promoting). A C-score analysis was therefore not feasible. [src: plant_microbiome_ecotypes] The Phase 2b refined-cohort re-test found 0 PGP-dominant, 3 pathogen-dominant and 66 dual-or-mixed of 69 genera. [src: plant_microbiome_ecotypes] Verification #12 (≥5 PGP-only genera) was not met, and this did not change H3. [src: plant_microbiome_ecotypes] Dual-nature genera dominate under both the 25-marker and 17-marker panels. The report concludes the test is structurally underpowered in this dataset, not a marker-panel artifact. [src: plant_microbiome_ecotypes]

## Slots into review practice

The formula error was caught by a paired adversarial review. See [[concepts/adversarial-review-pre-registration-and-multiple-testing-discipline]]. [src: plant_microbiome_ecotypes]

## Open Directions

- Re-run the complementarity test at reaction level or on substrate-specific subsets, to see whether the small redundancy effect hides complementarity that 80 pathways cannot resolve.
- Run the deferred sensitivity analysis on the 62 unmatched NMDC genera, for example by testing alternative taxonomy bridges. This would show whether missing partners make the redundancy signal artifactual.
- Test complementarity with a relaxed or graded GapMind completeness threshold, to see whether the 0% core-level result changes the effect.
- Apply the same corrected formula (raw pair-level SD) and prevalence-weighting to other habitats or datasets. This would show whether |d| ≈ 0.4 is general or specific to NMDC soil.
- Use a dataset with more PGP-only genera to run the PGP–pathogen C-score test, since NMDC cannot power it.
