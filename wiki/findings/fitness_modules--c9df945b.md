---
type: "Finding"
description: "There were 156 module families spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21)."
finding_id: "fitness_modules--c9df945b"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "156", "what": "module families spanning 2+ organisms", "unit": "families", "denominator": "", "scope": ""}, {"value": "28", "what": "families spanning 5+ organisms", "unit": "families", "denominator": "", "scope": ""}, {"value": "7", "what": "families spanning 10+ organisms", "unit": "families", "denominator": "", "scope": ""}, {"value": "21", "what": "organisms spanned by the largest family", "unit": "organisms", "denominator": "", "scope": "1 family"}]
caveat: "Module-ICA is complementary to sequence-based methods: it identifies co-regulated gene groups (biological process modules) but should not be used for predicting specific molecular functions, where ortholog transfer is far superior."
first_added: "2026-10-27"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Module families recur across organisms, reaching a pan-bacterial span

There were 156 module families spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21). [src: fitness_modules]

## Key figures

- **156 families**: module families spanning 2+ organisms [src: fitness_modules]
- **28 families**: families spanning 5+ organisms [src: fitness_modules]
- **7 families**: families spanning 10+ organisms [src: fitness_modules]
- **21 organisms**: organisms spanned by the largest family (scope 1 family) [src: fitness_modules]

## Evidence

> **156 module families** spanning 2+ organisms (28 spanning 5+, 7 spanning 10+, 1 spanning 21) [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

Module-ICA is complementary to sequence-based methods: it identifies co-regulated gene groups (biological process modules) but should not be used for predicting specific molecular functions, where ortholog transfer is far superior. [src: fitness_modules]

> Module-ICA is **complementary** to sequence-based methods: it excels at identifying co-regulated gene groups (biological process modules) but should not be used for predicting specific molecular functions, where ortholog transfer is far superior. [src: fitness_modules]

## Other caveats in this report

- The report contrasts PFam's broad annotation coverage with KEGG KO assignments, which it considers too gene-specific for module-level enrichment. [src: fitness_modules]
- The report attributes near-zero strict KO precision to gene-level KO labels, giving ~1.2 genes per unique KO and noting that a module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]
- Module-derived predictions should be interpreted as biological-process context rather than exact KO assignments. [src: fitness_modules]
- The report interprets ortholog transfer's 95.8% precision as stronger for gene-level prediction, while assigning Module-ICA a process-context role. [src: fitness_modules]
- The 6,691 predictions are explicitly qualified as process-participation predictions, not specific KO-function assignments. [src: fitness_modules]
