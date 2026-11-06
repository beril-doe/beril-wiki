---
type: "Finding"
description: "After controlling for phylogenetic structure via PGLS (n = 606 genera with AMR data), the number of distinct metal types resisted per genus is the only metal AMR predictor that survives Bonferroni correction (\u03b2 = +0.021, SE = 0.0056, p = 1.5\u00d710\u207b\u2074; threshold p < 0.0083 for 6 models)."
finding_id: "microbeatlas_metal_ecology--012a4b6c"
result: "observation"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "+0.021", "what": "PGLS coefficient of metal-type count on niche breadth", "unit": "", "denominator": "", "scope": "n = 606 genera with AMR data"}, {"value": "1.5\u00d710\u207b\u2074", "what": "p-value of the metal-type predictor", "unit": "", "denominator": "", "scope": "Bonferroni threshold p < 0.0083 for 6 models"}, {"value": "0.0056", "what": "standard error of the coefficient", "unit": "", "denominator": "", "scope": ""}]
caveat: "The cross-sectional observational design cannot establish the direction of the association; time-series genomic data or longitudinal metal-enrichment experiments would be needed."
first_added: "2026-10-27"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Metal-type diversity, not AMR gene count, predicts bacterial niche breadth after phylogeny

After controlling for phylogenetic structure via PGLS (n = 606 genera with AMR data), the number of distinct metal types resisted per genus is the only metal AMR predictor that survives Bonferroni correction (β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴; threshold p < 0.0083 for 6 models). [src: microbeatlas_metal_ecology]

## Key figures

- **+0.021**: PGLS coefficient of metal-type count on niche breadth (scope n = 606 genera with AMR data) [src: microbeatlas_metal_ecology]
- **1.5×10⁻⁴**: p-value of the metal-type predictor (scope Bonferroni threshold p < 0.0083 for 6 models) [src: microbeatlas_metal_ecology]
- **0.0056**: standard error of the coefficient [src: microbeatlas_metal_ecology]

## Evidence

> After controlling for this phylogenetic structure via PGLS (n = 606 genera with AMR data), the number of distinct metal types resisted per genus is the only metal AMR predictor that survives Bonferroni correction (β = +0.021, SE = 0.0056, p = 1.5×10⁻⁴; threshold p < 0.0083 for 6 models). [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

The cross-sectional observational design cannot establish the direction of the association; time-series genomic data or longitudinal metal-enrichment experiments would be needed. [src: microbeatlas_metal_ecology]

> The cross-sectional design of this study — comparing genera at a single snapshot in evolutionary time using observational global survey data — means the direction of this association cannot be established. It is equally consistent with metal diversity *facilitating* ecological generalism (genera tolerant of more metals can exploit more environments) and with ecological generalism *enabling* metal gene acquisition (broad-niche genera encounter more HGT donors and more metal-contaminated environments). Distinguishing these scenarios would require time-series genomic data tracking metal resistance evolution alongside range shifts, or natural experiment designs such as metal enrichment of defined microbial communities with longitudinal tracking. [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The signal ordering is consistent with, but does not establish, vertical inheritance of core resistance and horizontal transfer or local exposure shaping accessory genes and metal-type expansion. [src: microbeatlas_metal_ecology]
- The PGLS subset comprises 606 bacterial genera with ≥ 3 OTUs, GTDB r214 tree membership, and metal AMR data from kbase_ke_pangenome; predictors were z-scored. [src: microbeatlas_metal_ecology]
- The core-fraction association with number of environments (β = +0.142, p = 0.038) is nominal, not Bonferroni significant. [src: microbeatlas_metal_ecology]
- PGLS jointly estimated λ by maximum likelihood; data were sorted into tree-tip order before fitting. [src: microbeatlas_metal_ecology]
- The species-with-AMR count covariate is borderline (β = +0.0093, p = 0.068). [src: microbeatlas_metal_ecology]
