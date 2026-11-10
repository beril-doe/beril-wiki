---
type: "Finding"
description: "bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 there but ~25K in InterProScan."
finding_id: "phage_defense_arsenal--707f57b3"
result: "null result"
source: "phage_defense_arsenal"
quantities: [{"value": "0", "what": "Cas1 PF01867 hits in bakta_pfam_domains", "unit": "hits", "denominator": "", "scope": ""}, {"value": "~25K", "what": "Cas1 PF01867 hits in InterProScan", "unit": "hits", "denominator": "", "scope": ""}]
caveat: "The two tables use different Pfam accession formats (version-free PF01867 in InterProScan, versioned PF01867.29 in Bakta), so cross-database joins must strip versions on the Bakta side."
first_added: "2026-11-09"
source_hash: "9d450a848b83b2462d07d216ef01827f8a08f8e1c4fcddcdf74cfdb7dbcbe601"
---
# Bakta Pfam table misses classical defense markers such as Cas1

bakta_pfam_domains misses classical defense markers: CRISPR Cas1 PF01867 returns 0 there but ~25K in InterProScan. [src: phage_defense_arsenal]

## Key figures

- **0 hits**: Cas1 PF01867 hits in bakta_pfam_domains [src: phage_defense_arsenal]
- **~25K hits**: Cas1 PF01867 hits in InterProScan [src: phage_defense_arsenal]

## Evidence

> `bakta_pfam_domains` misses classical defense markers (e.g., CRISPR Cas1 PF01867 returns 0 there but ~25K in InterProScan). [src: phage_defense_arsenal]

From the report [[summaries/phage_defense_arsenal__REPORT]].

## Caveat

The two tables use different Pfam accession formats (version-free PF01867 in InterProScan, versioned PF01867.29 in Bakta), so cross-database joins must strip versions on the Bakta side. [src: phage_defense_arsenal]

> **`interproscan_domains.signature_acc` uses version-free Pfam accessions (`PF01867`), while `bakta_pfam_domains.pfam_id` uses versioned accessions (`PF01867.29`)**. Cross-database Pfam joins must strip versions on the Bakta side. [src: phage_defense_arsenal]

## Other caveats in this report

- Arms-race and syndrome tests use species with at least five sequenced genomes. [src: phage_defense_arsenal]
- The DISARM accessory-enrichment estimate is likely affected by nonspecific PF00176 DrmB/SNF2 helicase detection. [src: phage_defense_arsenal]
- The report argues that the DISARM per-cluster caveat does not undermine its species-level arms-race and syndrome results. [src: phage_defense_arsenal]
- The arms-race association varies by phylum; the Actinomycetota effect is described as roughly threefold weaker than the Campylobacterota effect. [src: phage_defense_arsenal]
- CRISPR-Cas prevalence is method-dependent: eggNOG description matching gives 96 %, versus ~55 % with Cas1 PF01867. [src: phage_defense_arsenal]
