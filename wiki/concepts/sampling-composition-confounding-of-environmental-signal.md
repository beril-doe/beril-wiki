---
type: "Concept"
description: "Sampling composition can create or mask apparent environmental genomic gradients."
sources: ["summaries/env_embedding_explorer__REPORT.md"]
---
# Sampling Composition Confounding of Environmental Signal

Apparent environmental genomic gradients can reflect differences in which sample types are represented, rather than environmental effects alone. The [[summaries/env_embedding_explorer__REPORT]] shows that AlphaEarth embedding analyses combine strongly uneven human-associated and environmental sampling strata, so composition must be treated as a potential confounder when relating environmental similarity to genome content. [src: env_embedding_explorer]

## Core Claim

The AlphaEarth dataset contains 83,287 genomes, representing 28.4% of 293,059 genomes in the KBase pangenome database; 38% of the embedded genomes are human-associated, including 16,390 Human clinical genomes (20%), 13,466 Human gut genomes (16%), and 1,669 Human other genomes (2%). [src: env_embedding_explorer] Environmental categories are smaller, including 6,073 Soil genomes (7%), 5,850 Marine genomes (7%), and 5,840 Freshwater genomes (7%), while 13,944 genomes (17%) were classified as Other. [src: env_embedding_explorer]

This composition matters because human-associated and environmental samples show different relationships between geographic separation and AlphaEarth embedding distance. [src: env_embedding_explorer] Environmental samples—Soil, Marine, Freshwater, Extreme, and Plant—show a 3.4x geographic gradient, with mean cosine distance increasing from 0.27 below 100 km to 0.90 above 10,000 km. [src: env_embedding_explorer] Human-associated samples—gut, clinical, and other—show a flatter 2.0x gradient, increasing from 0.37 nearby to 0.75 at far distances. [src: env_embedding_explorer]

Therefore, a pooled analysis can make an environmental signal appear weaker when a large human-associated subset occupies relatively interchangeable urban environments. [src: env_embedding_explorer] This is a confounding hypothesis rather than an established causal explanation: the report proposes testing it by repeating the [[concepts/ecotype-environment-gene-content]] analysis on environmental-only samples. [src: env_embedding_explorer]

## Evidence from Geographic and Embedding Structure

Across 50,000 sampled genome pairs with good-quality coordinates, mean embedding cosine distance increased monotonically with geographic distance and plateaued at intercontinental scales. [src: env_embedding_explorer] The reported mean distances were 0.41 for distances below 100 km across 231 pairs; 0.51 for 100–500 km across 1,058 pairs; 0.56 for 500–1K km across 2,016 pairs; 0.66 for 1K–2K km across 3,779 pairs; 0.78 for 2K–5K km across 5,824 pairs; 0.80 for 5K–10K km across 20,935 pairs; and 0.82 for 10K–20K km across 16,107 pairs. [src: env_embedding_explorer]

The geographic relationship is strongest below 2,000 km and plateaus above 5,000 km, so the pattern should not be interpreted as a simple raw-distance effect. [src: env_embedding_explorer] Instead, it is consistent with spatially autocorrelated environmental context, including likely climate, vegetation, land use, and urban/rural character. [src: env_embedding_explorer] Its strength in a pooled dataset can depend on the relative representation of environmental samples, human-associated samples, and heterogeneous residual categories. [src: env_embedding_explorer]

UMAP, a nonlinear dimensional-reduction method, produced two-dimensional structure in which many clusters were dominated by a single harmonized environment category. [src: env_embedding_explorer] Rare categories such as Air, Extreme, and Plant concentrated in a few clusters, whereas Human gut and Human clinical genomes were distributed across many clusters, potentially reflecting geographic substructure. [src: env_embedding_explorer] Taxonomic structure was also visible, but it was partly confounded with environment; Campylobacterota, for example, were predominantly gut-associated. [src: env_embedding_explorer] These results support stratifying or adjusting analyses by sample environment and taxonomy before interpreting embedding or gene-content gradients as environmental effects. [src: env_embedding_explorer]

## Metadata and Coverage Mechanisms

The embedded dataset has uneven metadata coverage: cleaned latitude/longitude were available for 83,286 genomes, geo_loc_name for 83,270, isolation_source for 76,295 (91.6%), host for 53,091 (63.7%), env_broad_scale for 34,800 (41.8%), env_local_scale for 31,541 (37.9%), and env_medium for 31,483 (37.8%). [src: env_embedding_explorer] These differences create opportunities for missingness and metadata resolution to track sample composition rather than environmental biology. [src: env_embedding_explorer]

