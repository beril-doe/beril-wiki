---
type: "Finding"
description: "After residualizing bacterial defense-system count and prophage burden on log\u2081\u2080(median genome size) and phylum, partial \u03c1 remained 0.301 (p = 1.6 \u00d7 10\u207b\u00b9\u2075\u00b3)."
finding_id: "phage_defense_arsenal--45162b93"
result: "observation"
source: "phage_defense_arsenal"
quantities: [{"value": "0.301", "what": "partial Spearman \u03c1 between defense-system count and prophage burden", "unit": "", "denominator": "", "scope": "bacterial species, after residualizing on log\u2081\u2080 genome size and phylum"}]
caveat: "The current results should be interpreted as consistent with, but not as a formal test of, a phylogenetically-independent arms race."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# Defense burden tracks prophage burden beyond genome size and phylum

After residualizing bacterial defense-system count and prophage burden on log₁₀(median genome size) and phylum, partial ρ remained 0.301 (p = 1.6 × 10⁻¹⁵³). [src: phage_defense_arsenal]

## Key figures

- **0.301**: partial Spearman ρ between defense-system count and prophage burden (scope bacterial species, after residualizing on log₁₀ genome size and phylum) [src: phage_defense_arsenal]

## Evidence

> After residualizing on log₁₀(median genome size) and phylum, partial ρ remains **0.301** (p = 1.6 × 10⁻¹⁵³) — a moderate effect that survives the two strongest known confounders. [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

The current results should be interpreted as consistent with, but not as a formal test of, a phylogenetically-independent arms race. [src: phage_defense_arsenal]

> The current results should be interpreted as consistent with, but not as a formal test of, a phylogenetically-independent arms race. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- The report warns that CRISPR prevalence comparisons must specify detection method because the two approaches differ by 40-percentage-point on the same pangenome. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
