---
type: "Finding"
description: "Using InterProScan GO annotations (68% gene coverage, reported as 3.6\u00d7 better than old SEED annotations), the report detects significant functional enrichment in AMR cofitness neighborhoods, with the top 6 GO terms enriched in \u22653 organisms at FDR < 0.05."
finding_id: "amr_cofitness_networks--9d334076"
result: "observation"
source: "amr_cofitness_networks"
quantities: [{"value": "68%", "what": "InterProScan GO gene coverage", "unit": "%", "denominator": "", "scope": ""}, {"value": "3.6\u00d7", "what": "coverage improvement reported over old SEED annotations", "unit": "", "denominator": "", "scope": ""}, {"value": "6", "what": "top GO terms enriched in AMR cofitness neighborhoods", "unit": "GO terms", "denominator": "", "scope": "enriched in \u22653 organisms, FDR < 0.05"}]
caveat: "The flagellar and biosynthesis enrichment may reflect shared dispensability under lab conditions (shaken liquid culture, supplemented media) rather than genuine co-regulation, and a fitness-matched permutation is needed to distinguish them."
first_added: "2026-11-09"
source_hash: "aff57c75024bdd9b12de29d4d39e499b07d78769cef6d0bd2d1a1161e467e9cd"
---
# InterProScan GO annotations reveal AMR cofitness enrichment across organisms

Using InterProScan GO annotations (68% gene coverage, reported as 3.6× better than old SEED annotations), the report detects significant functional enrichment in AMR cofitness neighborhoods, with the top 6 GO terms enriched in ≥3 organisms at FDR < 0.05. [src: amr_cofitness_networks]

## Key figures

- **68%**: InterProScan GO gene coverage [src: amr_cofitness_networks]
- **3.6×**: coverage improvement reported over old SEED annotations [src: amr_cofitness_networks]
- **6 GO terms**: top GO terms enriched in AMR cofitness neighborhoods (scope enriched in ≥3 organisms, FDR < 0.05) [src: amr_cofitness_networks]

## Evidence

> Using InterProScan GO annotations (68% gene coverage — 3.6× better than old SEED annotations), we detect significant functional enrichment in AMR cofitness neighborhoods. The top 6 GO terms enriched in ≥3 organisms (FDR < 0.05) are: [src: amr_cofitness_networks]

From the report [[summaries/amr_cofitness_networks__REPORT]].

## Caveat

The flagellar and biosynthesis enrichment may reflect shared dispensability under lab conditions (shaken liquid culture, supplemented media) rather than genuine co-regulation, and a fitness-matched permutation is needed to distinguish them. [src: amr_cofitness_networks]

> **Important caveat:** This enrichment may reflect **shared dispensability under lab conditions** rather than genuine co-regulation. FB experiments use shaken liquid culture (where flagella are useless) and often supplemented media (where biosynthesis is redundant). AMR genes, flagellar genes, and biosynthesis genes are all metabolic burdens under these conditions. A fitness-matched permutation (drawing random genes with the same slightly-positive fitness distribution) is needed to distinguish true co-regulation from shared dispensability — see Interpretation section for full discussion. [src: amr_cofitness_networks]

## Other caveats in this report

- Histidine biosynthesis occurred with efflux in 68% versus metal resistance in 30% of organisms, but p = 0.013 was uncorrected and q = 0.18 after FDR. [src: amr_cofitness_networks]
- Old KEGG analysis reported two FDR-significant mechanism-specific terms (lipoprotein and toluene tolerance), whereas InterProScan GO reported zero. [src: amr_cofitness_networks]
- The permutation matched conservation class but not mean fitness, leaving open whether fitness matching would eliminate the flagellar signal. [src: amr_cofitness_networks]
- Pearson correlation removes uniform mean-fitness differences, but condition-specific covariation among dispensable genes can still mimic co-regulation. [src: amr_cofitness_networks]
- The proposed discriminator is a non-AMR permutation matched to mean fitness −0.05 to +0.05: similar flagellar enrichment in controls would support shared dispensability, whereas AMR-specific enrichment would support co-regulation. [src: amr_cofitness_networks]
