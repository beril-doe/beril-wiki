---
type: "Summary"
description: "Summary of the project Thermodynamic Impact of OPAM2 pKa Predictions on Metabolic Modeling."
doc_type: "short"
full_text: "sources/thermodynamic_impact__REPORT.md"
---
# Thermodynamic Impact of OPAM2 pKa Predictions on Metabolic Modeling

This report asked whether replacing Marvin 23.4 (ChemAxon) pKa predictions with OPAM2, a graph-convolutional neural network fine-tuned on ModelSEED biochemistry, changes metabolic model predictions. It traced the change through the full pipeline: pKa, Legendre transform, reaction deltaG, then TMFA (thermodynamics-based metabolic flux analysis)-constrained FBA (flux balance analysis). [src: thermodynamic_impact] The pKa differences are large, but the downstream effect is negligible. [src: thermodynamic_impact] The report concludes that OPAM2 pKa predictions can replace Marvin pKa in the ModelSEED thermodynamic pipeline without meaningful impact on downstream FBA predictions. [src: thermodynamic_impact] An initial hard-cutoff analysis was flawed, and the report replaced it with a TMFA implementation. [src: thermodynamic_impact] The study measures downstream impact, not pKa prediction accuracy, and has no experimental validation of pKa accuracy. [src: thermodynamic_impact] See also [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms]], thermodynamic constraint formulation in flux balance models and [[concepts/disagreement-among-deltag-estimation-methods]].

## Key Findings

### pKa differences are large but buffered

Marvin and OPAM2 differ by a mean |delta| of 2.17 pKa units across 82,171 ionizable atoms in 22,399 compounds. [src: thermodynamic_impact]

OPAM2 diverges most strongly from Marvin for multi-protic compounds and molecules with complex electronic environments. [src: thermodynamic_impact]

The report attributes the buffering to the Legendre transform's summation over atoms per compound and compounds per reaction, giving a median Marvin–OPAM2 deltaG difference of 0.11 kJ/mol. [src: thermodynamic_impact] It concludes that the Legendre transform strongly buffers pKa-level differences, leaving deltaG changes small relative to group contribution uncertainty and disagreement between deltaG estimation tools. [src: thermodynamic_impact]

The BayesianRidge group contribution model predicts pKa-independent dG_model_only from molecular fingerprints, and pKa changes affect only the Legendre transform pH correction. [src: thermodynamic_impact] The report recomputed 31,924 reactions. [src: thermodynamic_impact] It reused the existing dG_model_only from the dGPredictor BayesianRidge model and recomputed ddG0_pH_correction via a Legendre transform with an updated compound cache (pH 7.0, I = 0.25 M, T = 298.15 K). [src: thermodynamic_impact] Their dG_model_only values were confirmed identical. [src: thermodynamic_impact] Their ddG0_pH_correction values differ because compound pKas were updated. [src: thermodynamic_impact]

Of the recomputed reactions:
- 72.9% change by < 1 kJ/mol. [src: thermodynamic_impact]
- 17.6% change by 1-5 kJ/mol. [src: thermodynamic_impact]
- 7.5% change by > 5 kJ/mol. [src: thermodynamic_impact]
- 311 reactions (1.0%) change by more than 100 kJ/mol. [src: thermodynamic_impact]
- 840 reactions (2.6%) reverse sign between favorable and unfavorable. [src: thermodynamic_impact]

The report argues that the physiological concentration range (1 µM to 20 mM) supplies ~25 kJ/mol of driving force per metabolite (RT × ln(20000) = 24.5 kJ/mol at 298 K). [src: thermodynamic_impact] It says this buffer easily compensates for the mean pKa-driven dG change of 13.35 kJ/mol. [src: thermodynamic_impact]

### Context: choice of deltaG method matters more

The contextual comparison used 24,619 reactions with estimates from both eQuilibrator and dGPredictor using Marvin predictions. [src: thermodynamic_impact] Marvin-to-OPAM2 deltaG differences are 4.3x smaller by mean and 155x smaller by median than the eQuilibrator–dGPredictor disagreement, whose median is 17 kJ/mol with 19.3% sign discordance. [src: thermodynamic_impact] The report concludes that the dominant source of thermodynamic uncertainty is the deltaG estimation method, not the pKa source: eQuilibrator vs dGPredictor disagreement (median 17 kJ/mol, 19.3% sign discordance) dwarfs Marvin vs OPAM2 (median 0.11 kJ/mol, 2.7% sign discordance). [src: thermodynamic_impact]

