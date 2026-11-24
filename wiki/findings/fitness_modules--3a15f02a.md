---
type: "Finding"
description: "The fitness-module analysis generated 6,691 function predictions for hypothetical proteins across all 32 organisms."
finding_id: "fitness_modules--3a15f02a"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "6,691", "what": "function predictions for hypothetical proteins", "unit": "predictions", "denominator": "", "scope": "32 organisms"}]
caveat: "Function predictions should be interpreted as biological process context, not exact KO assignments."
first_added: "2026-11-24"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Modules yield thousands of function predictions for hypothetical proteins

The fitness-module analysis generated 6,691 function predictions for hypothetical proteins across all 32 organisms. [src: fitness_modules]

## Key figures

- **6,691 predictions**: function predictions for hypothetical proteins (scope 32 organisms) [src: fitness_modules]

## Evidence

> **6,691 function predictions** for hypothetical proteins across all 32 organisms [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

Function predictions should be interpreted as biological process context, not exact KO assignments. [src: fitness_modules]

> Function predictions should be interpreted as biological process context, not exact KO assignments. [src: fitness_modules]

## Other caveats in this report

- KEGG KOs were too gene-specific for fitness-module-level enrichment. [src: fitness_modules]
- Module-ICA should not be used to predict specific molecular functions, for which ortholog transfer is far superior. [src: fitness_modules]
- Organisms with fewer than ~100 experiments produce weaker fitness modules; the report gives Caulo with 198 experiments and only 2.9x correlation enrichment as an example. [src: fitness_modules]
- The component cap of 40% (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss modules in low-experiment organisms. [src: fitness_modules]
- PFam annotations offer the best coverage but are domain-level and may overcount functional associations. [src: fitness_modules]
