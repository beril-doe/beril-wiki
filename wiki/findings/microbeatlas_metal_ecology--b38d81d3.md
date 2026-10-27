---
type: "Finding"
description: "Across 1,264 bacterial genera with \u2265 3 OTUs in MicrobeAtlas, Levins' B_std shows strong phylogenetic signal (Pagel's \u03bb = 0.787) and habitat range, the number of environment categories detected, is even more conserved (\u03bb = 0.909)."
finding_id: "microbeatlas_metal_ecology--b38d81d3"
result: "observation"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "0.787", "what": "Pagel's \u03bb for Levins' B_std", "unit": "", "denominator": "", "scope": "1,264 bacterial genera with \u2265 3 OTUs"}, {"value": "0.909", "what": "Pagel's \u03bb for habitat range (number of environment categories detected)", "unit": "", "denominator": "", "scope": "1,264 bacterial genera with \u2265 3 OTUs"}]
caveat: "MicrobeAtlas detections across 13 environment categories conflate genuine habitat use with sampling intensity, primer bias, and geographic and temporal non-uniformity of sample contributions."
first_added: "2026-10-27"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Niche breadth and habitat range are strongly phylogenetically conserved in bacteria

Across 1,264 bacterial genera with ≥ 3 OTUs in MicrobeAtlas, Levins' B_std shows strong phylogenetic signal (Pagel's λ = 0.787) and habitat range, the number of environment categories detected, is even more conserved (λ = 0.909). [src: microbeatlas_metal_ecology]

## Key figures

- **0.787**: Pagel's λ for Levins' B_std (scope 1,264 bacterial genera with ≥ 3 OTUs) [src: microbeatlas_metal_ecology]
- **0.909**: Pagel's λ for habitat range (number of environment categories detected) (scope 1,264 bacterial genera with ≥ 3 OTUs) [src: microbeatlas_metal_ecology]

## Evidence

> Across 1,264 bacterial genera with ≥ 3 OTUs in MicrobeAtlas, Levins' B_std shows strong phylogenetic signal (Pagel's λ = 0.787, p = 7.9×10⁻¹⁰², LRT). Habitat range (number of environment categories detected) is even more conserved (λ = 0.909, p = 1.4×10⁻¹⁵⁷). [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

MicrobeAtlas detections across 13 environment categories conflate genuine habitat use with sampling intensity, primer bias, and geographic and temporal non-uniformity of sample contributions. [src: microbeatlas_metal_ecology]

> MicrobeAtlas OTU detection across 13 environment categories conflates genuine habitat use with sampling intensity, primer bias (V3–V4 or V4), and the geographic and temporal non-uniformity of SRA/ENA sample contributions. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The signal ordering is consistent with, but does not establish, vertical inheritance of core resistance and horizontal transfer or local exposure shaping accessory genes and metal-type expansion. [src: microbeatlas_metal_ecology]
- The PGLS subset comprises 606 bacterial genera with ≥ 3 OTUs, GTDB r214 tree membership, and metal AMR data from kbase_ke_pangenome; predictors were z-scored. [src: microbeatlas_metal_ecology]
- The core-fraction association with number of environments (β = +0.142, p = 0.038) is nominal, not Bonferroni significant. [src: microbeatlas_metal_ecology]
- PGLS jointly estimated λ by maximum likelihood; data were sorted into tree-tip order before fitting. [src: microbeatlas_metal_ecology]
- The species-with-AMR count covariate is borderline (β = +0.0093, p = 0.068). [src: microbeatlas_metal_ecology]
