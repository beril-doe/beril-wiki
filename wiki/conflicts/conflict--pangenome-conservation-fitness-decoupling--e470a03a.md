<!-- tension-hash: e470a03a8a943d9a -->
# Does pangenome conservation predict fitness cost, or is it decoupled from it?

Two projects in this corpus disagree about whether a gene's conservation across genomes — whether it sits in the **core** (present in nearly all sampled genomes) or the **accessory** pool — carries information about the fitness consequence of disrupting it. The antimicrobial resistance (AMR) analysis finds no such information: core and accessory AMR genes have virtually identical baseline fitness distributions (mean fitness −0.024 for both; p = 0.33) [src: amr_fitness_cost]. The genome-wide analysis finds a positive, though weak, conservation gradient running from essential or broadly fitness-affecting genes to always-neutral genes (82% versus 66% core) [src: fitness_effects_conservation]. The disagreement matters because the decoupling claim on [[concepts/pangenome-conservation-fitness-decoupling]] is the load-bearing inference that conservation cannot be used as a proxy for cost.

## Evidence Sides

**Decoupling, within the resistance subset and the baseline measure.** Core and accessory AMR genes show virtually identical baseline fitness distributions, with mean fitness −0.024 for both groups and p = 0.33 by the applied test, i.e. no detectable difference [src: amr_fitness_cost]. This is a null result and stays null: it does not assert that the two pools are equal, only that no difference was detected in this subset for this measure. The claim is scoped to the analyzed resistance subset and to baseline (unconditional) fitness [src: amr_fitness_cost].

**Association, across the genome when effect breadth and conditional phenotypes are counted.** Genome-wide, conservation rises with fitness importance: essential or broadly fitness-affecting genes are 82% core, while always-neutral genes are 66% core — a positive but weak gradient [src: fitness_effects_conservation]. The claim is explicitly scoped to an analysis that includes effect breadth and conditional phenotypes rather than a single baseline value [src: amr_fitness_cost, fitness_effects_conservation].

## Possible Reconciliations

- *Hypothesis: the measure, not the biology, differs.* The null may hold for baseline fitness while the gradient arises only once breadth of effect and condition-specific phenotypes are counted, so the two results could describe non-overlapping quantities [src: amr_fitness_cost, fitness_effects_conservation].
- *Hypothesis: the resistance subset is unrepresentative.* AMR genes may occupy a narrow band of the genome-wide fitness spectrum, leaving too little variation for a weak gradient to register [src: amr_fitness_cost].
- *Hypothesis: the gradient is real but too weak to detect at subset scale.* A 82%-versus-66% difference across the genome-wide analysis may not be recoverable within the analyzed resistance subset [src: fitness_effects_conservation].

## Resolving Work

- Re-score the AMR gene set using the genome-wide fitness categories (breadth of effect, conditional phenotypes) rather than baseline fitness alone: does the gradient appear in AMR genes when the measure is matched?
- Restrict the genome-wide analysis to genes whose baseline fitness lies in the AMR range and re-test the core/accessory contrast: is the gradient absent under a matched baseline-only measure?
- Compute the statistical power of the core-versus-accessory AMR comparison against an effect size implied by 82% versus 66% core: was the null result capable of detecting that gradient?
- Stratify both analyses by organism to test whether the gradient and the null coexist within the same genomes or arise from different taxon sets.
