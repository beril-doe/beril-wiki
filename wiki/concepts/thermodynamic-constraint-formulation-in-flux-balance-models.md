---
type: "Concept"
description: "How hard deltaG cutoffs versus concentration-aware TMFA constraints affect growth, flux, directionality and carbon-source growth predictions (12-condition panel) in genome-scale models."
sources: ["summaries/thermodynamic_impact__REPORT.md"]
---
# Thermodynamic constraint formulation in flux balance models

This page compares two ways of adding thermodynamic constraints to genome-scale flux balance analysis (FBA) models: hard deltaG cutoffs and concentration-aware TMFA (thermodynamics-based metabolic flux analysis). In the thermodynamic_impact report, the constraint method had a far larger effect on predictions than the pKa source. [src: thermodynamic_impact] The evidence comes from [[entities/escherichia-coli]] and [[entities/bacillus-subtilis-168]] for the main comparison, plus a 10-organism TMFA analysis. See also [[concepts/effect-of-pka-source-on-flux-predictions-across-diverse-organisms]] and [[summaries/thermodynamic_impact__REPORT]].

## Literature Context

The candidate literature establishes that thermodynamic constraints are a recognised way to improve flux balance analysis (FBA), which predicts growth and fluxes by linear optimization over a stoichiometric network. Reviews describe adding thermodynamic, kinetic, expression and regulatory constraints to classical FBA to improve prediction accuracy and remove non-physical fluxes [PMID 36476223](https://pubmed.ncbi.nlm.nih.gov/36476223/) [PMID 31893383](https://pubmed.ncbi.nlm.nih.gov/31893383/). Thermodynamics-based metabolic flux analysis (TMFA) adds linear thermodynamic constraints to mass balance. It yields flux distributions with no thermodynamically infeasible reactions, and it also reports reaction free-energy changes and metabolite activity ranges [PMID 17172310](https://pubmed.ncbi.nlm.nih.gov/17172310/). In the original TMFA of an E. coli genome-scale model, some reactions had a free-energy change close to zero. Dihydroorotase was named as a possible thermodynamic bottleneck. Other reactions had a strongly negative free-energy change whatever the metabolite concentrations [PMID 17172310](https://pubmed.ncbi.nlm.nih.gov/17172310/). An earlier concentration-aware formulation made flux directions consistent with Gibbs energies that depend on metabolite levels. It was tested on a 30-reaction erythrocyte core network and on the 931-reaction E. coli network iJR904. It concluded that sensitivity to standard Gibbs energies and concentration ranges grows as network complexity increases [PMID 17543097](https://pubmed.ncbi.nlm.nih.gov/17543097/). Related work addresses tooling and tractability. Thermo-Flux automates building thermodynamic-stoichiometric models and was applied to 87 BiGG models, with improved flux predictions shown for one yeast model, iMM904 [PMID 42399466](https://pubmed.ncbi.nlm.nih.gov/42399466/). Localized loopless constraints speed up loopless flux variability analysis by a factor of 10-150 over the original loopless constraints [PMID 29868725](https://pubmed.ncbi.nlm.nih.gov/29868725/).

The corpus's central finding is that hard deltaG cutoffs (|dG| > 5 kJ/mol locked to the favorable direction) eliminated growth in E. coli and B. subtilis. Concentration-aware TMFA kept the unconstrained growth of 0.5625 and 0.5000. This is consistent with the literature's view that concentrations must enter the formulation. Standard-condition free energies alone do not decide feasibility, and the TMFA framework lets concentrations shift effective driving forces [PMID 17172310](https://pubmed.ncbi.nlm.nih.gov/17172310/) [PMID 17543097](https://pubmed.ncbi.nlm.nih.gov/17543097/). The corpus's example of phosphotransacetylase, with dG° +5.9 kJ/mol but an effective dGrxn near zero, illustrates this. The candidate papers do not test hard cutoffs directly, so the hard-cutoff failure is the corpus's own result, and it also reflects a broken constraint implementation.

The corpus's weak dependence on the free-energy source is only loosely aligned with the earlier sensitivity result. That study used two test networks, a 30-reaction erythrocyte core and the 931-reaction E. coli model, and found sensitivity rising with network complexity [PMID 17543097](https://pubmed.ncbi.nlm.nih.gov/17543097/). The corpus saw Marvin and OPAM2 give nearly identical solutions in 10 organisms, with 0–1.6% of fluxes affected. That outcome is therefore not predicted by the complexity trend, and it may reflect the LP relaxation and default 1 µM – 10 mM bounds the corpus used. It extends the literature to multiple phyla, but the comparison is indirect. The candidate papers say nothing on the corpus's carbon-source panel result, in which TMFA is reported to block alternative carbon sources despite preserved growth. That result is unresolved and novel here.

## Hard cutoffs versus TMFA: growth

Hard cutoffs gave zero growth with either Marvin or OPAM2 pKas, while TMFA kept full growth with both. [src: thermodynamic_impact] Hard cutoffs eliminated growth entirely; TMFA preserved it across all organisms and dG sources. [src: thermodynamic_impact]

The initial analysis locked reactions with |dG| > 5 kJ/mol to the thermodynamically favorable direction. This constrained 928 E. coli reactions (58.8%) and eliminated growth in both organisms. [src: thermodynamic_impact] The report says the earlier "minimal impact" conclusion was technically correct, because both gave identical zero growth. It was correct for the wrong reason: the constraint method was broken, not the dG values. [src: thermodynamic_impact]

Growth under TMFA matched the unconstrained values. Columns are unconstrained, TMFA+Marvin, TMFA+OPAM2, and number of constrained reactions.
- E. coli: 0.5625, 0.5625, 0.5625, 1,210 [src: thermodynamic_impact]
- B. subtilis: 0.5000, 0.5000, 0.5000, 941 [src: thermodynamic_impact]

TMFA constrains more E. coli reactions than hard cutoffs (1,210 vs 928) and still preserves full growth. [src: thermodynamic_impact] Across 10 diverse organisms spanning 6 phyla, TMFA constraints affect 0–1.6% of reaction fluxes. Growth rates are preserved to machine precision, and Marvin and OPAM2 dG sources give nearly identical FBA solutions. [src: thermodynamic_impact]

## Why hard cutoffs fail

Six essential reactions have standard-condition dG opposing their required in-vivo flux direction. One example is phosphotransacetylase, with dG° = +5.9 kJ/mol, which must run forward for acetate metabolism. [src: thermodynamic_impact] These reactions work in living cells because metabolite concentrations shift the effective dG to be favorable. Hard cutoffs ignore this driving force. [src: thermodynamic_impact] The GLPK MILP solver finds concentration assignments that make all active reactions thermodynamically feasible. [src: thermodynamic_impact]

Selected TMFA reaction results (Marvin dG°) show the concentration effect:
- Phosphotransacetylase (rxn00173) has dG° +5.9 kJ/mol, forward flux 1.0, actual dGrxn -0.0, z_fwd 1 and z_rev 0. [src: thermodynamic_impact] It carries forward flux because concentrations shift the effective dG to ~0, just at the feasibility boundary. [src: thermodynamic_impact]
- Polyphosphate kinase (rxn00499) has dG° +26.9 kJ/mol, reverse flux -999.0, actual dGrxn 0.0, z_fwd 0 and z_rev 1. [src: thermodynamic_impact] The report interprets this reverse flux as thermodynamically consistent. [src: thermodynamic_impact]
- ATP:sulfate adenylyltransferase (rxn00117) has dG° -2.2 kJ/mol, flux 0.0, actual dGrxn 17.6, and z_fwd and z_rev both 0. [src: thermodynamic_impact]
- Lactate dehydrogenase (rxn00209) has dG° -104.3 kJ/mol, flux 0.0, actual dGrxn -123.1 and z_fwd 0, with no z_rev reported. [src: thermodynamic_impact]
- G3P dehydrogenase (rxn05561) has dG° 0.0 kJ/mol, flux 0.0, actual dGrxn -16.4, and z_fwd and z_rev both 0. [src: thermodynamic_impact]
- F1-ATPase (rxn00062) has dG° -25.5 kJ/mol and flux 0.0, with no actual dGrxn or direction indicators reported. [src: thermodynamic_impact]

## Directionality (flux variability)

The initial flux variability analysis (FVA) used directional constraints with a |deltaG| > 5 kJ/mol threshold. [src: thermodynamic_impact] Under it, E. coli had 1,732 Marvin-blocked reactions and 1,731 OPAM2-blocked reactions, with 2 newly blocked and 3 newly unblocked. [src: thermodynamic_impact] B. subtilis had 1,337 blocked reactions for each pKa source, with 0 newly blocked and 0 newly unblocked. [src: thermodynamic_impact] The pKa source therefore changed very few reactions, even though the hard-cutoff method itself was broken. [src: thermodynamic_impact]

## Carbon-source growth predictions

Phenotype testing used 12 carbon-source conditions per organism. [src: thermodynamic_impact] It used minimal media with a single carbon source and an FBA growth > 1e-6 threshold. [src: thermodynamic_impact] Both hard-cutoff constraint sets eliminated growth entirely and produced identical false-negative patterns. [src: thermodynamic_impact] No predictions flipped between Marvin and OPAM2. [src: thermodynamic_impact] The phenotype results show TMFA blocking growth on all alternative carbon sources. [src: thermodynamic_impact]

Counts are CP (correct positive), CN (correct negative), FP (false positive), FN (false negative) and accuracy:
- E. coli, Unconstrained: CP 8, CN 2, FP 1, FN 1, accuracy 83.3% [src: thermodynamic_impact]
- E. coli, Marvin: CP 0, CN 3, FP 0, FN 9, accuracy 25.0% [src: thermodynamic_impact]
- E. coli, OPAM2: CP 0, CN 3, FP 0, FN 9, accuracy 25.0% [src: thermodynamic_impact]
- B. subtilis, Unconstrained: CP 7, CN 2, FP 1, FN 2, accuracy 75.0% [src: thermodynamic_impact]
- B. subtilis, Marvin: CP 0, CN 3, FP 0, FN 9, accuracy 25.0% [src: thermodynamic_impact]
- B. subtilis, OPAM2: CP 0, CN 3, FP 0, FN 9, accuracy 25.0% [src: thermodynamic_impact]

## Caveats

- The diverse-organism analysis used LP-relaxed TMFA (no integer variables) for tractability. Full MILP TMFA may reveal additional direction-locking effects, though the E. coli analysis suggests these are minor. [src: thermodynamic_impact]
- TMFA used default concentration bounds of 1 µM – 10 mM. Organism-specific metabolomics could shift some reactions across the feasibility boundary. [src: thermodynamic_impact]
- GLPK may find different optima than commercial solvers (Gurobi, CPLEX) in degenerate solution spaces. [src: thermodynamic_impact]
- The 12-carbon-source panel captures a limited phenotypic space. [src: thermodynamic_impact]

## Open Directions

- Run full MILP TMFA on the 10 diverse organisms. This would test whether the LP relaxation hides direction-locking effects.
- Replace the default 1 µM – 10 mM bounds with organism-specific metabolomics. This would show which reactions cross the feasibility boundary.
- Re-solve the TMFA models with a commercial solver. This would check whether degenerate optima change the result.
- Rerun the carbon-source panel under TMFA with more than 12 conditions. This would resolve why TMFA is reported to block alternative carbon sources despite preserved growth.
