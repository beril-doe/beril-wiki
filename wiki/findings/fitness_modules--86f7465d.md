---
type: "Finding"
description: "Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions."
finding_id: "fitness_modules--86f7465d"
result: "observation"
source: "fitness_modules"
quantities: [{"value": "8% to 80%", "what": "module annotation rate", "unit": "", "denominator": "", "scope": ""}, {"value": "92 to 890", "what": "annotated modules", "unit": "modules", "denominator": "", "scope": ""}, {"value": "7.6x", "what": "more function predictions", "unit": "", "denominator": "", "scope": ""}]
caveat: "PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations."
first_added: "2026-11-24"
source_hash: "4fce3013b064e0af4e90202509f2c93e0d181d2663930f839a35e0ae16b2f86e"
---
# PFam domains and a lower overlap threshold greatly raised module annotation

Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules]

## Key figures

- **8% to 80%**: module annotation rate [src: fitness_modules]
- **92 to 890 modules**: annotated modules [src: fitness_modules]
- **7.6x**: more function predictions [src: fitness_modules]

## Evidence

> Adding PFam domains and lowering the enrichment overlap threshold from 3 to 2 increased module annotation rate from 8% to 80% (92 to 890 modules), unlocking 7.6x more function predictions. [src: fitness_modules]

From the report [[summaries/fitness_modules__REPORT]].

## Caveat

PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations. [src: fitness_modules]

> PFam-based annotations, while providing the best coverage, are at the domain level and may overcount functional associations [src: fitness_modules]

## Other caveats in this report

- KEGG KOs were too gene-specific for fitness-module-level enrichment. [src: fitness_modules]
- Module-ICA should not be used to predict specific molecular functions, for which ortholog transfer is far superior. [src: fitness_modules]
- Fitness-module function predictions should be interpreted as biological process context rather than exact KO assignments. [src: fitness_modules]
- Organisms with fewer than ~100 experiments produce weaker fitness modules; the report gives Caulo with 198 experiments and only 2.9x correlation enrichment as an example. [src: fitness_modules]
- The component cap of 40% (components <= 40% of experiments) is necessary to avoid FastICA convergence failures but may miss modules in low-experiment organisms. [src: fitness_modules]
