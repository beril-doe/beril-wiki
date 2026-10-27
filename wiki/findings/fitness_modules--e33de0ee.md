---
type: "Finding"
description: "94.2% of modules show significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05)."
finding_id: "fitness_modules--e33de0ee"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "94.2%", "what": "modules with significantly elevated within-module cofitness", "unit": "", "denominator": "", "scope": "Mann-Whitney U, p < 0.05"}]
caveat: "Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment)."
first_added: "2026-10-27"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Nearly all modules show elevated within-module cofitness

94.2% of modules show significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05). [src: fitness_modules]

## Key figures

- **94.2%**: modules with significantly elevated within-module cofitness (scope Mann-Whitney U, p < 0.05) [src: fitness_modules]

## Evidence

> **94.2%** of modules show significantly elevated within-module cofitness (Mann-Whitney U, p < 0.05) [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment). [src: fitness_modules]

> Organisms with fewer than ~100 experiments produce weaker modules (e.g., Caulo with 198 experiments showed only 2.9x correlation enrichment) [src: fitness_modules]

## Other caveats in this report

- The report contrasts PFam's broad annotation coverage with KEGG KO assignments, which it considers too gene-specific for module-level enrichment. [src: fitness_modules]
- Module-ICA is presented as a process-level complement to sequence-based methods, not as a predictor of specific molecular functions. [src: fitness_modules]
- The report attributes near-zero strict KO precision to gene-level KO labels, giving ~1.2 genes per unique KO and noting that a module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]
- Module-derived predictions should be interpreted as biological-process context rather than exact KO assignments. [src: fitness_modules]
- The report interprets ortholog transfer's 95.8% precision as stronger for gene-level prediction, while assigning Module-ICA a process-context role. [src: fitness_modules]
