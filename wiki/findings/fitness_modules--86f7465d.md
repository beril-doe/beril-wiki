---
type: "Finding"
description: "Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions."
finding_id: "fitness_modules--86f7465d"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "8% to 80%", "what": "module annotation rate before and after", "unit": "", "denominator": "", "scope": ""}, {"value": "92 to 890", "what": "annotated modules before and after", "unit": "modules", "denominator": "", "scope": ""}, {"value": "7.6x", "what": "more function predictions unlocked", "unit": "", "denominator": "", "scope": ""}]
caveat: "PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations."
first_added: "2026-10-27"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# Adding PFam domains and relaxing overlap threshold sharply increased module annotation

Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules]

## Key figures

- **8% to 80%**: module annotation rate before and after [src: fitness_modules]
- **92 to 890 modules**: annotated modules before and after [src: fitness_modules]
- **7.6x**: more function predictions unlocked [src: fitness_modules]

## Evidence

> Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations. [src: fitness_modules]

> PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations [src: fitness_modules]

## Other caveats in this report

- The report contrasts PFam's broad annotation coverage with KEGG KO assignments, which it considers too gene-specific for module-level enrichment. [src: fitness_modules]
- Module-ICA is presented as a process-level complement to sequence-based methods, not as a predictor of specific molecular functions. [src: fitness_modules]
- The report attributes near-zero strict KO precision to gene-level KO labels, giving ~1.2 genes per unique KO and noting that a module with 20 annotated members typically has 20 different KOs. [src: fitness_modules]
- Module-derived predictions should be interpreted as biological-process context rather than exact KO assignments. [src: fitness_modules]
- The report interprets ortholog transfer's 95.8% precision as stronger for gene-level prediction, while assigning Module-ICA a process-context role. [src: fitness_modules]
