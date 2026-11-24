---
type: "Finding"
description: "The report suggests that conservation is a property of individual genes, not of the cross-organism scope of their regulatory module, given the null result for family breadth vs conservation (rho=-0.01)."
finding_id: "module_conservation--3c784bf6"
result: "inference"
source: "module_conservation"
quantities: [{"value": "rho=-0.01", "what": "Spearman correlation of family breadth with core fraction", "unit": "", "denominator": "", "scope": "module families"}]
caveat: "The core genome baseline is so high (~82%) that there is little room for a gradient."
first_added: "2026-11-24"
source_hash: "44e13c4ca1eae246521c79a559693fa556289043e35e7eeb7eaf3c806ed152de"
---
# Conservation appears to be a gene property, not module scope

The report suggests that conservation is a property of individual genes, not of the cross-organism scope of their regulatory module, given the null result for family breadth vs conservation (rho=-0.01). [src: module_conservation]

## Key figures

- **rho=-0.01**: Spearman correlation of family breadth with core fraction (scope module families) [src: module_conservation]

## Evidence

> The surprising null result for family breadth vs conservation (rho=-0.01) suggests that conservation is a property of individual genes, not of the cross-organism scope of their regulatory module. [src: module_conservation]

From the report [[summaries/module_conservation__REPORT]].

## Caveat

The core genome baseline is so high (~82%) that there is little room for a gradient. [src: module_conservation]

> The core genome baseline is so high (~82%) that there's little room for a gradient. [src: module_conservation]

## Other caveats in this report

- ICA modules capture only non-essential genes with measurable fitness variation and transposon insertions; essential genes are invisible because they have no fitness data. [src: module_conservation]
- A baseline core rate of ~81.5% limits maximum observable enrichment, and the statistically significant +4.5pp difference to 86% represents a modest absolute effect. [src: module_conservation]
- The analysis covers a 29/32 organism subset because 3 module organisms, Cola, Kang, and SB2B, lack pangenome links owing to too few genomes for their species in GTDB for pangenome construction. [src: module_conservation]
- The upstream ICA membership threshold affects which genes belong to a module and could influence conservation composition. [src: module_conservation]
- The 90% and 50% cutoffs for core, mixed, and accessory module classification are arbitrary conveniences rather than biologically motivated thresholds. [src: module_conservation]
