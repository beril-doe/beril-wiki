---
type: "Finding"
description: "Among 974 modules with >=3 mapped genes, 577 (59%) were classified as core (>90% core genes), 349 (36%) as mixed (50-90% core), and 48 (5%) as accessory (<50% core)."
finding_id: "module_conservation--b36fddee"
result: "observation"
source: "module_conservation"
quantities: [{"value": "577 (59%)", "what": "modules classified as core (>90% core genes)", "unit": "modules", "denominator": "974 modules with >=3 mapped genes", "scope": ""}, {"value": "349 (36%)", "what": "modules classified as mixed (50-90% core)", "unit": "modules", "denominator": "974 modules with >=3 mapped genes", "scope": ""}, {"value": "48 (5%)", "what": "modules classified as accessory (<50% core)", "unit": "modules", "denominator": "974 modules with >=3 mapped genes", "scope": ""}]
caveat: "The 90% and 50% cutoffs used to classify core, mixed and accessory modules are convenient but not biologically motivated."
first_added: "2026-10-27"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Most fitness modules are composed almost entirely of core genes

Among 974 modules with >=3 mapped genes, 577 (59%) were classified as core (>90% core genes), 349 (36%) as mixed (50-90% core), and 48 (5%) as accessory (<50% core). [src: module_conservation]

## Key figures

- **577 (59%) modules**: modules classified as core (>90% core genes) (denominator 974 modules with >=3 mapped genes) [src: module_conservation]
- **349 (36%) modules**: modules classified as mixed (50-90% core) (denominator 974 modules with >=3 mapped genes) [src: module_conservation]
- **48 (5%) modules**: modules classified as accessory (<50% core) (denominator 974 modules with >=3 mapped genes) [src: module_conservation]

## Evidence

> Of 974 modules with >=3 mapped genes: - **577 (59%) are core modules** (>90% core genes) - 349 (36%) are mixed modules (50-90% core) - **48 (5%) are accessory modules** (<50% core) [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The 90% and 50% cutoffs used to classify core, mixed and accessory modules are convenient but not biologically motivated. [src: module_conservation]

> - **Classification thresholds are arbitrary**: The 90% and 50% cutoffs for core/mixed/accessory module classification are convenient but not biologically motivated. [src: module_conservation]

## Other caveats in this report

- The report notes that families were nearly all core regardless of breadth and proposes the high core-genome baseline (~82%) as a reason a gradient may be hard to detect. [src: module_conservation]
- A baseline core rate of ~81.5% limits observable enrichment; the statistically significant +4.5pp difference to 86% is modest in absolute terms. [src: module_conservation]
- The conservation analysis covered a 29/32-organism subset: Cola, Kang, and SB2B lacked pangenome links because their species had too few genomes in GTDB for pangenome construction. GTDB is a named dataset. [src: module_conservation]
- Upstream ICA membership required |Pearson r| >= 0.3 and allowed at most 50 genes per module; these choices could affect measured conservation composition. [src: module_conservation]
- Because ICA requires fitness data, the modules capture only the non-essential portion of the genome. [src: module_conservation]
