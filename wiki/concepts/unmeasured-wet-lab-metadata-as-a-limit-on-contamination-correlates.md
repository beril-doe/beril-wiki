---
type: "Concept"
description: "Missing extraction, host-depletion, filtration and library-prep metadata in public collections and what that prevents testing."
sources: ["summaries/euk_in_prok_correlates__REPORT.md"]
---
# Unmeasured wet-lab metadata as a limit on contamination correlates

NMDC lacks the wet-lab metadata needed to test the strongest proposed causes of eukaryotic contamination in prokaryotic metagenomes. [src: euk_in_prok_correlates] The evidence is one report, [[summaries/euk_in_prok_correlates__REPORT]]. See also [[entities/nmdc-integrated-collections]] and annotation and environmental metadata table gaps in the data lakehouse.

## What is missing

NMDC does not populate DNA-extraction kit, size fractionation/filtration, host-depletion method or library-prep fields, so wet-lab factors cannot be tested. [src: euk_in_prok_correlates] The processing booleans in `biosample_to_workflow_run` are near-constant, and `has_filtration` is false everywhere. [src: euk_in_prok_correlates] The report names host depletion and extraction kit as strong literature levers that therefore stay in the unmeasured residual. [src: euk_in_prok_correlates]

## Why it matters

The report cites Sobolev et al. (2025, IJMS, PMID 41373768), who show that sample matrix together with extraction kit drives eukaryotic admixture. [src: euk_in_prok_correlates] Ortiz-Chura et al. (2024, Anim Microbiome, PMID 39456104) quantify metadata and structure limitations of public collections, with more than 40% of basic fields missing. [src: euk_in_prok_correlates] The report states that NMDC omits extraction kit, host-depletion method and size fraction. [src: euk_in_prok_correlates]

## Open Directions

- Acquire per-study protocols (extraction kit, host-depletion method, size fraction), either supplied by users or from a collection that records them, and rerun the correlate analysis with them. This closes the gap left by the unmeasured residual. [src: euk_in_prok_correlates]
- Check whether other collections on the Data Lakehouse record filtration or library-prep fields, since NMDC's `has_filtration` is uniformly false.
- Test extraction kit and sample matrix together on a subset with known kits, to compare against the Sobolev et al. finding.
