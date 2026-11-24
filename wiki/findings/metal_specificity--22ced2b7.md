---
type: "Finding"
description: "The Cochran-Mantel-Haenszel test finds metal-specific genes less core-enriched than general sick genes across organisms (p=0.011)."
finding_id: "metal_specificity--22ced2b7"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "p=0.011", "what": "CMH test, metal-specific vs general sick core enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment, so reported deltas are conservative."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Metal-specific genes are less core-enriched than general sick genes

The Cochran-Mantel-Haenszel test finds metal-specific genes less core-enriched than general sick genes across organisms (p=0.011). [src: metal_specificity]

## Key figures

- **p=0.011**: CMH test, metal-specific vs general sick core enrichment [src: metal_specificity]

## Evidence

> The Cochran-Mantel-Haenszel test comparing metal-specific vs general-sick core enrichment across organisms is statistically significant (p=0.011), confirming that metal-specific genes are less core-enriched than general sick genes across organisms. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment, so reported deltas are conservative. [src: metal_specificity]

> ~14% of protein-coding genes (~82% core) are putatively essential and absent from fitness data. This biases all categories toward core enrichment — the true baseline core fraction is likely lower than 81%, making the reported deltas conservative. [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- The report attributes lower novel-candidate metal-specificity to many candidates being identified in deeply-profiled organisms DvH, Btheta, and psRCH2, where more experiments provide more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]
- Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments comprise a small fraction of each organism's experiments. [src: metal_specificity]
