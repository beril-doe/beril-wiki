---
type: "Finding"
description: "The 2018 Web of Microbes snapshot has no \"Decreased\" (consumption) action for any organism, and all 742 'D' observations belong exclusively to the control; consumption data may exist in the newer GNPS2 version."
finding_id: "webofmicrobes_explorer--ab7e4ba4"
result: "null result"
source: "webofmicrobes_explorer"
quantities: [{"value": "742", "what": "'D' observations, all belonging to the control", "unit": "observations", "denominator": "", "scope": "2018 WoM snapshot"}]
caveat: "The absence of consumption data prevents testing whether consumed metabolites predict gene essentiality, and the data are small (37 organisms, 5 projects) and from a single laboratory."
first_added: "2026-11-09"
source_hash: "9a00ed7cecab68d7f9f290eb54f509ee70ab0950d80bcd48cd92b528748dd4da"
---
# No organism consumption data in the archived Web of Microbes export

The 2018 Web of Microbes snapshot has no "Decreased" (consumption) action for any organism, and all 742 'D' observations belong exclusively to the control; consumption data may exist in the newer GNPS2 version. [src: webofmicrobes_explorer]

## Key figures

- **742 observations**: 'D' observations, all belonging to the control (scope 2018 WoM snapshot) [src: webofmicrobes_explorer]

## Evidence

> **There is no "Decreased" (consumption) action for any organism** in this 2018 snapshot. All 742 'D' observations belong exclusively to the control. The original Kosina et al. (2018) paper describes "decrease" as a valid action, so consumption data may exist in the newer GNPS2 version. [src: webofmicrobes_explorer]

From the report [[summaries/webofmicrobes_explorer__REPORT]].

## Caveat

The absence of consumption data prevents testing whether consumed metabolites predict gene essentiality, and the data are small (37 organisms, 5 projects) and from a single laboratory. [src: webofmicrobes_explorer]

> However, the **absence of consumption data** is a fundamental limitation. The 2018 WoM snapshot records only what organisms produce, not what they consume. This prevents testing the most interesting question — whether consumed metabolites predict gene essentiality. The data is also small (37 organisms, 5 projects) and from a single laboratory. [src: webofmicrobes_explorer]

## Other caveats in this report

- The two direct Pseudomonas matches are ENIGMA groundwater isolates. Despite its strain match, E. coli BW25113 has only 12 WoM observations in ZMMG medium. [src: webofmicrobes_explorer]
- Exact names provide definitive ModelSEED links for 69 of 257 identified compounds. Formula-only links for 107 compounds are ambiguous, averaging 8.4 ModelSEED molecules per formula, and require manual curation. [src: webofmicrobes_explorer]
- The report describes an E-versus-I metabolic novelty rate for R2A isolates, but its displayed percentages do not equal E/(E+I) for the listed counts. [src: webofmicrobes_explorer]
- The report proposes relating its 32.4%-to-15.2% metabolic novelty-rate range to pangenome gene content; the rate denominator needs clarification. [src: webofmicrobes_explorer]
- Of 589 tracked metabolites, 332 (56.4%) are unidentified. The statement that 408 of 257 identified metabolites changed is internally impossible, although 408 is also given as 69.3% of all 589. Named active compounds include amino acids and nucleotides. [src: webofmicrobes_explorer]
