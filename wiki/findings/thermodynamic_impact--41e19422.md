---
type: "Finding"
description: "TMFA constraints affect 0\u20131.6% of reaction fluxes across 10 diverse organisms spanning 6 phyla, growth rates are preserved to machine precision in all cases, and Marvin vs OPAM2 dG sources produce nearly identical FBA solutions."
finding_id: "thermodynamic_impact--41e19422"
result: "observation"
source: "thermodynamic_impact"
quantities: [{"value": "0\u20131.6%", "what": "share of reaction fluxes affected by TMFA constraints", "unit": "%", "denominator": "reaction fluxes", "scope": "10 organisms, 6 phyla"}]
caveat: "The diverse organism analysis used LP-relaxed TMFA (no integer variables) for tractability, and full MILP TMFA may reveal additional direction-locking effects, though the E. coli analysis suggests these are minor."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# TMFA barely changes fluxes across ten diverse organisms

TMFA constraints affect 0–1.6% of reaction fluxes across 10 diverse organisms spanning 6 phyla, growth rates are preserved to machine precision in all cases, and Marvin vs OPAM2 dG sources produce nearly identical FBA solutions. [src: thermodynamic_impact]

## Key figures

- **0–1.6%**: share of reaction fluxes affected by TMFA constraints (denominator reaction fluxes; scope 10 organisms, 6 phyla) [src: thermodynamic_impact]

## Evidence

> TMFA constraints affect 0–1.6% of reaction fluxes across 10 diverse organisms spanning 6 phyla, growth rates are preserved to machine precision in all cases, and Marvin vs OPAM2 dG sources produce nearly identical FBA solutions. [src: thermodynamic_impact]

From the report [[summaries/thermodynamic_impact__REPORT]].

## Caveat

The diverse organism analysis used LP-relaxed TMFA (no integer variables) for tractability, and full MILP TMFA may reveal additional direction-locking effects, though the E. coli analysis suggests these are minor. [src: thermodynamic_impact]

> The diverse organism analysis used LP-relaxed TMFA (no integer variables) for tractability. Full MILP TMFA may reveal additional direction-locking effects, though the E. coli analysis suggests these are minor. [src: thermodynamic_impact]

## Other caveats in this report

- The initial hard-cutoff analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction, constraining 928 Escherichia coli reactions (58.8%) and eliminating growth in both organisms. [src: thermodynamic_impact]
- The report says the initial minimal-impact conclusion reflected identical zero growth from a broken constraint method rather than problems with the dG values. [src: thermodynamic_impact]
- Hard cutoffs ignore metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]
- The report states that LP relaxation provides an outer bound on MILP-feasible flux ranges and interprets dG differences as changing alternate optimal solution selection rather than which reactions can carry flux. [src: thermodynamic_impact]
- All models were gapfilled on complete media, potentially masking thermodynamic infeasibilities under minimal media conditions. [src: thermodynamic_impact]
