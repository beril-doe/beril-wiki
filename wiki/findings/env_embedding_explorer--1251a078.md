---
type: "Finding"
description: "Across 50,000 sampled genome pairs with good-quality coordinates, embedding cosine distance increases monotonically with geographic distance, most strongly below 2,000 km and plateauing beyond 5,000 km, which the report suggests reflects spatially autocorrelated local environmental conditions."
finding_id: "env_embedding_explorer--1251a078"
result: "observation"
source: "env_embedding_explorer"
quantities: [{"value": "50,000", "what": "sampled genome pairs", "unit": "pairs", "denominator": "", "scope": "good-quality coordinates only"}, {"value": "<2,000 km", "what": "distance range where the relationship is strongest", "unit": "km", "denominator": "", "scope": ""}, {"value": ">5,000 km", "what": "distance beyond which the relationship plateaus", "unit": "km", "denominator": "", "scope": ""}]
caveat: "The coordinate quality filter relies on a heuristic flagging 30,469 genomes (36.6%) at shared coordinates with >50 genomes and >10 species, which also includes legitimate field sites."
first_added: "2026-10-27"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Embedding distance rises with geographic distance, then plateaus at intercontinental scales

Across 50,000 sampled genome pairs with good-quality coordinates, embedding cosine distance increases monotonically with geographic distance, most strongly below 2,000 km and plateauing beyond 5,000 km, which the report suggests reflects spatially autocorrelated local environmental conditions. [src: env_embedding_explorer]

## Key figures

- **50,000 pairs**: sampled genome pairs (scope good-quality coordinates only) [src: env_embedding_explorer]
- **<2,000 km**: distance range where the relationship is strongest [src: env_embedding_explorer]
- **>5,000 km**: distance beyond which the relationship plateaus [src: env_embedding_explorer]

## Evidence

> Across all 50,000 sampled genome pairs (using only good-quality coordinates), there is a clear monotonic relationship between geographic distance and embedding cosine distance. The relationship is strongest at short distances (<2,000 km) and plateaus at intercontinental scales (>5,000 km), suggesting the embeddings capture local environmental conditions (climate, vegetation, land use) that are spatially autocorrelated. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The coordinate quality filter relies on a heuristic flagging 30,469 genomes (36.6%) at shared coordinates with >50 genomes and >10 species, which also includes legitimate field sites. [src: env_embedding_explorer]

> 30,469 genomes (36.6%) cluster at shared coordinates with >50 genomes and >10 species — a heuristic for institutional addresses rather than sampling sites. However, several flagged locations are legitimate field research sites: [src: env_embedding_explorer]

## Other caveats in this report

- The report interprets the flatter human-associated gradient as an urban-imagery effect and cautions that the pooled 2.0x curve blends distinct groups. [src: env_embedding_explorer]
- The Other category contains 13,944 genomes (17%) and includes site-specific, generic, and clinical labels missed by keywords. [src: env_embedding_explorer]
- Examples of flagged coordinate clusters include legitimate field sites, a likely institutional location, and an approximately geolocated location. [src: env_embedding_explorer]
- Coordinate QC needs isolation-source homogeneity checks to distinguish field sites from institutional addresses. [src: env_embedding_explorer]
- Apparent taxonomic clustering in UMAP is partly confounded with environment; the report gives gut-associated Campylobacterota as an example. [src: env_embedding_explorer]
