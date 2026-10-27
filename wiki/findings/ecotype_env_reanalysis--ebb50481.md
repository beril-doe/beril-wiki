---
type: "Finding"
description: "Of 224 species selected for the ecotype analysis (>=20 genomes with AlphaEarth embeddings, >=30% coverage), 106 (47%) are majority human-associated by genome-level isolation_source classification, 47 (21%) majority environmental, and 71 (32%) mixed/other."
finding_id: "ecotype_env_reanalysis--ebb50481"
result: "observation"
source: "ecotype_env_reanalysis"
quantities: [{"value": "106 (47%)", "what": "majority human-associated species", "unit": "species", "denominator": "224 selected species", "scope": "genome-level isolation_source majority classification"}, {"value": "47 (21%)", "what": "majority environmental species", "unit": "species", "denominator": "224 selected species", "scope": "Soil, Marine, Freshwater, Extreme, Plant"}, {"value": "71 (32%)", "what": "mixed/other species", "unit": "species", "denominator": "224 selected species", "scope": ""}]
caveat: "Majority-vote classification can label a species human-associated with only 51% gut genomes, though a continuous Spearman analysis was used to address this and confirmed the null."
first_added: "2026-10-27"
source_hash: "db74961114a7aabd8fccc5e50114a3f44b684ffbdd661104a55c40c7fb4e3723"
---
# Clinical sampling dominates species selected for the AlphaEarth ecotype analysis

Of 224 species selected for the ecotype analysis (>=20 genomes with AlphaEarth embeddings, >=30% coverage), 106 (47%) are majority human-associated by genome-level isolation_source classification, 47 (21%) majority environmental, and 71 (32%) mixed/other. [src: ecotype_env_reanalysis]

## Key figures

- **106 (47%) species**: majority human-associated species (denominator 224 selected species; scope genome-level isolation_source majority classification) [src: ecotype_env_reanalysis]
- **47 (21%) species**: majority environmental species (denominator 224 selected species; scope Soil, Marine, Freshwater, Extreme, Plant) [src: ecotype_env_reanalysis]
- **71 (32%) species**: mixed/other species (denominator 224 selected species) [src: ecotype_env_reanalysis]

## Evidence

> Of 224 species selected for the ecotype analysis (>=20 genomes with AlphaEarth embeddings, >=30% coverage), 106 (47%) are majority human-associated by genome-level isolation_source classification, 47 (21%) are majority environmental (Soil, Marine, Freshwater, Extreme, Plant), and 71 (32%) are mixed/other. [src: ecotype_env_reanalysis]

From the report [[summaries/ecotype_env_reanalysis__REPORT]].

## Caveat

Majority-vote classification can label a species human-associated with only 51% gut genomes, though a continuous Spearman analysis was used to address this and confirmed the null. [src: ecotype_env_reanalysis]

> - **Classification by majority vote**: A species with 51% gut genomes is classified as "Human-associated." The continuous Spearman analysis addresses this limitation and confirms the null result. [src: ecotype_env_reanalysis]

## Other caveats in this report

- Thirty species had NaN partial correlations. Reported NaN rates were Environmental 10/47 = 21%, Mixed/Other 13/66 = 20%, and Human-associated 7/100 = 7%. [src: ecotype_env_reanalysis]
- Environmental species are disproportionately excluded by NaN correlations, which the authors acknowledge could bias the group comparison; their stated direction of that bias is an interpretation, not a measured correction. [src: ecotype_env_reanalysis]
- The reanalysis used all genomes with embeddings, up to 3,505 per species, whereas the original used diversity-maximizing downsampling to a maximum of 250. [src: ecotype_env_reanalysis]
- The authors identify increased sample size and power as a possible contributor to the larger partial correlations. [src: ecotype_env_reanalysis]
- Omitting downsampling changes the genome sets and their distance distributions, limiting direct comparison with the original analysis. [src: ecotype_env_reanalysis]
