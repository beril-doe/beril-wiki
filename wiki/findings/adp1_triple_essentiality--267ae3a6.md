---
type: "Finding"
description: "Acinetobacter baylyi ADP1 proteomics strongly correlates with essentiality (r=0.35, AUC=0.74): essential genes are expressed 6.5-fold higher."
finding_id: "adp1_triple_essentiality--267ae3a6"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "r=0.35", "what": "correlation of expression with essentiality", "unit": "", "denominator": "", "scope": ""}, {"value": "AUC=0.74", "what": "ROC AUC of proteomics", "unit": "", "denominator": "", "scope": ""}, {"value": "6.5-fold", "what": "higher expression in essential genes", "unit": "", "denominator": "", "scope": ""}]
caveat: "Knockout experiments are the best proxy for lethality, while fitness, expression, and growth rates reveal additional biology."
first_added: "2026-11-24"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# Proteomic expression tracks knockout essentiality in ADP1

Acinetobacter baylyi ADP1 proteomics strongly correlates with essentiality (r=0.35, AUC=0.74): essential genes are expressed 6.5-fold higher. [src: adp1_triple_essentiality]

## Key figures

- **r=0.35**: correlation of expression with essentiality [src: adp1_triple_essentiality]
- **AUC=0.74**: ROC AUC of proteomics [src: adp1_triple_essentiality]
- **6.5-fold**: higher expression in essential genes [src: adp1_triple_essentiality]

## Evidence

> **Proteomics strongly correlates** with essentiality (r=0.35, AUC=0.74): essential genes are expressed 6.5-fold higher [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Knockout experiments are the best proxy for lethality, while fitness, expression, and growth rates reveal additional biology. [src: adp1_triple_essentiality]

> - Knockout experiments are best proxy for lethality - But fitness, expression, and growth rates reveal additional biology [src: adp1_triple_essentiality]

## Other caveats in this report

- All 478 Acinetobacter baylyi ADP1 genes with TnSeq, FBA, and growth data are TnSeq-dispensable on minimal media, restricting the original analysis to growth effects among dispensable genes. [src: adp1_triple_essentiality]
- The report explains that TnSeq-essential Acinetobacter baylyi ADP1 genes lack viable deletion mutants and therefore cannot have growth rate measurements. [src: adp1_triple_essentiality]
- The positive glucarate flux–growth correlation in Acinetobacter baylyi ADP1 is opposite to prediction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]
- The Acinetobacter baylyi ADP1 Q25 growth-defect threshold flags ~25% of genes per condition, so aggregating any defect across 8 conditions creates a high background rate by design, with expected 1 − 0.75⁸ = 90% under independence versus observed 72%. [src: adp1_triple_essentiality]
- The original Acinetobacter baylyi ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
