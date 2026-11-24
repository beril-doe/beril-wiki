---
type: "Finding"
description: "Across the fitness ICA modules, 94.2% showed significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05)."
finding_id: "fitness_modules--e33de0ee"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "94.2%", "what": "modules with significantly elevated within-module cofitness", "unit": "%", "denominator": "", "scope": ""}]
caveat: "The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms."
first_added: "2026-11-24"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Nearly all fitness modules show elevated within-module cofitness

Across the fitness ICA modules, 94.2% showed significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05). [src: fitness_modules]

## Key figures

- **94.2%**: modules with significantly elevated within-module cofitness [src: fitness_modules]

## Evidence

> **94.2%** of modules show significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05) [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms. [src: fitness_modules]

> The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms [src: fitness_modules]

## Other caveats in this report

- KEGG KOs were too gene-specific for fitness-module-level enrichment. [src: fitness_modules]
- Module-ICA should not be used to predict specific molecular functions, for which ortholog transfer is far superior. [src: fitness_modules]
- Fitness-module function predictions should be interpreted as biological process context rather than exact KO assignments. [src: fitness_modules]
- Organisms with fewer than ~100 experiments produce weaker fitness modules; the report gives Caulo with 198 experiments and only 2.9x correlation enrichment as an example. [src: fitness_modules]
- PFam annotations offer the best coverage but are domain-level and may overcount functional associations. [src: fitness_modules]
