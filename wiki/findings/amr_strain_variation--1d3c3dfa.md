---
type: "Finding"
description: "Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction."
finding_id: "amr_strain_variation--1d3c3dfa"
result: "null result"
source: "amr_strain_variation"
quantities: [{"value": "513", "what": "Species tested for temporal trend in AMR gene count", "unit": "species", "denominator": "", "scope": ">=20 genomes spanning >=3 years, post-1990"}]
caveat: "The null result likely reflects sparse and noisy collection date metadata in NCBI BioSample records rather than a true absence of temporal trends."
first_added: "2026-10-27"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# No AMR gene-count temporal trend survives multiple-testing correction

Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation]

## Key figures

- **513 species**: Species tested for temporal trend in AMR gene count (scope >=20 genomes spanning >=3 years, post-1990) [src: amr_strain_variation]

## Evidence

> Of 513 species with >=20 genomes spanning >=3 years (post-1990), none show significant temporal trends in AMR gene count after Benjamini-Hochberg FDR correction. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

The null result likely reflects sparse and noisy collection date metadata in NCBI BioSample records rather than a true absence of temporal trends. [src: amr_strain_variation]

> This null result likely reflects sparse and noisy collection date metadata in NCBI BioSample records rather than a true absence of temporal trends, as demonstrated by well-documented AMR expansions in species like *S. aureus* and *K. pneumoniae*. [src: amr_strain_variation]

## Other caveats in this report

- Coordinated defense against multiple drug classes is an interpretation of island composition, not a directly demonstrated functional effect. [src: amr_strain_variation]
- The authors interpret stronger non-core phylogenetic signal as suggesting clonal inheritance after acquisition rather than random horizontal acquisition. [src: amr_strain_variation]
- Environmental testing of AMR ecotypes was limited: 52.7% of genomes lacked a classifiable isolation_source, leaving only 2 species eligible for chi-squared tests under the stated criteria. [src: amr_strain_variation]
- Visual environmental structuring in three case-study species did not establish a statistically supported environment–ecotype association; the report describes the test as underpowered. [src: amr_strain_variation]
- Stable integration and vertical inheritance after acquisition are proposed as a model, not directly established by the reported Mantel associations. [src: amr_strain_variation]
