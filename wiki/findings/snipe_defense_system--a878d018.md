---
type: "Finding"
description: "InterPro/UniProt analysis of the E. coli SNIPE protein (A0A0A1A5Z2) shows its nuclease domain is PF13455 (Mug113), not PF01541; both belong to GIY-YIG clan CL0418 but are distinct Pfam families."
finding_id: "snipe_defense_system--a878d018"
result: "correction"
source: "snipe_defense_system"
quantities: []
caveat: "eggNOG Pfam annotations may miss divergent SNIPE homologues, and only 54/4,572 DUF4041 clusters show Mug113 co-annotation, suggesting many SNIPE nuclease domains go undetected."
first_added: "2026-11-09"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# SNIPE nuclease is Mug113 (PF13455), not canonical GIY-YIG PF01541

InterPro/UniProt analysis of the E. coli SNIPE protein (A0A0A1A5Z2) shows its nuclease domain is PF13455 (Mug113), not PF01541; both belong to GIY-YIG clan CL0418 but are distinct Pfam families. [src: snipe_defense_system]

## Evidence

> InterPro/UniProt analysis of the *E. coli* SNIPE protein ([A0A0A1A5Z2](https://www.uniprot.org/uniprotkb/A0A0A1A5Z2)) reveals why: the SNIPE nuclease domain is actually **PF13455** (Mug113, "Meiotically up-regulated gene 113"), not PF01541. Both PF13455 and PF01541 belong to the **GIY-YIG clan (CL0418)** — the paper describes the SNIPE nuclease as "GIY-YIG" at the superfamily level, but at the Pfam family level they are distinct entries. [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

eggNOG Pfam annotations may miss divergent SNIPE homologues, and only 54/4,572 DUF4041 clusters show Mug113 co-annotation, suggesting many SNIPE nuclease domains go undetected. [src: snipe_defense_system]

> - **Annotation sensitivity**: eggNOG Pfam annotations may miss divergent SNIPE homologues. The SNIPE nuclease domain is PF13455 (Mug113, GIY-YIG clan), not PF01541 (canonical GIY-YIG); only 54/4,572 DUF4041 clusters show Mug113 co-annotation, suggesting many SNIPE nuclease domains go undetected [src: snipe_defense_system]

## Other caveats in this report

- UniProt's fructose-specific ManX annotation conflicts with the reported Fitness Browser phenotypes. [src: snipe_defense_system]
- Fitness scores are log2 RB-TnSeq ratios; carbon-source conditions were selected by condition_1 and expGroup='carbon source'. [src: snipe_defense_system]
- The report proposes that SNIPE avoids the metabolic cost of man knockouts while blocking phage DNA; this passage does not present a direct comparative fitness measurement. [src: snipe_defense_system]
- Three Klebsiella DUF4041 proteins are 558 aa, matching E. coli SNIPE; their full two-domain architecture is inferred rather than directly confirmed here. [src: snipe_defense_system]
- The query footnote labels PF00358 as PTS_EIIC and PF02378 as PTS_EIID, conflicting with the report's table labels PF00358/PTS_EIIA_1 and PF02378/PTS_EIIC. [src: snipe_defense_system]
