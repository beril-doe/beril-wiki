---
type: "Finding"
description: "RB-TnSeq systematically disagrees with knockout experiments in Acinetobacter baylyi ADP1 (\u03ba<0 across all thresholds), measuring fitness cost rather than lethality."
finding_id: "adp1_triple_essentiality--3264ac68"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "\u03ba<0", "what": "Cohen's kappa between RB-TnSeq and knockout essentiality", "unit": "", "denominator": "", "scope": "all thresholds"}]
caveat: "RB-TnSeq and complete gene deletion capture different biology because transposon insertion is not gene deletion."
first_added: "2026-11-24"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# RB-TnSeq systematically disagrees with knockout essentiality in ADP1

RB-TnSeq systematically disagrees with knockout experiments in Acinetobacter baylyi ADP1 (κ<0 across all thresholds), measuring fitness cost rather than lethality. [src: adp1_triple_essentiality]

## Key figures

- **κ<0**: Cohen's kappa between RB-TnSeq and knockout essentiality (scope all thresholds) [src: adp1_triple_essentiality]

## Evidence

> **RB-TnSeq systematically disagrees** with knockout experiments (κ<0 across all thresholds), measuring fitness cost rather than lethality [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

RB-TnSeq and complete gene deletion capture different biology because transposon insertion is not gene deletion. [src: adp1_triple_essentiality]

> **Interpretation**: RB-TnSeq captures **different biology** than complete gene deletion: - The 211 KO-essential genes that TnSeq calls dispensable likely tolerate partial function from transposon-disrupted genes - The 293 TnSeq-essential but KO-dispensable genes may be fitness-important but not lethal - Transposon insertion ≠ gene deletion [src: adp1_triple_essentiality]

## Other caveats in this report

- All 478 Acinetobacter baylyi ADP1 genes with TnSeq, FBA, and growth data are TnSeq-dispensable on minimal media, restricting the original analysis to growth effects among dispensable genes. [src: adp1_triple_essentiality]
- The report explains that TnSeq-essential Acinetobacter baylyi ADP1 genes lack viable deletion mutants and therefore cannot have growth rate measurements. [src: adp1_triple_essentiality]
- The positive glucarate flux–growth correlation in Acinetobacter baylyi ADP1 is opposite to prediction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]
- The Acinetobacter baylyi ADP1 Q25 growth-defect threshold flags ~25% of genes per condition, so aggregating any defect across 8 conditions creates a high background rate by design, with expected 1 − 0.75⁸ = 90% under independence versus observed 72%. [src: adp1_triple_essentiality]
- The original Acinetobacter baylyi ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
