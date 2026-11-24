---
type: "Finding"
description: "A DerSimonian-Laird random-effects meta-analysis across 25 organisms yields a pooled effect of +0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0."
finding_id: "amr_fitness_cost--6ff13010"
result: "observation"
source: "amr_fitness_cost"
quantities: [{"value": "+0.086", "what": "pooled AMR knockout fitness shift relative to non-AMR background", "unit": "fitness units", "denominator": "", "scope": "25 organisms, random-effects meta-analysis"}, {"value": "[95% CI: +0.074, +0.098]", "what": "confidence interval of pooled effect", "unit": "", "denominator": "", "scope": ""}, {"value": "z = 14.3", "what": "test statistic", "unit": "", "denominator": "", "scope": ""}]
caveat: "The +0.086 is the difference between AMR knockout fitness (\u22120.024) and non-AMR knockout fitness (~\u22120.11), not an absolute selection coefficient."
first_added: "2026-11-24"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# AMR knockouts consistently fitter than background across organisms

A DerSimonian-Laird random-effects meta-analysis across 25 organisms yields a pooled effect of +0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0. [src: amr_fitness_cost]

## Key figures

- **+0.086 fitness units**: pooled AMR knockout fitness shift relative to non-AMR background (scope 25 organisms, random-effects meta-analysis) [src: amr_fitness_cost]
- **[95% CI: +0.074, +0.098]**: confidence interval of pooled effect [src: amr_fitness_cost]
- **z = 14.3**: test statistic [src: amr_fitness_cost]

## Evidence

> A DerSimonian-Laird random-effects meta-analysis across 25 organisms yields a pooled effect of **+0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0**. [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The +0.086 is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11), not an absolute selection coefficient. [src: amr_fitness_cost]

> The +0.086 is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11), not an absolute selection coefficient. [src: amr_fitness_cost]

## Other caveats in this report

- The report suggests that the 43% of AMR genes without an antibiotic fitness flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics rather than non-functional genes. [src: amr_fitness_cost]
- The report attributes the nonsignificant class-matched antibiotic result likely to small per-class sample sizes and organism heterogeneity, with strong flips in some organisms and near-zero flips in others. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- Most Fitness Browser species have few genomes in GTDB (median 9, range 2–399), making the ≥95% prevalence threshold for core AMR gene designation imprecise. [src: amr_fitness_cost]
- With only 2–9 genomes, a gene present in all 9 can be labeled core yet prove accessory with greater sampling depth. [src: amr_fitness_cost]
