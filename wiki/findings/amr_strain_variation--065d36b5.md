---
type: "Finding"
description: "The analysis detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827, indicating very tight co-occurrence within each island."
finding_id: "amr_strain_variation--065d36b5"
result: "observation"
source: "amr_strain_variation"
quantities: [{"value": "1,517", "what": "Resistance islands detected", "unit": "islands", "denominator": "", "scope": "705 species"}, {"value": "54%", "what": "Share of analyzed species with resistance islands", "unit": "%", "denominator": "species analyzed", "scope": "705 species"}, {"value": "6.2", "what": "Mean island size", "unit": "genes", "denominator": "", "scope": "median 4, max 43"}, {"value": "0.827", "what": "Mean phi coefficient within islands", "unit": "", "denominator": "", "scope": ""}]
caveat: "Co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy."
first_added: "2026-10-27"
source_hash: "281555811f8881723be3df2451fb1922ac3608fa2659d910741acb7a97cfcc9c"
---
# Tightly co-occurring resistance islands are detected in over half of species

The analysis detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827, indicating very tight co-occurrence within each island. [src: amr_strain_variation]

## Key figures

- **1,517 islands**: Resistance islands detected (scope 705 species) [src: amr_strain_variation]
- **54%**: Share of analyzed species with resistance islands (denominator species analyzed; scope 705 species) [src: amr_strain_variation]
- **6.2 genes**: Mean island size (scope median 4, max 43) [src: amr_strain_variation]
- **0.827**: Mean phi coefficient within islands [src: amr_strain_variation]

## Evidence

> We detected 1,517 resistance islands across 705 species (54% of those analyzed), with a mean island size of 6.2 genes (median 4, max 43) and a mean phi coefficient of 0.827 — indicating very tight co-occurrence within each island. [src: amr_strain_variation]

From the report [[summaries/amr_strain_variation__REPORT]].

## Caveat

Co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy. [src: amr_strain_variation]

> - **Causality**: The co-occurrence of AMR genes in islands does not prove co-selection; it may reflect linkage on the same mobile element without functional synergy. [src: amr_strain_variation]

## Other caveats in this report

- Coordinated defense against multiple drug classes is an interpretation of island composition, not a directly demonstrated functional effect. [src: amr_strain_variation]
- The authors interpret stronger non-core phylogenetic signal as suggesting clonal inheritance after acquisition rather than random horizontal acquisition. [src: amr_strain_variation]
- Environmental testing of AMR ecotypes was limited: 52.7% of genomes lacked a classifiable isolation_source, leaving only 2 species eligible for chi-squared tests under the stated criteria. [src: amr_strain_variation]
- Visual environmental structuring in three case-study species did not establish a statistically supported environment–ecotype association; the report describes the test as underpowered. [src: amr_strain_variation]
- The report cautions that sparse, noisy NCBI BioSample dates may explain the corrected temporal null result; it is not evidence that temporal trends are absent. [src: amr_strain_variation]
