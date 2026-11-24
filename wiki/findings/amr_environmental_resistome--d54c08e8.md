---
type: "Finding"
description: "Significant within-family environment effects on AMR occur in 20 of 141 testable families (14%) after FDR correction, which the report takes to show the environment-AMR link is not simply a proxy for phylogeny."
finding_id: "amr_environmental_resistome--d54c08e8"
result: "inference"
source: "amr_environmental_resistome"
quantities: [{"value": "20 of 141", "what": "testable families with significant within-family effects", "unit": "families", "denominator": "141 testable families", "scope": ""}, {"value": "14%", "what": "share of testable families significant", "unit": "", "denominator": "", "scope": ""}]
caveat: "Despite family-level control, environment and phylogeny are deeply entangled, and some families are almost entirely clinical (e.g., many Enterobacteriaceae)."
first_added: "2026-11-24"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Environment effects on AMR persist within some bacterial families

Significant within-family environment effects on AMR occur in 20 of 141 testable families (14%) after FDR correction, which the report takes to show the environment-AMR link is not simply a proxy for phylogeny. [src: amr_environmental_resistome]

## Key figures

- **20 of 141 families**: testable families with significant within-family effects (denominator 141 testable families) [src: amr_environmental_resistome]
- **14%**: share of testable families significant [src: amr_environmental_resistome]

## Evidence

> **Family-level**: 20 of 141 testable families (14%) show significant within-family environment effects after FDR correction. [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

Despite family-level control, environment and phylogeny are deeply entangled, and some families are almost entirely clinical (e.g., many Enterobacteriaceae). [src: amr_environmental_resistome]

> Despite family-level control, environment and phylogeny are deeply entangled. Some families are almost entirely clinical (e.g., many Enterobacteriaceae). [src: amr_environmental_resistome]

## Other caveats in this report

- Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene names or product annotations. [src: amr_environmental_resistome]
- The clinical-exposure analysis is a species-level proxy, not a true per-genome within-species comparison, which the report says would require billion-row joins. [src: amr_environmental_resistome]
- The report says the continuous AlphaEarth analysis confirms discrete environment results but adds limited interpretability because its dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The report did not test nucleotide identity between soil and clinical resistance genes, although its pangenome framework could identify shared clusters. [src: amr_environmental_resistome]
- The report regards the 14% of families with significant within-family environment effects as its most convincing evidence, but most families span too few environments for testing. [src: amr_environmental_resistome]
