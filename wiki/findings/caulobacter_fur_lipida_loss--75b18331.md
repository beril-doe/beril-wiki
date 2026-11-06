---
type: "Finding"
description: "No sphingolipid biosynthesis genes were upregulated (0/6 UP); spt was down -0.64 (FDR 0.002) and sphk down -0.40 (FDR 0.02)."
finding_id: "caulobacter_fur_lipida_loss--75b18331"
result: "null result"
source: "caulobacter_fur_lipida_loss"
quantities: [{"value": "0/6", "what": "biosynthesis genes UP", "unit": "genes", "denominator": "6 biosynthesis genes", "scope": ""}, {"value": "-0.64", "what": "spt change (FDR 0.002)", "unit": "", "denominator": "", "scope": ""}, {"value": "-0.40", "what": "sphk change (FDR 0.02)", "unit": "", "denominator": "", "scope": ""}]
caveat: "Transcriptomes were measured only in routine PYE rich medium, so the Fur signal is constitutive \u0394fur derepression, not a real iron-limitation response."
first_added: "2026-10-27"
source_hash: "ef8e4c5759abd14a915e18706ba9283e83019f0c753991a823669cf1d213b8cd"
---
# Sphingolipid biosynthesis is not transcriptionally induced during rescue

No sphingolipid biosynthesis genes were upregulated (0/6 UP); spt was down -0.64 (FDR 0.002) and sphk down -0.40 (FDR 0.02). [src: caulobacter_fur_lipida_loss]

## Key figures

- **0/6 genes**: biosynthesis genes UP (denominator 6 biosynthesis genes) [src: caulobacter_fur_lipida_loss]
- **-0.64**: spt change (FDR 0.002) [src: caulobacter_fur_lipida_loss]
- **-0.40**: sphk change (FDR 0.02) [src: caulobacter_fur_lipida_loss]

## Evidence

> | Sphingolipid biosynthesis pathway constitutive (not induced) | 0/6 biosynthesis genes UP; *spt* DOWN -0.64 FDR 0.002; *sphk* DOWN -0.40 FDR 0.02 | SUPPORTED strongly | [src: caulobacter_fur_lipida_loss]

From the report [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Caveat

Transcriptomes were measured only in routine PYE rich medium, so the Fur signal is constitutive Δfur derepression, not a real iron-limitation response. [src: caulobacter_fur_lipida_loss]

> - **Single growth condition** (PYE rich-medium routine) for the transcriptome — the Fur signal is constitutive Δ*fur* derepression, not a real iron-limitation response. [src: caulobacter_fur_lipida_loss]

## Other caveats in this report

- Transcript buffering is observed, but the fitness data do not establish that these respiratory genes cause Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The Fur arm is supported; SspB-mediated respiratory protection remains a hypothesis. [src: caulobacter_fur_lipida_loss]
- Passing the pre-registered ≥10% threshold alone cannot establish enrichment above genomic background. [src: caulobacter_fur_lipida_loss]
- The disjoint ChvI partition is 20 unique-early, 10 both-phase, and 49 late genes, totaling 79; an earlier label conflated the first two groups. [src: caulobacter_fur_lipida_loss]
- The report found no substantive published Caulobacter SigU reference for CCNA_02977; SigU as a late-cohort driver remains unvalidated. [src: caulobacter_fur_lipida_loss]
