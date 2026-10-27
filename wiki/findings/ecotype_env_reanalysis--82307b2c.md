---
type: "Finding"
description: "Environmental species (n=37, median partial correlation 0.051) did not show stronger environment\u2013gene content correlations than human-associated species (n=93, median 0.084); the one-sided Mann-Whitney U test gave U=1536, p=0.83, in the opposite direction from the hypothesis."
finding_id: "ecotype_env_reanalysis--82307b2c"
result: "null result"
source: "ecotype_env_reanalysis"
quantities: [{"value": "0.051", "what": "median partial correlation, environmental species", "unit": "partial correlation", "denominator": "", "scope": "n=37 species"}, {"value": "0.084", "what": "median partial correlation, human-associated species", "unit": "partial correlation", "denominator": "", "scope": "n=93 species"}, {"value": "U=1536, p=0.83", "what": "one-sided Mann-Whitney U test, environmental vs human-associated", "unit": "", "denominator": "", "scope": ""}]
caveat: "Environmental species have a higher NaN rate (21%) than human-associated (7%), so the environmental group is more filtered; the authors argue this would if anything favor a stronger environmental signal, but that bias direction was not directly tested."
first_added: "2026-10-27"
source_hash: "db74961114a7aabd8fccc5e50114a3f44b684ffbdd661104a55c40c7fb4e3723"
---
# Environmental species show no stronger environment–gene-content correlation than human-associated species

Environmental species (n=37, median partial correlation 0.051) did not show stronger environment–gene content correlations than human-associated species (n=93, median 0.084); the one-sided Mann-Whitney U test gave U=1536, p=0.83, in the opposite direction from the hypothesis. [src: ecotype_env_reanalysis]

## Key figures

- **0.051 partial correlation**: median partial correlation, environmental species (scope n=37 species) [src: ecotype_env_reanalysis]
- **0.084 partial correlation**: median partial correlation, human-associated species (scope n=93 species) [src: ecotype_env_reanalysis]
- **U=1536, p=0.83**: one-sided Mann-Whitney U test, environmental vs human-associated [src: ecotype_env_reanalysis]

## Evidence

> Environmental species (n=37, median partial correlation 0.051) do NOT show stronger environment–gene content correlations than human-associated species (n=93, median 0.084). The Mann-Whitney U test is far from significant (U=1536, p=0.83, one-sided). The result is the **opposite direction** from the hypothesis: human-associated species actually show slightly higher partial correlations. [src: ecotype_env_reanalysis]

From the report [[summaries/ecotype_env_reanalysis__REPORT]].

## Caveat

Environmental species have a higher NaN rate (21%) than human-associated (7%), so the environmental group is more filtered; the authors argue this would if anything favor a stronger environmental signal, but that bias direction was not directly tested. [src: ecotype_env_reanalysis]

> - **NaN exclusion**: Environmental species have a higher NaN rate (21%) than human-associated (7%), meaning the environmental group is more filtered. This would bias toward finding a stronger signal in the environmental group if anything — the opposite of what we observe. [src: ecotype_env_reanalysis]

## Other caveats in this report

- Thirty species had NaN partial correlations. Reported NaN rates were Environmental 10/47 = 21%, Mixed/Other 13/66 = 20%, and Human-associated 7/100 = 7%. [src: ecotype_env_reanalysis]
- Environmental species are disproportionately excluded by NaN correlations, which the authors acknowledge could bias the group comparison; their stated direction of that bias is an interpretation, not a measured correction. [src: ecotype_env_reanalysis]
- The reanalysis used all genomes with embeddings, up to 3,505 per species, whereas the original used diversity-maximizing downsampling to a maximum of 250. [src: ecotype_env_reanalysis]
- The authors identify increased sample size and power as a possible contributor to the larger partial correlations. [src: ecotype_env_reanalysis]
- Omitting downsampling changes the genome sets and their distance distributions, limiting direct comparison with the original analysis. [src: ecotype_env_reanalysis]
