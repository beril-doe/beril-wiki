---
type: "Finding"
description: "NEON functional gene content partitions by habitat with PERMANOVA pseudo-F = 137, p = 0.001, across soil n=1,800, benthic n=618, and water n=88 workflows."
finding_id: "neon_mag_functional_discovery--2a547277"
result: "observation"
source: "neon_mag_functional_discovery"
quantities: [{"value": "137", "what": "PERMANOVA pseudo-F for habitat", "unit": "", "denominator": "", "scope": ""}]
caveat: "Habitat enrichment of universal cellular machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, rather than acquisition of novel functional capability."
first_added: "2026-11-24"
source_hash: "a4bb7071930d6a46f2a824c1d675cf1ceb2dcdeab50b3b8fadd929d124cb80eb"
---
# Functional gene content partitions strongly by NEON habitat

NEON functional gene content partitions by habitat with PERMANOVA pseudo-F = 137, p = 0.001, across soil n=1,800, benthic n=618, and water n=88 workflows. [src: neon_mag_functional_discovery]

## Key figures

- **137**: PERMANOVA pseudo-F for habitat [src: neon_mag_functional_discovery]

## Evidence

> **PERMANOVA pseudo-F = 137, p = 0.001** for habitat (soil n=1,800; benthic n=618; water n=88) — one of the strongest habitat partitions ever measured at this scale on functional gene content [src: neon_mag_functional_discovery]

From the report [[summaries/neon_mag_functional_discovery__REPORT]].

## Caveat

Habitat enrichment of universal cellular machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, rather than acquisition of novel functional capability. [src: neon_mag_functional_discovery]

> These are universal cellular machinery — when one habitat shows enrichment in such modules, it usually reflects a **taxonomic-abundance shift** within the community (e.g., Cyanobacteria over-represented in water) rather than acquisition of a novel functional capability. [src: neon_mag_functional_discovery]

## Other caveats in this report

- The NEON H4b per-MAG analysis supports the hypothesis on the available cohort but inherits 53% cohort-attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery]
- Without independent ground-truth from full-length 16S phylogeny against an unbiased reference, the NEON soil novelty result is consistent with either biological novelty or a GTDB coverage gap concentrating in alkaline soils, with the report favoring the latter. [src: neon_mag_functional_discovery]
- The KBase Data Lakehouse table nmdc_arkin.kegg_module_terms has 370 rows with module_id only and empty name and category fields, limiting NEON habitat interpretation and requiring external KEGG labels for top hits. [src: neon_mag_functional_discovery]
- For the NEON soil two-factor PERMANOVA, p = 0.001 is the smallest permutation p-value attainable with 999 permutations. [src: neon_mag_functional_discovery]
- The report hypothesizes that a nested NEON soil model would capture additional pH × horizon interaction variance, but this unregistered test remains follow-up work. [src: neon_mag_functional_discovery]
