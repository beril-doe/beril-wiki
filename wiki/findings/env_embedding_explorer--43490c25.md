---
type: "Finding"
description: "For human-associated samples (gut, clinical, other), the AlphaEarth gradient is flatter: 0.37 nearby to 0.75 far, only a 2.0x ratio."
finding_id: "env_embedding_explorer--43490c25"
result: "observation"
source: "env_embedding_explorer"
quantities: [{"value": "0.37", "what": "mean cosine distance nearby", "unit": "", "denominator": "", "scope": "human-associated samples"}, {"value": "0.75", "what": "mean cosine distance far", "unit": "", "denominator": "", "scope": "human-associated samples"}, {"value": "2.0x", "what": "ratio of far to near", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 38% clinical/human bias in the AlphaEarth subset may not represent the overall NCBI or pangenome population."
first_added: "2026-11-24"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Human-associated genomes show a flatter embedding distance gradient

For human-associated samples (gut, clinical, other), the AlphaEarth gradient is flatter: 0.37 nearby to 0.75 far, only a 2.0x ratio. [src: env_embedding_explorer]

## Key figures

- **0.37**: mean cosine distance nearby (scope human-associated samples) [src: env_embedding_explorer]
- **0.75**: mean cosine distance far (scope human-associated samples) [src: env_embedding_explorer]
- **2.0x**: ratio of far to near [src: env_embedding_explorer]

## Evidence

> For **human-associated samples** (gut, clinical, other), the gradient is flatter: 0.37 nearby to 0.75 far — only a **2.0x ratio**. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The 38% clinical/human bias in the AlphaEarth subset may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]

> - **Clinical/human bias (38%)** may not represent the overall NCBI or pangenome population [src: env_embedding_explorer]

## Other caveats in this report

- Several AlphaEarth locations flagged as potential institutional addresses are legitimate field research sites. [src: env_embedding_explorer]
- The report calls the coordinate-quality heuristic a rough first pass and recommends distinguishing homogeneous isolation sources at real sites from diverse unrelated sources at institutions. [src: env_embedding_explorer]
- Taxonomic clustering in the AlphaEarth UMAP is partially confounded with environment, with Campylobacterota predominantly gut-associated. [src: env_embedding_explorer]
- Of the AlphaEarth genomes, 3,838 have NaN in at least one embedding dimension. [src: env_embedding_explorer]
- In the isolation-source environment mapping, 17% of genomes remain Other and 12.5% are Unknown because isolation_source is missing or null. [src: env_embedding_explorer]
