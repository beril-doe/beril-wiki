---
type: "Dataset"
description: "UC Davis / Arkin IBD and phage integrated data mart with documented lineage, schema, missing-data codes and mixed legacy/modern taxon naming."
sources: ["summaries/discoveries.md", "summaries/ibd_phage_targeting__REPORT.md", "summaries/pitfalls.md"]
aliases: ["CrohnsPhage", "CrohnsPhage integrated mart", "UC Davis CrohnsPhage mart"]
---
# CrohnsPhage data mart

The CrohnsPhage data mart is the UC Davis / Arkin IBD and phage integrated data mart, also called the CrohnsPhage integrated mart. It ships with documented lineage, schema and missing-data codes. [src: discoveries] Its mixed legacy and modern taxon naming caused real analysis errors. [src: pitfalls] The evidence comes from [[summaries/discoveries]], [[summaries/pitfalls]] and [[summaries/ibd_phage_targeting__REPORT]].

## Key facts

- The mart ships with a `lineage.yaml` (ETL provenance, changelog and known gaps) and a `schema_overview.yaml` (table inventory by category). [src: discoveries]
- It also ships per-table YAML dictionaries listing columns, dtypes, null counts, unique counts and sample values. [src: discoveries]
- Its `ref_missing_data_codes` table holds sentinel codes such as `PENDING_DAVE_LAB`, `PENDING_KUEHL` and `PENDING_HMP2_RAW`. These separate real NULLs from known-pending data. [src: discoveries]
- The discoveries digest states that this documentation pattern makes large local marts agent-readable without any live queries. [src: discoveries]
- The ibd_phage_targeting project used the local mart (v10, schema v2.4). It drew on `dim_samples`, `dim_participants`, `fact_taxon_abundance`, `fact_clinical_longitudinal`, `ref_taxonomy_crosswalk` and `crohns_patient_demographics.xlsx`. [src: ibd_phage_targeting]
- These supplied sample and participant metadata, MetaPhlAn3 and Kaiju taxonomy, severity markers and UC Davis demographics. [src: ibd_phage_targeting]

## Taxon naming problems

The mart mixes name formats and naming eras. See [[concepts/taxonomic-synonymy-and-strain-name-collisions-in-cross-database-matching]].

- Formats diverge. A short name (`Faecalibacterium prausnitzii`) appears alongside full lineage strings ending in `s__Faecalibacterium_prausnitzii`. [src: pitfalls]
- CMD_IBD uses modern names and CMD_HEALTHY uses legacy names. [src: pitfalls]
- Because of GTDB r214+ genus renames, `Bacteroides vulgatus` (CMD_HEALTHY lineage) and `Phocaeicola vulgatus` (CMD_IBD short name) share one NCBI taxid but are treated as separate species. [src: pitfalls]
- A naive pivot therefore gives log₂FC ≈ 28 (≈ 2.68 × 10⁸ fold) for every renamed species, because one cohort's mean abundance collapses to pseudocount. [src: pitfalls]
- The committed `ref_taxonomy_crosswalk` does not fully fix this. Legacy `Bacteroides_X` rows have `ncbi_taxid = NaN` (not a number), so joins through taxid leave them orphaned. [src: pitfalls]
- The crosswalk also lists *B. vulgatus* and *P. vulgatus* as two rows with different `canonical_name` values. [src: pitfalls]
- This is why ibd_phage_targeting treats pre-computed `ref_*` tables as starting points that need verification, not as ground truth. [src: discoveries]

## Sub-study coverage

Scoped to ecotype-assigned samples (8,489 total), the mart has 45 sub-studies with at least 10 healthy-control (HC) samples. [src: pitfalls] It has 5 sub-studies with at least 10 Crohn's disease (CD) samples. [src: pitfalls] No sub-study has at least 10 of both. [src: pitfalls] For related issues in pooled comparisons, see [[concepts/substudy-nesting-and-feature-leakage-in-pooled-cohort-microbiome-comparisons]].
