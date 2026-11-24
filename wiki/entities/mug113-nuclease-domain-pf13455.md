---
type: "Gene_Or_Pathway"
description: "Pfam PF13455, the SNIPE nuclease domain in GIY-YIG clan CL0418 but distinct from the canonical GIY-YIG family."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["Meiotically up-regulated gene 113", "PF13455"]
---
# Mug113 nuclease domain (PF13455)

Pfam PF13455, the SNIPE nuclease domain in GIY-YIG clan CL0418 but distinct from the canonical GIY-YIG family.

## Key facts

- The SNIPE nuclease domain belongs to PF13455 (Mug113), not PF01541. Both families are in clan CL0418. [src: discoveries, snipe_defense_system]
- InterPro/UniProt analysis of the E. coli SNIPE protein A0A0A1A5Z2 places PF13455 at positions 443–520, labelled as the nuclease. [src: discoveries, snipe_defense_system]
- The same analysis found PF13250 at positions 232–333. [src: discoveries]
- The SNIPE paper calls the nuclease "GIY-YIG" at the superfamily level and never cites Pfam accessions. [src: discoveries]
- Because both families share the clan, the paper's superfamily-level description fits, but at the Pfam family level they are distinct entries. [src: snipe_defense_system]

## Consequences for annotation

No gene clusters show DUF4041 together with PF01541. The report attributes this to the distinct family identity of the nuclease, not to an annotation artifact. [src: discoveries] See [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

Among 4,572 DUF4041 clusters, 54 carry the description "Meiotically up-regulated gene 113". This is consistent with full-length SNIPE proteins annotated with both domains. [src: snipe_defense_system] The report suggests that many SNIPE nuclease domains go undetected, since only 54 of 4,572 show this co-annotation. [src: snipe_defense_system]

## Fitness Browser occurrence

Among 48 Fitness Browser organisms, 7 genes carry PF13455. They fall in 6 organisms: Azospirillum brasilense, Bacteroides thetaiotaomicron, Cupriavidus, Desulfovibrio vulgaris, Paraburkholderia kururiensis and M. maripaludis. [src: snipe_defense_system] For coverage context, see [[concepts/fitness-data-coverage-gaps-for-defense-genes]].