| Metric | eQuilibrator vs dGPredictor | Marvin vs OPAM2 |
|---|---|---|
| Mean abs. deltaG difference | 57.47 kJ/mol [src: thermodynamic_impact] | 13.35 kJ/mol [src: thermodynamic_impact] |
| Median abs. deltaG difference | 17.00 kJ/mol [src: thermodynamic_impact] | 0.11 kJ/mol [src: thermodynamic_impact] |
| Sign changes | 4,741 (19.3%) [src: thermodynamic_impact] | 850 (2.7%) [src: thermodynamic_impact] |
| Same sign | 68.7% [src: thermodynamic_impact] | 86.2% [src: thermodynamic_impact] |

The report states that pKa-source choice introduces far less variation than deltaG-method choice, with a 7x lower sign-change rate (2.7% vs 19.3%). [src: thermodynamic_impact]

### Initial hard-cutoff analysis (flawed)

Reference models were built with modelseedpy 0.4.3, GramNeg/GramPos templates, BV-BRC genomes, ATP (adenosine triphosphate) correction and gapfilling. [src: thermodynamic_impact] The pipeline was ModelSEEDTemplates v7.0 with MSBuilder + MSATPCorrection + MSGapfill. [src: thermodynamic_impact] The Escherichia coli K-12 MG1655 model has 1,765 reactions, 1,317 genes and growth 0.5625. [src: thermodynamic_impact] The Bacillus subtilis 168 model has 1,345 reactions, 1,033 genes and growth 0.5000. [src: thermodynamic_impact]

FVA (flux variability analysis) used directional constraints with a |deltaG| > 5 kJ/mol threshold. [src: thermodynamic_impact] For E. coli, 1,732 reactions were blocked with Marvin and 1,731 with OPAM2, with 2 newly blocked and 3 newly unblocked. [src: thermodynamic_impact] For B. subtilis, 1,337 reactions were blocked under each pKa source, with none newly blocked or unblocked. [src: thermodynamic_impact]

The E. coli changes were:
- rxn01545 went from forward to blocked (Marvin dG = 3.8, OPAM2 dG = -159.8 kJ/mol). [src: thermodynamic_impact]
- rxn01649 went from reverse to blocked (Marvin dG = 11.6, OPAM2 dG = -152.4 kJ/mol). [src: thermodynamic_impact]
- rxn10052 went from blocked to variable as constraints relaxed. [src: thermodynamic_impact]
- rxn00097 went from blocked to variable as constraints relaxed. [src: thermodynamic_impact]
- rxn00104 went from blocked to variable as constraints relaxed. [src: thermodynamic_impact]

Carbon-source tests covered 12 conditions per organism. [src: thermodynamic_impact] Phenotype testing used minimal media with a single carbon source and an FBA growth > 1e-6 threshold. [src: thermodynamic_impact] The panel of 12 carbon sources captures a limited phenotypic space. [src: thermodynamic_impact] CP, CN, FP and FN are the report's counts.

| Organism | Constraint | CP | CN | FP | FN | Accuracy |
|---|---|---|---|---|---|---|
| E. coli | Unconstrained | 8 | 2 | 1 | 1 | 83.3% [src: thermodynamic_impact] |
| E. coli | Marvin | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |
| E. coli | OPAM2 | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |
| B. subtilis | Unconstrained | 7 | 2 | 1 | 2 | 75.0% [src: thermodynamic_impact] |
| B. subtilis | Marvin | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |
| B. subtilis | OPAM2 | 0 | 3 | 0 | 9 | 25.0% [src: thermodynamic_impact] |

Both hard-cutoff constraint sets eliminated growth entirely and produced identical false-negative patterns. [src: thermodynamic_impact] No phenotype predictions flipped between Marvin and OPAM2. [src: thermodynamic_impact]

### Why the hard cutoff failed

The initial analysis locked reactions with |dG| > 5 kJ/mol to the favorable direction. It constrained 928 E. coli reactions (58.8%) and eliminated growth in both organisms. [src: thermodynamic_impact] The "minimal impact" conclusion was technically correct because both gave identical zero growth. It held for the wrong reason, since the constraint method was broken, not the dG values. [src: thermodynamic_impact]

Six essential reactions have standard-condition dG opposing their required in-vivo flux direction. [src: thermodynamic_impact] Phosphotransacetylase has dG° = +5.9 kJ/mol but must run forward for acetate metabolism. [src: thermodynamic_impact] Hard cutoffs ignore the metabolite-concentration shifts that make effective dG favorable for essential reactions in living cells. [src: thermodynamic_impact]

