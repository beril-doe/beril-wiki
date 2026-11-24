---
type: "Concept"
description: "Comparison of continuous fitness, aggregated essentiality fraction and protein expression level as predictors of knockout essentiality by ROC AUC; stops at integration methods."
sources: ["summaries/adp1_triple_essentiality__REPORT.md"]
---
# Continuous versus binary predictors of gene essentiality

This page compares three predictors of knockout essentiality in *Acinetobacter baylyi* ADP1: continuous fitness, aggregated essentiality fraction and protein expression level. All evidence comes from one organism and one project ([[summaries/adp1_triple_essentiality__REPORT]]), scored by ROC (receiver operating characteristic) AUC (area under curve). Continuous measures (fitness and proteomics, AUC 0.700–0.743) beat the aggregated essentiality fraction, which scored below 0.5. [src: adp1_triple_essentiality]

## Continuous fitness versus essentiality fraction

Inverted fitness predicted essentiality far better than essentiality fraction, which performed worse than random. [src: adp1_triple_essentiality] Fitness was multiplied by -1 because negative fitness indicates a defect, so higher inverted fitness should predict essentiality. [src: adp1_triple_essentiality]

| Predictor | Medium | ROC AUC | Genes |
|---|---|---|---|
| Fitness (inverted) | Rich | 0.700 | 1,933 [src: adp1_triple_essentiality] |
| Fitness (inverted) | Minimal | 0.725 | 2,011 [src: adp1_triple_essentiality] |
| Essentiality fraction | Rich | 0.344 | 1,933 [src: adp1_triple_essentiality] |
| Essentiality fraction | Minimal | 0.403 | 2,011 [src: adp1_triple_essentiality] |

The report names fitness the best TnSeq (transposon sequencing) predictor in both media. [src: adp1_triple_essentiality] It defines essentiality fraction as the fraction of conditions with a fitness defect, aggregated across conditions. [src: adp1_triple_essentiality] Its proposed explanations are hypotheses rather than tested results. Essentiality fraction may measure something orthogonal to lethality. [src: adp1_triple_essentiality] It may aggregate across too many diverse conditions. [src: adp1_triple_essentiality] Fitness may capture growth cost more directly. [src: adp1_triple_essentiality] The report states that the magnitude of growth cost correlates with lethality better than the fraction of conditions with any defect. [src: adp1_triple_essentiality] It concludes that continuous growth or fitness metrics capture biology that binary classifications miss. [src: adp1_triple_essentiality] It cautions that essentiality fraction mixes diverse conditions and that condition-matched comparisons are more informative. [src: adp1_triple_essentiality] It recommends continuous fitness as the primary TnSeq metric. [src: adp1_triple_essentiality]

## Protein expression

Essential genes were expressed more highly than dispensable genes in minimal-media proteomics. [src: adp1_triple_essentiality] The report describes the proteomics AUC as comparable to fitness. [src: adp1_triple_essentiality] The analysis covered 2,288 genes: 464 essential and 1,824 dispensable. [src: adp1_triple_essentiality] Mean log2 expression was 28.43 ± 2.94 (SD, standard deviation) for essential genes and 25.73 ± 2.96 for dispensable genes. [src: adp1_triple_essentiality] The difference was 2.70 log2 units, or 6.5-fold, with Mann-Whitney p = 9.91×10⁻⁵⁹. [src: adp1_triple_essentiality] Expression correlated with essentiality at Pearson r = 0.345 (p = 5.32×10⁻⁶⁵) and Spearman ρ = 0.338 (p = 3.28×10⁻⁶²). [src: adp1_triple_essentiality] ROC AUC was 0.743, which the report calls fair-to-good. [src: adp1_triple_essentiality] The report summarises this as strong correlation (r=0.35, AUC=0.74). [src: adp1_triple_essentiality]

The report calls proteomics the best overall continuous predictor, alongside fitness, and says it is comparable to fitness (AUC=0.70-0.73) and better than FBA (flux balance analysis; ~60-70% accuracy). [src: adp1_triple_essentiality] The two minimal-medium analyses used different gene sets, so the comparison is not like-for-like: proteomics covers 2,288 genes and fitness covers 2,011 genes. [src: adp1_triple_essentiality] The report treats proteomics as independent validation of knockout essentiality and calls it the first integration of proteomics into ADP1 essentiality analysis. [src: adp1_triple_essentiality] Its interpretations are that essential functions need robust expression for viability, that dispensable genes can work at lower expression, and that expression reflects functional importance independent of growth or fitness. [src: adp1_triple_essentiality]

## Open Directions

- Recompute essentiality fraction using only conditions matched to the medium of the essentiality call. This would test whether mixing diverse conditions explains its AUC below 0.5.
- Score fitness and proteomics on the same gene set in minimal medium. This would make their AUC comparison like-for-like.
- Repeat the comparison in other organisms to test whether the ranking holds beyond ADP1.
