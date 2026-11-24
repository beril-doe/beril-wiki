---
type: "Finding"
description: "38 module families have <50% core genes, described as co-regulated accessory gene modules conserved across organisms."
finding_id: "module_conservation--4e62a9d2"
result: "observation"
source: "module_conservation"
quantities: [{"value": "38", "what": "module families with <50% core genes", "unit": "families", "denominator": "", "scope": ""}]
caveat: "Three module organisms (Cola, Kang, SB2B) lack pangenome links because their species had too few genomes in GTDB for pangenome construction."
first_added: "2026-11-24"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# A minority of module families are accessory yet cross-organism

38 module families have <50% core genes, described as co-regulated accessory gene modules conserved across organisms. [src: module_conservation]

## Key figures

- **38 families**: module families with <50% core genes [src: module_conservation]

## Evidence

> 38 families have <50% core genes -- these are co-regulated accessory gene modules conserved across organisms. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

Three module organisms (Cola, Kang, SB2B) lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

> - **29/32 organism subset**: 3 module organisms (Cola, Kang, SB2B) lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

## Other caveats in this report

- The report attributes the limited gradient in family breadth versus conservation to a high core genome baseline of ~82%. [src: module_conservation]
- ICA modules capture only non-essential genes with measurable fitness variation and transposon insertions; essential genes are invisible because they have no fitness data. [src: module_conservation]
- A baseline core rate of ~81.5% limits maximum observable enrichment, and the statistically significant +4.5pp difference to 86% represents a modest absolute effect. [src: module_conservation]
- The upstream ICA membership threshold affects which genes belong to a module and could influence conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs for core, mixed, and accessory module classification are arbitrary conveniences rather than biologically motivated thresholds. [src: module_conservation]
