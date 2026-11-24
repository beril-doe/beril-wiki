---
type: "Finding"
description: "The report concludes that bacterial genome size is independently positively associated with niche breadth and that the metal-type effect (p = 3.6\u00d710\u207b\u2074) has independent predictive power beyond total genomic complexity, rather than being a genome-size artefact."
finding_id: "microbeatlas_metal_ecology--96a9e349"
result: "inference"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "3.6\u00d710\u207b\u2074", "what": "p-value of metal types after genome-size control", "unit": "", "denominator": "", "scope": "bacterial PGLS"}, {"value": "+0.022", "what": "metal types \u03b2 with genome size covariate", "unit": "", "denominator": "", "scope": "bacteria"}]
caveat: "At query time, 79/606 bacterial genera (13%) lacked genome-size data in the KBase Data Lakehouse, reducing PGLS n from 606 to 527, but direction and significance agreed with full-data models."
first_added: "2026-11-24"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Metal-type effect is not a genome-size artefact

The report concludes that bacterial genome size is independently positively associated with niche breadth and that the metal-type effect (p = 3.6×10⁻⁴) has independent predictive power beyond total genomic complexity, rather than being a genome-size artefact. [src: microbeatlas_metal_ecology]

## Key figures

- **3.6×10⁻⁴**: p-value of metal types after genome-size control (scope bacterial PGLS) [src: microbeatlas_metal_ecology]
- **+0.022**: metal types β with genome size covariate (scope bacteria) [src: microbeatlas_metal_ecology]

## Evidence

> **Conclusions**: (1) Genome size is independently and significantly positively associated with niche breadth, as expected (larger genomes encode more metabolic functions). (2) Metal type diversity remains significant (p = 3.6×10⁻⁴) after controlling for genome size, with only a marginal change in β (+0.022 vs +0.021 without genome size covariate). The metal type diversity effect is **not an artefact of genome size**. (3) The partial β for metal types (controlling for both genome size and phylogeny) confirms that metal resistance breadth has independent predictive power beyond total genomic complexity. [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

At query time, 79/606 bacterial genera (13%) lacked genome-size data in the KBase Data Lakehouse, reducing PGLS n from 606 to 527, but direction and significance agreed with full-data models. [src: microbeatlas_metal_ecology]

> *Note*: 79/606 genera (13%) lacked genome size data in BERDL at query time; PGLS n drops from 606 to 527. Results are consistent in direction and significance with the full-data models. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The report says its five robustness analyses only partially address its main caveats. [src: microbeatlas_metal_ecology]
- The archaeal PGLS had 11% power at α = 0.05, so the report cautions that its non-significant result is not evidence against an association in archaea. [src: microbeatlas_metal_ecology]
- The report attributes the strict prevalence result's loss of significance primarily to a 37% sample-size drop (606 → 379), with β changing from +0.0215 to +0.0166, a 23% reduction. [src: microbeatlas_metal_ecology]
- The report states that the conservative 5% prevalence threshold excludes 89% of OTUs, many genuinely distributed across environments but uncommon within any one environment. [src: microbeatlas_metal_ecology]
- The report proposes a 1–2% prevalence threshold as a reasonable middle ground for future niche-breadth analyses. [src: microbeatlas_metal_ecology]
