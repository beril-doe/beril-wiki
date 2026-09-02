---
type: "Concept"
description: "How uneven environmental metadata can alter ecological genomic conclusions"
sources: ["summaries/env_embedding_explorer__REPORT.md"]
---
# Environmental Metadata Harmonization Can Reshape Ecological Genomic Inference

Environmental metadata harmonization converts heterogeneous sample descriptions into comparable ecological categories, but the conversion can change which patterns appear biologically meaningful. [src: env_embedding_explorer] The [[summaries/env_embedding_explorer__REPORT]] shows that metadata coverage, coordinate quality, category definitions, and sampling composition can all influence analyses linking environment, geography, and gene content. [src: env_embedding_explorer]

## Evidence from the AlphaEarth genome subset

The study analyzed 83,287 genomes with 64-dimensional AlphaEarth satellite-derived embeddings, representing 28.4% of 293,059 genomes in the KBase pangenome database. [src: env_embedding_explorer] Of these records, 79,449 had valid values across all 64 embedding dimensions and 3,838 contained at least one NaN. [src: env_embedding_explorer]

Environmental metadata were unevenly available: cleaned latitude and longitude were available for 83,286 genomes, geo_loc_name for 83,270, isolation_source for 76,295 (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%), and env_medium for 31,483 (37.8%). [src: env_embedding_explorer] The NCBI ncbi_env table contained 334 distinct harmonized attribute names across 4.1M rows, with collection_date covering 273K genomes, geo_loc_name covering 272K, and isolation_source covering 245K. [src: env_embedding_explorer]

A keyword-matching workflow mapped 5,774 unique isolation_source free-text values into 12 broad categories and captured 71% of genomes with an isolation_source label. [src: env_embedding_explorer] The resulting classification left 17% of genomes in Other and 12.5% in Unknown because isolation_source was missing or null. [src: env_embedding_explorer] The structured env_broad_scale field was cleaner but covered only 42% of genomes, and some records contained bare ENVO identifiers such as ENVO:00000428 or generic values such as not applicable and missing. [src: env_embedding_explorer]

These coverage differences create a direct [[concepts/metadata-resolution-and-within-species-heterogeneity]] concern: the apparent ecological distribution of genomes depends partly on which metadata field is available and how its values are interpreted. [src: env_embedding_explorer] Keyword matching can also miss site-specific labels and non-English terms, so the resulting categories should be treated as an operational harmonization rather than a complete ecological ontology. [src: env_embedding_explorer]

## Sampling composition as an inferential confounder

The AlphaEarth subset was strongly human-associated, with 38% of genomes classified as human-associated. [src: env_embedding_explorer] Human clinical samples accounted for 16,390 genomes (20%), Human gut for 13,466 (16%), and Human other for 1,669 (2%). [src: env_embedding_explorer] Environmental categories were smaller: Soil contained 6,073 genomes (7%), Marine 5,850 (7%), and Freshwater 5,840 (7%). [src: env_embedding_explorer] Other contained 13,944 genomes (17%) and included site-specific labels such as Aspo HRL and Olkiluoto, generic labels such as water and bodily fluid, and clinical sites not captured by the keyword rules. [src: env_embedding_explorer]

This composition supports the [[concepts/clinical-sampling-bias-and-ecological-inference]] concern that a metadata-defined dataset may not represent the ecological population from which broader conclusions are drawn. [src: env_embedding_explorer] It also affects [[concepts/environment-embedding-geography]] analyses because human-associated samples showed a flatter geographic embedding gradient than environmental samples. [src: env_embedding_explorer] For environmental samples, mean cosine distance increased from 0.27 for genomes collected within <100 km to 0.90 at intercontinental distances >10,000 km, whereas human-associated samples increased from 0.37 nearby to 0.75 far away. [src: env_embedding_explorer]

The report therefore refines interpretation of the earlier [[concepts/ecotype-environment-gene-content]] result: AlphaEarth-based environment similarity had a median partial correlation of 0.0025 with gene content, and the 38% human-associated composition may have diluted that relationship because many clinical samples occupied relatively interchangeable urban environments. [src: env_embedding_explorer] This is a hypothesis requiring environmental-only reanalysis, not evidence that environmental similarity is generally unrelated to gene content. [src: env_embedding_explorer]

## Coordinates are metadata, not ground truth

Among 83,286 genomes with latitude and longitude, 50,109 (60.2%) were classified as Good, 30,469 (36.6%) as Suspicious cluster, and 2,708 (3.3%) as Low precision because they used integer degrees. [src: env_embedding_explorer] The suspicious-cluster heuristic flagged locations shared by >50 genomes and >10 species as possible institutional addresses, but it also flagged legitimate field sites. [src: env_embedding_explorer]

