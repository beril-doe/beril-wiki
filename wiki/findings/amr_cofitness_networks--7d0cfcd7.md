---
type: "Finding"
description: "Different AMR mechanisms within the same organism share more support-network partners (J = 0.375) than the same mechanism across organisms (J = 0.207, p = 4.3\u00d710\u207b\u00b9\u00b3), which the report regards as robust to the dispensability confound."
finding_id: "amr_cofitness_networks--7d0cfcd7"
result: "observation"
source: "amr_cofitness_networks"
quantities: [{"value": "0.375", "what": "mean GO Jaccard between different AMR mechanisms in the same organism", "unit": "", "denominator": "", "scope": ""}, {"value": "0.207", "what": "mean GO Jaccard for the same mechanism across organisms", "unit": "", "denominator": "", "scope": ""}, {"value": "4.3\u00d710\u207b\u00b9\u00b3", "what": "MWU p-value for the difference", "unit": "", "denominator": "", "scope": ""}]
caveat: "High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation."
first_added: "2026-11-24"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# Organism identity shapes AMR support networks more than resistance mechanism

Different AMR mechanisms within the same organism share more support-network partners (J = 0.375) than the same mechanism across organisms (J = 0.207, p = 4.3×10⁻¹³), which the report regards as robust to the dispensability confound. [src: amr_cofitness_networks]

## Key figures

- **0.375**: mean GO Jaccard between different AMR mechanisms in the same organism [src: amr_cofitness_networks]
- **0.207**: mean GO Jaccard for the same mechanism across organisms [src: amr_cofitness_networks]
- **4.3×10⁻¹³**: MWU p-value for the difference [src: amr_cofitness_networks]

## Evidence

> The organism-specificity finding is **robust to the dispensability confound**: regardless of why AMR genes correlate with their partners, the fact that different AMR mechanisms within the same organism share more partners (J = 0.375) than the same mechanism across organisms (J = 0.207, p = 4.3×10⁻¹³) reveals that each organism has its own characteristic set of dispensable/co-varying genes. [src: amr_cofitness_networks]

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
