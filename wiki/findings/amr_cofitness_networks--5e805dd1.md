---
type: "Finding"
description: "GO:0071973, flagellum-dependent cell motility, is enriched in AMR support networks in 5 organisms (FDR<0.05), with mean OR 4.7."
finding_id: "amr_cofitness_networks--5e805dd1"
result: "observation"
source: "amr_cofitness_networks"
quantities: [{"value": "5", "what": "organisms with enrichment", "unit": "", "denominator": "", "scope": "FDR<0.05"}, {"value": "4.7", "what": "mean odds ratio", "unit": "", "denominator": "", "scope": ""}]
caveat: "This enrichment may reflect shared dispensability under lab conditions rather than genuine co-regulation."
first_added: "2026-11-24"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# Flagellar motility GO terms enriched in AMR support networks across organisms

GO:0071973, flagellum-dependent cell motility, is enriched in AMR support networks in 5 organisms (FDR<0.05), with mean OR 4.7. [src: amr_cofitness_networks]

## Key figures

- **5**: organisms with enrichment (scope FDR<0.05) [src: amr_cofitness_networks]
- **4.7**: mean odds ratio [src: amr_cofitness_networks]

## Evidence

> | GO Term | Description | Organisms (FDR<0.05) | Mean OR | |---------|-------------|---------------------|---------| | GO:0071973 | Flagellum-dependent cell motility | 5 | 4.7 | | GO:0044780 | Flagellum assembly | 5 | 5.3 | | GO:0009288 | Bacterial-type flagellum | 4 | 4.9 | | GO:0071978 | Flagellum-dependent swarming | 4 | 5.0 | | GO:0000105 | Histidine biosynthesis | 3 | 5.3 | | GO:0000162 | Tryptophan biosynthesis | 3 | 5.3 | [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

This enrichment may reflect shared dispensability under lab conditions rather than genuine co-regulation. [src: amr_cofitness_networks]

> **Important caveat:** This enrichment may reflect **shared dispensability under lab conditions** rather than genuine co-regulation. [src: amr_cofitness_networks]

## Other caveats in this report

- A fitness-matched permutation drawing random genes with the same slightly-positive fitness distribution is needed to distinguish genuine AMR co-regulation from shared dispensability. [src: amr_cofitness_networks]
- The report offers co-regulation and shared dispensability as competing interpretations of flagellar motility, chemotaxis, and amino acid biosynthesis enrichment in AMR support networks. [src: amr_cofitness_networks]
- The report's co-regulation interpretation hypothesizes that shared transcription factors or signaling cascades co-control resistance, motility, and biosynthesis, producing condition-specific cofitness. [src: amr_cofitness_networks]
- The report's shared-dispensability interpretation proposes that AMR, flagellar, and biosynthetic genes are metabolic burdens under standard laboratory conditions and yield modestly positive knockout fitness across most experiments. [src: amr_cofitness_networks]
- The shared-dispensability interpretation proposes that AMR cofitness reflects membership in a laboratory-dispensable gene class rather than a mechanistic connection. [src: amr_cofitness_networks]
