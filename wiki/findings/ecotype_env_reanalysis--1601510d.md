---
type: "Finding"
description: "In the ecotype reanalysis, environmental species (n=37, median partial correlation 0.051) did not show stronger environment\u2013gene content correlations than human-associated species (n=93, median 0.084), with a one-sided Mann-Whitney U test of U=1536, p=0.83."
finding_id: "ecotype_env_reanalysis--1601510d"
result: "null result"
source: "ecotype_env_reanalysis"
quantities: [{"value": "0.051", "what": "median partial correlation, environmental species", "unit": "", "denominator": "", "scope": "n=37 species"}, {"value": "0.084", "what": "median partial correlation, human-associated species", "unit": "", "denominator": "", "scope": "n=93 species"}, {"value": "p=0.83", "what": "one-sided Mann-Whitney U test p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "Environmental species have a higher NaN exclusion rate (21%) than human-associated (7%), which would bias toward a stronger environmental signal, opposite to the observed result."
first_added: "2026-11-24"
source_hash: "db74961114a7aabd8fccc5e50114a3f44b684ffbdd661104a55c40c7fb4e3723"
---
# Environmental species show no stronger environment–gene content correlation than human-associated species

In the ecotype reanalysis, environmental species (n=37, median partial correlation 0.051) did not show stronger environment–gene content correlations than human-associated species (n=93, median 0.084), with a one-sided Mann-Whitney U test of U=1536, p=0.83. [src: ecotype_env_reanalysis]

## Key figures

- **0.051**: median partial correlation, environmental species (scope n=37 species) [src: ecotype_env_reanalysis]
- **0.084**: median partial correlation, human-associated species (scope n=93 species) [src: ecotype_env_reanalysis]
- **p=0.83**: one-sided Mann-Whitney U test p-value [src: ecotype_env_reanalysis]

## Evidence

> Environmental species (n=37, median partial correlation 0.051) do NOT show stronger environment–gene content correlations than human-associated species (n=93, median 0.084). The Mann-Whitney U test is far from significant (U=1536, p=0.83, one-sided). [src: ecotype_env_reanalysis]

From the report [[summaries/ecotype_env_reanalysis__REPORT]].

## Caveat

Environmental species have a higher NaN exclusion rate (21%) than human-associated (7%), which would bias toward a stronger environmental signal, opposite to the observed result. [src: ecotype_env_reanalysis]

> - **NaN exclusion**: Environmental species have a higher NaN rate (21%) than human-associated (7%), meaning the environmental group is more filtered. This would bias toward finding a stronger signal in the environmental group if anything — the opposite of what we observe. [src: ecotype_env_reanalysis]

## Other caveats in this report

- The report states that disproportionately losing environmental species to NaN could slightly bias the comparison, but addressing this bias would only strengthen the null result. [src: ecotype_env_reanalysis]
- The report states that larger genome sample sizes detect weaker correlations. [src: ecotype_env_reanalysis]
- The report states that omitting genome downsampling changes distance distributions. [src: ecotype_env_reanalysis]
- The report states that the 27x difference in partial correlations changes absolute magnitude but does not invalidate the environmental versus human-associated comparison because both groups use the same methodology. [src: ecotype_env_reanalysis]
- The report proposes that geographically differentiated environmental embeddings may capture climate, vegetation, and land-use variation that does not strongly predict bacterial gene content. [src: ecotype_env_reanalysis]
