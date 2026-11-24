---
type: "Concept"
description: "How satellite-derived environmental embedding dissimilarity grows with geographic distance, and how it differs between environmental and human-associated samples; stops at community-composition distance-decay itself."
sources: ["summaries/discoveries.md", "summaries/ecotype_env_reanalysis__REPORT.md", "summaries/env_embedding_explorer__REPORT.md", "summaries/pitfalls.md"]
---
# Distance-decay of environmental embeddings with geographic distance

AlphaEarth embedding dissimilarity grows with geographic distance much more steeply for environmental genomes than for human-associated ones, and the pooled curve hides this. [src: discoveries] See [[entities/alphaearth-environmental-embeddings]] and [[entities/distance-decay]] for background.

## Literature Context

The candidate papers all concern distance-decay of community composition. The hub page stops short of that topic, so they give context and not direct tests of embedding decay. Distance-decay is widely reported across habitats. Examples include seamount sediments [PMID 37404136](https://pubmed.ncbi.nlm.nih.gov/37404136/), wastewater bioreactors within 442 km of each other [PMID 34668755](https://pubmed.ncbi.nlm.nih.gov/34668755/), metalloid-laden mining and smelting soils (r = 0.3448, p < 0.001) [PMID 34896705](https://pubmed.ncbi.nlm.nih.gov/34896705/), river sediments across China [PMID 35638840](https://pubmed.ncbi.nlm.nih.gov/35638840/), and cryoconite on glaciers across continents [PMID 41597681](https://pubmed.ncbi.nlm.nih.gov/41597681/).

The papers disagree on whether environment or space drives the pattern. In wastewater bioreactors, variation partitioning found that environmental characteristics explained more community variance than geographic distance did. The authors read this as environmental heterogeneity outweighing dispersal limitation [PMID 34668755](https://pubmed.ncbi.nlm.nih.gov/34668755/). In acid mine drainage sediments across southern China (90 samples, 18 sites), beta diversity correlated more strongly with geographic than environmental distance. The authors attribute this to dispersal limitation in structured sediment habitat [PMID 35108388](https://pubmed.ncbi.nlm.nih.gov/35108388/). Decay can also differ between groups within one habitat. In tropical and subtropical surface oceans, picoeukaryotes showed higher distance decay than prokaryotes, consistent with stronger dispersal limitation [PMID 32312331](https://pubmed.ncbi.nlm.nih.gov/32312331/). In salt marsh sulfate-reducing bacteria, 16S rRNA genes showed distance-decay while the functional dsrA gene did not [PMID 25727503](https://pubmed.ncbi.nlm.nih.gov/25727503/). In the western subtropical Pacific, significant decay appeared among rare taxa but not for all or abundant taxa over 1,100 km [PMID 35432250](https://pubmed.ncbi.nlm.nih.gov/35432250/). Rare and abundant river bacteria both showed strong decay, yet environmental selection governed the rare subcommunity (51.9%) and dispersal limitation the abundant one (62.7%) [PMID 35638840](https://pubmed.ncbi.nlm.nih.gov/35638840/). Assembly mechanisms also shift with spatial scale in seafloor sediments [PMID 34790173](https://pubmed.ncbi.nlm.nih.gov/34790173/) and cryoconite [PMID 41597681](https://pubmed.ncbi.nlm.nih.gov/41597681/). These papers report changes in mechanism with scale. They do not report a plateau in the decay curve.

The corpus's stratified result is that embedding distance rises 3.4x for environmental genomes and 2.0x for human-associated ones. It is consistent with the general finding that geographic decay is common in natural habitats. It also fits the literature's point that pooling heterogeneous groups can hide differences, as seen between picoeukaryotes and prokaryotes [PMID 32312331](https://pubmed.ncbi.nlm.nih.gov/32312331/). Those studies measured community composition. The corpus measures satellite-derived embedding dissimilarity between genome sampling sites, which none of these papers examined, so this application is novel. The papers do not test the report's explanation that hospitals and clinics share similar urban imagery.

The literature also bears on the report's reading that stronger environmental decay reflects environmental selection. The candidates show that decay alone does not identify the mechanism. Dispersal limitation can produce decay as well [PMID 35108388](https://pubmed.ncbi.nlm.nih.gov/35108388/), [PMID 37404136](https://pubmed.ncbi.nlm.nih.gov/37404136/). The decoupling of dsrA from 16S decay [PMID 25727503](https://pubmed.ncbi.nlm.nih.gov/25727503/) is consistent with the hub's tension. A strong geographic gradient in embeddings need not predict functional gene content.

## Stratified decay

Environmental genomes show a strong geographic gradient in embedding distance. Human-associated genomes show a flatter one. [src: discoveries, env_embedding_explorer]

For environmental genomes (Soil, Marine, Freshwater, Extreme, Plant), mean cosine distance is 0.27 at <100 km and 0.90 at >10,000 km, a 3.4x ratio. [src: discoveries, env_embedding_explorer] For human-associated genomes (gut, clinical, other), it rises from 0.37 nearby to 0.75 far, a 2.0x ratio. [src: discoveries, env_embedding_explorer] The cross-project pitfalls digest labels 3.4x a strong signal and 2.0x a weak one. [src: pitfalls]

The report attributes the flat human-associated gradient to hospitals and clinics worldwide sharing similar urban satellite imagery. That explanation is the report's proposal, not a separate measurement. [src: discoveries, env_embedding_explorer]

## Pooled curve

Across all 50,000 sampled genome pairs with good-quality coordinates, embedding distance rises monotonically with geographic distance. [src: env_embedding_explorer] The pooled curve has a 2.0x ratio. [src: pitfalls] It blends the two populations and is dominated by the 38% human-associated fraction. [src: discoveries, env_embedding_explorer] The report says this underestimates the true geographic signal. [src: discoveries, pitfalls]

Binned pooled means (mean cosine distance, number of pairs):

| Distance | Mean | Pairs |
|---|---|---|
| <100 km | 0.41 [src: env_embedding_explorer] | 231 [src: env_embedding_explorer] |
| 100–500 km | 0.51 [src: env_embedding_explorer] | 1,058 [src: env_embedding_explorer] |
| 500–1K km | 0.56 [src: env_embedding_explorer] | 2,016 [src: env_embedding_explorer] |
| 1K–2K km | 0.66 [src: env_embedding_explorer] | 3,779 [src: env_embedding_explorer] |
| 2K–5K km | 0.78 [src: env_embedding_explorer] | 5,824 [src: env_embedding_explorer] |
| 5K–10K km | 0.80 [src: env_embedding_explorer] | 20,935 [src: env_embedding_explorer] |
| 10K–20K km | 0.82 [src: env_embedding_explorer] | 16,107 [src: env_embedding_explorer] |

The relationship is strongest below 2,000 km and plateaus above 5,000 km. [src: env_embedding_explorer] The report reads this as embeddings capturing spatially autocorrelated local climate, vegetation and land use. [src: env_embedding_explorer] It also concludes that the signal comes mainly from natural environments rather than urban ones. [src: env_embedding_explorer]

## Interpretation and literature framing

The report treats the relationship as a form of distance-decay, the pattern in which community similarity falls with geographic distance. [src: env_embedding_explorer] It reads the stronger decay in environmental samples as consistent with environmental selection. It cites Pearman et al. (2024), who found macroalgal microbiome composition responds mainly to environmental variation rather than geographic separation. [src: env_embedding_explorer] It cites Liu et al. (2022), who found metal contamination explained more fungal community variation in mining soils (4.16%) than geographic distance (1.21%). [src: env_embedding_explorer] It also reads the weaker human-associated decay as echoing the idea that dispersal limitation produces stronger geographic patterns than selection alone. [src: env_embedding_explorer] Other cited context: Zhang et al. (2022) reported similar distance-decay but different mechanisms in rare and abundant bacterial subcommunities. [src: env_embedding_explorer] Wang et al. (2024) showed aridity shapes soil bacterial biogeography, with higher decay rates across environmental gradients. [src: env_embedding_explorer] These are literature context, not tests on this dataset.

The report says the strong correlation confirms the embeddings capture spatially varying features such as climate, land use, vegetation type and urban/rural character. [src: env_embedding_explorer] It concludes the embeddings are most informative for environmental samples and least informative for clinical isolates. [src: env_embedding_explorer]

## Practical implications

The digests recommend stratifying AlphaEarth analyses by sample type, or at minimum excluding human-associated samples. [src: discoveries, pitfalls] See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]] and [[concepts/clinical-and-human-associated-sampling-bias-in-genome-collections]].

## Tensions

- The ecotype_env_reanalysis report predicted stronger environment–gene content correlations in environmental species, because their embeddings carry more geographic signal (3.4x vs 2.0x). [src: ecotype_env_reanalysis] It proposes that this geographic differentiation may capture climate, vegetation and land-use variation that does not strongly predict bacterial gene content. [src: ecotype_env_reanalysis] A strong embedding distance-decay therefore does not by itself show ecological relevance for gene content. See [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

## Open Directions

- Fit decay curves per environment category (soil, marine, freshwater, gut, clinical) rather than two groups, to see whether the 3.4x and 2.0x ratios hide further structure. This addresses the coarse two-way split.
- Add pair counts or confidence intervals for the stratified ratios. Only the pooled bins have reported pair counts, so the stratified ratios cannot be assessed for uncertainty.
- Compare embedding decay with community-composition decay for the same sites, to test whether embeddings track what selects microbes.
- Test whether the >5,000 km plateau comes from embedding saturation or from real environmental convergence, for example by controlling for latitude or biome.
