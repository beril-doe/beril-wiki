---
type: "Finding"
description: "NEON cyanobacterial Planktothrix and Dolichospermum MAGs and uncultured peat-soil Palsa-465, Palsa-295, and Sulfotelmatobacter MAGs carry hundreds of accessory KOs absent from any cultured representative of their genus."
finding_id: "neon_mag_functional_discovery--3849de7c"
result: "observation"
source: "neon_mag_functional_discovery"
quantities: []
caveat: "The per-MAG re-analysis (H4b) supports the hypothesis on the available cohort but inherits a 53% cohort-attrition from a habitat-biased gap in NMDC's per-gene annotation tables."
first_added: "2026-11-24"
source_hash: "a4bb7071930d6a46f2a824c1d675cf1ceb2dcdeab50b3b8fadd929d124cb80eb"
---
# Field MAGs carry hundreds of accessory KOs absent from cultured relatives

NEON cyanobacterial Planktothrix and Dolichospermum MAGs and uncultured peat-soil Palsa-465, Palsa-295, and Sulfotelmatobacter MAGs carry hundreds of accessory KOs absent from any cultured representative of their genus. [src: neon_mag_functional_discovery]

## Evidence

> **Cyanobacterial (Planktothrix, Dolichospermum) and uncultured peat-soil (Palsa-465, Palsa-295, Sulfotelmatobacter) MAGs carry hundreds of accessory KOs absent from any cultured representative of their genus**, with KEGG-module enrichments for Photosystem I & II (M00161, M00163), the Calvin cycle (M00165), lycopene biosynthesis (M00097), and niche-specific transport systems (M00202 oligopeptide, M00220 rhamnose, M00246 nickel). [src: neon_mag_functional_discovery]

From the report [[summaries/neon_mag_functional_discovery__REPORT]].

## Caveat

The per-MAG re-analysis (H4b) supports the hypothesis on the available cohort but inherits a 53% cohort-attrition from a habitat-biased gap in NMDC's per-gene annotation tables. [src: neon_mag_functional_discovery]

> The per-MAG re-analysis (H4b) supports the hypothesis on the available cohort but inherits a **53% cohort-attrition** from a habitat-biased gap in NMDC's per-gene annotation tables — itself a project-level finding worth capturing as a pitfall for any downstream per-MAG NMDC work. [src: neon_mag_functional_discovery]

## Other caveats in this report

- Without independent ground-truth from full-length 16S phylogeny against an unbiased reference, the NEON soil novelty result is consistent with either biological novelty or a GTDB coverage gap concentrating in alkaline soils, with the report favoring the latter. [src: neon_mag_functional_discovery]
- The report cautions that habitat enrichment of universal cellular machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, rather than acquisition of novel functional capability. [src: neon_mag_functional_discovery]
- The KBase Data Lakehouse table nmdc_arkin.kegg_module_terms has 370 rows with module_id only and empty name and category fields, limiting NEON habitat interpretation and requiring external KEGG labels for top hits. [src: neon_mag_functional_discovery]
- For the NEON soil two-factor PERMANOVA, p = 0.001 is the smallest permutation p-value attainable with 999 permutations. [src: neon_mag_functional_discovery]
- The report hypothesizes that a nested NEON soil model would capture additional pH × horizon interaction variance, but this unregistered test remains follow-up work. [src: neon_mag_functional_discovery]
