---
type: Method
description: Complete-gene deletion method for testing essentiality and growth defects
sources:
- id: adp1_triple_essentiality
  resource: ../summaries/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
- id: amr_fitness_cost
  resource: ../summaries/amr_fitness_cost__REPORT.md
  title: amr fitness cost
- id: annotation_gap_discovery
  resource: ../summaries/annotation_gap_discovery__REPORT.md
  title: annotation gap discovery
- id: fitness_effects_conservation
  resource: ../summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
title: Gene knockout
---
# Gene knockout

## What this entity is

**Canonical name:** gene knockout. [^adp1_triple_essentiality]

**Known aliases:** complete-gene knockout; gene deletion; deletion mutant. [^adp1_triple_essentiality]

**Stable external identifier:** none reported in the source document. [^adp1_triple_essentiality]

Gene knockout is a method that removes an entire gene to test whether its absence causes lethality or a measurable growth defect. [^adp1_triple_essentiality] It provides a distinct essentiality measurement from [tnseq](tnseq.md), which uses transposon insertions, and from [flux-balance-analysis](flux-balance-analysis.md), which predicts growth consequences computationally. [^adp1_triple_essentiality] The AMR fitness analysis further **refines** this distinction: its RB-TnSeq measurements are fitness values relative to the pool average, whereas complete deletion tests the phenotype of removing the whole gene. [^amr_fitness_cost]

## Evidence from ADP1

In the refined comparison, FBA versus knockout data covered 724 genes in rich media and yielded recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486. [^adp1_triple_essentiality] In minimal media, the comparison covered 833 genes and yielded recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493. [^adp1_triple_essentiality] These results support moderate concordance between gene-knockout lethality and FBA at the lethal-versus-dispensable boundary, while not establishing that FBA predicts quantitative growth defects among TnSeq-dispensable genes. [^adp1_triple_essentiality]

Rich-media knockout data covered 2,953 genes, including 346 essential and 2,607 dispensable genes. [^adp1_triple_essentiality] The merged minimal-media set covered 3,092 genes, including 499 essential genes; minimal-media calls were prioritized and rich-media calls were used as fallback. [^adp1_triple_essentiality]

## Discordance with RB-TnSeq

At the RB-TnSeq essentiality threshold of 0.05, the comparison included 1,933 genes: 18 genes (0.9%) were essential by both methods, 1,411 (73.0%) were dispensable by both, 211 (10.9%) were knockout-essential but TnSeq-dispensable, and 293 (15.2%) were knockout-dispensable but TnSeq-essential. [^adp1_triple_essentiality] Across RB-TnSeq thresholds of 0.01, 0.025, 0.05, 0.10, and 0.20, Cohen’s kappa values were -0.139, -0.122, -0.081, -0.024, and -0.014, respectively. [^adp1_triple_essentiality]

The report interprets the discordance as consistent with transposon insertion measuring fitness cost while potentially preserving partial function, whereas complete deletion measures lethality. [^adp1_triple_essentiality] Partial or truncated protein production, read-through transcription, retained functional domains, and condition aggregation are proposed mechanisms rather than directly resolved demonstrations. [^adp1_triple_essentiality] The AMR study **supports** treating these assays as non-equivalent: only 4.6% of AMR genes were absent from its fitness matrices and therefore putatively essential, compared with an approximately 14% background essential rate estimated in a prior analysis using a different organism set. [^amr_fitness_cost] Because transposon insertions can have polar effects on downstream genes in operons, they can also confound AMR-gene fitness measurements. [^amr_fitness_cost]

## Relation to essentiality and model gaps

The knockout results contribute to [gene-essentiality](../concepts/gene-essentiality.md), where they provide a direct deletion-based reference for comparing FBA, [tnseq](tnseq.md), fitness, and proteomics. [^adp1_triple_essentiality] They also contribute to [condition-specific-fitness](../concepts/condition-specific-fitness.md), because knockout phenotypes are compared with mutant growth across conditions. [^adp1_triple_essentiality] The AMR analysis **refines** this comparison by showing that genome-wide transposon fitness data can quantify relative AMR-gene burden and condition-dependent importance, but not directly substitute for complete-gene deletion phenotypes. [^amr_fitness_cost]

The conservation analysis **supports** using mutant fitness as a complementary, quantitative context for knockout-based essentiality: across approximately 194,000 genes from 43 bacteria, essential genes were 82% core, whereas always-neutral genes were 66% core, although fitness importance was only a weak predictor of conservation. [^fitness_effects_conservation] It also **refines** the interpretation of condition dependence: genes with strong condition-specific effects were 77.3% core versus 70.3% without such annotations (OR=1.78, p=1.8e-97), and 4,450 genes (2.7%) were neutral overall but critical in one condition. [^fitness_effects_conservation] These findings do not replace complete-gene deletion tests, because the fitness measurements were based on single-gene transposon mutants and were biased toward rich media and standard stresses. [^fitness_effects_conservation]

