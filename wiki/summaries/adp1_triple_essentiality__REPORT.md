---
type: "Summary"
description: "Summary of the project Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1."
doc_type: "short"
full_text: "sources/adp1_triple_essentiality__REPORT.md"
---
# Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1

This report asks how well flux balance analysis (FBA), random barcode transposon sequencing (RB-TnSeq), knockout phenotypes, mutant growth rates and proteomics agree as predictors of gene essentiality in *Acinetobacter baylyi* ADP1. [src: adp1_triple_essentiality] Its main answer is that the methods capture different biology: FBA agrees moderately with knockout essentiality but does not predict growth defects among TnSeq-dispensable genes, and TnSeq measures fitness cost rather than lethality. [src: adp1_triple_essentiality] All results concern this one organism, and several are clear null results from statistical tests. The report includes an original study (Dehal, 2026-02-18) that asks whether FBA predicts growth defects among TnSeq-dispensable genes. [src: adp1_triple_essentiality] It also reports a refined analysis. [src: adp1_triple_essentiality]

## Key Findings

### Predictors of essentiality

Continuous measures predict knockout essentiality better than binary ones. Fitness is the best predictor in the report's summary (AUC=0.70-0.73, where AUC is area under curve), and binary essentiality_fraction is worse than random (AUC<0.5). [src: adp1_triple_essentiality] In the refined study, inverted fitness gave ROC AUC 0.700 in rich media across 1,933 genes. [src: adp1_triple_essentiality] Log2 proteomics gave ROC AUC 0.743 in minimal media across 2,288 genes, the best overall continuous predictor. [src: adp1_triple_essentiality] Essentiality fraction gave 0.403 in minimal media across 2,011 genes. [src: adp1_triple_essentiality] The report also states that proteomics correlates with essentiality (r=0.35, AUC=0.74) and treats it as independent validation of knockout essentiality. [src: adp1_triple_essentiality] It recommends continuous fitness scores over binary classifications for TnSeq analysis. [src: adp1_triple_essentiality]

### TnSeq versus knockouts

RB-TnSeq systematically disagrees with knockout experiments (κ<0 across all thresholds). The report attributes this to TnSeq measuring fitness cost rather than lethality. [src: adp1_triple_essentiality] At the optimal threshold, TnSeq catches only 7.9% (18/229) of knockout-essential genes. [src: adp1_triple_essentiality] In addition, 293 knockout-dispensable genes are TnSeq-essential, which the report calls fitness-important but not lethal. [src: adp1_triple_essentiality] In the refined study this category is 15.2% of genes, with mean fitness -0.34 (SD 0.66). [src: adp1_triple_essentiality] The both-essential category has 18 genes (0.9%) and mean fitness -1.18 (SD 1.49). [src: adp1_triple_essentiality] The report hypothesizes that knockout-essential, TnSeq-dispensable genes tolerate partial function from transposon-disrupted alleles. [src: adp1_triple_essentiality] It also notes that transposon insertion is not the same as gene deletion. [src: adp1_triple_essentiality]

### FBA and growth defects

FBA shows moderate concordance with experimental knockout essentiality (κ≈0.49, F1≈0.62-0.67). [src: adp1_triple_essentiality] Among 478 triple-covered, TnSeq-dispensable genes, however, FBA class is not significantly associated with growth defects (chi-squared = 0.93, p = 0.63, 2 df). [src: adp1_triple_essentiality] Defect rates are 73.1% (57/78) for FBA-essential genes and 69.4% (136/196) for FBA-blocked genes. [src: adp1_triple_essentiality] The FBA-essential rate matches the 72% background across all 478 genes. [src: adp1_triple_essentiality] The report concludes that growth measurements do not differentially validate FBA-essential versus FBA-blocked predictions. [src: adp1_triple_essentiality]

The null result is robust across Q10–Q35 thresholds. [src: adp1_triple_essentiality] The list gives the overall defect rate, then the essential/variable/blocked rates and the chi-squared p-value.

- Q10: 41% (41%/42%/41%), p = 0.985 [src: adp1_triple_essentiality]
- Q20: 65% (65%/68%/62%), p = 0.405 [src: adp1_triple_essentiality]
- Q30: 77% (79%/79%/73%), p = 0.313 [src: adp1_triple_essentiality]
- Q35: 82% (85%/85%/77%), p = 0.058 [src: adp1_triple_essentiality]

Only at Q40 did a marginal association appear (p = 0.048), driven by FBA-essential versus FBA-blocked defect rates of 90% versus 81%. [src: adp1_triple_essentiality] Growth measurements therefore provide independent information and do not act as a tie-breaker for FBA. [src: adp1_triple_essentiality]

### Condition-specific growth

Growth importance is condition-dependent and continuous, and neither FBA class nor TnSeq essentiality captures this variation. [src: adp1_triple_essentiality] Of 478 genes, 333 (70%) had condition-specific growth defects and 135 (28%) had no defect on any condition. [src: adp1_triple_essentiality]

FBA flux correlates only weakly with measured mutant growth. Acetate shows a weak negative correlation (n = 352, ρ = -0.153, p = 0.004). [src: adp1_triple_essentiality] Butanediol (n = 137, ρ = -0.145, p = 0.092) and lactate (n = 135, ρ = -0.160, p = 0.065) are non-significant weak trends. [src: adp1_triple_essentiality] Glucarate has a positive correlation (ρ = +0.246), opposite to prediction, which suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]

### Where the model fails

Aromatic degradation genes are enriched among FBA-discordant genes (OR=9.7, odds ratio), which the report reads as systematic model gaps. [src: adp1_triple_essentiality] Nine of 11 aromatic degradation genes are discordant, including the beta-ketoadipate pathway enzymes 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase. [src: adp1_triple_essentiality] Almost all are FBA-under-predicted: the model assigns zero flux, yet deletion impairs growth. [src: adp1_triple_essentiality] Lipid metabolism is depleted among discordant genes (OR = 0.34, q = 0.042), which the report suggests means FBA handles lipid pathways better than aromatic catabolism. [src: adp1_triple_essentiality] Pangenome status was not enriched in discordant genes (Fisher OR = 0.89, p = 0.80). [src: adp1_triple_essentiality]

## Executive Summary; Part I: Original Triple Essentiality Study

This part of the report covers the executive summary and the original study. The original study asks whether flux balance analysis (FBA) predicts growth defects among transposon sequencing (TnSeq)-dispensable *Acinetobacter baylyi* ADP1 genes. Its main result is that FBA class was not significantly associated with growth-defect status (p = 0.63). [src: adp1_triple_essentiality]

### Scope and the two studies

The report compares FBA, random barcode transposon sequencing (RB-TnSeq), knockout phenotypes, mutant growth rates and proteomics as predictors of gene essentiality in ADP1. [src: adp1_triple_essentiality] The original study (Dehal, 2026-02-18) asks whether FBA predicts growth defects among TnSeq-dispensable genes. It also asks whether growth measurements resolve FBA–TnSeq disagreements. [src: adp1_triple_essentiality] The refined study (Henry, 2026-02-19) compares FBA, RB-TnSeq at multiple thresholds, knockout experiments and proteomics across rich and minimal media. [src: adp1_triple_essentiality]

