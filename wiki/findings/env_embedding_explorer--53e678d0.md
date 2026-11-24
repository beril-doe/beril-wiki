---
type: "Finding"
description: "The report concludes that AlphaEarth embeddings are most informative for environmental microbiology samples and least informative for clinical isolates."
finding_id: "env_embedding_explorer--53e678d0"
result: "inference"
source: "env_embedding_explorer"
quantities: []
caveat: "AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid lat/lon metadata."
first_added: "2026-11-24"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Embeddings are most informative for environmental samples, least for clinical isolates

The report concludes that AlphaEarth embeddings are most informative for environmental microbiology samples and least informative for clinical isolates. [src: env_embedding_explorer]

## Evidence

> This has practical implications: the embeddings are most informative for environmental microbiology samples and least informative for clinical isolates. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

AlphaEarth coverage is only 28.4% of all genomes and is biased toward genomes with valid lat/lon metadata. [src: env_embedding_explorer]

> - **AlphaEarth coverage is only 28.4%** of all genomes — biased toward those with valid lat/lon metadata [src: env_embedding_explorer]

## Other caveats in this report

- Several AlphaEarth locations flagged as potential institutional addresses are legitimate field research sites. [src: env_embedding_explorer]
- The report calls the coordinate-quality heuristic a rough first pass and recommends distinguishing homogeneous isolation sources at real sites from diverse unrelated sources at institutions. [src: env_embedding_explorer]
- Taxonomic clustering in the AlphaEarth UMAP is partially confounded with environment, with Campylobacterota predominantly gut-associated. [src: env_embedding_explorer]
- Of the AlphaEarth genomes, 3,838 have NaN in at least one embedding dimension. [src: env_embedding_explorer]
- In the isolation-source environment mapping, 17% of genomes remain Other and 12.5% are Unknown because isolation_source is missing or null. [src: env_embedding_explorer]
