---
type: "Finding"
description: "Frontier areas (GDI > 1000) had mean pH 6.74 versus 5.94 in mapped areas, a +0.8 pH unit gap that the report interprets as systematic under-sampling of alkaline soil microbiomes in public genomic databases."
finding_id: "soil_frontier_genomics--25df967c"
result: "observation"
source: "soil_frontier_genomics"
quantities: [{"value": "6.74", "what": "Mean pH in frontier areas", "unit": "pH", "denominator": "", "scope": "GDI > 1000"}, {"value": "5.94", "what": "Mean pH in mapped areas", "unit": "pH", "denominator": "", "scope": "mapped areas"}, {"value": "+0.8", "what": "pH gap between frontier and mapped areas", "unit": "pH units", "denominator": "", "scope": ""}]
caveat: "The +0.8 pH unit gap needs a reverse-causality check, since fewer alkaline-soil genomes could reflect fewer sequenced samples rather than assembly or annotation gaps."
first_added: "2026-10-27"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Genomic-frontier soils are more alkaline than well-mapped soils

Frontier areas (GDI > 1000) had mean pH 6.74 versus 5.94 in mapped areas, a +0.8 pH unit gap that the report interprets as systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

## Key figures

- **6.74 pH**: Mean pH in frontier areas (scope GDI > 1000) [src: soil_frontier_genomics]
- **5.94 pH**: Mean pH in mapped areas (scope mapped areas) [src: soil_frontier_genomics]
- **+0.8 pH units**: pH gap between frontier and mapped areas [src: soil_frontier_genomics]

## Evidence

> - **pH discovery bias**: frontier areas (GDI > 1000) have mean pH = 6.74 vs. mapped areas mean pH = 5.94 — **+0.8 pH unit gap**, indicating systematic under-sampling of alkaline soil microbiomes in public genomic databases. [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

The +0.8 pH unit gap needs a reverse-causality check, since fewer alkaline-soil genomes could reflect fewer sequenced samples rather than assembly or annotation gaps. [src: soil_frontier_genomics]

> **pH discovery bias (+0.8 units) needs reverse-causality check.** Alkaline soils may have fewer genomes in databases simply because fewer samples from those pH ranges were ever sequenced (sampling effort bias), not because alkaline microbes are harder to assemble or less studied. Controlling for the number of 16S samples in each pH bin before computing GDI would distinguish true assembly/annotation gaps from sampling gaps. [src: soil_frontier_genomics]

## Other caveats in this report

- The report is preliminary: clay-shield and GDI analyses are complete, but spatial validation and figures remain pending. [src: soil_frontier_genomics]
- The cause of negative cross-validation R² is unresolved: distributional shift, high-leverage test outliers, and genuine unpredictability have not been distinguished. Only the last supports a biological null result. [src: soil_frontier_genomics]
- GDI is a novel index without published precedent; it can equal 902 with zero genomes (completeness = 0, denominator = 1), and richness may dominate its combined measure of sampling gap and richness. [src: soil_frontier_genomics]
- Forest GDI 902.36 and Cropland GDI 890.82 differ by 1.3%; without bootstrap confidence intervals, the report says they are not meaningfully distinguishable and should not be ranked. [src: soil_frontier_genomics]
- NB05 validations require re-running the 16S and completeness data; no local CSV output is available. [src: soil_frontier_genomics]
