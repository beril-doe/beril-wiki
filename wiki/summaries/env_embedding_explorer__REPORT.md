---
type: "Summary"
description: "AlphaEarth embeddings reveal environmental geography signals and clinical sampling bias."
doc_type: "short"
full_text: "sources/env_embedding_explorer__REPORT.md"
---
# AlphaEarth Embeddings, Geography & Environment Explorer

## Overview

This project characterizes 64-dimensional AlphaEarth satellite-derived embeddings for 83,287 genomes in the KBase pangenome database, combining geographic coordinates, NCBI environmental metadata, environment harmonization, coordinate quality control, dimensionality reduction, clustering, and geographic-distance analyses. The embeddings cover 28.4% of 293,059 genomes; 79,449 have valid values across all 64 dimensions and 3,838 contain at least one NaN. [src: env_embedding_explorer]

## Key Findings

### Geographic signal is stronger for environmental samples

Environmental samples—Soil, Marine, Freshwater, Extreme, and Plant—show a 3.4x geographic gradient: mean cosine distance rises from 0.27 for genomes collected within <100 km to 0.90 at intercontinental distances >10,000 km. Human-associated samples—gut, clinical, and other—show a flatter 2.0x gradient, from 0.37 nearby to 0.75 far away. The interpretation is that natural environments vary more in satellite-observed landscape properties, whereas hospitals and clinics worldwide have more homogeneous urban imagery. [src: env_embedding_explorer]

### Embedding distance increases with geographic distance

Across 50,000 sampled genome pairs with good-quality coordinates, mean embedding cosine distance increased monotonically with geographic distance and plateaued at intercontinental scales. The reported bins were: <100 km, 0.41 across 231 pairs; 100–500 km, 0.51 across 1,058 pairs; 500–1K km, 0.56 across 2,016 pairs; 1K–2K km, 0.66 across 3,779 pairs; 2K–5K km, 0.78 across 5,824 pairs; 5K–10K km, 0.80 across 20,935 pairs; and 10K–20K km, 0.82 across 16,107 pairs. This supports the interpretation that AlphaEarth embeddings capture spatially autocorrelated environmental context, including likely climate, vegetation, land use, and urban/rural character, rather than random variation. [src: env_embedding_explorer]

### The AlphaEarth subset has a strong human-associated sampling bias

Of the 83,287 genomes with AlphaEarth embeddings, 38% are human-associated: Human clinical includes 16,390 genomes (20%), Human gut includes 13,466 (16%), and Human other includes 1,669 (2%). Environmental categories are smaller: Soil includes 6,073 (7%), Marine 5,850 (7%), and Freshwater 5,840 (7%). An additional 13,944 genomes (17%) were classified as Other, including site-specific labels such as Aspo HRL and Olkiluoto, generic terms such as water and bodily fluid, and clinical sites not captured by the keyword rules. [src: env_embedding_explorer]

### Coordinate quality is heterogeneous

Among 83,286 genomes with latitude and longitude, 50,109 (60.2%) were classified as Good, 30,469 (36.6%) as Suspicious cluster, and 2,708 (3.3%) as Low precision (integer degrees). The suspicious-cluster heuristic flags locations shared by >50 genomes and >10 species as potential institutional addresses, but it also flags legitimate field sites. Examples include Rifle, Colorado (39.54, -107.78; 1,883 genomes; DOE IFRC groundwater research site), Saanich Inlet, British Columbia (48.36, -123.30; 1,529 genomes; oceanographic O2-minimum zone), Siberian soda lakes (52.11, 79.17; 812 genomes; extremophile sampling campaigns), Pittsburgh, Pennsylvania (40.44, -79.97; 630 genomes; likely institutional and diverse clinical sampling), and Lima, Peru (-12.0, -77.0; 1,641 genomes; integer coordinates likely approximate). [src: env_embedding_explorer]

### UMAP structure correlates with environment and taxonomy

UMAP, a nonlinear dimensionality-reduction method, projected the embeddings into two dimensions; DBSCAN, a density-based clustering method, identified 320 clusters. Many clusters were dominated by a single harmonized environment category. Rare categories such as Air, Extreme, and Plant concentrated in a few clusters, whereas Human gut and Human clinical genomes were distributed across many clusters, potentially reflecting geographic substructure. Coloring the UMAP by phylum also showed taxonomic structure, although this was partly confounded with environment; Campylobacterota, for example, were predominantly gut-associated. [src: env_embedding_explorer]