The report's headline conclusions cover both studies:
- Continuous fitness is the best predictor of essentiality (AUC=0.70-0.73, where AUC is area under curve). It outperforms binary essentiality_fraction (AUC<0.5). [src: adp1_triple_essentiality] See [[concepts/continuous-versus-binary-predictors-of-gene-essentiality]].
- FBA shows moderate concordance with experimental knockouts (κ≈0.49, F1≈0.62-0.67). [src: adp1_triple_essentiality]
- RB-TnSeq disagrees systematically with knockout experiments (κ<0 across all thresholds). The report attributes this to RB-TnSeq measuring fitness cost rather than lethality. [src: adp1_triple_essentiality]
- Proteomics correlates with essentiality (r=0.35, AUC=0.74). Essential genes are expressed 6.5-fold higher. [src: adp1_triple_essentiality]
- Aromatic degradation genes are enriched among FBA-discordant genes (OR=9.7, where OR is odds ratio). The report reads this as systematic model gaps. [src: adp1_triple_essentiality]
- The report argues that each method measures different biology: FBA measures metabolic necessity, knockouts measure lethality, TnSeq measures fitness cost, proteomics indicates expression requirement, and growth measurements capture condition-specific optimization. [src: adp1_triple_essentiality]

### Data and design of the original study

The original analysis used these inputs:
- Binary TnSeq essentiality calls from Fitness Browser in minimal media. [src: adp1_triple_essentiality]
- Essential, variable or blocked FBA predictions from a ModelSEED metabolic model in minimal media. [src: adp1_triple_essentiality]
- Deletion mutant growth on 8 carbon sources (glucose, acetate, asparagine, butanediol, glucarate, lactate, pyruvate, succinate) from de Berardinis et al. (2008). [src: adp1_triple_essentiality]
- Gene annotations from COG categories (clusters of orthologous groups), KEGG pathways, RAST functions and pangenome cluster assignments. [src: adp1_triple_essentiality]
- Per-condition FBA flux from the gene_phenotypes table for 6 matched carbon sources. [src: adp1_triple_essentiality]

Its methods were:
- Growth defects were defined as the 25th percentile (Q25) per condition. [src: adp1_triple_essentiality]
- FBA class versus growth defect was tested with chi-squared and Kruskal-Wallis tests. [src: adp1_triple_essentiality]
- Condition-specific FBA flux was correlated with growth rate using Spearman correlations. [src: adp1_triple_essentiality]
- Discordant genes were characterized with Fisher's exact test and BH-FDR (Benjamini-Hochberg false discovery rate). [src: adp1_triple_essentiality]

A structural limit applies to everything below. All 478 genes with TnSeq, FBA and growth data are TnSeq-dispensable on minimal media. [src: adp1_triple_essentiality] This is expected, because TnSeq-essential genes have no viable deletion mutants and so have no growth rates. [src: adp1_triple_essentiality] The analysis therefore tests growth effects among dispensable genes only.

### FBA class and growth defects

Among the 478 triple-covered genes, FBA class was not significantly associated with growth defect status (chi-squared = 0.93, p = 0.63, 2 df). [src: adp1_triple_essentiality] Defect rates were similar across classes:

| FBA class | Genes with growth defects |
|---|---|
| Essential | 73.1% (57/78) [src: adp1_triple_essentiality] |
| Variable | 73.5% (150/204) [src: adp1_triple_essentiality] |
| Blocked | 69.4% (136/196) [src: adp1_triple_essentiality] |

The Kruskal-Wallis test on mean growth rates was also non-significant (H = 1.67, p = 0.43). [src: adp1_triple_essentiality]

### Threshold sensitivity

The sensitivity analysis shows no significant association at Q10 to Q35, and only a marginal one at Q40. [src: adp1_triple_essentiality] The table gives the share of genes with defects overall, then for FBA-essential, variable and blocked genes, then the chi-squared p-value.

| Threshold | All | Essential | Variable | Blocked | p |
|---|---|---|---|---|---|
| Q10 | 41% | 41% | 42% | 41% | 0.985 [src: adp1_triple_essentiality] |
| Q15 | 56% | 55% | 57% | 55% | 0.887 [src: adp1_triple_essentiality] |
| Q20 | 65% | 65% | 68% | 62% | 0.405 [src: adp1_triple_essentiality] |
| Q25 | 72% | 73% | 74% | 69% | 0.629 [src: adp1_triple_essentiality] |
| Q30 | 77% | 79% | 79% | 73% | 0.313 [src: adp1_triple_essentiality] |
| Q35 | 82% | 85% | 85% | 77% | 0.058 [src: adp1_triple_essentiality] |
| Q40 | 85% | 90% | 88% | 81% | 0.048 [src: adp1_triple_essentiality] |

The report attributes the Q40 result to a slight divergence between FBA-essential and FBA-blocked defect rates (90% vs 81%). [src: adp1_triple_essentiality]

### Discordant genes

Since all 478 genes are TnSeq-dispensable, the discordant genes are the 78 FBA-essential ones. [src: adp1_triple_essentiality] Of these, 57/78 (73%) showed growth defects, which matches the background rate of 72% of all 478 genes. [src: adp1_triple_essentiality] The other 21/78 (27%) grew normally, which the report calls FBA over-prediction. [src: adp1_triple_essentiality]

FBA-blocked genes have zero predicted flux (n=196). [src: adp1_triple_essentiality] Of these, 136/196 (69%) showed growth defects, which the report calls FBA under-prediction. [src: adp1_triple_essentiality] The other 60/196 (31%) grew normally, consistent with FBA. [src: adp1_triple_essentiality] Growth measurements therefore do not differentially validate FBA-essential versus FBA-blocked predictions, because the defect rate is uniform across FBA classes. [src: adp1_triple_essentiality] See [[concepts/metabolic-model-prediction-of-growth-defects-among-dispensable-genes]].

### Condition-specific flux versus growth

Across carbon sources, the correlations between FBA flux and measured mutant growth are weak and vary in sign. [src: adp1_triple_essentiality]

| Carbon source | n genes | Spearman ρ | p |
|---|---|---|---|
| Glucose | 387 | -0.021 | 0.677 [src: adp1_triple_essentiality] |
| Acetate | 352 | -0.153 | 0.004 [src: adp1_triple_essentiality] |
| Asparagine | 286 | -0.257 | <0.001 [src: adp1_triple_essentiality] |
| Butanediol | 137 | -0.145 | 0.092 [src: adp1_triple_essentiality] |
| Glucarate | 127 | +0.246 | 0.005 [src: adp1_triple_essentiality] |
| Lactate | 135 | -0.160 | 0.065 [src: adp1_triple_essentiality] |

Glucose shows no correlation. Butanediol and lactate show non-significant weak trends. [src: adp1_triple_essentiality] Asparagine gave the strongest correlation. The report calls its negative direction biologically expected, since higher FBA flux through a gene implies a greater growth impact when the gene is deleted. [src: adp1_triple_essentiality] Glucarate was positive, opposite to prediction. The report suggests this reflects condition-specific model inaccuracies. [src: adp1_triple_essentiality]

### Breadth of growth defects

Of the 478 genes, 333 (70%) showed condition-specific growth defects, meaning defects on some but not all conditions. [src: adp1_triple_essentiality] Only 10 (2%) had defects across all 8 conditions. [src: adp1_triple_essentiality]

## Part I: Original Triple Essentiality Study; Part II: Refined Comprehensive Analysis

The original study covered only TnSeq-dispensable genes (n=478) with a single binary TnSeq classification. [src: adp1_triple_essentiality] It set TnSeq, FBA and growth measurements side by side as methods that measure different aspects of gene function. [src: adp1_triple_essentiality] The refined study covered all genes (n=5,852) and asked how FBA, RB-TnSeq and proteomics agree with experimental knockout truth. [src: adp1_triple_essentiality]

In the original study, 333 of 478 genes (70%) had condition-specific growth defects. [src: adp1_triple_essentiality] FBA did not predict growth defects among TnSeq-dispensable genes (p = 0.63). [src: adp1_triple_essentiality] In the refined study, no RB-TnSeq threshold gave positive kappa. [src: adp1_triple_essentiality] Of the genes compared, 211 (10.9%) were knockout-essential but TnSeq-dispensable, and 293 (15.2%) were knockout-dispensable but TnSeq-essential. [src: adp1_triple_essentiality]

