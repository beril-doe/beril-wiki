---
type: "Finding"
description: "53 of the 93 Leaden \u0394fur DEGs are buffered in the report's data (logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden), and the buffered set is dominated by the cbb3 / cyd / fix-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476, ccoNOPQ, cydCDA, fixG/H/I)."
finding_id: "caulobacter_fur_lipida_loss--088e2303"
result: "observation"
source: "caulobacter_fur_lipida_loss"
quantities: [{"value": "53 of 93", "what": "Leaden \u0394fur DEGs buffered in 4584-vs-4580", "unit": "genes", "denominator": "93 Leaden \u0394fur DEGs", "scope": "Caulobacter"}, {"value": "-5 to -9", "what": "logFC of the buffered genes in Leaden", "unit": "logFC", "denominator": "", "scope": ""}]
caveat: "The transcript-level \u0394sspB buffering effect on the respiratory chain is real, but whether these specific genes are mechanistically critical for the \u0394lpxc rescue is not established by the fitness data alone."
first_added: "2026-10-27"
source_hash: "ef8e4c5759abd14a915e18706ba9283e83019f0c753991a823669cf1d213b8cd"
---
# ΔsspB buffers a Fur-dependent respiratory operon at transcript level

53 of the 93 Leaden Δfur DEGs are buffered in the report's data (logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden), and the buffered set is dominated by the cbb3 / cyd / fix-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476, ccoNOPQ, cydCDA, fixG/H/I). [src: caulobacter_fur_lipida_loss]

## Key figures

- **53 of 93 genes**: Leaden Δfur DEGs buffered in 4584-vs-4580 (denominator 93 Leaden Δfur DEGs; scope Caulobacter) [src: caulobacter_fur_lipida_loss]
- **-5 to -9 logFC**: logFC of the buffered genes in Leaden [src: caulobacter_fur_lipida_loss]

## Evidence

> 53 of those 93 Leaden Δ*fur* DEGs are *buffered* in our data (logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden), and the buffered set is dominated by the **cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon** (CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, *fixG/H/I*). [src: caulobacter_fur_lipida_loss]

From the report [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Caveat

The transcript-level ΔsspB buffering effect on the respiratory chain is real, but whether these specific genes are mechanistically critical for the Δlpxc rescue is not established by the fitness data alone. [src: caulobacter_fur_lipida_loss]

> The transcript-level Δ*sspB* buffering effect on the respiratory chain is real, but **whether these specific genes are mechanistically critical for the Δ*lpxc* rescue is not established by the fitness data alone** (see Finding 2 and Limitations). [src: caulobacter_fur_lipida_loss]

## Other caveats in this report

- The Fur arm is supported; SspB-mediated respiratory protection remains a hypothesis. [src: caulobacter_fur_lipida_loss]
- Passing the pre-registered ≥10% threshold alone cannot establish enrichment above genomic background. [src: caulobacter_fur_lipida_loss]
- The disjoint ChvI partition is 20 unique-early, 10 both-phase, and 49 late genes, totaling 79; an earlier label conflated the first two groups. [src: caulobacter_fur_lipida_loss]
- The report found no substantive published Caulobacter SigU reference for CCNA_02977; SigU as a late-cohort driver remains unvalidated. [src: caulobacter_fur_lipida_loss]
- CtpA failed the pre-registered borderline criterion because pvalue=0.048 was below its lower bound and protein was not detected. [src: caulobacter_fur_lipida_loss]
