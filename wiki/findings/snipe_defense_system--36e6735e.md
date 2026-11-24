---
type: "Finding"
description: "A Pfam-domain survey of the 293K-genome KBase Data Lakehouse pangenome found SNIPE homologues in 1,696 species across 33 phyla, compared with >500 reported in the original paper (Saxton et al. 2026)."
finding_id: "snipe_defense_system--36e6735e"
result: "observation"
source: "snipe_defense_system"
quantities: [{"value": "1,696", "what": "species with SNIPE homologues", "unit": "species", "denominator": "", "scope": "293K-genome pangenome"}, {"value": "33", "what": "phyla with SNIPE homologues", "unit": "phyla", "denominator": "", "scope": ""}, {"value": ">500", "what": "homologues reported in original paper", "unit": "", "denominator": "", "scope": "Saxton et al. 2026"}]
caveat: "DUF4041 (T5orf172) is strongly associated with SNIPE, but some hits may represent non-SNIPE proteins."
first_added: "2026-11-24"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# SNIPE homologues far more widespread than originally reported

A Pfam-domain survey of the 293K-genome KBase Data Lakehouse pangenome found SNIPE homologues in 1,696 species across 33 phyla, compared with >500 reported in the original paper (Saxton et al. 2026). [src: snipe_defense_system]

## Key figures

- **1,696 species**: species with SNIPE homologues (scope 293K-genome pangenome) [src: snipe_defense_system]
- **33 phyla**: phyla with SNIPE homologues [src: snipe_defense_system]
- **>500**: homologues reported in original paper (scope Saxton et al. 2026) [src: snipe_defense_system]

## Evidence

> We surveyed the 293K-genome BERDL pangenome for SNIPE homologues using Pfam domain annotations and found them in **1,696 species across 33 phyla** — far more than the >500 reported in the original paper (Saxton et al. 2026, *Nature*). [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

DUF4041 (T5orf172) is strongly associated with SNIPE, but some hits may represent non-SNIPE proteins. [src: snipe_defense_system]

> **DUF4041 specificity**: while DUF4041 (T5orf172) is strongly associated with SNIPE, some hits may represent non-SNIPE proteins [src: snipe_defense_system]

## Other caveats in this report

- The report states that the original SNIPE paper named DUF4041 and GIY-YIG without citing Pfam accessions. [src: snipe_defense_system]
- The published ManYZ knockout and coevolution studies used to explain the resistance–metabolic-cost trade-off are not from the KBase Data Lakehouse. [src: snipe_defense_system]
- Methanococcus maripaludis is an archaeon whose phage biology context differs significantly from the Enterobacterales phage lambda system. [src: snipe_defense_system]
- The KBase Data Lakehouse Fitness Browser API was experiencing a 503 outage during the analysis. [src: snipe_defense_system]
- PhageFoundry provides genome annotations only in GenomeDepot format, with no fitness/TnSeq tables, leaving no Klebsiella-specific SNIPE or ManYZ fitness data in this analysis. [src: snipe_defense_system]
