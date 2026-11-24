---
type: "Finding"
description: "Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction."
finding_id: "acinetobacter_adp1_explorer--2c5f48a7"
result: "observation"
source: "acinetobacter_adp1_explorer"
quantities: [{"value": "105,376", "what": "predictions requiring at least one gapfilled reaction", "unit": "predictions", "denominator": "121,519 growth phenotype predictions", "scope": "14 Acinetobacter genomes"}, {"value": "87%", "what": "fraction requiring gapfilling", "unit": "percent", "denominator": "121,519 predictions", "scope": "14 genomes"}]
caveat: "This heavy dependence on gapfilling means that prediction accuracy is tightly coupled to gapfilling quality."
first_added: "2026-11-24"
source_hash: "ec7429b1cf2b99caae21a458ffae48609efc6384c9a4b7e3a9b1385d70024218"
---
# Most Acinetobacter growth predictions depend on gapfilled reactions

Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction. [src: acinetobacter_adp1_explorer]

## Key figures

- **105,376 predictions**: predictions requiring at least one gapfilled reaction (denominator 121,519 growth phenotype predictions; scope 14 Acinetobacter genomes) [src: acinetobacter_adp1_explorer]
- **87%**: fraction requiring gapfilling (denominator 121,519 predictions; scope 14 genomes) [src: acinetobacter_adp1_explorer]

## Evidence

> Of 121,519 growth phenotype predictions across 14 genomes, 105,376 (87%) require at least one gapfilled reaction. [src: acinetobacter_adp1_explorer]

From the report [[summaries/acinetobacter_adp1_explorer__REPORT]].

## Caveat

This heavy dependence on gapfilling means that prediction accuracy is tightly coupled to gapfilling quality. [src: acinetobacter_adp1_explorer]

> This heavy dependence on gapfilling means that prediction accuracy is tightly coupled to gapfilling quality. [src: acinetobacter_adp1_explorer]

## Other caveats in this report

- The 120 unmatched ADP1 database reactions (9%) may be custom or draft reactions not yet in ModelSEED. [src: acinetobacter_adp1_explorer]
- The discordant 26% of ADP1 genes with FBA and experimental essentiality data are model-refinement candidates or may reflect regulatory effects absent from FBA. [src: acinetobacter_adp1_explorer]
- No gene in the Acinetobacter baylyi ADP1 database has data across all 6 modalities. [src: acinetobacter_adp1_explorer]
- FBA flux data are the sparsest modality in the Acinetobacter baylyi ADP1 database, covering 15% of genes and limiting concordance analysis to 866 genes. [src: acinetobacter_adp1_explorer]
- The KBase Data Lakehouse–ADP1 pangenome cluster mapping goes through 3 tables and is 100% complete, but may have edge cases for clusters that split or merge between the two pangenome analyses. [src: acinetobacter_adp1_explorer]