### Part I: Original study

**Growth defects are widespread and condition-specific.** Of 478 genes, 333 (70%) had defects on some but not all conditions, 10 (2%) had defects on all 8, and 135 (28%) had none. [src: adp1_triple_essentiality] Mean pairwise defect correlation across conditions was 0.38 (range: -0.03 to 1.0), which indicates moderate but incomplete overlap in the genes needed on different carbon sources. [src: adp1_triple_essentiality] One caveat applies: the Q25 threshold flags about 25% of genes per condition. Aggregating "any defect" across 8 conditions therefore gives a high background rate by design. Independence would predict 1 − 0.75⁸ = 90%, and the observed rate was 72%. [src: adp1_triple_essentiality]

**FBA does not predict growth defects.** Among TnSeq-dispensable genes, FBA did not predict growth defects (p = 0.63), and the null result held across Q10–Q35 thresholds. [src: adp1_triple_essentiality] Defect rates were uniform (~70-73%) across all FBA classes. [src: adp1_triple_essentiality] The report concludes that growth measurements do not validate FBA predictions as a tie-breaker. It says the three methods capture different biology and that growth data carry independent information. [src: adp1_triple_essentiality] It describes TnSeq as measuring lethal or severe fitness impairment, FBA as measuring in-silico flux requirement, and growth measurements as measuring condition-specific growth-rate optimization. [src: adp1_triple_essentiality] It also concludes that growth importance is condition-dependent and continuous, and that neither FBA nor TnSeq captures this. [src: adp1_triple_essentiality] A limit of the original study is that it had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]

**Discordant genes.** Enrichment among the 157 discordant genes used RAST function annotations (100% gene coverage), Fisher's exact test and Benjamini-Hochberg false discovery rate (BH-FDR) correction. [src: adp1_triple_essentiality] Two functional categories were significant. [src: adp1_triple_essentiality]

- Aromatic degradation was strongly enriched (OR = 9.70, q = 0.012), and 9 of 11 of its genes were discordant. [src: adp1_triple_essentiality] These genes include the beta-ketoadipate pathway enzymes 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase. [src: adp1_triple_essentiality] The report calls them central to ADP1's well-characterized aromatic catabolism. [src: adp1_triple_essentiality]
- Almost all of these genes were FBA-under-predicted: the model assigned zero flux, yet deletion impaired growth. [src: adp1_triple_essentiality] The directional analysis gave OR = 12.0, q = 0.004. [src: adp1_triple_essentiality]
- The report names aromatic degradation the main source of FBA discordance. It points to the model's environmental assumptions, specifically a lack of aromatic substrates. [src: adp1_triple_essentiality]
- Lipid metabolism was depleted (OR = 0.34, q = 0.042), with only 7 of 46 genes discordant. [src: adp1_triple_essentiality] The report suggests that the FBA model handles lipid pathways better than aromatic catabolism. [src: adp1_triple_essentiality]

Pangenome status was overwhelmingly core across all classes (93–100%). It was not enriched in discordant genes (Fisher OR = 0.89, p = 0.80). [src: adp1_triple_essentiality]

### Part II: Refined analysis

**Design.** The refined study asked how FBA, RB-TnSeq (random barcode transposon sequencing) and proteomics agree with experimental knockout truth across all genes. It also asked what continuous predictors reveal that binary classifications miss. [src: adp1_triple_essentiality] It covered all genes (n=5,852), including TnSeq-essential ones, and used RB-TnSeq thresholds 0.01, 0.025, 0.05, 0.10 and 0.20. [src: adp1_triple_essentiality] Ground truth came from de Berardinis et al. (2008). [src: adp1_triple_essentiality] The rich-media (LB) set tested 2,953 genes (346 essential, 2,607 dispensable). [src: adp1_triple_essentiality] The minimal-media set tested 3,092 genes (499 essential). [src: adp1_triple_essentiality] Proteomics added average log2 expression across 7 *Acinetobacter* strains for 2,383 genes from the KBase Data Lakehouse. [src: adp1_triple_essentiality] This tested the hypothesis that essential genes require robust expression. [src: adp1_triple_essentiality] The analysis used ROC (receiver operating characteristic) curves for fitness, essentiality_fraction and proteomics expression. It also used Pearson and Spearman correlations, Mann-Whitney U tests, and AUC (area under curve). [src: adp1_triple_essentiality]

**TnSeq and knockout calls disagree.** None of the 5 thresholds gave positive kappa, so threshold choice did not resolve the discordance. [src: adp1_triple_essentiality] The essentiality_fraction distribution had mean=0.026 and median=0.0. [src: adp1_triple_essentiality] Knockout versus TnSeq classes were:

| Class | Genes |
|---|---|
| Both essential | 18 (0.9%) [src: adp1_triple_essentiality] |
| Both dispensable | 1,411 (73.0%) [src: adp1_triple_essentiality] |
| Knockout essential, TnSeq dispensable (false negatives) | 211 (10.9%) [src: adp1_triple_essentiality] |
| Knockout dispensable, TnSeq essential (false positives) | 293 (15.2%) [src: adp1_triple_essentiality] |

The study also characterized mean essentiality_fraction and fitness for each discordance category. [src: adp1_triple_essentiality]

**Predictor performance.** FBA performed better in minimal media (F1=0.67) than rich media (F1=0.62). The report tentatively attributes this to tighter metabolic constraints. [src: adp1_triple_essentiality] Inverted fitness predicted essentiality much better (AUC=0.70-0.73) than essentiality_fraction (AUC=0.34-0.40), which performed worse than random. [src: adp1_triple_essentiality]

## Part II: Refined Comprehensive Analysis: Results

This part of the report refines the *Acinetobacter baylyi* ADP1 analysis. It uses knockout (KO) essentiality as ground truth and scores flux balance analysis (FBA), random barcode transposon sequencing (RB-TnSeq) and proteomics against it, in rich and minimal media. FBA agrees moderately with knockouts, RB-TnSeq agrees poorly, and proteomics and fitness are the best continuous predictors. [src: adp1_triple_essentiality]

### Inputs and statistical methods

Rich-media inputs were FBA `rich_media_class` for 866 genes and ground-truth `essentiality_lb` for 2,953 genes (346 essential, 2,607 dispensable). The RB-TnSeq signal was continuous fitness, inverted for ROC (receiver operating characteristic) analysis. [src: adp1_triple_essentiality]

Minimal-media inputs were FBA `minimal_media_class` for 866 genes and a merged ground truth of 3,092 genes, 499 of them essential. The merge prioritized `essentiality_minimal` and fell back to `essentiality_lb`. RB-TnSeq used `essentiality_fraction` plus fitness-based classification. [src: adp1_triple_essentiality]

The methods were:
- Binary concordance: confusion matrices, sensitivity, specificity, precision, F1 and Cohen's kappa. [src: adp1_triple_essentiality]
- Continuous correlation: Pearson r and Spearman ρ. [src: adp1_triple_essentiality]
- Group comparison: Mann-Whitney U test of expression, essential versus dispensable genes. [src: adp1_triple_essentiality]
- ROC area under the curve (AUC) for continuous predictors. [src: adp1_triple_essentiality]
- Discordant genes, broken down by concordance category with mean metrics. [src: adp1_triple_essentiality]

### FBA against knockouts

FBA showed moderate agreement with knockout lethality in both media, and minimal media scored slightly better. [src: adp1_triple_essentiality]

