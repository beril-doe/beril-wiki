---
type: "Concept"
description: "Whether Marvin versus OPAM2 deltaG changes alter TMFA flux distributions, blocked reactions, or growth across phylogenetically diverse models; stops at experimental validation."
sources: ["summaries/thermodynamic_impact__REPORT.md"]
---
# Effect of pKa source on flux predictions across diverse organisms

This page asks whether swapping the pKa source behind the deltaG values (Marvin versus OPAM2) changes thermodynamics-based metabolic flux analysis (TMFA) results across phylogenetically diverse models. In the one report behind it, the effect is small: TMFA changed 0–1.6% of reaction fluxes in 10 organisms spanning 6 phyla, and growth was preserved. [src: thermodynamic_impact] Marvin and OPAM2 gave nearly identical flux balance analysis (FBA) solutions. [src: thermodynamic_impact] The evidence is computational only, from a single report, and the page stops at experimental validation. See also thermodynamic constraint formulation in flux balance models and [[summaries/thermodynamic_impact__REPORT]].

## Growth and flux changes under TMFA

The report expanded its analysis to 10 organisms spanning 6 phyla and diverse metabolic lifestyles to test whether the TMFA findings generalize. [src: thermodynamic_impact] All 10 kept their unconstrained growth rate under TMFA to machine precision (deltas < 10^-13), and neither Marvin nor OPAM2 caused growth reduction. [src: thermodynamic_impact] For example, [[entities/escherichia-coli]] grew at 0.5625 unconstrained, with TMFA+Marvin and with TMFA+OPAM2, with 1,210 constrained reactions. [src: thermodynamic_impact] [[entities/bacillus-subtilis-168]] grew at 0.5000 in all three conditions, with 941 constrained reactions. [src: thermodynamic_impact]

Six of 10 organisms show some TMFA flux changes, all below 2%. [src: thermodynamic_impact] Four show none: B. subtilis, S. aureus, M. tuberculosis and Synechocystis. The report reads this as full compatibility of the TMFA constraints with the unconstrained solution. [src: thermodynamic_impact]

| Organism | Reactions | Constrained | Flux-changed | % column | Newly blocked | Newly active | Reversed | Marvin vs OPAM2 differences |
|---|---|---|---|---|---|---|---|---|
| E. coli | 1,765 | 1,210 | 18 | 1.02 | 4 | 12 | 2 | 25 [src: thermodynamic_impact] |
| B. subtilis | 1,345 | 941 | 0 | 0.00 | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| P. putida | 1,494 | 1,018 | 24 | 1.61 | 14 | 9 | 0 | 17 [src: thermodynamic_impact] |
| S. enterica | 1,683 | 1,153 | 20 | 1.19 | 3 | 13 | 4 | 10 [src: thermodynamic_impact] |
| K. pneumoniae | 1,793 | 1,243 | 6 | 0.33 | 0 | 5 | 1 | 6 [src: thermodynamic_impact] |
| S. aureus | 1,128 | 775 | 0 | 0.00 | 0 | 0 | 0 | 8 [src: thermodynamic_impact] |
| M. tuberculosis | 1,150 | 797 | 0 | 0.00 | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| C. acetobutylicum | 1,066 | 708 | 10 | 0.94 | 4 | 6 | 0 | 0 [src: thermodynamic_impact] |
| Synechocystis | 980 | 684 | 0 | 0.00 | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| D. radiodurans | 1,070 | 757 | 5 | 0.47 | 0 | 4 | 1 | 0 [src: thermodynamic_impact] |

Flux changes were not random. They concentrate in exchange reactions, polyphosphate kinase rxn00499 (consistently across Proteobacteria), transport-coupled reactions rxn08527, rxn08793 and rxn09188, and reversible central-carbon reactions near thermodynamic equilibrium. [src: thermodynamic_impact] The report interprets the small range across aerobes, anaerobes, phototrophs and extremophiles as meaning that gapfilled ModelSEED models are approximately thermodynamically consistent by construction. [src: thermodynamic_impact] That is an interpretation, not a tested result.

## Marvin versus OPAM2 specifically

The pKa source has real but minor downstream effects. Under TMFA, 0–25 reactions per organism differ between Marvin and OPAM2. These are mainly alternate optimal pathways, where deltaG shifts of 1–10 kJ/mol tip the MILP solver toward different equivalent optima. [src: thermodynamic_impact] Differences can appear even where TMFA itself changes no fluxes: S. aureus shows 8 differences with 0 flux-changed reactions. [src: thermodynamic_impact] B. subtilis shows 0 differences, so the OPAM2 changes do not affect its optimal flux distribution. [src: thermodynamic_impact]

E. coli has the most differences, 25 reactions. [src: thermodynamic_impact]
- 6 reactions with large differences (|delta| = 999-1000), from alternate routing through reactions with extreme flux bounds and different MILP optima. [src: thermodynamic_impact]
- 7 reactions with small differences (|delta| = 0.25-1.0) in amino acid biosynthesis, cofactor metabolism and transport. [src: thermodynamic_impact]
- 12 reactions with unit differences (|delta| = 1.0), described as binary on/off switches in non-essential pathways. [src: thermodynamic_impact]

## Blocked reactions and directionality

With binary variables relaxed to continuous [0,1], flux variability analysis (FVA) shows 0 directionality classification changes between Marvin and OPAM2 for E. coli or B. subtilis. [src: thermodynamic_impact] Blocked-reaction counts are unchanged: E. coli has 1,139 at baseline, under TMFA+Marvin and under TMFA+OPAM2, and B. subtilis has 1,007 in each. [src: thermodynamic_impact] The report states the counts are identical for all organisms and concludes that network connectivity, not thermodynamics, determines blocked reactions. [src: thermodynamic_impact] The LP relaxation is an outer bound on the MILP-feasible range. The report therefore reads the deltaG differences as changing which alternate optimum is selected, not which reactions can carry flux. [src: thermodynamic_impact]

In the TMFA impact table, some organisms do show newly blocked reactions under TMFA, for example 14 in P. putida. [src: thermodynamic_impact] The page does not reconcile these two results.

## Caveats

All models were gapfilled on complete media. This may mask thermodynamic infeasibilities that would emerge under minimal media. [src: thermodynamic_impact]

## Open Directions

- Repeat the 10-organism comparison on minimal-media gapfilled models, to test whether the complete-media caveat hides larger Marvin-versus-OPAM2 effects.
- Report LP-relaxed FVA blocked-reaction counts for all 10 organisms in a table. Only E. coli and B. subtilis are tabulated, and this would settle the apparent mismatch with the newly blocked reactions seen in P. putida.
- Enumerate alternate optima, for example by sampling, for E. coli and P. putida. This would test whether the 1–10 kJ/mol deltaG shifts only select between equivalent optima.
- Check rxn00499 and the transport-coupled reactions in non-Proteobacteria. This would test whether the recurring affected reactions are specific to one lineage.
