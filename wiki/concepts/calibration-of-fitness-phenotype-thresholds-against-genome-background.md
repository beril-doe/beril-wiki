---
type: "Concept"
description: "How pre-registered fitness-phenotype thresholds should be set relative to the genome-wide background rate, and what an RB-TnSeq compendium can and cannot test (e.g. missing iron-limitation conditions); stops at fitness-compendium design."
sources: ["summaries/caulobacter_fur_lipida_loss__REPORT.md", "summaries/costly_dispensable_genes__REPORT.md"]
---
# Calibration of fitness-phenotype thresholds against genome background

How pre-registered fitness-phenotype thresholds should be set relative to the genome-wide background rate, and what an RB-TnSeq compendium can and cannot test (e.g. missing iron-limitation conditions); stops at fitness-compendium design.

## The miscalibration

The pre-registered ≥10% phenotype-bearing threshold sat below the 33.25% background rate. The report calls this a methodological miscalibration that adversarial review surfaced. [src: caulobacter_fur_lipida_loss] Background was defined as |fitness t| > 4 in ≥ 2 envelope-stress experiments. It came to 33.25% (n=3943 Caulobacter genes; K=1311 phenotype-bearing). [src: caulobacter_fur_lipida_loss] Passing the threshold was therefore uninformative about specific mechanistic importance. [src: caulobacter_fur_lipida_loss] The threshold was essentially a presence test, not an enrichment test. [src: caulobacter_fur_lipida_loss] The report states that a ≥10% threshold against a 33% background passes any random gene set. [src: caulobacter_fur_lipida_loss]

## Recalibrated verdicts

The revised formal H2 verdict uses hypergeometric enrichment against background, with the requirement p<0.05 AND fold≥1.5×. [src: caulobacter_fur_lipida_loss] The 22-experiment envelope-stress subset was judged large enough for this comparison. [src: caulobacter_fur_lipida_loss] The two Fur-regulon paths gave different results under the recalibrated test. The verdicts are recorded in a two-row results file. [src: caulobacter_fur_lipida_loss]

- Path A (concordant_strong, clean Fur signature) had 17 of 32 genes phenotype-bearing (53.1%). Fold was 1.60× and p = 0.016, which the report judged marginally enriched and SUPPORTED. [src: caulobacter_fur_lipida_loss]
- Path B (SspB-buffered) had 9 of 26 genes phenotype-bearing (34.6%). Fold was 1.04× and p = 0.515, which is indistinguishable from the 33.25% background. The recalibrated verdict is NOT SUPPORTED. [src: caulobacter_fur_lipida_loss]

Path B passed the old ≥10% threshold at 9/26 = 35%. The report demoted that arm to a hypothesis. [src: caulobacter_fur_lipida_loss]

The report recommends calibrating pre-registered thresholds in Fitness Browser projects against the genome-wide background, not a fixed percentage. [src: caulobacter_fur_lipida_loss] It also recommends fold-enrichment over background for future H2 thresholds. [src: caulobacter_fur_lipida_loss] See also [[concepts/fur-derepression-and-transcript-buffering-by-regulator-co-deletion]].

## What the compendium cannot test

The Caulobacter compendium (see [[entities/fitness-browser]] and [[entities/random-barcode-transposon-sequencing]]) has 198 experiments. [src: caulobacter_fur_lipida_loss] The report describes these as 95 stress experiments (envelope-, drug-, and metal-related), 46 nitrogen-source, 42 carbon-source and 10 PYE control experiments, plus 5 others. [src: caulobacter_fur_lipida_loss] The report's separate per-experiment condition classification file also has 198 rows and reports envelope=22, oxidative=4, carbon=48, iron=0. [src: caulobacter_fur_lipida_loss] The claims do not explain why its carbon count (48) differs from the 42 carbon-source experiments above, so the two breakdowns are stated separately and not reconciled. Both agree that the compendium has zero iron-limitation experiments. [src: caulobacter_fur_lipida_loss]

The plan's preflight rule required at least 3 iron-limitation experiments and found 0. [src: caulobacter_fur_lipida_loss] H2's iron-limitation arm was therefore descoped to exploratory. [src: caulobacter_fur_lipida_loss] H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss] The iron-flux arm was untestable in this report. [src: caulobacter_fur_lipida_loss]

The report proposes two ways to close the gap: new experiments under bipyridyl chelation, or a cross-walk to Leaden 2018's published Δfur phenotype. [src: caulobacter_fur_lipida_loss] It also proposes targeted fitness experiments under bipyridyl chelation, ferric salt supplementation and hemin. These would test whether the Fur-released subset that scores phenotype-bearing under envelope stress also scores under iron limitation. [src: caulobacter_fur_lipida_loss]

## Related caveat on classification definitions

A separate project defines gene burden as max_fit > 1 in any experiment. A single experiment can then classify a gene as burdensome, which makes the classification sensitive to noise in the fitness data. [src: costly_dispensable_genes]

## Open Directions

- Recompute the Caulobacter background rate on other condition subsets (carbon, nitrogen, oxidative). Then test whether a single enrichment criterion holds across axes. This addresses the fact that the 33.25% background was measured only for envelope stress.
- Add bipyridyl, ferric salt and hemin RB-TnSeq experiments in Caulobacter. This would let the iron arm of H2 be tested against its own background and would close the preflight failure.
- Run a permutation or random-gene-set null for the burden definition max_fit > 1. This would measure how often one noisy experiment classifies a gene as burdensome.
- Re-evaluate Path A, which is only marginally enriched (fold 1.60×, p = 0.016), with a stricter multiple-testing or sensitivity analysis. Vary the |t| and experiment-count cutoffs to see whether the verdict is stable.
