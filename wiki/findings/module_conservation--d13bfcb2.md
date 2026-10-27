---
type: "Finding"
description: "The report found 38 module families with <50% core genes, which it describes as co-regulated accessory gene modules conserved across organisms that may represent horizontally transferred functional units or niche-specific operons (a hypothesis, not established)."
finding_id: "module_conservation--d13bfcb2"
result: "inference"
source: "module_conservation"
quantities: [{"value": "38", "what": "module families with <50% core genes", "unit": "families", "denominator": "", "scope": ""}]
caveat: "The conservation analysis covered only a 29/32 organism subset, because Cola, Kang and SB2B lack pangenome links as their species had too few genomes in GTDB for pangenome construction."
first_added: "2026-10-27"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Some module families are accessory-dominated, possibly mobile or niche-specific

The report found 38 module families with <50% core genes, which it describes as co-regulated accessory gene modules conserved across organisms that may represent horizontally transferred functional units or niche-specific operons (a hypothesis, not established). [src: module_conservation]

## Key figures

- **38 families**: module families with <50% core genes [src: module_conservation]

## Evidence

> 38 families have <50% core genes -- these are co-regulated accessory gene modules conserved across organisms. They may represent horizontally transferred functional units or niche-specific operons. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The conservation analysis covered only a 29/32 organism subset, because Cola, Kang and SB2B lack pangenome links as their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

> - **29/32 organism subset**: 3 module organisms (Cola, Kang, SB2B) lack pangenome links because their species had too few genomes in GTDB for pangenome construction. [src: module_conservation]

## Other caveats in this report

- The report notes that families were nearly all core regardless of breadth and proposes the high core-genome baseline (~82%) as a reason a gradient may be hard to detect. [src: module_conservation]
- A baseline core rate of ~81.5% limits observable enrichment; the statistically significant +4.5pp difference to 86% is modest in absolute terms. [src: module_conservation]
- Upstream ICA membership required |Pearson r| >= 0.3 and allowed at most 50 genes per module; these choices could affect measured conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs used to classify core, mixed, and accessory modules were convenient rather than biologically motivated. [src: module_conservation]
- Because ICA requires fitness data, the modules capture only the non-essential portion of the genome. [src: module_conservation]
