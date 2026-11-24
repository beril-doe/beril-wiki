---
type: "Finding"
description: "Soil genomic-frontier areas (GDI > 1000) have mean pH = 6.74 versus mapped areas mean pH = 5.94, a +0.8 pH unit gap that the report interprets as systematic under-sampling of alkaline soil microbiomes in public genomic databases."
finding_id: "soil_frontier_genomics--e9fe5cac"
result: "inference"
source: "soil_frontier_genomics"
quantities: [{"value": "6.74", "what": "mean pH of frontier areas", "unit": "", "denominator": "", "scope": "GDI > 1000"}, {"value": "5.94", "what": "mean pH of mapped areas", "unit": "", "denominator": "", "scope": ""}, {"value": "+0.8 pH unit", "what": "pH gap", "unit": "", "denominator": "", "scope": ""}]
caveat: "The pH discovery bias (+0.8 units) needs a reverse-causality check because alkaline soils may have fewer genomes simply because fewer samples from those pH ranges were ever sequenced."
first_added: "2026-11-24"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Genomic-frontier soils skew toward higher pH, suggesting alkaline under-sampling

Soil genomic-frontier areas (GDI > 1000) have mean pH = 6.74 versus mapped areas mean pH = 5.94, a +0.8 pH unit gap that the report interprets as systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

## Key figures

- **6.74**: mean pH of frontier areas (scope GDI > 1000) [src: soil_frontier_genomics]
- **5.94**: mean pH of mapped areas [src: soil_frontier_genomics]
- **+0.8 pH unit**: pH gap [src: soil_frontier_genomics]

## Evidence

> **pH discovery bias**: frontier areas (GDI > 1000) have mean pH = 6.74 vs. mapped areas mean pH = 5.94 — **+0.8 pH unit gap**, indicating systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

The pH discovery bias (+0.8 units) needs a reverse-causality check because alkaline soils may have fewer genomes simply because fewer samples from those pH ranges were ever sequenced. [src: soil_frontier_genomics]

> **pH discovery bias (+0.8 units) needs reverse-causality check.** Alkaline soils may have fewer genomes in databases simply because fewer samples from those pH ranges were ever sequenced (sampling effort bias), not because alkaline microbes are harder to assemble or less studied. [src: soil_frontier_genomics]

## Other caveats in this report

- The soil_frontier_genomics report is preliminary, with clay shield and GDI analyses complete across all source notebooks but NB05 spatial validation and NB06 figures pending. [src: soil_frontier_genomics]
- The report suggests that the inability to predict soil functional potential from measured stressors at this scale is likely due to spatial autocorrelation, batch effects, and unmeasured confounders. [src: soil_frontier_genomics]
- The report states that diagnosis of the negative out-of-sample R² is incomplete and that all three predictive model families predict worse than the training mean. [src: soil_frontier_genomics]
- Train/test distributional shift due to spatial autocorrelation within GroupKFold folds remains an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
- High-leverage outlier samples in test folds dominating the MSE remain an undistinguished possible cause of the negative soil-model CV R². [src: soil_frontier_genomics]
