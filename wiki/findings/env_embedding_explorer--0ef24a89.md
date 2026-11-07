---
type: "Finding"
description: "Of the 83,287 genomes with AlphaEarth embeddings, 38% are human-associated (Human clinical 16,390; 20%, Human gut 13,466; 16%, Human other 1,669; 2%), while Soil (6,073; 7%), Marine (5,850; 7%) and Freshwater (5,840; 7%) are much smaller, which the report attributes to NCBI pathogen-sequencing bias and good clinical geographic metadata."
finding_id: "env_embedding_explorer--0ef24a89"
result: "observation"
source: "env_embedding_explorer"
quantities: [{"value": "38%", "what": "share of embedded genomes that are human-associated", "unit": "%", "denominator": "83,287 genomes with AlphaEarth embeddings", "scope": ""}, {"value": "16,390", "what": "Human clinical genomes", "unit": "genomes", "denominator": "83,287 genomes with AlphaEarth embeddings", "scope": "20%"}, {"value": "6,073", "what": "Soil genomes", "unit": "genomes", "denominator": "83,287 genomes with AlphaEarth embeddings", "scope": "7%"}]
caveat: "The 38% clinical/human bias may not represent the overall NCBI or pangenome population."
first_added: "2026-10-27"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Embedded genomes are heavily skewed toward human-associated sources

Of the 83,287 genomes with AlphaEarth embeddings, 38% are human-associated (Human clinical 16,390; 20%, Human gut 13,466; 16%, Human other 1,669; 2%), while Soil (6,073; 7%), Marine (5,850; 7%) and Freshwater (5,840; 7%) are much smaller, which the report attributes to NCBI pathogen-sequencing bias and good clinical geographic metadata. [src: env_embedding_explorer]

## Key figures

- **38%**: share of embedded genomes that are human-associated (denominator 83,287 genomes with AlphaEarth embeddings) [src: env_embedding_explorer]
- **16,390 genomes**: Human clinical genomes (denominator 83,287 genomes with AlphaEarth embeddings; scope 20%) [src: env_embedding_explorer]
- **6,073 genomes**: Soil genomes (denominator 83,287 genomes with AlphaEarth embeddings; scope 7%) [src: env_embedding_explorer]

## Evidence

> 38% of the 83,287 genomes with AlphaEarth embeddings are human-associated: Human clinical (16,390; 20%), Human gut (13,466; 16%), and Human other (1,669; 2%). Environmental categories are much smaller: Soil (6,073; 7%), Marine (5,850; 7%), Freshwater (5,840; 7%). This reflects NCBI's overall bias toward pathogen sequencing — clinical isolates tend to have good geographic metadata from epidemiological tracking, which is why they have AlphaEarth embeddings. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The 38% clinical/human bias may not represent the overall NCBI or pangenome population. [src: env_embedding_explorer]

> - **Clinical/human bias (38%)** may not represent the overall NCBI or pangenome population [src: env_embedding_explorer]

## Other caveats in this report

- The report interprets the flatter human-associated gradient as an urban-imagery effect and cautions that the pooled 2.0x curve blends distinct groups. [src: env_embedding_explorer]
- The Other category contains 13,944 genomes (17%) and includes site-specific, generic, and clinical labels missed by keywords. [src: env_embedding_explorer]
- A shared-coordinate heuristic flags 30,469 genomes (36.6%) at locations with >50 genomes and >10 species, but includes legitimate field sites. [src: env_embedding_explorer]
- Examples of flagged coordinate clusters include legitimate field sites, a likely institutional location, and an approximately geolocated location. [src: env_embedding_explorer]
- Coordinate QC needs isolation-source homogeneity checks to distinguish field sites from institutional addresses. [src: env_embedding_explorer]