The report concludes that constraint formulation (hard cutoff vs TMFA) has a far greater effect on model predictions than pKa source. [src: thermodynamic_impact] Hard cutoffs predicted zero growth with either Marvin or OPAM2, while TMFA preserved full growth with both. [src: thermodynamic_impact] Hard cutoffs eliminated growth entirely; TMFA preserved it across all organisms and dG sources. [src: thermodynamic_impact]

## TMFAPkg and the corrected result

The report implemented TMFAPkg, a new ModelSEEDpy FBA package following the TMFA formulation of Henry, Broadbelt, and Hatzimanikatis (2007, Biophys J 92:1792-1805). [src: thermodynamic_impact] Its source code is in src/tmfapkg.py and is also installed as modelseedpy.fbapkg.tmfapkg. [src: thermodynamic_impact] The methods describe it as a MILP (mixed-integer linear program) with binary direction variables z_fwd and z_rev, continuous ln(concentration) variables bounded by [1 µM, 20 mM], and dG decomposition constraints including transport membrane potential correction. [src: thermodynamic_impact] The formulation is:
- Each reaction has binary forward and reverse use variables coupled to flux through big-M constraints. [src: thermodynamic_impact]
- Each metabolite has a continuous ln(concentration) variable with default bounds of 1 uM to 20 mM. [src: thermodynamic_impact]
- Reaction dG is decomposed into standard dG, RT-weighted stoichiometric log-concentration terms, a transport correction and an error term. [src: thermodynamic_impact]
- Active forward reactions require dG_rxn <= 0, and active reverse reactions require dG_rxn >= 0. [src: thermodynamic_impact]
- Mutual exclusion is imposed through z_fwd + z_rev <= 1. [src: thermodynamic_impact]
- In Mode A, H+ is excluded from the concentration sum because reaction-level dG is already pH-transformed by the Legendre transform. [src: thermodynamic_impact]
- Water is excluded, with activity = 1. [src: thermodynamic_impact]
- Transport reactions carry a membrane-potential correction of F * delta_psi * net_charge with c0 = -160 mV. [src: thermodynamic_impact]
- The big-M constant is computed automatically from the data range with a 20% safety margin. [src: thermodynamic_impact]
- Each reaction's error variable is bounded by +/- 2 * dG_std. [src: thermodynamic_impact]

pKa predictions came from OPAM2 v1.0 with ModelSEED-finetuned weights (weight_acid_modelseed.pth, weight_base_modelseed.pth). [src: thermodynamic_impact] The solver was GLPK, used as MILP for TMFA and as LP for standard FBA and relaxed FVA. [src: thermodynamic_impact]

With TMFA, E. coli growth is 0.5625 unconstrained, 0.5625 with TMFA+Marvin and 0.5625 with TMFA+OPAM2, with 1,210 constrained reactions. [src: thermodynamic_impact] B. subtilis growth is 0.5000 unconstrained, with TMFA+Marvin and with TMFA+OPAM2, with 941 constrained reactions. [src: thermodynamic_impact] TMFA constrains more E. coli reactions than hard cutoffs (1,210 vs 928) while preserving full growth. [src: thermodynamic_impact] The GLPK MILP solver finds concentration assignments that make all active reactions thermodynamically feasible. [src: thermodynamic_impact]

### Worked reaction examples under TMFA (B. subtilis)

Concentrations can make reactions feasible despite their standard dG. Phosphotransacetylase (dG° = +5.9) carries forward flux because concentrations shift the effective dG to ~0, just at the feasibility boundary. [src: thermodynamic_impact] The report calls reverse flux through polyphosphate kinase (dG° = +26.9) thermodynamically consistent. [src: thermodynamic_impact]

| Reaction | Marvin dG° (kJ/mol) | Flux | Actual dGrxn | z_fwd | z_rev |
|---|---|---|---|---|---|
| rxn00173 phosphotransacetylase | +5.9 [src: thermodynamic_impact] | 1.0 (forward) [src: thermodynamic_impact] | -0.0 [src: thermodynamic_impact] | 1 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] |
| rxn00499 polyphosphate kinase | +26.9 [src: thermodynamic_impact] | -999.0 (reverse) [src: thermodynamic_impact] | 0.0 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] | 1 [src: thermodynamic_impact] |
| rxn00117 ATP:sulfate adenylyltransferase | -2.2 [src: thermodynamic_impact] | 0.0 [src: thermodynamic_impact] | 17.6 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] |
| rxn00209 lactate dehydrogenase | -104.3 [src: thermodynamic_impact] | 0.0 [src: thermodynamic_impact] | -123.1 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] | not reported [src: thermodynamic_impact] |
| rxn05561 G3P dehydrogenase | 0.0 [src: thermodynamic_impact] | 0.0 [src: thermodynamic_impact] | -16.4 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] | 0 [src: thermodynamic_impact] |
| rxn00062 F1-ATPase | -25.5 [src: thermodynamic_impact] | 0.0 [src: thermodynamic_impact] | not reported [src: thermodynamic_impact] | not reported [src: thermodynamic_impact] | not reported [src: thermodynamic_impact] |

