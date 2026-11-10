---
type: "Finding"
description: "Across 1,933 rich-medium genes, all five tested RB-TnSeq thresholds had negative kappa against knockout essentiality, and the best tabulated F1 was 0.077 at threshold 0.025, with 15.3% recall and 5.1% precision."
finding_id: "adp1_triple_essentiality--b191b064"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "0.077", "what": "best tabulated F1", "unit": "", "denominator": "", "scope": "rich medium, 1,933 genes"}, {"value": "15.3%", "what": "recall in the best-F1 row", "unit": "", "denominator": "", "scope": "rich medium"}, {"value": "5.1%", "what": "precision in the best-F1 row", "unit": "", "denominator": "", "scope": "rich medium"}, {"value": "-0.122", "what": "kappa in the best-F1 row", "unit": "", "denominator": "", "scope": "rich medium"}]
caveat: "Residual function after transposon insertion and fitness effects without lethality are proposed explanations for the discordance, not demonstrated mechanisms."
first_added: "2026-10-27"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# RB-TnSeq thresholds all disagree with knockout essentiality in rich medium

Across 1,933 rich-medium genes, all five tested RB-TnSeq thresholds had negative kappa against knockout essentiality, and the best tabulated F1 was 0.077 at threshold 0.025, with 15.3% recall and 5.1% precision. [src: adp1_triple_essentiality]

## Key figures

- **0.077**: best tabulated F1 (scope rich medium, 1,933 genes) [src: adp1_triple_essentiality]
- **15.3%**: recall in the best-F1 row (scope rich medium) [src: adp1_triple_essentiality]
- **5.1%**: precision in the best-F1 row (scope rich medium) [src: adp1_triple_essentiality]
- **-0.122**: kappa in the best-F1 row (scope rich medium) [src: adp1_triple_essentiality]

## Evidence

> **Threshold Analysis (Rich Media, N=1,933 genes)** | Threshold | Recall | Precision | F1 | Kappa | Interpretation | |-----------|--------|-----------|-------|--------|----------------| | 0.01 | 18.8% | 4.8% | 0.076 | -0.139 | Poor | | 0.025 | 15.3% | 5.1% | 0.077 | -0.122 | **Optimal F1** | | 0.05 | 7.9% | 5.8% | 0.067 | -0.081 | Poor | | 0.10 | 2.6% | 7.5% | 0.039 | -0.024 | Very poor | | 0.20 | 0.4% | 4.3% | 0.008 | -0.014 | Very poor | [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Residual function after transposon insertion and fitness effects without lethality are proposed explanations for the discordance, not demonstrated mechanisms. [src: adp1_triple_essentiality]

> - The 211 KO-essential genes that TnSeq calls dispensable likely tolerate partial function from transposon-disrupted genes - The 293 TnSeq-essential but KO-dispensable genes may be fitness-important but not lethal - Transposon insertion ≠ gene deletion [src: adp1_triple_essentiality]

## Other caveats in this report

- The report cautions that FBA, knockout, TnSeq, proteomics, and growth measurements address distinct biological outcomes. [src: adp1_triple_essentiality]
- The 478-gene triple-covered sample excludes TnSeq-essential genes, limiting its FBA–growth comparison to TnSeq-dispensable genes. [src: adp1_triple_essentiality]
- The FBA-class null persisted through Q35; Q40 produced a marginal p = 0.048 association, while the continuous-rate test remained nonsignificant. [src: adp1_triple_essentiality]
- The glucarate correlation (ρ = +0.246) ran opposite to the predicted direction; the report suggests condition-specific model inaccuracy. [src: adp1_triple_essentiality]
- The per-condition Q25 cutoff and eight-condition ‘any defect’ aggregation inflate background defect prevalence by design; observed prevalence was 72%, versus 90% expected under independence. [src: adp1_triple_essentiality]
