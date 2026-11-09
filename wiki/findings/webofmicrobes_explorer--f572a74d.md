---
type: "Finding"
description: "Among identified WoM compounds, 69 (26.8%) are exact-name matches to ModelSEED, 107 (41.6%) match by formula only (107 WoM to 900 MS molecules, 1:8.4 average expansion), 176 (68.5%) have any link, and 81 (31.5%) are unmatched."
finding_id: "webofmicrobes_explorer--f572a74d"
result: "observation"
source: "webofmicrobes_explorer"
quantities: [{"value": "69", "what": "exact name matches", "unit": "compounds", "denominator": "", "scope": "identified WoM compounds; 26.8%"}, {"value": "107", "what": "formula-only matches", "unit": "compounds", "denominator": "", "scope": "41.6%; 107 WoM mapped to 900 ModelSEED molecules"}, {"value": "176", "what": "compounds with any link", "unit": "compounds", "denominator": "", "scope": "68.5%"}, {"value": "81", "what": "unmatched compounds", "unit": "compounds", "denominator": "", "scope": "31.5%"}]
caveat: "Exact names give definitive ModelSEED links for only 69 of 257 identified compounds, while formula-only links for 107 compounds average 8.4 ModelSEED molecules each and need manual curation."
first_added: "2026-11-09"
source_hash: "9a00ed7cecab68d7f9f290eb54f509ee70ab0950d80bcd48cd92b528748dd4da"
---
# Most Web of Microbes compounds lack definitive ModelSEED links

Among identified WoM compounds, 69 (26.8%) are exact-name matches to ModelSEED, 107 (41.6%) match by formula only (107 WoM to 900 MS molecules, 1:8.4 average expansion), 176 (68.5%) have any link, and 81 (31.5%) are unmatched. [src: webofmicrobes_explorer]

## Key figures

- **69 compounds**: exact name matches (scope identified WoM compounds; 26.8%) [src: webofmicrobes_explorer]
- **107 compounds**: formula-only matches (scope 41.6%; 107 WoM mapped to 900 ModelSEED molecules) [src: webofmicrobes_explorer]
- **176 compounds**: compounds with any link (scope 68.5%) [src: webofmicrobes_explorer]
- **81 compounds**: unmatched compounds (scope 31.5%) [src: webofmicrobes_explorer]

## Evidence

> | Exact name match | 69 | **High** — 1:1 mapping | 26.8% | | Formula-only match | 107 | **Low** — 1:8.4 avg expansion (107 WoM → 900 MS molecules) | 41.6% | | **Total with any link** | **176** | Mixed | **68.5%** | | Unmatched | 81 | — | 31.5% | [src: webofmicrobes_explorer]

From the report [[summaries/webofmicrobes_explorer__REPORT]].

## Caveat

Exact names give definitive ModelSEED links for only 69 of 257 identified compounds, while formula-only links for 107 compounds average 8.4 ModelSEED molecules each and need manual curation. [src: webofmicrobes_explorer]

> Of 257 identified (non-unknown) WoM compounds, **69 (26.8%) have definitive ModelSEED links** by exact name match. An additional 107 match by molecular formula alone, but formula matches are inherently ambiguous — each WoM formula maps to an average of 8.4 ModelSEED molecules (e.g., C5H11NO2 matches valine, norvaline, betaine, 5-aminopentanoate, and others). Formula matches provide candidate sets for manual curation, not definitive identifications. [src: webofmicrobes_explorer]

## Other caveats in this report

- The two direct Pseudomonas matches are ENIGMA groundwater isolates. Despite its strain match, E. coli BW25113 has only 12 WoM observations in ZMMG medium. [src: webofmicrobes_explorer]
- The report describes an E-versus-I metabolic novelty rate for R2A isolates, but its displayed percentages do not equal E/(E+I) for the listed counts. [src: webofmicrobes_explorer]
- The report proposes relating its 32.4%-to-15.2% metabolic novelty-rate range to pangenome gene content; the rate denominator needs clarification. [src: webofmicrobes_explorer]
- Of 589 tracked metabolites, 332 (56.4%) are unidentified. The statement that 408 of 257 identified metabolites changed is internally impossible, although 408 is also given as 69.3% of all 589. Named active compounds include amino acids and nucleotides. [src: webofmicrobes_explorer]
- Pangenome linkage is genus-level only; strain-to-genome mapping needed for species-level linkage was not attempted. [src: webofmicrobes_explorer]
