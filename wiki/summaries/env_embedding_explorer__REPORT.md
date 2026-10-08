---
type: "Summary"
description: "Characterization of 64-dimensional AlphaEarth satellite-derived environmental embeddings for 83,287 pangenome genomes, covering geographic distance-decay, human-associated sampling bias, coordinate quality, metadata harmonization, and UMAP/DBSCAN structure."
doc_type: "short"
full_text: "sources/env_embedding_explorer__REPORT.md"
---
# AlphaEarth Embeddings, Geography & Environment Explorer

## Overview

This project characterizes 64-dimensional AlphaEarth satellite-derived embeddings for 83,287 genomes in the KBase pangenome database. It combines geographic coordinates, NCBI environmental metadata, environment harmonization, coordinate quality control, dimensionality reduction, clustering and geographic-distance analyses. The embeddings cover 28.4% of 293,059 genomes. Of the embedded genomes, 79,449 have valid values across all 64 dimensions and 3,838 contain at least one NaN. [src: env_embedding_explorer]

The 64 embedding dimensions (A00–A63) take values in [-0.544, 0.544], with mean near zero (-0.008) and mean standard deviation 0.109. The embedded genomes span 135 phyla, 15,046 species, and the full global extent (latitude -85 to +84, longitude -178 to +180). [src: env_embedding_explorer]

The analysis draws on two tables in [[data/kbase-ke-pangenome]]. The first, `alphaearth_embeddings_all_years`, supplies the 64-dimensional environmental embeddings, cleaned latitude/longitude and taxonomy. The second, `ncbi_env`, supplies NCBI environmental metadata in EAV (entity–attribute–value, one row per attribute) format. [src: env_embedding_explorer]

## Key Findings

### Geographic signal is stronger for environmental samples

Environmental samples (Soil, Marine, Freshwater, Extreme and Plant) show a 3.4x geographic gradient. Their mean cosine distance rises from 0.27 for genomes collected within <100 km to 0.90 at intercontinental distances >10,000 km. Human-associated samples (gut, clinical and other) show a flatter 2.0x gradient, from 0.37 nearby to 0.75 far away. The report's interpretation is that natural environments vary more in satellite-observed landscape properties, while hospitals and clinics worldwide share similar urban built-environment imagery. The pooled "All samples" curve (2.0x ratio) therefore blends these two signals and is dominated by the 38% human-associated fraction. It should not be read as a single homogeneous relationship. [src: env_embedding_explorer]

The report interprets the embeddings as encoding geographic/environmental context derived from satellite imagery at each genome's sampling location. This context likely includes climate, land use, vegetation type and urban/rural character, but these specific features are inferred rather than measured. Because the signal comes mainly from variation in natural environments rather than urban settings, the report concludes that the embeddings are most informative for environmental microbiology samples and least informative for clinical isolates. [src: env_embedding_explorer]

### Embedding distance increases with geographic distance

Across 50,000 sampled genome pairs with good-quality coordinates, mean embedding cosine distance increased monotonically with geographic distance. The relationship is strongest at short distances (<2,000 km) and plateaus at intercontinental scales (>5,000 km). The reported bins were: <100 km, 0.41 across 231 pairs; 100–500 km, 0.51 across 1,058 pairs; 500–1K km, 0.56 across 2,016 pairs; 1K–2K km, 0.66 across 3,779 pairs; 2K–5K km, 0.78 across 5,824 pairs; 5K–10K km, 0.80 across 20,935 pairs; and 10K–20K km, 0.82 across 16,107 pairs. This supports the interpretation that AlphaEarth embeddings capture spatially autocorrelated environmental context rather than random variation. That context likely includes climate, vegetation, land use and urban/rural character. [src: env_embedding_explorer]

### The AlphaEarth subset has a strong human-associated sampling bias