A keyword workflow mapped 5,774 unique isolation_source free-text values to 12 broad categories and captured 71% of genomes with a label; 17% remained Other and 12.5% were Unknown because isolation_source was missing or null. [src: env_embedding_explorer] The structured env_broad_scale field was cleaner but covered only 42% of genomes, and many records contained bare ENVO identifiers such as ENVO:00000428 or generic terms such as not applicable and missing. [src: env_embedding_explorer] Consequently, category assignment itself can alter the apparent balance between human-associated, environmental, and unresolved samples. [src: env_embedding_explorer]

Coordinate quality provides a second composition-related source of bias. [src: env_embedding_explorer] Among 83,286 genomes with latitude and longitude, 50,109 (60.2%) were classified as Good, 30,469 (36.6%) as Suspicious cluster, and 2,708 (3.3%) as Low precision. [src: env_embedding_explorer] The suspicious-cluster heuristic flags locations shared by >50 genomes and >10 species, but it also flags legitimate field sites such as Rifle, Colorado, with 1,883 genomes, and Saanich Inlet, British Columbia, with 1,529 genomes. [src: env_embedding_explorer] Thus, removing all clustered coordinates could preferentially remove well-sampled environmental campaigns, while retaining them could preserve institutional or clinical sampling concentrations. [src: env_embedding_explorer]

## Relation to Environment–Gene-Content Inference

The prior [[concepts/ecotype-environment-gene-content]] analysis found AlphaEarth-based environment similarity to be a weak predictor of gene content, with a median partial correlation of 0.0025. [src: env_embedding_explorer] The 38% human-associated composition may dilute that relationship because clinical samples can occupy relatively interchangeable urban environments, but this explanation has not yet been demonstrated by a stratified reanalysis. [src: env_embedding_explorer] The appropriate interpretation is therefore that sampling composition makes the pooled environment–gene-content result potentially non-diagnostic, not that environmental similarity is known to have a stronger association after correction. [src: env_embedding_explorer]

This concept **refines** [[concepts/environment-embedding-geography]] by distinguishing a geographic or environmental signal in the embeddings from the sample-composition structure that determines how strongly that signal appears in pooled analyses. [src: env_embedding_explorer] It also **connects** to [[concepts/clinical-sampling-bias-and-ecological-inference]], because the large human-associated subset can make clinical and environmental observations non-exchangeable in ecological comparisons. [src: env_embedding_explorer] Interpretation should additionally account for [[concepts/metadata-resolution-and-within-species-heterogeneity]] and [[concepts/sampling-depth-and-downsampling-effects]], since metadata resolution and unequal representation can change the effective comparison set. [src: env_embedding_explorer]

## Tensions

The embeddings show a clear pooled distance–geography relationship, but the report also identifies a strong human-associated sampling bias and a flatter human-associated geographic gradient. [src: env_embedding_explorer] These observations are not contradictory: the pooled gradient may combine genuine environmental distance-decay with differences in sample composition, while the relative contribution of each component remains unresolved. [src: env_embedding_explorer]

## Open Directions

- Restrict the AlphaEarth dataset to environmental categories, recompute partial correlations between embedding similarity and gene-content similarity, and test whether the median partial correlation differs from 0.0025. [src: env_embedding_explorer]
- Reweight or downsample Human clinical, Human gut, Human other, Soil, Marine, Freshwater, Extreme, and Plant categories, then repeat the geographic-distance analysis to test whether the reported 0.41-to-0.82 distance pattern changes with composition. [src: env_embedding_explorer]
- Compare keyword-based isolation_source categories with env_broad_scale for the 42% of genomes covered by the structured field, and test whether environment–gene-content associations are stable across classification schemes. [src: env_embedding_explorer]
- Use isolation_source homogeneity together with coordinate clustering to distinguish institutional addresses from legitimate field sites, then recompute embedding distance–geography relationships under each coordinate-quality definition. [src: env_embedding_explorer]
- Fit phylogeny-aware models to environmental-only samples and test whether similar AlphaEarth embeddings predict greater accessory-gene sharing after controlling for taxonomic relatedness. [src: env_embedding_explorer]
