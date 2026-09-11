<!-- tension-hash: 75c4d8f77885aac9 -->
# Broad AMR fitness signals versus class-specific and conservation-matched nulls

The corpus contains several related tensions over how broadly AMR fitness effects, conservation patterns, and cofitness structure can be generalized. The strongest pooled signals appear when conditions are aggregated or when all genes are analyzed, while class-matched AMR comparisons and AMR-specific core/accessory comparisons are weaker or null. These disagreements matter because they determine whether observed AMR patterns reflect general biological effects, particular antibiotic classes, gene-conservation structure, or differences in measurement scope.

## Evidence Sides

**Broad pooled and all-gene analyses support strong fitness–conservation structure.**  
The any-antibiotic analysis found a **57.0%** flip rate for **N = 797** genes with **p = 0.0001**. [src: amr_fitness_cost] The all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails among core genes. [src: fitness_effects_conservation] Mechanism was strongly associated with conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**). [src: amr_fitness_cost]

**Class-matched and AMR-specific analyses provide weaker or null validation.**  
The class-matched analysis found a **54.8%** flip rate for **157** pairs with **p = 0.14**. [src: amr_fitness_cost] The class-matched analysis was less powered than the any-antibiotic analysis, so the positive pooled signal should not be treated as equally strong for every drug-resistance class. [src: amr_fitness_cost] Core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**). [src: fitness_effects_conservation] [src: amr_fitness_cost] Mechanism was not associated with baseline cost (**H = 0.65, p = 0.89**). [src: amr_fitness_cost]

**Cofitness and genomic linkage support association but not necessarily mechanism.**  
Flagellar motility, chemotaxis, and amino acid biosynthesis were enriched in AMR support neighborhoods, but the cofitness analysis identifies shared dispensability under laboratory conditions as an alternative explanation and reports no network-size relationship with cost. [src: amr_cofitness_networks] Resistance islands had mean phi **0.827** and **88%** multi-mechanism islands, indicating strong co-inheritance. [src: amr_strain_variation] However, linkage on mobile genetic elements does not prove co-selection or functional synergy. [src: amr_strain_variation]

## Possible Reconciliations

- **Hypothesis — power and matching:** The any-antibiotic and class-matched results could reflect different sample sizes and matching designs rather than opposing biological effects. [src: amr_fitness_cost]
- **Hypothesis — scope:** AMR genes may not follow the all-gene conservation gradient, making the AMR-specific null a scope-dependent exception. [src: fitness_effects_conservation] [src: amr_fitness_cost]
- **Hypothesis — distinct observables:** Cofitness enrichment and resistance-island co-inheritance may measure shared laboratory dispensability and genomic linkage, respectively, rather than the same network architecture. [src: amr_strain_variation] [src: amr_cofitness_networks]

## Resolving Work

- Analyze a larger, condition-matched AMR subset across resistance classes; compare any-antibiotic and class-matched flip rates using confidence intervals and interaction models to test whether class specificity explains the difference.
- Assemble matched core, accessory, and singleton AMR sets with comparable gene and condition coverage; test whether conservation predicts baseline cost and fitness tails within AMR genes.
- Fit models including mechanism, conservation status, antibiotic class, and their interactions; test whether mechanism affects cost directly, conservation directly, or both.
- Reanalyze cofitness neighborhoods while controlling for gene dispensability, genomic linkage, and island membership; test whether enrichment predicts cost independently of shared dispensability.
- Compare resistance-island co-inheritance with measured cofitness and antibiotic-dependent fitness across strains; test whether linkage predicts functional synergy or only physical transmission.
