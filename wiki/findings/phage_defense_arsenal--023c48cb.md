---
type: "Finding"
description: "All 9 major GTDB bacterial phyla show significant positive partial-\u03c1 between defense-system count and prophage burden after controlling for log\u2081\u2080 genome size within each phylum, ranging from 0.18 in Actinomycetota to 0.53 in Campylobacterota."
finding_id: "phage_defense_arsenal--023c48cb"
result: "observation"
source: "phage_defense_arsenal"
quantities: [{"value": "0.18", "what": "partial \u03c1 in Actinomycetota", "unit": "", "denominator": "", "scope": "GTDB bacterial phylum"}, {"value": "0.53", "what": "partial \u03c1 in Campylobacterota", "unit": "", "denominator": "", "scope": "GTDB bacterial phylum"}]
caveat: "The universal-phylum arms-race pattern applies within the filtered analysis set; extrapolation to the full 293K-genome tree including many environmental MAGs is plausible but untested."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# Defense–prophage association is positive in all nine major phyla

All 9 major GTDB bacterial phyla show significant positive partial-ρ between defense-system count and prophage burden after controlling for log₁₀ genome size within each phylum, ranging from 0.18 in Actinomycetota to 0.53 in Campylobacterota. [src: phage_defense_arsenal]

## Key figures

- **0.18**: partial ρ in Actinomycetota (scope GTDB bacterial phylum) [src: phage_defense_arsenal]
- **0.53**: partial ρ in Campylobacterota (scope GTDB bacterial phylum) [src: phage_defense_arsenal]

## Evidence

> all 9 major GTDB phyla show significant positive partial-ρ (0.18 Actinomycetota → 0.53 Campylobacterota) between defense-system count and prophage burden after controlling for log₁₀ genome size within each phylum. [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

The universal-phylum arms-race pattern applies within the filtered analysis set; extrapolation to the full 293K-genome tree including many environmental MAGs is plausible but untested. [src: phage_defense_arsenal]

> The universal-phylum arms-race pattern applies within this analysis set; extrapolation to the full 293K-genome tree (which includes many MAGs from environmental samples) is plausible but untested here. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- The report warns that CRISPR prevalence comparisons must specify detection method because the two approaches differ by 40-percentage-point on the same pangenome. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
