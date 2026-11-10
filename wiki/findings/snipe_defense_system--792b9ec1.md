---
type: "Finding"
description: "PhageFoundry has ManYZ annotations in Klebsiella (28 ManZ proteins, 4,619 PTS_EIIC Pfam hits) but is GenomeDepot format with genome annotations only and no fitness/TnSeq tables, so Klebsiella-specific fitness remains unmeasured there."
finding_id: "snipe_defense_system--792b9ec1"
result: "null result"
source: "snipe_defense_system"
quantities: [{"value": "28", "what": "ManZ proteins annotated in Klebsiella", "unit": "proteins", "denominator": "", "scope": "PhageFoundry"}, {"value": "4,619", "what": "PTS_EIIC Pfam hits in Klebsiella", "unit": "annotations", "denominator": "", "scope": "PhageFoundry"}]
caveat: "Generating Klebsiella-specific SNIPE or ManYZ fitness data would require new mutant libraries in natural SNIPE-carrying strains such as K. pneumoniae NCTC9140 or HS11286."
first_added: "2026-11-09"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# PhageFoundry has no Klebsiella fitness tables to test SNIPE–ManYZ interplay

PhageFoundry has ManYZ annotations in Klebsiella (28 ManZ proteins, 4,619 PTS_EIIC Pfam hits) but is GenomeDepot format with genome annotations only and no fitness/TnSeq tables, so Klebsiella-specific fitness remains unmeasured there. [src: snipe_defense_system]

## Key figures

- **28 proteins**: ManZ proteins annotated in Klebsiella (scope PhageFoundry) [src: snipe_defense_system]
- **4,619 annotations**: PTS_EIIC Pfam hits in Klebsiella (scope PhageFoundry) [src: snipe_defense_system]

## Evidence

> PhageFoundry has ManYZ annotations in *Klebsiella* (28 ManZ proteins, 4,619 PTS_EIIC Pfam hits — see above), but PhageFoundry is GenomeDepot format (genome annotations only, no fitness/TnSeq tables). [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

Generating Klebsiella-specific SNIPE or ManYZ fitness data would require new mutant libraries in natural SNIPE-carrying strains such as K. pneumoniae NCTC9140 or HS11286. [src: snipe_defense_system]

> Generating *Klebsiella*-specific SNIPE or ManYZ fitness data would require new mutant libraries in natural SNIPE-carrying strains such as *K. pneumoniae* NCTC9140 or HS11286. [src: snipe_defense_system]

## Other caveats in this report

- UniProt's fructose-specific ManX annotation conflicts with the reported Fitness Browser phenotypes. [src: snipe_defense_system]
- Fitness scores are log2 RB-TnSeq ratios; carbon-source conditions were selected by condition_1 and expGroup='carbon source'. [src: snipe_defense_system]
- The report proposes that SNIPE avoids the metabolic cost of man knockouts while blocking phage DNA; this passage does not present a direct comparative fitness measurement. [src: snipe_defense_system]
- Three Klebsiella DUF4041 proteins are 558 aa, matching E. coli SNIPE; their full two-domain architecture is inferred rather than directly confirmed here. [src: snipe_defense_system]
- The query footnote labels PF00358 as PTS_EIIC and PF02378 as PTS_EIID, conflicting with the report's table labels PF00358/PTS_EIIA_1 and PF02378/PTS_EIIC. [src: snipe_defense_system]
