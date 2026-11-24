---
type: "Finding"
description: "In the simple bacterial PGLS model for Levins' B_std against z-scored metal types, n = 606, \u03bb_PGLS = 0.708, \u03b2 = +0.021, SE = 0.0056, p = 1.5\u00d710\u207b\u2074, and \u0394AIC = \u221212.4, meeting Bonferroni significance."
finding_id: "microbeatlas_metal_ecology--a04cfc3a"
result: "observation"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "+0.021", "what": "PGLS coefficient of metal types on Levins' B_std", "unit": "", "denominator": "", "scope": "bacterial genera"}, {"value": "1.5\u00d710\u207b\u2074", "what": "p-value", "unit": "", "denominator": "", "scope": "simple bacterial PGLS"}, {"value": "606", "what": "genera in PGLS", "unit": "genera", "denominator": "", "scope": "bacteria"}, {"value": "\u221212.4", "what": "\u0394AIC", "unit": "", "denominator": "", "scope": "simple bacterial PGLS"}]
caveat: "The PGLS coefficient is a partial correlation after phylogenetic correction, not a causal estimate."
first_added: "2026-11-24"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Metal type diversity predicts bacterial niche breadth beyond phylogeny

In the simple bacterial PGLS model for Levins' B_std against z-scored metal types, n = 606, λ_PGLS = 0.708, β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴, and ΔAIC = −12.4, meeting Bonferroni significance. [src: microbeatlas_metal_ecology]

## Key figures

- **+0.021**: PGLS coefficient of metal types on Levins' B_std (scope bacterial genera) [src: microbeatlas_metal_ecology]
- **1.5×10⁻⁴**: p-value (scope simple bacterial PGLS) [src: microbeatlas_metal_ecology]
- **606 genera**: genera in PGLS (scope bacteria) [src: microbeatlas_metal_ecology]
- **−12.4**: ΔAIC (scope simple bacterial PGLS) [src: microbeatlas_metal_ecology]

## Evidence

> | Levins' B_std | Metal types | 606 | 0.708 | +0.021 | 0.0056 | 1.5×10⁻⁴ | −12.4 | **yes** | [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

The PGLS coefficient is a partial correlation after phylogenetic correction, not a causal estimate. [src: microbeatlas_metal_ecology]

> The PGLS coefficient is a *partial correlation* after phylogenetic correction, not a causal estimate. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The report says its five robustness analyses only partially address its main caveats. [src: microbeatlas_metal_ecology]
- The archaeal PGLS had 11% power at α = 0.05, so the report cautions that its non-significant result is not evidence against an association in archaea. [src: microbeatlas_metal_ecology]
- The report attributes the strict prevalence result's loss of significance primarily to a 37% sample-size drop (606 → 379), with β changing from +0.0215 to +0.0166, a 23% reduction. [src: microbeatlas_metal_ecology]
- The report states that the conservative 5% prevalence threshold excludes 89% of OTUs, many genuinely distributed across environments but uncommon within any one environment. [src: microbeatlas_metal_ecology]
- The report proposes a 1–2% prevalence threshold as a reasonable middle ground for future niche-breadth analyses. [src: microbeatlas_metal_ecology]
