---
type: "Finding"
description: "FBA shows moderate concordance with experimental Acinetobacter baylyi ADP1 knockouts (\u03ba\u22480.49, F1\u22480.62-0.67)."
finding_id: "adp1_triple_essentiality--d1af4698"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "\u03ba\u22480.49", "what": "Cohen's kappa FBA vs knockout", "unit": "", "denominator": "", "scope": ""}, {"value": "F1\u22480.62-0.67", "what": "F1 score", "unit": "", "denominator": "", "scope": ""}]
caveat: "FBA is a threshold classifier predicting whether a knockout reduces growth to zero, not the magnitude of growth reduction."
first_added: "2026-11-24"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# FBA moderately matches ADP1 knockout essentiality

FBA shows moderate concordance with experimental Acinetobacter baylyi ADP1 knockouts (κ≈0.49, F1≈0.62-0.67). [src: adp1_triple_essentiality]

## Key figures

- **κ≈0.49**: Cohen's kappa FBA vs knockout [src: adp1_triple_essentiality]
- **F1≈0.62-0.67**: F1 score [src: adp1_triple_essentiality]

## Evidence

> **FBA shows moderate concordance** with experimental knockouts (κ≈0.49, F1≈0.62-0.67) but **does not predict growth defects** among TnSeq-dispensable genes (p=0.63) [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

FBA is a threshold classifier predicting whether a knockout reduces growth to zero, not the magnitude of growth reduction. [src: adp1_triple_essentiality]

> 1. **FBA is a threshold classifier**: FBA predicts whether a gene knockout reduces growth to **zero** (lethal), not the magnitude of growth reduction [src: adp1_triple_essentiality]

## Other caveats in this report

- All 478 Acinetobacter baylyi ADP1 genes with TnSeq, FBA, and growth data are TnSeq-dispensable on minimal media, restricting the original analysis to growth effects among dispensable genes. [src: adp1_triple_essentiality]
- The report explains that TnSeq-essential Acinetobacter baylyi ADP1 genes lack viable deletion mutants and therefore cannot have growth rate measurements. [src: adp1_triple_essentiality]
- The positive glucarate flux–growth correlation in Acinetobacter baylyi ADP1 is opposite to prediction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]
- The Acinetobacter baylyi ADP1 Q25 growth-defect threshold flags ~25% of genes per condition, so aggregating any defect across 8 conditions creates a high background rate by design, with expected 1 − 0.75⁸ = 90% under independence versus observed 72%. [src: adp1_triple_essentiality]
- The original Acinetobacter baylyi ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
