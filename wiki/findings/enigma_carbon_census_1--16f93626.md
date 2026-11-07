---
type: "Finding"
description: "Even for the enriched phenylethylamine pairs the Jaccard stays \u2248 0.04 (only ~4% of genomes with either capacity carry both), and only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic capacity."
finding_id: "enigma_carbon_census_1--16f93626"
result: "observation"
source: "enigma_carbon_census_1"
quantities: [{"value": "25 of 3109", "what": "genomes carrying both an aromatic and a non-aromatic capacity", "unit": "genomes", "denominator": "3109 genomes", "scope": ""}, {"value": "0.8%", "what": "share of genomes carrying both capacity types", "unit": "", "denominator": "3109 genomes", "scope": ""}, {"value": "\u2248 0.04", "what": "Jaccard index for the enriched pairs", "unit": "", "denominator": "", "scope": "enriched pairs"}]
caveat: "The first-pass \u03c6 coefficient compresses toward zero when a capacity is rare (most are present in tens-to-hundreds of 3109 genomes), so the reanalysis used Haldane-corrected odds ratios with 95% CI and Jaccard indices from saved 2\u00d72 counts."
first_added: "2026-10-27"
source_hash: "62204d5c4271f61cef9bd5c3aee8b1410bebd0a60d508276d2875691a7194f49"
---
# Aromatic and non-aromatic capacities almost never occur in the same genome

Even for the enriched phenylethylamine pairs the Jaccard stays ≈ 0.04 (only ~4% of genomes with either capacity carry both), and only 25 of 3109 genomes (0.8%) carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1]

## Key figures

- **25 of 3109 genomes**: genomes carrying both an aromatic and a non-aromatic capacity (denominator 3109 genomes) [src: enigma_carbon_census_1]
- **0.8%**: share of genomes carrying both capacity types (denominator 3109 genomes) [src: enigma_carbon_census_1]
- **≈ 0.04**: Jaccard index for the enriched pairs (scope enriched pairs) [src: enigma_carbon_census_1]

## Evidence

> Crucially the **Jaccard stays ≈ 0.04** even for these enriched pairs — only ~4% of genomes with either capacity carry both — and only **25 of 3109 genomes (0.8%)** carry both an aromatic and a non-aromatic capacity. [src: enigma_carbon_census_1]

From the report [[summaries/enigma_carbon_census_1__REPORT]].

## Caveat

The first-pass φ coefficient compresses toward zero when a capacity is rare (most are present in tens-to-hundreds of 3109 genomes), so the reanalysis used Haldane-corrected odds ratios with 95% CI and Jaccard indices from saved 2×2 counts. [src: enigma_carbon_census_1]

> NB05 first reported co-occurrence with the **φ coefficient**, but φ compresses toward zero when a capacity is rare (most are present in tens-to-hundreds of 3109 genomes), which can hide a real multiplicative enrichment. Review I4 (NB05b) recomputes two interpretable effect sizes per pair from the saved 2×2 counts — a **Haldane-corrected odds ratio + 95% CI** and the **Jaccard index** — with no Spark re-run. [src: enigma_carbon_census_1]

## Other caveats in this report

- Lauric acid's measured-fitness organism is a reference bacterium, not an ENIGMA isolate. [src: enigma_carbon_census_1]
- Resource darkness is not evidence of biological absence; a shallow PubMed title screen yielded zero literature rescues. [src: enigma_carbon_census_1]
- Xanthine's R02107 reaction reflects purine nitrogen acquisition, not carbon catabolism; the effective carbon-callable count is 8 rather than 9. [src: enigma_carbon_census_1]
- The class-gradient analysis is underpowered and confounded by uneven annotation coverage. [src: enigma_carbon_census_1]
- The 34 all-high-certainty terephthalic-acid calls reflect a single-reaction-signature artifact, not stronger evidence. [src: enigma_carbon_census_1]
