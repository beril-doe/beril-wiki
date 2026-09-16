---
type: "Dataset"
description: "PROTECT Gold is a curated data collection of isolate, assay, growth-kinetic, patient-metagenomic and pairwise-interaction tables used in cystic fibrosis formulation-design analyses."
sources: ["summaries/cf_formulation_design__REPORT.md", "summaries/pitfalls.md"]
---
# PROTECT Gold

**PROTECT Gold** (stored at `~/protect/gold/`) is a named data collection of 23 tables (30.5M rows). It covers an isolate catalog, inhibition assays, carbon utilization, growth kinetics, patient metagenomics and pairwise interactions. [src: cf_formulation_design]

## Data-quality caveat

Two PROTECT Gold tables, `fact_pairwise_interaction` and `fact_carbon_utilization`, contain identical values (correlation = 1.0, mean difference = 0.0). This was flagged in the cf_formulation_design project. The endpoint optical-density (OD) data therefore does not capture co-culture metabolic interactions. Only the RFU-based (relative fluorescence unit) competition assay provides pairwise interaction effects. Analyses that need pairwise effects should not treat `fact_pairwise_interaction` as an independent measurement. [src: pitfalls]

## Related Pages

- [[summaries/cf_formulation_design__REPORT]] — the project that used PROTECT Gold
- [[summaries/pitfalls]] — the central record of the pairwise-interaction table duplication
