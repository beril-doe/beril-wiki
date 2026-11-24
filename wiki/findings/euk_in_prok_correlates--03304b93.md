---
type: "Finding"
description: "The report concludes that eukaryotic contamination in these prokaryote-targeted metagenomes is dominated by photosynthetic DNA, not animal-host DNA, in the largely environmental NMDC collection."
finding_id: "euk_in_prok_correlates--03304b93"
result: "inference"
source: "euk_in_prok_correlates"
quantities: []
caveat: "The within-study result is demonstrated for one soil study only and may not extend to aquatic or host-associated collections."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Photosynthetic DNA, not animal-host DNA, dominates eukaryotic contamination

The report concludes that eukaryotic contamination in these prokaryote-targeted metagenomes is dominated by photosynthetic DNA, not animal-host DNA, in the largely environmental NMDC collection. [src: euk_in_prok_correlates]

## Evidence

> eukaryotic contamination in these prokaryote-targeted metagenomes is dominated by **photosynthetic** DNA, not animal-host DNA. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

The within-study result is demonstrated for one soil study only and may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

> The cross-study generalization test is therefore under-powered, and the within-study result is demonstrated for **one soil study only** — it may not extend to aquatic or host-associated collections. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- In NMDC each biome is ~80–100% nested within a single study, preventing separation of the strong univariate environment signal from study/batch. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
