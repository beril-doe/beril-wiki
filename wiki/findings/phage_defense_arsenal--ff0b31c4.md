---
type: "Finding"
description: "In the same pangenome dataset, eggNOG description matches yield 96 % species prevalence for CRISPR versus ~55 % using the specific Cas1 Pfam (PF01867)."
finding_id: "phage_defense_arsenal--ff0b31c4"
result: "correction"
source: "phage_defense_arsenal"
quantities: [{"value": "96 %", "what": "CRISPR species prevalence by eggNOG description", "unit": "", "denominator": "", "scope": ""}, {"value": "~55 %", "what": "CRISPR species prevalence by Cas1 Pfam PF01867", "unit": "", "denominator": "", "scope": ""}]
caveat: "Any downstream pangenome project comparing CRISPR prevalence across studies must specify the detection method; the 40-percentage-point gap on the same pangenome is an interpretation trap."
first_added: "2026-11-24"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# eggNOG-based CRISPR detection greatly overstates prevalence versus Cas1 Pfam

In the same pangenome dataset, eggNOG description matches yield 96 % species prevalence for CRISPR versus ~55 % using the specific Cas1 Pfam (PF01867). [src: phage_defense_arsenal]

## Key figures

- **96 %**: CRISPR species prevalence by eggNOG description [src: phage_defense_arsenal]
- **~55 %**: CRISPR species prevalence by Cas1 Pfam PF01867 [src: phage_defense_arsenal]

## Evidence

> **eggNOG description-based CRISPR detection dramatically over-counts** — 96 % species prevalence via eggNOG description matches vs ~55 % using the specific Cas1 Pfam (PF01867). [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

Any downstream pangenome project comparing CRISPR prevalence across studies must specify the detection method; the 40-percentage-point gap on the same pangenome is an interpretation trap. [src: phage_defense_arsenal]

> Any downstream pangenome project comparing CRISPR prevalence numbers across studies must specify which detection method they used; the 40-percentage-point gap between these two approaches on the *same* pangenome is a real interpretation trap. [src: phage_defense_arsenal]

## Other caveats in this report

- The bacterial arms-race and syndrome tests used the ≥5-genome analysis set because reliable core/accessory calls require ≥5 sequenced genomes per species. [src: phage_defense_arsenal]
- The report attributes DISARM's near-baseline core fraction almost certainly to detection artefact because its DrmB SNF2 helicase Pfam anchor PF00176 is a widespread housekeeping-helicase domain that inflates the DISARM cluster set with non-mobile SNF2 helicases. [src: phage_defense_arsenal]
- bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 hits there versus ~25K in InterProScan. [src: phage_defense_arsenal]
- Cross-database Pfam joins must strip versions on the Bakta side; this mismatch was undocumented in docs/pitfalls.md for kbase_ke_pangenome and cost ~15 min of debugging. [src: phage_defense_arsenal]
- Spark Connect .write.parquet() writes to cluster storage (S3), not the client-side notebook filesystem, and can report success while leaving only an empty local _SUCCESS marker. [src: phage_defense_arsenal]
