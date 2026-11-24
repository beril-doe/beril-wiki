---
type: "Finding"
description: "There is no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = \u22120.006, p = 0.87, N = 769)."
finding_id: "amr_cofitness_networks--ca058750"
result: "null result"
source: "amr_cofitness_networks"
quantities: [{"value": "\u22120.006", "what": "Spearman rho", "unit": "", "denominator": "", "scope": ""}, {"value": "0.87", "what": "p-value", "unit": "", "denominator": "", "scope": ""}, {"value": "769", "what": "AMR genes", "unit": "", "denominator": "", "scope": ""}]
caveat: "At |r| > 0.3, mean network size is 233 genes, which includes many weak associations, so confirmation at |r| > 0.4 is needed."
first_added: "2026-11-24"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# Support-network size does not track AMR gene fitness cost

There is no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks]

## Key figures

- **−0.006**: Spearman rho [src: amr_cofitness_networks]
- **0.87**: p-value [src: amr_cofitness_networks]
- **769**: AMR genes [src: amr_cofitness_networks]

## Evidence

> There is no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

At |r| > 0.3, mean network size is 233 genes, which includes many weak associations, so confirmation at |r| > 0.4 is needed. [src: amr_cofitness_networks]

> At |r| > 0.3, mean network size is 233 genes (large). This includes many weak associations. Confirmation at |r| > 0.4 is needed. [src: amr_cofitness_networks]

## Other caveats in this report

- AMR cofitness enrichment may reflect shared dispensability under laboratory conditions rather than genuine co-regulation. [src: amr_cofitness_networks]
- A fitness-matched permutation drawing random genes with the same slightly-positive fitness distribution is needed to distinguish genuine AMR co-regulation from shared dispensability. [src: amr_cofitness_networks]
- The report offers co-regulation and shared dispensability as competing interpretations of flagellar motility, chemotaxis, and amino acid biosynthesis enrichment in AMR support networks. [src: amr_cofitness_networks]
- The report's co-regulation interpretation hypothesizes that shared transcription factors or signaling cascades co-control resistance, motility, and biosynthesis, producing condition-specific cofitness. [src: amr_cofitness_networks]
- The report's shared-dispensability interpretation proposes that AMR, flagellar, and biosynthetic genes are metabolic burdens under standard laboratory conditions and yield modestly positive knockout fitness across most experiments. [src: amr_cofitness_networks]
