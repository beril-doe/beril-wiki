---
type: "Finding"
description: "In Caulobacter crescentus, 53 of the 93 Leaden \u0394fur DEGs are buffered at logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden, and the buffered set is dominated by the cbb3 / cyd / fix-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476)."
finding_id: "caulobacter_fur_lipida_loss--088e2303"
result: "observation"
source: "caulobacter_fur_lipida_loss"
quantities: [{"value": "53 of those 93", "what": "Leaden \u0394fur DEGs buffered in 4584-vs-4580", "unit": "genes", "denominator": "93 Leaden \u0394fur DEGs", "scope": "Caulobacter crescentus"}, {"value": "-5 to -9", "what": "logFC of these genes in Leaden", "unit": "logFC", "denominator": "", "scope": ""}]
caveat: "The \u0394sspB-buffering effect on these genes is real at the transcript level, but the fitness data do not independently support this set as mechanistically critical for the \u0394lpxc rescue."
first_added: "2026-11-24"
source_hash: "ef8e4c5759abd14a915e18706ba9283e83019f0c753991a823669cf1d213b8cd"
---
# Many Fur-dependent transcripts are buffered, led by the cbb3/fix respiratory operon

In Caulobacter crescentus, 53 of the 93 Leaden Δfur DEGs are buffered at logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden, and the buffered set is dominated by the cbb3 / cyd / fix-NOPQ micro-aerobic respiratory operon (CCNA_01466-01476). [src: caulobacter_fur_lipida_loss]

## Key figures

- **53 of those 93 genes**: Leaden Δfur DEGs buffered in 4584-vs-4580 (denominator 93 Leaden Δfur DEGs; scope Caulobacter crescentus) [src: caulobacter_fur_lipida_loss]
- **-5 to -9 logFC**: logFC of these genes in Leaden [src: caulobacter_fur_lipida_loss]

## Evidence

> 53 of those 93 Leaden Δ*fur* DEGs are *buffered* in our data (logFC ~0 in 4584-vs-4580 despite -5 to -9 in Leaden), and the buffered set is dominated by the **cbb3 / cyd / *fix*-NOPQ micro-aerobic respiratory operon** (CCNA_01466-01476, *ccoNOPQ*, *cydCDA*, *fixG/H/I*). [src: caulobacter_fur_lipida_loss]

From the report [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Caveat

The ΔsspB-buffering effect on these genes is real at the transcript level, but the fitness data do not independently support this set as mechanistically critical for the Δlpxc rescue. [src: caulobacter_fur_lipida_loss]

> The Δ*sspB*-buffering effect on these genes is real at the transcript level (NB01) but the fitness data do not provide independent support that this specific set is mechanistically critical for the Δ*lpxc* rescue. [src: caulobacter_fur_lipida_loss]

## Other caveats in this report

- The report regards ΔsspB-mediated respiratory protection in Caulobacter crescentus as a plausible hypothesis rather than a statistically supported mechanism of Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The iron-limitation arm of H2 could not be tested because the Caulobacter fitness compendium contains zero iron-limitation experiments, so H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]
- The pre-registered ≥10% phenotype threshold lies below the Caulobacter genome-background rate, making threshold passage alone uninformative about specific mechanistic importance. [src: caulobacter_fur_lipida_loss]
- The report demotes the assertion that respiratory ATP is required for Caulobacter Δlpxc rescue from an established finding to a working hypothesis. [src: caulobacter_fur_lipida_loss]
- Earlier drafts conflated 20 unique-to-early and 10 both-phase Caulobacter ChvI genes as 30 early genes; the corrected disjoint partition is 20 + 10 + 49 = 79 engaged ChvI-induced genes. [src: caulobacter_fur_lipida_loss]
