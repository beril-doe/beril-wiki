---
type: "Finding"
description: "In E. coli K-12 (Keio collection) Fitness Browser RB-TnSeq data, across 168 experiments per gene, worst fitness was -3.93 for manX, -3.82 for manY and -4.14 for manZ, with 4 conditions below -2 for each gene."
finding_id: "snipe_defense_system--69396dc3"
result: "observation"
source: "snipe_defense_system"
quantities: [{"value": "-3.93", "what": "worst fitness for manX", "unit": "log2 ratio", "denominator": "168 experiments", "scope": "E. coli K-12, Fitness Browser"}, {"value": "-3.82", "what": "worst fitness for manY", "unit": "log2 ratio", "denominator": "168 experiments", "scope": "E. coli K-12, Fitness Browser"}, {"value": "-4.14", "what": "worst fitness for manZ", "unit": "log2 ratio", "denominator": "168 experiments", "scope": "E. coli K-12, Fitness Browser"}, {"value": "4", "what": "conditions with fitness < -2 for each of manX, manY, manZ", "unit": "conditions", "denominator": "168 experiments", "scope": "E. coli K-12, Fitness Browser"}]
caveat: "Among the 48 Fitness Browser organisms ManXYZ by gene name is present only in E. coli K-12, and no Klebsiella strain carries it by gene name."
first_added: "2026-11-09"
source_hash: "f7d78af3b2d5fc355bdd55bc72ce728519a3dc854968793d401b959f1e9ae555"
---
# E. coli K-12 ManXYZ genes show severe fitness defects in few conditions

In E. coli K-12 (Keio collection) Fitness Browser RB-TnSeq data, across 168 experiments per gene, worst fitness was -3.93 for manX, -3.82 for manY and -4.14 for manZ, with 4 conditions below -2 for each gene. [src: snipe_defense_system]

## Key figures

- **-3.93 log2 ratio**: worst fitness for manX (denominator 168 experiments; scope E. coli K-12, Fitness Browser) [src: snipe_defense_system]
- **-3.82 log2 ratio**: worst fitness for manY (denominator 168 experiments; scope E. coli K-12, Fitness Browser) [src: snipe_defense_system]
- **-4.14 log2 ratio**: worst fitness for manZ (denominator 168 experiments; scope E. coli K-12, Fitness Browser) [src: snipe_defense_system]
- **4 conditions**: conditions with fitness < -2 for each of manX, manY, manZ (denominator 168 experiments; scope E. coli K-12, Fitness Browser) [src: snipe_defense_system]

## Evidence

> | Gene | Experiments | Worst fitness | Avg fitness | Conditions with fit < -1 | Conditions with fit < -2 | |------|------------|--------------|-------------|--------------------------|--------------------------| | *manX* | 168 | **-3.93** | -0.249 | 6 | 4 | | *manY* | 168 | **-3.82** | -0.171 | 10 | 4 | | *manZ* | 168 | **-4.14** | -0.082 | 7 | 4 | [src: snipe_defense_system]

From the report [[summaries/snipe_defense_system__REPORT]].

## Caveat

Among the 48 Fitness Browser organisms ManXYZ by gene name is present only in E. coli K-12, and no Klebsiella strain carries it by gene name. [src: snipe_defense_system]

> **ManXYZ**: Present only in *E. coli* K-12 (Keio collection) among the 48 Fitness Browser organisms. Full fitness data for 168 conditions is presented above. No *Klebsiella* strain in the Fitness Browser carries ManXYZ by gene name. [src: snipe_defense_system]

## Other caveats in this report

- UniProt's fructose-specific ManX annotation conflicts with the reported Fitness Browser phenotypes. [src: snipe_defense_system]
- Fitness scores are log2 RB-TnSeq ratios; carbon-source conditions were selected by condition_1 and expGroup='carbon source'. [src: snipe_defense_system]
- The report proposes that SNIPE avoids the metabolic cost of man knockouts while blocking phage DNA; this passage does not present a direct comparative fitness measurement. [src: snipe_defense_system]
- Three Klebsiella DUF4041 proteins are 558 aa, matching E. coli SNIPE; their full two-domain architecture is inferred rather than directly confirmed here. [src: snipe_defense_system]
- The query footnote labels PF00358 as PTS_EIIC and PF02378 as PTS_EIID, conflicting with the report's table labels PF00358/PTS_EIIA_1 and PF02378/PTS_EIIC. [src: snipe_defense_system]
