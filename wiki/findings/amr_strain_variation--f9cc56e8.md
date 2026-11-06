---
type: "Finding"
description: "Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are rare (present in <=5% of strains), 41.3% are variable (5-95%), and only 7.5% are fixed (>=95%), with a median variability index of 0.526 and a median pairwise Jaccard distance between strains of 0.435."
finding_id: "amr_strain_variation--f9cc56e8"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "51.3%", "what": "AMR gene-species occurrences that are rare (present in <=5% of strains)", "unit": "%", "denominator": "AMR gene-species occurrences", "scope": "1,305 species, 180,025 genomes"}, {"value": "7.5%", "what": "AMR gene-species occurrences that are fixed (>=95%)", "unit": "%", "denominator": "AMR gene-species occurrences", "scope": "1,305 species, 180,025 genomes"}, {"value": "0.526", "what": "Median variability index", "unit": "", "denominator": "", "scope": "1,305 species"}, {"value": "0.435", "what": "Median pairwise Jaccard distance between strains within a species", "unit": "", "denominator": "", "scope": "1,305 species"}]
caveat: "The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for K. pneumoniae, S. aureus and E. coli, and environmental species are underrepresented."
first_added: "2026-10-27"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Most within-species AMR gene occurrences are rare or variable, rarely fixed

Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are rare (present in <=5% of strains), 41.3% are variable (5-95%), and only 7.5% are fixed (>=95%), with a median variability index of 0.526 and a median pairwise Jaccard distance between strains of 0.435. [src: amr_strain_variation]

## Key figures

- **51.3%**: AMR gene-species occurrences that are rare (present in <=5% of strains) (denominator AMR gene-species occurrences; scope 1,305 species, 180,025 genomes) [src: amr_strain_variation]
- **7.5%**: AMR gene-species occurrences that are fixed (>=95%) (denominator AMR gene-species occurrences; scope 1,305 species, 180,025 genomes) [src: amr_strain_variation]
- **0.526**: Median variability index (scope 1,305 species) [src: amr_strain_variation]
- **0.435**: Median pairwise Jaccard distance between strains within a species (scope 1,305 species) [src: amr_strain_variation]

## Evidence

> Across 1,305 species and 180,025 genomes, 51.3% of AMR gene-species occurrences are **rare** (present in <=5% of strains), 41.3% are **variable** (5-95%), and only 7.5% are **fixed** (>=95%). The median variability index is 0.526, meaning over half of a species' AMR genes fall in the variable zone. The median pairwise Jaccard distance between strains is 0.435, indicating that strains within the same species share less than 60% of their AMR repertoire. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for K. pneumoniae, S. aureus and E. coli, and environmental species are underrepresented. [src: amr_strain_variation]

> - **Collection bias**: The GTDB/NCBI genome collection is heavily biased toward clinical and human-associated isolates, particularly for species like *K. pneumoniae*, *S. aureus*, and *E. coli*. Environmental species are underrepresented. [src: amr_strain_variation]

## Other caveats in this report

- Coordinated defense against multiple drug classes is an interpretation of island composition, not a directly demonstrated functional effect. [src: amr_strain_variation]
- The authors interpret stronger non-core phylogenetic signal as suggesting clonal inheritance after acquisition rather than random horizontal acquisition. [src: amr_strain_variation]
- Environmental testing of AMR ecotypes was limited: 52.7% of genomes lacked a classifiable isolation_source, leaving only 2 species eligible for chi-squared tests under the stated criteria. [src: amr_strain_variation]
- Visual environmental structuring in three case-study species did not establish a statistically supported environment–ecotype association; the report describes the test as underpowered. [src: amr_strain_variation]
- The report cautions that sparse, noisy NCBI BioSample dates may explain the corrected temporal null result; it is not evidence that temporal trends are absent. [src: amr_strain_variation]
