# Mark Andrew Miller

ORCID: [0000-0001-9076-6066](https://orcid.org/0000-0001-9076-6066)

## Contributions

### Eukaryotic reads in NMDC metagenomes

[[summaries/euk_in_prok_correlates__REPORT]] analysed GOTTCHA2 classifications from 2,759 ReadbasedAnalysis runs across 9 studies. Of these runs, 77% carried detectable eukaryotic reads, with a median eukaryotic fraction of 2.7% and a mean of 13.3%. [src: euk_in_prok_correlates] Plastid DNA was a median 100% of the eukaryotic signal among runs with detectable eukaryotic reads. [src: euk_in_prok_correlates] Eukaryote detection was 99.5% in freshwater, 55.7% in soil and 100% in plant roots. [src: euk_in_prok_correlates] The association with matrix was strong (Kruskal–Wallis H=77.8, p=1.3×10⁻¹⁷), but each biome is ~80–100% nested within a single study, so it is confounded with study/batch. [src: euk_in_prok_correlates]

The project found that cross-study prediction failed. A study_id-only model reached random-CV R² of 0.24, and the environment model reached 0.35 under random CV. Under out-of-study GroupKFold the environment model fell to −0.30, and out-of-study detection AUC was 0.56. [src: euk_in_prok_correlates] Within the dominant NEON soil study (1,186 runs), local environment plus geography gave within-study 5-fold R² = +0.17 ± 0.06. [src: euk_in_prok_correlates] Median eukaryotic fractions in that study were 23% in sedge/forb herbaceous soil and 2% in evergreen forest. [src: euk_in_prok_correlates] The within-study result is demonstrated for one soil study only. [src: euk_in_prok_correlates] The depth correlation (Spearman ρ = −0.29, n=292) was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]

### NMDC labelling in the KBase Data Lakehouse

[[summaries/nmdc_context_audit__REPORT]] found that 20 database names containing "nmdc" resolve to 7 real, maintained resources across three tenants and six provenance classes. [src: nmdc_context_audit] nmdc.ncbi_biosamples holds 51,711,888 biosamples and is NCBI-derived. nmdc.metadata.biosample_set holds 16,640 samples, a ~3,000× difference. [src: nmdc_context_audit] kbase.nmdc_neon is a namesake collision with NEON, not NMDC. [src: nmdc_context_audit] Snapshot ages differ by ~4 months, from nmdc.ncbi_biosamples (2026-03-09) to kbase.nmdc_mags (2026-07-02). [src: nmdc_context_audit] The audit found that docs/schemas/nmdc.md returns a 404 and that the berdl skill has zero NMDC content. [src: nmdc_context_audit] It recommended five fixes and applied none. The link between the overloaded label and poor resource choices is inferred, not observed. [src: nmdc_context_audit]

### Carbon utilization in Pseudomonas

[[summaries/pseudomonas_carbon_ecology__REPORT]] used GapMind predictions for 12,732 genomes in 433 Pseudomonas species. Of 62 carbon pathways, 43 differed significantly between 7 Pseudomonas s.s. species and 189 Pseudomonas_E species. [src: pseudomonas_carbon_ecology] All 7 pathways that differed by more than 50 percentage points involved plant-derived sugars or sugar alcohols. For example, xylose was 0.0% complete in the P. aeruginosa group and 74.4% in the P. fluorescens group. [src: pseudomonas_carbon_ecology] Amino acid pathways stayed above 99% in both subgenera. [src: pseudomonas_carbon_ecology] Rhamnose (66.8% vs 41.3%) and fucose (66.8% vs 45.1%) were higher in P. aeruginosa, but neither difference was significant after FDR correction. [src: pseudomonas_carbon_ecology]

Among 54 free-living and plant-associated species, carbon profiles were linked to isolation environment (permutation test, p = 0.006; between/within ratio 1.087). [src: pseudomonas_carbon_ecology] A Random Forest on 4 environment classes reached balanced accuracy of 0.408 ± 0.169 against 0.250 chance, which the report calls not strongly predictive. [src: pseudomonas_carbon_ecology]

## Projects (3)

- [[summaries/euk_in_prok_correlates__REPORT|euk_in_prok_correlates]]
- [[summaries/nmdc_context_audit__REPORT|nmdc_context_audit]]
- [[summaries/pseudomonas_carbon_ecology__REPORT|pseudomonas_carbon_ecology]]
