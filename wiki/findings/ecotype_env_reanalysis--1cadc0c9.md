---
type: "Finding"
description: "Although the parent env_embedding_explorer project reported a geographic-signal ratio of 3.4x for environmental versus 2.0x for human-associated embeddings, this reanalysis found no difference in environment\u2013gene content correlations between the groups."
finding_id: "ecotype_env_reanalysis--1cadc0c9"
result: "null result"
source: "ecotype_env_reanalysis"
quantities: [{"value": "3.4x", "what": "geographic-signal ratio of environmental species' embeddings", "unit": "ratio", "denominator": "", "scope": "from env_embedding_explorer"}, {"value": "2.0x", "what": "geographic-signal ratio of human-associated species' embeddings", "unit": "ratio", "denominator": "", "scope": "from env_embedding_explorer"}]
caveat: "The authors propose, without testing it here, that environmental embeddings may be more geographically differentiated yet capture climate, vegetation and land use that do not strongly predict bacterial gene content."
first_added: "2026-10-27"
source_hash: "db74961114a7aabd8fccc5e50114a3f44b684ffbdd661104a55c40c7fb4e3723"
---
# Greater geographic signal in environmental embeddings did not strengthen gene-content correlations

Although the parent env_embedding_explorer project reported a geographic-signal ratio of 3.4x for environmental versus 2.0x for human-associated embeddings, this reanalysis found no difference in environment–gene content correlations between the groups. [src: ecotype_env_reanalysis]

## Key figures

- **3.4x ratio**: geographic-signal ratio of environmental species' embeddings (scope from env_embedding_explorer) [src: ecotype_env_reanalysis]
- **2.0x ratio**: geographic-signal ratio of human-associated species' embeddings (scope from env_embedding_explorer) [src: ecotype_env_reanalysis]

## Evidence

> We predicted that environmental species would show stronger environment–gene content correlations because their AlphaEarth embeddings carry more geographic signal (3.4x ratio vs 2.0x for human-associated, from `env_embedding_explorer`). But the data shows no difference. [src: ecotype_env_reanalysis]

From the report [[summaries/ecotype_env_reanalysis__REPORT]].

## Caveat

The authors propose, without testing it here, that environmental embeddings may be more geographically differentiated yet capture climate, vegetation and land use that do not strongly predict bacterial gene content. [src: ecotype_env_reanalysis]

> 1. **Embedding similarity ≠ ecological relevance**: Environmental embeddings are more geographically differentiated, but the environmental variation they capture (climate, vegetation, land use) may not strongly predict which genes a bacterium has. [src: ecotype_env_reanalysis]

## Other caveats in this report

- Thirty species had NaN partial correlations. Reported NaN rates were Environmental 10/47 = 21%, Mixed/Other 13/66 = 20%, and Human-associated 7/100 = 7%. [src: ecotype_env_reanalysis]
- Environmental species are disproportionately excluded by NaN correlations, which the authors acknowledge could bias the group comparison; their stated direction of that bias is an interpretation, not a measured correction. [src: ecotype_env_reanalysis]
- The reanalysis used all genomes with embeddings, up to 3,505 per species, whereas the original used diversity-maximizing downsampling to a maximum of 250. [src: ecotype_env_reanalysis]
- The authors identify increased sample size and power as a possible contributor to the larger partial correlations. [src: ecotype_env_reanalysis]
- Omitting downsampling changes the genome sets and their distance distributions, limiting direct comparison with the original analysis. [src: ecotype_env_reanalysis]
