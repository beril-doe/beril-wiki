---
type: "Finding"
description: "Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are rare (present in <=5% of strains), 41.3% are variable (5-95%), and only 7.5% are fixed (>=95%)."
finding_id: "amr_strain_variation--8ac8eced"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "51.3%", "what": "AMR gene-species occurrences that are rare", "unit": "", "denominator": "", "scope": "1,305 species, 180,025 genomes"}, {"value": "41.3%", "what": "occurrences that are variable", "unit": "", "denominator": "", "scope": ""}, {"value": "7.5%", "what": "occurrences that are fixed", "unit": "", "denominator": "", "scope": ""}]
caveat: "The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates such as K. pneumoniae, S. aureus and E. coli, and environmental species are underrepresented."
first_added: "2026-11-24"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Over half of AMR gene occurrences are rare within species

Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are rare (present in <=5% of strains), 41.3% are variable (5-95%), and only 7.5% are fixed (>=95%). [src: amr_strain_variation]

## Key figures

- **51.3%**: AMR gene-species occurrences that are rare (scope 1,305 species, 180,025 genomes) [src: amr_strain_variation]
- **41.3%**: occurrences that are variable [src: amr_strain_variation]
- **7.5%**: occurrences that are fixed [src: amr_strain_variation]

## Evidence

> Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are **rare** (present in <=5% of strains), 41.3% are **variable** (5-95%), and only 7.5% are **fixed** (>=95%). [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates such as K. pneumoniae, S. aureus and E. coli, and environmental species are underrepresented. [src: amr_strain_variation]

> The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for species like *K. pneumoniae*, *S. aureus*, and *E. coli*. Environmental species are underrepresented. [src: amr_strain_variation]

## Other caveats in this report

- Environment–AMR ecotype association testing is limited by metadata sparsity: 52.7% of genomes lack a classifiable isolation_source, and only 2 species meet within-species environmental diversity and strict expected-frequency criteria for chi-squared testing. [src: amr_strain_variation]
- The report cautions that underpowered environment–ecotype testing does not imply ecotypes are unrelated to environment. [src: amr_strain_variation]
- Escherichia coli was excluded from the AMR ecotype case studies because it exceeds the 500-genome computational cap. [src: amr_strain_variation]
- The report suggests the temporal null result reflects sparse and noisy NCBI BioSample collection dates rather than true absence of temporal trends, citing well-documented AMR expansions in Staphylococcus aureus and Klebsiella pneumoniae. [src: amr_strain_variation]
- The report states that near-universal core AMR genes (>=95% prevalence by definition) have near-zero Jaccard distances and little variance, suppressing distance-based metrics such as Mantel r and partially explaining their lower phylogenetic signal independently of biology. [src: amr_strain_variation]
