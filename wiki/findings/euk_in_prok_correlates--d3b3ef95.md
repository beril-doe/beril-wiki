---
type: "Finding"
description: "NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields, and has_filtration is all false, so the strongest literature levers remain the unmeasured residual."
finding_id: "euk_in_prok_correlates--d3b3ef95"
result: "null result"
source: "euk_in_prok_correlates"
quantities: []
caveat: "The report says NMDC omits wet-lab metadata on extraction kit, host-depletion method, and size fraction, so these factors need other protocols or a collection that records them."
first_added: "2026-10-27"
source_hash: "345875dfe9abb66eeb33126277f33a3a655e7e7feed29ff12ebd79787207c86a"
---
# Wet-lab factors could not be tested because NMDC leaves them unpopulated

NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields, and has_filtration is all false, so the strongest literature levers remain the unmeasured residual. [src: euk_in_prok_correlates]

## Evidence

> - **Wet-lab factors not testable.** NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method, or library-prep fields (`data/00_feasibility_findings.md`); processing booleans in `biosample_to_workflow_run` are near-constant (`has_filtration` all false). The strongest literature levers (host depletion, extraction kit) thus remain the unmeasured residual. [src: euk_in_prok_correlates]

From the report [[summaries/euk_in_prok_correlates__REPORT]].

## Caveat

The report says NMDC omits wet-lab metadata on extraction kit, host-depletion method, and size fraction, so these factors need other protocols or a collection that records them. [src: euk_in_prok_correlates]

> 3. **Acquire wet-lab metadata** (extraction kit, host-depletion method, size fraction) — either user-supplied per-study protocols or a collection that records them — to test the strongest literature levers that NMDC omits. [src: euk_in_prok_correlates]

## Other caveats in this report

- Kraken2 and Centrifuge yielded approximately zero domain-level Eukaryota signal because their NMDC reference databases were prokaryote-restricted; GOTTCHA2 was the only usable estimator here. [src: euk_in_prok_correlates]
- Ecosystem type reduced to the same three biomes as matrix and was not an independent confirmation; an earlier p≈10⁻⁵⁰ with the Unknown bucket was a missingness artifact. [src: euk_in_prok_correlates]
- Each biome was approximately 80–100% nested within a single study, so the univariate environment signal was confounded with study/batch. [src: euk_in_prok_correlates]
- In 292 runs with measured depth, cross-study Spearman ρ=−0.29, p=5.2×10⁻⁷; the shallower–higher-eukaryote association was not batch-controlled and is suggestive only. [src: euk_in_prok_correlates]
- The Kraken2 classification report had approximately 29 million rows; the report advises aggregation to one row per workflow_run_id before metadata joins. [src: euk_in_prok_correlates]
