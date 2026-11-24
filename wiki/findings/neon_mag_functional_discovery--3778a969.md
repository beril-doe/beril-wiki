---
type: "Finding"
description: "Lineage novelty among NEON soil MQ+HQ MAGs increases with pH, which is opposite the report's literature prior that acidic and peat-bog soils harbor the most novel and uncultured lineages."
finding_id: "neon_mag_functional_discovery--3778a969"
result: "correction"
source: "neon_mag_functional_discovery"
quantities: []
caveat: "Without independent ground-truth from full-length 16S phylogeny against an unbiased reference, the result is consistent with both true novelty in alkaline soils and a GTDB coverage gap there, and the report considers the latter more likely."
first_added: "2026-11-24"
source_hash: "a4bb7071930d6a46f2a824c1d675cf1ceb2dcdeab50b3b8fadd929d124cb80eb"
---
# Soil MAG novelty rises with pH, opposite the acidic-soil prior

Lineage novelty among NEON soil MQ+HQ MAGs increases with pH, which is opposite the report's literature prior that acidic and peat-bog soils harbor the most novel and uncultured lineages. [src: neon_mag_functional_discovery]

## Evidence

> **Direction is opposite the literature prior.** Soil microbial ecology has long pointed at acidic / peat-bog soils as harboring the most novel and uncultured lineages (Fierer & Jackson 2006; Lauber et al. 2009). [src: neon_mag_functional_discovery]

From the report [[summaries/neon_mag_functional_discovery__REPORT]].

## Caveat

Without independent ground-truth from full-length 16S phylogeny against an unbiased reference, the result is consistent with both true novelty in alkaline soils and a GTDB coverage gap there, and the report considers the latter more likely. [src: neon_mag_functional_discovery]

> Without an independent ground-truth (full-length 16S phylogeny against an unbiased reference), the result is consistent with both "true biological novelty concentrates in alkaline soils" and "GTDB coverage gap concentrates in alkaline soils"; the latter is more likely. [src: neon_mag_functional_discovery]

## Other caveats in this report

- The NEON H4b per-MAG analysis supports the hypothesis on the available cohort but inherits 53% cohort-attrition from a habitat-biased gap in NMDC per-gene annotation tables. [src: neon_mag_functional_discovery]
- The report cautions that habitat enrichment of universal cellular machinery usually reflects a taxonomic-abundance shift, such as Cyanobacteria over-represented in water, rather than acquisition of novel functional capability. [src: neon_mag_functional_discovery]
- The KBase Data Lakehouse table nmdc_arkin.kegg_module_terms has 370 rows with module_id only and empty name and category fields, limiting NEON habitat interpretation and requiring external KEGG labels for top hits. [src: neon_mag_functional_discovery]
- For the NEON soil two-factor PERMANOVA, p = 0.001 is the smallest permutation p-value attainable with 999 permutations. [src: neon_mag_functional_discovery]
- The report hypothesizes that a nested NEON soil model would capture additional pH × horizon interaction variance, but this unregistered test remains follow-up work. [src: neon_mag_functional_discovery]
