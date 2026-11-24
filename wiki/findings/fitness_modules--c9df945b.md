---
type: "Finding"
description: "Cross-organism alignment identified 156 module families spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21)."
finding_id: "fitness_modules--c9df945b"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "156", "what": "module families spanning 2+ organisms", "unit": "families", "denominator": "", "scope": ""}, {"value": "28", "what": "families spanning 5+ organisms", "unit": "", "denominator": "", "scope": ""}, {"value": "1", "what": "family spanning 21 organisms", "unit": "", "denominator": "", "scope": ""}]
caveat: "Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment)."
first_added: "2026-11-24"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Cross-organism alignment finds module families spanning many bacteria

Cross-organism alignment identified 156 module families spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21). [src: fitness_modules]

## Key figures

- **156 families**: module families spanning 2+ organisms [src: fitness_modules]
- **28**: families spanning 5+ organisms [src: fitness_modules]
- **1**: family spanning 21 organisms [src: fitness_modules]

## Evidence

> **156 module families** spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21) [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment). [src: fitness_modules]

> Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment) [src: fitness_modules]

## Other caveats in this report

- KEGG KOs were too gene-specific for fitness-module-level enrichment. [src: fitness_modules]
- Module-ICA should not be used to predict specific molecular functions, for which ortholog transfer is far superior. [src: fitness_modules]
- Fitness-module function predictions should be interpreted as biological process context rather than exact KO assignments. [src: fitness_modules]
- The component cap of 40% (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss modules in low-experiment organisms. [src: fitness_modules]
- PFam annotations offer the best coverage but are domain-level and may overcount functional associations. [src: fitness_modules]
