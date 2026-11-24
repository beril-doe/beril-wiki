---
type: "Finding"
description: "The top 18 FW300-N2E3 fitness genes are significant across all 21 metabolite conditions because they encode essential histidine, leucine, methionine, and aromatic amino acid biosynthesis rather than substrate-specific catabolism."
finding_id: "fw300_metabolic_consistency--cd02f79c"
result: "observation"
source: "fw300_metabolic_consistency"
quantities: [{"value": "18", "what": "genes significant in all 21 conditions", "unit": "", "denominator": "", "scope": ""}, {"value": "21", "what": "metabolite conditions", "unit": "", "denominator": "", "scope": ""}]
caveat: "The fitness signal contains both housekeeping and substrate-specific components that the report recommends separating in future WoM\u2013Fitness Browser integration."
first_added: "2026-11-24"
source_hash: "7ba873873f7c42649450d7c75e18227257c5c7c8eb2fee052525f3732c997c05"
---
# Top fitness genes reflect housekeeping amino acid biosynthesis, not substrate-specific catabolism

The top 18 FW300-N2E3 fitness genes are significant across all 21 metabolite conditions because they encode essential histidine, leucine, methionine, and aromatic amino acid biosynthesis rather than substrate-specific catabolism. [src: fw300_metabolic_consistency]

## Key figures

- **18**: genes significant in all 21 conditions [src: fw300_metabolic_consistency]
- **21**: metabolite conditions [src: fw300_metabolic_consistency]

## Evidence

> The top 18 fitness genes are significant across all 21 metabolite conditions because they are essential amino acid biosynthesis genes (histidine, leucine, methionine, aromatic amino acids), not substrate-specific catabolism genes. [src: fw300_metabolic_consistency]

From the report [[summaries/fw300_metabolic_consistency__REPORT]].

## Caveat

The fitness signal contains both housekeeping and substrate-specific components that the report recommends separating in future WoM–Fitness Browser integration. [src: fw300_metabolic_consistency]

> The fitness signal contains both "housekeeping" and "substrate-specific" components; future work should separate these to sharpen the WoM↔FB integration. [src: fw300_metabolic_consistency]

## Other caveats in this report

- The remaining 37 metabolites (64%) of Pseudomonas FW300-N2E3 were observed only in Web of Microbes and were not tested in BacDive, predicted by GapMind, or used as Fitness Browser conditions for this organism. [src: fw300_metabolic_consistency]
- The report describes the 94% concordance for Pseudomonas FW300-N2E3 as largely structural because Fitness Browser (21/21 = 100%) and GapMind (13/13 = 100%) are invariably concordant with Web of Microbes production. [src: fw300_metabolic_consistency]
- The FW300-N2E3 crosswalk includes two approximate Fitness Browser base-to-nucleoside matches, Cytosine→Cytidine and Uracil→Uridine, flagged with fb_match_quality=approximate. [src: fw300_metabolic_consistency]
- The report interprets pleiotropic amino acid biosynthesis fitness genes in FW300-N2E3 as essential for growth on any minimal medium and as housekeeping fitness rather than substrate-specific metabolism. [src: fw300_metabolic_consistency]
- Lysine Emerged in FW300-N2E3 Web of Microbes data and had BacDive counts 0+/3-, classified Moderate confidence (n=3), with consistent negatives but a small sample. [src: fw300_metabolic_consistency]
