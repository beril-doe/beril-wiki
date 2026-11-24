---
type: "Finding"
description: "Under a phylum-stratified column-permutation null (N = 1,000 permutations), 27 of 28 tested defense-system pairs show significant positive co-occurrence at BH-FDR q < 0.05."
finding_id: "phage_defense_arsenal--e530a309"
result: "observation"
source: "phage_defense_arsenal"
quantities: [{"value": "27 of 28", "what": "defense-system pairs with significant positive co-occurrence", "unit": "pairs", "denominator": "28 tested pairs", "scope": "BH-FDR q < 0.05"}]
caveat: "Retron detection uses only RVT_1 (PF00078), a broad reverse-transcriptase Pfam."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# Nearly all defense-system pairs co-occur more than expected

Under a phylum-stratified column-permutation null (N = 1,000 permutations), 27 of 28 tested defense-system pairs show significant positive co-occurrence at BH-FDR q < 0.05. [src: phage_defense_arsenal]

## Key figures

- **27 of 28 pairs**: defense-system pairs with significant positive co-occurrence (denominator 28 tested pairs; scope BH-FDR q < 0.05) [src: phage_defense_arsenal]

## Evidence

> Under a phylum-stratified column-permutation null (N = 1,000 permutations), **27 of 28 tested defense-system pairs** show significant positive co-occurrence at BH-FDR q < 0.05 (`data/syndrome_pairs.tsv`). [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

Retron detection uses only RVT_1 (PF00078), a broad reverse-transcriptase Pfam. [src: phage_defense_arsenal]

> **Retron detection uses only RVT_1 (PF00078)** — a broad reverse-transcriptase Pfam. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- The report warns that CRISPR prevalence comparisons must specify detection method because the two approaches differ by 40-percentage-point on the same pangenome. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
