---
type: "Finding"
description: "The report concludes the dominant source of thermodynamic uncertainty is the deltaG estimation method, since eQuilibrator vs dGPredictor disagreements (median 17 kJ/mol, 19.3% sign discordance) dwarf the Marvin vs OPAM2 differences (median 0.11 kJ/mol, 2.7% sign discordance)."
finding_id: "thermodynamic_impact--4d50645c"
result: "inference"
source: "thermodynamic_impact"
quantities: [{"value": "17 kJ/mol", "what": "median eQuilibrator vs dGPredictor disagreement", "unit": "kJ/mol", "denominator": "", "scope": ""}, {"value": "19.3%", "what": "sign discordance, eQuilibrator vs dGPredictor", "unit": "", "denominator": "", "scope": ""}, {"value": "0.11 kJ/mol", "what": "median Marvin vs OPAM2 difference", "unit": "kJ/mol", "denominator": "", "scope": ""}, {"value": "2.7%", "what": "sign discordance, Marvin vs OPAM2", "unit": "", "denominator": "", "scope": ""}]
caveat: "No experimental validation of pKa accuracy: this study measures downstream impact, not pKa prediction accuracy per se."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# deltaG estimation method outweighs pKa source as uncertainty

The report concludes the dominant source of thermodynamic uncertainty is the deltaG estimation method, since eQuilibrator vs dGPredictor disagreements (median 17 kJ/mol, 19.3% sign discordance) dwarf the Marvin vs OPAM2 differences (median 0.11 kJ/mol, 2.7% sign discordance). [src: thermodynamic_impact]

## Key figures

- **17 kJ/mol kJ/mol**: median eQuilibrator vs dGPredictor disagreement [src: thermodynamic_impact]
- **19.3%**: sign discordance, eQuilibrator vs dGPredictor [src: thermodynamic_impact]
- **0.11 kJ/mol kJ/mol**: median Marvin vs OPAM2 difference [src: thermodynamic_impact]
- **2.7%**: sign discordance, Marvin vs OPAM2 [src: thermodynamic_impact]

## Evidence

> 6. **The dominant source of thermodynamic uncertainty is the deltaG estimation method, not the pKa source.** eQuilibrator vs dGPredictor disagreements (median 17 kJ/mol, 19.3% sign discordance) dwarf the Marvin vs OPAM2 differences (median 0.11 kJ/mol, 2.7% sign discordance). [src: thermodynamic_impact]

From the report [[summaries/thermodynamic_impact__REPORT]].

## Caveat

No experimental validation of pKa accuracy: this study measures downstream impact, not pKa prediction accuracy per se. [src: thermodynamic_impact]

> **No experimental validation of pKa accuracy**: This study measures downstream impact, not pKa prediction accuracy per se. [src: thermodynamic_impact]

## Other caveats in this report

- The initial hard-cutoff analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction, constraining 928 Escherichia coli reactions (58.8%) and eliminating growth in both organisms. [src: thermodynamic_impact]
- The report says the initial minimal-impact conclusion reflected identical zero growth from a broken constraint method rather than problems with the dG values. [src: thermodynamic_impact]
- Hard cutoffs ignore metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]
- The report states that LP relaxation provides an outer bound on MILP-feasible flux ranges and interprets dG differences as changing alternate optimal solution selection rather than which reactions can carry flux. [src: thermodynamic_impact]
- All models were gapfilled on complete media, potentially masking thermodynamic infeasibilities under minimal media conditions. [src: thermodynamic_impact]
