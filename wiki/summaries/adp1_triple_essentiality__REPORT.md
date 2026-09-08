---
type: Summary
description: Integrated comparison of FBA, TnSeq, knockout, growth, and proteomics
  essentiality.
doc_type: short
full_text: ../sources/adp1_triple_essentiality__REPORT.md
title: Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1
sources:
- id: adp1_triple_essentiality
  resource: ../sources/adp1_triple_essentiality__REPORT.md
  title: adp1 triple essentiality
---
# Triple Essentiality Concordance Analysis for *Acinetobacter baylyi* ADP1

## Overview

This report integrates an original analysis of 478 triple-covered *Acinetobacter baylyi* ADP1 genes with a refined analysis of up to 5,852 genes, comparing [flux-balance-analysis](../entities/flux-balance-analysis.md) (FBA), [tnseq](../entities/tnseq.md)/RB-TnSeq (random barcode transposon sequencing), complete-gene knockout phenotypes, mutant growth rates, and proteomics. The original study asked whether FBA distinguishes growth-defective genes among TnSeq-dispensable genes; the refined study evaluated concordance with experimental knockout lethality across rich and minimal media and tested continuous fitness and expression predictors. [^adp1_triple_essentiality]

## Key Findings

### FBA and experimental essentiality

Among 478 genes with TnSeq, FBA, and mutant-growth data, all genes were TnSeq-dispensable. FBA class was not associated with growth-defect status: chi-squared = 0.93, p = 0.63, 2 df. Defect rates were 73.1% (57/78) for FBA-essential genes, 73.5% (150/204) for FBA-variable genes, and 69.4% (136/196) for FBA-blocked genes; the Kruskal-Wallis test on mean growth rates was also non-significant (H = 1.67, p = 0.43). [^adp1_triple_essentiality]

The null association persisted from Q10 through Q35 growth-defect thresholds. At Q10, Q15, Q20, Q25, Q30, Q35, and Q40, the chi-squared p-values were 0.985, 0.887, 0.405, 0.629, 0.313, 0.058, and 0.048, respectively. The Q25 threshold classified 72% of genes as defective, with defect rates of 73%, 74%, and 69% in the FBA-essential, FBA-variable, and FBA-blocked groups. [^adp1_triple_essentiality]

The refined analysis found moderate FBA concordance with knockout lethality. In rich media, FBA versus knockout data covered 724 genes and yielded recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486. In minimal media, 833 genes yielded recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493. [^adp1_triple_essentiality]

These results distinguish two prediction tasks: FBA shows moderate concordance at the lethal-versus-dispensable boundary, but FBA class does not predict quantitative growth defects within the TnSeq-dispensable set. [^adp1_triple_essentiality]

### RB-TnSeq, fitness, and knockout discordance

RB-TnSeq essentiality thresholds systematically disagreed with knockout essentiality in rich media. Across thresholds of 0.01, 0.025, 0.05, 0.10, and 0.20, Cohen’s kappa was -0.139, -0.122, -0.081, -0.024, and -0.014, respectively. At the 0.05 threshold, the comparison included 1,933 genes: recall = 7.9%, precision = 5.8%, specificity = 82.8%, F1 = 0.067, and kappa = -0.081. [^adp1_triple_essentiality]

At the 0.05 threshold, the concordance categories were both essential = 18 genes (0.9%), both dispensable = 1,411 genes (73.0%), knockout-essential/TnSeq-dispensable = 211 genes (10.9%), and knockout-dispensable/TnSeq-essential = 293 genes (15.2%). The report interprets these differences as evidence that transposon insertion measures fitness cost and may preserve partial function, whereas complete deletion measures lethality. [^adp1_triple_essentiality]

Continuous fitness performed better than binary essentiality fraction. Inverted fitness had AUC = 0.700 in rich media and AUC = 0.725 in minimal media, whereas essentiality fraction had AUC = 0.344 and AUC = 0.403, respectively. AUC means Area Under the ROC Curve, a threshold-independent classification measure. [^adp1_triple_essentiality]

The discordant knockout-essential/TnSeq-dispensable genes had mean essentiality fraction = 0.0034, standard deviation = 0.010, mean fitness = -0.79, and standard deviation = 0.93. The knockout-dispensable/TnSeq-essential genes had mean essentiality fraction = 0.1023, standard deviation = 0.118, mean fitness = -0.34, and standard deviation = 0.66. The 18 genes called essential by both methods had mean essentiality fraction = 0.0969, standard deviation = 0.041, mean fitness = -1.18, and standard deviation = 1.49. [^adp1_triple_essentiality]

### Proteomics and multi-omic evidence

Proteomics measured average log2 expression across 7 *Acinetobacter* strains. Among 2,288 genes, essential genes (n = 464) had mean log2 expression = 28.43 ± 2.94, while dispensable genes (n = 1,824) had mean log2 expression = 25.73 ± 2.96; the difference was 2.70 log2 units, corresponding to 6.5-fold higher expression. The Mann-Whitney U p-value was 9.91×10⁻⁵⁹. [^adp1_triple_essentiality]

Expression correlated with knockout essentiality at Pearson r = 0.345 (p = 5.32×10⁻⁶⁵) and Spearman ρ = 0.338 (p = 3.28×10⁻⁶²), with ROC AUC = 0.743. These results make proteomics a fair-to-good continuous predictor and provide an independent evidence axis alongside FBA and fitness. [^adp1_triple_essentiality]

