---
title: Broad AMR fitness signals versus class-specific and conservation-matched nulls
type: Conflict
sources:
- id: amr_fitness_cost
  resource: ../../wiki/summaries/amr_fitness_cost__REPORT.md
  title: amr fitness cost
- id: fitness_effects_conservation
  resource: ../../wiki/summaries/fitness_effects_conservation__REPORT.md
  title: fitness effects conservation
- id: amr_cofitness_networks
  resource: ../../wiki/summaries/amr_cofitness_networks__REPORT.md
  title: amr cofitness networks
- id: amr_strain_variation
  resource: ../../wiki/summaries/amr_strain_variation__REPORT.md
  title: amr strain variation
---
<!-- tension-hash: 5ab2bd116659e70f -->
# Broad AMR fitness signals versus class-specific and conservation-matched nulls

The corpus contains several related tensions over how broadly AMR fitness effects, conservation patterns, and cofitness structure can be generalized. The strongest pooled signals appear when conditions are aggregated or when all genes are analyzed, while class-matched AMR comparisons and AMR-specific core/accessory comparisons are weaker or null. These disagreements matter because they determine whether observed AMR patterns reflect general biological effects, particular antibiotic classes, gene-conservation structure, or differences in measurement scope.

## Evidence Sides

**Broad pooled and all-gene analyses support strong fitness–conservation structure.**  
The any-antibiotic analysis found a **57.0%** flip rate for **N = 797** genes with **p = 0.0001**. [^amr_fitness_cost] The all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails among core genes. [^fitness_effects_conservation] Mechanism was strongly associated with conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**). [^amr_fitness_cost]

**Class-matched and AMR-specific analyses provide weaker or null validation.**  
The class-matched analysis found a **54.8%** flip rate for **157** pairs with **p = 0.14**. [^amr_fitness_cost] The class-matched analysis was less powered than the any-antibiotic analysis, so the positive pooled signal should not be treated as equally strong for every drug-resistance class. [^amr_fitness_cost] Core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**). [^fitness_effects_conservation] [^amr_fitness_cost] Mechanism was not associated with baseline cost (**H = 0.65, p = 0.89**). [^amr_fitness_cost]

**Cofitness and genomic linkage support association but not necessarily mechanism.**  
Flagellar motility, chemotaxis, and amino acid biosynthesis were enriched in AMR support neighborhoods, but the cofitness analysis identifies shared dispensability under laboratory conditions as an alternative explanation and reports no network-size relationship with cost. [^amr_cofitness_networks] Resistance islands had mean phi **0.827** and **88%** multi-mechanism islands, indicating strong co-inheritance. [^amr_strain_variation] However, linkage on mobile genetic elements does not prove co-selection or functional synergy. [^amr_strain_variation]

## Possible Reconciliations

- **Hypothesis — power and matching:** The any-antibiotic and class-matched results could reflect different sample sizes and matching designs rather than opposing biological effects. [^amr_fitness_cost]
- **Hypothesis — scope:** AMR genes may not follow the all-gene conservation gradient, making the AMR-specific null a scope-dependent exception. [^fitness_effects_conservation] [^amr_fitness_cost]
- **Hypothesis — distinct observables:** Cofitness enrichment and resistance-island co-inheritance may measure shared laboratory dispensability and genomic linkage, respectively, rather than the same network architecture. [^amr_strain_variation] [^amr_cofitness_networks]

## Resolving Work

- Analyze a larger, condition-matched AMR subset across resistance classes; compare any-antibiotic and class-matched flip rates using confidence intervals and interaction models to test whether class specificity explains the difference.
- Assemble matched core, accessory, and singleton AMR sets with comparable gene and condition coverage; test whether conservation predicts baseline cost and fitness tails within AMR genes.
- Fit models including mechanism, conservation status, antibiotic class, and their interactions; test whether mechanism affects cost directly, conservation directly, or both.
- Reanalyze cofitness neighborhoods while controlling for gene dispensability, genomic linkage, and island membership; test whether enrichment predicts cost independently of shared dispensability.
- Compare resistance-island co-inheritance with measured cofitness and antibiotic-dependent fitness across strains; test whether linkage predicts functional synergy or only physical transmission.

[^amr_fitness_cost]: [amr fitness cost](../../wiki/summaries/amr_fitness_cost__REPORT.md)
[^fitness_effects_conservation]: [fitness effects conservation](../../wiki/summaries/fitness_effects_conservation__REPORT.md)
[^amr_cofitness_networks]: [amr cofitness networks](../../wiki/summaries/amr_cofitness_networks__REPORT.md)
[^amr_strain_variation]: [amr strain variation](../../wiki/summaries/amr_strain_variation__REPORT.md)
