---
type: "Finding"
description: "B. subtilis shows 0 flux differences under TMFA, so the OPAM2 pKa changes do not affect the optimal flux distribution for this organism."
finding_id: "thermodynamic_impact--d3f5a72f"
result: "null result"
source: "thermodynamic_impact"
quantities: [{"value": "0", "what": "Marvin vs OPAM2 flux differences under TMFA", "unit": "", "denominator": "", "scope": "B. subtilis"}]
caveat: "MILP solutions were obtained with GLPK, which may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces."
first_added: "2026-11-24"
source_hash: "2ea89c665f90710dd14b322d9dfb494aedf9763161b54fafb11e832cae371ae4"
---
# OPAM2 does not alter B. subtilis optimal TMFA flux

B. subtilis shows 0 flux differences under TMFA, so the OPAM2 pKa changes do not affect the optimal flux distribution for this organism. [src: thermodynamic_impact]

## Key figures

- **0**: Marvin vs OPAM2 flux differences under TMFA (scope B. subtilis) [src: thermodynamic_impact]

## Evidence

> B. subtilis shows **0 flux differences** — the OPAM2 pKa changes do not affect the optimal flux distribution for this organism. [src: thermodynamic_impact]

From the report [[summaries/thermodynamic_impact__REPORT]].

## Caveat

MILP solutions were obtained with GLPK, which may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces. [src: thermodynamic_impact]

> MILP solutions were obtained with GLPK, which may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces. [src: thermodynamic_impact]

## Other caveats in this report

- The initial hard-cutoff analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction, constraining 928 Escherichia coli reactions (58.8%) and eliminating growth in both organisms. [src: thermodynamic_impact]
- The report says the initial minimal-impact conclusion reflected identical zero growth from a broken constraint method rather than problems with the dG values. [src: thermodynamic_impact]
- Hard cutoffs ignore metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]
- The report states that LP relaxation provides an outer bound on MILP-feasible flux ranges and interprets dG differences as changing alternate optimal solution selection rather than which reactions can carry flux. [src: thermodynamic_impact]
- All models were gapfilled on complete media, potentially masking thermodynamic infeasibilities under minimal media conditions. [src: thermodynamic_impact]