- Rich media (N = 724 genes): recall 60.8%, precision 64.0%, F1 0.624, Cohen's kappa 0.486 (moderate). [src: adp1_triple_essentiality]
- Minimal media (N = 833 genes): recall 65.6%, precision 69.2%, F1 0.673, Cohen's kappa 0.493 (moderate). [src: adp1_triple_essentiality]

This differs from the original study, which found that FBA did not predict growth defects among TnSeq-dispensable genes (p=0.63). The refined study found moderate concordance with knockout lethality (κ≈0.49). [src: adp1_triple_essentiality] The report adds that FBA still cannot predict growth-rate variation within dispensable genes. [src: adp1_triple_essentiality]

### RB-TnSeq against knockouts

RB-TnSeq agreed poorly with knockout essentiality at every threshold tested in rich media (N=1,933 genes). F1 peaked at 0.077 at threshold 0.025. [src: adp1_triple_essentiality]

- Threshold 0.01: recall 18.8%, precision 4.8%, F1 0.076, kappa -0.139. [src: adp1_triple_essentiality]
- Threshold 0.025: recall 15.3%, precision 5.1%, F1 0.077, kappa -0.122. [src: adp1_triple_essentiality]
- Threshold 0.05: recall 7.9%, precision 5.8%, F1 0.067, kappa -0.081. [src: adp1_triple_essentiality]
- Threshold 0.10: recall 2.6%, precision 7.5%, F1 0.039, kappa -0.024. [src: adp1_triple_essentiality]
- Threshold 0.20: recall 0.4%, precision 4.3%, F1 0.008, kappa -0.014. [src: adp1_triple_essentiality]

All kappas were negative. The report reads this as systematic disagreement worse than random chance. [src: adp1_triple_essentiality]

At cutoff=0.05, the two methods agreed on dispensable genes but overlapped little on essential genes (only 18/229 agreement):
- Both essential: 18 genes (0.9%). [src: adp1_triple_essentiality]
- Both dispensable: 1,411 genes (73.0%). [src: adp1_triple_essentiality]
- KO-essential but TnSeq-dispensable (false negatives): 211 genes (10.9%). [src: adp1_triple_essentiality]
- KO-dispensable but TnSeq-essential (false positives): 293 genes (15.2%). [src: adp1_triple_essentiality]

The report proposes that RB-TnSeq captures different biology from complete deletion, because transposon insertion is not gene deletion. [src: adp1_triple_essentiality] It suggests the 211 false negatives tolerate partial function from transposon-disrupted genes. [src: adp1_triple_essentiality] It suggests the 293 false positives may be fitness-important but not lethal. [src: adp1_triple_essentiality] See [[concepts/limits-of-transposon-based-essentiality-calls]].

The report links this to the original study, which analyzed only TnSeq-dispensable genes (n=478). Among KO-essential genes, only 7.9% (18/229) were caught by TnSeq at the optimal threshold. The report therefore calls the original constraint limiting, because TnSeq misses most truly essential genes. [src: adp1_triple_essentiality]

### Proteomics and expression

In minimal media (N=2,288 genes), essential genes had higher protein expression than dispensable genes. The report presents this as independent validation of essentiality, and it was absent from the original study. [src: adp1_triple_essentiality]

- Essential genes (n=464) had mean log2 expression 28.43 ± 2.94. [src: adp1_triple_essentiality]
- Dispensable genes (n=1,824) had mean log2 expression 25.73 ± 2.96. [src: adp1_triple_essentiality]
- The difference was 2.70 log2 units, or 6.5-fold, with Mann-Whitney U p = 9.91×10⁻⁵⁹. [src: adp1_triple_essentiality]
- Expression correlated positively with essentiality: Pearson r = 0.345 (p = 5.32×10⁻⁶⁵) and Spearman ρ = 0.338 (p = 3.28×10⁻⁶²). [src: adp1_triple_essentiality]
- The ROC AUC was 0.743, called fair-to-good. [src: adp1_triple_essentiality]

### Continuous predictors compared

Inverted fitness and proteomics were the best continuous predictors. The essentiality fraction scored below 0.5. [src: adp1_triple_essentiality]

- Fitness (inverted), rich media: AUC 0.700, fair, best predictor. [src: adp1_triple_essentiality]
- Fitness (inverted), minimal media: AUC 0.725, fair, best predictor. [src: adp1_triple_essentiality]
- Proteomics (log2), minimal media: AUC 0.743, fair to very good. [src: adp1_triple_essentiality]
- Essentiality fraction, rich media: AUC 0.344, worse than random. [src: adp1_triple_essentiality]
- Essentiality fraction, minimal media: AUC 0.403, worse than random. [src: adp1_triple_essentiality]

The report names fitness the best TnSeq predictor across both media (AUC=0.70-0.73). [src: adp1_triple_essentiality] See [[concepts/continuous-versus-binary-predictors-of-gene-essentiality]].

## Part II: Refined Comprehensive Analysis; Integrated Discussion

This part of the report integrates the original and refined studies of [[entities/acinetobacter-baylyi-adp1]]. It argues that different experimental methods measure different aspects of gene importance, and it describes five distinct biological phenomena. [src: adp1_triple_essentiality] Both studies show that continuous growth or fitness metrics capture biology that binary classifications miss. [src: adp1_triple_essentiality] The explanations below are the report's interpretations of its analyses, not new direct measurements.

### Five phenomena

The original study used mutant growth rates on 8 carbon sources as a continuous predictor. The refined study uses fitness from TnSeq (transposon sequencing) data. [src: adp1_triple_essentiality]

| Phenomenon | Measured by | Biology |
|---|---|---|
| Lethality | Complete gene deletion and viable colony formation; a binary outcome [src: adp1_triple_essentiality] | Absolute requirement for cellular viability, for example DNA replication, cell division and core metabolic pathways [src: adp1_triple_essentiality] |
| Metabolic necessity | In silico FBA (flux balance analysis); asks whether flux through the gene is required for growth in defined media [src: adp1_triple_essentiality] | Metabolic network requirement given environmental constraints [src: adp1_triple_essentiality] |
| Fitness cost | Transposon-insertion fitness and mutant growth rates; a continuous outcome [src: adp1_triple_essentiality] | Growth-rate optimization and competitive fitness [src: adp1_triple_essentiality] |
| Protein expression | Protein abundance across strains or conditions; a continuous outcome [src: adp1_triple_essentiality] | How highly a gene is expressed [src: adp1_triple_essentiality] |
| Condition-specific growth | Growth rate on specific substrates [src: adp1_triple_essentiality] | Metabolic pathway usage varies by substrate [src: adp1_triple_essentiality] |

The report stresses that fitness cost is not lethality, because many genes impose a fitness cost without being lethal. [src: adp1_triple_essentiality] Proteomics reaches AUC (area under curve) = 0.74, with essential genes showing 6.5-fold higher expression. The report calls it the best continuous predictor alongside fitness. [src: adp1_triple_essentiality] For mutant growth, 70% of genes show condition-specific growth defects. [src: adp1_triple_essentiality] Correlations with FBA flux are weak (ρ = -0.26 to +0.25). [src: adp1_triple_essentiality] FBA essentiality class does not capture these growth defects (p=0.63). [src: adp1_triple_essentiality]

### Why TnSeq and knockouts disagree

The refined study reports systematic discordance (κ<0) between TnSeq and knockout experiments. [src: adp1_triple_essentiality] The report offers two mechanisms.

First, the two methods perturb the gene differently. KO deletion removes the gene completely and yields zero protein. [src: adp1_triple_essentiality] A TnSeq insertion may still allow partial or truncated protein, read-through transcription, or functional domains upstream of the insertion. [src: adp1_triple_essentiality] The report explains the 211 KO-essential/TnSeq-dispensable genes (mean essentiality_fraction = 0.0034) this way: partial function suffices. [src: adp1_triple_essentiality]

