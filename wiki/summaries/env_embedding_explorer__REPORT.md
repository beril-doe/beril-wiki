---
type: "Summary"
description: "Summary of the project AlphaEarth Embeddings, Geography & Environment Explorer."
doc_type: "short"
full_text: "sources/env_embedding_explorer__REPORT.md"
---
# AlphaEarth Embeddings, Geography & Environment Explorer

This page summarises the env_embedding_explorer project, "AlphaEarth Embeddings, Geography & Environment Explorer". Embedding distance rises with geographic distance, more steeply for environmental genomes than for human-associated ones. [src: env_embedding_explorer] The report attributes its key exploratory analyses to one notebook. [src: env_embedding_explorer] It describes itself as the first systematic characterization of the AlphaEarth embedding space in the KBase Data Lakehouse. [src: env_embedding_explorer] See also [[entities/alphaearth-environmental-embeddings]].

## Key Findings

### What the embeddings are

AlphaEarth embeddings encode geographic/environmental context derived from satellite imagery at each genome's sampling location. [src: env_embedding_explorer] The 64 dimensions A00–A63 have values in [-0.544, 0.544], mean near zero (-0.008), and mean standard deviation 0.109. [src: env_embedding_explorer] They span 135 phyla and 15,046 species. [src: env_embedding_explorer] They also span the full global extent, from latitude -85 to +84 and longitude -178 to +180. [src: env_embedding_explorer] The embeddings come from the kbase_ke_pangenome.alphaearth_embeddings_all_years table, which supplies 64-dim environmental embeddings, cleaned latitude/longitude, and taxonomy. [src: env_embedding_explorer] Environment metadata comes from the kbase_ke_pangenome.ncbi_env table, in EAV format. [src: env_embedding_explorer]

### Geographic distance and embedding distance

Embedding distance increases with geographic distance, then flattens at intercontinental scales. [src: env_embedding_explorer] The report suggests the embeddings capture spatially autocorrelated local climate, vegetation and land use. [src: env_embedding_explorer] It reads the strong correlation as confirming that they capture spatially varying environmental features, likely climate, land use, vegetation type, and urban/rural character. [src: env_embedding_explorer] The curve is steeper for environmental genomes than for human-associated ones. [src: env_embedding_explorer] The report quantifies the geographic signal strength as 3.4x for environmental samples and 2.0x for human-associated samples. [src: env_embedding_explorer]

- Environmental samples (Soil, Marine, Freshwater, Extreme, Plant): mean cosine distance 0.27 at <100 km and 0.90 at >10,000 km, a 3.4x ratio. [src: env_embedding_explorer]
- Human-associated samples (gut, clinical, other): 0.37 nearby and 0.75 far, a 2.0x ratio. [src: env_embedding_explorer]
- The report attributes the flatter human curve to hospitals and clinics worldwide sharing similar urban built-environment imagery. [src: env_embedding_explorer]
- The pooled curve has a 2.0x ratio. It blends the two signals and is dominated by the 38% human-associated fraction. [src: env_embedding_explorer]
- The report concludes the signal is primarily driven by variation in natural environments, not urban settings. [src: env_embedding_explorer] It concludes the embeddings are most informative for environmental microbiology samples and least informative for clinical isolates. [src: env_embedding_explorer]

The binned pooled curve for good-quality coordinates, over 50,000 sampled pairs, is below. [src: env_embedding_explorer]

| Distance | Mean cosine distance | Pairs |
|---|---|---|
| <100 km | 0.41 | 231 [src: env_embedding_explorer] |
| 100–500 km | 0.51 | 1,058 [src: env_embedding_explorer] |
| 500–1K km | 0.56 | 2,016 [src: env_embedding_explorer] |
| 1K–2K km | 0.66 | 3,779 [src: env_embedding_explorer] |
| 2K–5K km | 0.78 | 5,824 [src: env_embedding_explorer] |
| 5K–10K km | 0.80 | 20,935 [src: env_embedding_explorer] |
| 10K–20K km | 0.82 | 16,107 [src: env_embedding_explorer] |

### Relation to the distance-decay literature

The report describes distance-decay as a biogeographic pattern in which community similarity decreases with geographic distance, and interprets its embedding relationship as this pattern. [src: env_embedding_explorer] See [[entities/distance-decay]]. It treats its stronger decay in environmental than human-associated samples as consistent with environmental selection. [src: env_embedding_explorer] This interpretation is the report's, set against the literature below.

