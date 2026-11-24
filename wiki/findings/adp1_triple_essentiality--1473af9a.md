---
type: "Finding"
description: "In the refined Acinetobacter baylyi ADP1 analysis, inverted fitness was a much better essentiality predictor (AUC=0.70-0.73) than essentiality_fraction (AUC=0.34-0.40), which performed worse than random."
finding_id: "adp1_triple_essentiality--1473af9a"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "AUC=0.70-0.73", "what": "inverted fitness ROC AUC for essentiality", "unit": "", "denominator": "", "scope": ""}, {"value": "AUC=0.34-0.40", "what": "essentiality_fraction ROC AUC", "unit": "", "denominator": "", "scope": ""}]
caveat: "Essentiality fraction mixes diverse conditions, and condition-matched comparisons are more informative."
first_added: "2026-11-24"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# Continuous fitness predicts essentiality; essentiality fraction is worse than random

In the refined Acinetobacter baylyi ADP1 analysis, inverted fitness was a much better essentiality predictor (AUC=0.70-0.73) than essentiality_fraction (AUC=0.34-0.40), which performed worse than random. [src: adp1_triple_essentiality]

## Key figures

- **AUC=0.70-0.73**: inverted fitness ROC AUC for essentiality [src: adp1_triple_essentiality]
- **AUC=0.34-0.40**: essentiality_fraction ROC AUC [src: adp1_triple_essentiality]

## Evidence

> - **Refined**: Tested both essentiality_fraction AND fitness (inverted) - Finding: Fitness is MUCH better predictor (AUC=0.70-0.73) than essentiality_fraction (AUC=0.34-0.40) - Essentiality fraction performs WORSE than random! [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Essentiality fraction mixes diverse conditions, and condition-matched comparisons are more informative. [src: adp1_triple_essentiality]

> 4. **Account for condition-specific effects** when aggregating across experiments - Essentiality fraction mixes diverse conditions - Condition-matched comparisons are more informative [src: adp1_triple_essentiality]

## Other caveats in this report

- All 478 Acinetobacter baylyi ADP1 genes with TnSeq, FBA, and growth data are TnSeq-dispensable on minimal media, restricting the original analysis to growth effects among dispensable genes. [src: adp1_triple_essentiality]
- The report explains that TnSeq-essential Acinetobacter baylyi ADP1 genes lack viable deletion mutants and therefore cannot have growth rate measurements. [src: adp1_triple_essentiality]
- The positive glucarate flux–growth correlation in Acinetobacter baylyi ADP1 is opposite to prediction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]
- The Acinetobacter baylyi ADP1 Q25 growth-defect threshold flags ~25% of genes per condition, so aggregating any defect across 8 conditions creates a high background rate by design, with expected 1 − 0.75⁸ = 90% under independence versus observed 72%. [src: adp1_triple_essentiality]
- The original Acinetobacter baylyi ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
