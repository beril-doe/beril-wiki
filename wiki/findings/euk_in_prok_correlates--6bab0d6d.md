---
type: "Finding"
description: "Adding sequencing metadata (platform, depth) does not improve NMDC out-of-study prediction of eukaryotic fraction."
finding_id: "euk_in_prok_correlates--6bab0d6d"
result: "null result"
source: "euk_in_prok_correlates"
quantities: []
caveat: "NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields, so wet-lab factors are not testable."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Platform and sequencing depth metadata add no out-of-study predictive power

Adding sequencing metadata (platform, depth) does not improve NMDC out-of-study prediction of eukaryotic fraction. [src: euk_in_prok_correlates]

## Evidence

> Adding sequencing metadata (platform, depth) does not help. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields, so wet-lab factors are not testable. [src: euk_in_prok_correlates]

> - **Wet-lab factors not testable.** NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields (`data/00_feasibility_findings.md`); processing booleans in `biosample_to_workflow_run` are near-constant (`has_filtration` all false). [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- In NMDC each biome is ~80–100% nested within a single study, preventing separation of the strong univariate environment signal from study/batch. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
