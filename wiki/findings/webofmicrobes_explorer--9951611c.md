---
type: "Finding"
description: "Simple name matching failed to link WoM metabolites to GapMind pathways."
finding_id: "webofmicrobes_explorer--9951611c"
result: "null result"
source: "webofmicrobes_explorer"
quantities: []
caveat: "GapMind pathway names (internal IDs) do not contain simple metabolite names, so a lookup table mapping GapMind pathways to substrate/product metabolites is needed."
first_added: "2026-11-24"
source_hash: "9a00ed7cecab68d7f9f290eb54f509ee70ab0950d80bcd48cd92b528748dd4da"
---
# Simple name matching fails to link WoM metabolites to GapMind pathways

Simple name matching failed to link WoM metabolites to GapMind pathways. [src: webofmicrobes_explorer]

## Evidence

> **GapMind pathway matching requires a lookup table**: Simple name matching failed. [src: webofmicrobes_explorer]

From the report [[summaries/webofmicrobes_explorer__REPORT]].

## Caveat

GapMind pathway names (internal IDs) do not contain simple metabolite names, so a lookup table mapping GapMind pathways to substrate/product metabolites is needed. [src: webofmicrobes_explorer]

> **WoM ↔ GapMind**: Blocked by naming convention mismatch. GapMind pathway names (internal IDs) don't contain simple metabolite names. A proper lookup table mapping GapMind pathways to substrate/product metabolites is needed. [src: webofmicrobes_explorer]

## Other caveats in this report

- Consumption data may exist in the newer GNPS2 version because the original Kosina et al. (2018) paper describes decrease as a valid action. [src: webofmicrobes_explorer]
- WoM data for Escherichia coli BW25113 are limited to 12 observations in ZMMG medium focused only on sulfur metabolism. [src: webofmicrobes_explorer]
- WoM formula matches to ModelSEED supply candidate sets for manual curation rather than definitive identifications. [src: webofmicrobes_explorer]
- WoM–pangenome species-level matching requires strain-to-genome mapping, which the project did not attempt. [src: webofmicrobes_explorer]
- The 2018 WoM snapshot records production but not consumption, preventing tests of whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer]