Of the 83,287 genomes with AlphaEarth embeddings, 38% are human-associated: Human clinical includes 16,390 genomes (20%), Human gut 13,466 (16%) and Human other 1,669 (2%). Environmental categories are smaller: Soil includes 6,073 (7%), Marine 5,850 (7%) and Freshwater 5,840 (7%). The report attributes this to NCBI's overall bias toward pathogen sequencing. Clinical isolates tend to have good geographic metadata from epidemiological tracking, which is why they have AlphaEarth embeddings. Another 13,944 genomes (17%) were classified as Other. These include site-specific labels such as Aspo HRL and Olkiluoto (underground research labs), generic terms such as water and bodily fluid, and clinical sites the keyword rules did not capture. [src: env_embedding_explorer]

The report notes that public genome databases are heavily skewed toward pathogens and clinical isolates (Saha et al., 2023), which biases any analysis of environment–genome relationships. This bias is known, but it had not been quantified for satellite-derived environmental embeddings. [src: env_embedding_explorer]

### Coordinate quality is heterogeneous

The 83,286 genomes with latitude and longitude occupy 11,765 unique coordinate locations. Of these genomes, 50,109 (60.2%) were classified as Good, 30,469 (36.6%) as Suspicious cluster and 2,708 (3.3%) as Low precision (integer degrees). [src: env_embedding_explorer]

The suspicious-cluster heuristic flags 30,469 genomes (36.6%) at shared coordinates with >50 genomes and >10 species. It treats these locations as potential institutional addresses rather than sampling sites, but it also flags several legitimate field research sites. Examples include Rifle, Colorado (39.54, -107.78; 1,883 genomes; DOE IFRC groundwater research site), Saanich Inlet, British Columbia (48.36, -123.30; 1,529 genomes; oceanographic O2-minimum zone), Siberian soda lakes (52.11, 79.17; 812 genomes; extremophile sampling campaigns), Pittsburgh, Pennsylvania (40.44, -79.97; 630 genomes; likely institutional, diverse clinical) and Lima, Peru (-12.0, -77.0; 1,641 genomes; integer coordinates likely approximate). [src: env_embedding_explorer]

### UMAP structure correlates with environment and taxonomy

UMAP, a nonlinear dimensionality-reduction method, projected the embeddings into two dimensions. DBSCAN, a density-based clustering method, then identified 320 clusters, many of them dominated by a single harmonized environment category. Rare categories such as Air, Extreme and Plant concentrated in a few clusters. Human gut and Human clinical genomes were spread across many clusters, which the report interprets as likely geographic substructure. Coloring the UMAP by phylum also showed taxonomic structure, but this was partly confounded with environment; for example, Campylobacterota were predominantly gut-associated. [src: env_embedding_explorer]

### Metadata coverage and harmonization are uneven

Among the 83,287 AlphaEarth genomes, cleaned latitude/longitude were available for 83,286 (100.0%), geo_loc_name for 83,270 (100.0%), isolation_source for 76,295 (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%) and env_medium for 31,483 (37.8%). The NCBI ncbi_env table contains 334 distinct harmonized attribute names across 4.1M rows. Its most populated attributes are collection_date (273K genomes), geo_loc_name (272K) and isolation_source (245K). [src: env_embedding_explorer]

A keyword-matching workflow mapped 5,774 unique isolation_source free-text values to 12 broad categories and captured 71% of genomes with a label. Another 17% remained Other, and 12.5% were Unknown because isolation_source was missing or null. The structured env_broad_scale ENVO ontology field is cleaner but covers only 42% of genomes. Many of its records contain bare ENVO identifiers such as ENVO:00000428 or generic terms such as not applicable and missing. Where available, structured terms such as marine biome [ENVO:00000447] provide standardized categories. [src: env_embedding_explorer]

### Implication for environment–gene-content analyses

