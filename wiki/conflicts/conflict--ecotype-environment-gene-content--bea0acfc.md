<!-- tension-hash: bea0acfc5914fb3d -->
# Compartment Signal in Plant-Marker Gene Content: Small Real Effect or Taxonomic-Sampling Artifact?

Two readings of the same plant-compartment analysis sit side by side in [[concepts/ecotype-environment-gene-content]] and do not agree on what a small multivariate effect size means. One reading takes the compartment differences in refined plant-marker profiles at face value — PERMANOVA (permutational multivariate analysis of variance, a distance-based test of whether group centroids differ) gives R² = 0.071, the share of profile variance attributed to compartment, and db-RDA (distance-based redundancy analysis, a constrained ordination computed on a distance matrix) gives R² = 0.060 [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]. The other reading holds that the effect fell to R² = 0.072 after removing genome-rich species and was attributed mainly to taxonomic sampling [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]. The question matters because every downstream claim that root, rhizosphere and phyllosphere are *functionally* differentiated rests on whether that few-percent signal indexes compartment-specific gene content or merely which lineages happened to be sequenced.

## Evidence Sides

**Side A — the compartment effect is a real, if small, functional signal.** Refined plant-marker profiles differed by compartment at PERMANOVA R² = 0.071 and at db-RDA R² = 0.060 [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]. Read this way, compartment identity is a reported feature of the marker profiles themselves, accounting for a few percent of profile variance.

**Side B — the effect is mainly taxonomic sampling.** On this reading the compartment effect fell to R² = 0.072 after removing genome-rich species, and was attributed mainly to taxonomic sampling [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]. The claim here is about provenance rather than magnitude: whatever variance compartment explains is carried by a subset of densely sequenced lineages, so the marker profile is reading genome availability, not habitat.

## Possible Reconciliations

- *Hypothesis:* the two sides address different questions — Side A reports how much variance compartment explains, Side B reports where that variance comes from — so a small effect could be simultaneously reported as present and attributed mainly to taxonomic sampling.
- *Hypothesis:* the reported drop and the headline value are not comparable quantities, since R² = 0.072 after removing genome-rich species is stated beside, not below, PERMANOVA R² = 0.071 [src: plant_microbiome_ecotypes; ecotype_env_reanalysis]; the numbers should not be averaged or reconciled until the denominators and panels behind each are pinned down.
- *Hypothesis:* the disagreement is one of attribution rather than measurement, and only a decomposition that assigns the measured variance to lineages versus compartments — not the multivariate R² on its own — would distinguish the two readings.

## Resolving Work

- Recompute PERMANOVA and db-RDA on the refined marker panel with explicit, reported denominators for each run, asking whether the pre- and post-removal R² values share a common variance basis.
- Apply phylogenetically-aware permutation (restricting label shuffles within clades) to ask whether compartment structure persists once lineage identity is held fixed.
- Rarefy (subsample each species to a common number of genomes) before ordination, asking how much of the effect tracks sequencing density.
- Test per-marker compartment associations independently of the multivariate fit, asking which functions, if any, carry signal that the community-level R² dilutes.
