<!-- tension-hash: 3139de09db601678 -->
# Do AMR genes escape the conservation–fitness gradient?

Across the corpus, one analysis reports that conservation tracks fitness importance genome-wide, while a second finds no such signal within antimicrobial-resistance (AMR) genes — genes whose products reduce susceptibility to antibiotics or metals. The all-gene result says core genes (those present across essentially all genomes in a lineage, as opposed to accessory genes present in only some) are enriched among fitness-important genes; the AMR-specific result says core or intrinsic and accessory or acquired AMR genes are statistically indistinguishable in baseline fitness (**d = 0.002, p = 0.33**). [src: fitness_effects_conservation] [src: amr_fitness_cost] Whether AMR genes are a genuine exception, or whether the two analyses simply cannot see the same thing, determines how far genome-wide conservation heuristics can be pushed onto resistance gene sets. The tension originates on [[concepts/antimicrobial-resistance-fitness-cost]].

## Evidence Sides

**Conservation tracks fitness genome-wide.** The all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails among core genes. [src: fitness_effects_conservation] This is a gradient claim over the full gene complement, with conservation as the outcome and fitness category as the predictor — a direction, not a threshold.

**Within AMR genes, conservation says nothing about baseline fitness.** Core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**). [src: fitness_effects_conservation] [src: amr_fitness_cost] This is a null result on a two-group comparison inside the AMR subset, with baseline fitness as the observable and conservation class as the grouping. Cohen's *d* is a standardized mean difference; *p* here is the significance of that group comparison. The null is reported as a null and is not evidence that a small effect is absent — only that none was distinguished at this scope and coverage.

## Possible Reconciliations

- *Scope hypothesis*: the two results address different scopes and observables — a genome-wide gradient versus a within-subset contrast — so they may both hold without contradiction, the gradient being invisible once the analysis is restricted to AMR genes. [src: fitness_effects_conservation] [src: amr_fitness_cost]
- *Power hypothesis*: the AMR subset may lack the coverage of core, accessory, and singleton genes needed to detect a gradient that exists but is weak within resistance functions, making the null a limit of resolution rather than a biological exception.
- *Exception hypothesis*: AMR genes may genuinely be exempt, if resistance function is maintained by conditional benefit under exposure rather than by the broad fitness activity that drives conservation elsewhere.

## Resolving Work

- Assemble a larger, condition-matched AMR subset with comparable coverage of core, accessory, and singleton genes, and re-run the same conservation contrast: does the null survive matched coverage? [src: fitness_effects_conservation] [src: amr_fitness_cost]
- Apply the all-gene binning procedure (fitness category → core fraction) to AMR genes alone, asking whether a gradient is present but attenuated rather than absent.
- Run a power analysis on the AMR subset for the observed effect size, asking what magnitude of conservation-linked difference the subset could have detected at all.
- Compare non-AMR gene subsets matched to AMR genes on size and condition coverage, asking whether any small subset reproduces the genome-wide gradient — a negative control for the scope hypothesis.
- Stratify AMR baseline fitness by condition (with versus without antibiotic or metal exposure), asking whether conservation predicts conditional benefit even where it does not predict baseline fitness.
