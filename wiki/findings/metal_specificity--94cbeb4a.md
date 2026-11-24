---
type: "Finding"
description: "Metal-specific genes are 1.64x more likely than general sick genes to match metal-resistance keywords such as efflux, transporter, metal, CDF, and siderophore (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8)."
finding_id: "metal_specificity--94cbeb4a"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "12.2% vs 7.8%", "what": "metal-resistance keyword match, metal-specific vs general sick", "unit": "", "denominator": "", "scope": ""}, {"value": "OR=1.64", "what": "Fisher exact odds ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 5% sick-rate threshold is arbitrary, and results are qualitatively stable across 1-20% but exact fractions vary."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Metal-specific genes are enriched for metal-resistance keywords versus general sick genes

Metal-specific genes are 1.64x more likely than general sick genes to match metal-resistance keywords such as efflux, transporter, metal, CDF, and siderophore (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity]

## Key figures

- **12.2% vs 7.8%**: metal-resistance keyword match, metal-specific vs general sick [src: metal_specificity]
- **OR=1.64**: Fisher exact odds ratio [src: metal_specificity]

## Evidence

> Metal-specific genes are 1.64x more likely to match metal-resistance keywords (efflux, transporter, metal, CDF, siderophore, etc.) than general sick genes (12.2% vs 7.8%, Fisher exact OR=1.64, p=2.4e-8). [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

The 5% sick-rate threshold is arbitrary, and results are qualitatively stable across 1-20% but exact fractions vary. [src: metal_specificity]

> **Threshold sensitivity**: The 5% sick-rate threshold is arbitrary. Results are qualitatively stable across 1-20% but exact fractions vary. [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment; the report says true baseline core fraction is likely lower than 81%, making reported deltas conservative. [src: metal_specificity]
- The report attributes lower novel-candidate metal-specificity to many candidates being identified in deeply-profiled organisms DvH, Btheta, and psRCH2, where more experiments provide more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]
