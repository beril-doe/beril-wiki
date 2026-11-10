---
type: "Finding"
description: "Among 478 triple-covered genes (all TnSeq-dispensable), FBA class was not significantly associated with growth defect status (chi-squared = 0.93, p = 0.63, 2 df), with defect rates of 73.1% (57/78), 73.5% (150/204), and 69.4% (136/196) for FBA-essential, FBA-variable, and FBA-blocked classes."
finding_id: "adp1_triple_essentiality--93d338c1"
result: "null result"
source: "adp1_triple_essentiality"
quantities: [{"value": "0.63", "what": "chi-squared p-value for FBA class vs growth defect status", "unit": "", "denominator": "", "scope": "478 genes, 2 df"}, {"value": "73.1%", "what": "growth defect rate, FBA-essential", "unit": "", "denominator": "78 genes", "scope": ""}, {"value": "73.5%", "what": "growth defect rate, FBA-variable", "unit": "", "denominator": "204 genes", "scope": ""}, {"value": "69.4%", "what": "growth defect rate, FBA-blocked", "unit": "", "denominator": "196 genes", "scope": ""}]
caveat: "The FBA-class null persisted through Q35, but Q40 produced a marginal association (p = 0.048), while the continuous-rate Kruskal-Wallis test remained nonsignificant (H = 1.67, p = 0.43)."
first_added: "2026-10-27"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# FBA class does not predict growth defects among TnSeq-dispensable genes

Among 478 triple-covered genes (all TnSeq-dispensable), FBA class was not significantly associated with growth defect status (chi-squared = 0.93, p = 0.63, 2 df), with defect rates of 73.1% (57/78), 73.5% (150/204), and 69.4% (136/196) for FBA-essential, FBA-variable, and FBA-blocked classes. [src: adp1_triple_essentiality]

## Key figures

- **0.63**: chi-squared p-value for FBA class vs growth defect status (scope 478 genes, 2 df) [src: adp1_triple_essentiality]
- **73.1%**: growth defect rate, FBA-essential (denominator 78 genes) [src: adp1_triple_essentiality]
- **73.5%**: growth defect rate, FBA-variable (denominator 204 genes) [src: adp1_triple_essentiality]
- **69.4%**: growth defect rate, FBA-blocked (denominator 196 genes) [src: adp1_triple_essentiality]

## Evidence

> Among 478 triple-covered genes (all TnSeq-dispensable), FBA class was **not significantly associated** with growth defect status (chi-squared = 0.93, p = 0.63, 2 df). Growth defect rates were nearly identical across FBA classes: - **FBA-essential**: 73.1% (57/78 genes) - **FBA-variable**: 73.5% (150/204 genes) - **FBA-blocked**: 69.4% (136/196 genes) [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

The FBA-class null persisted through Q35, but Q40 produced a marginal association (p = 0.048), while the continuous-rate Kruskal-Wallis test remained nonsignificant (H = 1.67, p = 0.43). [src: adp1_triple_essentiality]

> The chi-squared p-value remained above 0.05 for thresholds Q10–Q35. Only at Q40 did a marginal association appear (p = 0.048), driven by a slight divergence in FBA-essential vs FBA-blocked defect rates (90% vs 81%). The threshold-independent Kruskal-Wallis test on continuous mean growth rates confirms no association (H = 1.67, p = 0.43). [src: adp1_triple_essentiality]

## Other caveats in this report

- The report cautions that FBA, knockout, TnSeq, proteomics, and growth measurements address distinct biological outcomes. [src: adp1_triple_essentiality]
- The 478-gene triple-covered sample excludes TnSeq-essential genes, limiting its FBA–growth comparison to TnSeq-dispensable genes. [src: adp1_triple_essentiality]
- The glucarate correlation (ρ = +0.246) ran opposite to the predicted direction; the report suggests condition-specific model inaccuracy. [src: adp1_triple_essentiality]
- The per-condition Q25 cutoff and eight-condition ‘any defect’ aggregation inflate background defect prevalence by design; observed prevalence was 72%, versus 90% expected under independence. [src: adp1_triple_essentiality]
- The original analysis lacked direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
