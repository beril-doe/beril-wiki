---
type: "Finding"
description: "Community-weighted mean metal-type diversity has a positive association with time point across 133 samples (Spearman \u03c1 = +0.383, p < 0.0001)."
finding_id: "microbeatlas_metal_ecology--e5de5df1"
result: "observation"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "+0.383", "what": "Spearman \u03c1 of community-weighted mean metal-type diversity versus time point", "unit": "", "denominator": "", "scope": "133 samples"}]
caveat: "Only 16.8% of reads had genus-level SILVA-to-GTDB AMR matches (~83% excluded), and robustness to variation in covered-read fraction was not formally tested."
first_added: "2026-10-27"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Community metal diversity rises with time point in groundwater amplicon samples

Community-weighted mean metal-type diversity has a positive association with time point across 133 samples (Spearman ρ = +0.383, p < 0.0001). [src: microbeatlas_metal_ecology]

## Key figures

- **+0.383**: Spearman ρ of community-weighted mean metal-type diversity versus time point (scope 133 samples) [src: microbeatlas_metal_ecology]

## Evidence

> | Spearman ρ: CWM vs. time point (R#) | ρ = +0.383 | 133 | **< 0.0001** | [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

Only 16.8% of reads had genus-level SILVA-to-GTDB AMR matches (~83% excluded), and robustness to variation in covered-read fraction was not formally tested. [src: microbeatlas_metal_ecology]

> **Coverage limitation**: The 16.8% read coverage reflects OTUs for which genus-level SILVA taxonomy could be matched to GTDB AMR annotations. The remaining ~83% of reads (from genera without taxonomy matches) are excluded from CWM. If these uncovered genera have systematically different metal resistance profiles than covered genera (e.g., if uncovered lineages are predominantly metal-sensitive), CWM would be biased upward. The between-sample variance in CWM (1.01–1.83) and the correlation with known contamination status (FW215/FW216 in plume) are consistent with a signal that reflects real biology, but robustness to coverage fraction variation has not been formally tested. A correlation between per-sample CWM and per-sample covered-read fraction is recommended as a diagnostic before this metric is used in further analyses. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The signal ordering is consistent with, but does not establish, vertical inheritance of core resistance and horizontal transfer or local exposure shaping accessory genes and metal-type expansion. [src: microbeatlas_metal_ecology]
- The PGLS subset comprises 606 bacterial genera with ≥ 3 OTUs, GTDB r214 tree membership, and metal AMR data from kbase_ke_pangenome; predictors were z-scored. [src: microbeatlas_metal_ecology]
- The core-fraction association with number of environments (β = +0.142, p = 0.038) is nominal, not Bonferroni significant. [src: microbeatlas_metal_ecology]
- PGLS jointly estimated λ by maximum likelihood; data were sorted into tree-tip order before fitting. [src: microbeatlas_metal_ecology]
- The species-with-AMR count covariate is borderline (β = +0.0093, p = 0.068). [src: microbeatlas_metal_ecology]