Aromatic degradation was strongly enriched among FBA-discordant genes, with 9 of 11 genes discordant, odds ratio (OR) = 9.70, and Benjamini-Hochberg false discovery rate (FDR)-adjusted q = 0.012. [^adp1_triple_essentiality] Directional enrichment for FBA under-prediction was OR = 12.0 and q = 0.004. [^adp1_triple_essentiality] The report identifies beta-ketoadipate-pathway genes, including 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase, as examples predicted as blocked by FBA but associated with experimental growth defects. [^adp1_triple_essentiality] These findings feed [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) by indicating that knockout phenotypes can expose environmental assumptions missing from a metabolic model. [^adp1_triple_essentiality]

The annotation-gap study **refines** this model-gap connection by using gene knockouts as a proposed validation route for 23 inserted gene-protein-reaction (GPR) rules, formal links between genes and reactions, representing high- and medium-confidence candidates from gapfilled models. [^annotation_gap_discovery] Those simulations produced zero wildtype growth on minimal carbon-source media; this was inconclusive because the models required the gapfilled reactions themselves to grow on those carbon sources, making the knockout test circular in that setting. [^annotation_gap_discovery] Accordingly, the study prioritizes targeted gene-knockout or CRISPRi validation of 44 high-confidence gene-reaction assignments, especially reactions rxn02185 and rxn03436 across 9 organisms, rather than treating the in-model knockout results as independent validation. [^annotation_gap_discovery] This **supports** using complete-gene deletion as an experimental test of candidate annotations while distinguishing it from computational knockout simulations whose growth state depends on the candidate reaction. [^annotation_gap_discovery]

## Limitations and next tests

The original analysis was restricted to 478 TnSeq-dispensable genes because TnSeq-essential genes did not provide viable deletion mutants for growth-rate analysis. [^adp1_triple_essentiality] Therefore, its null result concerns growth variation among dispensable genes and is not a whole-genome test of FBA lethality prediction. [^adp1_triple_essentiality] Similarly, the AMR fitness estimate excludes approximately 4.6% of AMR genes absent from fitness matrices; if these are the most costly genes, the reported relative effect may be a lower bound. [^amr_fitness_cost]

The conservation study **supports** retaining this caution about assay coverage: novel singleton genes showed near-zero mean fitness under the tested laboratory conditions, but the apparent neutrality may reflect poor transposon coverage rather than true dispensability. [^fitness_effects_conservation] Its conservation gradient was statistically robust but spanned only a 16-percentage-point difference between essential and always-neutral categories, so mutant fitness remains a weak predictor of pangenome status. [^fitness_effects_conservation]

The annotation-gap study **supports** this caution about computational knockout validation: its zero-growth results cannot distinguish a correct gene-reaction assignment from the enforced requirement for the gapfilled reaction. [^annotation_gap_discovery] It also **refines** the next-test design by recommending targeted deletion or CRISPRi of experimentally testable high-confidence candidates, with emphasis on the 44 assignments and the two reactions resolved with high confidence in 9 organisms. [^annotation_gap_discovery]

The report recommends condition-matched TnSeq and knockout experiments, domain- and insertion-position analysis of the 211 knockout-essential/TnSeq-dispensable genes, and combined FBA-plus-fitness-plus-proteomics prediction. [^adp1_triple_essentiality] The conservation results **support** adding core and accessory status, fitness breadth, and condition-specific phenotype annotations to that comparison, while testing whether deletion phenotypes reproduce the observed core-gene enrichment. [^fitness_effects_conservation] The AMR study **supports** condition matching as a next test: it found 57.0% of AMR genes showing a flip toward greater importance under any-antibiotic exposure, but its class-matched validation covered only 157 gene-antibiotic pairs and was non-significant (p = 0.14). [^amr_fitness_cost]

## Related pages

- [adp1_triple_essentiality__REPORT](../summaries/adp1_triple_essentiality__REPORT.md) — source summary for the concordance analysis. [^adp1_triple_essentiality]
- [amr_fitness_cost__REPORT](../summaries/amr_fitness_cost__REPORT.md) — source summary for AMR fitness-cost analysis. [^amr_fitness_cost]
- [annotation_gap_discovery__REPORT](../summaries/annotation_gap_discovery__REPORT.md) — source summary for integrated annotation-gap discovery. [^annotation_gap_discovery]
- [fitness_effects_conservation__REPORT](../summaries/fitness_effects_conservation__REPORT.md) — source summary for the fitness–conservation analysis. [^fitness_effects_conservation]
- [gene-essentiality](../concepts/gene-essentiality.md) — cross-method essentiality synthesis. [^adp1_triple_essentiality]
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — model gaps revealed by knockout/FBA disagreement and candidate-gene testing. [^adp1_triple_essentiality][^annotation_gap_discovery]
- [tnseq](tnseq.md) — transposon-based comparison method. [^adp1_triple_essentiality]
- [flux-balance-analysis](flux-balance-analysis.md) — computational comparison method. [^adp1_triple_essentiality]

[^adp1_triple_essentiality]: [adp1 triple essentiality](../summaries/adp1_triple_essentiality__REPORT.md)
[^amr_fitness_cost]: [amr fitness cost](../summaries/amr_fitness_cost__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../summaries/fitness_effects_conservation__REPORT.md)
[^annotation_gap_discovery]: [annotation gap discovery](../summaries/annotation_gap_discovery__REPORT.md)
