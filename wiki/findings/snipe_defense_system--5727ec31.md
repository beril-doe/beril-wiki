---
type: "Finding"
description: "The survey detected DUF4041 (PF13250, InterPro IPR025280), the diagnostic SNIPE domain, in 4,572 gene clusters across 1,696 species spanning 33 bacterial and archaeal phyla, which substantially expands the >500 homologues reported in the original paper."
finding_id: "snipe_defense_system--5727ec31"
result: "observation"
source: "snipe_defense_system"
quantities: [{"value": "4,572", "what": "DUF4041 gene clusters detected", "unit": "gene clusters", "denominator": "", "scope": "pangenome survey"}, {"value": "1,696", "what": "species carrying DUF4041", "unit": "species", "denominator": "", "scope": "33 bacterial and archaeal phyla"}, {"value": "33", "what": "bacterial and archaeal phyla with DUF4041", "unit": "phyla", "denominator": "", "scope": ""}, {"value": ">500", "what": "homologues reported in the original paper", "unit": "homologues", "denominator": "", "scope": "original paper"}]
caveat: "The report estimates that 3,675/4,572 (80.4%) of DUF4041 clusters are SNIPE-family proteins, while the remaining ~20% (897 clusters) may be non-SNIPE multi-domain proteins or annotation noise."
first_added: "2026-11-09"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# DUF4041 SNIPE domain is far more widespread than originally reported

The survey detected DUF4041 (PF13250, InterPro IPR025280), the diagnostic SNIPE domain, in 4,572 gene clusters across 1,696 species spanning 33 bacterial and archaeal phyla, which substantially expands the >500 homologues reported in the original paper. [src: snipe_defense_system]

## Key figures

- **4,572 gene clusters**: DUF4041 gene clusters detected (scope pangenome survey) [src: snipe_defense_system]
- **1,696 species**: species carrying DUF4041 (scope 33 bacterial and archaeal phyla) [src: snipe_defense_system]
- **33 phyla**: bacterial and archaeal phyla with DUF4041 [src: snipe_defense_system]
- **>500 homologues**: homologues reported in the original paper (scope original paper) [src: snipe_defense_system]

## Evidence

> DUF4041 (PF13250, InterPro [IPR025280](https://www.ebi.ac.uk/interpro/entry/InterPro/IPR025280/)), the diagnostic SNIPE domain, was detected in **4,572 gene clusters** across **1,696 species** spanning **33 bacterial and archaeal phyla**. This substantially expands the >500 homologues reported in the original paper. [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

The report estimates that 3,675/4,572 (80.4%) of DUF4041 clusters are SNIPE-family proteins, while the remaining ~20% (897 clusters) may be non-SNIPE multi-domain proteins or annotation noise. [src: snipe_defense_system]

> **False-positive estimate**: The top two descriptions — T5orf172 (2,109) and DUF4041 (1,566) — account for 3,675/4,572 clusters (80.4%) and represent bona fide SNIPE-family proteins. The remaining ~20% (897 clusters) have primary annotations like Histidine kinase (319) and seryl-tRNA aminoacylation (238), suggesting DUF4041 was detected as a secondary/minor domain in multi-domain proteins whose primary function is unrelated to phage defense. These likely represent annotation noise rather than functional SNIPE proteins. [src: snipe_defense_system]

## Other caveats in this report

- UniProt's fructose-specific ManX annotation conflicts with the reported Fitness Browser phenotypes. [src: snipe_defense_system]
- Fitness scores are log2 RB-TnSeq ratios; carbon-source conditions were selected by condition_1 and expGroup='carbon source'. [src: snipe_defense_system]
- The report proposes that SNIPE avoids the metabolic cost of man knockouts while blocking phage DNA; this passage does not present a direct comparative fitness measurement. [src: snipe_defense_system]
- Three Klebsiella DUF4041 proteins are 558 aa, matching E. coli SNIPE; their full two-domain architecture is inferred rather than directly confirmed here. [src: snipe_defense_system]
- The query footnote labels PF00358 as PTS_EIIC and PF02378 as PTS_EIID, conflicting with the report's table labels PF00358/PTS_EIIA_1 and PF02378/PTS_EIIC. [src: snipe_defense_system]
