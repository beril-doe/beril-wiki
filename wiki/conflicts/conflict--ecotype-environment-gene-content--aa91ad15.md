<!-- tension-hash: aa91ad15ec599647 -->
# Core-Dominated Beneficial Clusters vs. Elevated Mobilome Burden in Plant-Associated Genera

The plant-microbiome ecotype study reports two findings that point in different directions about plant-associated bacteria [src: plant_microbiome_ecotypes]. Beneficial plant-interaction clusters are mostly **core genome**, meaning gene clusters shared by nearly all genomes of a species [src: plant_microbiome_ecotypes]. Yet plant-associated genera carry a larger **mobilome**, the transposons, plasmids, phage and other horizontally transferable elements in a genome [src: plant_microbiome_ecotypes]. This matters for [[concepts/ecotype-environment-gene-content]] because it leaves open whether plant-interaction gene content is stably inherited or horizontally mobile. A related **prophage** (a bacteriophage genome integrated into a bacterial genome) result also splits gene modules into conserved and variable parts, but it does not directly contradict either finding [src: prophage_ecology].

## Evidence Sides

**Side 1: Beneficial plant-interaction functions are predominantly core**

Beneficial plant-interaction gene clusters were 64.6% core, compared with 45.2% for pathogenic clusters [src: plant_microbiome_ecotypes]. This measure is a core fraction of gene clusters, compared across functional cohorts [src: plant_microbiome_ecotypes]. It suggests the hypothesis that beneficial functions, once present, tend to be retained across a species.

**Side 2: Plant-associated genera carry a higher mobilome burden**

Plant-associated genera had a median mobilome burden of 3.7 mobile elements per genome, compared with 2.8 for other genera [src: plant_microbiome_ecotypes]. This comparison is made at the genus level using medians. It implies that horizontally transferable material is more abundant in plant-associated lineages.

**Related context (not directly contradictory): prophage module variability**

Prophage modules split into two groups:
- **Environmentally variable:** anti-defense modules (genes that counter host defense systems) and structural modules [src: prophage_ecology].
- **Near-universal and more core-like:** packaging, lysis and regulation modules [src: prophage_ecology].

This shows that mobile-element-derived content can itself divide into conserved and variable parts [src: prophage_ecology].

## Possible Reconciliations

- **Hypothesis (scale difference):** The two sides use different units. The core fraction is computed over gene clusters within functional cohorts, while the mobilome burden is a per-genome median compared between genera [src: plant_microbiome_ecotypes]. Both could hold if plant-associated genera carry more mobile elements while the specific beneficial clusters stay core.
- **Hypothesis (functional partitioning):** Mobile elements in plant-associated genera may mainly carry **accessory** content (genes present in only a subset of genomes), such as pathogenic clusters, rather than beneficial clusters. This would parallel the prophage split between near-universal and variable modules [src: prophage_ecology].
- **Hypothesis (acquisition then retention):** Beneficial functions may arrive through mobile elements and later become core. On this view, high mobilome burden reflects ongoing acquisition, and the core fraction reflects retention after it.

## Resolving Work

- **Location of beneficial clusters:** Using the plant study's cluster annotations together with mobile-element calls, test whether beneficial clusters sit on or next to mobile elements less often than pathogenic clusters do. This shows whether core status and mobilome burden apply to the same genes.
- **Same unit for both measures:** Recompute mobilome burden per species, within the same core/accessory framework as the core fraction, to test whether the genus-level contrast holds once both measures share one unit.
- **Habitat stratification:** Using sample metadata, split plant-associated genera into rhizosphere (soil surrounding and influenced by roots) and endosphere (inside plant tissues) groups, and compare mobilome burden within each to test whether one niche drives the elevated burden.
- **Composition of anti-defense modules:** Using the prophage module calls, test whether the environmentally variable anti-defense modules are enriched in plant-associated genera, linking the prophage pattern to the plant mobilome result.
