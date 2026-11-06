---
type: "Finding"
description: "No essential genes (0) appeared in any module, which the report attributes to ICA capturing only genes with measurable fitness variation, since essential genes lack transposon-insertion fitness data."
finding_id: "module_conservation--1e6a89d4"
result: "null result"
source: "module_conservation"
quantities: [{"value": "0", "what": "essential genes appearing in any module", "unit": "genes", "denominator": "", "scope": "all ICA modules"}]
caveat: "Because ICA requires fitness data, essential genes (no transposon insertions) are absent from all modules, so modules capture only the non-essential portion of the genome."
first_added: "2026-10-27"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# No essential genes appear in any fitness module

No essential genes (0) appeared in any module, which the report attributes to ICA capturing only genes with measurable fitness variation, since essential genes lack transposon-insertion fitness data. [src: module_conservation]

## Key figures

- **0 genes**: essential genes appearing in any module (scope all ICA modules) [src: module_conservation]

## Evidence

> 0 essential genes appear in any module, confirming that ICA modules only capture genes with measurable fitness variation (non-essential genes with transposon insertions). Essential genes are invisible to ICA because they have no fitness data. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

Because ICA requires fitness data, essential genes (no transposon insertions) are absent from all modules, so modules capture only the non-essential portion of the genome. [src: module_conservation]

> - **Essential genes excluded**: ICA requires fitness data, so essential genes (no transposon insertions) are absent from all modules. This means modules only capture the non-essential portion of the genome. [src: module_conservation]

## Other caveats in this report

- The report notes that families were nearly all core regardless of breadth and proposes the high core-genome baseline (~82%) as a reason a gradient may be hard to detect. [src: module_conservation]
- A baseline core rate of ~81.5% limits observable enrichment; the statistically significant +4.5pp difference to 86% is modest in absolute terms. [src: module_conservation]
- The conservation analysis covered a 29/32-organism subset: Cola, Kang, and SB2B lacked pangenome links because their species had too few genomes in GTDB for pangenome construction. GTDB is a named dataset. [src: module_conservation]
- Upstream ICA membership required |Pearson r| >= 0.3 and allowed at most 50 genes per module; these choices could affect measured conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs used to classify core, mixed, and accessory modules were convenient rather than biologically motivated. [src: module_conservation]
