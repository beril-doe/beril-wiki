---
type: "Finding"
description: "Within-biome Mann-Whitney tests found no significant difference in total bacterial CAZyme counts between isolate and MAG genome types (all Cohen's d < 0.21), which the report treats as validating that MAG incompleteness does not drive biome patterns."
finding_id: "cazyme_pangenome_ecology--d2c37a63"
result: "null result"
source: "cazyme_pangenome_ecology"
quantities: [{"value": "0.21", "what": "upper bound on Cohen's d across biomes", "unit": "", "denominator": "", "scope": ""}]
caveat: "Incomplete MAGs may still undercount CAZymes in absolute terms."
first_added: "2026-11-24"
source_hash: "1ce54ec75c76a907e66fb3384355bc52bed7225dc2b7b0ae857f63fc93273712"
---
# No isolate-versus-MAG difference in CAZyme counts within biomes

Within-biome Mann-Whitney tests found no significant difference in total bacterial CAZyme counts between isolate and MAG genome types (all Cohen's d < 0.21), which the report treats as validating that MAG incompleteness does not drive biome patterns. [src: cazyme_pangenome_ecology]

## Key figures

- **0.21**: upper bound on Cohen's d across biomes [src: cazyme_pangenome_ecology]

## Evidence

> Within-biome Mann-Whitney tests show no significant difference in total CAZyme counts between Isolate and MAG genome types (all Cohen's d < 0.21), validating that MAG incompleteness does not drive the observed biome patterns. [src: cazyme_pangenome_ecology]

From the report [[summaries/cazyme_pangenome_ecology__REPORT]].

## Caveat

Incomplete MAGs may still undercount CAZymes in absolute terms. [src: cazyme_pangenome_ecology]

> While we found no systematic Isolate-vs-MAG bias within biomes (Cohen's d < 0.21), incomplete MAGs may still undercount CAZymes in absolute terms. [src: cazyme_pangenome_ecology]

## Other caveats in this report

- In the bacterial CAZyme–pangenome analysis, genome_count severely confounded cloud_fraction (ρ = 0.913), indicating that much apparent openness reflects sampling effort rather than biology. [src: cazyme_pangenome_ecology]
- In the report's bacterial dataset, genome_count and cloud_fraction correlate at ρ = 0.913, making pangenome openness largely a sampling artifact and limiting biological interpretation. [src: cazyme_pangenome_ecology]
- The report presents the genome_count → cloud_fraction correlation of ρ = 0.913 as a methodological caution for pangenome openness studies using MGnify-scale catalogs. [src: cazyme_pangenome_ecology]
- The kescience_mgnify.genome_cazy dataset provides only 7 top-level CAZy classes, GH, GT, PL, CE, AA, CB, and CL, rather than individual CAZy families. [src: cazyme_pangenome_ecology]
- The report states that finer CAZyme substrate-specificity analysis would require arkinlab_dbcan, which contains only 1,161 MGnify genomes, or 2.3% of the catalog. [src: cazyme_pangenome_ecology]
