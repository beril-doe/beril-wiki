---
type: "Finding"
description: "Metal resistance makes up 45% of AMR in aquatic species and 44% in soil species but only 6% in human gut species (\u03b7\u00b2 = 0.107, the largest effect among the mechanisms)."
finding_id: "amr_environmental_resistome--0cf37cb9"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "45%", "what": "metal resistance share of AMR in aquatic species", "unit": "%", "denominator": "", "scope": "aquatic"}, {"value": "44%", "what": "metal resistance share of AMR in soil species", "unit": "%", "denominator": "", "scope": "soil"}, {"value": "6%", "what": "metal resistance share of AMR in human gut species", "unit": "%", "denominator": "", "scope": "human gut"}, {"value": "\u03b7\u00b2 = 0.107", "what": "effect size of metal-resistance fraction across environments", "unit": "", "denominator": "", "scope": "largest reported mechanism effect"}]
caveat: "Mechanisms could not be assigned to 18.7% of AMR clusters (15,550), and excluding them from mechanism fractions could bias environmental comparisons if they are non-randomly distributed."
first_added: "2026-10-27"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Metal resistance dominates soil and aquatic AMR but is rare in gut

Metal resistance makes up 45% of AMR in aquatic species and 44% in soil species but only 6% in human gut species (η² = 0.107, the largest effect among the mechanisms). [src: amr_environmental_resistome]

## Key figures

- **45%**: metal resistance share of AMR in aquatic species (scope aquatic) [src: amr_environmental_resistome]
- **44%**: metal resistance share of AMR in soil species (scope soil) [src: amr_environmental_resistome]
- **6%**: metal resistance share of AMR in human gut species (scope human gut) [src: amr_environmental_resistome]
- **η² = 0.107**: effect size of metal-resistance fraction across environments (scope largest reported mechanism effect) [src: amr_environmental_resistome]

## Evidence

> - **Metal resistance**: 45% of AMR in aquatic, 44% in soil, but only 6% in human gut (η² = 0.107 — the largest effect) [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

Mechanisms could not be assigned to 18.7% of AMR clusters (15,550), and excluding them from mechanism fractions could bias environmental comparisons if they are non-randomly distributed. [src: amr_environmental_resistome]

> 8. **Mechanism classification completeness**: 18.7% of AMR clusters (15,550) could not be classified to a mechanism. These are excluded from H3 mechanism fractions, potentially biasing the analysis if unclassified genes are non-randomly distributed across environments. [src: amr_environmental_resistome]

## Other caveats in this report

- The report interprets core AMR as chromosomally encoded/intrinsic and accessory AMR as mobile/acquired by analogy to Jiang et al. (2024); it does not establish those mechanisms for every cluster here. [src: amr_environmental_resistome]
- The report proposes niche-specific selection and links it to amr_fitness_cost (metal 44% accessory versus efflux 13% core); the proposed ecological cause is an interpretation rather than a direct test here. [src: amr_environmental_resistome]
- 15,550 AMR clusters (18.7%) could not be assigned a mechanism from gene name or product annotation and were excluded from mechanism fractions. Tetracycline genes were divided between efflux tet(A-E,K,L) and target modification tet(M,O,Q,W). [src: amr_environmental_resistome]
- H4 is a species-level proxy, not a per-genome within-species comparison; the report says the latter would require billion-row joins. [src: amr_environmental_resistome]
- AlphaEarth analysis has limited interpretability because embedding dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
