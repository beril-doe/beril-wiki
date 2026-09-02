<!-- tension-hash: ee9b5b4acb582310 -->
# Strong metal cross-resistance signal vs weak or non-comparable environmental validation

The conflict is whether metal-associated genetic and fitness signals represent a reproducible, metal-specific cross-resistance phenomenon or instead reflect general cellular vulnerability, environmental structure, or analysis-specific definitions. The disagreement matters because strong pangenome, soil, and gene-neighborhood associations coexist with null or weak species-scale and groundwater validations, and the reported estimates do not measure the same outcomes. [[concepts/metal-cross-resistance]]

## Evidence Sides

### **Evidence for a broad and partly metal-specific signal**

The prior [[entities/metal-fitness-atlas]] validation reported Cohen's d = +1.0 from pangenome-scale analysis of 42K strains. [src: metal_cross_resistance] All tested metal pairs were positive, although no non-metal stress controls were included. [src: metal_cross_resistance] The specificity analysis supports the existence of a substantial metal-specific component, but also found 38.0% general-sick records and 7.2% metal+stress records. [src: metal_specificity] Metal-specific genes were 89.8% core, while the atlas found broad metal-important genes to be 87.4% core versus 76.9% baseline. [src: metal_cross_resistance, metal_fitness_atlas] The specificity analysis adds 84.8% pooled core for metal-specific genes and 90.2% for general sick genes. [src: metal_specificity]

Related observational studies also report positive environmental or genomic associations. MicrobeAtlas found a groundwater prevalence association of ρ = +0.112, p = 0.0019. [src: microbeatlas_metal_ecology] The conditional soil db-RDA model reported R² = 0.799 and p = 0.005 after conditioning on batch and project effects. [src: soil_metal_functional_genomics] GT2-neighborhood MAGs showed 0.045 versus 0.004 metal-resistance types and an 11× difference in metal-resistance genes. [src: t4ss_cazy_environmental_hgt]

### **Evidence against a unified or specifically causal signal**

The species-scale BacDive validation was null, with Spearman rho approximately -0.02 and p > 0.8. [src: metal_cross_resistance] MicrobeAtlas also found a null groundwater-specific fold-enrichment test (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] The soil results address residual community functional variance, whereas the BacDive and groundwater tests address environmental occurrence and isolation. [src: soil_metal_functional_genomics] The T4SS result concerns syntenic gene neighborhoods rather than fitness, isolation, or prevalence outcomes. [src: t4ss_cazy_environmental_hgt]

The soil analysis reported 2,355 discoveries among 3,915 implied tests, a 60% discovery rate, but positive correlation among co-contaminating metals may make Benjamini–Hochberg FDR correction anti-conservative and the true FDR higher than reported. [src: soil_metal_functional_genomics] Effect sizes were not systematically reported. [src: soil_metal_functional_genomics] The atlas explicitly attributes much of its signal to general cellular vulnerability, and the different core estimates use different gene classes, organism sets, and analytical definitions. [src: metal_cross_resistance, metal_fitness_atlas]

## Possible Reconciliations

- **Hypothesis — measurement:** Pangenome fitness effects may be detectable where species-scale isolation and prevalence measures are underpowered or affected by imprecise matching.
- **Hypothesis — scope:** Soil community variance, groundwater prevalence, isolation, fitness, and syntenic mobility may be distinct outcomes rather than convergent effect estimates.
- **Hypothesis — definition:** “Metal-specific,” “broad metal-important,” core, and general-sick gene classes may produce different estimates without contradiction.
- **Hypothesis — cause:** A substantial metal-specific component may coexist with general-stress responses; the absence of non-metal stress controls leaves this unresolved.

## Resolving Work

- Re-test matched strains across the atlas and BacDive with preregistered power analysis and identical metal-pair and species definitions; ask whether the BacDive null persists after improved matching.
- Add non-metal stress controls and fit hierarchical models separating metal-specific, general-stress, and metal-plus-stress effects; ask whether universal positivity is metal-specific.
- Harmonize groundwater, soil, and isolation outcomes while retaining environmental strata; ask whether associations replicate across outcome definitions without pooling incomparable estimates.
- Reanalyze soil discoveries with dependence-aware FDR or permutation methods and report effect sizes and confidence intervals; ask whether the 60% discovery rate reflects substantial biological effects.
- Reclassify genes under a shared inclusion scheme across the three-tier analysis and atlas; ask whether the 89.8%, 87.4%, 76.9%, 84.8%, and 90.2% core estimates remain distinct after harmonization.
