---
type: "Finding"
description: "Under non-antibiotic conditions, AMR knockouts have higher relative fitness than non-AMR knockouts, with a DerSimonian-Laird random-effects meta-analysis across 25 organisms giving a pooled effect of +0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0."
finding_id: "amr_fitness_cost--4f2f8508"
result: "observation"
source: "amr_fitness_cost"
quantities: [{"value": "+0.086", "what": "pooled effect, AMR minus non-AMR knockout fitness", "unit": "fitness units", "denominator": "", "scope": "DerSimonian-Laird random-effects meta-analysis across 25 organisms, non-antibiotic conditions"}, {"value": "+0.074, +0.098", "what": "95% CI of the pooled effect", "unit": "fitness units", "denominator": "", "scope": "25 organisms"}, {"value": "14.3", "what": "z statistic of the pooled effect", "unit": "", "denominator": "", "scope": "25 organisms"}]
caveat: "The +0.086 is the difference between AMR knockout fitness (\u22120.024) and non-AMR knockout fitness (~\u22120.11) relative to the pool average, not an absolute selection coefficient."
first_added: "2026-10-27"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# AMR gene knockouts are less costly than other knockouts without antibiotics

Under non-antibiotic conditions, AMR knockouts have higher relative fitness than non-AMR knockouts, with a DerSimonian-Laird random-effects meta-analysis across 25 organisms giving a pooled effect of +0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0. [src: amr_fitness_cost]

## Key figures

- **+0.086 fitness units**: pooled effect, AMR minus non-AMR knockout fitness (scope DerSimonian-Laird random-effects meta-analysis across 25 organisms, non-antibiotic conditions) [src: amr_fitness_cost]
- **+0.074, +0.098 fitness units**: 95% CI of the pooled effect (scope 25 organisms) [src: amr_fitness_cost]
- **14.3**: z statistic of the pooled effect (scope 25 organisms) [src: amr_fitness_cost]

## Evidence

> AMR gene knockouts show systematically higher fitness than non-AMR gene knockouts under non-antibiotic conditions, confirming that resistance genes impose a metabolic burden. A DerSimonian-Laird random-effects meta-analysis across 25 organisms yields a pooled effect of **+0.086 [95% CI: +0.074, +0.098], z = 14.3, p ~ 0**. [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The +0.086 is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11) relative to the pool average, not an absolute selection coefficient. [src: amr_fitness_cost]

> RB-TnSeq measures fitness relative to the pool average. The +0.086 is the difference between AMR knockout fitness (−0.024) and non-AMR knockout fitness (~−0.11), not an absolute selection coefficient. [src: amr_fitness_cost]

## Other caveats in this report

- The report argues that low AMR putative essentiality reduces concern about strong right-censoring. [src: amr_fitness_cost]
- The report proposes antibiotic mismatch, rather than nonfunction, as an explanation for the 43% of AMR genes without a flip. [src: amr_fitness_cost]
- Small per-class samples and organism heterogeneity are proposed, not established, explanations for the class-matched null result. [src: amr_fitness_cost]
- Compensatory evolution as the explanation for uniform mechanism costs is a hypothesis, not a direct measurement. [src: amr_fitness_cost]
- An irreducible gene-maintenance cost floor is speculative. [src: amr_fitness_cost]
