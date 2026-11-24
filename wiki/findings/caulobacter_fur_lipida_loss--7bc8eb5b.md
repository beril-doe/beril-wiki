---
type: "Finding"
description: "Caulobacter crescentus peptidoglycan remodeling was predominantly downregulated (20 DOWN) with specific inductions (5 UP transcript + 3 UP protein); the earlier framing of coordinated bidirectional reorganization overstated the bidirectionality."
finding_id: "caulobacter_fur_lipida_loss--7bc8eb5b"
result: "correction"
source: "caulobacter_fur_lipida_loss"
quantities: [{"value": "20 DOWN", "what": "downregulated peptidoglycan genes", "unit": "", "denominator": "", "scope": ""}]
caveat: "Two likely regex false-positives in the gene set do not change the H4 verdict, which remains well above the \u22653 threshold, but downstream interpretation should not rest on them."
first_added: "2026-11-24"
source_hash: "ef8e4c5759abd14a915e18706ba9283e83019f0c753991a823669cf1d213b8cd"
---
# Peptidoglycan remodeling is mostly shutdown with few specific inductions

Caulobacter crescentus peptidoglycan remodeling was predominantly downregulated (20 DOWN) with specific inductions (5 UP transcript + 3 UP protein); the earlier framing of coordinated bidirectional reorganization overstated the bidirectionality. [src: caulobacter_fur_lipida_loss]

## Key figures

- **20 DOWN**: downregulated peptidoglycan genes [src: caulobacter_fur_lipida_loss]

## Evidence

> Direction is **predominantly downregulation (20 DOWN) punctuated by specific inductions (5 UP transcript + 3 UP protein)** — earlier draft framing of "coordinated bidirectional reorganization" overstated the bidirectionality. [src: caulobacter_fur_lipida_loss]

From the report [[summaries/caulobacter_fur_lipida_loss__REPORT]].

## Caveat

Two likely regex false-positives in the gene set do not change the H4 verdict, which remains well above the ≥3 threshold, but downstream interpretation should not rest on them. [src: caulobacter_fur_lipida_loss]

> Their inclusion does not change the H4 verdict (well above the ≥3 threshold) but they are flagged here so downstream interpretation does not rest on them. [src: caulobacter_fur_lipida_loss]

## Other caveats in this report

- The report regards ΔsspB-mediated respiratory protection in Caulobacter crescentus as a plausible hypothesis rather than a statistically supported mechanism of Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The iron-limitation arm of H2 could not be tested because the Caulobacter fitness compendium contains zero iron-limitation experiments, so H2 was restricted to the envelope axis. [src: caulobacter_fur_lipida_loss]
- The pre-registered ≥10% phenotype threshold lies below the Caulobacter genome-background rate, making threshold passage alone uninformative about specific mechanistic importance. [src: caulobacter_fur_lipida_loss]
- Although ΔsspB buffering of respiratory-chain genes is real at the Caulobacter transcript level, fitness data do not independently support this set as mechanistically critical for Δlpxc rescue. [src: caulobacter_fur_lipida_loss]
- The report demotes the assertion that respiratory ATP is required for Caulobacter Δlpxc rescue from an established finding to a working hypothesis. [src: caulobacter_fur_lipida_loss]
