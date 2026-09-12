<!-- tension-hash: c7715a75d1a00d01 -->
# Metal conservation versus species-scale environmental validation

The disagreement concerns whether conserved metal-related functions and positive environmental associations validate a broad metal-tolerance architecture, or whether species-scale environmental isolation provides independent support. Positive evidence comes from pangenome fitness, isolate contamination gradients, gene-level responses, and ecological occurrence, whereas the species-scale BacDive test was null. The distinction matters because conserved metal-important genes may reflect general cellular vulnerability rather than metal-specific resistance, and because strain-level environmental occupancy may not be interchangeable with species-level summaries. This tension links [[concepts/within-species-conservation-between-species-functional-divergence]], [[concepts/metal-cross-resistance]], and [[concepts/environmental-resistome]].

## Evidence Sides

**Positive conservation and ecological-association side**

BacDive found Cohen's d = +1.00 for heavy-metal contamination in n=10 isolates, and the pangenome-scale Metal Fitness Atlas found Cohen's d = +1.0 across 42K strains. [src: bacdive_metal_validation] The atlas reported an 87.4% core fraction, supporting conservation, although its broad metal-important definition (fit < -1 OR n_sick ≥ 1) captures general stress functions as well as metal-specific resistance and the simple repertoire score failed to predict fitness. [src: metal_fitness_atlas] The cross-resistance study found broadly positive gene-level responses across 28 organisms. [src: metal_cross_resistance]

MicrobeAtlas found that metal-type diversity predicted broader inferred niche breadth after phylogenetic adjustment. [src: microbeatlas_metal_ecology] Its groundwater validation found metal-type diversity correlated with groundwater prevalence (Spearman ρ = +0.112, p = 0.0019), although groundwater-specific fold-enrichment was null (ρ = +0.042, p = 0.242). [src: microbeatlas_metal_ecology] In soil, the conditional db-RDA model reported R² = 0.799 and p = 0.005 after conditioning on batch and project effects. [src: soil_metal_functional_genomics] GT2-neighborhood MAGs showed 0.045 versus 0.004 metal-resistance types and an 11× difference in metal-resistance genes. [src: t4ss_cazy_environmental_hgt]

**Species-scale null and specificity-caution side**

The cross-resistance study found no correlation between multi-metal tolerance scores and BacDive metal-environment isolation at Fitness Browser species scale (Spearman rho approximately -0.02, p > 0.8); after matching and collapsing strains, it retained 20 independent species and judged the test underpowered. [src: metal_cross_resistance] The heavy-metal estimate was imprecise: n=10 matched isolates produced an observed d=1.00 that barely exceeded the approximately d=0.93 minimum detectable effect size reported for 80% power with n=10 heavy-metal isolates versus approximately 5,000 environmental-baseline strains. [src: bacdive_metal_validation]

The BacDive bridge left 55,107 of 97,334 strains (56.6%) unmatched, primarily because GTDB species boundaries differed from LPSN/DSMZ-based naming. [src: bacdive_metal_validation] BacDive represents culturable, described strains rather than the full diversity of environmental bacteria and may under-represent metal-tolerant extremophiles. [src: bacdive_metal_validation] The three-tier analysis found metal-specific genes to be 89.8% core, while the atlas found broad metal-important genes to be 87.4% core versus 76.9% baseline. [src: metal_cross_resistance, metal_fitness_atlas] The specificity analysis found 84.8% pooled core for metal-specific genes and 90.2% for general sick genes. [src: metal_specificity] These values use different gene classes, organism sets, and analytical definitions and should not be treated as a single estimate. [src: metal_cross_resistance, metal_fitness_atlas]

## Possible Reconciliations

- **Hypothesis — scale mismatch:** pangenome- and strain-level conservation could be real while collapsing observations to independent species removes within-species variation or reduces power.
- **Hypothesis — matching and taxonomy:** incomplete BacDive matching and differing species boundaries may change which genome-size, annotation-breadth, and environmental classes enter the comparison.
- **Hypothesis — phenotype definition:** multi-metal tolerance scores, broad metal-important fitness genes, metal-specific genes, environmental isolation, groundwater prevalence, and inferred niche breadth measure related but non-identical outcomes.
- **Hypothesis — general stress versus metal-specific response:** the 38.0% general-sick records and 7.2% metal+stress records could permit broad conservation without uniquely metal-driven environmental occupancy. [src: metal_specificity]
- **Hypothesis — environmental structure:** soil functional variance, groundwater occurrence, and culturable-isolate recovery may capture different ecological processes rather than one common environmental effect.

## Resolving Work

- Reanalyze BacDive and fitness data at strain, lineage, and species levels using a harmonized taxonomy; test whether the association disappears only after collapsing strains.
- Replicate the heavy-metal comparison with additional isolates and adjust explicitly for genome size, annotated-cluster count, taxonomy, and sampling source. [src: bacdive_metal_validation]
- Compare metal-specific, general-sick, and broad metal-important gene sets against non-metal stress controls to test whether conservation predicts metal-specific tolerance.
- Fit phylogenetically independent contrasts or PGLS for environmental isolation, groundwater prevalence, and metal-tolerance phenotypes.
- Validate occurrence associations with direct exposure and fitness measurements, while auditing soil spatial structure, effect sizes, and FDR under correlated metal contaminants.
