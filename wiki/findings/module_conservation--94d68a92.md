---
type: "Finding"
description: "Of 974 modules with >=3 mapped genes, 577 (59%) are core modules with >90% core genes."
finding_id: "module_conservation--94d68a92"
result: "observation"
source: "module_conservation"
quantities: [{"value": "577 (59%)", "what": "modules that are core (>90% core genes)", "unit": "modules", "denominator": "974 modules with >=3 mapped genes", "scope": ""}]
caveat: "The 90% and 50% cutoffs for core/mixed/accessory module classification are convenient but not biologically motivated."
first_added: "2026-11-24"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Most fitness modules are almost entirely core

Of 974 modules with >=3 mapped genes, 577 (59%) are core modules with >90% core genes. [src: module_conservation]

## Key figures

- **577 (59%) modules**: modules that are core (>90% core genes) (denominator 974 modules with >=3 mapped genes) [src: module_conservation]

## Evidence

> Of 974 modules with >=3 mapped genes: - **577 (59%) are core modules** (>90% core genes) [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The 90% and 50% cutoffs for core/mixed/accessory module classification are convenient but not biologically motivated. [src: module_conservation]

> - **Classification thresholds are arbitrary**: The 90% and 50% cutoffs for core/mixed/accessory module classification are convenient but not biologically motivated. [src: module_conservation]

## Other caveats in this report

- The report attributes the limited gradient in family breadth versus conservation to a high core genome baseline of ~82%. [src: module_conservation]
- ICA modules capture only non-essential genes with measurable fitness variation and transposon insertions; essential genes are invisible because they have no fitness data. [src: module_conservation]
- A baseline core rate of ~81.5% limits maximum observable enrichment, and the statistically significant +4.5pp difference to 86% represents a modest absolute effect. [src: module_conservation]
- The analysis covers a 29/32 organism subset because 3 module organisms, Cola, Kang, and SB2B, lack pangenome links owing to too few genomes for their species in GTDB for pangenome construction. [src: module_conservation]
- The upstream ICA membership threshold affects which genes belong to a module and could influence conservation composition. [src: module_conservation]