Second, the conditions differ. KO experiments use defined LB or minimal media. [src: adp1_triple_essentiality] Fitness Browser TnSeq spans diverse conditions across many studies. [src: adp1_triple_essentiality] Essentiality_fraction aggregates across conditions. [src: adp1_triple_essentiality] A gene can therefore be essential under KO conditions but dispensable in most TnSeq conditions. That gives a low essentiality_fraction despite high lethality. [src: adp1_triple_essentiality]

The report also says that essentiality fraction measures the fraction of conditions with a fitness defect. [src: adp1_triple_essentiality] Fitness measures the growth-rate cost of disruption. [src: adp1_triple_essentiality] KO essentiality asks whether the organism can survive without the gene. [src: adp1_triple_essentiality] Many genes cause slower growth without being lethal. The report uses this to explain the 293 KO-dispensable/TnSeq-essential genes (mean essentiality_fraction = 0.10). [src: adp1_triple_essentiality]

### Continuous versus binary predictors

Continuous fitness values (AUC=0.70-0.73) outperform binary essentiality_fraction (AUC=0.34-0.40) for essentiality prediction. [src: adp1_triple_essentiality] Essentiality fraction performs worse than random (AUC<0.5). The report suggests this means it measures something orthogonal to lethality. [src: adp1_triple_essentiality] The report suggests that it aggregates across too many diverse conditions. [src: adp1_triple_essentiality] It also suggests that fitness captures growth cost more directly. [src: adp1_triple_essentiality] Fitness captures the magnitude of growth cost, which correlates with lethality better than the fraction of conditions with any fitness defect. [src: adp1_triple_essentiality]

### Why FBA misses growth defects

The original study found that FBA class does not predict growth defects among TnSeq-dispensable genes (p=0.63). The report says the refined results explain this. [src: adp1_triple_essentiality] It gives these reasons.

- FBA is a threshold classifier. It predicts whether a knockout reduces growth to zero, not the magnitude of the reduction. [src: adp1_triple_essentiality] A gene with 95% wild-type growth and one with 5% are both "dispensable", and FBA cannot distinguish them. [src: adp1_triple_essentiality]
- Among dispensable genes, growth rates vary from 10% to 100% of wild-type. [src: adp1_triple_essentiality] The report attributes this variation to condition-specific pathway usage, not core essentiality. [src: adp1_triple_essentiality]
- FBA's moderate concordance (κ=0.49) applies at the essential/dispensable boundary. [src: adp1_triple_essentiality] There it distinguishes lethal from non-lethal knockouts with ~65% accuracy. [src: adp1_triple_essentiality] Within the non-lethal space, FBA provides no information about growth rate. [src: adp1_triple_essentiality]
- Aromatic degradation genes are systematically under-predicted by FBA. [src: adp1_triple_essentiality] FBA predicts zero flux because minimal media lacks aromatic substrates. [src: adp1_triple_essentiality] The report notes that environmental assumptions, including missing aromatic substrates, limit FBA. [src: adp1_triple_essentiality] Experimental media may contain trace aromatics, or the genes may have moonlighting functions. Either would explain growth defects despite predicted dispensability. [src: adp1_triple_essentiality]

## Integrated Discussion; Integrated Conclusions

This part of the report draws its conclusions from four lines of evidence: aromatic-catabolism discordance with flux balance analysis (FBA), how FBA and transposon sequencing (TnSeq) compare with knockout experiments, proteomics, and condition-specific growth. FBA is moderately concordant with knockouts, while RB-TnSeq disagrees with them systematically. Its main message is that no single method is ground truth and that the methods are complementary. [src: adp1_triple_essentiality]

### Aromatic degradation is mis-modeled by FBA

Almost all of them are FBA-blocked, with zero predicted flux, yet show growth defects. [src: adp1_triple_essentiality] The refined study confirms this under-prediction for genes that are blocked in FBA but KO-essential or associated with growth defects. [src: adp1_triple_essentiality] In contrast, lipid metabolism is well captured by FBA (OR = 0.34). [src: adp1_triple_essentiality]

The case study names 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase as beta-ketoadipate pathway genes. [src: adp1_triple_essentiality] The report notes that ADP1 is renowned for aromatic compound metabolism (Barbe et al. 2004) and that the beta-ketoadipate pathway is a signature feature. [src: adp1_triple_essentiality]

The report explains the discordance by the environment, not the network. The FBA model assumes minimal media without aromatic compounds. [src: adp1_triple_essentiality] Experimental media may contain trace aromatics from yeast extract or agar impurities. [src: adp1_triple_essentiality] The report therefore reads the discordance as a systematic gap in model assumptions, not in network topology. [src: adp1_triple_essentiality] This is an interpretation, not a tested result. The report recommends adding trace aromatics to the media definition and testing whether the discordance resolves. [src: adp1_triple_essentiality]

### FBA and TnSeq against knockout experiments

FBA shows moderate concordance with experimental knockout truth (κ≈0.49, F1≈0.62-0.67). [src: adp1_triple_essentiality] It does better in minimal media (F1=0.67) than in rich media (F1=0.62). [src: adp1_triple_essentiality] FBA does not predict growth defects among TnSeq-dispensable genes (p=0.63). [src: adp1_triple_essentiality] The report says its essentiality predictions need experimental validation. [src: adp1_triple_essentiality]

At the optimal threshold, TnSeq catches only 7.9% (18/229) of KO-essential genes. [src: adp1_triple_essentiality] Also, 211 KO-essential genes are TnSeq-dispensable, which the report reads as tolerance of partial function. [src: adp1_triple_essentiality] And 293 KO-dispensable genes are TnSeq-essential, which it calls fitness-important but not lethal. [src: adp1_triple_essentiality] The report suggests that RB-TnSeq likely measures fitness importance, not lethality, and that transposon insertion is not the same as gene deletion. [src: adp1_triple_essentiality]

Continuous fitness (AUC=0.70-0.73, where AUC is area under curve) beats essentiality_fraction (AUC=0.34-0.40). [src: adp1_triple_essentiality] Essentiality fraction performs worse than random (AUC<0.5). [src: adp1_triple_essentiality] The report recommends continuous fitness values as the primary TnSeq metric. [src: adp1_triple_essentiality]

### Proteomics

In the refined study, essential genes are expressed 6.5-fold higher than dispensable genes (p = 9.91×10⁻⁵⁹). [src: adp1_triple_essentiality] Proteomics correlates with essentiality (r=0.35, AUC=0.74). [src: adp1_triple_essentiality] The report describes this AUC as comparable to fitness (AUC=0.70-0.73) and better than FBA (~60-70% accuracy). [src: adp1_triple_essentiality] It treats proteomics as independent validation of knockout essentiality and as a best continuous predictor alongside fitness. [src: adp1_triple_essentiality] The report claims this is the first integration of proteomics into ADP1 essentiality analysis. It also claims strong support for knockout essentiality as a meaningful biological category. [src: adp1_triple_essentiality]

The report's explanations are interpretive. Essential functions need robust expression for viability, and dispensable genes can work at lower expression. [src: adp1_triple_essentiality] It also holds that expression reflects functional importance independent of growth or fitness. [src: adp1_triple_essentiality]

### Condition-specific growth

In the original study, 70% of genes show condition-specific growth defects, and the mean inter-condition correlation is 0.38. [src: adp1_triple_essentiality] Growth importance is condition-dependent and continuous. [src: adp1_triple_essentiality] Mutant growth rates vary by condition in ways FBA class does not capture. [src: adp1_triple_essentiality] Neither FBA class nor TnSeq essentiality captures this variation. [src: adp1_triple_essentiality]

