---
type: "Finding"
description: "The NEON limonene-pathway cohort contains 43 GENERIC_ONLY MAGs carrying K00128 only, including all 14 Planktothrix and Dolichospermum MAGs, making their limonene-degrader signal a false positive."
finding_id: "neon_mag_functional_discovery--2efef210"
result: "correction"
source: "neon_mag_functional_discovery"
quantities: [{"value": "43", "what": "GENERIC_ONLY MAGs carrying K00128 only", "unit": "", "denominator": "", "scope": ""}, {"value": "14", "what": "Planktothrix and Dolichospermum MAGs included", "unit": "", "denominator": "", "scope": ""}]
caveat: "Module-level enrichment should be cross-checked with per-KO step assignment because broad-substrate housekeeping enzymes shared across pathways can alone drive spurious enrichment."
first_added: "2026-11-24"
source_hash: "a4bb7071930d6a46f2a824c1d675cf1ceb2dcdeab50b3b8fadd929d124cb80eb"
---
# Cyanobacterial limonene-degrader signal is a false positive

The NEON limonene-pathway cohort contains 43 GENERIC_ONLY MAGs carrying K00128 only, including all 14 Planktothrix and Dolichospermum MAGs, making their limonene-degrader signal a false positive. [src: neon_mag_functional_discovery]

## Key figures

- **43**: GENERIC_ONLY MAGs carrying K00128 only [src: neon_mag_functional_discovery]
- **14**: Planktothrix and Dolichospermum MAGs included [src: neon_mag_functional_discovery]

## Evidence

> | **GENERIC_ONLY** (K00128 only) | 43 | The "limonene-degrader" signal is a false positive — only the housekeeping aldehyde dehydrogenase is present. **Includes all 14 Planktothrix and Dolichospermum MAGs.** | [src: neon_mag_functional_discovery]

From the report [[summaries/neon_mag_functional_discovery__REPORT]].

## Caveat

Module-level enrichment should be cross-checked with per-KO step assignment because broad-substrate housekeeping enzymes shared across pathways can alone drive spurious enrichment. [src: neon_mag_functional_discovery]

> **A methodological lesson**: module-level enrichment should always be cross-checked with per-KO step assignment before drawing biological conclusions; broad-substrate housekeeping enzymes (here, an aldehyde dehydrogenase shared by dozens of pathways) can drive spurious module enrichment by themselves. [src: neon_mag_functional_discovery]

## Other caveats in this report

- The NEON H4b per-MAG analysis supports the hypothesis on the available cohort but inherits 53% cohort-attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery]
- Without independent ground-truth from full-length 16S phylogeny against an unbiased reference, the NEON soil novelty result is consistent with either biological novelty or a GTDB coverage gap concentrating in alkaline soils, with the report favoring the latter. [src: neon_mag_functional_discovery]
- The report cautions that habitat enrichment of universal cellular machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, rather than acquisition of novel functional capability. [src: neon_mag_functional_discovery]
- The KBase Data Lakehouse table nmdc_arkin.kegg_module_terms has 370 rows with module_id only and empty name and category fields, limiting NEON habitat interpretation and requiring external KEGG labels for top hits. [src: neon_mag_functional_discovery]
- For the NEON soil two-factor PERMANOVA, p = 0.001 is the smallest permutation p-value attainable with 999 permutations. [src: neon_mag_functional_discovery]
