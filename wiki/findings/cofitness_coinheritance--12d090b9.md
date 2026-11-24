---
type: "Finding"
description: "The overall effect size is small (aggregate delta = +0.003, Mann-Whitney p=1.66e-29) and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13), reflecting high inter-organism variance."
finding_id: "cofitness_coinheritance--12d090b9"
result: "null result"
source: "cofitness_coinheritance"
quantities: [{"value": "W=9", "what": "Wilcoxon signed-rank statistic", "unit": "", "denominator": "", "scope": ""}, {"value": "p=0.13", "what": "Wilcoxon p-value across organisms", "unit": "", "denominator": "", "scope": ""}, {"value": "+0.003", "what": "aggregate delta", "unit": "", "denominator": "", "scope": ""}]
caveat: "The pairwise signal is attenuated by a prevalence ceiling: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs."
first_added: "2026-11-24"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Across-organism test of co-fitness effect is not significant

The overall effect size is small (aggregate delta = +0.003, Mann-Whitney p=1.66e-29) and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13), reflecting high inter-organism variance. [src: cofitness_coinheritance]

## Key figures

- **W=9**: Wilcoxon signed-rank statistic [src: cofitness_coinheritance]
- **p=0.13**: Wilcoxon p-value across organisms [src: cofitness_coinheritance]
- **+0.003**: aggregate delta [src: cofitness_coinheritance]

## Evidence

> However, the overall effect size is small (aggregate delta = +0.003, Mann-Whitney p=1.66e-29) and the Wilcoxon signed-rank test across organisms is not significant (W=9, p=0.13), reflecting high inter-organism variance. [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The pairwise signal is attenuated by a prevalence ceiling: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs. [src: cofitness_coinheritance]

> The pairwise signal is attenuated by a **prevalence ceiling**: most FB genes map to core clusters (>95% prevalence), where phi approaches 0 for both cofit and random pairs because there is almost no variance to correlate. [src: cofitness_coinheritance]

## Other caveats in this report

- In Korea, 95.2% of cofit pairs had NaN phi because both genes had 100% prevalence across 72 genomes, producing zero-variance vectors. [src: cofitness_coinheritance]
- Only ~8,000 of 166,601 Korea pairs were computable, and the report attributes the negative delta to statistical noise rather than a biological signal. [src: cofitness_coinheritance]
- The report suggests that the negative co-fitness-strength association likely reflects a prevalence ceiling effect, because the strongest co-fitness pairs are core genes with near-universal prevalence and little co-occurrence variance. [src: cofitness_coinheritance]
- Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 were excluded from primary analysis because they had zero Fitness Browser co-fitness data despite appearing in its organism table. [src: cofitness_coinheritance]
