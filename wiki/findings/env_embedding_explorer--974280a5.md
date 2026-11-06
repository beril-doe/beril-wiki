---
type: "Finding"
description: "For environmental samples (Soil, Marine, Freshwater, Extreme, Plant), mean AlphaEarth cosine distance rises from 0.27 for nearby genomes (<100 km) to 0.90 at intercontinental distances (>10,000 km), a 3.4x ratio, whereas human-associated samples (gut, clinical, other) rise from 0.37 to 0.75, only a 2.0x ratio."
finding_id: "env_embedding_explorer--974280a5"
result: "observation"
source: "env_embedding_explorer"
quantities: [{"value": "3.4x", "what": "ratio of far to near mean cosine distance, environmental samples", "unit": "ratio", "denominator": "", "scope": "<100 km vs >10,000 km; Soil, Marine, Freshwater, Extreme, Plant"}, {"value": "2.0x", "what": "ratio of far to near mean cosine distance, human-associated samples", "unit": "ratio", "denominator": "", "scope": "<100 km vs >10,000 km; gut, clinical, other"}, {"value": "0.27", "what": "mean cosine distance for nearby environmental genomes", "unit": "cosine distance", "denominator": "", "scope": "<100 km"}, {"value": "0.90", "what": "mean cosine distance for environmental genomes at intercontinental distance", "unit": "cosine distance", "denominator": "", "scope": ">10,000 km"}]
caveat: "The report attributes the flatter human gradient to hospitals sharing similar urban satellite imagery, and notes the pooled 2.0x curve blends two signals and is dominated by the 38% human-associated fraction."
first_added: "2026-10-27"
source_hash: "9d8367c2702227ec806ff62e384e9178954f1455f3826dafd569baa34a61a76f"
---
# Geographic gradient in embeddings is stronger for environmental than human-associated samples

For environmental samples (Soil, Marine, Freshwater, Extreme, Plant), mean AlphaEarth cosine distance rises from 0.27 for nearby genomes (<100 km) to 0.90 at intercontinental distances (>10,000 km), a 3.4x ratio, whereas human-associated samples (gut, clinical, other) rise from 0.37 to 0.75, only a 2.0x ratio. [src: env_embedding_explorer]

## Key figures

- **3.4x ratio**: ratio of far to near mean cosine distance, environmental samples (scope <100 km vs >10,000 km; Soil, Marine, Freshwater, Extreme, Plant) [src: env_embedding_explorer]
- **2.0x ratio**: ratio of far to near mean cosine distance, human-associated samples (scope <100 km vs >10,000 km; gut, clinical, other) [src: env_embedding_explorer]
- **0.27 cosine distance**: mean cosine distance for nearby environmental genomes (scope <100 km) [src: env_embedding_explorer]
- **0.90 cosine distance**: mean cosine distance for environmental genomes at intercontinental distance (scope >10,000 km) [src: env_embedding_explorer]

## Evidence

> AlphaEarth embeddings encode geographic/environmental signal, but the strength depends on the sample source. For **environmental samples** (Soil, Marine, Freshwater, Extreme, Plant), nearby genomes (<100 km) have mean cosine distance 0.27, rising to 0.90 at intercontinental distances (>10,000 km) — a **3.4x ratio**. For **human-associated samples** (gut, clinical, other), the gradient is flatter: 0.37 nearby to 0.75 far — only a **2.0x ratio**. [src: env_embedding_explorer]

From the report [[summaries/env_embedding_explorer__REPORT]].

## Caveat

The report attributes the flatter human gradient to hospitals sharing similar urban satellite imagery, and notes the pooled 2.0x curve blends two signals and is dominated by the 38% human-associated fraction. [src: env_embedding_explorer]

> This reflects the fact that hospitals and clinics worldwide share similar satellite imagery (urban built environment), so human-associated genomes have more homogeneous embeddings regardless of geography. Environmental samples, from genuinely diverse landscapes, show much stronger geographic differentiation. The pooled "All samples" curve (2.0x ratio) is a blend of these two signals, dominated by the 38% human-associated fraction. [src: env_embedding_explorer]

## Other caveats in this report

- The Other category contains 13,944 genomes (17%) and includes site-specific, generic, and clinical labels missed by keywords. [src: env_embedding_explorer]
- A shared-coordinate heuristic flags 30,469 genomes (36.6%) at locations with >50 genomes and >10 species, but includes legitimate field sites. [src: env_embedding_explorer]
- Examples of flagged coordinate clusters include legitimate field sites, a likely institutional location, and an approximately geolocated location. [src: env_embedding_explorer]
- Coordinate QC needs isolation-source homogeneity checks to distinguish field sites from institutional addresses. [src: env_embedding_explorer]
- Apparent taxonomic clustering in UMAP is partly confounded with environment; the report gives gut-associated Campylobacterota as an example. [src: env_embedding_explorer]
