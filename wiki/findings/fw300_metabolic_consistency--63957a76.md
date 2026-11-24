---
type: "Finding"
description: "A binomial test found no significant difference between BacDive utilization of metabolites produced by FW300-N2E3 (3/7 = 43%) and the overall P. fluorescens baseline (22/80 = 27.5%; p = 0.40)."
finding_id: "fw300_metabolic_consistency--63957a76"
result: "null result"
source: "fw300_metabolic_consistency"
quantities: [{"value": "3/7 = 43%", "what": "BacDive utilization of WoM-produced metabolites", "unit": "", "denominator": "", "scope": ""}, {"value": "22/80 = 27.5%", "what": "P. fluorescens baseline utilization", "unit": "", "denominator": "", "scope": ""}, {"value": "p = 0.40", "what": "binomial test p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "BacDive compound coverage varies from 1 to 51 strains under per-strain consensus, and raw record counts can be higher because of duplicate entries per strain."
first_added: "2026-11-24"
source_hash: "7ba873873f7c42649450d7c75e18227257c5c7c8eb2fee052525f3732c997c05"
---
# BacDive utilization of produced metabolites matches species baseline

A binomial test found no significant difference between BacDive utilization of metabolites produced by FW300-N2E3 (3/7 = 43%) and the overall P. fluorescens baseline (22/80 = 27.5%; p = 0.40). [src: fw300_metabolic_consistency]

## Key figures

- **3/7 = 43%**: BacDive utilization of WoM-produced metabolites [src: fw300_metabolic_consistency]
- **22/80 = 27.5%**: P. fluorescens baseline utilization [src: fw300_metabolic_consistency]
- **p = 0.40**: binomial test p-value [src: fw300_metabolic_consistency]

## Evidence

> A binomial test comparing the BacDive utilization rate for WoM-produced metabolites (3/7 = 43%) against the overall *P. fluorescens* baseline (22/80 = 27.5%) shows no significant difference (p = 0.40), indicating that the metabolites FW300-N2E3 produces are utilized at a rate consistent with the species norm. [src: fw300_metabolic_consistency]

From the report [[summaries/fw300_metabolic_consistency__REPORT]].

## Caveat

BacDive compound coverage varies from 1 to 51 strains under per-strain consensus, and raw record counts can be higher because of duplicate entries per strain. [src: fw300_metabolic_consistency]

> This is a general caveat for BacDive-based analyses — compound coverage varies from 1 to 51 strains (per-strain consensus; raw records can be higher due to duplicate entries per strain). [src: fw300_metabolic_consistency]

## Other caveats in this report

- The remaining 37 metabolites (64%) of Pseudomonas FW300-N2E3 were observed only in Web of Microbes and were not tested in BacDive, predicted by GapMind, or used as Fitness Browser conditions for this organism. [src: fw300_metabolic_consistency]
- The report describes the 94% concordance for Pseudomonas FW300-N2E3 as largely structural because Fitness Browser (21/21 = 100%) and GapMind (13/13 = 100%) are invariably concordant with Web of Microbes production. [src: fw300_metabolic_consistency]
- The FW300-N2E3 crosswalk includes two approximate Fitness Browser base-to-nucleoside matches, Cytosine→Cytidine and Uracil→Uridine, flagged with fb_match_quality=approximate. [src: fw300_metabolic_consistency]
- The report interprets pleiotropic amino acid biosynthesis fitness genes in FW300-N2E3 as essential for growth on any minimal medium and as housekeeping fitness rather than substrate-specific metabolism. [src: fw300_metabolic_consistency]
- Lysine Emerged in FW300-N2E3 Web of Microbes data and had BacDive counts 0+/3-, classified Moderate confidence (n=3), with consistent negatives but a small sample. [src: fw300_metabolic_consistency]
