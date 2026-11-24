# Andrew Freiburger

## Contributions

The project [[summaries/thermodynamic_impact__REPORT]] tested whether replacing Marvin 23.4 (ChemAxon) pKa predictions with OPAM2 changes metabolic model predictions. OPAM2 is a graph-convolutional neural network fine-tuned on ModelSEED biochemistry. The project traced the change through the pipeline from pKa to Legendre transform, reaction deltaG, and TMFA-constrained FBA. TMFA is thermodynamics-based metabolic flux analysis, and FBA is flux balance analysis. [src: thermodynamic_impact] It concluded that OPAM2 pKa predictions can replace Marvin pKa in the ModelSEED thermodynamic pipeline without meaningful impact on downstream FBA predictions. [src: thermodynamic_impact] The study measures downstream impact only and has no experimental validation of pKa accuracy. [src: thermodynamic_impact]

Marvin and OPAM2 differ by a mean |delta| of 2.17 pKa units across 82,171 ionizable atoms in 22,399 compounds. [src: thermodynamic_impact] The project recomputed 31,924 reactions and found a median Marvin–OPAM2 deltaG difference of 0.11 kJ/mol. [src: thermodynamic_impact] Of these reactions, 72.9% changed by < 1 kJ/mol, 17.6% by 1-5 kJ/mol, and 7.5% by > 5 kJ/mol. [src: thermodynamic_impact] 311 reactions (1.0%) changed by more than 100 kJ/mol, and 840 reactions (2.6%) reversed sign between favorable and unfavorable. [src: thermodynamic_impact] The project attributed the buffering to the Legendre transform's summation over atoms and compounds. [src: thermodynamic_impact]

For 24,619 reactions with both eQuilibrator and dGPredictor estimates, the eQuilibrator–dGPredictor disagreement had a median of 17 kJ/mol and 19.3% sign discordance. Marvin vs OPAM2 had a median of 0.11 kJ/mol and 2.7% sign discordance. [src: thermodynamic_impact] The project concluded that the deltaG estimation method contributes more thermodynamic uncertainty than the pKa source. [src: thermodynamic_impact] See also [[concepts/disagreement-among-deltag-estimation-methods]].

An initial hard-cutoff analysis (|dG| > 5 kJ/mol) eliminated growth in both E. coli and B. subtilis. It constrained 928 E. coli reactions (58.8%). Accuracy on 12 carbon sources fell to 25.0% under both Marvin and OPAM2, and no phenotype predictions flipped between them. [src: thermodynamic_impact] The project judged the constraint method to be broken, so the "minimal impact" result held for the wrong reason. [src: thermodynamic_impact] It then implemented TMFAPkg, a MILP-based ModelSEEDpy FBA package following the TMFA formulation of Henry, Broadbelt, and Hatzimanikatis (2007). [src: thermodynamic_impact] With TMFA, E. coli growth was 0.5625 unconstrained, with Marvin and with OPAM2, and 1,210 reactions were constrained. B. subtilis growth was 0.5000 in all three cases, with 941 constrained reactions. [src: thermodynamic_impact]

## Projects (1)

- [[summaries/thermodynamic_impact__REPORT|thermodynamic_impact]]
