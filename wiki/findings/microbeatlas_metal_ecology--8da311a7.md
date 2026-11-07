---
type: "Finding"
description: "Track A confirms a modest groundwater-prevalence association for metal-diverse genera (\u03c1 = +0.112, p = 0.0019) but does not confirm groundwater-specific fold enrichment (\u03c1 = +0.042, p = 0.242); the report says the non-significant enrichment could reflect a general breadth effect or an underpowered 1,624-sample groundwater subset, and neither explanation is established."
finding_id: "microbeatlas_metal_ecology--8da311a7"
result: "null result"
source: "microbeatlas_metal_ecology"
quantities: [{"value": "+0.042", "what": "Spearman \u03c1 of metal-type diversity versus groundwater fold enrichment", "unit": "", "denominator": "", "scope": "p = 0.242"}, {"value": "+0.112", "what": "Spearman \u03c1 of metal-type diversity versus groundwater prevalence", "unit": "", "denominator": "", "scope": "p = 0.0019"}]
caveat: "The groundwater analysis includes only 767 genera with at least one detected groundwater OTU and non-null metal-resistance data."
first_added: "2026-10-27"
source_hash: "45fedd7ae4d79ed996ffeb2f8c38d1298866c9714db14c499b03c3e3882594ad"
---
# Metal-diverse genera more prevalent in groundwater; groundwater-specific enrichment not detected

Track A confirms a modest groundwater-prevalence association for metal-diverse genera (ρ = +0.112, p = 0.0019) but does not confirm groundwater-specific fold enrichment (ρ = +0.042, p = 0.242); the report says the non-significant enrichment could reflect a general breadth effect or an underpowered 1,624-sample groundwater subset, and neither explanation is established. [src: microbeatlas_metal_ecology]

## Key figures

- **+0.042**: Spearman ρ of metal-type diversity versus groundwater fold enrichment (scope p = 0.242) [src: microbeatlas_metal_ecology]
- **+0.112**: Spearman ρ of metal-type diversity versus groundwater prevalence (scope p = 0.0019) [src: microbeatlas_metal_ecology]

## Evidence

> **Interpretation**: The Spearman correlation (ρ = +0.112, p = 0.0019) and Mann-Whitney (p = 0.007) confirm that genera with broader metal-type resistance repertoires are significantly more prevalent in groundwater than genera with narrow resistance repertoires, at both the correlation and quartile-comparison level. The effect size is modest (0.62% → 0.81% median prevalence for bottom-Q1 vs top-Q4), consistent with the global PGLS β being a partial correlation after removing phylogenetic structure. The fold-enrichment metric (groundwater vs. non-groundwater) does not reach significance (ρ = +0.042, p = 0.242). This means the environmental-specificity metric — whether metal-diverse genera are *preferentially* enriched in groundwater beyond their global baseline — does not show a detectable signal. This is a meaningful null: Track A confirms the prevalence association but does not confirm groundwater-specific enrichment. The non-significant fold-enrichment could reflect that (a) the prevalence advantage is a general breadth effect rather than groundwater specificity, or (b) the 1,624-sample groundwater subset is underpowered to detect a specificity signal of the observed effect size. Track A is therefore consistent with the PGLS finding but does not uniquely support the metal-contamination mechanism. [src: microbeatlas_metal_ecology]

From the report [[summaries/microbeatlas_metal_ecology__REPORT]].

## Caveat

The groundwater analysis includes only 767 genera with at least one detected groundwater OTU and non-null metal-resistance data. [src: microbeatlas_metal_ecology]

> **Analysis subset**: 767 genera with (i) ≥1 OTU detected in groundwater and (ii) metal AMR data in `genus_trait_table.csv` (mean_n_metal_types non-null). [src: microbeatlas_metal_ecology]

## Other caveats in this report

- The signal ordering is consistent with, but does not establish, vertical inheritance of core resistance and horizontal transfer or local exposure shaping accessory genes and metal-type expansion. [src: microbeatlas_metal_ecology]
- The PGLS subset comprises 606 bacterial genera with ≥ 3 OTUs, GTDB r214 tree membership, and metal AMR data from kbase_ke_pangenome; predictors were z-scored. [src: microbeatlas_metal_ecology]
- The core-fraction association with number of environments (β = +0.142, p = 0.038) is nominal, not Bonferroni significant. [src: microbeatlas_metal_ecology]
- PGLS jointly estimated λ by maximum likelihood; data were sorted into tree-tip order before fitting. [src: microbeatlas_metal_ecology]
- The species-with-AMR count covariate is borderline (β = +0.0093, p = 0.068). [src: microbeatlas_metal_ecology]
