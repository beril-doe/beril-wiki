<!-- tension-hash: 1585d18c67fe9e3f -->
# Does genomic compartment track resistance origin and cost, or only mode of maintenance?

The [[concepts/environmental-resistome]] page reads core versus accessory placement of antimicrobial-resistance (AMR) genes as a sign of intrinsic versus acquired resistance. Core genes are those shared across a species' genomes; accessory genes are present in only some of them. Fitness evidence does not separate the two groups, so the corpus does not settle whether genomic compartment reveals where resistance came from, how mobile it is, or what it costs the cell. [src: amr_pangenome_atlas, amr_fitness_cost] This matters because the concept page interprets compartment as evidence of origin. If compartment captures only how a gene is maintained, then claims about acquisition, spread or burden need their own evidence.

## Evidence Sides

**Side A: conservation status maps onto intrinsic versus acquired resistance.**
The pangenome atlas links core status to intrinsic resistance examples and accessory status to acquired resistance examples. [src: amr_pangenome_atlas, amr_fitness_cost] Under this reading, compartment works as an interpretive label for resistance origin. The TENSION text does not grade this as a demonstrated mapping. Its stated basis is examples.

**Side B: fitness does not distinguish the core/intrinsic and accessory/acquired groups.**
The fitness analysis measured the growth effect of disrupting each gene. It found identical mean fitness values of −0.024 for the core/intrinsic group and for the accessory/acquired group. [src: amr_pangenome_atlas, amr_fitness_cost] The effect size was Cohen's d = 0.002 (Cohen's d is a standardized difference between group means). The p-value was p = 0.33 (the probability, if the null hypothesis of no group difference and the test's assumptions hold, of a test statistic at least as extreme as the one observed). [src: amr_pangenome_atlas, amr_fitness_cost] This is a null result. It shows no detectable cost difference between the compartments. It does not show that the compartments are equivalent in origin or mobility.

The source concludes that genomic compartment supports a mode-of-maintenance hypothesis but does not by itself establish resistance origin, mobility, or cost. [src: amr_pangenome_atlas, amr_fitness_cost]

## Possible Reconciliations

- **Hypothesis: compartment reflects maintenance, not burden.** Core and accessory placement may record how a gene persists in a lineage, such as vertical inheritance versus patchy retention. Fitness cost may be set by factors independent of compartment. The two sides would then describe different properties and would not truly conflict.
- **Hypothesis: the intrinsic/acquired labels are proxies too coarse to carry cost signal.** If the core-to-intrinsic and accessory-to-acquired correspondence holds only for selected examples, any cost difference between true intrinsic and true acquired genes could be diluted.
- **Hypothesis: the assay cannot detect cost differences between compartments.** The fitness measurement may lack the resolution, or the conditions, to separate cost by origin. In that case the null would say little about real burden.

## Resolving Work

- **Mobility annotation, then a fitness comparison:** Annotate AMR genes for proximity to mobile genetic elements and re-test fitness by mobility class rather than by core/accessory status. Question: does mobility, unlike compartment, predict cost?
- **Origin labels independent of compartment:** Assign intrinsic and acquired labels from phylogenetic or horizontal-transfer evidence, not from conservation, and cross-tabulate them against core/accessory status. Question: how often does compartment actually match origin?
- **Condition-specific fitness:** Compare fitness of core and accessory AMR genes under antibiotic exposure versus no exposure. Question: does any compartment difference appear only under selection?
- **Stratified null check:** Repeat the core-versus-accessory fitness test within resistance-mechanism strata. Question: is the overall null hiding opposing differences within mechanisms?
