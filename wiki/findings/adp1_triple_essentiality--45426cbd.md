---
type: "Finding"
description: "Aromatic degradation discordance is predominantly FBA under-prediction: genes assigned zero flux nonetheless show deletion growth defects (directional OR = 12.0, q = 0.004)."
finding_id: "adp1_triple_essentiality--45426cbd"
result: "observation"
source: "adp1_triple_essentiality"
quantities: [{"value": "12.0", "what": "directional odds ratio for FBA under-prediction in aromatic degradation", "unit": "OR", "denominator": "", "scope": ""}, {"value": "0.004", "what": "q-value of the directional analysis", "unit": "q", "denominator": "", "scope": ""}]
caveat: "Absent modeled aromatic substrates, trace aromatics in experimental media, and moonlighting functions are proposed explanations for growth defects despite predicted zero flux; the cause is unresolved."
first_added: "2026-10-27"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# Aromatic degradation discordance is mostly FBA under-prediction

Aromatic degradation discordance is predominantly FBA under-prediction: genes assigned zero flux nonetheless show deletion growth defects (directional OR = 12.0, q = 0.004). [src: adp1_triple_essentiality]

## Key figures

- **12.0 OR**: directional odds ratio for FBA under-prediction in aromatic degradation [src: adp1_triple_essentiality]
- **0.004 q**: q-value of the directional analysis [src: adp1_triple_essentiality]

## Evidence

> - Almost all are **FBA-under-predicted** (blocked + growth defect) - FBA model assigns zero flux to these genes - Yet their deletion impairs growth - Directional analysis: aromatic degradation OR = 12.0, q = 0.004 for FBA-under-prediction [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Absent modeled aromatic substrates, trace aromatics in experimental media, and moonlighting functions are proposed explanations for growth defects despite predicted zero flux; the cause is unresolved. [src: adp1_triple_essentiality]

> - FBA predicts zero flux (blocked) because minimal media lacks aromatic substrates - But experimental media contain trace aromatics or genes have moonlighting functions - These genes show growth defects despite FBA predicting dispensability [src: adp1_triple_essentiality]

## Other caveats in this report

- The report cautions that FBA, knockout, TnSeq, proteomics, and growth measurements address distinct biological outcomes. [src: adp1_triple_essentiality]
- The 478-gene triple-covered sample excludes TnSeq-essential genes, limiting its FBA–growth comparison to TnSeq-dispensable genes. [src: adp1_triple_essentiality]
- The FBA-class null persisted through Q35; Q40 produced a marginal p = 0.048 association, while the continuous-rate test remained nonsignificant. [src: adp1_triple_essentiality]
- The glucarate correlation (ρ = +0.246) ran opposite to the predicted direction; the report suggests condition-specific model inaccuracy. [src: adp1_triple_essentiality]
- The per-condition Q25 cutoff and eight-condition ‘any defect’ aggregation inflate background defect prevalence by design; observed prevalence was 72%, versus 90% expected under independence. [src: adp1_triple_essentiality]