### What each method measures

The report characterizes each method by what it measures, as below. Its table labels knockouts "ground truth for essentiality" [src: adp1_triple_essentiality], but its own conclusion says no single method is ground truth. [src: adp1_triple_essentiality] It also calls knockouts only the best proxy for lethality. [src: adp1_triple_essentiality] These statements conflict in wording. The more cautious conclusion (best proxy, not ground truth) is the report's stated summary position. [src: adp1_triple_essentiality]

| Method | Measures | Output | Use |
|---|---|---|---|
| KO | Lethality | Binary (lethal/viable) | Labeled "ground truth for essentiality" in the report's table; see the caveat above [src: adp1_triple_essentiality] |
| FBA | Metabolic necessity | Binary (essential/dispensable) | First-pass computational screen [src: adp1_triple_essentiality] |
| TnSeq (fitness) | Growth rate cost | Continuous | Fitness effects, gene importance [src: adp1_triple_essentiality] |
| TnSeq (ess. fraction) | Cross-condition fitness | Continuous (poor for lethality) | Condition-dependent importance [src: adp1_triple_essentiality] |
| Proteomics | Expression requirement | Continuous | Validates essentiality [src: adp1_triple_essentiality] |
| Growth assays | Condition-specific optimization | Continuous per condition | Metabolic pathway usage [src: adp1_triple_essentiality] |

The report says fitness, expression and growth rates reveal additional biology beyond lethality. [src: adp1_triple_essentiality] Integrating complementary methods gives the most complete picture. [src: adp1_triple_essentiality]

## Recommendations; Data Availability

This part of the report gives recommendations and proposed follow-up analyses for [[entities/acinetobacter-baylyi-adp1]] essentiality work. It also names the project's data products. [src: adp1_triple_essentiality]

### Recommendations

The report recommends using flux balance analysis (FBA) as a first-pass computational screen, and it expects about 60-70% accuracy (κ≈0.49). [src: adp1_triple_essentiality] For dispensable genes it states that FBA cannot predict growth defects, so it recommends growth assays on specific carbon sources. [src: adp1_triple_essentiality] See [[concepts/metabolic-model-prediction-of-growth-defects-among-dispensable-genes]] for that point.

Two cautions go with these recommendations. Transposon insertion may leave partial gene function through truncated proteins or read-through transcription. That is a different mechanism from complete gene deletion. [src: adp1_triple_essentiality] See [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality]]. The essentiality fraction also mixes diverse conditions, so condition-matched comparisons are more informative. [src: adp1_triple_essentiality]

The first recommendation is to add trace aromatic compounds to the minimal-media definition. This would test whether the discordance in aromatic degradation genes resolves, and it would match in silico environmental assumptions to experimental reality. [src: adp1_triple_essentiality]

### Interpretation of the media results

The report calls proteomics (essentiality area under curve, AUC=0.74) and FBA (metabolic requirement F1=0.67) complementary for minimal-media studies. [src: adp1_triple_essentiality] It explains FBA's better performance in minimal media by tighter metabolic constraints and by FBA assumptions that better match reality. [src: adp1_triple_essentiality] It also states that robust expression is critical for essential functions. [src: adp1_triple_essentiality]

### Proposed follow-up analyses

- Use continuous FBA flux instead of the binary essentiality class. Linear or rank regression between flux and growth rate may capture quantitative growth effects. [src: adp1_triple_essentiality] See [[concepts/continuous-versus-binary-predictors-of-gene-essentiality]].
- Run condition-specific FBA simulations that match the FBA carbon source to the growth-assay carbon source. This would test whether per-condition predictions improve. [src: adp1_triple_essentiality]
- Investigate the 211 knockout-essential, TnSeq-dispensable genes to understand tolerance of partial function. [src: adp1_triple_essentiality] TnSeq is transposon sequencing.
- Analyze N-terminal versus C-terminal insertion effects, and test whether transposon position affects phenotype. [src: adp1_triple_essentiality]
- Develop a combined predictor from FBA, fitness and proteomics by machine learning. It may perform better than any single method. [src: adp1_triple_essentiality]
- Test predictions experimentally in ADP1. This would validate high-confidence FBA predictions, confirm proteomics-based predictions and resolve ambiguous cases. [src: adp1_triple_essentiality]
- Refine the FBA environmental assumptions. This means adding aromatic compounds to the minimal-media definition, testing whether the β-ketoadipate pathway discordance resolves, and updating from measured media composition. [src: adp1_triple_essentiality]
- Run TnSeq in media identical to the knockout experiments. This would test whether condition matching improves concordance and would separate condition effects from method effects. [src: adp1_triple_essentiality]
- Expand to other *Acinetobacter* species. This would test whether the FBA-growth relationship holds across the pangenome, compare species with different aromatic degradation capabilities, and identify species-specific versus universal patterns. [src: adp1_triple_essentiality]

### Data availability

The report states that all analysis code, data and figures are in the project directory. [src: adp1_triple_essentiality]

#### Original study

The original study built a 478-gene triple table from SQLite in its first notebook. [src: adp1_triple_essentiality] A second notebook covers the triple concordance matrix, threshold sensitivity, and FBA flux versus growth correlations. [src: adp1_triple_essentiality] A third covers RAST functional enrichment and pangenome status. [src: adp1_triple_essentiality] The main data tables are:

- `data/triple_gene_table.csv` has 478 genes. It integrates TnSeq, FBA, growth and annotations. [src: adp1_triple_essentiality]
- `data/cluster_id_mapping.csv` has 4,891 mappings from the KBase Data Lakehouse to ADP1 pangenome cluster identifiers (IDs). [src: adp1_triple_essentiality]

#### Refined study

The refined study provides notebooks for essentiality-vector construction, binary concordance, proteomics correlation, receiver operating characteristic (ROC) analysis of continuous predictors, and discordant-gene characterization. [src: adp1_triple_essentiality] Its outputs are:

| File | Contents |
|---|---|
| `data/essentiality_vectors.csv` | 5,852 genes × 19 columns [src: adp1_triple_essentiality] |
| `data/concordance_summary.csv` | 8 rows of performance metrics for all methods [src: adp1_triple_essentiality] |
| `data/roc_summary.csv` | 6 rows of ROC AUC values for continuous predictors [src: adp1_triple_essentiality] |
| `data/proteomics_correlation.csv` | 1 row of expression correlation statistics [src: adp1_triple_essentiality] |
| `data/discordance_summary.csv` | 4 rows, a summary by concordance category [src: adp1_triple_essentiality] |
| `data/discordant_ko_essential_tnseq_dispensable.csv` | 211 genes [src: adp1_triple_essentiality] |
| `data/discordant_ko_dispensable_tnseq_essential.csv` | 293 genes [src: adp1_triple_essentiality] |

#### Shared database

The shared database is `user_data/berdl_tables.db`, a 136 MB SQLite file that is not stored in git. [src: adp1_triple_essentiality] Its `genome_features` table has 5,852 genes and 51 columns. [src: adp1_triple_essentiality] Its `gene_phenotypes` table has 239,584 rows. [src: adp1_triple_essentiality]

## Methods: Essentiality Vector Construction (Refined Study)

This part of the report describes how the refined study built its per-gene essentiality vectors (flux balance analysis, knockout, transposon sequencing and proteomics). It also lists the statistics used and the settings of the original study that the report reuses. [src: adp1_triple_essentiality]

### Flux balance analysis and knockout vectors

The refined study uses binary essential versus non-essential flux balance analysis (FBA) calls from ModelSEED predictions. It classifies 866 genes in rich media and 866 genes in minimal media. [src: adp1_triple_essentiality]

