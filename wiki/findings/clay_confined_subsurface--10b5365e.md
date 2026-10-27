---
type: "Finding"
description: "Under the CheckM\u226580 filter, the 6 deep anchors had lower mean GapMind pathway completeness than 137 baseline genomes: 15.50 versus 17.14 (Cohen's d=\u22120.84, p=0.009)."
finding_id: "clay_confined_subsurface--10b5365e"
result: "observation"
source: "clay_confined_subsurface"
quantities: [{"value": "15.50", "what": "mean pathway completeness, deep anchors", "unit": "", "denominator": "6 genomes", "scope": "CheckM\u226580"}, {"value": "17.14", "what": "mean pathway completeness, baseline", "unit": "", "denominator": "137 genomes", "scope": "CheckM\u226580"}, {"value": "\u22120.84", "what": "Cohen's d, deep anchors versus baseline", "unit": "", "denominator": "", "scope": "CheckM\u226580"}, {"value": "0.009", "what": "p-value for the comparison", "unit": "", "denominator": "", "scope": "CheckM\u226580"}]
caveat: "The 18-pathway GapMind measure has a ceiling: most cultured organisms score 17\u201318/18 regardless of habitat, limiting detection of differences at the upper end."
first_added: "2026-10-27"
source_hash: "93b0616d8ca5b3e28c3abd934fdaf5a1c4aa678b99ef85f1baeb9f9c637b0c2c"
---
# Quality-filtered deep-clay genomes show lower amino-acid pathway completeness than soil baseline

Under the CheckM≥80 filter, the 6 deep anchors had lower mean GapMind pathway completeness than 137 baseline genomes: 15.50 versus 17.14 (Cohen's d=−0.84, p=0.009). [src: clay_confined_subsurface]

## Key figures

- **15.50**: mean pathway completeness, deep anchors (denominator 6 genomes; scope CheckM≥80) [src: clay_confined_subsurface]
- **17.14**: mean pathway completeness, baseline (denominator 137 genomes; scope CheckM≥80) [src: clay_confined_subsurface]
- **−0.84**: Cohen's d, deep anchors versus baseline (scope CheckM≥80) [src: clay_confined_subsurface]
- **0.009**: p-value for the comparison (scope CheckM≥80) [src: clay_confined_subsurface]

## Evidence

> | anchor_deep vs baseline | CheckM≥80 | 6 | 137 | 15.50 | 17.14 | −0.84 | 0.009 | [src: clay_confined_subsurface]

From the report [[summaries/clay_confined_subsurface__REPORT]].

## Caveat

The 18-pathway GapMind measure has a ceiling: most cultured organisms score 17–18/18 regardless of habitat, limiting detection of differences at the upper end. [src: clay_confined_subsurface]

> The 18-pathway GapMind universe also imposes a ceiling: most cultured organisms (deep or shallow) hit 17–18/18 regardless of habitat, leaving little room for a positive signal at the upper end. [src: clay_confined_subsurface]

## Other caveats in this report

- The original iron-reduction comparison used unrelated KOs, invalidating its 1/9 versus 15/30 contrast. [src: clay_confined_subsurface]
- The cited outer-surface cytochromes lacked canonical KEGG KOs, and the original analysis substituted unrelated genes. [src: clay_confined_subsurface]
- The report withdraws its iron-reduction-based account of a shallow-clay, rock-attached pattern. [src: clay_confined_subsurface]
- The porewater-bias interpretation is supported by sulfate-reduction evidence only; its iron-reduction side is unsupported. [src: clay_confined_subsurface]
- The report identifies a broader risk of silent functional substitution when KEGG-based mining targets niche genes without canonical KOs. [src: clay_confined_subsurface]
