---
type: "Finding"
description: "Across 2,759 NMDC ReadbasedAnalysis runs (native nmdc.results GOTTCHA2 classifications, 9 studies), 77% carry detectable eukaryotic reads, and among detectable runs plastid (plant/algal chloroplast) is a median 100% of the eukaryotic signal, so contamination is dominated by photosynthetic rather than animal-host DNA."
finding_id: "euk_in_prok_correlates--59085a38"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "2,759", "what": "NMDC ReadbasedAnalysis runs analysed", "unit": "runs", "denominator": "", "scope": "9 studies, GOTTCHA2 classifications"}, {"value": "77%", "what": "runs with detectable eukaryotic reads", "unit": "", "denominator": "2,759 runs", "scope": ""}, {"value": "20%", "what": "runs exceeding 20% eukaryotic fraction", "unit": "", "denominator": "2,759 runs", "scope": ""}, {"value": "100%", "what": "median plastid share of the eukaryotic signal", "unit": "", "denominator": "", "scope": "among runs with detectable eukaryotic reads"}]
caveat: "Only GOTTCHA2 yields a usable eukaryotic fraction; absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination."
first_added: "2026-10-27"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Eukaryotic reads in prokaryote metagenomes are mostly photosynthetic plastid DNA

Across 2,759 NMDC ReadbasedAnalysis runs (native nmdc.results GOTTCHA2 classifications, 9 studies), 77% carry detectable eukaryotic reads, and among detectable runs plastid (plant/algal chloroplast) is a median 100% of the eukaryotic signal, so contamination is dominated by photosynthetic rather than animal-host DNA. [src: euk_in_prok_correlates]

## Key figures

- **2,759 runs**: NMDC ReadbasedAnalysis runs analysed (scope 9 studies, GOTTCHA2 classifications) [src: euk_in_prok_correlates]
- **77%**: runs with detectable eukaryotic reads (denominator 2,759 runs) [src: euk_in_prok_correlates]
- **20%**: runs exceeding 20% eukaryotic fraction (denominator 2,759 runs) [src: euk_in_prok_correlates]
- **100%**: median plastid share of the eukaryotic signal (scope among runs with detectable eukaryotic reads) [src: euk_in_prok_correlates]

## Evidence

> Across **2,759 NMDC ReadbasedAnalysis runs** (native `nmdc.results` GOTTCHA2 classifications, 9 studies), **77% carry detectable eukaryotic reads** (median eukaryotic fraction 2.7%, mean 13.3%; **20% of runs exceed 20% eukaryotic**). Among detectable runs, **plastid (plant/algal chloroplast) is a median 100% of the eukaryotic signal** — eukaryotic contamination in these prokaryote-targeted metagenomes is dominated by **photosynthetic** DNA, not animal-host DNA. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

Only GOTTCHA2 yields a usable eukaryotic fraction; absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]

> - **Classifier/database dependence.** Only GOTTCHA2 yields a usable eukaryotic fraction; absolute values are database-dependent and should be read as relative/ordinal, not calibrated absolute contamination. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge yielded approximately zero domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; GOTTCHA2 was the only usable estimator here. [src: euk_in_prok_correlates]
- Ecosystem type reduced to the same three biomes as matrix and was not an independent confirmation; an earlier p≈10⁻⁵⁰ with the Unknown bucket was a missingness artifact. [src: euk_in_prok_correlates]
- Each biome was approximately 80–100% nested within a single study, so the univariate environment signal was confounded with study/batch. [src: euk_in_prok_correlates]
- In 292 runs with measured depth, cross-study Spearman ρ=−0.29, p=5.2×10⁻⁷; the shallower–higher-eukaryote association was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]
- The Kraken2 classification report had approximately 29 million rows; the report advises aggregation to one row per workflow_run_id before metadata joins. [src: euk_in_prok_correlates]
