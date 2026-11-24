---
type: "Finding"
description: "Plant-root NMDC samples have 100% eukaryotic detection and a plastid share of eukaryotes of 0.03, indicating predominantly non-plastid root-associated fungi/protists."
finding_id: "euk_in_prok_correlates--77a05e86"
result: "observation"
source: "euk_in_prok_correlates"
quantities: [{"value": "100%", "what": "eukaryotic detection in plant-root samples", "unit": "%", "denominator": "", "scope": "NMDC plant roots"}, {"value": "0.03", "what": "plastid share of eukaryotes in roots", "unit": "", "denominator": "", "scope": "NMDC plant roots"}]
caveat: "In NMDC each biome is ~80\u2013100% nested within a single study, so the strong univariate environment signal cannot be separated from study/batch."
first_added: "2026-11-24"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Plant-root samples carry mostly non-plastid fungal and protist eukaryotes

Plant-root NMDC samples have 100% eukaryotic detection and a plastid share of eukaryotes of 0.03, indicating predominantly non-plastid root-associated fungi/protists. [src: euk_in_prok_correlates]

## Key figures

- **100%**: eukaryotic detection in plant-root samples (scope NMDC plant roots) [src: euk_in_prok_correlates]
- **0.03**: plastid share of eukaryotes in roots (scope NMDC plant roots) [src: euk_in_prok_correlates]

## Evidence

> | Plants (roots) | 100% | **0.03** | root-associated **fungi/protists** (non-plastid) | [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

In NMDC each biome is ~80–100% nested within a single study, so the strong univariate environment signal cannot be separated from study/batch. [src: euk_in_prok_correlates]

> In NMDC, **each biome is ~80–100% nested within a single study**, so the strong univariate environment signal cannot be separated from study/batch. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge have domain-level Eukaryota signals of ≈0 because their NMDC reference databases are prokaryote-restricted, leaving GOTTCHA2 as the only usable eukaryotic estimator here. [src: euk_in_prok_correlates]
- After excluding Unknown or missing metadata, NMDC ecosystem_type reduces to Soil, Freshwater and Roots, making its test identical to the matrix test rather than independent confirmation. [src: euk_in_prok_correlates]
- An earlier NMDC analysis including the Unknown bucket, which has the highest median eukaryotic fraction, reported inflated p≈10⁻⁵⁰ that the report removed as a missingness artifact. [src: euk_in_prok_correlates]
- The report warns that naive cross-collection regression of NMDC eukaryotic fraction on environmental metadata would report a strong but largely spurious batch-driven association. [src: euk_in_prok_correlates]
- The NMDC depth association is suggestive only because it is not batch-controlled, measured-depth runs come from a handful of non-soil studies, and the dominant NEON soil study records no depth. [src: euk_in_prok_correlates]
