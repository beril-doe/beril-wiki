---
type: "Finding"
description: "The fitness cost of AMR genes does not vary by resistance mechanism: the Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89)."
finding_id: "amr_fitness_cost--104baecc"
result: "null result"
source: "amr_fitness_cost"
quantities: [{"value": "0.65", "what": "Kruskal-Wallis H", "unit": "", "denominator": "", "scope": "four testable mechanisms"}, {"value": "0.89", "what": "Kruskal-Wallis p-value", "unit": "", "denominator": "", "scope": "four testable mechanisms"}]
caveat: "The Tier 2 product classifier does not handle fosfomycin or tellurite resistance annotations, placing ~25 genes in the unknown mechanism category."
first_added: "2026-10-27"
source_hash: "37cff6733111944d43de76281816b859093e2ba9f743e964e9b5a9fc5652e034"
---
# Fitness cost does not vary by resistance mechanism

The fitness cost of AMR genes does not vary by resistance mechanism: the Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89). [src: amr_fitness_cost]

## Key figures

- **0.65**: Kruskal-Wallis H (scope four testable mechanisms) [src: amr_fitness_cost]
- **0.89**: Kruskal-Wallis p-value (scope four testable mechanisms) [src: amr_fitness_cost]

## Evidence

> Contrary to H2, the fitness cost of AMR genes does not vary by resistance mechanism. The Kruskal-Wallis test across four testable mechanisms (efflux N=254, enzymatic inactivation N=304, metal resistance N=144, unknown N=74) is not significant (H = 0.65, p = 0.89). [src: amr_fitness_cost]

From the report [[summaries/amr_fitness_cost__REPORT]].

## Caveat

The Tier 2 product classifier does not handle fosfomycin or tellurite resistance annotations, placing ~25 genes in the unknown mechanism category. [src: amr_fitness_cost]

> The Tier 2 product classifier does not handle fosfomycin resistance or tellurite resistance annotations, placing ~25 genes in the "unknown" mechanism category. [src: amr_fitness_cost]

## Other caveats in this report

- The report argues that low AMR putative essentiality reduces concern about strong right-censoring. [src: amr_fitness_cost]
- The report proposes antibiotic mismatch, rather than nonfunction, as an explanation for the 43% of AMR genes without a flip. [src: amr_fitness_cost]
- Small per-class samples and organism heterogeneity are proposed, not established, explanations for the class-matched null result. [src: amr_fitness_cost]
- Compensatory evolution as the explanation for uniform mechanism costs is a hypothesis, not a direct measurement. [src: amr_fitness_cost]
- An irreducible gene-maintenance cost floor is speculative. [src: amr_fitness_cost]
