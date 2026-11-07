---
type: "Finding"
description: "Across 9 organisms (2.25M cofit pairs vs 22.5M prevalence-matched random pairs), co-fit gene pairs show a weak positive co-occurrence signal, with mean delta phi +0.011, 7 of 9 organisms positive and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided), but aggregate delta is +0.003 and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13)."
finding_id: "cofitness_coinheritance--67c8c90f"
result: "observation"
source: "cofitness_coinheritance"
quantities: [{"value": "+0.011", "what": "mean delta phi (cofit - random) across organisms", "unit": "phi", "denominator": "", "scope": "9 organisms"}, {"value": "+0.003", "what": "aggregate delta phi", "unit": "phi", "denominator": "2.25M cofit pairs vs 22.5M random pairs", "scope": "Mann-Whitney p=1.66e-29"}, {"value": "W=9, p=0.13", "what": "Wilcoxon signed-rank test across organisms", "unit": "", "denominator": "", "scope": "9 organisms"}]
caveat: "The pairwise signal is attenuated by a prevalence ceiling: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate."
first_added: "2026-10-27"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Pairwise co-fitness shows only weak positive co-occurrence signal across organisms

Across 9 organisms (2.25M cofit pairs vs 22.5M prevalence-matched random pairs), co-fit gene pairs show a weak positive co-occurrence signal, with mean delta phi +0.011, 7 of 9 organisms positive and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided), but aggregate delta is +0.003 and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13). [src: cofitness_coinheritance]

## Key figures

- **+0.011 phi**: mean delta phi (cofit - random) across organisms (scope 9 organisms) [src: cofitness_coinheritance]
- **+0.003 phi**: aggregate delta phi (denominator 2.25M cofit pairs vs 22.5M random pairs; scope Mann-Whitney p=1.66e-29) [src: cofitness_coinheritance]
- **W=9, p=0.13**: Wilcoxon signed-rank test across organisms (scope 9 organisms) [src: cofitness_coinheritance]

## Evidence

> Across 9 organisms with co-fitness data (2.25M cofit pairs vs 22.5M prevalence-matched random pairs), co-fit gene pairs show a weak but consistent positive co-occurrence signal. The mean delta phi (cofit - random) is +0.011 across organisms, with 7 of 9 organisms showing a positive effect and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided). However, the overall effect size is small (aggregate delta = +0.003, Mann-Whitney p=1.66e-29) and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13), reflecting high inter-organism variance. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The pairwise signal is attenuated by a prevalence ceiling: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate. [src: cofitness_coinheritance]

> The pairwise signal is attenuated by a **prevalence ceiling**: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate. [src: cofitness_coinheritance]

## Other caveats in this report

- Korea's negative delta is qualified by extensive undefined phi values and a small computable subset; the report interprets it as statistical noise. [src: cofitness_coinheritance]
- Nearby genomes have higher cofit-pair phi, but missing far-distance genomes limit phylogenetic control. [src: cofitness_coinheritance]
- The report explains Korea's null module result by high module core prevalence; calling Korea the best pairwise organism conflicts with its earlier negative pairwise delta. [src: cofitness_coinheritance]
- The proposed selective importance of coordinated multi-gene regulation is the report's interpretation, not a separately measured result. [src: cofitness_coinheritance]
- The report makes a cross-project assertion about 48 accessory modules from `module_conservation`; this is an attributed interpretation rather than an independently shown result of this project's analyses. [src: cofitness_coinheritance]
