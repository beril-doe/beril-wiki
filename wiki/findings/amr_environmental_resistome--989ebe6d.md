---
type: "Finding"
description: "Metal resistance is 45% of AMR in aquatic, 44% in soil, but only 6% in human gut, with the largest environment effect (\u03b7\u00b2 = 0.107)."
finding_id: "amr_environmental_resistome--989ebe6d"
result: "observation"
source: "amr_environmental_resistome"
quantities: [{"value": "45%", "what": "metal resistance share of aquatic AMR", "unit": "", "denominator": "", "scope": "aquatic"}, {"value": "44%", "what": "metal resistance share of soil AMR", "unit": "", "denominator": "", "scope": "soil"}, {"value": "6%", "what": "metal resistance share of human gut AMR", "unit": "", "denominator": "", "scope": "human gut"}, {"value": "\u03b7\u00b2 = 0.107", "what": "effect size", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 18.7% of AMR clusters (15,550) that could not be classified to a mechanism were excluded from mechanism fractions, potentially biasing results if they are non-randomly distributed across environments."
first_added: "2026-11-24"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Metal resistance dominates soil and aquatic AMR but not gut AMR

Metal resistance is 45% of AMR in aquatic, 44% in soil, but only 6% in human gut, with the largest environment effect (η² = 0.107). [src: amr_environmental_resistome]

## Key figures

- **45%**: metal resistance share of aquatic AMR (scope aquatic) [src: amr_environmental_resistome]
- **44%**: metal resistance share of soil AMR (scope soil) [src: amr_environmental_resistome]
- **6%**: metal resistance share of human gut AMR (scope human gut) [src: amr_environmental_resistome]
- **η² = 0.107**: effect size [src: amr_environmental_resistome]

## Evidence

> **Metal resistance**: 45% of AMR in aquatic, 44% in soil, but only 6% in human gut (η² = 0.107 — the largest effect) [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

The 18.7% of AMR clusters (15,550) that could not be classified to a mechanism were excluded from mechanism fractions, potentially biasing results if they are non-randomly distributed across environments. [src: amr_environmental_resistome]

> 18.7% of AMR clusters (15,550) could not be classified to a mechanism. These are excluded from H3 mechanism fractions, potentially biasing the analysis if unclassified genes are non-randomly distributed across environments. [src: amr_environmental_resistome]

## Other caveats in this report

- Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene names or product annotations. [src: amr_environmental_resistome]
- The clinical-exposure analysis is a species-level proxy, not a true per-genome within-species comparison, which the report says would require billion-row joins. [src: amr_environmental_resistome]
- The report says the continuous AlphaEarth analysis confirms discrete environment results but adds limited interpretability because its dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The report did not test nucleotide identity between soil and clinical resistance genes, although its pangenome framework could identify shared clusters. [src: amr_environmental_resistome]
- In the environmental resistome analysis, environment and phylogeny remain deeply entangled despite family-level control, and some families, including many Enterobacteriaceae, are almost entirely clinical. [src: amr_environmental_resistome]
