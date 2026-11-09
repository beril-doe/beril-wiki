---
type: "Finding"
description: "The report states that 99% (208/209) of AMR gene-module assignments are in cross-organism conserved module families, and interprets this as indicating ancient regulatory relationships."
finding_id: "amr_cofitness_networks--8fa18a88"
result: "inference"
source: "amr_cofitness_networks"
quantities: [{"value": "99%", "what": "AMR gene-module assignments in cross-organism conserved module families", "unit": "%", "denominator": "209 AMR gene-module assignments", "scope": ""}, {"value": "208/209", "what": "assignments in conserved module families", "unit": "", "denominator": "209", "scope": ""}]
caveat: "High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation, so the 'ancient regulatory relationships' reading is interpretive."
first_added: "2026-11-09"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# AMR gene-module assignments fall almost entirely in conserved module families

The report states that 99% (208/209) of AMR gene-module assignments are in cross-organism conserved module families, and interprets this as indicating ancient regulatory relationships. [src: amr_cofitness_networks]

## Key figures

- **99%**: AMR gene-module assignments in cross-organism conserved module families (denominator 209 AMR gene-module assignments) [src: amr_cofitness_networks]
- **208/209**: assignments in conserved module families (denominator 209) [src: amr_cofitness_networks]

## Evidence

> Notably, 99% (208/209) of AMR gene-module assignments are in cross-organism conserved module families, indicating these are ancient regulatory relationships. [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

High cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation, so the 'ancient regulatory relationships' reading is interpretive. [src: amr_cofitness_networks]

> 2. **Cofitness ≠ co-regulation**: Even without the dispensability confound, high cofitness implies shared fitness phenotypes, not direct transcriptional co-regulation. Additionally, the cofitness computation treats missing fitness values as zero in z-score space (via `np.nan_to_num`), which approximates but does not equal pairwise-complete Pearson correlation. For the relatively dense FB matrices this is unlikely to affect conclusions. [src: amr_cofitness_networks]

## Other caveats in this report

- Flagellar and biosynthesis enrichment may reflect shared dispensability in shaken liquid culture and supplemented media rather than co-regulation; the report calls for a fitness-matched permutation. [src: amr_cofitness_networks]
- Histidine biosynthesis occurred with efflux in 68% versus metal resistance in 30% of organisms, but p = 0.013 was uncorrected and q = 0.18 after FDR. [src: amr_cofitness_networks]
- Old KEGG analysis reported two FDR-significant mechanism-specific terms (lipoprotein and toluene tolerance), whereas InterProScan GO reported zero. [src: amr_cofitness_networks]
- The permutation matched conservation class but not mean fitness, leaving open whether fitness matching would eliminate the flagellar signal. [src: amr_cofitness_networks]
- Pearson correlation removes uniform mean-fitness differences, but condition-specific covariation among dispensable genes can still mimic co-regulation. [src: amr_cofitness_networks]
