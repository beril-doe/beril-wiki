---
type: "Finding"
description: "The 2018 WoM snapshot contains no organism consumption action, with all 742 D observations belonging to the control."
finding_id: "webofmicrobes_explorer--ccaa3dcd"
result: "null result"
source: "webofmicrobes_explorer"
quantities: [{"value": "742", "what": "D observations, all belonging to the control", "unit": "observations", "denominator": "", "scope": "2018 WoM snapshot"}]
caveat: "The 2018 WoM snapshot records only what organisms produce, not what they consume, which prevents testing whether consumed metabolites predict gene essentiality."
first_added: "2026-11-24"
source_hash: "9a00ed7cecab68d7f9f290eb54f509ee70ab0950d80bcd48cd92b528748dd4da"
---
# WoM snapshot contains no organism consumption data

The 2018 WoM snapshot contains no organism consumption action, with all 742 D observations belonging to the control. [src: webofmicrobes_explorer]

## Key figures

- **742 observations**: D observations, all belonging to the control (scope 2018 WoM snapshot) [src: webofmicrobes_explorer]

## Evidence

> **There is no "Decreased" (consumption) action for any organism** in this 2018 snapshot. All 742 'D' observations belong exclusively to the control. [src: webofmicrobes_explorer]

From the report [[summaries/webofmicrobes_explorer__REPORT]].

## Caveat

The 2018 WoM snapshot records only what organisms produce, not what they consume, which prevents testing whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer]

> The 2018 WoM snapshot records only what organisms produce, not what they consume. This prevents testing the most interesting question — whether consumed metabolites predict gene essentiality. [src: webofmicrobes_explorer]

## Other caveats in this report

- Consumption data may exist in the newer GNPS2 version because the original Kosina et al. (2018) paper describes decrease as a valid action. [src: webofmicrobes_explorer]
- WoM data for Escherichia coli BW25113 are limited to 12 observations in ZMMG medium focused only on sulfur metabolism. [src: webofmicrobes_explorer]
- WoM formula matches to ModelSEED supply candidate sets for manual curation rather than definitive identifications. [src: webofmicrobes_explorer]
- WoM–GapMind linkage is blocked because GapMind internal pathway names do not contain simple metabolite names, requiring a pathway-to-substrate/product lookup table. [src: webofmicrobes_explorer]
- WoM–pangenome species-level matching requires strain-to-genome mapping, which the project did not attempt. [src: webofmicrobes_explorer]
