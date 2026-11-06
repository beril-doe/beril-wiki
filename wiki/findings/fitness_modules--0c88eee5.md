---
type: "Finding"
description: "In the held-out benchmark, Module-ICA had <1% strict KO precision and 23.3% coverage, with no F1 value reported."
finding_id: "fitness_modules--0c88eee5"
result: "null result"
source: "fitness_modules"
quantities: [{"value": "<1%", "what": "strict KO precision of Module-ICA", "unit": "", "denominator": "", "scope": "Module-ICA row of the benchmark table"}, {"value": "23.3%", "what": "coverage of Module-ICA", "unit": "", "denominator": "", "scope": "Module-ICA row of the benchmark table"}]
caveat: "Module-ICA and cofitness show near-zero strict KO precision because KEGG KO groups are gene-level assignments (~1.2 genes per unique KO), so a module with 20 annotated members typically has 20 different KOs."
first_added: "2026-10-27"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Module-ICA fails to recover exact KO assignments

In the held-out benchmark, Module-ICA had <1% strict KO precision and 23.3% coverage, with no F1 value reported. [src: fitness_modules]

## Key figures

- **<1%**: strict KO precision of Module-ICA (scope Module-ICA row of the benchmark table) [src: fitness_modules]
- **23.3%**: coverage of Module-ICA (scope Module-ICA row of the benchmark table) [src: fitness_modules]

## Evidence

> | Module-ICA | <1% | 23.3% | -- | [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

Module-ICA and cofitness show near-zero strict KO precision because KEGG KO groups are gene-level assignments (~1.2 genes per unique KO), so a module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]

> Module-ICA and cofitness show near-zero strict KO precision because KEGG KO groups are gene-level assignments (~1.2 genes per unique KO). A module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]

## Other caveats in this report

- The report contrasts PFam's broad annotation coverage with KEGG KO assignments, which it considers too gene-specific for module-level enrichment. [src: fitness_modules]
- Module-ICA is presented as a process-level complement to sequence-based methods, not as a predictor of specific molecular functions. [src: fitness_modules]
- Module-derived predictions should be interpreted as biological-process context rather than exact KO assignments. [src: fitness_modules]
- The report interprets ortholog transfer's 95.8% precision as stronger for gene-level prediction, while assigning Module-ICA a process-context role. [src: fitness_modules]
- The 6,691 predictions are explicitly qualified as process-participation predictions, not specific KO-function assignments. [src: fitness_modules]
