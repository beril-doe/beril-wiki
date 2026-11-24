---
type: "Finding"
description: "ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), which the report reads as co-regulated functional units preferentially residing in the conserved genome."
finding_id: "module_conservation--ba3f89b5"
result: "observation"
source: "module_conservation"
quantities: [{"value": "86%", "what": "core fraction of module genes", "unit": "percent", "denominator": "module genes", "scope": ""}, {"value": "81.5%", "what": "baseline core fraction of all genes", "unit": "percent", "denominator": "all genes", "scope": ""}, {"value": "OR=1.46", "what": "odds ratio of core enrichment", "unit": "", "denominator": "", "scope": ""}]
caveat: "The baseline core rate is already ~81.5%, limiting the maximum observable enrichment, so the +4.5pp difference to 86% is significant but a modest absolute effect."
first_added: "2026-11-24"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Fitness modules are enriched in core genes

ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), which the report reads as co-regulated functional units preferentially residing in the conserved genome. [src: module_conservation]

## Key figures

- **86%**: core fraction of module genes (denominator module genes) [src: module_conservation]
- **81.5%**: baseline core fraction of all genes (denominator all genes) [src: module_conservation]
- **OR=1.46**: odds ratio of core enrichment [src: module_conservation]

## Evidence

> ICA fitness modules are enriched in core genes (86% vs 81.5% baseline, OR=1.46, p=1.6e-87), confirming that co-regulated functional units preferentially reside in the conserved genome. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The baseline core rate is already ~81.5%, limiting the maximum observable enrichment, so the +4.5pp difference to 86% is significant but a modest absolute effect. [src: module_conservation]

> - **Ceiling effect**: The baseline core rate is already ~81.5%, limiting the maximum observable enrichment. The +4.5pp difference to 86% is statistically significant but represents a modest absolute effect. [src: module_conservation]

## Other caveats in this report

- The report attributes the limited gradient in family breadth versus conservation to a high core genome baseline of ~82%. [src: module_conservation]
- ICA modules capture only non-essential genes with measurable fitness variation and transposon insertions; essential genes are invisible because they have no fitness data. [src: module_conservation]
- The analysis covers a 29/32 organism subset because 3 module organisms, Cola, Kang, and SB2B, lack pangenome links owing to too few genomes for their species in GTDB for pangenome construction. [src: module_conservation]
- The upstream ICA membership threshold affects which genes belong to a module and could influence conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs for core, mixed, and accessory module classification are arbitrary conveniences rather than biologically motivated thresholds. [src: module_conservation]
