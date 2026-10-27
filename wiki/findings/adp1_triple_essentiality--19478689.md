---
type: "Finding"
description: "Protein expression correlated with essentiality (Pearson r = 0.345, p = 5.32\u00d710\u207b\u2076\u2075; Spearman \u03c1 = 0.338, p = 3.28\u00d710\u207b\u2076\u00b2) and gave ROC AUC = 0.743."
finding_id: "adp1_triple_essentiality--19478689"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "0.345", "what": "Pearson r between expression and essentiality", "unit": "r", "denominator": "", "scope": ""}, {"value": "0.338", "what": "Spearman rho between expression and essentiality", "unit": "rho", "denominator": "", "scope": ""}, {"value": "0.743", "what": "ROC AUC of proteomics for essentiality", "unit": "AUC", "denominator": "", "scope": ""}]
caveat: "Proteomics input was average log2 expression across 7 Acinetobacter strains for 2,383 genes, not an ADP1-only measurement."
first_added: "2026-10-27"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# Protein expression correlates with knockout essentiality and classifies it fairly

Protein expression correlated with essentiality (Pearson r = 0.345, p = 5.32×10⁻⁶⁵; Spearman ρ = 0.338, p = 3.28×10⁻⁶²) and gave ROC AUC = 0.743. [src: adp1_triple_essentiality]

## Key figures

- **0.345 r**: Pearson r between expression and essentiality [src: adp1_triple_essentiality]
- **0.338 rho**: Spearman rho between expression and essentiality [src: adp1_triple_essentiality]
- **0.743 AUC**: ROC AUC of proteomics for essentiality [src: adp1_triple_essentiality]

## Evidence

> - **Pearson r**: 0.345 (p = 5.32×10⁻⁶⁵) - **Spearman ρ**: 0.338 (p = 3.28×10⁻⁶²) - **ROC AUC**: 0.743 (FAIR-to-GOOD predictor) [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Proteomics input was average log2 expression across 7 Acinetobacter strains for 2,383 genes, not an ADP1-only measurement. [src: adp1_triple_essentiality]

> 3. **Proteomics**: Average log2 expression across 7 *Acinetobacter* strains (2,383 genes) [src: adp1_triple_essentiality]

## Other caveats in this report

- The report cautions that FBA, knockout, TnSeq, proteomics, and growth measurements address distinct biological outcomes. [src: adp1_triple_essentiality]
- The 478-gene triple-covered sample excludes TnSeq-essential genes, limiting its FBA–growth comparison to TnSeq-dispensable genes. [src: adp1_triple_essentiality]
- The FBA-class null persisted through Q35; Q40 produced a marginal p = 0.048 association, while the continuous-rate test remained nonsignificant. [src: adp1_triple_essentiality]
- The glucarate correlation (ρ = +0.246) ran opposite to the predicted direction; the report suggests condition-specific model inaccuracy. [src: adp1_triple_essentiality]
- The per-condition Q25 cutoff and eight-condition ‘any defect’ aggregation inflate background defect prevalence by design; observed prevalence was 72%, versus 90% expected under independence. [src: adp1_triple_essentiality]
