---
type: "Finding"
description: "Across all 149 novel metal candidate families, 45.6% have dominant specificity of metal-specific versus 58.2% for annotated families (Fisher exact OR=0.60, p=0.003), making novel candidates less metal-specific."
finding_id: "metal_specificity--09020647"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "45.6%", "what": "novel families with metal-specific dominant specificity", "unit": "", "denominator": "", "scope": "149 novel families"}, {"value": "58.2%", "what": "annotated families metal-specific", "unit": "", "denominator": "", "scope": ""}]
caveat: "Many novel candidates were identified in deeply-profiled organisms (DvH, Btheta, psRCH2), where more experiments give more opportunities to detect pleiotropic effects and classify genes as general sick."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Novel metal candidate families are less metal-specific than annotated ones

Across all 149 novel metal candidate families, 45.6% have dominant specificity of metal-specific versus 58.2% for annotated families (Fisher exact OR=0.60, p=0.003), making novel candidates less metal-specific. [src: metal_specificity]

## Key figures

- **45.6%**: novel families with metal-specific dominant specificity (scope 149 novel families) [src: metal_specificity]
- **58.2%**: annotated families metal-specific [src: metal_specificity]

## Evidence

> Across all 149 novel metal candidate families, 45.6% have a dominant specificity of "metal-specific" — compared to 58.2% for annotated families (Fisher exact OR=0.60, p=0.003). Novel candidates are less metal-specific than annotated ones. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

Many novel candidates were identified in deeply-profiled organisms (DvH, Btheta, psRCH2), where more experiments give more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]

> This reflects the composition of the novel set: many novel candidates were identified in deeply-profiled organisms (DvH, Btheta, psRCH2) where the high experiment count provides more opportunities to detect pleiotropic effects, pushing genes toward "general sick." [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment; the report says true baseline core fraction is likely lower than 81%, making reported deltas conservative. [src: metal_specificity]
- Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments comprise a small fraction of each organism's experiments. [src: metal_specificity]
