---
type: "Finding"
description: "Reported GDI values were Forest 902.36 and Cropland 890.82 as highest (genomic frontier), versus Grassland 503.42 and Wetland 525.13 as relatively well-mapped."
finding_id: "soil_frontier_genomics--2ab586c6"
result: "observation"
source: "soil_frontier_genomics"
quantities: [{"value": "902.36", "what": "GDI for Forest", "unit": "", "denominator": "", "scope": "Forest biome"}, {"value": "890.82", "what": "GDI for Cropland", "unit": "", "denominator": "", "scope": "Cropland biome"}, {"value": "503.42", "what": "GDI for Grassland", "unit": "", "denominator": "", "scope": "Grassland biome"}, {"value": "525.13", "what": "GDI for Wetland", "unit": "", "denominator": "", "scope": "Wetland biome"}]
caveat: "Forest (902.36) and Cropland (890.82) differ by 1.3%, and without bootstrap CIs they are not meaningfully distinguishable and should not be ranked."
first_added: "2026-10-27"
source_hash: "f3931fe9d68922f56c7c150229f466d5cddab2ea6b166362e8b31933149f9a8d"
---
# Forest and Cropland show the highest genomic discovery index

Reported GDI values were Forest 902.36 and Cropland 890.82 as highest (genomic frontier), versus Grassland 503.42 and Wetland 525.13 as relatively well-mapped. [src: soil_frontier_genomics]

## Key figures

- **902.36**: GDI for Forest (scope Forest biome) [src: soil_frontier_genomics]
- **890.82**: GDI for Cropland (scope Cropland biome) [src: soil_frontier_genomics]
- **503.42**: GDI for Grassland (scope Grassland biome) [src: soil_frontier_genomics]
- **525.13**: GDI for Wetland (scope Wetland biome) [src: soil_frontier_genomics]

## Evidence

> - Highest GDI (genomic frontier): Forest (902.36), Cropland (890.82). - Lower GDI (relatively well-mapped): Grassland (503.42), Wetland (525.13). [src: soil_frontier_genomics]

From the report [[summaries/soil_frontier_genomics__REPORT]].

## Caveat

Forest (902.36) and Cropland (890.82) differ by 1.3%, and without bootstrap CIs they are not meaningfully distinguishable and should not be ranked. [src: soil_frontier_genomics]

> **Forest vs. Cropland GDI difference is small.** Forest (902.36) vs. Cropland (890.82) is a 1.3% difference; without bootstrap CIs these are not meaningfully distinguishable. The scientific claim should be framed as "Forest and Cropland are jointly the highest-GDI biomes" rather than implying a ranked ordering. [src: soil_frontier_genomics]

## Other caveats in this report

- The report is preliminary: clay-shield and GDI analyses are complete, but spatial validation and figures remain pending. [src: soil_frontier_genomics]
- The cause of negative cross-validation R² is unresolved: distributional shift, high-leverage test outliers, and genuine unpredictability have not been distinguished. Only the last supports a biological null result. [src: soil_frontier_genomics]
- GDI is a novel index without published precedent; it can equal 902 with zero genomes (completeness = 0, denominator = 1), and richness may dominate its combined measure of sampling gap and richness. [src: soil_frontier_genomics]
- The +0.8-unit pH gap needs a sampling-effort check: fewer alkaline-soil genomes could reflect fewer sequenced samples rather than an assembly or annotation gap. [src: soil_frontier_genomics]
- NB05 validations require re-running the 16S and completeness data; no local CSV output is available. [src: soil_frontier_genomics]