Examples of potentially legitimate flagged sites included Rifle, Colorado (39.54, -107.78; 1,883 genomes; DOE IFRC groundwater research site), Saanich Inlet, British Columbia (48.36, -123.30; 1,529 genomes; oceanographic O2-minimum zone), and Siberian soda lakes (52.11, 79.17; 812 genomes; extremophile sampling campaigns). [src: env_embedding_explorer] Pittsburgh, Pennsylvania (40.44, -79.97; 630 genomes) was likely institutional and included diverse clinical sampling, while Lima, Peru (-12.0, -77.0; 1,641 genomes) had integer coordinates that were likely approximate. [src: env_embedding_explorer]

This ambiguity connects to [[concepts/collection-site-versus-microenvironment-mismatch]]: a shared coordinate can represent a genuine field site, an institution, or an approximate geographic placeholder rather than a common microbial microenvironment. [src: env_embedding_explorer] Because AlphaEarth embedding cosine distance increased with geographic distance, coordinate errors or institutional clustering can propagate into apparent environmental structure. [src: env_embedding_explorer] Across 50,000 sampled genome pairs with good-quality coordinates, mean cosine distance increased monotonically across the reported distance bins: 0.41 for <100 km across 231 pairs; 0.51 for 100–500 km across 1,058 pairs; 0.56 for 500–1K km across 2,016 pairs; 0.66 for 1K–2K km across 3,779 pairs; 0.78 for 2K–5K km across 5,824 pairs; 0.80 for 5K–10K km across 20,935 pairs; and 0.82 for 10K–20K km across 16,107 pairs. [src: env_embedding_explorer]

## Category definitions can create or hide ecological structure

UMAP, a nonlinear dimensional-reduction method, projected the embeddings into two dimensions, and DBSCAN, a density-based clustering method, identified 320 clusters. [src: env_embedding_explorer] Many clusters were dominated by a single harmonized environment category, while rare categories such as Air, Extreme, and Plant concentrated in a few clusters. [src: env_embedding_explorer] Human gut and Human clinical genomes were distributed across many clusters, potentially reflecting geographic substructure. [src: env_embedding_explorer]

The apparent structure is therefore partly dependent on category construction and projection choices, linking this issue to [[concepts/environmental-embedding-ecological-validity]] and [[concepts/ontology-and-category-schema-sensitivity]]. [src: env_embedding_explorer] UMAP cluster structure depends on parameters including n_neighbors and min_dist, and DBSCAN with eps=0.5 produced 320 clusters that may be too fine-grained to match environment categories. [src: env_embedding_explorer] Taxonomic coloring also showed structure, but that structure was partly confounded with environment; Campylobacterota, for example, were predominantly gut-associated. [src: env_embedding_explorer]

## Tensions

The structured env_broad_scale field is cleaner than free-text isolation_source but covers only 42% of the AlphaEarth genomes, whereas keyword harmonization covers 71% of genomes with an isolation_source label but leaves 17% in Other and 12.5% in Unknown. [src: env_embedding_explorer] This creates a tension between broader coverage and cleaner semantic interpretation: using the free-text workflow may increase sample inclusion while increasing category ambiguity, whereas using env_broad_scale may improve consistency while reducing analyzable coverage. [src: env_embedding_explorer]

The geographic signal is also compatible with two interpretations that should not be conflated: AlphaEarth embeddings may capture spatially autocorrelated environmental context, but coordinate clustering and metadata errors may contribute to the observed pattern. [src: env_embedding_explorer] The reported distance relationship was strongest below 2,000 km and plateaued above 5,000 km, so it should not be interpreted as a simple raw-distance effect. [src: env_embedding_explorer]

## Open Directions

- Use isolation_source homogeneity, species composition, and coordinate precision to reclassify the 30,469 Suspicious cluster and 2,708 Low precision coordinates, then test whether the embedding–geographic-distance relationship changes. [src: env_embedding_explorer]
- For the 34,800 genomes with env_broad_scale and the 76,295 with isolation_source, compare keyword categories with structured classifications using confusion matrices and category-specific embedding distances, asking which schema preserves ecological separation with fewer ambiguous assignments. [src: env_embedding_explorer]
- Repeat the [[concepts/ecotype-environment-gene-content]] analysis on environmental-only samples, using phylogeny-controlled partial correlations, to test whether removing the 38% human-associated subset increases the median association above 0.0025. [src: env_embedding_explorer]
- Add clinical body-site terms, underground-laboratory terms, generic water-source terms, and env_broad_scale fallback values to the harmonization workflow, then measure how many of the 13,944 Other genomes move into interpretable categories. [src: env_embedding_explorer]
- Re-run UMAP and DBSCAN across alternative n_neighbors, min_dist, and eps values, then test whether environment-dominated clusters persist in the original 64-dimensional space rather than only in the projection. [src: env_embedding_explorer]
- Correlate embedding dimensions A00–A63 with latitude, temperature, precipitation, NDVI, and land-cover classifications to identify which environmental features drive the observed distance-decay pattern. [src: env_embedding_explorer]
