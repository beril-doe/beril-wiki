---
type: "Finding"
description: "The report hypothesizes that clinical bias may partially explain the weak environment\u2013gene content signal because if 38% of compared genomes are from interchangeable hospital environments, the relationship would be diluted."
finding_id: "env_embedding_explorer--2b7f8fd1"
result: "inference"
source: "env_embedding_explorer"
quantities: [{"value": "38%", "what": "genomes assumed from interchangeable hospital environments", "unit": "", "denominator": "", "scope": ""}]
caveat: "The 38% clinical/human bias in the AlphaEarth subset may not represent the overall NCBI or pangenome population."
first_added: "2026-11-24"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Clinical bias may explain weak environment–gene content signal

The report hypothesizes that clinical bias may partially explain the weak environment–gene content signal because if 38% of compared genomes are from interchangeable hospital environments, the relationship would be diluted. [src: env_embedding_explorer]

## Key figures

- **38%**: genomes assumed from interchangeable hospital environments [src: env_embedding_explorer]

## Evidence

> The strong clinical bias identified here may partially explain that weak signal — if 38% of the genomes being compared are from interchangeable hospital environments, the environment–gene content relationship would be diluted. [src: env_embedding_explorer]

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
