---
type: "Finding"
description: "The report detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827."
finding_id: "amr_strain_variation--065d36b5"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "1,517", "what": "resistance islands detected", "unit": "", "denominator": "", "scope": ""}, {"value": "705", "what": "species with islands", "unit": "", "denominator": "", "scope": ""}, {"value": "0.827", "what": "mean phi coefficient", "unit": "", "denominator": "", "scope": ""}]
caveat: "Co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy."
first_added: "2026-11-24"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Tightly co-occurring resistance islands are common across species

The report detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827. [src: amr_strain_variation]

## Key figures

- **1,517**: resistance islands detected [src: amr_strain_variation]
- **705**: species with islands [src: amr_strain_variation]
- **0.827**: mean phi coefficient [src: amr_strain_variation]

## Evidence

> We detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827 — indicating very tight co-occurrence within each island. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

Co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy. [src: amr_strain_variation]

> The co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy. [src: amr_strain_variation]

## Other caveats in this report

- Environment–AMR ecotype association testing is limited by metadata sparsity: 52.7% of genomes lack a classifiable isolation_source, and only 2 species meet within-species environmental diversity and strict expected-frequency criteria for chi-squared testing. [src: amr_strain_variation]
- The report cautions that underpowered environment–ecotype testing does not imply ecotypes are unrelated to environment. [src: amr_strain_variation]
- Escherichia coli was excluded from the AMR ecotype case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- The report suggests the temporal null result reflects sparse and noisy NCBI BioSample collection dates rather than true absence of temporal trends, citing well-documented AMR expansions in Staphylococcus aureus and Klebsiella pneumoniae. [src: amr_strain_variation]
- The report states that near-universal core AMR genes (>=95% prevalence by definition) have near-zero Jaccard distances and little variance, suppressing distance-based metrics such as Mantel r and partially explaining their lower phylogenetic signal independently of biology. [src: amr_strain_variation]
