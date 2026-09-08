---
type: Dataset
description: Pathogen-genome data collection supporting PROTECT and BERDL analyses
sources:
- id: berdl_data_atlas
  resource: ../summaries/berdl_data_atlas__REPORT.md
  title: berdl data atlas
- id: cf_formulation_design
  resource: ../summaries/cf_formulation_design__REPORT.md
  title: cf formulation design
title: PROTECT Genome Depot
---
# PROTECT Genome Depot

## What this entity is

**Canonical name:** PROTECT Genome Depot. [^berdl_data_atlas]

**Known aliases:** protect_genomedepot; PROTECT. [^berdl_data_atlas]

**Stable external identifier:** No stable external identifier is specified in the source document. [^berdl_data_atlas]

PROTECT Genome Depot is a dataset catalog used for pathogen-genome data within the BERDL inventory. [^berdl_data_atlas]

## Key facts

The BERDL Data Atlas reports that the PROTECT tenant contains 4% of the inventoried tables, appears in 2 of 66 audited BERIL projects, and covers 6 biological topics. [^berdl_data_atlas]

PROTECT has a topic-coverage entropy of 2.37 in the atlas comparison. [^berdl_data_atlas]

The atlas recommends PROTECT Genome Depot for pathogen-genome data. [^berdl_data_atlas]

The cf formulation study **supports** this pathogen-genome recommendation by analyzing 643 annotated PROTECT genomes: 304 (47%) were PAO1-like, 48 (7%) were PA14-like, and 291 (45%) were intermediate; among classifiable isolates, 86% were PAO1-like. [^cf_formulation_design]

The study further **refines** the dataset’s pathogen-diversity context: PROTECT isolates were distributed across the broader lung-PA diversity in a Pfam-based tree of 165 genomes rather than clustering in one lineage. [^cf_formulation_design]

The proposed UC4 bridge between NMDC and PROTECT had 10 shared schema-level join keys and zero realized use at audit time; the proposed use was to study environmental distributions of clinically relevant pathogens and associated biogeochemistry. [^berdl_data_atlas]

The UC4 bridge remains a proposal rather than a validated integration because the atlas sample-validated only UC1; UC4 requires live-cluster execution to establish value-space overlap. [^berdl_data_atlas]

The dataset is therefore relevant to [environmental-resistome](../concepts/environmental-resistome.md), particularly analyses connecting environmental samples with pathogen genomes and resistance-associated context. [^berdl_data_atlas]

The dataset is also part of the cross-tenant integration opportunities described in [berdl_data_atlas__REPORT](../summaries/berdl_data_atlas__REPORT.md). [^berdl_data_atlas]

The new formulation analysis is documented in [cf_formulation_design__REPORT](../summaries/cf_formulation_design__REPORT.md). [^cf_formulation_design]

[^berdl_data_atlas]: [berdl data atlas](../summaries/berdl_data_atlas__REPORT.md)
[^cf_formulation_design]: [cf formulation design](../summaries/cf_formulation_design__REPORT.md)
