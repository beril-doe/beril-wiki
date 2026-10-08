<!-- tension-hash: 0f004ed3873d9d65 -->
# Detectable Environmental Signal vs. Modest, Confounded Effect in Habitat-Association Analyses

This tension, recorded on [[concepts/condition-specific-fitness]], concerns how to read genome-to-habitat association results. Raw plant-versus-non-plant tests and the SNIPE environmental-embedding comparison both return many significant features. Effect sizes, phylogenetic controls, data coverage and negative controls are much weaker by comparison. The open question is how much weight the significant counts deserve against the modest effects. This matters because neither project measured habitat performance or fitness directly, so any link to condition-specific fitness is an inference, not a measurement.

## Evidence Sides

**Side 1: Widespread, statistically detectable association**

- 94.2% of 5,671 eggNOG ortholog groups were significant in raw plant-versus-non-plant tests [src: plant_microbiome_ecotypes]. eggNOG is an orthology database; an ortholog group is a cluster of genes inferred to share common ancestry.
- The project's refined "dual-nature" classification of plant-associated species reached 78.7% [src: plant_microbiome_ecotypes]. The tension text does not give the classification's operational definition.
- 22 of 64 AlphaEarth dimensions were significant [src: snipe_defense_system]. AlphaEarth provides environmental embedding vectors attached to genomes.

**Side 2: Signal shrinks under control, effect size and coverage scrutiny**

- Only 50 ortholog groups kept their enrichment after phylum-level control [src: plant_microbiome_ecotypes]. This control is a correction for shared ancestry at the phylum rank.
- Compartment separation explained only 0.060 of variance by db-RDA [src: plant_microbiome_ecotypes]. db-RDA (distance-based redundancy analysis) is a constrained ordination that partitions variation in a distance matrix among explanatory factors.
- The 78.7% dual-nature classification conflicted with its four-of-four neutral-control failures [src: plant_microbiome_ecotypes]. Neutral controls are tests expected to yield no signal.
- The largest Cohen's d was 0.26, and geographic metadata existed for only 28.4% of genomes [src: snipe_defense_system]. Cohen's d is a standardized mean difference.

The concept page reads the plant results [src: plant_microbiome_ecotypes] and the SNIPE results [src: snipe_defense_system] as statistically detectable but modest environmental structure, not as direct habitat or causal-fitness measurement. That reading leaves open how much of Side 1 survives the problems listed under Side 2.

## Possible Reconciliations

- *Hypothesis:* Most raw significance reflects phylogenetic composition. If so, the phylum-controlled set is the habitat-specific core, and the raw results mainly describe which lineages occupy plant habitats.
- *Hypothesis:* A real but small habitat effect is spread across many features. Large sample sizes would make it significant while each effect stays small, which would fit both sides without either being an artifact.
- *Hypothesis:* The neutral-control failures and the limited geographic coverage may indicate systematic biases in the classification and embedding pipelines. If so, part of the detected structure would be methodological rather than biological.

## Resolving Work

- **Plant ortholog groups:** Repeat the plant-versus-non-plant enrichment with finer phylogenetic control, such as genus-level or tree-based comparative models. The question is whether the 50 surviving groups stay stable or shrink further.
- **Dual-nature classification:** Diagnose the four-of-four neutral-control failures by running the refined classification on shuffled or randomly drawn marker sets. The question is whether the 78.7% rate is above what a null marker panel produces.
- **SNIPE environmental signal:** Re-test the AlphaEarth dimensions with phylogenetic correction and with reweighting for which genomes have geographic metadata. The question is whether significant dimensions remain once coverage bias is addressed.
- **Link to measured fitness:** Map the surviving plant-enriched ortholog groups onto Fitness Browser mutant-fitness data, a collection of transposon mutant fitness assays. The question is whether these genes show condition-specific fitness under plant-relevant conditions, which would turn the associations into a testable fitness claim.