## Marvin versus OPAM2 under TMFA

Under TMFA, 25 E. coli reactions show flux differences between Marvin and OPAM2 dG values. [src: thermodynamic_impact] They fall into three groups:
- 6 reactions with large differences (|delta| = 999-1000), attributed to alternate pathway routing through reactions with extreme flux bounds and different optimal solutions to the MILP. [src: thermodynamic_impact]
- 7 reactions with small differences (|delta| = 0.25-1.0) in amino acid biosynthesis, cofactor metabolism and transport pathways. [src: thermodynamic_impact]
- 12 reactions with unit differences (|delta| = 1.0), described as binary on/off switches in non-essential pathways. [src: thermodynamic_impact]

B. subtilis shows 0 flux differences, so OPAM2 pKa changes do not affect its optimal flux distribution. [src: thermodynamic_impact] Across organisms, Marvin-versus-OPAM2 flux differences affect 0–25 reactions per organism, mainly alternate optimal pathways where dG shifts of 1–10 kJ/mol tip the MILP solver toward equivalent optima. [src: thermodynamic_impact]

With binary variables relaxed to continuous [0,1], FVA shows 0 directionality classification changes between Marvin and OPAM2 for either E. coli or B. subtilis. [src: thermodynamic_impact] FVA used cobra flux_variability_analysis with fraction_of_optimum=0.0. [src: thermodynamic_impact] The report reads the LP relaxation as an outer bound on the MILP-feasible flux range. It infers that dG differences change which alternate optimal solution the solver selects, not which reactions can carry flux. [src: thermodynamic_impact] Blocked reaction counts are unchanged:
- E. coli has 1,139 blocked reactions at baseline, 1,139 under TMFA+Marvin and 1,139 under TMFA+OPAM2, with 0 changes. [src: thermodynamic_impact]
- B. subtilis has 1,007 at baseline, 1,007 under TMFA+Marvin and 1,007 under TMFA+OPAM2, with 0 changes. [src: thermodynamic_impact]

The report concludes that blocked reactions are determined by network connectivity, not thermodynamic constraints, because blocked counts are identical under LP-relaxed TMFA-FVA for all organisms. [src: thermodynamic_impact]

## Generalization to 10 organisms

To test whether the TMFA findings generalize, the report expanded the analysis to 10 organisms spanning 6 phyla and diverse metabolic lifestyles. [src: thermodynamic_impact] All models were built with the ModelSEEDpy pipeline (MSBuilder → MSATPCorrection → MSGapfill), BV-BRC genome annotations and ModelSEED v7.0 templates. [src: thermodynamic_impact] Across them, TMFA constraints affect 0–1.6% of reaction fluxes. [src: thermodynamic_impact] Growth rates are preserved to machine precision, and Marvin and OPAM2 dG sources give nearly identical FBA solutions. [src: thermodynamic_impact] All 10 organisms keep their unconstrained growth under TMFA with deltas < 10^-13, and neither dG source reduces growth. [src: thermodynamic_impact]

