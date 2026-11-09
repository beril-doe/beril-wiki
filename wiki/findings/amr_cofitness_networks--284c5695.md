---
type: "Finding"
description: "Flagellum-dependent cell motility (GO:0071973) was enriched in 5 organisms, with mean odds ratio 4.7."
finding_id: "amr_cofitness_networks--284c5695"
result: "observation"
source: "amr_cofitness_networks"
quantities: [{"value": "5", "what": "organisms with GO:0071973 enrichment", "unit": "organisms", "denominator": "", "scope": ""}, {"value": "4.7", "what": "mean odds ratio for flagellum-dependent cell motility", "unit": "", "denominator": "", "scope": ""}]
caveat: "The permutation matched random genes by conservation class but not by mean fitness level, so the flagellar enrichment might disappear if fitness-matched genes were drawn."
first_added: "2026-11-09"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# Flagellum-dependent motility GO term enriched across several organisms

Flagellum-dependent cell motility (GO:0071973) was enriched in 5 organisms, with mean odds ratio 4.7. [src: amr_cofitness_networks]

## Key figures

- **5 organisms**: organisms with GO:0071973 enrichment [src: amr_cofitness_networks]
- **4.7**: mean odds ratio for flagellum-dependent cell motility [src: amr_cofitness_networks]

## Evidence

> | GO:0071973 | Flagellum-dependent cell motility | 5 | 4.7 | [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

The permutation matched random genes by conservation class but not by mean fitness level, so the flagellar enrichment might disappear if fitness-matched genes were drawn. [src: amr_cofitness_networks]

> - The permutation test matched random genes by conservation class but **not by mean fitness level**. If we had drawn random genes with the same slightly-positive fitness distribution as AMR genes, the flagellar enrichment might disappear entirely [src: amr_cofitness_networks]

## Other caveats in this report

- Flagellar and biosynthesis enrichment may reflect shared dispensability in shaken liquid culture and supplemented media rather than co-regulation; the report calls for a fitness-matched permutation. [src: amr_cofitness_networks]
- Histidine biosynthesis occurred with efflux in 68% versus metal resistance in 30% of organisms, but p = 0.013 was uncorrected and q = 0.18 after FDR. [src: amr_cofitness_networks]
- Old KEGG analysis reported two FDR-significant mechanism-specific terms (lipoprotein and toluene tolerance), whereas InterProScan GO reported zero. [src: amr_cofitness_networks]
- Pearson correlation removes uniform mean-fitness differences, but condition-specific covariation among dispensable genes can still mimic co-regulation. [src: amr_cofitness_networks]
- The proposed discriminator is a non-AMR permutation matched to mean fitness −0.05 to +0.05: similar flagellar enrichment in controls would support shared dispensability, whereas AMR-specific enrichment would support co-regulation. [src: amr_cofitness_networks]
