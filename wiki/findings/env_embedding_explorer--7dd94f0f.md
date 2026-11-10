---
type: "Finding"
description: "The earlier ecotype_analysis project found AlphaEarth-based environment similarity to be a weak predictor of gene content (median partial correlation 0.0025), and this report proposes, without demonstrating it, that the 38% clinical bias may have diluted the signal, suggesting a rerun restricted to environmental samples."
finding_id: "env_embedding_explorer--7dd94f0f"
result: "null result"
source: "env_embedding_explorer"
quantities: [{"value": "0.0025", "what": "median partial correlation between AlphaEarth environment similarity and gene content", "unit": "partial correlation", "denominator": "", "scope": "ecotype_analysis project"}]
caveat: "The 38% clinical/human composition may not represent the overall NCBI or pangenome population, so the dilution explanation is not established."
first_added: "2026-10-27"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Prior weak embedding-gene content link may reflect clinical dilution, untested here

The earlier ecotype_analysis project found AlphaEarth-based environment similarity to be a weak predictor of gene content (median partial correlation 0.0025), and this report proposes, without demonstrating it, that the 38% clinical bias may have diluted the signal, suggesting a rerun restricted to environmental samples. [src: env_embedding_explorer]

## Key figures

- **0.0025 partial correlation**: median partial correlation between AlphaEarth environment similarity and gene content (scope ecotype_analysis project) [src: env_embedding_explorer]

## Evidence

> The `ecotype_analysis` project previously found that AlphaEarth-based environment similarity was a weak predictor of gene content (median partial correlation 0.0025). The strong clinical bias identified here may partially explain that weak signal — if 38% of the genomes being compared are from interchangeable hospital environments, the environment–gene content relationship would be diluted. Repeating the ecotype analysis restricted to environmental samples could reveal a stronger signal. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The 38% clinical/human composition may not represent the overall NCBI or pangenome population, so the dilution explanation is not established. [src: env_embedding_explorer]

> - **Clinical/human bias (38%)** may not represent the overall NCBI or pangenome population [src: env_embedding_explorer]

## Other caveats in this report

- The report interprets the flatter human-associated gradient as an urban-imagery effect and cautions that the pooled 2.0x curve blends distinct groups. [src: env_embedding_explorer]
- The Other category contains 13,944 genomes (17%) and includes site-specific, generic, and clinical labels missed by keywords. [src: env_embedding_explorer]
- A shared-coordinate heuristic flags 30,469 genomes (36.6%) at locations with >50 genomes and >10 species, but includes legitimate field sites. [src: env_embedding_explorer]
- Examples of flagged coordinate clusters include legitimate field sites, a likely institutional location, and an approximately geolocated location. [src: env_embedding_explorer]
- Coordinate QC needs isolation-source homogeneity checks to distinguish field sites from institutional addresses. [src: env_embedding_explorer]
