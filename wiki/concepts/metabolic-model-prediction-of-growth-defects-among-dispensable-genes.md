---
type: "Concept"
description: "Whether FBA class or flux predicts quantitative mutant growth defects among genes dispensable by TnSeq, including threshold sensitivity and per-carbon-source correlations; stops at lethality calls."
sources: ["summaries/adp1_triple_essentiality__REPORT.md"]
---
# Metabolic model prediction of growth defects among dispensable genes

In Acinetobacter baylyi ADP1, flux balance analysis (FBA) class does not predict growth-defect status among genes that transposon sequencing (TnSeq) shows to be dispensable. [src: adp1_triple_essentiality] The evidence comes from one organism and one project, and it is a null result. The null result held across Q10–Q35 growth-defect thresholds. [src: adp1_triple_essentiality] Correlations between FBA flux and measured mutant growth are weak, with ρ from -0.26 to +0.25. [src: adp1_triple_essentiality] The report says FBA cannot predict growth-rate variation within dispensable genes. [src: adp1_triple_essentiality] The page stops at lethality calls. See also [[summaries/adp1_triple_essentiality__REPORT]] and [[concepts/condition-specific-fitness-correlation-across-carbon-sources]].

## Main null result

All 478 ADP1 genes that have TnSeq, FBA and growth data are TnSeq-dispensable on minimal media. The analysis therefore tests growth effects among dispensable genes only. [src: adp1_triple_essentiality] Among these genes, FBA class was not significantly associated with growth-defect status (chi-squared = 0.93, p = 0.63, 2 df). [src: adp1_triple_essentiality] FBA essentiality class does not capture mutant growth defects (p=0.63). [src: adp1_triple_essentiality] A Kruskal-Wallis test on mean growth rates was also non-significant (H = 1.67, p = 0.43). [src: adp1_triple_essentiality]

Defect rates were nearly the same in every class, about 70-73%. [src: adp1_triple_essentiality]

| FBA class | Genes with growth defects |
|---|---|
| FBA-essential | 73.1% (57/78) [src: adp1_triple_essentiality] |
| FBA-variable | 73.5% (150/204) [src: adp1_triple_essentiality] |
| FBA-blocked | 69.4% (136/196) [src: adp1_triple_essentiality] |

The 78 FBA-essential genes are the "discordant" ones, because all 478 genes are TnSeq-dispensable. [src: adp1_triple_essentiality] Of these, 57/78 (73%) show defects, which matches the 72% background rate across all 478 genes. [src: adp1_triple_essentiality] The other 21/78 (27%) grew normally, which the report calls FBA over-prediction. [src: adp1_triple_essentiality] Among FBA-blocked genes, 136/196 (69%) show defects, which the report calls under-prediction. [src: adp1_triple_essentiality] The other 60/196 (31%) grew normally, consistent with FBA. [src: adp1_triple_essentiality] Because defect rates are uniform across classes, growth measurements do not differentially validate FBA-essential versus FBA-blocked predictions. [src: adp1_triple_essentiality]

## Threshold sensitivity

The null result does not depend on the Q25 threshold, which is the standard choice. [src: adp1_triple_essentiality] The report states that it holds from Q10 to Q35. [src: adp1_triple_essentiality] The table gives the percentage of genes with a defect overall and by FBA class, plus the chi-squared p-value.

| Threshold | All | Essential | Variable | Blocked | p |
|---|---|---|---|---|---|
| Q10 | 41% | 41% | 42% | 41% | 0.985 [src: adp1_triple_essentiality] |
| Q15 | 56% | 55% | 57% | 55% | 0.887 [src: adp1_triple_essentiality] |
| Q20 | 65% | 65% | 68% | 62% | 0.405 [src: adp1_triple_essentiality] |
| Q25 | 72% | 73% | 74% | 69% | 0.629 [src: adp1_triple_essentiality] |
| Q30 | 77% | 79% | 79% | 73% | 0.313 [src: adp1_triple_essentiality] |
| Q35 | 82% | 85% | 85% | 77% | 0.058 [src: adp1_triple_essentiality] |
| Q40 | 85% | 90% | 88% | 81% | 0.048 [src: adp1_triple_essentiality] |

Only at Q40 did a marginal association appear. The report attributes it to a slight divergence between FBA-essential and FBA-blocked defect rates (90% vs 81%). [src: adp1_triple_essentiality]

The high background rate is partly built into the design. Q25 flags about 25% of genes per condition, so aggregating "any defect" over 8 conditions gives an expected 90% if conditions were independent (1 − 0.75⁸). The observed 72% reflects positive inter-condition correlation. [src: adp1_triple_essentiality]

## Per-carbon-source flux correlations

Correlations between FBA flux and measured mutant growth are weak overall (ρ = -0.26 to +0.25). [src: adp1_triple_essentiality] The table gives Spearman ρ for each carbon source.

| Carbon source | n genes | ρ | p |
|---|---|---|---|
| Glucose | 387 | -0.021 | 0.677 [src: adp1_triple_essentiality] |
| Acetate | 352 | -0.153 | 0.004 [src: adp1_triple_essentiality] |
| Asparagine | 286 | -0.257 | <0.001 [src: adp1_triple_essentiality] |
| Butanediol | 137 | -0.145 | 0.092 [src: adp1_triple_essentiality] |
| Glucarate | 127 | +0.246 | 0.005 [src: adp1_triple_essentiality] |
| Lactate | 135 | -0.160 | 0.065 [src: adp1_triple_essentiality] |

Asparagine is the strongest correlation. The report calls its negative sign biologically expected, because higher flux through a gene should mean a larger growth effect when the gene is deleted. [src: adp1_triple_essentiality] Glucarate is positive, opposite to prediction. The report suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]

## Interpretation

Among dispensable genes, mutant growth rates range from 10% to 100% of wild-type. [src: adp1_triple_essentiality] FBA classifies a gene with 95% wild-type growth and one with 5% as both dispensable and cannot tell them apart. [src: adp1_triple_essentiality] The report says FBA provides no growth-rate information within the non-lethal space. [src: adp1_triple_essentiality] It attributes the variation to condition-specific pathway usage rather than core essentiality. [src: adp1_triple_essentiality] This is the report's explanation, not a tested result. For dispensable genes it recommends growth assays on specific carbon sources instead of FBA. [src: adp1_triple_essentiality] It also states that growth measurements do not validate FBA predictions as a tie-breaker and carry independent information. [src: adp1_triple_essentiality]

The report proposes two follow-ups. One is to use continuous FBA flux instead of binary essentiality class, with linear or rank regression against growth rate, which may capture quantitative growth effects. [src: adp1_triple_essentiality] The other is to run condition-specific FBA simulations that match each growth assay's carbon source, to test whether per-condition predictions improve. [src: adp1_triple_essentiality]

## Open Directions

- Regress continuous FBA flux against growth rate rather than using binary essentiality class, to see whether quantitative effects appear.
- Run FBA simulations whose carbon source matches each growth assay, and test whether per-condition predictions improve.
- Examine the glucarate model, where the sign was opposite to prediction, to find the source of the condition-specific error.
- Repeat the class-versus-defect test in organisms where genes span essential and dispensable classes, to check whether the null result is specific to ADP1's all-dispensable set.
