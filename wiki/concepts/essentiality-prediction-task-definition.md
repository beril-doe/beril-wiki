---
type: "Concept"
description: "Defines what essentiality analyses predict and where their evaluations apply"
sources: ["summaries/adp1_triple_essentiality__REPORT.md"]
---
# Prediction Targets and Evaluation Boundaries in Gene-Essentiality Analysis

Gene-essentiality analysis does not evaluate one universal prediction task: lethality, quantitative growth impairment, continuous mutant fitness, and condition-specific defects are distinct targets. The [[summaries/adp1_triple_essentiality__REPORT]] provides a direct case in which changing the target changes the apparent performance of [[entities/flux-balance-analysis]], [[entities/tnseq]], knockout assays, and proteomics. [src: adp1_triple_essentiality]

## Distinct prediction targets

### Lethal versus dispensable genes

The refined analysis evaluated whether FBA classification agreed with complete-gene knockout lethality, a binary task that separates lethal from dispensable genes. In rich media, 724 genes were covered, with recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486; in minimal media, 833 genes were covered, with recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493. [src: adp1_triple_essentiality]

These results support [[concepts/essentiality-prediction-task-definition]] as a task-boundary distinction: FBA showed moderate concordance at the lethal-versus-dispensable boundary, but that result should not be generalized to prediction of quantitative growth defects among genes already classified as TnSeq-dispensable. [src: adp1_triple_essentiality]

### Quantitative growth impairment among dispensable genes

The original analysis was restricted to 478 genes that were TnSeq-dispensable and had FBA and mutant-growth data; it therefore tested whether FBA classes distinguished different degrees of growth impairment within a viable-mutant subset, not whether FBA predicted whole-genome lethality. [src: adp1_triple_essentiality]

FBA class was not associated with growth-defect status in this subset: the chi-squared statistic was 0.93 with p = 0.63 and 2 degrees of freedom. Defect rates were 73.1% (57/78) for FBA-essential genes, 73.5% (150/204) for FBA-variable genes, and 69.4% (136/196) for FBA-blocked genes; the Kruskal-Wallis test on mean growth rates was also non-significant, with H = 1.67 and p = 0.43. [src: adp1_triple_essentiality]

The null association persisted across growth-defect thresholds from Q10 through Q35: the chi-squared p-values at Q10, Q15, Q20, Q25, Q30, Q35, and Q40 were 0.985, 0.887, 0.405, 0.629, 0.313, 0.058, and 0.048, respectively. [src: adp1_triple_essentiality]

### Continuous fitness versus binary calls

Continuous fitness was more informative for knockout-essentiality prediction than a binary or fraction-based essentiality call. Inverted fitness produced AUC = 0.700 in rich media and AUC = 0.725 in minimal media, whereas essentiality fraction produced AUC = 0.344 and AUC = 0.403, respectively; AUC means Area Under the ROC Curve, a threshold-independent classification measure. [src: adp1_triple_essentiality]

This finding refines [[concepts/condition-specific-fitness]]: a continuous phenotype can preserve ranking information that is lost when mutant outcomes are reduced to an essential-versus-dispensable label. [src: adp1_triple_essentiality]

## Assay definitions create different evaluation boundaries

RB-TnSeq, or random barcode transposon sequencing, and complete-gene knockout assays disagreed strongly when both were treated as binary essentiality tests in rich media. Across RB-TnSeq thresholds of 0.01, 0.025, 0.05, 0.10, and 0.20, Cohen’s kappa was -0.139, -0.122, -0.081, -0.024, and -0.014, respectively. [src: adp1_triple_essentiality]

At the 0.05 threshold, 1,933 genes were compared: recall = 7.9%, precision = 5.8%, specificity = 82.8%, F1 = 0.067, and Cohen’s kappa = -0.081. The concordance categories were both essential = 18 genes (0.9%), both dispensable = 1,411 genes (73.0%), knockout-essential/TnSeq-dispensable = 211 genes (10.9%), and knockout-dispensable/TnSeq-essential = 293 genes (15.2%). [src: adp1_triple_essentiality]

The report interprets this discordance as consistent with transposon insertion measuring fitness cost while potentially preserving partial function, whereas complete deletion measures lethality; the proposed mechanisms, including partial or truncated protein production, read-through transcription, retained functional domains, and condition aggregation, remain hypotheses rather than resolved demonstrations. [src: adp1_triple_essentiality]

The evaluation boundary is also defined by data availability: rich-media knockout data covered 2,953 genes, including 346 essential and 2,607 dispensable genes, while the merged minimal-media set covered 3,092 genes, including 499 essential genes. The merged set prioritized minimal-media calls and used rich-media data as fallback. [src: adp1_triple_essentiality]

## Condition dependence changes the target

