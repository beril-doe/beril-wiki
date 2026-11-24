---
type: "Finding"
description: "R-M Type II \u00d7 Gabija is the strongest pan-bacterial defense syndrome in the report, with odds ratio \u2248 24 and z \u2248 46 under a phylum-preserving null; the two systems co-occur in 2,429 of 4,096 R-M Type II-carrying species (59 %) vs an expected 1,555 (38 %)."
finding_id: "phage_defense_arsenal--606107b1"
result: "observation"
source: "phage_defense_arsenal"
quantities: [{"value": "2,429", "what": "observed co-occurring species", "unit": "species", "denominator": "4,096 R-M Type II-carrying species", "scope": ""}, {"value": "1,555", "what": "expected co-occurrence under null", "unit": "species", "denominator": "", "scope": ""}]
caveat: "Prevalence numbers should be interpreted as an upper bound; the syndrome analysis uses the combined presence set (eggNOG OR Pfam) which favours recall."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# R-M Type II and Gabija form the strongest defense syndrome

R-M Type II × Gabija is the strongest pan-bacterial defense syndrome in the report, with odds ratio ≈ 24 and z ≈ 46 under a phylum-preserving null; the two systems co-occur in 2,429 of 4,096 R-M Type II-carrying species (59 %) vs an expected 1,555 (38 %). [src: phage_defense_arsenal]

## Key figures

- **2,429 species**: observed co-occurring species (denominator 4,096 R-M Type II-carrying species) [src: phage_defense_arsenal]
- **1,555 species**: expected co-occurrence under null [src: phage_defense_arsenal]

## Evidence

> **R-M Type II × Gabija is the strongest pan-bacterial defense syndrome to date** — odds ratio ≈ 24 with z ≈ 46 under a phylum-preserving null; the two systems co-occur in 2,429 of 4,096 R-M Type II-carrying species (59 %) vs an expected 1,555 (38 %). [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

Prevalence numbers should be interpreted as an upper bound; the syndrome analysis uses the combined presence set (eggNOG OR Pfam) which favours recall. [src: phage_defense_arsenal]

> Prevalence numbers in Finding 1 should be interpreted as an upper bound; the syndrome analysis uses the combined presence set (eggNOG OR Pfam) which favours recall, meaning CRISPR-Cas syndromes may be slightly underestimated in specificity but not in significance. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- The report warns that CRISPR prevalence comparisons must specify detection method because the two approaches differ by 40-percentage-point on the same pangenome. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
