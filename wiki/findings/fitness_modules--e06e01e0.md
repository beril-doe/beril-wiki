---
type: "Finding"
description: "The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal (59% enriched, 1-17x correlation); after switching to absolute weight thresholds, modules became biologically coherent (94% enriched, 2.8x correlation enrichment)."
finding_id: "fitness_modules--e06e01e0"
result: "correction"
source: "fitness_modules"
quantities: [{"value": "100-280", "what": "genes per module under the initial D'Agostino K-squared approach", "unit": "genes per module", "denominator": "", "scope": "initial approach"}, {"value": "59%", "what": "modules enriched under the initial approach", "unit": "", "denominator": "", "scope": "D'Agostino K-squared approach"}, {"value": "94%", "what": "modules enriched after switching to absolute weight thresholds", "unit": "", "denominator": "", "scope": "absolute weight thresholds"}, {"value": "2.8x", "what": "correlation enrichment after switching to absolute weight thresholds", "unit": "", "denominator": "", "scope": "absolute weight thresholds"}]
caveat: "The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms."
first_added: "2026-10-27"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Absolute weight thresholds replaced weak D'Agostino-selected modules with coherent ones

The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal (59% enriched, 1-17x correlation); after switching to absolute weight thresholds, modules became biologically coherent (94% enriched, 2.8x correlation enrichment). [src: fitness_modules]

## Key figures

- **100-280 genes per module**: genes per module under the initial D'Agostino K-squared approach (scope initial approach) [src: fitness_modules]
- **59%**: modules enriched under the initial approach (scope D'Agostino K-squared approach) [src: fitness_modules]
- **94%**: modules enriched after switching to absolute weight thresholds (scope absolute weight thresholds) [src: fitness_modules]
- **2.8x**: correlation enrichment after switching to absolute weight thresholds (scope absolute weight thresholds) [src: fitness_modules]

## Evidence

> The initial D'Agostino K-squared approach gave 100-280 genes per module with weak cofitness signal (59% enriched, 1-17x correlation). After switching to absolute weight thresholds, modules became biologically coherent (94% enriched, 2.8x correlation enrichment). [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms. [src: fitness_modules]

> The 40% component cap (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss some modules in low-experiment organisms [src: fitness_modules]

## Other caveats in this report

- The report contrasts PFam's broad annotation coverage with KEGG KO assignments, which it considers too gene-specific for module-level enrichment. [src: fitness_modules]
- Module-ICA is presented as a process-level complement to sequence-based methods, not as a predictor of specific molecular functions. [src: fitness_modules]
- The report attributes near-zero strict KO precision to gene-level KO labels, giving ~1.2 genes per unique KO and noting that a module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]
- Module-derived predictions should be interpreted as biological-process context rather than exact KO assignments. [src: fitness_modules]
- The report interprets ortholog transfer's 95.8% precision as stronger for gene-level prediction, while assigning Module-ICA a process-context role. [src: fitness_modules]