- Pearman et al. (2024) found macroalgal microbiome composition responds primarily to environmental variation rather than geographic separation. [src: env_embedding_explorer]
- Liu et al. (2022) found that metal contamination explained more mining-soil fungal community structure variation (4.16%) than geographic distance (1.21%). [src: env_embedding_explorer]
- The report interprets the plateau above ~5,000 km as suggesting the embeddings capture environmental features such as land use and vegetation more than raw distance. [src: env_embedding_explorer]
- Zhang et al. (2022) found similar distance-decay patterns but different mechanisms in rare and abundant bacterial subcommunities. [src: env_embedding_explorer]
- The report sees weaker decay in human-associated samples as echoing the idea that dispersal limitation produces stronger geographic patterns than deterministic selection alone. [src: env_embedding_explorer]
- Wang et al. (2024) showed that aridity shapes distinct soil bacterial biogeographic patterns, with higher similarity-distance decay rates across environmental gradients. [src: env_embedding_explorer]

### Composition of the embedded genomes

Human-associated sources make up 38% of the 83,287 genomes with AlphaEarth embeddings. [src: env_embedding_explorer] They are Human clinical with 16,390 genomes (20%) [src: env_embedding_explorer], Human gut with 13,466 (16%) [src: env_embedding_explorer] and Human other with 1,669 (2%). [src: env_embedding_explorer] Environmental categories are much smaller: Soil has 6,073 (7%) [src: env_embedding_explorer], Marine 5,850 (7%) [src: env_embedding_explorer] and Freshwater 5,840 (7%). [src: env_embedding_explorer] The report attributes the clinical skew to NCBI's pathogen-sequencing bias, because clinical isolates tend to have good geographic metadata from epidemiological tracking. [src: env_embedding_explorer] It cites Saha et al., 2023 for public genome databases being heavily skewed toward pathogens and clinical isolates. [src: env_embedding_explorer] It states that clinical sampling bias is known in genomic databases but had not been quantified for satellite-derived environmental embeddings. [src: env_embedding_explorer] See [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]]. The "Other" class has 13,944 genomes (17%). It holds site-specific labels, generic terms and clinical sites the keywords missed. [src: env_embedding_explorer] Aspo HRL and Olkiluoto are underground research labs. [src: env_embedding_explorer]

### Link to gene content and ecotype analysis

The earlier ecotype_analysis project found AlphaEarth-based environment similarity to be a weak predictor of gene content, with median partial correlation 0.0025. [src: env_embedding_explorer] It also found that phylogeny dominates over environment. [src: env_embedding_explorer] The report hypothesizes that clinical bias may partly explain the weak signal, since 38% of compared genomes from interchangeable hospital environments would dilute the relationship. [src: env_embedding_explorer] It proposes that repeating the ecotype analysis on environmental samples could reveal a stronger signal. [src: env_embedding_explorer] See [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]].

### Coordinate quality

The report flags 30,469 genomes (36.6%) that share coordinates with >50 genomes and >10 species. This is a heuristic for institutional addresses rather than sampling sites. [src: env_embedding_explorer] The report provides a coordinate quality-control framework for flagging institutional addresses, with known limitations. [src: env_embedding_explorer] The dataset has 11,765 unique coordinate locations across 83,286 genomes with latitude/longitude. [src: env_embedding_explorer] The quality classes are Good with 50,109 genomes (60.2%) [src: env_embedding_explorer], Suspicious cluster with 30,469 (36.6%) [src: env_embedding_explorer] and Low precision (integer degrees) with 2,708 (3.3%). [src: env_embedding_explorer]

Several flagged locations are legitimate field research sites [src: env_embedding_explorer]:

- Rifle, CO has 1,883 genomes and is a DOE IFRC groundwater research site. [src: env_embedding_explorer]
- Saanich Inlet, BC has 1,529 genomes and is an oceanographic O2-minimum zone. [src: env_embedding_explorer]
- The Siberian soda lakes have 812 genomes from extremophile sampling campaigns. [src: env_embedding_explorer]
- Pittsburgh, PA has 630 genomes and is considered likely institutional because of diverse clinical sources. [src: env_embedding_explorer]
- Lima, Peru has 1,641 genomes. Its integer coordinates are considered likely approximate. [src: env_embedding_explorer]

### Embedding structure

UMAP (uniform manifold approximation and projection) of the 64-dimensional embeddings to 2D reveals substantial structure. [src: env_embedding_explorer] DBSCAN identified 320 clusters. [src: env_embedding_explorer] Many clusters are dominated by a single environment category. [src: env_embedding_explorer] Rare types (Air, Extreme, Plant) concentrate in a few clusters. Human gut and Human clinical span many clusters, likely reflecting geographic sub-structure. [src: env_embedding_explorer] Colouring by phylum shows some taxonomic clustering. [src: env_embedding_explorer] This is partly confounded with environment, for example Campylobacterota are predominantly gut-associated. [src: env_embedding_explorer]

### Metadata coverage and environment labels

The embeddings table covers 83,287 genomes, 28.4% of the 293,059 in the pangenome database. [src: env_embedding_explorer] Of these, 79,449 have valid embeddings in all 64 dimensions. [src: env_embedding_explorer] The other 3,838 have NaN (not a number) in at least one dimension. [src: env_embedding_explorer]

