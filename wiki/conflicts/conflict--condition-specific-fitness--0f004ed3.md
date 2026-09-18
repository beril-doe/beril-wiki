<!-- tension-hash: 0f004ed3873d9d65 -->
# Pervasive Habitat Signal or Modest Environmental Structure? Raw Enrichment Versus Phylogeny- and Effect-Size-Controlled Tests

Two projects in this corpus report genome-wide associations between gene content and habitat, and each reports them twice: once from raw association testing, where the signal looks pervasive, and once after confounder control or effect-size accounting, where it shrinks to a small but detectable shift. The disagreement is not between the two projects — it is between the two readings of the same data, and it matters because downstream pages that treat habitat association as a proxy for fitness in a condition (see [[concepts/condition-specific-fitness]]) inherit whichever reading they adopt. The raw reading licenses claims about habitat-determined gene content; the controlled reading licenses only a claim of modest environmental structure.

## Evidence Sides

**Counts of significant associations read as pervasive habitat structure.** In the plant study, 94.2% of 5,671 eggNOG ortholog groups (OGs — clusters of genes inferred to descend from a common ancestral gene) were significant in raw plant-versus-non-plant tests, and the refined dual-nature classification stood at 78.7% [src: plant_microbiome_ecotypes]. The defense-system study similarly found 22 of 64 AlphaEarth dimensions (axes of a learned environmental embedding attached to genomes) significant [src: snipe_defense_system].

**Confounder control and effect sizes read as modest structure.** Applying phylum-level control — re-testing each OG while holding taxonomic lineage constant, so that shared ancestry cannot manufacture an association — left only 50 OGs enriched; compartment separation explained only 0.060 of variance by db-RDA (distance-based redundancy analysis, a constrained ordination that partitions variance onto explanatory variables); and the 78.7% refined dual-nature classification conflicted with its four-of-four neutral-control failures [src: plant_microbiome_ecotypes]. On the defense side, the largest Cohen's d (a standardized difference between group means) was 0.26, and geographic metadata existed for only 28.4% of genomes [src: snipe_defense_system]. Together these support statistically detectable but modest environmental structure rather than direct habitat or causal-fitness measurement [src: plant_microbiome_ecotypes, snipe_defense_system].

## Possible Reconciliations

- *Hypothesis:* the raw and controlled counts measure different quantities — significance under a large denominator versus effect magnitude — so both can hold without contradiction, and only the controlled figures bear on habitat causation.
- *Hypothesis:* phylogenetic autocorrelation supplies most of the raw signal, so the 50 surviving OGs are the habitat-linked remainder and the rest are lineage markers [src: plant_microbiome_ecotypes].
- *Hypothesis:* incomplete and non-random metadata coverage attenuates true effects, so the small Cohen's d values are a floor rather than an estimate [src: snipe_defense_system].
- *Hypothesis:* the neutral-control failures indicate a mis-specified null rather than a wrong dual-nature rate, leaving the rate itself untested.

## Resolving Work

- Re-run the plant-versus-non-plant OG tests with a permutation null built from lineage-matched genome pairs; does the surviving OG count move away from 50?
- Apply the same phylum-level control to the AlphaEarth dimension tests; do any of the 22 dimensions survive, and does the largest Cohen's d change?
- Construct a positive-control marker set with known habitat dependence and run it through the identical pipeline; does it pass where four of four neutral controls failed?
- Restrict the embedding analysis to the 28.4% metadata-covered genomes' nearest taxonomic neighbours to test whether coverage bias, not habitat, drives the shift.
- Cross-check a subset of the 50 phylo-controlled OGs against measured fitness under matched conditions; does habitat enrichment predict condition-specific fitness at all?
