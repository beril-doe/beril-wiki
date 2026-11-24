---
type: "Finding"
description: "The fraction of environmental genomes per species did not predict partial correlation strength in the ecotype reanalysis (Spearman rho=-0.085, p=0.25)."
finding_id: "ecotype_env_reanalysis--34295080"
result: "null result"
source: "ecotype_env_reanalysis"
quantities: [{"value": "rho=-0.085", "what": "Spearman correlation of environmental genome fraction with partial correlation", "unit": "", "denominator": "", "scope": ""}, {"value": "p=0.25", "what": "p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Majority-vote classification labels a species with 51% gut genomes as human-associated; the report says the continuous Spearman analysis addresses this limitation and confirms the null result."
first_added: "2026-11-24"
source_hash: "db74961114a7aabd8fccc5e50114a3f44b684ffbdd661104a55c40c7fb4e3723"
---
# Environmental genome fraction does not predict partial correlation strength

The fraction of environmental genomes per species did not predict partial correlation strength in the ecotype reanalysis (Spearman rho=-0.085, p=0.25). [src: ecotype_env_reanalysis]

## Key figures

- **rho=-0.085**: Spearman correlation of environmental genome fraction with partial correlation [src: ecotype_env_reanalysis]
- **p=0.25**: p-value [src: ecotype_env_reanalysis]

## Evidence

> The continuous Spearman analysis confirms this: fraction of environmental genomes per species does not predict partial correlation strength (rho=-0.085, p=0.25). [src: ecotype_env_reanalysis]

From the report [[summaries/ecotype_env_reanalysis__REPORT]].

## Caveat

Majority-vote classification labels a species with 51% gut genomes as human-associated; the report says the continuous Spearman analysis addresses this limitation and confirms the null result. [src: ecotype_env_reanalysis]

> - **Classification by majority vote**: A species with 51% gut genomes is classified as "Human-associated." The continuous Spearman analysis addresses this limitation and confirms the null result. [src: ecotype_env_reanalysis]

## Other caveats in this report

- The report states that disproportionately losing environmental species to NaN could slightly bias the comparison, but addressing this bias would only strengthen the null result. [src: ecotype_env_reanalysis]
- The report states that larger genome sample sizes detect weaker correlations. [src: ecotype_env_reanalysis]
- The report states that omitting genome downsampling changes distance distributions. [src: ecotype_env_reanalysis]
- The report states that the 27x difference in partial correlations changes absolute magnitude but does not invalidate the environmental versus human-associated comparison because both groups use the same methodology. [src: ecotype_env_reanalysis]
- The report proposes that geographically differentiated environmental embeddings may capture climate, vegetation, and land-use variation that does not strongly predict bacterial gene content. [src: ecotype_env_reanalysis]
