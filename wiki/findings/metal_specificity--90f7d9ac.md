---
type: "Finding"
description: "The report argues the Metal Atlas's 87.4% core finding was not inflated by general stress genes because removing all pleiotropic genes leaves a metal-specific set that is 88% core."
finding_id: "metal_specificity--90f7d9ac"
result: "correction"
source: "metal_specificity"
quantities: [{"value": "87.4%", "what": "Metal Atlas core fraction", "unit": "", "denominator": "", "scope": ""}, {"value": "88%", "what": "core fraction of metal-specific set", "unit": "", "denominator": "", "scope": ""}]
caveat: "~14% of genes (~82% core) are absent from fitness data, biasing all conservation estimates toward core enrichment."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Metal Atlas core-genome finding is not inflated by general stress genes

The report argues the Metal Atlas's 87.4% core finding was not inflated by general stress genes because removing all pleiotropic genes leaves a metal-specific set that is 88% core. [src: metal_specificity]

## Key figures

- **87.4%**: Metal Atlas core fraction [src: metal_specificity]
- **88%**: core fraction of metal-specific set [src: metal_specificity]

## Evidence

> **The Metal Atlas's 87.4% core finding is not an artifact.** It was not inflated by general stress genes. Even after removing all pleiotropic genes, the remaining metal-specific set is 88% core. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

~14% of genes (~82% core) are absent from fitness data, biasing all conservation estimates toward core enrichment. [src: metal_specificity]

> **Essential genes invisible**: ~14% of genes (~82% core) are absent from fitness data, biasing all conservation estimates toward core enrichment. [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment; the report says true baseline core fraction is likely lower than 81%, making reported deltas conservative. [src: metal_specificity]
- The report attributes lower novel-candidate metal-specificity to many candidates being identified in deeply-profiled organisms DvH, Btheta, and psRCH2, where more experiments provide more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]
