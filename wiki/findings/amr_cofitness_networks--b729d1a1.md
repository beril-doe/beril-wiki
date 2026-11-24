---
type: "Finding"
description: "AMR-containing ICA fitness modules have median 46 vs 27 genes in non-AMR modules (MWU p = 1.7\u00d710\u207b\u2078)."
finding_id: "amr_cofitness_networks--b729d1a1"
result: "observation"
source: "amr_cofitness_networks"
quantities: [{"value": "46", "what": "median genes in AMR modules", "unit": "", "denominator": "", "scope": ""}, {"value": "27", "what": "median genes in non-AMR modules", "unit": "", "denominator": "", "scope": ""}, {"value": "1.7\u00d710\u207b\u2078", "what": "MWU p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation."
first_added: "2026-11-24"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# AMR-containing ICA modules are larger than non-AMR modules

AMR-containing ICA fitness modules have median 46 vs 27 genes in non-AMR modules (MWU p = 1.7×10⁻⁸). [src: amr_cofitness_networks]

## Key figures

- **46**: median genes in AMR modules [src: amr_cofitness_networks]
- **27**: median genes in non-AMR modules [src: amr_cofitness_networks]
- **1.7×10⁻⁸**: MWU p-value [src: amr_cofitness_networks]

## Evidence

> Only 24% of AMR genes (192/801) are assigned to ICA fitness modules, but the modules they inhabit are significantly larger than non-AMR modules: median 46 vs 27 genes (MWU p = 1.7×10⁻⁸). [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation. [src: amr_cofitness_networks]

> Even without the dispensability confound, high cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation. [src: amr_cofitness_networks]

## Other caveats in this report

- AMR cofitness enrichment may reflect shared dispensability under laboratory conditions rather than genuine co-regulation. [src: amr_cofitness_networks]
- A fitness-matched permutation drawing random genes with the same slightly-positive fitness distribution is needed to distinguish genuine AMR co-regulation from shared dispensability. [src: amr_cofitness_networks]
- The report offers co-regulation and shared dispensability as competing interpretations of flagellar motility, chemotaxis, and amino acid biosynthesis enrichment in AMR support networks. [src: amr_cofitness_networks]
- The report's co-regulation interpretation hypothesizes that shared transcription factors or signaling cascades co-control resistance, motility, and biosynthesis, producing condition-specific cofitness. [src: amr_cofitness_networks]
- The report's shared-dispensability interpretation proposes that AMR, flagellar, and biosynthetic genes are metabolic burdens under standard laboratory conditions and yield modestly positive knockout fitness across most experiments. [src: amr_cofitness_networks]
