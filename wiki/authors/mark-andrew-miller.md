# Mark Andrew Miller

ORCID: [0000-0001-9076-6066](https://orcid.org/0000-0001-9076-6066)

## Contributions

The [[summaries/nmdc_context_audit__REPORT]] project audited KBase Data Lakehouse resources whose names contain `nmdc` and found that 20 database names resolved to 7 maintained resources spanning three tenants and six provenance classes. It found that the genuine NMDC biosample universe contained 16,640 samples, whereas the co-hosted NCBI mirror contained 51,711,888 biosamples and 756,112,544 attribute rows, and that `kbase.nmdc_mags` contained 62,346 MAGs. [src: nmdc_context_audit] The project also found that Iceberg snapshot ages ranged across approximately four months, with the latest commits dated 2026-07-02 for `kbase.nmdc_mags` and `kbase.nmdc_neon`, 2026-05-27 for `kbase.nmdc_arkin`, 2026-05-20 for `nmdc.metadata`, `nmdc.results`, and `nmdc.ref_data`, and 2026-03-09 for `nmdc.ncbi_biosamples`. [src: nmdc_context_audit]

The [[summaries/euk_in_prok_correlates__REPORT]] project quantified eukaryotic read fractions in 2,759 NMDC ReadbasedAnalysis runs from 9 studies using GOTTCHA2 and found detectable eukaryotic reads in 77% of runs, with a median fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20%; among runs with detectable signal, plastid sequences represented a median 100% of that signal. [src: euk_in_prok_correlates] It found that aquatic freshwater samples had 99.5% eukaryotic detection with a plastid share of 1.00, terrestrial soil samples had 55.7% detection with a plastid share of 0.43, and plant-root samples had 100% detection with a plastid share of 0.03. [src: euk_in_prok_correlates] The project found that environment-only prediction achieved R²=0.35 under random cross-validation but R²=−0.30 under GroupKFold out-of-study validation, while environment plus sequencing achieved R²=−0.39; within 1,186 runs from the NEON soil study, local vegetation was associated with eukaryotic fraction at H=119.1 and p=7.6×10⁻²¹. [src: euk_in_prok_correlates]

The [[summaries/pseudomonas_carbon_ecology__REPORT]] project analyzed GapMind carbon-pathway predictions from 12,732 genomes across 433 *Pseudomonas* species clades and found that 43 of 62 pathways differed significantly between 7 *Pseudomonas* s.s. species and 189 *Pseudomonas_E* species after Benjamini–Hochberg correction. [src: pseudomonas_carbon_ecology] It reported that xylose completeness was 0.0% versus 74.4%, ribose 27.9% versus 92.0%, and arabinose 0.0% versus 62.6% in the *P. aeruginosa* and *P. fluorescens* groups, respectively. [src: pseudomonas_carbon_ecology] Among 54 free-living and plant-associated species, carbon profiles were associated with isolation environment with permutation p=0.006, while a four-class Random Forest classifier achieved balanced accuracy of 0.408 +/- 0.169 compared with a 0.250 chance baseline. [src: pseudomonas_carbon_ecology]

## Projects (3)

- [[summaries/euk_in_prok_correlates__REPORT|euk_in_prok_correlates]]
- [[summaries/nmdc_context_audit__REPORT|nmdc_context_audit]]
- [[summaries/pseudomonas_carbon_ecology__REPORT|pseudomonas_carbon_ecology]]
