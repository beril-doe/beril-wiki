---
type: "Dataset"
description: "Cohorts (anchor_deep, anchor_shallow, soil_baseline) assembled from kbase_ke_pangenome biosample metadata and CheckM-filtered for comparison."
sources: ["summaries/bacillota_b_subsurface_accessory__REPORT.md", "summaries/clay_confined_subsurface__REPORT.md"]
aliases: ["anchor_deep", "anchor_shallow", "soil_baseline"]
---
# Clay-confined cultured genome cohort

This page covers the clay-confined cultured genome cohort: the anchor_deep, anchor_shallow and soil_baseline cohorts assembled from kbase_ke_pangenome biosample metadata and CheckM-filtered for comparison. The clay report built the cohort from `ncbi_env` keywords and filtered it with CheckM ≥80% / ≤5%. [src: clay_confined_subsurface] Its deep cohort is small (9 genomes before filtering). [src: clay_confined_subsurface] The compartment labels are keyword-inferred. [src: clay_confined_subsurface] See [[summaries/clay_confined_subsurface__REPORT]] and [[summaries/bacillota_b_subsurface_accessory__REPORT]].

## Key facts

### Assembly in the clay report

The clay report assembled the cohort from `kbase_ke_pangenome.ncbi_env` in the KBase Data Lakehouse. It filtered on clay-related isolation_source and env_* keywords and joined to the pangenome through `genome.ncbi_biosample_id`. [src: clay_confined_subsurface] See [[entities/kbase-ke-pangenome]]. The quality filter required CheckM ≥80% / ≤5%. [src: clay_confined_subsurface] The notebook 01_cohort_assembly.ipynb pulls clay-mentioning biosamples, classifies them as deep, shallow or unclassified, and joins them to the pangenome. [src: clay_confined_subsurface] The notebook 03_soil_baseline.ipynb builds a phylum-stratified soil/sediment baseline with the same feature pipeline as the clay cohort. [src: clay_confined_subsurface]

### Cohort sizes

| Cohort | Before → after filtering | Composition |
|---|---|---|
| anchor_deep | 9 → 6 | Mont Terri Opalinus borehole 8 (BRC-3 + BIC-A1); bentonite formation 1 [src: clay_confined_subsurface] |
| anchor_shallow | 30 → 30 | Coalvale silty clay 8; Cerrado clay 1; agricultural clay 21 [src: clay_confined_subsurface] |
| soil_baseline | 150 → 137 | Phylum-stratified soil/sediment with no clay mention: Pseudomonadota 50, Bacillota 40, Bacillota_B 20, Bacteroidota 20, Actinomycetota 20 [src: clay_confined_subsurface] |

The deep cohort has 9 genomes before filtering, 8 from Mont Terri Opalinus boreholes and 1 from a bentonite formation. [src: clay_confined_subsurface] See [[entities/mont-terri-opalinus-clay]]. The shallow comparison cohort is n=30 isolates from Coalvale, Cerrado and agricultural soils. [src: clay_confined_subsurface]

### Use in the clay report's comparison

In that report the deep and shallow marker profiles mirror each other. anchor_deep is dominated by SR_only (5/9). anchor_shallow is dominated by IR_only (15/30). SR is sulfate reduction and IR is iron reduction. The report gives a Fisher's exact OR=∞ (odds ratio), p=2×10⁻⁴ for SR_complete. It also gives 3.7-fold IR enrichment in shallow versus the broader soil baseline (p=0.0025). [src: clay_confined_subsurface]

### Bacillota_B version

The [[entities/bacillota-b]] report built a separate deep-clay anchor of 10 genomes. BacDive expansion using kescience_bacdive isolation and taxonomy yielded zero additional Bacillota_B in that run. The anchor came almost entirely from an `ncbi_env` keyword search. [src: bacillota_b_subsurface_accessory] See [[entities/bacdive]]. Its soil baseline has 62 phylum-matched soil/sediment genomes: Syntrophomonadales 29, Desulfitobacteriales 16, Moorellales 6, Thermacetogeniales 4, Ammonifexales 2, Carboxydocellales 2, Desulfotomaculales 1, Heliobacteriales 1 and Thermincolales 1. [src: bacillota_b_subsurface_accessory] The notebook 01_cohort_assembly.ipynb there assembles the Bacillota_B universe, the 10-anchor / 62-baseline cohort and the IR PFAM availability gate. [src: bacillota_b_subsurface_accessory]

## Data files

The clay report ships these tables:
- cohort_assignments.tsv has 61 rows. It gives per-genome cohort_class, sub_cohort, compartment and depth_class with full GTDB taxonomy. [src: clay_confined_subsurface]
- cohort_summary.tsv has 10 rows of cohort breakdown counts. [src: clay_confined_subsurface]
- genome_features.parquet has 61 rows. It holds per-genome WL, NiFe, SR, IR and Nif marker booleans, counts, toolkit_score and GapMind amino-acid pathway counts. [src: clay_confined_subsurface]
- baseline_features.parquet has 150 rows for the phylum-stratified soil baseline, with the same schema. [src: clay_confined_subsurface]

The Bacillota_B report's cohort_assignments.tsv has 124 rows: anchor_deep_clay 10, soil_baseline 62, anchor_other_clay and unclassified Bacillota_B genomes. [src: bacillota_b_subsurface_accessory]

## Caveats

The compartment field is keyword-inferred from isolation_source strings. A small number of bentonite or "rock" entries could be either porewater or rock-attached. [src: clay_confined_subsurface] See [[concepts/cultivation-bias-toward-porewater-versus-rock-attached-subsurface-communities]] and [[concepts/harmonizing-free-text-isolation-source-and-environment-metadata]].
