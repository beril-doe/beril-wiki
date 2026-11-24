---
type: "Concept"
description: "How much the choice of deltaG estimation tool (eQuilibrator, dGPredictor) and pKa source (Marvin vs OPAM2, via the Legendre transform) changes reaction free-energy estimates and sign calls; stops at downstream flux effects."
sources: ["summaries/thermodynamic_impact__REPORT.md"]
---
# Disagreement among deltaG estimation methods

The choice of deltaG estimation tool changes reaction free-energy estimates far more than the choice of pKa source does. In one project (see [[summaries/thermodynamic_impact__REPORT]]), swapping Marvin for OPAM2 pKa predictions left most reactions nearly unchanged, while eQuilibrator and dGPredictor disagreed widely on the same reactions. [src: thermodynamic_impact] The evidence comes from a single report. It measures downstream impact and does not test pKa accuracy against experiment. [src: thermodynamic_impact]

## pKa-level differences versus deltaG differences

Marvin and OPAM2 differ substantially at the pKa level. The mean |delta| is 2.17 pKa units across 82,171 ionizable atoms in 22,399 compounds. [src: thermodynamic_impact] The differences are largest for multi-protic compounds and molecules with complex electronic environments. [src: thermodynamic_impact]

The report argues the Legendre transform buffers these differences. It attributes this to summation over atoms per compound and compounds per reaction. [src: thermodynamic_impact] Only the Legendre-transform pH correction changes when pKa values change. The BayesianRidge group contribution model predicts a pKa-independent dG_model_only from molecular fingerprints. [src: thermodynamic_impact] The recomputed dG_model_only values were confirmed identical, and the ddG0_pH_correction values differ because compound pKas were updated. [src: thermodynamic_impact]

### Size of the change across recomputed reactions

The report recomputed 31,924 reactions with updated pKa predictions. [src: thermodynamic_impact] Most changed little:

- 72.9% changed by < 1 kJ/mol. [src: thermodynamic_impact]
- 17.6% changed by 1-5 kJ/mol. [src: thermodynamic_impact]
- 7.5% changed by > 5 kJ/mol. [src: thermodynamic_impact]
- 311 reactions (1.0%) changed by > 100 kJ/mol. [src: thermodynamic_impact]
- 840 reactions (2.6%) reversed sign between favorable and unfavorable. [src: thermodynamic_impact]

The tail is real, so the buffering is not uniform.

## Comparison with tool disagreement

For context, the report compared dGPredictor (using Marvin predictions) with eQuilibrator on 24,619 reactions where both tools give estimates. [src: thermodynamic_impact]

| Metric | eQuilibrator vs dGPredictor | Marvin vs OPAM2 |
|---|---|---|
| Mean absolute deltaG difference | 57.47 kJ/mol [src: thermodynamic_impact] | 13.35 kJ/mol [src: thermodynamic_impact] |
| Median absolute deltaG difference | 17.00 kJ/mol [src: thermodynamic_impact] | 0.11 kJ/mol [src: thermodynamic_impact] |
| Sign changes | 4,741 (19.3%) [src: thermodynamic_impact] | 850 (2.7%) [src: thermodynamic_impact] |
| Same sign | 68.7% [src: thermodynamic_impact] | 86.2% [src: thermodynamic_impact] |

The report states that Marvin-to-OPAM2 differences are 4.3x smaller by mean and 155x smaller by median than the tool disagreement. It also states that the sign-change rate is 7x lower. [src: thermodynamic_impact] It concludes that estimation method, not pKa source, dominates thermodynamic uncertainty. [src: thermodynamic_impact] It also concludes that OPAM2 can replace Marvin in the ModelSEED thermodynamic pipeline without meaningful impact on downstream FBA (flux balance analysis) predictions. [src: thermodynamic_impact]

The report adds a concentration argument. The physiological range of 1 µM to 20 mM gives ~25 kJ/mol of driving force per metabolite, with RT × ln(20000) = 24.5 kJ/mol at 298 K. [src: thermodynamic_impact] It argues this easily compensates for the mean pKa-driven dG change of 13.35 kJ/mol. [src: thermodynamic_impact]

## Tensions

- The report calls the downstream impact on metabolic model predictions negligible [src: thermodynamic_impact], yet 7.5% of recomputed reactions change by > 5 kJ/mol and 840 (2.6%) reverse sign. [src: thermodynamic_impact] The negligible conclusion is about downstream model predictions, not about every individual reaction.

## Open Directions

- Check whether the 840 sign-reversing and 311 extreme-change reactions cluster in multi-protic compounds. This would link the tail to the pKa divergence pattern.
- Compare the Marvin–OPAM2 and eQuilibrator–dGPredictor differences on the same reaction set. That would make the 7x ratio directly comparable.
- Validate OPAM2 and Marvin pKa values against experimental pKa measurements, which this study did not do.
- Test whether the sign-reversing reactions change flux predictions under realistic concentration bounds.
