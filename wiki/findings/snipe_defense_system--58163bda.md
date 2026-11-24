---
type: "Finding"
description: "The Fitness Browser contains an archaeal SNIPE protein from Methanococcus maripaludis JJ, locus MMJJ_RS01635, with DUF4041 and Mug113 nuclease domains and 129 experiments of fitness data, described as the first SNIPE homologue with genome-wide knockout phenotypes."
finding_id: "snipe_defense_system--58163bda"
result: "observation"
source: "snipe_defense_system"
quantities: [{"value": "129", "what": "experiments of fitness data", "unit": "experiments", "denominator": "", "scope": "MMJJ_RS01635"}]
caveat: "Methanococcus maripaludis is an archaeon whose phage biology context differs significantly from the Enterobacterales phage lambda system."
first_added: "2026-11-24"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# Archaeal SNIPE protein with genome-wide fitness data found

The Fitness Browser contains an archaeal SNIPE protein from Methanococcus maripaludis JJ, locus MMJJ_RS01635, with DUF4041 and Mug113 nuclease domains and 129 experiments of fitness data, described as the first SNIPE homologue with genome-wide knockout phenotypes. [src: snipe_defense_system]

## Key figures

- **129 experiments**: experiments of fitness data (scope MMJJ_RS01635) [src: snipe_defense_system]

## Evidence

> Notably, the Fitness Browser contains one archaeal SNIPE protein (*Methanococcus maripaludis* JJ, locus MMJJ_RS01635) with both the DUF4041 and Mug113 nuclease domains and 129 experiments of fitness data — the first SNIPE homologue with genome-wide knockout phenotypes. [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

Methanococcus maripaludis is an archaeon whose phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]

> This is the first organism with both a confirmed SNIPE protein and genome-wide fitness data — though as an archaeon, the phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]

## Other caveats in this report

- The report states that the original SNIPE paper named DUF4041 and GIY-YIG without citing Pfam accessions. [src: snipe_defense_system]
- The published ManYZ knockout and coevolution studies used to explain the resistance–metabolic-cost trade-off are not from the KBase Data Lakehouse. [src: snipe_defense_system]
- The KBase Data Lakehouse Fitness Browser API was experiencing a 503 outage during the analysis. [src: snipe_defense_system]
- PhageFoundry provides genome annotations only in GenomeDepot format, with no fitness/TnSeq tables, leaving no Klebsiella-specific SNIPE or ManYZ fitness data in this analysis. [src: snipe_defense_system]
- Generating Klebsiella-specific SNIPE or ManYZ fitness data would require new mutant libraries in natural SNIPE carriers such as Klebsiella pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system]
