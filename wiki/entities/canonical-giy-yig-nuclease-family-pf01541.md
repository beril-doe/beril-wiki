---
type: "Gene_Or_Pathway"
description: "Pfam PF01541 / IPR000305, a large nuclease family of restriction and DNA repair enzymes that is not the SNIPE nuclease."
sources: ["summaries/discoveries.md", "summaries/snipe_defense_system__REPORT.md"]
aliases: ["GIY-YIG", "IPR000305", "PF01541"]
---
# Canonical GIY-YIG nuclease family (PF01541)

The canonical GIY-YIG nuclease family is Pfam PF01541 (InterPro IPR000305), covering restriction enzymes and DNA repair proteins, and it is not the SNIPE nuclease. [src: snipe_defense_system]

## Key facts

- The family is Pfam PF01541 and InterPro IPR000305. It covers 68,148 proteins, including restriction enzymes and DNA repair proteins. [src: snipe_defense_system]
- The [[entities/snipe|SNIPE]] nuclease domain belongs to Pfam PF13455 (Mug113), not PF01541. Both families sit in the GIY-YIG clan CL0418 but are distinct families. [src: discoveries] See [[entities/mug113-nuclease-domain-pf13455]].
- The snipe_defense_system report queried PF01541 independently and found it was the wrong Pfam family for the SNIPE nuclease. [src: snipe_defense_system]
- The report identifies the 74,686 PF01541 clusters it found as non-SNIPE GIY-YIG family members: restriction enzymes, DNA repair enzymes and other family members. [src: snipe_defense_system]

## No co-occurrence with DUF4041

No gene clusters contained both DUF4041 and PF01541 in their eggNOG Pfam annotations. [src: snipe_defense_system] The snipe_defense_system report attributes the zero hits to genuinely different Pfam families, not to annotation artifacts. [src: snipe_defense_system] The discoveries digest makes the same attribution and calls it biological truth. [src: discoveries] The co-occurrence analysis found zero DUF4041+PF01541 overlaps. [src: snipe_defense_system] For the wider issue of domain-based detection, see [[concepts/domain-based-marker-detection-and-annotation-method-bias]].

## Outputs

The output `giy_yig_species.csv` lists 728 species with GIY-YIG, taken from a 1,000-cluster sample. [src: snipe_defense_system]

See also [[summaries/snipe_defense_system__REPORT]] and [[summaries/discoveries]].
