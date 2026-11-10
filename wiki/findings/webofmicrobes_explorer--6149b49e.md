---
type: "Finding"
description: "Matching WoM metabolites to GapMind pathways was blocked by a naming mismatch because GapMind pathway names (internal IDs) do not contain simple metabolite names, so a lookup table of substrate/product metabolites is needed."
finding_id: "webofmicrobes_explorer--6149b49e"
result: "null result"
source: "webofmicrobes_explorer"
quantities: []
caveat: "The report judges its cross-collection integration hypothesis (H1) only partially supported, so the blocked GapMind link leaves that integration incomplete."
first_added: "2026-11-09"
source_hash: "9a00ed7cecab68d7f9f290eb54f509ee70ab0950d80bcd48cd92b528748dd4da"
---
# Direct metabolite-name matching to GapMind pathways failed

Matching WoM metabolites to GapMind pathways was blocked by a naming mismatch because GapMind pathway names (internal IDs) do not contain simple metabolite names, so a lookup table of substrate/product metabolites is needed. [src: webofmicrobes_explorer]

## Evidence

> **WoM ↔ GapMind**: Blocked by naming convention mismatch. GapMind pathway names (internal IDs) don't contain simple metabolite names. A proper lookup table mapping GapMind pathways to substrate/product metabolites is needed. [src: webofmicrobes_explorer]

From the report [[summaries/webofmicrobes_explorer__REPORT]].

## Caveat

The report judges its cross-collection integration hypothesis (H1) only partially supported, so the blocked GapMind link leaves that integration incomplete. [src: webofmicrobes_explorer]

> **H1 is partially supported.** Cross-collection links are real and actionable: [src: webofmicrobes_explorer]

## Other caveats in this report

- The two direct Pseudomonas matches are ENIGMA groundwater isolates. Despite its strain match, E. coli BW25113 has only 12 WoM observations in ZMMG medium. [src: webofmicrobes_explorer]
- Exact names provide definitive ModelSEED links for 69 of 257 identified compounds. Formula-only links for 107 compounds are ambiguous, averaging 8.4 ModelSEED molecules per formula, and require manual curation. [src: webofmicrobes_explorer]
- The report describes an E-versus-I metabolic novelty rate for R2A isolates, but its displayed percentages do not equal E/(E+I) for the listed counts. [src: webofmicrobes_explorer]
- The report proposes relating its 32.4%-to-15.2% metabolic novelty-rate range to pangenome gene content; the rate denominator needs clarification. [src: webofmicrobes_explorer]
- Of 589 tracked metabolites, 332 (56.4%) are unidentified. The statement that 408 of 257 identified metabolites changed is internally impossible, although 408 is also given as 69.3% of all 589. Named active compounds include amino acids and nucleotides. [src: webofmicrobes_explorer]
