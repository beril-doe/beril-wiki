---
type: "Finding"
description: "Mantel tests comparing ANI distance with AMR Jaccard distance across 1,261 species show that 55.6% (701 species) have significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247."
finding_id: "amr_strain_variation--6ebb7e8b"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "55.6%", "what": "species with significant signal", "unit": "", "denominator": "", "scope": "1,261 species"}, {"value": "701", "what": "species with significant signal", "unit": "", "denominator": "", "scope": ""}, {"value": "0.247", "what": "median Mantel r", "unit": "", "denominator": "", "scope": ""}]
caveat: "ANI extraction was limited to species with <=500 genomes, excluding E. coli (15,388 genomes) and K. pneumoniae (14,240 genomes) from the phylogenetic signal analysis."
first_added: "2026-11-24"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# AMR profiles track phylogeny in over half of species

Mantel tests comparing ANI distance with AMR Jaccard distance across 1,261 species show that 55.6% (701 species) have significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247. [src: amr_strain_variation]

## Key figures

- **55.6%**: species with significant signal (scope 1,261 species) [src: amr_strain_variation]
- **701**: species with significant signal [src: amr_strain_variation]
- **0.247**: median Mantel r [src: amr_strain_variation]

## Evidence

> Mantel tests comparing ANI distance matrices with AMR Jaccard distance matrices across 1,261 species reveal that 55.6% (701 species) show significant phylogenetic signal (FDR < 0.05), with a median Mantel r of 0.247 and 87.8% of species showing positive correlation. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

ANI extraction was limited to species with <=500 genomes, excluding E. coli (15,388 genomes) and K. pneumoniae (14,240 genomes) from the phylogenetic signal analysis. [src: amr_strain_variation]

> ANI extraction was limited to species with <=500 genomes for computational feasibility, excluding mega-species like *E. coli* (15,388 genomes) and *K. pneumoniae* (14,240 genomes) from the phylogenetic signal analysis. [src: amr_strain_variation]

## Other caveats in this report

- Environment–AMR ecotype association testing is limited by metadata sparsity: 52.7% of genomes lack a classifiable isolation_source, and only 2 species meet within-species environmental diversity and strict expected-frequency criteria for chi-squared testing. [src: amr_strain_variation]
- The report cautions that underpowered environment–ecotype testing does not imply ecotypes are unrelated to environment. [src: amr_strain_variation]
- Escherichia coli was excluded from the AMR ecotype case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- The report suggests the temporal null result reflects sparse and noisy NCBI BioSample collection dates rather than true absence of temporal trends, citing well-documented AMR expansions in Staphylococcus aureus and Klebsiella pneumoniae. [src: amr_strain_variation]
- The report states that near-universal core AMR genes (>=95% prevalence by definition) have near-zero Jaccard distances and little variance, suppressing distance-based metrics such as Mantel r and partially explaining their lower phylogenetic signal independently of biology. [src: amr_strain_variation]
