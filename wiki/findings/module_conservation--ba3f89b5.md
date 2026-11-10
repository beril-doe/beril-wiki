---
type: "Finding"
description: "ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), which the report takes as confirming that co-regulated functional units preferentially reside in the conserved genome."
finding_id: "module_conservation--ba3f89b5"
result: "observation"
source: "module_conservation"
quantities: [{"value": "86%", "what": "core fraction of module genes", "unit": "", "denominator": "", "scope": "ICA fitness modules"}, {"value": "81.5%", "what": "baseline core fraction of all genes", "unit": "", "denominator": "", "scope": ""}, {"value": "1.46", "what": "odds ratio for core-gene enrichment", "unit": "", "denominator": "", "scope": ""}, {"value": "1.6e-87", "what": "p-value for enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "The baseline core rate is already ~81.5%, limiting the maximum observable enrichment, so the statistically significant +4.5pp difference to 86% is a modest absolute effect."
first_added: "2026-10-27"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Module genes are modestly but significantly enriched in the core genome

ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), which the report takes as confirming that co-regulated functional units preferentially reside in the conserved genome. [src: module_conservation]

## Key figures

- **86%**: core fraction of module genes (scope ICA fitness modules) [src: module_conservation]
- **81.5%**: baseline core fraction of all genes [src: module_conservation]
- **1.46**: odds ratio for core-gene enrichment [src: module_conservation]
- **1.6e-87**: p-value for enrichment [src: module_conservation]

## Evidence

> ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), confirming that co-regulated functional units preferentially reside in the conserved genome. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The baseline core rate is already ~81.5%, limiting the maximum observable enrichment, so the statistically significant +4.5pp difference to 86% is a modest absolute effect. [src: module_conservation]

> - **Ceiling effect**: The baseline core rate is already ~81.5%, limiting the maximum observable enrichment. The +4.5pp difference to 86% is statistically significant but represents a modest absolute effect. [src: module_conservation]

## Other caveats in this report

- The report notes that families were nearly all core regardless of breadth and proposes the high core-genome baseline (~82%) as a reason a gradient may be hard to detect. [src: module_conservation]
- The conservation analysis covered a 29/32-organism subset: Cola, Kang, and SB2B lacked pangenome links because their species had too few genomes in GTDB for pangenome construction. GTDB is a named dataset. [src: module_conservation]
- Upstream ICA membership required |Pearson r| >= 0.3 and allowed at most 50 genes per module; these choices could affect measured conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs used to classify core, mixed, and accessory modules were convenient rather than biologically motivated. [src: module_conservation]
- Because ICA requires fitness data, the modules capture only the non-essential portion of the genome. [src: module_conservation]
