---
type: "Finding"
description: "The report finds that 86.7% of SNIPE genes are accessory or singleton, consistent with mobile defense island carriage."
finding_id: "snipe_defense_system--b75e826b"
result: "inference"
source: "snipe_defense_system"
quantities: [{"value": "86.7%", "what": "SNIPE genes that are accessory or singleton", "unit": "%", "denominator": "", "scope": "DUF4041 gene clusters"}]
caveat: "The remaining ~20% (897 clusters) with unrelated primary annotations likely represent annotation noise rather than functional SNIPE proteins."
first_added: "2026-11-24"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# Most SNIPE genes are accessory, suggesting mobile defense islands

The report finds that 86.7% of SNIPE genes are accessory or singleton, consistent with mobile defense island carriage. [src: snipe_defense_system]

## Key figures

- **86.7%**: SNIPE genes that are accessory or singleton (scope DUF4041 gene clusters) [src: snipe_defense_system]

## Evidence

> 86.7% of SNIPE genes are accessory or singleton, consistent with mobile defense island carriage. [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

The remaining ~20% (897 clusters) with unrelated primary annotations likely represent annotation noise rather than functional SNIPE proteins. [src: snipe_defense_system]

> The remaining ~20% (897 clusters) have primary annotations like Histidine kinase (319) and seryl-tRNA aminoacylation (238), suggesting DUF4041 was detected as a secondary/minor domain in multi-domain proteins whose primary function is unrelated to phage defense. These likely represent annotation noise rather than functional SNIPE proteins. [src: snipe_defense_system]

## Other caveats in this report

- The report states that the original SNIPE paper named DUF4041 and GIY-YIG without citing Pfam accessions. [src: snipe_defense_system]
- The published ManYZ knockout and coevolution studies used to explain the resistance–metabolic-cost trade-off are not from the KBase Data Lakehouse. [src: snipe_defense_system]
- Methanococcus maripaludis is an archaeon whose phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]
- The KBase Data Lakehouse Fitness Browser API was experiencing a 503 outage during the analysis. [src: snipe_defense_system]
- PhageFoundry provides genome annotations only in GenomeDepot format, with no fitness/TnSeq tables, leaving no Klebsiella-specific SNIPE or ManYZ fitness data in this analysis. [src: snipe_defense_system]
