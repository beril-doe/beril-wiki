<!-- tension-hash: edc61e98d8da5e88 -->
# Conservation Status Versus Baseline Fitness Cost

The disagreement concerns whether conservation patterns across the pangenome indicate a corresponding fitness burden. The evidence is not a direct statistical contradiction: conservation status and knockout fitness are different response variables. However, the contrast matters because a mechanism-associated distribution pattern cannot automatically be treated as evidence for a mechanism-associated fitness cost. The tension is summarized on [[concepts/pangenome-conservation-fitness-decoupling]].

## Evidence Sides

**AMR-specific decoupling**

The AMR analysis found that mechanism strongly predicted conservation status, but mechanism did not predict baseline fitness cost. [src: amr_fitness_cost] For the analyzed resistance subset and baseline measure, core and accessory AMR genes had virtually identical baseline fitness distributions: mean fitness −0.024 for both; p = 0.33. [src: amr_fitness_cost] This supports decoupling between AMR mechanism-associated conservation and baseline knockout fitness, rather than showing that conserved AMR genes carry a larger baseline burden. [src: amr_fitness_cost]

**Genome-wide association with fitness importance**

The genome-wide analysis found a positive, though weak, conservation gradient from essential or broadly fitness-affecting genes to always-neutral genes: 82% versus 66% core. [src: fitness_effects_conservation] The new 33-organism integration found the same directional association with a smaller effect: 86.1% core essential genes versus 81.2% core non-essential genes, with median odds ratio 1.56. [src: conservation_vs_fitness] The synthesis supports a modest genome-wide gradient but also shows that core genes can be more burdensome in the laboratory, so conservation, essentiality, and laboratory cost should not be treated as interchangeable. [src: conservation_fitness_synthesis] The module result is directionally consistent with enrichment of conserved, coordinated fitness units: 86.0% versus 81.5%. [src: module_conservation]

## Possible Reconciliations

- **Hypothesis — scope:** The AMR null may be specific to resistance genes, whereas the genome-wide gradients may arise from broader gene classes that include essential and conditionally fitness-affecting genes.
- **Hypothesis — measurement:** Mean baseline knockout fitness may average away condition-specific or environment-dependent effects captured by effect breadth and conditional phenotypes.
- **Hypothesis — definitions:** Essentiality, conservation, and fitness cost may be operationalized differently across analyses, producing different associations without a true contradiction.
- **Hypothesis — sampling and callability:** Organism composition, pangenome sampling, or ICA module-callability may alter observed conservation enrichment. The module result does not resolve the AMR-specific null because modules exclude essential genes and summarize membership rather than AMR baseline means. [src: module_conservation]

## Resolving Work

- Assemble matched AMR and non-AMR gene sets across the same organisms, measuring conservation status and knockout fitness with identical definitions; test whether the AMR-specific null persists after scope is controlled.
- Reanalyze fitness under matched laboratory conditions and condition-specific perturbations; determine whether mechanism predicts conditional fitness effects even when it does not predict baseline mean fitness.
- Fit models that include essentiality, effect breadth, mechanism, gene category, organism composition, and interaction terms; test whether the conservation–fitness association is genome-wide or restricted to particular classes.
- Compare gene-level analyses with module-level analyses after excluding or separately modeling essential genes; test whether module callability changes the apparent conservation gradient.
- Integrate additional organisms and matched pangenome sampling; estimate whether the reported gradients remain after controlling for sampling and lineage composition.
