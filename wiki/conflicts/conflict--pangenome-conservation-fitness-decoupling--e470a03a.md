<!-- tension-hash: e470a03a8a943d9a -->
# Does pangenome conservation track gene fitness importance, or are the two decoupled?

Two analyses disagree on whether a gene's conservation across a species' pangenome (whether it is *core*, present in nearly all genomes, or *accessory*, present in only some) relates to the fitness effect of disrupting it. A focused analysis of antimicrobial resistance (AMR) genes found no difference between core and accessory genes, while a genome-wide analysis found a weak but positive gradient in which genes that matter more for fitness are more often core [src: amr_fitness_cost, fitness_effects_conservation]. The two results may differ because of scope, so this is a scope-dependent tension. It matters because [[concepts/pangenome-conservation-fitness-decoupling]] presents decoupling as a property of the data, and that framing depends on which gene set and which fitness measure are used.

## Evidence Sides

**Decoupling: AMR genes show no core–accessory difference in baseline fitness**

For the AMR gene subset, core and accessory genes had virtually identical baseline fitness distributions. Mean fitness was −0.024 for both groups, and the comparison was not significant (p = 0.33, where p is the probability of a difference at least this large arising by chance if there were no true difference) [src: amr_fitness_cost, fitness_effects_conservation]. This null result supports decoupling for the analyzed resistance subset and for the baseline fitness measure [src: amr_fitness_cost, fitness_effects_conservation].

**Association: genome-wide, fitness importance tracks conservation**

Across the genome-wide gene set, conservation showed a positive, though weak, gradient from essential or broadly fitness-affecting genes to always-neutral genes: 82% versus 66% core [src: amr_fitness_cost, fitness_effects_conservation]. This result supports an association between conservation and fitness importance when effect breadth (how widely a gene's fitness effects occur across experiments) and conditional phenotypes (fitness effects seen only under particular conditions) are included [src: amr_fitness_cost, fitness_effects_conservation].

## Possible Reconciliations

- **Hypothesis (scope):** Both results may hold. AMR genes could be a subset in which conservation and fitness are decoupled, while the genome-wide gradient is driven mainly by essential and broadly important genes. This would require that such genes are scarce within the AMR subset, an unverified possibility that the supplied evidence does not establish.
- **Hypothesis (measure):** The AMR comparison used a single baseline fitness summary. The genome-wide analysis used effect breadth and conditional phenotypes. Any association might show up only when fitness is measured as importance across many conditions, not as a mean baseline effect.
- **Hypothesis (power and effect size):** The genome-wide gradient is described as weak. A weak association could go undetected in a much smaller gene subset, so the AMR null result may reflect limited sensitivity rather than true absence.

The supplied evidence reports no test of these hypotheses, so the tension remains open.

## Resolving Work

- **Same categories, AMR subset only:** Assign the AMR genes to the genome-wide fitness categories (essential, broadly affecting, conditional, always neutral) and compute the core fraction in each. Does the AMR subset show the same gradient once the genome-wide measure is used?
- **Same baseline measure, genome-wide:** Apply the AMR baseline-fitness comparison (core vs accessory mean fitness) to all genes. Does decoupling appear genome-wide when only baseline fitness is used?
- **Conditional phenotypes for AMR genes:** Using antibiotic and metal-stress fitness experiments, test whether AMR genes with conditional phenotypes are more often core than AMR genes that are always neutral. Do conditional phenotypes restore an association within AMR genes?
- **Power analysis:** Draw random gene subsets of AMR-subset size from the genome-wide data and estimate how often the weak gradient reaches significance. Is the AMR null result informative at this sample size?
