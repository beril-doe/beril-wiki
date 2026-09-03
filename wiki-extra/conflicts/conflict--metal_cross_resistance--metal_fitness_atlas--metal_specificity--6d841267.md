<!-- tension-hash: ee9b5b4acb582310 -->
# Species-Scale Nulls Versus Broad Environmental and Fitness Signals

The disagreement concerns whether metal cross-resistance is a reproducible, metal-specific biological relationship or an apparent association shaped by scale, environmental definition, general stress, and analytical choices. A species-scale BacDive validation was null, while pangenome, groundwater, soil, and gene-neighborhood analyses reported positive signals. These results matter because they support different interpretations of the same proposed phenomenon: shared metal fitness effects, environmental occurrence, community functional variation, or general cellular vulnerability.

## Evidence Sides

**Species-scale validation and causal caution.** The BacDive validation was null, with Spearman rho approximately -0.02 and p > 0.8, whereas the prior [[entities/metal-fitness-atlas]] validation reported Cohen's d = +1.0 from pangenome-scale analysis of 42K strains. [src: metal_cross_resistance] All tested metal pairs were positive, but no non-metal stress controls were included. [src: metal_cross_resistance] The specificity analysis found 38.0% general-sick records and 7.2% metal+stress records, despite supporting a substantial metal-specific component. [src: metal_specificity]

**Environmental and community-level positive signals.** The MicrobeAtlas groundwater prevalence association was ρ = +0.112, p = 0.0019, while its groundwater-specific fold-enrichment test was ρ = +0.042, p = 0.242. [src: microbeatlas_metal_ecology] The soil conditional db-RDA model reported R² = 0.799 and p = 0.005 after conditioning on batch and project effects. [src: soil_metal_functional_genomics] GT2-neighborhood MAGs showed 0.045 versus 0.004 metal-resistance types and an 11× difference in metal-resistance genes. [src: t4ss_cazy_environmental_hgt]

**Conflicting core-gene estimates.** The three-tier analysis found metal-specific genes to be 89.8% core, while the atlas found broad metal-important genes to be 87.4% core versus 76.9% baseline. [src: metal_cross_resistance, metal_fitness_atlas] The specificity analysis reported 84.8% pooled core for metal-specific genes and 90.2% for general sick genes. [src: metal_specificity] These estimates use different gene classes, organism sets, inclusion rules, and classification rules. [src: metal_cross_resistance, metal_fitness_atlas] [src: metal_specificity]

## Possible Reconciliations

- **Hypothesis — scale and power:** The pangenome-scale Cohen's d = +1.0 signal may not reproduce in a species-scale dataset if matching is imprecise or power is insufficient.
- **Hypothesis — outcome mismatch:** Fitness, isolation, prevalence, residual community variance, and syntenic neighborhood abundance may measure distinct biological processes rather than one common effect.
- **Hypothesis — environmental definitions:** The groundwater, soil, and BacDive datasets differ in environmental definition, taxonomic aggregation, and outcome, so their estimates should not be combined.
- **Hypothesis — general stress and confounding:** Positive metal-pair associations may partly reflect general cellular vulnerability, co-contamination, project structure, or mobility rather than metal-specific cross-resistance.

## Resolving Work

- Reanalyze matched strains across BacDive and the atlas with a preregistered power analysis and identical taxonomic and phenotype-matching rules; test whether the null and Cohen's d = +1.0 estimates persist.
- Add non-metal stress controls and fit hierarchical models separating metal-specific, general-stress, and metal+stress responses; test the causal specificity of the universal positive metal-pair result.
- Harmonize groundwater, soil, and isolation outcomes in a stratified analysis; test whether environmental definition, taxonomic aggregation, or outcome explains the differing associations.
- Replicate the soil db-RDA with spatial validation, effect sizes, and dependence-aware FDR procedures; test whether R² = 0.799 and p = 0.005 remain after project and co-contamination structure are addressed.
- Compare identically defined gene classes across the three-tier, atlas, and specificity analyses; test whether the 89.8%, 87.4%, 76.9%, 84.8%, and 90.2% core estimates converge under shared inclusion rules.