Experimental knockout calls come from the de Berardinis et al. (2008) knockout collection. They were extracted from user_data/berdl_tables.db, which was originally assembled in the acinetobacter_adp1_explorer project. [src: adp1_triple_essentiality] That database integrates ADP1 genome features with experimental phenotypes, FBA predictions and KBase Data Lakehouse pangenome annotations. [src: adp1_triple_essentiality] See [[entities/de-berardinis-et-al-2008-adp1-deletion-mutant-collection]].

The rich-media (LB) data cover 2,953 genes, of which 346 are essential and 2,607 are dispensable. [src: adp1_triple_essentiality] The minimal-media data cover 3,092 genes, of which 499 are essential. [src: adp1_triple_essentiality] The study merges the two by prioritizing essentiality_minimal and falling back to essentiality_lb. [src: adp1_triple_essentiality]

### TnSeq vectors

The study builds binary transposon sequencing (TnSeq) vectors at 5 thresholds (0.01-0.20). It also keeps the continuous essentiality_fraction and fitness. [src: adp1_triple_essentiality] It chose the thresholds from the essentiality_fraction distribution, which has mean=0.026 and median=0.0. [src: adp1_triple_essentiality] For receiver operating characteristic (ROC) analysis, continuous fitness is inverted (fitness × -1). [src: adp1_triple_essentiality]

The five thresholds were tested without formal multiple-testing correction. [src: adp1_triple_essentiality] The report argues that correction would not change the conclusion, because all thresholds show negative Cohen's kappa. In its words, this is systematic disagreement of TnSeq with the knockout experiments across all reasonable threshold choices. [src: adp1_triple_essentiality] See [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality]].

### Proteomics

Expression is log2 proteomics averaged across 7 *Acinetobacter* strains. [src: adp1_triple_essentiality] Locus tags are parsed from the complex feature IDs by searching for `[locus_tag=` and extracting up to `]`. [src: adp1_triple_essentiality] Expression data exist for 2,383 genes. [src: adp1_triple_essentiality]

### Original-study growth-defect definition

The original study thresholds each condition independently at the 25th percentile (Q25) of its growth-rate distribution. This classifies the bottom 25% as growth defects. [src: adp1_triple_essentiality] It then flags "any defect" as a defect on at least one of 8 conditions. [src: adp1_triple_essentiality]

The any-defect background rate is 72% of 478 genes. The report expected 90% if conditions were independent and attributes the observed 72% to inter-condition correlation. [src: adp1_triple_essentiality]

For sensitivity, the original study tested Q10, Q15, Q20, Q25, Q30, Q35 and Q40. [src: adp1_triple_essentiality] Its null result holds across Q10–Q35, although Q25 is the standard choice. [src: adp1_triple_essentiality]

### Statistics

- **Concordance:** confusion matrices and Cohen's kappa (κ). κ > 0.6 is read as substantial agreement, κ 0.4-0.6 as moderate agreement, and κ < 0 as systematic disagreement. [src: adp1_triple_essentiality]
- **Performance:** sensitivity (recall), specificity, precision (PPV) and F1 score. [src: adp1_triple_essentiality] Sensitivity is TP / (TP + FN), the fraction of essential genes caught. [src: adp1_triple_essentiality] Precision is TP / (TP + FP), the accuracy when predicting essential. [src: adp1_triple_essentiality] F1 is 2 × (Precision × Recall) / (Precision + Recall), a harmonic mean. [src: adp1_triple_essentiality]
- **Correlation:** Pearson r for linear relationships and Spearman ρ for monotonic ones, with P-values reported. [src: adp1_triple_essentiality]
- **Group comparisons:** the refined study uses a Mann-Whitney U test of expression in essential versus dispensable genes. [src: adp1_triple_essentiality] The original study uses a Kruskal-Wallis test of growth rate by FBA class. [src: adp1_triple_essentiality]
- **Classification:** ROC curves and area under curve (AUC). AUC > 0.7 is fair, AUC > 0.8 is good, and AUC < 0.5 is worse than random. [src: adp1_triple_essentiality]
- **Enrichment:** the original study tests functional-category enrichment in discordant genes with Fisher's exact test and Benjamini-Hochberg false discovery rate (FDR) correction. It reports odds ratios (OR) and adjusted q-values. [src: adp1_triple_essentiality]

### Software

The report lists Python 3.11+ and pandas 2.0+ for data manipulation. [src: adp1_triple_essentiality] It lists scikit-learn 1.3+ for ROC curves and confusion matrices. [src: adp1_triple_essentiality] It lists scipy 1.11+ for the Mann-Whitney, Spearman, chi-squared and Kruskal-Wallis tests. [src: adp1_triple_essentiality] Plotting uses matplotlib 3.7+ and seaborn 0.12+. [src: adp1_triple_essentiality] Database queries use sqlite3. [src: adp1_triple_essentiality]

## References; Supplementary Information

### References and what each supplies

The knockout collection of de Berardinis et al. (2008) is the essentiality ground truth in both studies. The original study used mutant growth rates on 8 carbon sources. The refined study used rich (LB) and minimal-media essentiality calls. [src: adp1_triple_essentiality] See [[entities/de-berardinis-et-al-2008-adp1-deletion-mutant-collection]].

Durot et al. (2008) is the source of the flux balance analysis (FBA) model predictions for both studies. [src: adp1_triple_essentiality] The report attributes an original ~75% FBA-TnSeq concordance to this paper. [src: adp1_triple_essentiality] See [[entities/durot-et-al-2008-adp1-metabolic-model]].

Fitness Browser random barcode transposon sequencing (RB-TnSeq) data, aggregated across multiple studies, supply the transposon sequencing (TnSeq) data. The original study used binary TnSeq essentiality. The refined study used essentiality fraction and fitness. [src: adp1_triple_essentiality] Price et al. (2018) is cited for the Fitness Browser, RB-TnSeq and TnSeq essentiality metrics. [src: adp1_triple_essentiality]

The KBase Data Lakehouse supplies three things:
- proteomics expression across 7 Acinetobacter strains (refined study); [src: adp1_triple_essentiality]
- genome features and annotations (both studies); [src: adp1_triple_essentiality]
- pangenome cluster assignments (original study). [src: adp1_triple_essentiality]

The remaining citations give context:
- Barbe et al. (2004) is cited for genome annotation and aromatic degradation pathways, and as context for the aromatic-catabolism findings. [src: adp1_triple_essentiality]
- Monk et al. (2013) is cited for FBA model reconstruction methodology. [src: adp1_triple_essentiality]
- Guzman et al. (2018) is cited as a conceptual framework for condition-dependent essentiality. [src: adp1_triple_essentiality]
- The report says this framework supports its finding that 70% of genes show condition-specific defects. [src: adp1_triple_essentiality]
- Suárez et al. (2020) is cited as context for combining FBA and TnSeq in ADP1 genome engineering. [src: adp1_triple_essentiality]

### Refined study: knockout versus TnSeq categories

The 1,933 genes split into four categories. Most are dispensable by both methods, and only 18 are essential by both. [src: adp1_triple_essentiality]

| Category | Genes | Share | Mean essentiality_fraction (SD) | Mean fitness (SD) | Claim |
|---|---|---|---|---|---|
| KO essential, TnSeq dispensable | 211 | 10.9% | 0.0034 (0.010) | -0.79 (0.93) | [src: adp1_triple_essentiality] |
| KO dispensable, TnSeq essential | 293 | 15.2% | 0.1023 (0.118) | -0.34 (0.66) | [src: adp1_triple_essentiality] |
| Both dispensable | 1,411 | 73.0% | 0.0116 (0.016) | -0.32 (0.60) | [src: adp1_triple_essentiality] |
| Both essential | 18 | 0.9% | 0.0969 (0.041) | -1.18 (1.49) | [src: adp1_triple_essentiality] |