### Metadata coverage and harmonization are uneven

Among the 83,287 AlphaEarth genomes, cleaned latitude/longitude were available for 83,286, geo_loc_name for 83,270, isolation_source for 76,295 (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%), and env_medium for 31,483 (37.8%). The NCBI ncbi_env table contains 334 distinct harmonized attribute names across 4.1M rows; its most populated attributes are collection_date (273K genomes), geo_loc_name (272K), and isolation_source (245K). [src: env_embedding_explorer]

A keyword-matching workflow mapped 5,774 unique isolation_source free-text values to 12 broad categories, capturing 71% of genomes with a label; 17% remained Other and 12.5% were Unknown because isolation_source was missing or null. The structured env_broad_scale field is cleaner but covers only 42% of genomes, and many records contain bare ENVO identifiers such as ENVO:00000428 or generic terms such as not applicable and missing. [src: env_embedding_explorer]

### Implication for environment–gene-content analyses

The project reports that the prior [[concepts/ecotype-environment-gene-content]] analysis found AlphaEarth-based environment similarity to be a weak predictor of gene content, with a median partial correlation of 0.0025. The newly identified 38% human-associated composition may dilute that relationship because many clinical samples occupy relatively interchangeable urban environments; this motivates repeating the ecotype analysis on environmental-only samples rather than treating a stronger environmental signal as established. [src: env_embedding_explorer]

## Caveats and Limitations

AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid latitude and longitude metadata; the 38% human-associated fraction may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]

The coordinate-quality heuristic is a crude first pass: it flags legitimate field sites such as Rifle and Saanich Inlet. Refinement should use isolation_source homogeneity at each location to distinguish genuine sampling sites from institutional addresses. [src: env_embedding_explorer]

Environment harmonization has a long tail: 17% of genomes fall into Other, and keyword matching may miss site-specific labels and non-English terms. The proposed improvements are to add clinical body-site terms such as cerebrospinal fluid, lung, and throat; add underground-laboratory terms such as Aspo and Olkiluoto; use generic water-source terms; and use env_broad_scale as a fallback when isolation_source is ambiguous. [src: env_embedding_explorer]

UMAP is a nonlinear projection whose apparent cluster structure depends on parameters including n_neighbors and min_dist and may not represent the true high-dimensional topology. DBSCAN with eps=0.5 produced 320 clusters, which may be too fine-grained; coarser clustering may better match environment categories. [src: env_embedding_explorer]

Embedding NaN values affect 4.6% of the AlphaEarth records, and their cause is unknown; missing satellite imagery at the corresponding coordinates is one possible explanation. [src: env_embedding_explorer]

The coordinate-distance relationship is strongest below 2,000 km and plateaus above 5,000 km, so it should not be interpreted as a simple raw-distance effect. The report instead relates it to environmental distance-decay and notes that environmental variation can explain community differences more strongly than geographic separation in comparable microbial-ecology studies. [src: env_embedding_explorer]

## Open Directions

- Refine coordinate QC with isolation_source homogeneity and test whether flagged locations are institutional addresses or legitimate field sites. [src: env_embedding_explorer]
- Re-run [[concepts/ecotype-environment-gene-content]] using environmental-only samples to test whether the environment–gene-content relationship strengthens when the human-associated subset is removed. [src: env_embedding_explorer]
- Correlate embedding dimensions A00–A63 with latitude, temperature, precipitation, NDVI, and land-cover classifications to identify the environmental features represented by individual dimensions. [src: env_embedding_explorer]
- Compare keyword-based harmonization with env_broad_scale classifications for the 42% of genomes covered by the structured field. [src: env_embedding_explorer]
- Test whether environmental samples with similar embeddings share more accessory genes after controlling for phylogeny. [src: env_embedding_explorer]

## Slots Into

- [[concepts/ecotype-environment-gene-content]] — The project quantifies why AlphaEarth environment similarity may have appeared weak as a predictor of gene content and proposes an environmental-only reanalysis. [src: env_embedding_explorer]
- [[concepts/pangenome-integration]] — The project integrates AlphaEarth embeddings, pangenome genomes, taxonomy, coordinates, and NCBI environmental metadata across 83,287 records. [src: env_embedding_explorer]
- [[concepts/environment-embedding-geography]] — The project establishes the geographic and environment-stratified behavior of AlphaEarth embeddings, including stronger distance-decay for environmental samples and the effects of coordinate quality. [src: env_embedding_explorer]
