<!-- tension-hash: ab525b1ae46f6c90 -->
# Continuous Phenotype Gradient or Discrete Fitness Modules?

Two analyses in the corpus give opposite pictures of how gene fitness is organized. A deletion screen in ADP1 describes a continuous gradient of phenotypes with almost no discrete modules. A cross-organism decomposition of transposon fitness data instead recovers many stable, coherent modules. This matters for [[concepts/fitness-module-detection-sensitivity]]. If the module structure seen in one analysis is a product of the method, perturbation type or condition count, then module calls from any single dataset cannot be read as intrinsic biological organization. The source reports say outright that the analyses are not direct contradictions and that the factor driving the difference is unresolved. [src: adp1_deletion_phenotypes, fitness_modules]

## Evidence Sides

**Side A: fitness phenotypes form a continuous gradient**

The ADP1 deletion screen used hierarchical clustering, a method that groups genes step by step according to the similarity of their profiles. It found a continuous phenotype gradient with only one discrete 24-gene module. Clustering quality was a silhouette of 0.24, where silhouette measures how well each gene fits its own cluster compared with the nearest other cluster. [src: adp1_deletion_phenotypes, discoveries, fitness_modules] The screen used single-gene deletions profiled across 8 conditions. [src: adp1_deletion_phenotypes, fitness_modules]

**Side B: fitness phenotypes resolve into many stable modules**

Robust ICA recovered 1,116 stable modules across 32 organisms. ICA (independent component analysis) separates correlated measurements into statistically independent components, and "robust" means only modules that recur reliably are kept. Of these modules, 94.2% showed elevated within-module cofitness, which is correlated fitness across experiments among genes in the same module. [src: adp1_deletion_phenotypes, discoveries, fitness_modules] This analysis used pooled transposon mutants and at least 100 experiments. [src: adp1_deletion_phenotypes, fitness_modules]

## Possible Reconciliations

- **Hypothesis 1: method.** Hierarchical clustering and robust ICA may differ in how readily they detect co-regulated gene groups, so the contrast may follow the method rather than the data.
- **Hypothesis 2: condition count.** Eight conditions may be too few to separate co-regulated groups. Many experiments may supply enough independent variation for modules to emerge.
- **Hypothesis 3: perturbation type.** Single-gene deletions and pooled transposon mutants may capture different parts of the fitness response. This could change how modular the measured phenotypes appear.
- **Hypothesis 4: organism.** ADP1's phenotype landscape may genuinely be more continuous than those of the organisms in the ICA collection.

## Resolving Work

- **Same data, both methods:** Run robust ICA on the ADP1 deletion profiles from 8 conditions, and run hierarchical clustering with silhouette scoring on transposon fitness data from the ICA organisms. Does each method's result follow the method or the data?
- **Condition subsampling:** Subsample the transposon fitness experiments down to 8 conditions and rerun robust ICA. Does module stability and the cofitness enrichment rate collapse toward a gradient as the number of conditions falls?
- **Perturbation comparison in ADP1:** If ADP1 transposon fitness data exist, decompose them alongside the deletion screen. Do pooled-mutant phenotypes yield modules where deletions do not?
- **Module concordance:** Test whether the single ADP1 24-gene module has a matching ICA module in related organisms. Does the one discrete signal recur across perturbation types?