The report offers these interpretations:
- KO-essential/TnSeq-dispensable genes are truly essential but rarely show fitness defects in TnSeq conditions. [src: adp1_triple_essentiality]
- It hypothesizes that these genes tolerate partial function from transposon-disrupted alleles. [src: adp1_triple_essentiality]
- KO-dispensable/TnSeq-essential genes are important for competitive fitness but not viability. [src: adp1_triple_essentiality]
- The 18 genes essential by both methods are the unambiguous true positives, with the highest fitness cost of all categories (mean=-1.18). [src: adp1_triple_essentiality]

See [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality]] and [[concepts/limits-of-transposon-based-essentiality-calls]].

### Confusion matrices against knockout essentiality

FBA agreed with knockout calls moderately. RB-TnSeq at the 0.05 threshold agreed poorly in rich media, with negative kappa. [src: adp1_triple_essentiality]

| Comparison | Genes | TP | FP | FN | TN | Recall | Precision | Specificity | F1 | Kappa | Claims |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FBA vs KO, rich | 724 | 164 | 92 | 106 | 362 | 60.8% | 64.0% | 79.7% | 0.624 | 0.486 | [src: adp1_triple_essentiality] |
| FBA vs KO, minimal | 833 | 229 | 102 | 120 | 382 | 65.6% | 69.2% | 78.9% | 0.673 | 0.493 | [src: adp1_triple_essentiality] |
| RB-TnSeq (0.05) vs KO, rich | 1,933 | 18 | 293 | 211 | 1,411 | 7.9% | 5.8% | 82.8% | 0.067 | -0.081 | [src: adp1_triple_essentiality] |

See [[concepts/concordance-of-genome-scale-metabolic-model-predictions-with-experimental-data]].

### ROC AUC of continuous predictors

Proteomics was the best continuous predictor of knockout essentiality. Inverted fitness was the best TnSeq-based predictor, and essentiality fraction was worse than random. [src: adp1_triple_essentiality] Fitness was multiplied by -1 because negative fitness indicates a defect, so higher inverted fitness should predict essentiality. [src: adp1_triple_essentiality]

| Predictor | Medium | ROC AUC | Genes | Claim |
|---|---|---|---|---|
| Fitness (inverted) | Rich | 0.700 | 1,933 | [src: adp1_triple_essentiality] |
| Fitness (inverted) | Minimal | 0.725 | 2,011 | [src: adp1_triple_essentiality] |
| Proteomics (log2) | Minimal | 0.743 | 2,288 | [src: adp1_triple_essentiality] |
| Essentiality fraction | Rich | 0.344 | 1,933 | [src: adp1_triple_essentiality] |
| Essentiality fraction | Minimal | 0.403 | 2,011 | [src: adp1_triple_essentiality] |

See [[concepts/continuous-versus-binary-predictors-of-gene-essentiality]].

### Proteomics statistics

Essential genes had higher proteomics expression than dispensable genes. The analysis included 2,288 genes: 464 essential and 1,824 dispensable. [src: adp1_triple_essentiality] Mean log2 expression was 28.43 (SD 2.94) for essential genes [src: adp1_triple_essentiality] and 25.73 (SD 2.96) for dispensable genes. [src: adp1_triple_essentiality] The difference was 2.70 log2 units, a 6.5× fold change, with Mann-Whitney p=9.91×10⁻⁵⁹. [src: adp1_triple_essentiality] Expression correlated with essentiality at Pearson r=0.345 (p=5.32×10⁻⁶⁵) [src: adp1_triple_essentiality] and Spearman ρ=0.338 (p=3.28×10⁻⁶²). [src: adp1_triple_essentiality]

## Authors; Acknowledgments; Revision History

This part of the report lists the authors and funding. [src: adp1_triple_essentiality] It also lists the resources the report builds on. [src: adp1_triple_essentiality] Its revision history separates the original study from the refined analysis. [src: adp1_triple_essentiality]

### Authors and funding

Paramvir Dehal (ORCID 0000-0001-5810-2497, Lawrence Berkeley National Laboratory, US Department of Energy) conducted the original triple essentiality study, dated 2026-02-18. [src: adp1_triple_essentiality] Christopher Henry (ORCID 0000-0001-8058-9123, same institution) conducted the refined comprehensive analysis and integration, dated 2026-02-19. [src: adp1_triple_essentiality] The study was funded by the U.S. Department of Energy, Office of Science, Biological and Environmental Research. [src: adp1_triple_essentiality]

### Acknowledged resources

The report builds on the [[entities/de-berardinis-et-al-2008-adp1-deletion-mutant-collection|de Berardinis et al. (2008) knockout collection]]. [src: adp1_triple_essentiality] It also builds on the [[entities/durot-et-al-2008-adp1-metabolic-model|Durot et al. (2008) FBA metabolic model]], where FBA is flux balance analysis. [src: adp1_triple_essentiality] It uses the [[entities/fitness-browser]] random barcode transposon sequencing (RB-TnSeq) aggregation at fit.genomics.lbl.gov. [src: adp1_triple_essentiality] It acknowledges the [[entities/kbase-data-lakehouse]] infrastructure. [src: adp1_triple_essentiality]

### Revision history

The original study reported two results. FBA did not predict growth defects among transposon sequencing (TnSeq)-dispensable genes (p=0.63). [src: adp1_triple_essentiality] Aromatic degradation was enriched among discordant genes (odds ratio, OR=9.7). [src: adp1_triple_essentiality]

The refined analysis added multiple RB-TnSeq thresholds (0.01-0.20). [src: adp1_triple_essentiality] Its revision summary states that TnSeq systematically disagrees with KO (KEGG ortholog) (κ<0). It also states that fitness predicts essentiality better (area under curve, AUC=0.70-0.73) than essentiality_fraction (AUC=0.34-0.40). [src: adp1_triple_essentiality]

## Caveats and Open Work

- The Q25 threshold flags about 25% of genes per condition, so aggregating "any defect" over 8 conditions gives a high background rate by design. The expected rate is 1 − 0.75⁸ = 90% if conditions were independent, against 72% observed. [src: adp1_triple_essentiality]
- The glucarate result runs opposite to prediction, so the weak flux–growth trends are not uniform across conditions. [src: adp1_triple_essentiality]
- The report states that FBA essentiality predictions require experimental validation. [src: adp1_triple_essentiality]
- The report calls knockouts the best proxy for lethality, but notes that fitness, expression and growth rates reveal additional biology. [src: adp1_triple_essentiality]
- Aromatic enrichment (OR = 9.7) and the 70% figure come from the original study. [src: adp1_triple_essentiality]

## Slots Into

- [[concepts/continuous-versus-binary-predictors-of-gene-essentiality]]: continuous fitness and proteomics outperform binary essentiality fraction. [src: adp1_triple_essentiality]
- [[concepts/transposon-insertion-fitness-versus-gene-deletion-lethality]]: TnSeq tracks fitness cost, not lethality (κ<0). [src: adp1_triple_essentiality]
- [[concepts/metabolic-model-prediction-of-growth-defects-among-dispensable-genes]]: FBA class does not predict growth defects (p = 0.63). [src: adp1_triple_essentiality]
- [[concepts/systematic-blind-spots-of-flux-balance-models-for-condition-specific-requirements]]: aromatic degradation genes are enriched among discordant genes. [src: adp1_triple_essentiality]
- [[concepts/condition-specific-gene-importance-across-carbon-sources]]: 70% of genes show condition-specific defects. [src: adp1_triple_essentiality]
