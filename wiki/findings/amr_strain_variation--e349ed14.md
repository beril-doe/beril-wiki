---
type: "Finding"
description: "Non-core (putatively acquired) AMR genes show stronger phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489)."
finding_id: "amr_strain_variation--e349ed14"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "0.222", "what": "Median Mantel r for non-core AMR genes", "unit": "", "denominator": "", "scope": "n = 489"}, {"value": "0.117", "what": "Median Mantel r for core AMR genes", "unit": "", "denominator": "", "scope": "n = 489"}, {"value": "7.0e-16", "what": "p-value of paired t-test, non-core vs core", "unit": "", "denominator": "", "scope": "t = -8.35, n = 489"}]
caveat: "Core AMR genes are nearly universal (>=95% prevalence by definition), so their near-zero Jaccard distances with little variance inherently suppress Mantel r, a statistical artifact that partially explains the lower signal independent of biology."
first_added: "2026-10-27"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Putatively acquired AMR genes show stronger phylogenetic signal than core genes

Non-core (putatively acquired) AMR genes show stronger phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489). [src: amr_strain_variation]

## Key figures

- **0.222**: Median Mantel r for non-core AMR genes (scope n = 489) [src: amr_strain_variation]
- **0.117**: Median Mantel r for core AMR genes (scope n = 489) [src: amr_strain_variation]
- **7.0e-16**: p-value of paired t-test, non-core vs core (scope t = -8.35, n = 489) [src: amr_strain_variation]

## Evidence

> Counter-intuitively, non-core (putatively acquired) AMR genes show **stronger** phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a highly significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489). [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

Core AMR genes are nearly universal (>=95% prevalence by definition), so their near-zero Jaccard distances with little variance inherently suppress Mantel r, a statistical artifact that partially explains the lower signal independent of biology. [src: amr_strain_variation]

> Core AMR genes, being nearly universal (>=95% prevalence by definition), have near-zero Jaccard distances with little variance, which inherently suppresses distance-based correlation metrics like the Mantel r — a statistical artifact that partially explains the lower signal, independent of biology. [src: amr_strain_variation]

## Other caveats in this report

- Coordinated defense against multiple drug classes is an interpretation of island composition, not a directly demonstrated functional effect. [src: amr_strain_variation]
- The authors interpret stronger non-core phylogenetic signal as suggesting clonal inheritance after acquisition rather than random horizontal acquisition. [src: amr_strain_variation]
- Environmental testing of AMR ecotypes was limited: 52.7% of genomes lacked a classifiable isolation_source, leaving only 2 species eligible for chi-squared tests under the stated criteria. [src: amr_strain_variation]
- Visual environmental structuring in three case-study species did not establish a statistically supported environment–ecotype association; the report describes the test as underpowered. [src: amr_strain_variation]
- The report cautions that sparse, noisy NCBI BioSample dates may explain the corrected temporal null result; it is not evidence that temporal trends are absent. [src: amr_strain_variation]
