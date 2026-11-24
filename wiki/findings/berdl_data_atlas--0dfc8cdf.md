---
type: "Finding"
description: "The corrected structural fitness atlas join yields 55,454 FitnessBrowser genes across 48 organisms with both fitness measurements and an AlphaFold model."
finding_id: "berdl_data_atlas--0dfc8cdf"
result: "observation"
source: "berdl_data_atlas"
quantities: [{"value": "55,454", "what": "genes with both fitness data and an AlphaFold model", "unit": "genes", "denominator": "", "scope": ""}, {"value": "48", "what": "organisms covered", "unit": "organisms", "denominator": "", "scope": ""}]
caveat: "UC2\u2013UC5 require their own first sample-execution before publication, whereas UC1 has been completed."
first_added: "2026-11-24"
source_hash: "be5f29816668f7662998e22a666a6a398c84a18d10e70464cfbd943fc645831e"
---
# Corrected join links fitness data to AlphaFold models for many genes

The corrected structural fitness atlas join yields 55,454 FitnessBrowser genes across 48 organisms with both fitness measurements and an AlphaFold model. [src: berdl_data_atlas]

## Key figures

- **55,454 genes**: genes with both fitness data and an AlphaFold model [src: berdl_data_atlas]
- **48 organisms**: organisms covered [src: berdl_data_atlas]

## Evidence

> The corrected join produces a working dataset of **55,454 FitnessBrowser genes across 48 organisms** with both fitness measurements AND an AlphaFold model. [src: berdl_data_atlas]

From the report [[summaries/berdl_data_atlas__REPORT]].

## Caveat

UC2–UC5 require their own first sample-execution before publication, whereas UC1 has been completed. [src: berdl_data_atlas]

> UC2–UC5 require their own first sample-execution before publication. UC1 has been completed — see Finding 6. [src: berdl_data_atlas]

## Other caveats in this report

- The proposed structural fitness atlas join required correction because FitnessBrowser exposes (orgId, locusId), not protein_id, and its AlphaFold bridge runs through besthitswissprot.sprotAccession. [src: berdl_data_atlas]
- The proposed structural-fitness atlas bridge through protein_id was incorrect because FitnessBrowser uses a composite (orgId, locusId) primary key and does not expose protein_id. [src: berdl_data_atlas]
- The atlas references canonically cite catalogued data systems rather than biological hypotheses being tested. [src: berdl_data_atlas]
- Join value-space validity is established only for UC1; the bridge atlas establishes schema compatibility but not overlapping values. [src: berdl_data_atlas]
- The genome_id key has different meanings in KBase, NCBI, and MAG pipelines: UPA, accession, and hash, respectively. [src: berdl_data_atlas]
