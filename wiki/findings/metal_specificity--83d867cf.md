---
type: "Finding"
description: "The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules."
finding_id: "metal_specificity--83d867cf"
result: "null result"
source: "metal_specificity"
quantities: [{"value": "0", "what": "metal-specific modules found", "unit": "modules", "denominator": "", "scope": "z-scored activity profiles"}]
caveat: "Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of total experiments per organism, limiting detection."
first_added: "2026-10-27"
source_hash: "8555e9245da861451c7bb26e5536567914d3b5cdeeaddefdd4919d2eb6810e89"
---
# Module-level analysis found no metal-specific modules

The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules. [src: metal_specificity]

## Key figures

- **0 modules**: metal-specific modules found (scope z-scored activity profiles) [src: metal_specificity]

## Evidence

> The module-level specificity analysis using z-scored activity profiles found 0 metal-specific modules. [src: metal_specificity]

From the report [[summaries/metal_specificity__REPORT]].

## Caveat

Per-module z-normalization produced max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of total experiments per organism, limiting detection. [src: metal_specificity]

> The per-module z-normalization produces max |z| values < 2.0 for most metal experiments because metal experiments are a small fraction of total experiments per organism. [src: metal_specificity]

## Other caveats in this report

- The metal-specific fraction was ~41% at a 2% sick-rate cutoff and ~67% at 10%. [src: metal_specificity]
- Seven of 31 metal-tested organisms were excluded because locusId formats did not match fitness-matrix indices. [src: metal_specificity]
- Included organisms represented 7,609 of 12,838 metal-important gene records (59.3%). [src: metal_specificity]
- The report expects no systematic bias from the taxonomically diverse exclusions, but does not establish that empirically. [src: metal_specificity]
- The conservation analysis covered 22 organisms with pangenome links and distinguished pooled from organism-mean core fractions. [src: metal_specificity]
