---
type: "Finding"
description: "CRISPR-Cas \u00d7 CBASS was the only defense pair not reaching significance (z = 0.21, p_emp = 0.98), with CBASS essentially independent of CRISPR-Cas presence."
finding_id: "phage_defense_arsenal--8c6a7f5f"
result: "null result"
source: "phage_defense_arsenal"
quantities: [{"value": "0.21", "what": "z", "unit": "", "denominator": "", "scope": "CRISPR-Cas \u00d7 CBASS"}, {"value": "0.98", "what": "empirical p", "unit": "", "denominator": "", "scope": ""}]
caveat: "CRISPR-Cas prevalence (96 %) is inflated by permissive eggNOG description-based matching; Pfam Cas1 (PF01867) is present in only 55 % of species."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# CBASS occurrence is independent of CRISPR-Cas

CRISPR-Cas × CBASS was the only defense pair not reaching significance (z = 0.21, p_emp = 0.98), with CBASS essentially independent of CRISPR-Cas presence. [src: phage_defense_arsenal]

## Key figures

- **0.21**: z (scope CRISPR-Cas × CBASS) [src: phage_defense_arsenal]
- **0.98**: empirical p [src: phage_defense_arsenal]

## Evidence

> The only pair that does not reach significance is **CRISPR-Cas × CBASS** (z = 0.21, p_emp = 0.98) — the two systems with the largest prevalence gap (96 % vs 7 %), where CBASS is essentially independent of CRISPR-Cas presence. [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

CRISPR-Cas prevalence (96 %) is inflated by permissive eggNOG description-based matching; Pfam Cas1 (PF01867) is present in only 55 % of species. [src: phage_defense_arsenal]

> **CRISPR-Cas prevalence (96 %) is inflated** by permissive eggNOG description-based matching. The Pfam Cas1 (PF01867) hit is only present in 55 % of species. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- The report warns that CRISPR prevalence comparisons must specify detection method because the two approaches differ by 40-percentage-point on the same pangenome. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
