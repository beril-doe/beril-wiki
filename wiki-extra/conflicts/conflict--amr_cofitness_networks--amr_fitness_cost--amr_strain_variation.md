<!-- tension-hash: 75c4d8f77885aac9 -->
# Broad AMR fitness signals versus class-specific and mechanistic explanations

The disagreement is whether broad antibiotic-condition analyses reveal a general AMR fitness pattern or whether that signal weakens under class-matched validation, and how that pattern relates to conservation, cofitness, and genomic co-inheritance. It matters because pooled effects may describe real average behavior without supporting uniform biological conclusions across resistance classes, mechanisms, or genomic contexts.

## Evidence Sides

**Broad antibiotic analyses show a strong pooled signal.**  
The any-antibiotic analysis found a **57.0%** flip rate for **N = 797** genes with **p = 0.0001**. [src: amr_fitness_cost] This supports a broad condition-dependent fitness effect in the AMR analysis. The class-matched analysis, however, found a **54.8%** flip rate for **157** pairs with **p = 0.14**. [src: amr_fitness_cost]

**Class-matched validation provides weaker evidence.**  
The class-matched analysis was less powered than the any-antibiotic analysis, so the positive pooled signal should not be treated as equally strong for every drug-resistance class. [src: amr_fitness_cost] The analyses differ in sample size and matching design; whether broad condition coverage or antibiotic-class specificity best explains the stronger result remains unresolved. [src: amr_fitness_cost]

**Mechanism predicts conservation more strongly than baseline cost.**  
Mechanism was not associated with baseline cost (**H = 0.65, p = 0.89**) but was strongly associated with conservation status (**χ² = 69.3, p = 1.4×10⁻¹³**). [src: amr_fitness_cost] This supports different roles for mechanism in fitness and pangenome distribution rather than a single mechanism-to-cost-to-retention pathway. [src: amr_fitness_cost]

**AMR conservation does not mirror the all-gene conservation gradient.**  
The all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails among core genes. [src: fitness_effects_conservation] In contrast, core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**). [src: fitness_effects_conservation] [src: amr_fitness_cost]

**Cofitness enrichment and resistance-island linkage support different interpretations.**  
Flagellar motility, chemotaxis, and amino acid biosynthesis were enriched in AMR support neighborhoods, but shared dispensability under laboratory conditions is an alternative explanation, and the cofitness analysis reports no network-size relationship with cost. [src: amr_cofitness_networks] Mean phi **0.827** and **88%** multi-mechanism islands indicate strong co-inheritance, but linkage on mobile genetic elements does not prove co-selection or functional synergy. [src: amr_strain_variation]

## Possible Reconciliations

- **Hypothesis — power and matching:** the class-matched result may be compatible with the pooled result if smaller, more specific comparisons lose power or capture fewer relevant conditions.
- **Hypothesis — scope:** AMR genes may not follow the all-gene conservation gradient because the AMR subset has different coverage of core, accessory, and singleton genes.
- **Hypothesis — distinct observables:** cofitness enrichment may reflect shared dispensability, while resistance-island linkage reflects genomic co-inheritance; neither must explain measured fitness cost.
- **Hypothesis — mechanism-specific retention:** mechanism may influence pangenome distribution through transmission or ecological processes without producing different baseline costs.

## Resolving Work

- Reanalyze the any-antibiotic and class-matched data with identical condition coverage and explicitly matched resistance classes; test whether flip rates remain different after design effects are controlled.
- Assemble a larger, condition-matched AMR subset spanning core, accessory, and singleton genes; compare baseline fitness distributions and conservation while controlling for gene category.
- Partition cofitness neighborhoods by function and dispensability, then test whether enrichment predicts cost independently of shared laboratory-condition effects and network size.
- Compare resistance-island co-inheritance with measured cofitness and antibiotic-dependent fitness across strains; test whether linkage predicts co-selection or merely physical transmission.
