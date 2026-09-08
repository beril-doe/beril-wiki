---
type: Dataset
description: BERDL biochemistry dataset used to validate ADP1 reactions and compounds
sources:
- id: acinetobacter_adp1_explorer
  resource: ../summaries/acinetobacter_adp1_explorer__REPORT.md
  title: acinetobacter adp1 explorer
title: KBase MSD Biochemistry
---
# KBase MSD Biochemistry

## What this entity is

**KBase MSD Biochemistry** is a BERDL biochemistry dataset used to connect metabolic reactions and compounds from the ADP1 Data Explorer to reference biochemical records. [^acinetobacter_adp1_explorer]

- **Canonical name:** KBase MSD Biochemistry. [^acinetobacter_adp1_explorer]
- **Known alias:** `kbase_msd_biochemistry`. [^acinetobacter_adp1_explorer]
- **Stable external identifier:** No stable external identifier was reported in the source document. [^acinetobacter_adp1_explorer]

## Evidence from the ADP1 Data Explorer

The ADP1 database connected to the `kbase_msd_biochemistry` collection as part of its BERDL integration. [^acinetobacter_adp1_explorer]

Of 1,330 tested metabolic reactions, 1,210 matched the biochemistry collection. [^acinetobacter_adp1_explorer]

All 230 tested compounds matched the biochemistry collection. [^acinetobacter_adp1_explorer]

The 120 unmatched reactions represented 9% of the 1,330 reactions and may be custom or draft reactions not yet present in ModelSEED. [^acinetobacter_adp1_explorer]

Across the 14 analyzed genomes, 1,330 unique metabolic reactions were identified; 1,248, or 94%, were shared across all 14 genomes and classified as core, 62 were variable, and 20 were genome-unique. [^acinetobacter_adp1_explorer]

Gapfilling accounted for 7.7% of reactions on average, and 243 missing functions were cataloged. [^acinetobacter_adp1_explorer]

Of 121,519 growth phenotype predictions across the 14 genomes, 105,376, or 87%, required at least one gapfilled reaction, making prediction accuracy tightly coupled to gapfilling quality in this analysis. [^acinetobacter_adp1_explorer]

## Relations to other pages

The collection is linked to [metabolic-model-gapfilling](../concepts/metabolic-model-gapfilling.md), where reaction conservation, missing functions, and gapfilling dependence are interpreted across the ADP1 metabolic analysis. [^acinetobacter_adp1_explorer]

It is part of the BERDL integration used alongside [kbase-ke-pangenome](kbase-ke-pangenome.md) and the ADP1 resource [acinetobacter-baylyi-adp1-data-explorer-database](acinetobacter-baylyi-adp1-data-explorer-database.md). [^acinetobacter_adp1_explorer]

Its reaction-level evidence supports interpretation of [flux-balance-analysis](flux-balance-analysis.md) results in the source report. [^acinetobacter_adp1_explorer]

The source analysis is summarized in [acinetobacter_adp1_explorer__REPORT](../summaries/acinetobacter_adp1_explorer__REPORT.md). [^acinetobacter_adp1_explorer]

[^acinetobacter_adp1_explorer]: [acinetobacter adp1 explorer](../summaries/acinetobacter_adp1_explorer__REPORT.md)
