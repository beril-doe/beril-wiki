---
type: "Finding"
description: "Detectable eukaryotic reads occur in 77% of the NMDC prokaryote-targeted metagenomic runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20% eukaryotic."
finding_id: "euk_in_prok_correlates--20d8ac8c"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "77%", "what": "runs with detectable eukaryotic reads", "unit": "%", "denominator": "NMDC prokaryote-targeted metagenomic runs", "scope": "NMDC"}, {"value": "2.7%", "what": "median eukaryotic fraction", "unit": "%", "denominator": "", "scope": "NMDC"}, {"value": "13.3%", "what": "mean eukaryotic fraction", "unit": "%", "denominator": "", "scope": "NMDC"}, {"value": "20%", "what": "runs exceeding 20% eukaryotic", "unit": "%", "denominator": "runs", "scope": "NMDC"}]
caveat: "Only GOTTCHA2 yields a usable eukaryotic fraction, and its absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Most NMDC prokaryote-targeted metagenomes carry detectable eukaryotic reads

Detectable eukaryotic reads occur in 77% of the NMDC prokaryote-targeted metagenomic runs, with a median eukaryotic fraction of 2.7%, a mean of 13.3%, and 20% of runs exceeding 20% eukaryotic. [src: euk_in_prok_correlates]

## Key figures

- **77%**: runs with detectable eukaryotic reads (denominator NMDC prokaryote-targeted metagenomic runs; scope NMDC) [src: euk_in_prok_correlates]
- **2.7%**: median eukaryotic fraction (scope NMDC) [src: euk_in_prok_correlates]
- **13.3%**: mean eukaryotic fraction (scope NMDC) [src: euk_in_prok_correlates]
- **20%**: runs exceeding 20% eukaryotic (denominator runs; scope NMDC) [src: euk_in_prok_correlates]

## Evidence

> **77% carry detectable eukaryotic reads** (median eukaryotic fraction 2.7%, mean 13.3%; **20% of runs exceed 20% eukaryotic**). [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

Only GOTTCHA2 yields a usable eukaryotic fraction, and its absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]

> - **Classifier/database dependence.** Only GOTTCHA2 yields a usable eukaryotic fraction; absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- In NMDC each biome is ~80–100% nested within a single study, preventing separation of the strong univariate environment signal from study/batch. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
