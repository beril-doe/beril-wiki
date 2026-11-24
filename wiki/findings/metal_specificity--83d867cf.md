---
type: "Finding"
description: "The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules."
finding_id: "metal_specificity--83d867cf"
result: "null result"
source: "metal_specificity"
quantities: [{"value": "0", "what": "metal-specific modules found", "unit": "", "denominator": "", "scope": ""}]
caveat: "Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of each organism's experiments."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# No metal-specific ICA modules found in module-level analysis

The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules. [src: metal_specificity]

## Key figures

- **0**: metal-specific modules found [src: metal_specificity]

## Evidence

> The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of each organism's experiments. [src: metal_specificity]

> The per-module z-normalization produces max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of total experiments per organism. [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment; the report says true baseline core fraction is likely lower than 81%, making reported deltas conservative. [src: metal_specificity]
- The report attributes lower novel-candidate metal-specificity to many candidates being identified in deeply-profiled organisms DvH, Btheta, and psRCH2, where more experiments provide more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]