The report cites the earlier Ecotype Correlation Analysis project ([[summaries/ecotype_analysis__REPORT]]). That project found AlphaEarth-based environment similarity to be a weak predictor of gene content, with a median partial correlation of 0.0025 (a null-leaning result; see [[concepts/ecotype-environment-gene-content]]). The 38% human-associated composition found here may dilute that relationship, because many clinical samples come from relatively interchangeable hospital environments. This dilution is proposed, not demonstrated. It motivates repeating the ecotype analysis on environmental-only samples; a stronger environmental signal should not yet be treated as established. [src: env_embedding_explorer]

### Literature context

- Pearman et al. (2024) found that macroalgal microbiome composition responds primarily to environmental variation rather than geographic separation. The report reads its stronger distance-decay for environmental samples as consistent with this. [src: env_embedding_explorer]
- Liu et al. (2022) found that in mining soils, metal contamination explained more variation in fungal community structure (4.16%) than geographic distance (1.21%). The report draws a parallel with the plateau above ~5,000 km, which it takes as evidence that the embeddings capture environmental features more than raw distance. [src: env_embedding_explorer]
- Zhang et al. (2022) found that rare and abundant bacterial subcommunities show similar distance-decay patterns but differ mechanistically. The report suggests the weaker human-associated distance-decay echoes the idea that dispersal limitation generates stronger geographic patterns than deterministic selection alone. [src: env_embedding_explorer]
- Wang et al. (2024) showed that aridity shapes distinct soil-bacterial biogeographic patterns, with higher similarity-distance decay rates across environmental gradients. The report takes this as support for environmentally driven variation in the embeddings. [src: env_embedding_explorer]

The report also cites [[entities/gtdb]], a genome-based taxonomy of bacterial and archaeal diversity, as a reference resource; this citation carries no finding of the report. [src: env_embedding_explorer]

## Caveats and Limitations

AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid latitude and longitude metadata. The 38% human-associated fraction may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]

The coordinate-quality heuristic is a crude first pass that flags legitimate field sites such as Rifle and Saanich Inlet. Refinement should check whether genomes at each location have homogeneous isolation sources (a real site) or diverse unrelated sources (an institutional address). [src: env_embedding_explorer]

Environment harmonization has a long tail: 17% of genomes fall into Other, and keyword matching may miss site-specific labels and non-English terms. [src: env_embedding_explorer]

The proposed harmonization improvements are to:

- add clinical body-site terms such as cerebrospinal fluid, lung and throat;
- add underground-laboratory terms such as Aspo and Olkiluoto;
- use generic water-source terms;
- use env_broad_scale as a fallback when isolation_source is ambiguous. [src: env_embedding_explorer]

UMAP is a nonlinear projection. Its apparent cluster structure depends on parameters including n_neighbors and min_dist and may not represent the true high-dimensional topology. DBSCAN with eps=0.5 produced 320 clusters, which may be too fine-grained; coarser clustering may better match environment categories. [src: env_embedding_explorer]

Embedding NaN values affect 4.6% of the AlphaEarth records, and their cause is unknown; missing satellite imagery at the corresponding coordinates is one possible explanation. [src: env_embedding_explorer]

The coordinate-distance relationship is strongest below 2,000 km and plateaus above 5,000 km, so it should not be read as a simple raw-distance effect. The report instead relates it to environmental distance-decay. It also notes that in comparable microbial-ecology studies, environmental variation can explain community differences more strongly than geographic separation. [src: env_embedding_explorer]

## Outputs and Figures

Generated data files: `data/alphaearth_with_env.csv` (83,287 rows; merged embeddings plus pivoted environment labels), `data/coverage_stats.csv` (7 rows; per-attribute population rates), `data/ncbi_env_attribute_counts.csv` (334 rows; full inventory of harmonized_name values), `data/isolation_source_raw_counts.csv` (5,774 rows; raw isolation_source value frequencies) and `data/umap_coords.csv` (79,449 rows; pre-computed UMAP 2D coordinates). [src: env_embedding_explorer]