Across eight carbon sources, 333 of 478 genes (70%) showed condition-specific growth defects, 10 genes (2%) showed defects across all eight conditions, and 135 genes (28%) showed no defect on any condition. Mean pairwise defect correlation was 0.38, with a range of -0.03 to 1.0. [src: adp1_triple_essentiality]

The Q25 threshold classified 72% of genes as defective in the analyzed condition-specific comparison, with defect rates of 73%, 74%, and 69% in the FBA-essential, FBA-variable, and FBA-blocked groups. The report notes an expected rate of 1 − 0.75⁸ = 90% under independent conditions, compared with the observed 72%, because the aggregation depends on inter-condition correlation. [src: adp1_triple_essentiality]

These results support [[concepts/condition-specific-fitness]] and constrain interpretation of [[concepts/gene-essentiality]]: an essentiality label must specify the assay, medium, phenotype threshold, and aggregation rule rather than being treated as a condition-free gene property. [src: adp1_triple_essentiality]

## Complementary predictors are not interchangeable

Proteomics supplied an independent continuous evidence axis rather than a condition-matched causal test. Across 2,288 genes measured over 7 *Acinetobacter* strains, essential genes (n = 464) had mean log2 expression = 28.43 ± 2.94, while dispensable genes (n = 1,824) had mean log2 expression = 25.73 ± 2.96; the difference was 2.70 log2 units, corresponding to 6.5-fold higher expression. The Mann-Whitney U p-value was 9.91×10⁻⁵⁹. [src: adp1_triple_essentiality]

Expression correlated with knockout essentiality at Pearson r = 0.345 (p = 5.32×10⁻⁶⁵) and Spearman ρ = 0.338 (p = 3.28×10⁻⁶²), with ROC AUC = 0.743. Because expression was averaged across 7 *Acinetobacter* strains rather than measured only in the exact knockout assay condition, it provides supporting evidence but does not establish condition-matched causation. [src: adp1_triple_essentiality]

This complements [[concepts/multi-omics-integration]]: FBA, knockout phenotype, TnSeq fitness, and proteomics should be evaluated as predictors of explicitly defined targets, not collapsed into a single undifferentiated essentiality score. [src: adp1_triple_essentiality]

## Implications for model evaluation

Condition-specific FBA flux had weak and mixed correlations with measured growth: glucose ρ = -0.021 (p = 0.677; n = 387), acetate ρ = -0.153 (p = 0.004; n = 352), asparagine ρ = -0.257 (p < 0.001; n = 286), butanediol ρ = -0.145 (p = 0.092; n = 137), glucarate ρ = +0.246 (p = 0.005; n = 127), and lactate ρ = -0.160 (p = 0.065; n = 135). The positive glucarate correlation was opposite the expected direction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]

Aromatic degradation was strongly enriched among FBA-discordant genes: 9 of 11 genes were discordant, with odds ratio (OR) = 9.70 and Benjamini-Hochberg false discovery rate (FDR)-adjusted q = 0.012; directional enrichment for FBA under-prediction was OR = 12.0 with q = 0.004. Lipid metabolism was depleted among discordant genes, with OR = 0.34 and q = 0.042, and only 7 of 46 lipid-metabolism genes were discordant. [src: adp1_triple_essentiality]

This evidence supports [[concepts/metabolic-model-gapfilling]]: model evaluation should distinguish failure to predict lethality from failure to predict condition-specific growth, and should test whether environmental assumptions explain errors in particular functional groups. [src: adp1_triple_essentiality]

Pangenome status did not explain discordance: genes were overwhelmingly core across discordance classes at 93–100%, and the enrichment test gave OR = 0.89 and p = 0.80. [src: adp1_triple_essentiality]

## Open Directions

- Perform condition-matched RB-TnSeq and complete-gene knockout experiments, then compare binary lethality, continuous fitness, and quantitative growth within the same media and genes to determine which discordances arise from assay modality. [src: adp1_triple_essentiality]
- Analyze insertion position, retained domains, and transcript structure for the 211 knockout-essential/TnSeq-dispensable genes to test whether partial gene products explain the discordance. [src: adp1_triple_essentiality]
- Add measured trace aromatic compounds to the FBA media definitions and rerun condition-specific flux simulations to test whether environmental assumptions explain the aromatic-degradation errors. [src: adp1_triple_essentiality]
- Fit combined FBA-plus-fitness-plus-proteomics predictors separately for lethal-versus-dispensable classification and quantitative growth ranking, then compare metrics appropriate to each target. [src: adp1_triple_essentiality]
- Reanalyze the eight-carbon-source data with explicitly condition-specific labels and dependence-aware aggregation to determine how inter-condition correlation changes essentiality estimates. [src: adp1_triple_essentiality]
