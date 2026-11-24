<!-- tension-hash: daff4d3a04fed1c5 -->
# Core-Enriched Cofitness Modules Versus Accessory-Module Co-inheritance: A Tension

Cofitness modules are groups of genes whose fitness effects rise and fall together, identified by ICA (independent component analysis, a method that separates mixed signals into independent components). Most are over 90% core, meaning their genes are present across the genomes examined. [src: conservation_fitness_synthesis] Yet the strongest co-inheritance beyond a null expectation appears in a few accessory modules, while the Korea modules, which are more than 90% core with prevalence near 1.0, show none. [src: cofitness_coinheritance] The disagreement matters because it bears on whether module coherence reflects shared ancestry or selection for gene sets to stay together. See [[concepts/conservation-of-cofitness-modules-across-genomes-and-organisms]].

## Evidence Sides

**Side A: modules are mostly core, and breadth does not track core fraction**
- Modules are enriched in core genes, and most are over 90% core. [src: conservation_fitness_synthesis]
- Cross-organism families are widespread, but breadth does not track core fraction. [src: fitness_modules, conservation_fitness_synthesis]

**Side B: co-inheritance is strongest in accessory modules, with caveats**
- The strongest co-inheritance beyond the null is in the few accessory modules. Korea's modules, all more than 90% core with prevalence near 1.0, show none. [src: cofitness_coinheritance]
- The accessory-versus-core difference is only a trend (p=0.051; p is the probability of a difference at least this large under no true difference). [src: cofitness_coinheritance]
- It rests on only 11 modules. [src: cofitness_coinheritance]

The two sides need not be incompatible, since they measure different things: core fraction on one side and co-inheritance beyond the null on the other. The accessory result is a trend, not a significant difference.

## Possible Reconciliations

- **Hypothesis: prevalence limits detectability.** Genes with prevalence near 1.0 may leave little presence/absence variation to test, so the Korea null may reflect low power rather than absent coupling. This is untested.
- **Hypothesis: the accessory signal is small-sample noise.** With only 11 modules and p=0.051, the accessory excess may not hold up in a larger set. [src: cofitness_coinheritance]
- **Hypothesis: breadth and co-inheritance capture different properties.** Family breadth across organisms may reflect conserved function, while co-inheritance reflects gene-content coupling within a species, so neither need track core fraction.

## Resolving Work

- Data: more accessory modules from additional organisms. Method: rerun the co-inheritance test against prevalence-matched random gene sets. Question: does the accessory-versus-core difference reach conventional significance with more than 11 modules?
- Data: Korea's modules and other modules with prevalence near 1.0. Method: a power analysis of the co-inheritance statistic as prevalence approaches 1.0. Question: is the null informative or underpowered?
- Data: module-family breadth and core fraction across organisms. Method: a regression of breadth on core fraction, with organism as a random effect. Question: does the lack of a relationship persist after controlling for organism?
- Data: the same modules scored per organism. Method: a leave-one-organism-out comparison of co-inheritance. Question: is the accessory signal driven by one organism?
