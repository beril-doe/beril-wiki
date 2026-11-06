---
type: "Finding"
description: "Module families spanning more organisms did not have higher core fractions (Spearman rho=-0.01, p=0.914)."
finding_id: "module_conservation--ef29c9c3"
result: "null result"
source: "module_conservation"
quantities: [{"value": "-0.01", "what": "Spearman rho between family organism breadth and core fraction", "unit": "", "denominator": "", "scope": "module families"}, {"value": "0.914", "what": "p-value of the correlation", "unit": "", "denominator": "", "scope": ""}]
caveat: "Families are nearly all core regardless of breadth, and the core genome baseline of ~82% is so high that there is little room for a gradient."
first_added: "2026-10-27"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Module family breadth does not predict core fraction

Module families spanning more organisms did not have higher core fractions (Spearman rho=-0.01, p=0.914). [src: module_conservation]

## Key figures

- **-0.01**: Spearman rho between family organism breadth and core fraction (scope module families) [src: module_conservation]
- **0.914**: p-value of the correlation [src: module_conservation]

## Evidence

> Surprisingly, module families spanning more organisms do NOT have higher core fractions (Spearman rho=-0.01, p=0.914). [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

Families are nearly all core regardless of breadth, and the core genome baseline of ~82% is so high that there is little room for a gradient. [src: module_conservation]

> Families are nearly all core regardless of how many organisms they span. The core genome baseline is so high (~82%) that there's little room for a gradient. [src: module_conservation]

## Other caveats in this report

- A baseline core rate of ~81.5% limits observable enrichment; the statistically significant +4.5pp difference to 86% is modest in absolute terms. [src: module_conservation]
- The conservation analysis covered a 29/32-organism subset: Cola, Kang, and SB2B lacked pangenome links because their species had too few genomes in GTDB for pangenome construction. GTDB is a named dataset. [src: module_conservation]
- Upstream ICA membership required |Pearson r| >= 0.3 and allowed at most 50 genes per module; these choices could affect measured conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs used to classify core, mixed, and accessory modules were convenient rather than biologically motivated. [src: module_conservation]
- Because ICA requires fitness data, the modules capture only the non-essential portion of the genome. [src: module_conservation]
