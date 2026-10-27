---
type: "Finding"
description: "In ROC analysis against knockout essentiality, inverted fitness had AUC 0.700 in rich medium and 0.725 in minimal medium, whereas essentiality fraction had AUC 0.344 and 0.403 in rich and minimal media respectively."
finding_id: "adp1_triple_essentiality--73c3cad3"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "0.700", "what": "ROC AUC of inverted fitness", "unit": "AUC", "denominator": "", "scope": "rich medium"}, {"value": "0.725", "what": "ROC AUC of inverted fitness", "unit": "AUC", "denominator": "", "scope": "minimal medium"}, {"value": "0.344", "what": "ROC AUC of essentiality fraction", "unit": "AUC", "denominator": "", "scope": "rich medium"}, {"value": "0.403", "what": "ROC AUC of essentiality fraction", "unit": "AUC", "denominator": "", "scope": "minimal medium"}]
caveat: "Aggregated TnSeq essentiality fraction mixes experimental conditions, so condition-matched comparisons may be more informative."
first_added: "2026-10-27"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# Continuous fitness predicts knockout essentiality; essentiality fraction does worse than random

In ROC analysis against knockout essentiality, inverted fitness had AUC 0.700 in rich medium and 0.725 in minimal medium, whereas essentiality fraction had AUC 0.344 and 0.403 in rich and minimal media respectively. [src: adp1_triple_essentiality]

## Key figures

- **0.700 AUC**: ROC AUC of inverted fitness (scope rich medium) [src: adp1_triple_essentiality]
- **0.725 AUC**: ROC AUC of inverted fitness (scope minimal medium) [src: adp1_triple_essentiality]
- **0.344 AUC**: ROC AUC of essentiality fraction (scope rich medium) [src: adp1_triple_essentiality]
- **0.403 AUC**: ROC AUC of essentiality fraction (scope minimal medium) [src: adp1_triple_essentiality]

## Evidence

> | **Fitness (inverted)** | Rich | **0.700** | **FAIR - BEST predictor** | | **Fitness (inverted)** | Minimal | **0.725** | **FAIR - BEST predictor** | | **Proteomics (log2)** | Minimal | **0.743** | **FAIR - VERY GOOD** | | Essentiality Fraction | Rich | 0.344 | **WORSE than random!** | | Essentiality Fraction | Minimal | 0.403 | **WORSE than random!** | [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Aggregated TnSeq essentiality fraction mixes experimental conditions, so condition-matched comparisons may be more informative. [src: adp1_triple_essentiality]

> Essentiality fraction mixes diverse conditions - Condition-matched comparisons are more informative [src: adp1_triple_essentiality]

## Other caveats in this report

- The report cautions that FBA, knockout, TnSeq, proteomics, and growth measurements address distinct biological outcomes. [src: adp1_triple_essentiality]
- The 478-gene triple-covered sample excludes TnSeq-essential genes, limiting its FBA–growth comparison to TnSeq-dispensable genes. [src: adp1_triple_essentiality]
- The FBA-class null persisted through Q35; Q40 produced a marginal p = 0.048 association, while the continuous-rate test remained nonsignificant. [src: adp1_triple_essentiality]
- The glucarate correlation (ρ = +0.246) ran opposite to the predicted direction; the report suggests condition-specific model inaccuracy. [src: adp1_triple_essentiality]
- The per-condition Q25 cutoff and eight-condition ‘any defect’ aggregation inflate background defect prevalence by design; observed prevalence was 72%, versus 90% expected under independence. [src: adp1_triple_essentiality]
