---
type: "Finding"
description: "The report concludes that NMDC environment explains no more variance than study_id alone and performs worse than predicting the mean when whole studies are held out."
finding_id: "euk_in_prok_correlates--c74ec1ab"
result: "null result"
source: "euk_in_prok_correlates"
quantities: []
caveat: "NMDC's read-based taxonomy spans only ~9 studies (one soil study \u224843% of runs), so the cross-study generalization test is under-powered."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Environment does not generalize across studies beyond study identity

The report concludes that NMDC environment explains no more variance than study_id alone and performs worse than predicting the mean when whole studies are held out. [src: euk_in_prok_correlates]

## Evidence

> Environment explains **no more variance than `study_id` alone**, and when whole studies are held out the environment model performs **worse than predicting the mean** [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

NMDC's read-based taxonomy spans only ~9 studies (one soil study ≈43% of runs), so the cross-study generalization test is under-powered. [src: euk_in_prok_correlates]

> - **Few independent studies.** NMDC's read-based taxonomy spans only ~9 studies (one soil study ≈43% of runs); `data/01_data_landscape.md` documents that no on-system source provides per-sample eukaryotic read fraction across many studies (MGnify here is a MAG catalog; SPIRE/GEM/Tara are MAG collections; EMP is 16S). The cross-study generalization test is therefore under-powered, and the within-study result is demonstrated for **one soil study only** — it may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- In NMDC each biome is ~80–100% nested within a single study, preventing separation of the strong univariate environment signal from study/batch. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
