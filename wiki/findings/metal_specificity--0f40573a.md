---
type: "Finding"
description: "Across 24 organisms with fitness matrix data, 4,177 (54.9%) of 7,609 metal-important gene records are metal-specific, showing significant metal-stress fitness defects but a <5% sick rate across 5,945 non-metal experiments."
finding_id: "metal_specificity--0f40573a"
result: "observation"
source: "metal_specificity"
quantities: [{"value": "4,177 (54.9%)", "what": "metal-specific gene records", "unit": "", "denominator": "7,609 metal-important gene records", "scope": "24 organisms"}, {"value": "5,945", "what": "non-metal experiments used for sick rate", "unit": "", "denominator": "", "scope": ""}]
caveat: "The report notes 40.7% gene attrition: 7 organisms and 5,229 gene records were excluded for locusId format mismatches, and excluded genes may differ in specificity."
first_added: "2026-11-24"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Over half of metal-important genes are metal-specific across organisms

Across 24 organisms with fitness matrix data, 4,177 (54.9%) of 7,609 metal-important gene records are metal-specific, showing significant metal-stress fitness defects but a <5% sick rate across 5,945 non-metal experiments. [src: metal_specificity]

## Key figures

- **4,177 (54.9%)**: metal-specific gene records (denominator 7,609 metal-important gene records; scope 24 organisms) [src: metal_specificity]
- **5,945**: non-metal experiments used for sick rate [src: metal_specificity]

## Evidence

> Of the 7,609 metal-important gene records with fitness matrix data across 24 organisms, 4,177 (54.9%) are metal-specific — they show significant fitness defects under metal stress but a <5% sick rate across 5,945 non-metal experiments. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

The report notes 40.7% gene attrition: 7 organisms and 5,229 gene records were excluded for locusId format mismatches, and excluded genes may differ in specificity. [src: metal_specificity]

> **40.7% gene attrition**: 7 organisms and 5,229 gene records were excluded due to locusId format mismatches between the metal atlas and fitness matrices. These excluded organisms include Keio (*E. coli*), MR1 (*Shewanella*), and ANA3 — all important model organisms. The excluded genes may have different specificity profiles. [src: metal_specificity]

## Other caveats in this report

- The report could not process 7 of 31 metal-tested organisms (ANA3, Dino, Keio, MR1, Miya, PV4, SB2B) because metal-important gene locusIds did not match fitness matrix index format. [src: metal_specificity]
- The 24 included organisms account for 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report considers excluded organisms taxonomically diverse and does not expect their absence to introduce systematic bias. [src: metal_specificity]
- Putatively essential genes comprise ~14% of protein-coding genes (~82% core) and are absent from fitness data, biasing all categories toward core enrichment; the report says true baseline core fraction is likely lower than 81%, making reported deltas conservative. [src: metal_specificity]
- The report attributes lower novel-candidate metal-specificity to many candidates being identified in deeply-profiled organisms DvH, Btheta, and psRCH2, where more experiments provide more opportunities to detect pleiotropic effects and classify genes as general sick. [src: metal_specificity]
