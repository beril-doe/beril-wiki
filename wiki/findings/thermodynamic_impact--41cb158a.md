---
type: "Finding"
description: "No phenotype predictions flipped between Marvin and OPAM2."
finding_id: "thermodynamic_impact--41cb158a"
result: "null result"
source: "thermodynamic_impact"
quantities: []
caveat: "Simple phenotype panel: 12 carbon sources capture a limited phenotypic space."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# No carbon-source phenotype flipped between Marvin and OPAM2

No phenotype predictions flipped between Marvin and OPAM2. [src: thermodynamic_impact]

## Evidence

> No phenotype predictions flipped between Marvin and OPAM2. [src: thermodynamic_impact]

From the report [[summaries/thermodynamic_impact__REPORT]].

## Caveat

Simple phenotype panel: 12 carbon sources capture a limited phenotypic space. [src: thermodynamic_impact]

> **Simple phenotype panel**: 12 carbon sources capture a limited phenotypic space. [src: thermodynamic_impact]

## Other caveats in this report

- The initial hard-cutoff analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction, constraining 928 Escherichia coli reactions (58.8%) and eliminating growth in both organisms. [src: thermodynamic_impact]
- The report says the initial minimal-impact conclusion reflected identical zero growth from a broken constraint method rather than problems with the dG values. [src: thermodynamic_impact]
- Hard cutoffs ignore metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]
- The report states that LP relaxation provides an outer bound on MILP-feasible flux ranges and interprets dG differences as changing alternate optimal solution selection rather than which reactions can carry flux. [src: thermodynamic_impact]
- All models were gapfilled on complete media, potentially masking thermodynamic infeasibilities under minimal media conditions. [src: thermodynamic_impact]