- `coverage_bar.png`: attribute population rates across AlphaEarth genomes. [src: env_embedding_explorer]
- `coverage_intersections.png`: UpSet-style intersection of metadata attribute combinations. [src: env_embedding_explorer]
- `coord_quality_map.png`: global map with coordinate-quality flags (good/suspicious/low precision). [src: env_embedding_explorer]
- `env_categories.png`: harmonized environment-category frequencies. [src: env_embedding_explorer]
- `umap_by_env_category.png`: UMAP of embeddings colored by harmonized environment category. [src: env_embedding_explorer]
- `umap_by_phylum.png`: UMAP colored by phylum (top 10 + Other); an interactive HTML version allows toggling phyla. [src: env_embedding_explorer]
- `umap_by_coord_quality.png`: UMAP colored by coordinate-quality flag. [src: env_embedding_explorer]
- `umap_clusters.png`: DBSCAN clusters in UMAP space. [src: env_embedding_explorer]
- `cluster_env_heatmap.png`: environment-category composition of the top 20 UMAP clusters. [src: env_embedding_explorer]
- `env_cluster_distribution.png`: cluster distribution per environment category. [src: env_embedding_explorer]
- `geo_vs_embedding_distance.png`: scatter of geographic vs embedding distance (10K sample). [src: env_embedding_explorer]
- `geo_vs_embedding_binned.png`: mean embedding distance by geographic-distance bin. [src: env_embedding_explorer]
- `geo_vs_embedding_by_env_group.png`: stratified distance curves for environmental, human-associated and animal samples. [src: env_embedding_explorer]

## Open Directions

- Refine coordinate QC with isolation_source homogeneity and test whether flagged locations are institutional addresses or legitimate field sites. [src: env_embedding_explorer]
- Re-run [[concepts/ecotype-environment-gene-content]] using environmental-only samples to test whether the environment–gene-content relationship strengthens when the human-associated subset is removed. [src: env_embedding_explorer]
- Correlate embedding dimensions A00–A63 with latitude, temperature, precipitation, NDVI and land-cover classifications to identify the environmental features represented by individual dimensions. [src: env_embedding_explorer]
- Compare keyword-based harmonization with env_broad_scale classifications for the 42% of genomes covered by the structured field. [src: env_embedding_explorer]
- Test whether environmental samples with similar embeddings share more accessory genes after controlling for phylogeny. [src: env_embedding_explorer]

## Slots Into

- [[concepts/ecotype-environment-gene-content]]: The project offers a possible reason why AlphaEarth environment similarity appeared to be a weak predictor of gene content (median partial correlation 0.0025) and proposes an environmental-only reanalysis. [src: env_embedding_explorer]
- [[concepts/pangenome-integration]]: The project integrates AlphaEarth embeddings, pangenome genomes, taxonomy, coordinates and NCBI environmental metadata across 83,287 records. [src: env_embedding_explorer]
- [[concepts/environment-embedding-geography]]: The project establishes how AlphaEarth embeddings behave across geography and environment strata. This includes stronger distance-decay for environmental samples, UMAP/DBSCAN structure and the effects of coordinate quality. [src: env_embedding_explorer]
- [[concepts/cultivation-collection-bias-in-ecological-genomics]]: The embedded subset is 38% human-associated, which the report attributes to pathogen-sequencing bias and coordinate availability; this limits environment–genome inference. [src: env_embedding_explorer]
- [[concepts/spatial-sampling-effort-confounding]]: A shared-coordinate heuristic flags 30,469 genomes (36.6%) as potential institutional addresses. However, the flagged set includes heavily sampled legitimate field sites such as Rifle and Saanich Inlet, a Pittsburgh cluster described only as likely institutional, and Lima's integer coordinates, described as likely approximate. Distinguishing these cases still needs isolation-source homogeneity checks. [src: env_embedding_explorer]
- [[concepts/ontology-and-category-schema-sensitivity]]: Keyword harmonization leaves 17% Other and 12.5% Unknown, while the ENVO env_broad_scale field covers only 42% of genomes. [src: env_embedding_explorer]
