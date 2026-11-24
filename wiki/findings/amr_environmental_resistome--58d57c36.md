---
type: "Finding"
description: "The continuous correlation of clinical fraction with % accessory AMR is borderline (rho = 0.065, p = 0.064)."
finding_id: "amr_environmental_resistome--58d57c36"
result: "null result"
source: "amr_environmental_resistome"
quantities: [{"value": "rho = 0.065", "what": "correlation of clinical fraction with % accessory AMR", "unit": "", "denominator": "", "scope": ""}, {"value": "p = 0.064", "what": "p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The within-species analysis used a species-level proxy rather than the planned per-genome Fisher's exact test, due to the computational cost of billion-row joins."
first_added: "2026-11-24"
source_hash: "48d007e13fa6f22f0af5ab50fce2658553a23932da5b203ebca2d18948d147b4"
---
# Clinical fraction does not clearly predict accessory AMR share

The continuous correlation of clinical fraction with % accessory AMR is borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome]

## Key figures

- **rho = 0.065**: correlation of clinical fraction with % accessory AMR [src: amr_environmental_resistome]
- **p = 0.064**: p-value [src: amr_environmental_resistome]

## Evidence

> The continuous correlation of clinical fraction with % accessory is borderline (rho = 0.065, p = 0.064). [src: amr_environmental_resistome]

From the report [[summaries/amr_environmental_resistome__REPORT]].

## Caveat

The within-species analysis used a species-level proxy rather than the planned per-genome Fisher's exact test, due to the computational cost of billion-row joins. [src: amr_environmental_resistome]

> The within-species analysis (NB03) uses a species-level proxy rather than the per-genome Fisher's exact test originally planned, due to the computational cost of billion-row joins. [src: amr_environmental_resistome]

## Other caveats in this report

- Mechanism fractions exclude 18.7% of AMR clusters (15,550) that could not be classified from gene names or product annotations. [src: amr_environmental_resistome]
- The clinical-exposure analysis is a species-level proxy, not a true per-genome within-species comparison, which the report says would require billion-row joins. [src: amr_environmental_resistome]
- The report says the continuous AlphaEarth analysis confirms discrete environment results but adds limited interpretability because its dimensions are opaque and genome coverage is 28%. [src: amr_environmental_resistome]
- The report did not test nucleotide identity between soil and clinical resistance genes, although its pangenome framework could identify shared clusters. [src: amr_environmental_resistome]
- In the environmental resistome analysis, environment and phylogeny remain deeply entangled despite family-level control, and some families, including many Enterobacteriaceae, are almost entirely clinical. [src: amr_environmental_resistome]
