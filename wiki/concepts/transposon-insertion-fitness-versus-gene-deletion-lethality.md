---
type: "Concept"
description: "Why RB-TnSeq (random barcode transposon sequencing) calls disagree with complete-deletion knockout essentiality, across thresholds, and what each method measures; stops at choice of continuous predictor."
sources: ["summaries/adp1_triple_essentiality__REPORT.md"]
---
# Transposon insertion fitness versus gene deletion lethality

In Acinetobacter baylyi ADP1, random barcode transposon sequencing (RB-TnSeq) calls disagree with complete-deletion knockout essentiality at every threshold tested. Cohen's kappa was negative at all five thresholds. [src: adp1_triple_essentiality] The report explains this by saying that transposon insertion is not gene deletion, so RB-TnSeq likely reflects fitness cost more than lethality. [src: adp1_triple_essentiality] The evidence comes from one organism and one report, and the report words its mechanisms as likely or suggested. [src: adp1_triple_essentiality] See also [[concepts/limits-of-transposon-based-essentiality-calls]] and [[summaries/adp1_triple_essentiality__REPORT]].

## What the two methods measure

A knockout deletion removes the gene completely and leaves zero protein. [src: adp1_triple_essentiality] A transposon insertion disrupts the gene but may still allow truncated protein, read-through transcription, or functional domains upstream of the insertion. [src: adp1_triple_essentiality] The report therefore argues that the methods measure different things: knockout experiments measure lethality, and transposon sequencing (TnSeq) measures fitness cost. [src: adp1_triple_essentiality] It calls knockouts the best proxy for lethality, while noting that fitness, expression and growth rates reveal additional biology. [src: adp1_triple_essentiality] The original ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]

## Disagreement across thresholds

Kappa was negative at all five thresholds tested on rich-media RB-TnSeq (N=1,933 genes), which the report reads as systematic disagreement worse than random chance. [src: adp1_triple_essentiality] The report states that threshold choice does not resolve the discordance, and none of the five thresholds showed positive kappa. [src: adp1_triple_essentiality]

| Threshold | Recall | Precision | F1 | Kappa |
|---|---|---|---|---|
| 0.01 | 18.8% | 4.8% | 0.076 | -0.139 [src: adp1_triple_essentiality] |
| 0.025 | 15.3% | 5.1% | 0.077 | -0.122 [src: adp1_triple_essentiality] |
| 0.05 | 7.9% | 5.8% | 0.067 | -0.081 [src: adp1_triple_essentiality] |
| 0.10 | 2.6% | 7.5% | 0.039 | -0.024 [src: adp1_triple_essentiality] |
| 0.20 | 0.4% | 4.3% | 0.008 | -0.014 [src: adp1_triple_essentiality] |

The report marks 0.025 as the optimal F1. [src: adp1_triple_essentiality] Raising the threshold lowers recall at every step, while precision stays between 4.3% and 7.5%. [src: adp1_triple_essentiality] The five thresholds were tested without formal multiple-testing correction. [src: adp1_triple_essentiality] The report argues that correction would not change the conclusion, because every threshold has negative kappa. [src: adp1_triple_essentiality]

## Concordance at the 0.05 cutoff

At the 0.05 threshold the two methods agree mostly on dispensable genes. Of 1,933 genes compared, 1,411 (73.0%) were dispensable by both and only 18 (0.9%) were essential by both. [src: adp1_triple_essentiality] Disagreements outnumber agreements on essentiality: 211 genes (10.9%) were knockout-essential but TnSeq-dispensable (false negatives), and 293 genes (15.2%) were knockout-dispensable but TnSeq-essential (false positives). [src: adp1_triple_essentiality] At this threshold recall was 7.9%, precision 5.8% and specificity 82.8%. [src: adp1_triple_essentiality] TnSeq caught only 18 of 229 knockout-essential genes. [src: adp1_triple_essentiality]

| Category | Genes | Mean essentiality_fraction (SD) | Mean fitness (SD) |
|---|---|---|---|
| Knockout-essential, TnSeq-dispensable | 211 (10.9%) | 0.0034 (0.010) | -0.79 (0.93) [src: adp1_triple_essentiality] |
| Knockout-dispensable, TnSeq-essential | 293 (15.2%) | 0.1023 (0.118) | -0.34 (0.66) [src: adp1_triple_essentiality] |
| Both dispensable | 1,411 (73.0%) | 0.0116 (0.016) | -0.32 (0.60) [src: adp1_triple_essentiality] |
| Both essential | 18 (0.9%) | 0.0969 (0.041) | -1.18 (1.49) [src: adp1_triple_essentiality] |

The 18 genes essential by both methods have the highest fitness cost of any category, and the report treats them as unambiguous true positives. [src: adp1_triple_essentiality]

## Proposed explanations

The report offers two interpretations of the discordant categories. [src: adp1_triple_essentiality]

- **Knockout-essential, TnSeq-dispensable.** The report suggests these genes tolerate partial function from transposon-disrupted alleles. [src: adp1_triple_essentiality] It describes them as truly essential but rarely showing fitness defects in TnSeq conditions. [src: adp1_triple_essentiality] A gene could also be essential under knockout conditions and dispensable under most TnSeq conditions, which gives a low essentiality_fraction despite high lethality. [src: adp1_triple_essentiality]
- **Knockout-dispensable, TnSeq-essential.** The report suggests these genes cause fitness defects such as slower growth without being lethal. [src: adp1_triple_essentiality] It describes them as important for competitive fitness but not viability. [src: adp1_triple_essentiality] The report summarises this as "fitness cost is not lethality". [src: adp1_triple_essentiality]

The original study analysed only TnSeq-dispensable genes (n=478). The report calls this limiting, because TnSeq misses most truly essential genes. [src: adp1_triple_essentiality] The report concludes that no single method is ground truth and that integrating complementary methods gives the most complete picture. [src: adp1_triple_essentiality]

## Follow-up the report proposes

The report proposes investigating the 211 knockout-essential/TnSeq-dispensable genes to understand tolerance of partial function. [src: adp1_triple_essentiality] It also proposes analysing N-terminal versus C-terminal insertion effects and testing whether transposon position affects phenotype. [src: adp1_triple_essentiality] Finally, it proposes running TnSeq in media identical to the knockout experiments, to test whether condition matching improves concordance and to separate condition effects from method effects. [src: adp1_triple_essentiality]

## Open Directions

- Examine the 211 knockout-essential/TnSeq-dispensable genes to learn which tolerate partial function. This tests the partial-function explanation.
- Compare insertion position within genes against fitness. This tests the truncated-protein and upstream-domain mechanism.
- Run condition-matched TnSeq against the knockout media. This would separate condition effects from method effects.
- Replace the binary threshold with a continuous predictor, such as essentiality_fraction or fitness, and compare it with knockout lethality directly. No threshold gave positive kappa, so this tests whether the binary cut is the problem.
