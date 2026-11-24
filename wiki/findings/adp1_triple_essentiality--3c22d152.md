---
type: "Finding"
description: "None of the 5 tested Acinetobacter baylyi ADP1 RB-TnSeq thresholds (0.01, 0.025, 0.05, 0.10, 0.20) showed positive kappa, so threshold choice did not resolve TnSeq\u2013knockout discordance."
finding_id: "adp1_triple_essentiality--3c22d152"
result: "null result"
source: "adp1_triple_essentiality"
quantities: [{"value": "5", "what": "thresholds tested", "unit": "", "denominator": "", "scope": ""}]
caveat: "Five thresholds were tested without formal multiple-testing correction."
first_added: "2026-11-24"
source_hash: "5b0b80cbb8215ef660717892ae828f95ef135b781bd6f7024b19d981c94fe52f"
---
# No RB-TnSeq threshold rescues agreement with knockouts

None of the 5 tested Acinetobacter baylyi ADP1 RB-TnSeq thresholds (0.01, 0.025, 0.05, 0.10, 0.20) showed positive kappa, so threshold choice did not resolve TnSeq–knockout discordance. [src: adp1_triple_essentiality]

## Key figures

- **5**: thresholds tested [src: adp1_triple_essentiality]

## Evidence

> - **Refined**: Tested 5 thresholds (0.01, 0.025, 0.05, 0.10, 0.20) based on essentiality_fraction distribution - Distribution analysis: mean=0.026, median=0.0 - Identified optimal threshold for concordance (none showed positive kappa!) - Revealed that threshold choice doesn't resolve TnSeq-KO discordance [src: adp1_triple_essentiality]

From the report [[summaries/adp1_triple_essentiality__REPORT]].

## Caveat

Five thresholds were tested without formal multiple-testing correction. [src: adp1_triple_essentiality]

> **Multiple testing note**: Five thresholds were tested without formal multiple-testing correction. [src: adp1_triple_essentiality]

## Other caveats in this report

- All 478 Acinetobacter baylyi ADP1 genes with TnSeq, FBA, and growth data are TnSeq-dispensable on minimal media, restricting the original analysis to growth effects among dispensable genes. [src: adp1_triple_essentiality]
- The report explains that TnSeq-essential Acinetobacter baylyi ADP1 genes lack viable deletion mutants and therefore cannot have growth rate measurements. [src: adp1_triple_essentiality]
- The positive glucarate flux–growth correlation in Acinetobacter baylyi ADP1 is opposite to prediction and suggests condition-specific model inaccuracies. [src: adp1_triple_essentiality]
- The Acinetobacter baylyi ADP1 Q25 growth-defect threshold flags ~25% of genes per condition, so aggregating any defect across 8 conditions creates a high background rate by design, with expected 1 − 0.75⁸ = 90% under independence versus observed 72%. [src: adp1_triple_essentiality]
- The original Acinetobacter baylyi ADP1 study had no direct lethality measurements and used TnSeq as a proxy. [src: adp1_triple_essentiality]
