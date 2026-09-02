---
type: "Concept"
description: "Why transposon fitness and complete-knockout essentiality diverge"
sources: ["summaries/adp1_triple_essentiality__REPORT.md"]
---
# Why transposon fitness and complete-knockout essentiality disagree

[[summaries/adp1_triple_essentiality__REPORT]] shows that transposon-based assays and complete-gene knockouts do not measure identical phenotypes. RB-TnSeq (random barcode transposon sequencing) reports the fitness of insertion mutants, whereas a complete knockout tests whether removing the entire gene produces lethality under the assay conditions. [src: adp1_triple_essentiality] This distinction places the result within [[concepts/gene-essentiality]] and [[concepts/perturbation-modality-dependent-phenotypic-architecture]].

## Core evidence

At an RB-TnSeq essentiality threshold of 0.05 in rich medium, the comparison covered 1,933 genes. [src: adp1_triple_essentiality] Only 18 genes (0.9%) were called essential by both RB-TnSeq and knockout assays, while 1,411 genes (73.0%) were called dispensable by both. [src: adp1_triple_essentiality] The two major discordant groups were knockout-essential/RB-TnSeq-dispensable genes, comprising 211 genes (10.9%), and knockout-dispensable/RB-TnSeq-essential genes, comprising 293 genes (15.2%). [src: adp1_triple_essentiality]

Agreement was poor across all tested RB-TnSeq thresholds of 0.01, 0.025, 0.05, 0.10, and 0.20, for which Cohen’s kappa was -0.139, -0.122, -0.081, -0.024, and -0.014, respectively. [src: adp1_triple_essentiality] At the 0.05 threshold, recall was 7.9%, precision was 5.8%, specificity was 82.8%, F1 was 0.067, and Cohen’s kappa was -0.081. [src: adp1_triple_essentiality] The uniformly negative kappa values support systematic assay discordance rather than a disagreement caused by one arbitrary threshold, although the thresholds were not formally corrected for multiple testing. [src: adp1_triple_essentiality]

## Continuous fitness is more informative than a binary call

Continuous RB-TnSeq fitness performed better than the binary essentiality fraction for identifying knockout-essential genes. [src: adp1_triple_essentiality] Inverted fitness produced an AUC (Area Under the ROC Curve, a threshold-independent classification measure) of 0.700 in rich medium and 0.725 in minimal medium, whereas essentiality fraction produced AUC values of 0.344 and 0.403 in the same media. [src: adp1_triple_essentiality]

The discordant groups also differed in their continuous measurements. Knockout-essential/RB-TnSeq-dispensable genes had mean essentiality fraction = 0.0034, standard deviation = 0.010, mean fitness = -0.79, and standard deviation = 0.93. [src: adp1_triple_essentiality] Knockout-dispensable/RB-TnSeq-essential genes had mean essentiality fraction = 0.1023, standard deviation = 0.118, mean fitness = -0.34, and standard deviation = 0.66. [src: adp1_triple_essentiality] The 18 genes called essential by both assays had mean essentiality fraction = 0.0969, standard deviation = 0.041, mean fitness = -1.18, and standard deviation = 1.49. [src: adp1_triple_essentiality]

These results support treating fitness as a graded phenotype rather than converting it immediately into an essential/dis­pensable label. [src: adp1_triple_essentiality] They also refine the broader [[concepts/gene-essentiality]] distinction between predicting lethality and predicting the magnitude of growth impairment. [src: adp1_triple_essentiality]

## Why the assays can disagree

The report interprets the pattern as consistent with insertion mutants retaining partial function, whereas complete deletion removes the entire gene. [src: adp1_triple_essentiality] Partial or truncated protein production, read-through transcription, retained functional domains, and aggregation across conditions are proposed mechanisms for RB-TnSeq mutants appearing dispensable when complete knockouts are lethal. [src: adp1_triple_essentiality] These mechanisms remain hypotheses in this analysis rather than directly resolved demonstrations. [src: adp1_triple_essentiality]

The reverse discordance is also informative: some genes classified as RB-TnSeq-essential were knockout-dispensable. [src: adp1_triple_essentiality] This pattern suggests that insertion position, polar effects on neighboring genes, or assay-specific fitness costs may make an insertion mutant more impaired than a complete deletion, but these explanations were not directly established by the report. [src: adp1_triple_essentiality]

## Relation to FBA and growth assays

The assay disagreement is not equivalent to a general failure of every essentiality predictor. [src: adp1_triple_essentiality] In the refined analysis, FBA (flux balance analysis) versus knockout data showed moderate concordance, with rich-medium recall = 60.8%, precision = 64.0%, specificity = 79.7%, F1 = 0.624, and Cohen’s kappa = 0.486 across 724 genes. [src: adp1_triple_essentiality] In minimal medium, the comparison covered 833 genes and yielded recall = 65.6%, precision = 69.2%, specificity = 78.9%, F1 = 0.673, and Cohen’s kappa = 0.493. [src: adp1_triple_essentiality]

However, among 478 genes that were all TnSeq-dispensable, FBA class did not predict quantitative growth-defect status: chi-squared = 0.93, p = 0.63, 2 df, and the Kruskal-Wallis test on mean growth rates was H = 1.67, p = 0.43. [src: adp1_triple_essentiality] Thus, the evidence supports a distinction between FBA’s moderate performance at the lethal-versus-dispensable boundary and its inability in this subset to explain the severity of growth defects among transposon-dispensable genes. [src: adp1_triple_essentiality]

## Condition dependence

Assay discordance is partly condition-dependent because mutant growth phenotypes vary across environments. [src: adp1_triple_essentiality] Across eight carbon sources, 333 of 478 genes (70%) showed condition-specific growth defects, 10 genes (2%) showed defects across all eight conditions, and 135 genes (28%) showed no defect on any condition. [src: adp1_triple_essentiality] Mean pairwise defect correlation was 0.38, with a range of -0.03 to 1.0. [src: adp1_triple_essentiality] These findings support [[concepts/condition-specific-fitness]]: an assay comparison made across mismatched or aggregated conditions can conflate perturbation modality with environmental dependence. [src: adp1_triple_essentiality]

## Tensions

The data support two conclusions that must be kept separate: continuous transposon fitness contains useful information about knockout lethality, but thresholded RB-TnSeq essentiality shows poor agreement with complete-knockout calls. [src: adp1_triple_essentiality] The first conclusion is supported by AUC values of 0.700 and 0.725 for inverted fitness, while the second is supported by the 0.05-threshold AUC of 0.344 for essentiality fraction and Cohen’s kappa of -0.081. [src: adp1_triple_essentiality] The apparent tension is resolved by distinguishing graded fitness prediction from binary assay concordance rather than treating either assay as a universal definition of essentiality. [src: adp1_triple_essentiality]

## Open Directions

- Perform condition-matched RB-TnSeq and complete-knockout experiments, then test whether discordance remains after aligning media and growth conditions. [src: adp1_triple_essentiality]
- Analyze insertion positions, gene domains, transcriptional polarity, and truncated-protein potential for the 211 knockout-essential/RB-TnSeq-dispensable genes to test the proposed partial-function mechanisms. [src: adp1_triple_essentiality]
- Compare continuous fitness, essentiality fraction, knockout calls, and growth rates with a preregistered threshold-selection and multiple-testing procedure to determine which representation generalizes across conditions. [src: adp1_triple_essentiality]
- Fit combined FBA-plus-fitness-plus-proteomics models and evaluate whether multi-omic predictors improve knockout-essentiality classification over any single assay. [src: adp1_triple_essentiality]
