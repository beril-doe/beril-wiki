---
type: "Finding"
description: "Non-core (putatively acquired) AMR genes show stronger phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a highly significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489)."
finding_id: "amr_strain_variation--e349ed14"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "0.222", "what": "median Mantel r for non-core AMR genes", "unit": "", "denominator": "", "scope": ""}, {"value": "0.117", "what": "median Mantel r for core AMR genes", "unit": "", "denominator": "", "scope": ""}, {"value": "n = 489", "what": "species in paired test", "unit": "", "denominator": "", "scope": ""}]
caveat: "Core AMR genes are nearly universal (>=95% prevalence by definition), so they have near-zero Jaccard distances and little variance, which suppresses Mantel r as a statistical artifact independent of biology."
first_added: "2026-11-24"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Acquired AMR genes show stronger phylogenetic signal than intrinsic ones

Non-core (putatively acquired) AMR genes show stronger phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a highly significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489). [src: amr_strain_variation]

## Key figures

- **0.222**: median Mantel r for non-core AMR genes [src: amr_strain_variation]
- **0.117**: median Mantel r for core AMR genes [src: amr_strain_variation]
- **n = 489**: species in paired test [src: amr_strain_variation]

## Evidence

> Counter-intuitively, non-core (putatively acquired) AMR genes show **stronger** phylogenetic signal (median r = 0.222) than core (intrinsic) genes (median r = 0.117), with a highly significant difference (paired t-test: t = -8.35, p = 7.0e-16, n = 489). [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

Core AMR genes are nearly universal (>=95% prevalence by definition), so they have near-zero Jaccard distances and little variance, which suppresses Mantel r as a statistical artifact independent of biology. [src: amr_strain_variation]

> Core AMR genes, being nearly universal (>=95% prevalence by definition), have near-zero Jaccard distances with little variance, which inherently suppresses distance-based correlation metrics like the Mantel r — a statistical artifact that partially explains the lower signal, independent of biology. [src: amr_strain_variation]

## Other caveats in this report

- Environment–AMR ecotype association testing is limited by metadata sparsity: 52.7% of genomes lack a classifiable isolation_source, and only 2 species meet within-species environmental diversity and strict expected-frequency criteria for chi-squared testing. [src: amr_strain_variation]
- The report cautions that underpowered environment–ecotype testing does not imply ecotypes are unrelated to environment. [src: amr_strain_variation]
- Escherichia coli was excluded from the AMR ecotype case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- The report suggests the temporal null result reflects sparse and noisy NCBI BioSample collection dates rather than true absence of temporal trends, citing well-documented AMR expansions in Staphylococcus aureus and Klebsiella pneumoniae. [src: amr_strain_variation]
- The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly Klebsiella pneumoniae, Staphylococcus aureus, and Escherichia coli, while environmental species are underrepresented. [src: amr_strain_variation]
