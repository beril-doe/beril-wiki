---
type: "Finding"
description: "Across 9 organisms with co-fitness data, the mean delta phi (cofit - random) is +0.011, with 7 of 9 organisms showing a positive effect and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided)."
finding_id: "cofitness_coinheritance--06bfd124"
result: "observation"
source: "cofitness_coinheritance"
quantities: [{"value": "+0.011", "what": "mean delta phi (cofit - random)", "unit": "", "denominator": "", "scope": "across organisms"}, {"value": "7 of 9", "what": "organisms with positive effect", "unit": "", "denominator": "", "scope": ""}, {"value": "8 of 9", "what": "organisms significant at p<0.05", "unit": "organisms", "denominator": "", "scope": ""}]
caveat: "The effect size is small (delta=+0.003 overall, +0.011 mean across organisms), indicating that lab-measured functional coupling explains only a tiny fraction of co-inheritance patterns."
first_added: "2026-11-24"
source_hash: "c42104325d32cf92b9baff7341246a79f8b8347e87d245d42d91303d7e98b44c"
---
# Co-fit gene pairs show weak but consistent positive co-occurrence across organisms

Across 9 organisms with co-fitness data, the mean delta phi (cofit - random) is +0.011, with 7 of 9 organisms showing a positive effect and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided). [src: cofitness_coinheritance]

## Key figures

- **+0.011**: mean delta phi (cofit - random) (scope across organisms) [src: cofitness_coinheritance]
- **7 of 9**: organisms with positive effect [src: cofitness_coinheritance]
- **8 of 9 organisms**: organisms significant at p<0.05 [src: cofitness_coinheritance]

## Evidence

> The mean delta phi (cofit - random) is +0.011 across organisms, with 7 of 9 organisms showing a positive effect and 8 of 9 significant at p<0.05 (Mann-Whitney two-sided). [src: cofitness_coinheritance]

From the report [[summaries/cofitness_coinheritance__REPORT]].

## Caveat

The effect size is small (delta=+0.003 overall, +0.011 mean across organisms), indicating that lab-measured functional coupling explains only a tiny fraction of co-inheritance patterns. [src: cofitness_coinheritance]

> However, the effect size is small (delta=+0.003 overall, +0.011 mean across organisms), indicating that lab-measured functional coupling explains only a tiny fraction of co-inheritance patterns. [src: cofitness_coinheritance]

## Other caveats in this report

- In Korea, 95.2% of cofit pairs had NaN phi because both genes had 100% prevalence across 72 genomes, producing zero-variance vectors. [src: cofitness_coinheritance]
- Only ~8,000 of 166,601 Korea pairs were computable, and the report attributes the negative delta to statistical noise rather than a biological signal. [src: cofitness_coinheritance]
- The report suggests that the negative co-fitness-strength association likely reflects a prevalence ceiling effect, because the strongest co-fitness pairs are core genes with near-universal prevalence and little co-occurrence variance. [src: cofitness_coinheritance]
- Most species lacked genomes in the far stratum (>0.05 branch distance), limiting separation of functional coupling from phylogenetic signal. [src: cofitness_coinheritance]
- Ralstonia UW163 and GMI1000 were excluded from primary analysis because they had zero Fitness Browser co-fitness data despite appearing in its organism table. [src: cofitness_coinheritance]
