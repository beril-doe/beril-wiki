---
type: "Method"
description: "Coverage-adjusted and fraction-aware OLS models with bootstrap CIs used to test contamination–defense associations."
sources: ["summaries/enigma_contamination_functional_potential__REPORT.md", "summaries/pitfalls.md"]
aliases: ["OLS"]
---
# Ordinary least squares sensitivity models

Ordinary least squares (OLS) sensitivity models are coverage-adjusted and fraction-aware regressions that the ENIGMA contamination project used to test contamination–defense associations. [src: enigma_contamination_functional_potential] The evidence comes from one project and is exploratory. [src: enigma_contamination_functional_potential] See [[summaries/enigma_contamination_functional_potential__REPORT]] and [[concepts/robustness-of-exploratory-associations-to-coverage-fraction-and-site-covariate-specification]].

## Key facts

The report finds its strongest positive exploratory defense associations in coverage-aware adjustments. [src: enigma_contamination_functional_potential]

### Model specifications

- The coverage-adjusted OLS model includes contamination, depth, latitude, longitude, and mapped_abundance_fraction. [src: enigma_contamination_functional_potential]
- The fraction-aware adjusted model includes contamination, mapped_abundance_fraction, and categorical community_fraction_type. [src: enigma_contamination_functional_potential]

### Results for defense

Only the coverage-adjusted relaxed_all_clades model has a false discovery rate (FDR) q-value below 0.05. All four models have positive betas with bootstrap confidence intervals (CIs) above zero. [src: enigma_contamination_functional_potential]

- Coverage-adjusted, relaxed_all_clades: beta = 0.000751, 95% bootstrap CI [0.000224, 0.001779], p = 0.000398, FDR q = 0.0462. [src: enigma_contamination_functional_potential]
- Coverage-adjusted, strict_single_clade: beta = 0.000640, 95% bootstrap CI [0.000169, 0.001538], p = 0.00354, FDR q = 0.130. [src: enigma_contamination_functional_potential]
- Fraction-aware, relaxed_all_clades: beta = 0.000607, 95% bootstrap CI [0.000213, 0.001221], p = 0.00144, FDR q = 0.0838. [src: enigma_contamination_functional_potential]
- Fraction-aware, strict_single_clade: beta = 0.000566, 95% bootstrap CI [0.000214, 0.001113], p = 0.00548, FDR q = 0.130. [src: enigma_contamination_functional_potential]

## Practical notes

Bootstrap CIs across many outcomes and model families can slow notebook NB03 noticeably when bootstrap counts are too high. [src: pitfalls] The report recommends moderate bootstrap sizes such as 250-400, fixed seeds, and CI estimation restricted to key coefficients or endpoints. [src: pitfalls] See also [[summaries/pitfalls]] and [[concepts/contamination-and-metal-gradients-as-drivers-of-community-functional-potential]].