| Organism | Phylum, template | Genes | Reactions | Growth |
|---|---|---|---|---|
| E. coli K-12 MG1655 | Proteobacteria, GramNeg [src: thermodynamic_impact] | 1,317 [src: thermodynamic_impact] | 1,765 [src: thermodynamic_impact] | 0.5625 [src: thermodynamic_impact] |
| B. subtilis 168 | Firmicutes, GramPos [src: thermodynamic_impact] | 1,033 [src: thermodynamic_impact] | 1,345 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |
| P. putida KT2440 | Proteobacteria, GramNeg [src: thermodynamic_impact] | 1,350 [src: thermodynamic_impact] | 1,494 [src: thermodynamic_impact] | 0.1667 [src: thermodynamic_impact] |
| S. aureus NCTC 8325 | Firmicutes, GramPos [src: thermodynamic_impact] | 777 [src: thermodynamic_impact] | 1,128 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |
| S. enterica LT2 | Proteobacteria, GramNeg [src: thermodynamic_impact] | 1,306 [src: thermodynamic_impact] | 1,683 [src: thermodynamic_impact] | 0.5625 [src: thermodynamic_impact] |
| M. tuberculosis H37Rv | Actinobacteria, GramPos [src: thermodynamic_impact] | 879 [src: thermodynamic_impact] | 1,150 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |
| C. acetobutylicum ATCC 824 | Firmicutes, GramPos [src: thermodynamic_impact] | 819 [src: thermodynamic_impact] | 1,066 [src: thermodynamic_impact] | 1.0000 [src: thermodynamic_impact] |
| Synechocystis sp. PCC 6803 | Cyanobacteria, GramNeg [src: thermodynamic_impact] | 719 [src: thermodynamic_impact] | 980 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |
| K. pneumoniae HS11286 | Proteobacteria, GramNeg [src: thermodynamic_impact] | 1,601 [src: thermodynamic_impact] | 1,793 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |
| D. radiodurans ATCC 13939 | Deinococcota, GramNeg [src: thermodynamic_impact] | 712 [src: thermodynamic_impact] | 1,070 [src: thermodynamic_impact] | 0.5000 [src: thermodynamic_impact] |

The TMFA impact table gives, per organism, reactions, constrained reactions, flux-changed reactions (percentage), newly blocked, newly active, reversed, and Marvin-versus-OPAM2 differences:

| Organism | Reactions | Constrained | Flux-changed (%) | Newly blocked | Newly active | Reversed | Marvin vs OPAM2 |
|---|---|---|---|---|---|---|---|
| E. coli | 1,765 | 1,210 | 18 (1.02) | 4 | 12 | 2 | 25 [src: thermodynamic_impact] |
| B. subtilis | 1,345 | 941 | 0 (0.00) | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| P. putida | 1,494 | 1,018 | 24 (1.61) | 14 | 9 | 0 | 17 [src: thermodynamic_impact] |
| S. aureus | 1,128 | 775 | 0 (0.00) | 0 | 0 | 0 | 8 [src: thermodynamic_impact] |
| S. enterica | 1,683 | 1,153 | 20 (1.19) | 3 | 13 | 4 | 10 [src: thermodynamic_impact] |
| M. tuberculosis | 1,150 | 797 | 0 (0.00) | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| C. acetobutylicum | 1,066 | 708 | 10 (0.94) | 4 | 6 | 0 | 0 [src: thermodynamic_impact] |
| Synechocystis | 980 | 684 | 0 (0.00) | 0 | 0 | 0 | 0 [src: thermodynamic_impact] |
| K. pneumoniae | 1,793 | 1,243 | 6 (0.33) | 0 | 5 | 1 | 6 [src: thermodynamic_impact] |
| D. radiodurans | 1,070 | 757 | 5 (0.47) | 0 | 4 | 1 | 0 [src: thermodynamic_impact] |

Six of 10 organisms show some TMFA flux changes, all below 2%. [src: thermodynamic_impact] Four (B. subtilis, S. aureus, M. tuberculosis, Synechocystis) show zero flux changes, which the report reads as TMFA constraints being entirely compatible with the unconstrained solution. [src: thermodynamic_impact] Flux changes concentrate in exchange reactions, polyphosphate kinase (rxn00499, consistently affected across Proteobacteria), transport-coupled reactions (rxn08527, rxn08793, rxn09188) and reversible central carbon reactions near thermodynamic equilibrium. [src: thermodynamic_impact] The report interprets the small, consistent 0–1.6% range across 6 phyla and aerobes, anaerobes, phototrophs and extremophiles as showing that gapfilled ModelSEED models are approximately thermodynamically consistent by construction. [src: thermodynamic_impact]

## Caveats and Open Work

All models were gapfilled on complete media, which may mask thermodynamic infeasibilities that would emerge under minimal media conditions. [src: thermodynamic_impact] The phenotype prediction results (NB08) highlight this: TMFA blocks growth on all alternative carbon sources. [src: thermodynamic_impact]

- The diverse organism analysis used LP-relaxed TMFA without integer variables for tractability. Full MILP TMFA may reveal additional direction-locking effects, although the E. coli analysis suggests these are minor. [src: thermodynamic_impact]
- TMFA used default concentration bounds of 1 µM – 10 mM, and organism-specific metabolomics could shift some reactions across the feasibility boundary. [src: thermodynamic_impact]
- MILP solutions came from GLPK, which may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces. [src: thermodynamic_impact]
- The study did not experimentally validate pKa accuracy. [src: thermodynamic_impact]
- The phenotype panel of 12 carbon sources captures a limited phenotypic space. [src: thermodynamic_impact]
