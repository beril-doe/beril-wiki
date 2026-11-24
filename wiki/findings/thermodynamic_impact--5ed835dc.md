---
type: "Finding"
description: "The report concludes the constraint method matters more than the pKa source: hard cutoffs produced zero growth regardless of whether Marvin or OPAM2 pKas were used, while TMFA preserved full growth with both."
finding_id: "thermodynamic_impact--5ed835dc"
result: "inference"
source: "thermodynamic_impact"
quantities: []
caveat: "All models were gapfilled on complete media, which may mask thermodynamic infeasibilities that would emerge under minimal media conditions."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# Constraint method matters more than pKa source

The report concludes the constraint method matters more than the pKa source: hard cutoffs produced zero growth regardless of whether Marvin or OPAM2 pKas were used, while TMFA preserved full growth with both. [src: thermodynamic_impact]

## Evidence

> 1. **The constraint method matters more than the pKa source.** Hard cutoffs produced catastrophically wrong predictions (zero growth) regardless of whether Marvin or OPAM2 pKas were used. TMFA produces correct predictions (full growth preserved) with both. [src: thermodynamic_impact]

From the report [[summaries/thermodynamic_impact__REPORT]].

## Caveat

All models were gapfilled on complete media, which may mask thermodynamic infeasibilities that would emerge under minimal media conditions. [src: thermodynamic_impact]

> All models were gapfilled on complete media, which may mask thermodynamic infeasibilities that would emerge under minimal media conditions. [src: thermodynamic_impact]

## Other caveats in this report

- The initial hard-cutoff analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction, constraining 928 Escherichia coli reactions (58.8%) and eliminating growth in both organisms. [src: thermodynamic_impact]
- The report says the initial minimal-impact conclusion reflected identical zero growth from a broken constraint method rather than problems with the dG values. [src: thermodynamic_impact]
- Hard cutoffs ignore metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]
- The report states that LP relaxation provides an outer bound on MILP-feasible flux ranges and interprets dG differences as changing alternate optimal solution selection rather than which reactions can carry flux. [src: thermodynamic_impact]
- The diverse organism analysis used LP-relaxed TMFA without integer variables for tractability, and full MILP TMFA may reveal additional direction-locking effects, although the Escherichia coli analysis suggests these are minor. [src: thermodynamic_impact]
