---
type: "Finding"
description: "For environmental samples (Soil, Marine, Freshwater, Extreme, Plant), nearby genomes (<100 km) have mean AlphaEarth cosine distance 0.27, rising to 0.90 at intercontinental distances (>10,000 km), a 3.4x ratio."
finding_id: "env_embedding_explorer--7b972aad"
result: "observation"
source: "env_embedding_explorer"
quantities: [{"value": "0.27", "what": "mean cosine distance at nearby genomes", "unit": "", "denominator": "", "scope": "<100 km, environmental samples"}, {"value": "0.90", "what": "mean cosine distance at intercontinental distances", "unit": "", "denominator": "", "scope": ">10,000 km, environmental samples"}, {"value": "3.4x", "what": "ratio of far to near mean cosine distance", "unit": "", "denominator": "", "scope": ""}]
caveat: "The coordinate quality-control heuristic is crude and flags some legitimate field sites (Rifle, Saanich Inlet), so it needs refinement using isolation_source homogeneity."
first_added: "2026-11-24"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Embedding distance rises steeply with geographic distance for environmental genomes

For environmental samples (Soil, Marine, Freshwater, Extreme, Plant), nearby genomes (<100 km) have mean AlphaEarth cosine distance 0.27, rising to 0.90 at intercontinental distances (>10,000 km), a 3.4x ratio. [src: env_embedding_explorer]

## Key figures

- **0.27**: mean cosine distance at nearby genomes (scope <100 km, environmental samples) [src: env_embedding_explorer]
- **0.90**: mean cosine distance at intercontinental distances (scope >10,000 km, environmental samples) [src: env_embedding_explorer]
- **3.4x**: ratio of far to near mean cosine distance [src: env_embedding_explorer]

## Evidence

> For **environmental samples** (Soil, Marine, Freshwater, Extreme, Plant), nearby genomes (<100 km) have mean cosine distance 0.27, rising to 0.90 at intercontinental distances (>10,000 km) — a **3.4x ratio**. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The coordinate quality-control heuristic is crude and flags some legitimate field sites (Rifle, Saanich Inlet), so it needs refinement using isolation_source homogeneity. [src: env_embedding_explorer]

> - **Coordinate QC heuristic is crude** — flags some legitimate field sites (Rifle, Saanich Inlet); needs refinement using isolation_source homogeneity [src: env_embedding_explorer]

## Other caveats in this report

- Several AlphaEarth locations flagged as potential institutional addresses are legitimate field research sites. [src: env_embedding_explorer]
- The report calls the coordinate-quality heuristic a rough first pass and recommends distinguishing homogeneous isolation sources at real sites from diverse unrelated sources at institutions. [src: env_embedding_explorer]
- Taxonomic clustering in the AlphaEarth UMAP is partially confounded with environment, with Campylobacterota predominantly gut-associated. [src: env_embedding_explorer]
- Of the AlphaEarth genomes, 3,838 have NaN in at least one embedding dimension. [src: env_embedding_explorer]
- In the isolation-source environment mapping, 17% of genomes remain Other and 12.5% are Unknown because isolation_source is missing or null. [src: env_embedding_explorer]
