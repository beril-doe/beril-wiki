---
type: "Finding"
description: "Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction."
finding_id: "amr_strain_variation--1d3c3dfa"
result: "null result"
source: "amr_strain_variation"
quantities: [{"value": "513", "what": "species tested", "unit": "", "denominator": "", "scope": ""}]
caveat: "The null result is likely driven by incomplete NCBI BioSample collection date metadata, with only 70% of genomes having parseable dates."
first_added: "2026-11-24"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# No significant temporal trends in AMR gene count

Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation]

## Key figures

- **513**: species tested [src: amr_strain_variation]

## Evidence

> Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

The null result is likely driven by incomplete NCBI BioSample collection date metadata, with only 70% of genomes having parseable dates. [src: amr_strain_variation]

> The null temporal result is likely driven by incomplete collection date metadata in NCBI BioSample records. Only 70% of genomes had parseable dates. [src: amr_strain_variation]

## Other caveats in this report

- Environment–AMR ecotype association testing is limited by metadata sparsity: 52.7% of genomes lack a classifiable isolation_source, and only 2 species meet within-species environmental diversity and strict expected-frequency criteria for chi-squared testing. [src: amr_strain_variation]
- The report cautions that underpowered environment–ecotype testing does not imply ecotypes are unrelated to environment. [src: amr_strain_variation]
- Escherichia coli was excluded from the AMR ecotype case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- The report suggests the temporal null result reflects sparse and noisy NCBI BioSample collection dates rather than true absence of temporal trends, citing well-documented AMR expansions in Staphylococcus aureus and Klebsiella pneumoniae. [src: amr_strain_variation]
- The report states that near-universal core AMR genes (>=95% prevalence by definition) have near-zero Jaccard distances and little variance, suppressing distance-based metrics such as Mantel r and partially explaining their lower phylogenetic signal independently of biology. [src: amr_strain_variation]