### Condition-specific growth and model gaps

Across eight carbon sources, 333 of 478 genes (70%) showed condition-specific growth defects, 10 genes (2%) showed defects across all eight conditions, and 135 genes (28%) showed no defect on any condition. Mean pairwise defect correlation was 0.38, with a range of -0.03 to 1.0. [^adp1_triple_essentiality]

Condition-specific FBA flux had weak, mixed correlations with measured growth: glucose ρ = -0.021 (p = 0.677; n = 387), acetate ρ = -0.153 (p = 0.004; n = 352), asparagine ρ = -0.257 (p < 0.001; n = 286), butanediol ρ = -0.145 (p = 0.092; n = 137), glucarate ρ = +0.246 (p = 0.005; n = 127), and lactate ρ = -0.160 (p = 0.065; n = 135). The positive glucarate correlation is opposite the expected direction and suggests condition-specific model inaccuracies. [^adp1_triple_essentiality]

Aromatic degradation was strongly enriched among FBA-discordant genes: 9 of 11 genes were discordant, with odds ratio (OR) = 9.70 and Benjamini-Hochberg false discovery rate (FDR)-adjusted q = 0.012. Directional enrichment for FBA under-prediction was OR = 12.0, q = 0.004. Lipid metabolism was depleted among discordant genes, with OR = 0.34 and q = 0.042; only 7 of 46 lipid-metabolism genes were discordant. [^adp1_triple_essentiality]

The report identifies beta-ketoadipate-pathway genes, including 4-carboxymuconolactone decarboxylase and beta-ketoadipate enol-lactone hydrolase, as examples of genes predicted as blocked by FBA but associated with experimental growth defects. It proposes that missing aromatic substrates or mismatched environmental assumptions, rather than network topology alone, may explain this model gap. [^adp1_triple_essentiality]

Pangenome status did not explain discordance: genes were overwhelmingly core across discordance classes at 93–100%, and the enrichment test gave OR = 0.89 and p = 0.80. [^adp1_triple_essentiality]

## Caveats and Interpretation Limits

The original analysis is restricted by design to 478 TnSeq-dispensable genes because TnSeq-essential genes do not provide viable deletion mutants for the growth-rate analysis. Therefore, its null result concerns growth variation among dispensable genes and cannot be interpreted as a whole-genome test of FBA lethality prediction. [^adp1_triple_essentiality]

The Q25 threshold flags the bottom 25% of growth rates separately in each condition, so the reported “any defect” rate across eight conditions is an aggregation-dependent quantity. The report notes an expected rate of 1 − 0.75⁸ = 90% under independent conditions, compared with the observed 72%, reflecting positive inter-condition correlation. [^adp1_triple_essentiality]

The refined knockout comparison merges minimal-media and rich-media calls by prioritizing minimal-media data and using rich-media data as fallback. Rich-media knockout data covered 2,953 genes, including 346 essential and 2,607 dispensable genes; the merged minimal-media set covered 3,092 genes, including 499 essential genes. [^adp1_triple_essentiality]

Proteomics expression was averaged across 7 *Acinetobacter* strains rather than measured only in the exact knockout assay condition, so its association with essentiality is independent supporting evidence rather than a condition-matched causal test. [^adp1_triple_essentiality]

The five RB-TnSeq thresholds were tested without formal multiple-testing correction. The report states that because every threshold produced negative Cohen’s kappa, correction would not change the conclusion of systematic disagreement across the tested thresholds. [^adp1_triple_essentiality]

The proposed explanations for TnSeq/knockout discordance—including partial or truncated protein production, read-through transcription, retained functional domains, and condition aggregation—are mechanistic hypotheses rather than directly resolved demonstrations in this report. Likewise, the proposed explanation that trace aromatics in experimental media account for aromatic-pathway discordance requires testing with measured media composition and revised FBA constraints. [^adp1_triple_essentiality]

The report recommends condition-matched TnSeq and knockout experiments, domain- and insertion-position analysis of the 211 knockout-essential/TnSeq-dispensable genes, addition of trace aromatic compounds to FBA media definitions, condition-specific flux simulations, and combined FBA-plus-fitness-plus-proteomics prediction. [^adp1_triple_essentiality]

## Slots Into

- [gene-essentiality](../concepts/gene-essentiality.md) — FBA, knockout, RB-TnSeq, fitness, and proteomics measure distinct aspects of essentiality, with exact concordance and AUC results.
- [condition-specific-fitness](../concepts/condition-specific-fitness.md) — Mutant growth defects vary across carbon sources, and continuous fitness outperforms binary essentiality fraction.
- [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md) — Aromatic degradation is enriched among FBA-discordant genes, identifying environmental assumptions as a model gap.
- [multi-omics-integration](../concepts/multi-omics-integration.md) — Proteomics, FBA, knockout, TnSeq, and growth measurements provide complementary essentiality evidence.
- [pangenome-integration](../concepts/pangenome-integration.md) — Pangenome core status was tested as a source of discordance and showed no significant enrichment.

[^adp1_triple_essentiality]: [adp1 triple essentiality](../sources/adp1_triple_essentiality__REPORT.md)
