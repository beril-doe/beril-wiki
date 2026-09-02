<!-- tension-hash: edc61e98d8da5e88 -->
# Mechanism-Associated Conservation Versus Fitness Burden — A Decoupling or a Scope Effect?

The disagreement concerns whether a mechanism-associated conservation pattern implies a mechanism-associated fitness burden. As summarized on [[concepts/pangenome-conservation-fitness-decoupling]], the AMR-specific analysis separates these outcomes, while genome-wide and integrated analyses report a modest association between conservation and fitness importance. The tension matters because conservation, essentiality, and laboratory-measured knockout cost may reflect related but non-interchangeable biological properties.

## Evidence Sides

**AMR-specific evidence supports decoupling.** Mechanism strongly predicted conservation status, yet mechanism did not predict baseline fitness cost. [src: amr_fitness_cost] The AMR analysis found virtually identical baseline fitness distributions for core and accessory AMR genes, with mean fitness −0.024 for both; p = 0.33. [src: amr_fitness_cost] Thus, a mechanism-associated distribution pattern cannot be treated as evidence for a mechanism-associated fitness burden. [src: amr_fitness_cost]

**Genome-wide and integrated evidence supports a modest association.** The genome-wide analysis found a positive, though weak, conservation gradient from essential or broadly fitness-affecting genes to always-neutral genes: 82% versus 66% core. [src: fitness_effects_conservation] The new 33-organism integration found 86.1% core essential genes versus 81.2% core non-essential genes, with median odds ratio 1.56. [src: conservation_vs_fitness] The synthesis supports a modest genome-wide gradient but also shows that core genes can be more burdensome in the laboratory, so conservation, essentiality, and laboratory cost should not be treated as interchangeable. [src: conservation_fitness_synthesis]

**Module-level evidence is directionally consistent but not decisive.** Conserved, coordinated fitness units were enriched among modules, with 86.0% versus 81.5% core. [src: module_conservation] However, ICA modules exclude essential genes and summarize module membership rather than AMR baseline means, so this result does not resolve the AMR-specific null. [src: module_conservation]

## Possible Reconciliations

- **Hypothesis — measurement difference:** Baseline knockout fitness may capture one laboratory condition, whereas “fitness importance” can include effect breadth and conditional phenotypes. The same genes could therefore have low baseline cost but substantial context-dependent importance.
- **Hypothesis — scope difference:** AMR genes may behave differently from the genome-wide gene set because resistance mechanisms, accessory transfer, and selection histories alter the relationship between conservation and fitness.
- **Hypothesis — composition and definitions:** Organism composition, essentiality definitions, pangenome sampling, averaging procedures, and module-callability may shift the observed association without producing a true contradiction.
- **Hypothesis — distinct biological axes:** Conservation status, essentiality, mechanism, and laboratory burden may correlate only partially, so each analysis may be measuring a different axis of constraint.

## Resolving Work

- Assemble matched AMR and non-AMR gene sets across the same organisms, conditions, and knockout-fitness assay; test whether mechanism predicts baseline fitness after controlling for conservation and gene prevalence.
- Reanalyze fitness using both baseline and condition-specific phenotypes; test whether effect breadth explains the difference between the AMR null and genome-wide gradient.
- Harmonize essentiality definitions and organism sampling, then fit a hierarchical model estimating conservation–fitness associations within organisms and across organisms.
- Compare gene-level and ICA-module-level results using the same analyzable gene universe; test whether module exclusion of essential genes or module-callability changes the estimated conservation effect.
