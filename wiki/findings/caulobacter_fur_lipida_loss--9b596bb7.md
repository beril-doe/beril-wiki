---
type: "Finding"
description: "Caulobacter Path B (SspB-buffered, cbb3/fix-rich) has 9 phenotype-bearing genes out of 26, or 34.6%, with background-corrected enrichment fold = 1.04\u00d7, p = 0.515, indistinguishable from background."
finding_id: "caulobacter_fur_lipida_loss--9b596bb7"
result: "null result"
source: "caulobacter_fur_lipida_loss"
quantities: [{"value": "34.6%", "what": "Path B phenotype-bearing rate", "unit": "", "denominator": "26 genes", "scope": ""}, {"value": "fold = 1.04\u00d7, p = 0.515", "what": "enrichment vs background", "unit": "", "denominator": "", "scope": ""}]
caveat: "The iron-limitation arm of H2 could not be tested because the Caulobacter fitness compendium contains zero iron-limitation experiments, so H2 was restricted to the envelope axis."
first_added: "2026-11-24"
source_hash: "ef8e4c5759abd14a915e18706ba9283e83019f0c753991a823669cf1d213b8cd"
---
# SspB-buffered Path B genes are not enriched for envelope-stress fitness phenotypes

Caulobacter Path B (SspB-buffered, cbb3/fix-rich) has 9 phenotype-bearing genes out of 26, or 34.6%, with background-corrected enrichment fold = 1.04×, p = 0.515, indistinguishable from background. [src: caulobacter_fur_lipida_loss]

## Key figures

- **34.6%**: Path B phenotype-bearing rate (denominator 26 genes) [src: caulobacter_fur_lipida_loss]
- **fold = 1.04×, p = 0.515**: enrichment vs background [src: caulobacter_fur_lipida_loss]

## Evidence

> | Path B (SspB-buffered, cbb3/*fix*-rich) | 26 | 9 | 34.6% | fold = 1.04×, p = 0.515 | **indistinguishable from background** | [src: caulobacter_fur_lipida_loss]

From the report [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Caveat

The iron-limitation arm of H2 could not be tested because the Caulobacter fitness compendium contains zero iron-limitation experiments, so H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]

> Caulobacter RB-TnSeq fitness data (`kescience_fitnessbrowser`, orgId=`Caulo`, 198 experiments) ranks the Fur-released gene sets by phenotypic importance under envelope stress (the iron-limitation arm could not be tested — zero iron-limitation experiments in the compendium; H2 was descoped to envelope-axis-only per the plan's preflight rule). [src: caulobacter_fur_lipida_loss]

## Other caveats in this report

- The report regards ΔsspB-mediated respiratory protection in Caulobacter crescentus as a plausible hypothesis rather than a statistically supported mechanism of Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The pre-registered ≥10% phenotype threshold lies below the Caulobacter genome-background rate, making threshold passage alone uninformative about specific mechanistic importance. [src: caulobacter_fur_lipida_loss]
- Although ΔsspB buffering of respiratory-chain genes is real at the Caulobacter transcript level, fitness data do not independently support this set as mechanistically critical for Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The report demotes the assertion that respiratory ATP is required for Caulobacter Δlpxc rescue from an established finding to a working hypothesis. [src: caulobacter_fur_lipida_loss]
- Earlier drafts conflated 20 unique-to-early and 10 both-phase Caulobacter ChvI genes as 30 early genes; the corrected disjoint partition is 20 + 10 + 49 = 79 engaged ChvI-induced genes. [src: caulobacter_fur_lipida_loss]
