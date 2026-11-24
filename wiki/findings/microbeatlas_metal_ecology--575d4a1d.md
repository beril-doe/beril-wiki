---
type: "Finding"
description: "Archaeal PGLS yields a nonsignificant positive metal-type coefficient (\u03b2 = +0.0145, p = 0.467), with standard errors >1\u00d7 the coefficient, which the report attributes to severe underpowering rather than a true null."
finding_id: "microbeatlas_metal_ecology--575d4a1d"
result: "null result"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "+0.0145", "what": "archaeal metal types \u03b2", "unit": "", "denominator": "", "scope": "archaea"}, {"value": "0.467", "what": "p-value", "unit": "", "denominator": "", "scope": "archaea"}]
caveat: "The archaeal PGLS had 11% power at \u03b1 = 0.05, so its non-significant result should not be interpreted as evidence against the association in archaea."
first_added: "2026-11-24"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Archaeal metal-type effect is non-significant but severely underpowered

Archaeal PGLS yields a nonsignificant positive metal-type coefficient (β = +0.0145, p = 0.467), with standard errors >1× the coefficient, which the report attributes to severe underpowering rather than a true null. [src: microbeatlas_metal_ecology]

## Key figures

- **+0.0145**: archaeal metal types β (scope archaea) [src: microbeatlas_metal_ecology]
- **0.467**: p-value (scope archaea) [src: microbeatlas_metal_ecology]

## Evidence

> The archaeal PGLS (R3) was run and yielded non-significant results with the expected positive direction for metal types (β = +0.0145, p = 0.467), but the standard errors are >1× the coefficient — consistent with severe underpowering rather than a true null effect. [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

The archaeal PGLS had 11% power at α = 0.05, so its non-significant result should not be interpreted as evidence against the association in archaea. [src: microbeatlas_metal_ecology]

> This is a severely underpowered analysis (11% power at α = 0.05); the non-significant result should not be interpreted as evidence against the association in archaea. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The report says its five robustness analyses only partially address its main caveats. [src: microbeatlas_metal_ecology]
- The report attributes the strict prevalence result's loss of significance primarily to a 37% sample-size drop (606 → 379), with β changing from +0.0215 to +0.0166, a 23% reduction. [src: microbeatlas_metal_ecology]
- The report states that the conservative 5% prevalence threshold excludes 89% of OTUs, many genuinely distributed across environments but uncommon within any one environment. [src: microbeatlas_metal_ecology]
- The report proposes a 1–2% prevalence threshold as a reasonable middle ground for future niche-breadth analyses. [src: microbeatlas_metal_ecology]
- At query time, 79/606 bacterial genera (13%) lacked genome-size data in the KBase Data Lakehouse, reducing PGLS n from 606 to 527, but direction and significance agreed with full-data models. [src: microbeatlas_metal_ecology]