| Field | Genomes | Share |
|---|---|---|
| Lat/lon (cleaned) | 83,286 | 100.0% [src: env_embedding_explorer] |
| geo_loc_name | 83,270 | 100.0% [src: env_embedding_explorer] |
| isolation_source | 76,295 | 91.6% [src: env_embedding_explorer] |
| host | 53,091 | 63.7% [src: env_embedding_explorer] |
| env_broad_scale | 34,800 | 41.8% [src: env_embedding_explorer] |
| env_local_scale | 31,541 | 37.9% [src: env_embedding_explorer] |
| env_medium | 31,483 | 37.8% [src: env_embedding_explorer] |

The NCBI ncbi_env table has 334 distinct harmonized attribute names across 4.1M rows. [src: env_embedding_explorer] The most populated are collection_date (273K genomes), geo_loc_name (272K) and isolation_source (245K). [src: env_embedding_explorer] The report mapped 5,774 unique isolation_source values to 12 broad categories by keyword matching. [src: env_embedding_explorer] It offers this as a reusable harmonization mapping. [src: env_embedding_explorer] The mapping captures 71% of genomes with a label. [src: env_embedding_explorer] 17% remain Other and 12.5% are Unknown because isolation_source is missing or null. [src: env_embedding_explorer] The ENVO (Environment Ontology) env_broad_scale field is cleaner but covers only 42% of genomes. [src: env_embedding_explorer] Many of its values are bare ENVO IDs or generic terms such as "not applicable" and "missing". [src: env_embedding_explorer] Where available, structured terms such as "marine biome [ENVO:00000447]" give standardized categories. [src: env_embedding_explorer]

## Caveats and Open Work

- The coordinate heuristic is a rough first pass. The report recommends checking whether genomes at each location share homogeneous isolation sources (a real site) or diverse unrelated ones (an institution). [src: env_embedding_explorer] It flags legitimate sites including Rifle and Saanich Inlet and needs refinement using isolation_source homogeneity. [src: env_embedding_explorer]
- The pooled distance curve blends environmental and human-associated signals. [src: env_embedding_explorer]
- Taxonomic structure in the UMAP is confounded with environment. [src: env_embedding_explorer] UMAP is non-linear, its cluster structure depends on n_neighbors and min_dist, and it may not reflect true high-dimensional topology. [src: env_embedding_explorer]
- DBSCAN eps=0.5 produced 320 clusters, likely too fine-grained, and coarser clustering may better match environment categories. [src: env_embedding_explorer]
- The keyword mapping leaves 17% of genomes as Other. [src: env_embedding_explorer] Keyword matching misses site-specific labels and non-English terms. [src: env_embedding_explorer]
- AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid lat/lon metadata. [src: env_embedding_explorer] The 38% clinical/human bias may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]
- The cause of the 4.6% NaN embedding values is unknown, possibly missing satellite imagery at those coordinates. [src: env_embedding_explorer]
- Proposed next steps from the report:
  - Reduce "Other" by adding keywords for clinical body sites, underground labs and generic water sources, with env_broad_scale as fallback. [src: env_embedding_explorer]
  - Re-run the ecotype analysis on environmental-only samples, where the embeddings carry more geographic signal. [src: env_embedding_explorer]
  - Correlate A00–A63 with latitude, temperature, precipitation, NDVI or land cover to learn what each dimension encodes. [src: env_embedding_explorer]
  - Compare ENVO-based classification with keyword harmonization for genomes with env_broad_scale. [src: env_embedding_explorer]
  - Test whether environmental samples with similar embeddings share more accessory genes after controlling for phylogeny. [src: env_embedding_explorer]

## Slots Into

- [[concepts/distance-decay-of-environmental-embeddings-with-geographic-distance]]: embedding distance rises from 0.27 to 0.90 for environmental samples (3.4x) but only from 0.37 to 0.75 for human-associated samples (2.0x). [src: env_embedding_explorer]
- [[concepts/clinical-sampling-bias-in-environment-embedding-analyses]]: human-associated sources are 38% of embedded genomes. [src: env_embedding_explorer]
- [[concepts/coordinate-quality-and-institutional-address-artifacts-in-genome-geolocation]]: 36.6% of genomes fall in suspicious coordinate clusters, and some of these are real sites. [src: env_embedding_explorer]
- [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]]: the keyword mapping captures 71% of labelled genomes. [src: env_embedding_explorer]
- [[concepts/metadata-and-annotation-coverage-gaps-biasing-environmental-genome-cohorts]]: env_broad_scale covers only 41.8% of genomes. [src: env_embedding_explorer]
- [[concepts/environmental-versus-phylogenetic-drivers-of-gene-content]]: ecotype_analysis found a weak median partial correlation of 0.0025 for environment similarity, which the report ties to clinical dilution. [src: env_embedding_explorer]
