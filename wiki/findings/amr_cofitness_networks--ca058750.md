---
type: "Finding"
description: "There was no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = \u22120.006, p = 0.87, N = 769)."
finding_id: "amr_cofitness_networks--ca058750"
result: "null result"
source: "amr_cofitness_networks"
quantities: [{"value": "\u22120.006", "what": "Spearman rho between support-network size and fitness cost", "unit": "", "denominator": "N = 769", "scope": "AMR genes"}, {"value": "0.87", "what": "p-value", "unit": "", "denominator": "", "scope": ""}]
caveat: "The absence of a network-size\u2013cost correlation may reflect insufficient variance in fitness cost across genes."
first_added: "2026-11-09"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# Support-network size does not predict AMR gene fitness cost

There was no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks]

## Key figures

- **−0.006**: Spearman rho between support-network size and fitness cost (denominator N = 769; scope AMR genes) [src: amr_cofitness_networks]
- **0.87**: p-value [src: amr_cofitness_networks]

## Evidence

> There is no correlation between cofitness support network size and AMR gene fitness cost (Spearman rho = −0.006, p = 0.87, N = 769). [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

The absence of a network-size–cost correlation may reflect insufficient variance in fitness cost across genes. [src: amr_cofitness_networks]

> 5. **H3 null result**: The absence of a network-size-cost correlation may reflect insufficient variance in fitness cost across genes. [src: amr_cofitness_networks]

## Other caveats in this report

- Flagellar and biosynthesis enrichment may reflect shared dispensability in shaken liquid culture and supplemented media rather than co-regulation; the report calls for a fitness-matched permutation. [src: amr_cofitness_networks]
- Histidine biosynthesis occurred with efflux in 68% versus metal resistance in 30% of organisms, but p = 0.013 was uncorrected and q = 0.18 after FDR. [src: amr_cofitness_networks]
- Old KEGG analysis reported two FDR-significant mechanism-specific terms (lipoprotein and toluene tolerance), whereas InterProScan GO reported zero. [src: amr_cofitness_networks]
- The permutation matched conservation class but not mean fitness, leaving open whether fitness matching would eliminate the flagellar signal. [src: amr_cofitness_networks]
- Pearson correlation removes uniform mean-fitness differences, but condition-specific covariation among dispensable genes can still mimic co-regulation. [src: amr_cofitness_networks]
