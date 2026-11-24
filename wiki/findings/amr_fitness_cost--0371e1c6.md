---
type: "Finding"
description: "The Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89)."
finding_id: "amr_fitness_cost--0371e1c6"
result: "null result"
source: "amr_fitness_cost"
quantities: [{"value": "H = 0.65", "what": "Kruskal-Wallis statistic", "unit": "", "denominator": "", "scope": "four mechanisms"}, {"value": "p = 0.89", "what": "significance", "unit": "", "denominator": "", "scope": ""}]
caveat: "The Tier 2 product classifier does not handle fosfomycin or tellurite resistance annotations, placing ~25 genes in the unknown mechanism category."
first_added: "2026-11-24"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Resistance mechanism does not explain AMR fitness cost differences

The Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89). [src: amr_fitness_cost]

## Key figures

- **H = 0.65**: Kruskal-Wallis statistic (scope four mechanisms) [src: amr_fitness_cost]
- **p = 0.89**: significance [src: amr_fitness_cost]

## Evidence

> The Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89). [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The Tier 2 product classifier does not handle fosfomycin or tellurite resistance annotations, placing ~25 genes in the unknown mechanism category. [src: amr_fitness_cost]

> The Tier 2 product classifier does not handle fosfomycin resistance or tellurite resistance annotations, placing ~25 genes in the "unknown" mechanism category. Adding these would reclassify them to enzymatic_inactivation and metal_resistance respectively, slightly reducing the unknown group. [src: amr_fitness_cost]

## Other caveats in this report

- The report suggests that the 43% of AMR genes without an antibiotic fitness flip likely reflect narrow-spectrum resistance tested against non-matching antibiotics rather than non-functional genes. [src: amr_fitness_cost]
- The report attributes the nonsignificant class-matched antibiotic result likely to small per-class sample sizes and organism heterogeneity, with strong flips in some organisms and near-zero flips in others. [src: amr_fitness_cost]
- The RB-TnSeq organisms are lab-adapted strains with extensive evolutionary time to compensate for resistance costs. [src: amr_fitness_cost]
- Most Fitness Browser species have few genomes in GTDB (median 9, range 2–399), making the ≥95% prevalence threshold for core AMR gene designation imprecise. [src: amr_fitness_cost]
- With only 2–9 genomes, a gene present in all 9 can be labeled core yet prove accessory with greater sampling depth. [src: amr_fitness_cost]
