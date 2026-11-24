---
type: "Finding"
description: "The report attributes the small Marvin\u2013OPAM2 deltaG difference (median 0.11 kJ/mol) to the Legendre transform's summation over multiple atoms per compound and multiple compounds per reaction, which attenuates large pKa differences."
finding_id: "thermodynamic_impact--5293b7f8"
result: "inference"
source: "thermodynamic_impact"
quantities: [{"value": "0.11 kJ/mol", "what": "median deltaG difference between Marvin and OPAM2", "unit": "kJ/mol", "denominator": "", "scope": ""}]
caveat: "No experimental validation of pKa accuracy: this study measures downstream impact, not pKa prediction accuracy per se."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# Legendre transform buffers large pKa differences before they reach deltaG

The report attributes the small Marvin–OPAM2 deltaG difference (median 0.11 kJ/mol) to the Legendre transform's summation over multiple atoms per compound and multiple compounds per reaction, which attenuates large pKa differences. [src: thermodynamic_impact]

## Key figures

- **0.11 kJ/mol kJ/mol**: median deltaG difference between Marvin and OPAM2 [src: thermodynamic_impact]

## Evidence

> The thermodynamic pipeline exhibits strong buffering: large pKa differences are attenuated by the Legendre transform's summation over multiple atoms per compound and multiple compounds per reaction, yielding median deltaG differences of only 0.11 kJ/mol between Marvin and OPAM2. [src: thermodynamic_impact]

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
