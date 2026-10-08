<!-- tension-hash: 3139de09db601678 -->
# Do AMR genes follow the all-gene link between fitness importance and conservation?

Across all genes, essential and broadly fitness-active genes showed higher core representation [src: fitness_effects_conservation]. Within antimicrobial-resistance (AMR) genes, however, core or intrinsic and accessory or acquired genes had indistinguishable baseline fitness distributions [src: fitness_effects_conservation] [src: amr_fitness_cost]. This matters for [[concepts/antimicrobial-resistance-fitness-cost]]. If AMR genes are an exception, the all-gene gradient does not carry over to the gene class where cost and compensation are argued. If the AMR null reflects only a narrow scope or a small subset, it says little about how AMR genes are maintained.

## Evidence Sides

**Side A: conservation tracks fitness importance across all genes.** An all-gene analysis found higher core representation among essential and broadly fitness-active genes, plus stronger positive and negative fitness tails (the extremes of the fitness distribution) among core genes [src: fitness_effects_conservation]. "Essential" here means genes for which no viable mutants were recovered. "Broadly fitness-active" means genes with fitness effects across many conditions. The analysis spans all genes and is not specific to AMR genes.

**Side B: no conservation-linked fitness difference within AMR genes.** Core or intrinsic and accessory or acquired AMR genes had indistinguishable baseline fitness distributions (**d = 0.002, p = 0.33**) [src: fitness_effects_conservation] [src: amr_fitness_cost]. Here d is a standardized effect size and p is the observed p-value of the comparison. Fitness in the AMR analysis comes from RB-TnSeq (random barcode transposon sequencing), which measures competitive fitness of insertion mutants relative to the pool average [src: amr_fitness_cost]. This is a null result: it fails to detect a difference, which is not the same as demonstrating equivalence. It also concerns baseline fitness distributions, not fitness under antibiotic exposure.

## Possible Reconciliations

- **Hypothesis 1: scope mismatch.** The two results address different scopes and observables [src: fitness_effects_conservation] [src: amr_fitness_cost]. Side A asks how often genes are core within fitness categories. Side B asks how fitness differs between conservation classes within one functional class. Both could hold without contradiction.
- **Hypothesis 2: insufficient AMR subset.** The AMR comparison may lack the size, condition matching, or singleton coverage needed to detect a gradient. Singletons are genes found in only one genome. Under this hypothesis, AMR genes are not truly an exception.
- **Hypothesis 3: genuine exception.** AMR genes may be retained or lost for reasons decoupled from baseline fitness, such as conditional benefit under drug exposure. If so, they would depart from the all-gene pattern.
- **Hypothesis 4: relative-fitness readout.** RB-TnSeq fitness is relative to the pool, not an absolute selection coefficient [src: amr_fitness_cost]. Conservation-linked effects visible across all genes might therefore be diluted within a small, functionally narrow class.

## Resolving Work

- Assemble a larger, condition-matched AMR subset with comparable coverage of core, accessory, and singleton genes. Re-run the core-versus-accessory fitness comparison to test whether the null persists with more genes. This is the resolution the source text itself names.
- Apply the all-gene binning (essential, broadly fitness-active, neutral) to AMR genes only, using the same fitness tables. Ask whether the core-representation gradient appears, flattens, or reverses.
- Compare positive and negative fitness tails between core and accessory AMR genes, not only central distributions. Ask whether the stronger tails reported for core genes genome-wide also appear among core AMR genes.
- Stratify AMR fitness by antibiotic-exposure versus baseline experiments. Ask whether conservation-linked differences emerge only where AMR genes are expected to be beneficial.
- Run an equivalence test with a pre-specified effect-size bound on the AMR comparison. Ask whether the null is a demonstrated absence of difference or merely a failure to detect one.
